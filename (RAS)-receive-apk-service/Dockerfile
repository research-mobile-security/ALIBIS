# Use Ubuntu 22.04 as the build stage
FROM ubuntu:22.04 AS build

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip nano net-tools tree && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy your application files
COPY server.py .
COPY upload_pb2.py .
COPY upload_pb2_grpc.py .
COPY upload.proto .

# Install required Python packages
RUN pip3 install grpcio grpcio-tools pandas

# Use a lightweight image for the final stage
FROM python:3.10-slim

WORKDIR /app

# Copy only the necessary files from the build stage
COPY --from=build /app /app

# Install dependencies in the final stage
RUN pip install grpcio grpcio-tools pandas

# Expose the port used by the server
EXPOSE 50051

# Command to run your application
CMD ["python", "server.py"]
