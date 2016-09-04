FROM alpine:latest

RUN apk update && \
    apk add --no-cache python

# Add app files
COPY . /app
WORKDIR /app

RUN apk add --no-cache py-pip && \

    # Install Fluent logger
    pip install fluent-logger && \

    # Remove Pip
    apk del py-pip && \
    rm -rf /var/cache/apk/*

CMD python logger.py
