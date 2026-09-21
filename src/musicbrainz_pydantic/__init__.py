import logging
import sys
from importlib.metadata import version

import platformdirs


__version__ = version("musicbrainz-pydantic")

APP_DIRS = platformdirs.PlatformDirs("musicbrainz-pydantic", ensure_exists=True)
USER_AGENT = f"musicbrainz-pydantic/{__version__} ( https://robert.huseli.us/ )"

# Logging everything above INFO level to stderr, the rest to stdout:
__stderr_handler = logging.StreamHandler(sys.stderr)
__stderr_handler.addFilter(lambda r: r.levelno > logging.INFO)
__stdout_handler = logging.StreamHandler(sys.stdout)
__stdout_handler.addFilter(lambda r: r.levelno <= logging.INFO)

logger = logging.getLogger(__name__)
logger.addHandler(__stderr_handler)
logger.addHandler(__stdout_handler)
logger.setLevel(logging.INFO)
