# log-level-formatter

로깅을 하다보면 로그 핸들러가 로그 레벨에 따라 다른 로그 포맷을 사용할 필요가 있을 수 있다.  
예를들어, DEBUG 레벨의 경우는 디버깅을 위한 상세한 정보들이 필요할 것이다. 하지만 INFO 레벨의 경우는 간단한 정보들만 출력하면 될 것이다. 또한 경우에 따라 WARN, ERROR 그리고 CRITICAL 레벨의 로그 정보를 달리 할 필요가 있을 수 있다.  

log-level-formatter는 위와 같은 경우를 위해 각 로깅 레벨에 따라 로그 포맷을 설정할 수 있는 기능을 제공하는 커스텀 포맷터이다. 

## Usage

log-level-formatter는 다음 다섯가지 파라메터를 가지고 있다.  
각각의 파라메터는 로그레벨을 가리키며, 해당 로그레벨의 로그 포맷을 설정한다. 

* debug
* info
* warn
* error
* critical

위 각각의 파라메터는 로그레벨과 동일하게 로그포맷을 전파한다.  
예를들어, debug 파라메터를 설정한 후 info, warn, error, critical 파라메터를 설정하지 않는다면, 설정되지 않은 로그레벨의 경우는 debug 파라메터에 설정 된 로그포맷을 사용하게 된다.  

다음 예제는 debug와 warn 파라메터에 자세한 로그포맷을 적용하고 info 파라메터에는 간단한 로그포맷을 적용하였다. 
따라서, 설정되지 않은 error와 critical 로그레벨의 경우는 warn 파라메터에 적용된 자세한 로그포맷이 적용된다.

```python
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
```

위 예제를 실행한 결과는 다음과 같다. 

```sh
DEBUG 2018-02-03 22:30:06,748 __main__ ex 10681 MainProcess 140735863001920 MainThread detail format
INFO simple format
WARNING 2018-02-03 22:30:06,748 __main__ ex 10681 MainProcess 140735863001920 MainThread detail format
ERROR 2018-02-03 22:30:06,748 __main__ ex 10681 MainProcess 140735863001920 MainThread detail format
CRITICAL 2018-02-03 22:30:06,748 __main__ ex 10681 MainProcess 140735863001920 MainThread detail format
```