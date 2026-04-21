# Use the official Python runtime as the base image
FROM python:3.12-slim

# Set working directory in container
WORKDIR /app

# Install system dependencies (if needed for audio processing)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml uv.lock* ./
COPY bird_audio_xeno_canto/ ./bird_audio_xeno_canto/
COPY apps/ ./apps/
COPY data/ ./data/

# Install Python dependencies
RUN pip install --no-cache-dir -e .

# Create non-root user for security
RUN useradd -m -u 1000 appuser

# Create Streamlit config directory with proper permissions
RUN mkdir -p /home/appuser/.streamlit && \
    chown -R appuser:appuser /app /home/appuser/.streamlit

# Copy Streamlit config
COPY .streamlit/config.toml /home/appuser/.streamlit/config.toml
RUN chown appuser:appuser /home/appuser/.streamlit/config.toml

# Switch to non-root user
USER appuser

# Expose Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "apps/streamlit_app.py"]