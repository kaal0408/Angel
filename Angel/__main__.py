import glob
from pathlib import Path
from Raizen.utils import load_plugins
import logging
from . import Raizen

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "Raizen/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")
print("Enjoy! Do visit @KristinaSupportChat")

if __name__ == "__main__":
    Raizen.run_until_disconnected()
