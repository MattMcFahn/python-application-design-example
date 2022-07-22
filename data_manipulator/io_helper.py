"""IO helpers - the only place that should read/write to disk!"""

from pathlib import Path

from pandas import DataFrame, read_csv


def read_csv_file(filepath: Path) -> DataFrame:
    """Read csv file into a dataframe"""
    return read_csv(filepath)


def output_csv_file(frame: DataFrame, filepath: Path) -> None:
    """Writes dataframe to path"""
    frame.to_csv(filepath)
