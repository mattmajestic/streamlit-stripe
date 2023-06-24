# Use the official Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files into the container
COPY . .

# Expose the port for the Streamlit app
EXPOSE 8501

# Set the command to run the Streamlit app
CMD ["streamlit", "run", "--server.enableCORS", "false", "streamlit_app.py"]