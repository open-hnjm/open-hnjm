import logging
import os

class CustomLogger:
    def __init__(self, name, log_file=None, level=logging.INFO):
        """Initialize custom logger with name and optional file output"""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.formatter = logging.Formatter(
            '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(self.formatter)
        self.logger.addHandler(console_handler)

        # File handler (optional)
        if log_file:
            if os.name == 'posix':
                log_file = os.path.join('/var/log/open-hnjm', log_file)
            else:
                log_file = os.path.join('logs/', log_file)
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(self.formatter)
            self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)