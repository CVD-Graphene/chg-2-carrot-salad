"""
MAIN FILE WITH SETTINGS
IMPORT HERE ALL NECESSARY SETTINGS FOR YOUR DEVICE AND CONNECTIONS

"""

import platform
from .actions import *
from .raspberry import *


LOCAL_MODE = platform.system() != 'Linux'
