import argparse


def parse_args(args):
    """
    Parse command line parameters.

    Args:
      args (List[str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Manage directory tree.")
    parser.add_argument(
        "-f", "--file", help="Path to the text file with commands.", type=str
    )
    return parser.parse_args(args)
