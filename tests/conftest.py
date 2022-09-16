import pytest


@pytest.fixture
def node(name=""):
    return {"name": name, "subdirs": []}
