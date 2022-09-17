from .directory_tree import AbstractDirectoryTree
from typing import List


class App:
    """
    The App is responsible for reading commands from a file
    and representing outputs.
    """

    def __init__(self, tree: AbstractDirectoryTree):
        """
        Initializes app with the directory tree.

        Attributes:
            tree:
                directory tree data structure.
        """
        self.tree = tree

    def read_commands(self, file: str):
        """
        Read commands from a file and run them.

        Args:
            file:
                str representing path to a file.
        """
        with open(file, "r") as reader:
            for command in reader.readlines():
                self.run_command(command)

    def run_command(self, command: str):
        """
        Parse and run commands.

        Args:
            command:
                str representing command.
        """
        command = command.strip()
        print(command)
        command, path1, path2 = self.parse(command)
        if command == "CREATE":
            self.create(path1)
        elif command == "DELETE":
            self.delete(path1)
        elif command == "MOVE":
            if path2:
                self.move(path1, path2)
        elif command == "LIST":
            self.list()

    def parse(self, command: str):
        """
        Create a path list from command string.

        Args:
            command:
                str representing command.
        Returns:
            command:
                str cleaned up command.
            path1:
                list representing path to the first directory.
            path2:
                list representing path to the second directory.
        """
        parsed_command = command.split(" ")
        command = parsed_command[0]
        if len(parsed_command) > 1:
            path1 = parsed_command[1].split("/")
        else:
            path1 = None
        if len(parsed_command) > 2:
            path2 = parsed_command[2].split("/")
        else:
            path2 = None
        return command, path1, path2

    def create(self, path: List[str]):
        """
        Invoke tree create method with path data.

        Args:
            path:
                list representing path to the directory.
        """
        self.tree.create(path)

    def delete(self, path: List[str]):
        """
        Invoke tree delete method with path data.

        Args:
            path:
                list representing path to the directory.

        Raises:
            ValueError: Cannot delete directory.
        """
        try:
            self.tree.delete(path)
        except ValueError as e:
            path_str = "/".join(path)
            print(f"Cannot delete {path_str} - {e}")

    def move(self, path_from: List[str], path_to: List[str]):
        """
        Invoke tree move method with path data.

        Args:
            path_from:
                A list representing a branch of the directory tree
                where method must cut a node.
            path_to:
                A list representing a branch of the directory tree
                where method must paste a node.
        """
        self.tree.move(path_from, path_to)

    def list(self):
        """
        Print directory tree structure to console.
        """
        data = self.tree.list()
        generated_list = self.generate_list(root=data.subdirs)
        for node in generated_list:
            print(node)

    def generate_list(
        self,
        depth: int = 0,
        root: dict = {},
    ):
        """
        Recursively generate string representation of directory tree.

        Yields:
            str representing tree node.
            recursively reiterates to display child nodes.
        """
        keys = list(root.keys())
        keys.sort()
        for node in keys:
            tab = "  " * depth
            yield f"{tab}{node}"
            if root[node].subdirs:
                yield from self.generate_list(
                    depth=depth + 1, root=root[node].subdirs
                )
