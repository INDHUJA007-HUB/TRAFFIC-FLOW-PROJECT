# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy only necessary files first to optimize caching
COPY requirements.txt ./

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the remaining project files
COPY . .

# Set environment variables for clean execution
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8

# Expose Streamlit port
EXPOSE 8501

# Define entrypoint properly
ENTRYPOINT ["python", "-m", "streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]