# logger_factory.py

"""
Logger Factory Module

This module provides a simple utility function to initialize and configure a logger
with both file and stream handlers. Logs are stored in a 'logs/' subdirectory
relative to this script's location. Each logger is independent and writes to its own
log file, named after the provided logger name.
"""

# Standard Library Imports
import logging
from pathlib import Path

# Define the output directory for all log files
OUTPUT_DIR = Path(__file__).parent / "logs"

def initialize_logger(
    name: str,
    level: str = "INFO",
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt: str = "%Y-%m-%d %H:%M:%S",
) -> logging.Logger:
    """
    Initialize and configure a logger.

    Parameters:
        name (str): The name of the logger and its associated log file.
        level (str): Logging level (e.g., 'DEBUG', 'INFO', 'WARNING', etc.).
                     Default: 'INFO'.
        format (str): Log message format string.
                      Default: "%(asctime)s - %(name)s - %(levelname)s - %(message)s".
        datefmt (str): Date/time format string for log timestamps.
                       Default: '%Y-%m-%d %H:%M:%S'.

    Returns:
        logging.Logger: A configured logger instance.
    """

    # Get or create a logger by name
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    # Prevent duplicate handlers if logger already exists
    if logger.hasHandlers():
        logger.handlers.clear()

    # Ensure the output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Set up file and stream handlers
    file_handler = logging.FileHandler(OUTPUT_DIR / f"{name}.log", encoding='utf-8')
    stream_handler = logging.StreamHandler()
    
    # Set formatting for both handlers
    formatter = logging.Formatter(fmt=format, datefmt=datefmt)
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Attach handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger