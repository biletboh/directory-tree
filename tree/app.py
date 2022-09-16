from .directory_tree import AbstractDirectoryTree


class App:
    """
    The App
    """

    def __init__(self, tree: AbstractDirectoryTree):
        """
        Initializes app with the directory tree.

        Args:
            tree:
                A directory tree data structure.
        """
        self.tree = tree

    def create(self, command, path):
        print(f"{command} {path}")
        parsed_path = path.split("/")
        self.tree.create(parsed_path)

    def delete(self, command, path):
        print(f"{command} {path}")
        parsed_path = path.split("/")
        self.tree.delete(parsed_path)

    def move(self, command, path_from, path_to):
        print(f"{command} {path_from} {path_to}")
        parsed_path_from = path_from.split("/")
        parsed_path_to = path_to.split("/")
        self.tree.move(parsed_path_from, parsed_path_to)
