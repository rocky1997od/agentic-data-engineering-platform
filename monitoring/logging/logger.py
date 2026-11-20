
import json
import logging
import os
from datetime import datetime, timezone


class JsonFormatter(logging.Formatter):

    def format(self, record):
        log_data = {
            "timestamp": datetime.fromtimestamp(
                record.created,
                tz=timezone.utc
            ).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "component": getattr(record, "component", "application"),
            "pipeline": getattr(record, "pipeline", None),
        }

        if record.exc_info:
            log_data["exception"] = self.formatException(
                record.exc_info
            )

        return json.dumps(log_data)


def get_logger(name: str) -> logging.Logger:

    logger = logging.getLogger(name)

    logger.setLevel(
        os.getenv("LOG_LEVEL", "INFO").upper()
    )

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)

    logger.propagate = True

    return logger
