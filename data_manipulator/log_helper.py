"""Module to configure logging handlers, filters and levels
in the application entrypoint
"""

from dataclasses import dataclass
from logging import FileHandler, Filter, Formatter, Handler, StreamHandler, getLevelName, getLogger, root
from os import makedirs
from os.path import exists
from typing import List

from data_manipulator import settings

LOG_LEVEL = getLevelName(settings.log_level)

# pylint: disable=too-few-public-methods


@dataclass()
class LogFields:
    """Standard fields present with each log, passed via the record filter"""

    run_id: str


class AppFilter(Filter):
    """
    Class that can act on a log handler to filter all records passed to the handle
    and add fields that should be present in all logs
    """

    def __init__(self, run_id: str, *args, **kwargs):
        self.run_id = run_id

        super().__init__(*args, **kwargs)

    def filter(self, record) -> bool:
        """Impose relevant fields on records"""
        record.runId = self.run_id
        record.component = "data-manipulator"
        return True


def get_log_handlers(log_fields) -> List[Handler]:
    """
    Define and format logging handlers to use in the app
    Currently output to stdout/stderr (StreamHandler), and to a local file.
    """
    log_format = "[%(asctime)s] %(levelname)s <%(runId)s> [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
    date_format = "%Y-%m-%dT%H:%M:%S"

    # TODO: I've added a file hander log for now, but we may want to remove
    simple_formatter = Formatter(log_format, date_format)

    # Setup file handler
    if not exists("./logs/manipulator.log"):
        makedirs("./logs", exist_ok=True)
    file_handler = FileHandler("./logs/manipulator.log")
    file_handler.setFormatter(simple_formatter)

    # Setup stdout/stderr handler
    stream_handler = StreamHandler()
    stream_handler.setFormatter(simple_formatter)

    app_filter = AppFilter(
        run_id=log_fields.run_id,
    )
    stream_handler.addFilter(app_filter)
    file_handler.addFilter(app_filter)

    return [handler for handler in [file_handler, stream_handler] if handler]


def setup_logging(
    log_fields: LogFields,
):
    """
    Configures logging with a chosen formatter.
    """
    handlers = get_log_handlers(log_fields=log_fields)

    # Pass handlers and level back to the root logger
    root.handlers = handlers
    root.setLevel(LOG_LEVEL)

    # pylint: disable=no-member
    for name in root.manager.loggerDict.keys():
        logger = getLogger(name)
        logger.handlers = []
        logger.propagate = True

    # # Add overrides for module specific loggers here if needed
    # modules = {
    #     "botocore": WARNING,
    # }
    # for name, level in modules.items():
    #     logger = getLogger(name)
    #     logger.handlers = []
    #     logger.setLevel(level)
    #     logger.propagate = True
