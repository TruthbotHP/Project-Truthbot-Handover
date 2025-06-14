# TruthBot V7.1 Docker Deployment
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy entire application
COPY . .

# Expose port for API or web interface (optional)
EXPOSE 8501

# Run CLI or API (adjustable as needed)
CMD ["python", "ui/gui_panel.py"]