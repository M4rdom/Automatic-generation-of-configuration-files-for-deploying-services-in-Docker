# Python Aplication Dockerfile
# Fask Aplication Dockerfile

FROM python:3.13.0-alpine3.20

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app
# Install the application dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --no-cache-dir -r requirements.txt


# Install Gunicorn This is not recommended for production, requirements.txt should be used instead

RUN pip install --no-cache-dir gunicorn==23.0.0

# Run the application using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5001", "app:app"]

# Make port 5001 available to the world outside this container
EXPOSE 5001
