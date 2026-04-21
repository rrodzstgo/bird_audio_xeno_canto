# Use the official Python runtime as the base image
FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Install system dependencies (if needed for audio processing)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml uv.lock* .
COPY bird_audio_xeno_canto/ ./bird_audio_xeno_canto/
COPY apps/ ./apps/
COPY data/ ./data/

# Install Python dependencies
RUN pip install --no-cache-dir -e .

# Create .streamlit directory
RUN mkdir -p /root/.streamlit

# Copy Streamlit config (we'll create this next)
COPY .streamlit/config.toml /root/.streamlit/config.toml

# Expose Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "apps/streamlit_app.py"]