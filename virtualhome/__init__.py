import glob
import sys
from sys import platform

import importlib.util, pathlib
import virtualhome
SIM_PATH = str(pathlib.Path(virtualhome.__file__).parent / 'simulation')
sys.path.append(SIM_PATH)

from unity_simulator.comm_unity import UnityCommunication
from unity_simulator import utils_viz
