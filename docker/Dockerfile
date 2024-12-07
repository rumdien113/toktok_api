FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
gcc \
libpq-dev \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

ADD ../requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

ADD docker/exec.sh /app/docker/exec.sh
RUN chmod +x /app/docker/exec.sh
COPY src /app/src

EXPOSE 8070

ENV PYTHONPATH=/app:/app/src
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD ["bash", "/app/docker/exec.sh"]
