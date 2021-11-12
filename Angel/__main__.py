import glob
from pathlib import Path
from Angel.utils import load_plugins
import logging
from . import Angel

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "Angel/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")
print("Enjoy! Do visit @MeowUserbot")

if __name__ == "__main__":
    Raizen.run_until_disconnected()
