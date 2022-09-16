import argparse
from .app import App
from .directory_tree import DirectoryTree


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


def main(args):
    """
    Calls parse_args function to retrieve input from command line.

    Passes input data to function that loads and executes commands.

    Args:
      args (List[str]): command line parameters as list of strings
    """
    args = parse_args(args)

    app = App(tree=DirectoryTree())

    if args.file:
        app.read_commands(args.file)
