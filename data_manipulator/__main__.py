"""Main entrypoint for the package"""
from data_manipulator import settings
from data_manipulator.log_helper import LogFields, setup_logging
from data_manipulator.process import main

log_fields = LogFields(
    run_id=settings.run_id,
)

setup_logging(log_fields=log_fields)

main(settings)
