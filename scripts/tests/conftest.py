import pytest


@pytest.fixture
def v31():
    return "resources/dtd/naf_v3.1.dtd"


@pytest.fixture
def v32():
    return "resources/dtd/naf_v3.2.dtd"


@pytest.fixture
def v33():
    return "resources/dtd/naf_v3.3.dtd"


@pytest.fixture
def ex():
    return "examples"
