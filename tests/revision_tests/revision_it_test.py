from graphlembic.revision.revision import RevisionID
from graphlembic.helpers.revision import generate_revision


def test_with_valide_revision_id() -> None:
    raw_rev_id = "aaaaaaaaaaaa"
    rev_id = RevisionID(raw_rev_id)
    assert rev_id == raw_rev_id