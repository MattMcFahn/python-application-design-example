"""Wrapper around IO and data transformation methods"""

from data_manipulator.config import Settings
from data_manipulator.data_helper import manipulate_data
from data_manipulator.io_helper import output_csv_file, read_csv_file


def main(settings: Settings) -> None:
    """Main execution"""
    frame = read_csv_file(filepath=settings.input_location)
    frame = manipulate_data(frame=frame)
    output_csv_file(frame=frame, filepath=settings.output_filepath)
