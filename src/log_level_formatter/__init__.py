import logging

class LogLevelFormatter(logging.Formatter):
    _fmt_repo = {}

    def __init__(self, fmt=None, datefmt=None, debug=None, info=None, warn=None, error=None, critical=None):
        logging.Formatter.__init__(self, fmt, datefmt)

        self._fmt_repo[logging.CRITICAL] = critical or error or warn or info or debug or self._fmt
        self._fmt_repo[logging.ERROR] = error or warn or info or debug or self._fmt
        self._fmt_repo[logging.WARN] = warn or info or debug or self._fmt
        self._fmt_repo[logging.INFO] = info or debug or self._fmt
        self._fmt_repo[logging.DEBUG] = debug or self._fmt

    def format(self, record):
        self._fmt = self._fmt_repo[record.levelno]
        return logging.Formatter.format(self, record)
