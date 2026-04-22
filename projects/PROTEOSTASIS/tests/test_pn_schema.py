"""Tests for the Proteostasis Network LinkML schema."""

from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView


REPO_ROOT = next(
    path for path in Path(__file__).resolve().parents if (path / "project.justfile").exists()
)
SCHEMA_PATH = REPO_ROOT / "src/ai_gene_review/schema/contrib/pn.yaml"


def _enum_texts(view: SchemaView, enum_name: str) -> set[str]:
    """Return the display text for all permissible values in an enum."""
    enum_definition = view.schema.enums[enum_name]
    return {
        permissible_value.text or key
        for key, permissible_value in enum_definition.permissible_values.items()
    }


def test_pn_schema_has_expected_vocab_counts() -> None:
    """The generated schema should expose the full workbook vocabulary."""
    view = SchemaView(str(SCHEMA_PATH))

    assert "PNPath" in view.all_classes()
    assert "PNToGOMapping" in view.all_classes()
    assert set(view.all_classes()) == {"PNPath", "PNToGOMapping"}

    assert len(_enum_texts(view, "PNBranchEnum")) == 9
    assert len(_enum_texts(view, "PNClassEnum")) == 32
    assert len(_enum_texts(view, "PNGroupEnum")) == 251
    assert len(_enum_texts(view, "PNTypeEnum")) == 559
    assert len(_enum_texts(view, "PNSubtypeEnum")) == 381

    assert "(no Group)" not in _enum_texts(view, "PNGroupEnum")
    assert "(no Type)" not in _enum_texts(view, "PNTypeEnum")
    assert "(no Subtype)" not in _enum_texts(view, "PNSubtypeEnum")


def test_pn_schema_contains_known_categories() -> None:
    """The PN schema should retain representative workbook labels verbatim."""
    view = SchemaView(str(SCHEMA_PATH))

    assert "Autophagy-Lysosome Pathway" in _enum_texts(view, "PNBranchEnum")
    assert "Chaperone-mediated autophagy" in _enum_texts(view, "PNClassEnum")
    assert "Nascent peptide husbandry" in _enum_texts(view, "PNGroupEnum")
    assert "Nascent peptide sorting" in _enum_texts(view, "PNTypeEnum")
    assert "NAC component" in _enum_texts(view, "PNSubtypeEnum")
