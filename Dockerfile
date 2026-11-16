
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ingestion application
COPY ingestion/ ./ingestion/

# Run the ingestion pipeline
CMD ["python", "-m", "ingestion.main"]
