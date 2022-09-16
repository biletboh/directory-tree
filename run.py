import sys

from tree.cli import main


def run():
    """
    Calls main function passing the CLI arguments.

    This function is an entry point to this command line utility.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
