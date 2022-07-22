FROM python:3.10.4-slim-buster

# Fix known security vulnerabilities in the base python image from dockerhub
RUN apt-get update && apt-get upgrade -y

# Copy across a local python wheel (can add any dependencies if required)
COPY dist dist

RUN pip install ./dist/data_manipulator-0.1.0.tar.gz --no-cache-dir

CMD ["python", "-m", "data_manipulator"]
