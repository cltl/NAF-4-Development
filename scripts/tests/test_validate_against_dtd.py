import os

import pytest

from scripts.validate_against_dtd import validate


@pytest.mark.parametrize(
    "file",
    [
        "before_v31/compound/compound.naf", "after_v31/compound/compound.naf", "after_v31/compound/remove_compound.naf"
    ],
)
def test_compound(v31, ex, file):
    assert validate(os.path.join(ex, file), v31)


@pytest.mark.parametrize(
    "file",
    [
        "before_v31/coreference/coreference.naf",
        "after_v31/coreference/coreference.naf",
        "after_v31/coreference/update_coreference.naf",
        "after_v31/coreference/deprecate_coreference.naf"
    ],
)
def test_coreference(v31, ex, file):
    assert validate(os.path.join(ex, file), v31)


@pytest.mark.parametrize(
    "file",
    [
        "before_v31/entity/entity.naf",
        "after_v31/entity/entity.naf",
    ],
)
def test_entities(v31, ex, file):
    assert validate(os.path.join(ex, file), v31)


@pytest.mark.parametrize(
    "file",
    [
        "before_v31/predicate/unexpressed_frame_element.naf",
        "after_v31/predicate/unexpressed_frame_element.naf",
        "before_v31/predicate/update_frame_element.naf",
        "after_v31/predicate/update_frame_element.naf"
    ],
)
def test_frame_elements(v31, ex, file):
    assert validate(os.path.join(ex, file), v31)


@pytest.mark.parametrize(
    "file",
    [
        "before_v31/mw/idiom.naf",
        "after_v31/mw/idiom.naf",
        "after_v31/mw/remove_idiom.naf"
    ],
)
def test_idiom(v31, ex, file):
    assert validate(os.path.join(ex, file), v31)


@pytest.mark.parametrize(
    "file",
    [
        "before_v31/mw/phrasal.naf",
        "after_v31/mw/phrasal.naf",
        "after_v31/mw/remove_phrasal.naf"
    ],
)
def test_mw(v31, ex, file):
    assert validate(os.path.join(ex, file), v31)


@pytest.mark.parametrize(
    "file",
    [
        "before_v31/predicate/new_predicate.naf",
        "after_v31/predicate/new_predicate.naf",
        "before_v31/predicate/update_predicate.naf",
        "after_v31/predicate/update_predicate.naf",
        "before_v31/predicate/deprecate_predicate.naf",
        "after_v31/predicate/deprecate_predicate.naf"
    ],
)
def test_predicate(v31, ex, file):
    assert validate(os.path.join(ex, file), v31)


@pytest.mark.parametrize(
    "file",
    [
        "before_v31/predicate/predicate_in_compound.naf",
        "after_v31/predicate/predicate_in_compound.naf",
    ],
)
def test_predicate_in_compound(v31, ex, file):
    assert validate(os.path.join(ex, file), v31)


@pytest.mark.parametrize(
    "file",
    [
        "after_v32/tunits.naf",
    ],
)
def test_tunits(v32, ex, file):
    assert validate(os.path.join(ex, file), v32)


@pytest.mark.parametrize(
    "file",
    [
        "v33/lpdep.naf",
    ],
)
def test_lpdeps(v33, ex, file):
    assert validate(os.path.join(ex, file), v33)
