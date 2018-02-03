import logging
import logging.config
import log_level_formatter

SIMPLE = '%(levelname)s %(message)s'
DETAIL = '%(levelname)s %(asctime)s %(name)s %(module)s %(process)d %(processName)s %(thread)d %(threadName)s %(message)s'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            '()': log_level_formatter.LogLevelFormatter,
            'debug': DETAIL,
            'info': SIMPLE,
            'warn': DETAIL
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'filename': 'test.log',
            'maxBytes': 1048576,
            'backupCount': 10
        }
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)

logger.debug('detail format')
logger.info('simple format')
logger.warn('detail format')
logger.error('detail format')
logger.critical('detail format')
