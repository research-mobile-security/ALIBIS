#!/usr/bin/env python3
import pandas as pd
import os
import subprocess
from datetime import datetime, timedelta
from confluent_kafka import Producer

# Function to calculate timeout based on file size
def calculate_timeout(file_size):
    if file_size < 10000000:
        return 600  # 10 minutes
    elif 10000000 <= file_size < 20000000:
        return 1200  # 20 minutes
    elif 20000000 <= file_size < 50000000:
        return 1800  # 30 minutes
    elif 50000000 <= file_size < 70000000:
        return 2400  # 40 minutes
    elif 70000000 <= file_size < 100000000:
        return 3600  # 60 minutes
    elif 100000000 <= file_size < 120000000:
        return 5400  # 90 minutes
    else:
        return 7200  # 120 minutes

# Function to update CSV file with result
def update_csv(csv_path, apk_name, result):
    df = pd.read_csv(csv_path)
    df.loc[df['apk_name'] == apk_name, ['decompile_jar', 'decompile_java']] = [result, result]
    df.to_csv(csv_path, index=False)

# Function to execute command with timeout
def run_command(command, timeout):
    try:
        subprocess.run(command, timeout=timeout, check=True, shell=True)
        return True
    except subprocess.TimeoutExpired:
        return False
    except subprocess.CalledProcessError:
        return False

# Function to produce Kafka message
def produce_kafka_message(producer, message):
    producer.produce("decompile-log", value=message)
    producer.flush()

# Main script
csv_path = '/root/decompile/decompile.csv'
log_path = '/root/decompile/decompile-apk.log'
kafka_broker = '192.168.1.15:29093'

df = pd.read_csv(csv_path)

# Kafka producer configuration
producer_conf = {'bootstrap.servers': kafka_broker}
producer = Producer(producer_conf)

for index, row in df.iterrows():
    apk_name = row['apk_name']
    apk_path = f'/root/decompile/apk/{apk_name}.apk'

    if os.path.exists(apk_path):
        file_size = os.path.getsize(apk_path)
        timeout_value = calculate_timeout(file_size)

        command1 = f'timeout {timeout_value} sh /root/apk-tool/dex2jar/dex-tools/build/distributions/dex-tools-2.x/d2j-dex2jar.sh "{apk_name}.apk" -o "/root/decompile/java/{apk_name}.jar"'
        command2 = f'timeout {timeout_value} java -jar /root/apk-tool/procyon-decompiler-0.6.0.jar "/root/decompile/java/{apk_name}.jar" -o "/root/decompile/java/{apk_name}-java"'

        command = f'{command1} 2>&1 | tee -a {log_path} && {command2} 2>&1 | tee -a {log_path}'

        produce_kafka_message(producer, f"Start decompile file {apk_name}")

        if run_command(command, timeout_value):
            update_csv(csv_path, apk_name, 'DONE')
            os.remove(f'/root/decompile/java/{apk_name}.jar')
            produce_kafka_message(producer, f"Finish decompile file {apk_name}")
        else:
            update_csv(csv_path, apk_name, 'TIMEOUT')
            produce_kafka_message(producer, f"Timeout decompile file {apk_name}")
    else:
        print(f"APK file not found for {apk_name}")
        produce_kafka_message(producer, f"APK file not found for {apk_name}")

# Close Kafka producer
#producer.close()

print("Script execution complete.")
