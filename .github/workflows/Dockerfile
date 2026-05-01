# Use lightweight Python
FROM python:3.9-slim

# Workdir
WORKDIR /app

# Copy only requirements first (better caching)
COPY requirements.txt .

# Install deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the code
COPY . .

# Expose Flask port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]