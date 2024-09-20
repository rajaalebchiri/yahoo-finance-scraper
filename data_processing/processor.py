"""processor.py

cleaning and processing functions
"""

import datetime
import argparse


def date_validator(date: str) -> bool:
    """Date Validator"""
    date_format = '%Y-%m-%d'
    try:
        datetime.datetime.strptime(date, date_format)
        return True
    except ValueError as exc:
        raise argparse.ArgumentTypeError(f"Invalid date: {date}") from exc


def validate_date_range(start_date, end_date):
    """Ensure the range between dates is no more than a year."""
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    delta = end_date - start_date
    if delta.days > 365:
        raise argparse.ArgumentTypeError(
            "The period between start and end date cannot be more than 1 year.")
        return
    return True