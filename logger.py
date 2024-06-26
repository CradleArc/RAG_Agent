import functools
import sys
from pathlib import Path

from loguru import logger


@functools.lru_cache()
def get_logger(save_dir: str = "."):
    loguru_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )

    logger.remove()
    logger.add(
        sys.stderr,
        format=loguru_format,
        level="INFO",
        enqueue=True,
    )
    save_file = Path(save_dir) / "{time:YYYY-MM-DD-HH-mm-ss}.log"
    logger.add(save_file, rotation=None, retention="5 days")
    return logger


log_dir = Path(__file__).resolve().parent.parent.parent / "log"
logger = get_logger(str(log_dir))
