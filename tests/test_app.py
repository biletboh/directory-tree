from tree.app import App
from tree.directory_tree import DirectoryTree


def test_app_create(mocker):
    mocker.patch("tree.directory_tree.DirectoryTree.create")
    app = App(tree=DirectoryTree())
    app.create("CREATE", "grains/squash")
    DirectoryTree.create.assert_called_once()


def test_app_delete(mocker):
    mocker.patch("tree.directory_tree.DirectoryTree.delete")
    app = App(tree=DirectoryTree())
    app.delete("DELETE", "grains/squash")
    DirectoryTree.delete.assert_called_once()


def test_app_move(mocker):
    mocker.patch("tree.directory_tree.DirectoryTree.move")
    app = App(tree=DirectoryTree())
    app.move("MOVE", "grains/squash", "fruits/apples")
    DirectoryTree.move.assert_called_once()
