import pytest
from rfc_forge import render_rfc

def test_render_contains_required_sections() -> None:
    assert "## Decision" in render_rfc("Edge design","John","Current design is fragile","Use dual uplinks")

def test_render_rejects_missing_fields() -> None:
    with pytest.raises(ValueError):
        render_rfc("","John","Problem","Decision")
