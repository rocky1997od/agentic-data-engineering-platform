
import json
import logging

from monitoring.logging.logger import get_logger, JsonFormatter


def test_logger_outputs_valid_json(caplog):

    logger = get_logger("data_platform")

    with caplog.at_level(logging.INFO, logger="data_platform"):

        logger.info(
            "Pipeline started",
            extra={
                "component": "ingestion",
                "pipeline": "customer_transaction",
            },
        )

    assert len(caplog.records) == 1

    record = caplog.records[0]

    formatted = JsonFormatter().format(record)
    log_data = json.loads(formatted)

    assert log_data["level"] == "INFO"
    assert log_data["message"] == "Pipeline started"
    assert log_data["component"] == "ingestion"
    assert log_data["pipeline"] == "customer_transaction"
    assert "timestamp" in log_data


def test_logger_captures_exception(caplog):

    logger = get_logger("data_platform")

    with caplog.at_level(logging.ERROR, logger="data_platform"):

        try:
            raise ValueError("Invalid transaction amount")

        except ValueError:
            logger.exception(
                "Transaction processing failed",
                extra={
                    "component": "transformation",
                    "pipeline": "payment_pipeline",
                },
            )

    assert len(caplog.records) == 1

    record = caplog.records[0]

    formatted = JsonFormatter().format(record)
    log_data = json.loads(formatted)

    assert log_data["level"] == "ERROR"
    assert log_data["message"] == "Transaction processing failed"
    assert "ValueError" in log_data["exception"]
    assert "Invalid transaction amount" in log_data["exception"]
