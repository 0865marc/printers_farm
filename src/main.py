""""
---------- PRINTERS_FARM Project----------

Usage:
py main.py --c <path_to_cfg_file>
or
py main.py --configuration <path_to_cfg_file>

For help page:     python main.py --help
"""

from email.policy import default
import click        ## Create CLI


@click.command()
@click.option("--c", "--configuration", default ="printers_farm_cfg.yaml", type = click.Path("rb"), help = "Path of the configuration file (.yaml)")
def get_config(cfg_file):
    with open(cfg_file) as f:
        "Load and save the cfg_file"

    "Return the cfg_file"


if __name__ == "__main__":
    pass