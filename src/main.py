""""
---------- PRINTERS_FARM Project----------

Usage:
py main.py --c <path_to_cfg_file>

For help page:     python main.py --help
"""

import click       
import yaml
from farm import Farm

@click.command()
@click.option("--c", default ="printers_farm_cfg.yaml", type = click.Path("rb"), help = "Path of the configuration file (.yaml)")
def get_config(c):
    with open(c) as f:
        "Load and save the cfg_file"
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config



if __name__ == "__main__":
    config = get_config.main(standalone_mode=False)
    farm = Farm(config)
    farm.start()