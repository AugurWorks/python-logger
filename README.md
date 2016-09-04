# Python Logger
**Python Logger** is a very light-weight Fluent logger wrapped in a Docker container for easy use in a Dockerized environment.

## Use
An example Docker run command is:
```bash
docker run --rm -e MESSAGE="Test docker message" 274685854631.dkr.ecr.us-east-1.amazonaws.com/python-logger
```

The Docker option `--rm` is used so the Docker container is cleaned up after exiting. Additional environment variables are below.

### Environment Variables
- **FLUENTD_HOST** (default: localhost) - Remote Fluentd host
- **ENV** (default: DOCKER) - Logging context environment
- **HOST** (default: docker) - Logging context host
- **FUNCTION** (default: BSH) - Logging context function
- **MESSAGE** - Logging message
