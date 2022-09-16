from tree.cli import parse_args
import sys


def main(args):
    """
    Calls parse_args function to retrieve input from command line.

    Passes input data to function that loads and executes commands.

    Args:
      args (List[str]): command line parameters as list of strings
    """
    args = parse_args(args)
    if args.file:
        print(args.file)
        pass


def run():
    """
    Calls main function passing the CLI arguments.

    This function is an entry point to this command line utility.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
