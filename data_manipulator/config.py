"""Application settings inheriting from pydantic.BaseSettings"""
from functools import lru_cache
from logging import getLogger
from os import getenv
from pathlib import Path
from typing import Optional
from uuid import uuid4

from pydantic import BaseSettings, validator

logger = getLogger(__name__)

SUPPORTED_FORMATS = {".csv", ".xlsx"}


class Settings(BaseSettings):
    """
    Relevant application settings exposed via settings
    https://pydantic-docs.helpmanual.io/usage/settings/
    """

    run_id: Optional[str] = getenv("RUN_ID", str(uuid4()))
    log_level: Optional[str] = getenv("LOG_LEVEL", "INFO")

    # Main application settings
    input_location: Path
    output_location: Path
    filename: Path
    output_format: str

    # AWS storage details
    aws_access_key_id: Optional[str]
    aws_secret_access_key: Optional[str]
    s3_bucket: Optional[str]
    aws_role_arn: Optional[str]

    @property
    def output_filepath(self):
        """Derive the output filepath"""
        return Path(f"{self.output_location}/{self.filename}{self.output_format}")

    # TODO: Link validators and exceptions.py
    @validator("output_format")
    def check_output_format_supported(cls, value):  # pylint: disable=E0213
        """Validate that the output format is supported"""
        if value not in SUPPORTED_FORMATS:
            raise Exception(f"Output format: {value} is not supported. Supported formats are: {SUPPORTED_FORMATS}")
        return value

    @validator("input_location")
    def check_input_format_supported(cls, value):  # pylint: disable=E0213
        """Validate that the input format is supported"""
        if value.suffix not in SUPPORTED_FORMATS:
            raise Exception(f"Input format: {value} is not supported. Supported formats are: {SUPPORTED_FORMATS}")
        return value


@lru_cache()
def get_settings(**kwargs) -> Settings:
    """Retrieve application settings"""
    logger.info("Loading config settings from the environment...")
    return Settings(**kwargs)
