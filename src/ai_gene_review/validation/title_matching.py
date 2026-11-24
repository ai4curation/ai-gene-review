"""Let a literature quote match the cached record's title.

The reference validator (``linkml-reference-validator``) reads a cached
publication's frontmatter ``title`` into ``ReferenceContent.title`` and strips
the ``# title`` heading from the text it searches, so a quote can only match the
body. Records cached in the older MEDLINE layout repeat the title and citation
line in their body; records in the canonical layout that ``etl/publication.py``
writes do not. A ``supporting_text`` that is exactly a paper's title (over a
hundred in the corpus) therefore passes or fails depending only on which layout
its record was last cached in, and regenerating a record silently breaks them.

The title is verbatim source text, so it is a legitimate thing to quote. This
module makes it one more searchable text for ``PMID:`` and ``DOI:`` references.
It is a separate text, not concatenated to the body: each quote part must fall
within the title or within the body, so a quote cannot run from one into the
other.

The library constructs ``SupportingTextValidator`` in several places (its CLI,
its LinkML plugin, its repairer), each importing the class by name, so the
classmethod is replaced on the class itself rather than in a subclass. Call
:func:`install_title_matching` before validating; the repo's validator builder
and its CLI entry point both do.
"""

from __future__ import annotations

from linkml_reference_validator.models import ReferenceContent
from linkml_reference_validator.validation.supporting_text_validator import (
    SupportingTextValidator,
)

#: Reference prefixes whose cached ``title`` is the paper's own title.
TITLE_SEARCHABLE_PREFIXES = frozenset({"PMID", "DOI"})

_MARKER = "_ai_gene_review_title_matching"


def install_title_matching() -> None:
    """Make a literature reference's title searchable by every quote check. Idempotent.

    Examples:
        >>> install_title_matching()
        >>> ref = ReferenceContent(reference_id="PMID:1", content="Body.", title="Title")
        >>> SupportingTextValidator.searchable_texts(ref)
        ['Body.', 'Title']
        >>> install_title_matching()  # a second call changes nothing
        >>> SupportingTextValidator.searchable_texts(ref)
        ['Body.', 'Title']
        >>> local = ReferenceContent(reference_id="file:x.md", content="Body.", title="x.md")
        >>> SupportingTextValidator.searchable_texts(local)
        ['Body.']
    """
    if getattr(SupportingTextValidator, _MARKER, False):
        return
    original = SupportingTextValidator.searchable_texts.__func__  # type: ignore[attr-defined]

    def searchable_texts(cls: type, reference: ReferenceContent) -> list[str]:
        texts = original(cls, reference)
        prefix = reference.reference_id.partition(":")[0].upper()
        title = (reference.title or "").strip()
        if title and prefix in TITLE_SEARCHABLE_PREFIXES and title not in texts:
            return [*texts, title]
        return texts

    searchable_texts.__doc__ = original.__doc__
    SupportingTextValidator.searchable_texts = classmethod(searchable_texts)  # type: ignore[method-assign,assignment]
    setattr(SupportingTextValidator, _MARKER, True)
