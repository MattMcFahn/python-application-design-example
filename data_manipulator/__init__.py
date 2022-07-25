"""Load env vars and expose settings for the module"""
from dotenv import load_dotenv

from data_manipulator.config import get_settings

load_dotenv(".env")
settings = get_settings()
