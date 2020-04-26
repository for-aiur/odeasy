import os
from pathlib import Path
home = str(Path.home())

ODEASY_MODELS_FOLDER = os.path.join(home, '.odeasy')
Path(ODEASY_MODELS_FOLDER).mkdir(parents=True, exist_ok=True)