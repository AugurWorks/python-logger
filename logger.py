import os
from fluent import sender

logger = sender.FluentSender('bash', host=os.environ.get('FLUENTD_HOST', 'localhost'), port=24224)

logger.emit('follow', {
    'env': os.environ.get('ENV', 'DOCKER'),
    'host': os.environ.get('HOST', 'docker'),
    'function': os.environ.get('FUNCTION', 'BSH'),
    'message': os.environ.get('MESSAGE')
})

logger.close()
