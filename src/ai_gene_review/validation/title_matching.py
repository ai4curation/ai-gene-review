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
(``build_supporting_text_validator``) and its CLI entry point (``reference_cli``,
used by ``scripts/run_reference_validator.sh``) both do. A bare
``linkml-reference-validator`` console-script run bypasses both and still judges
title quotes the upstream way. :func:`uninstall_title_matching` restores the
library's own method, for tests that need a clean class.
"""

from __future__ import annotations

from linkml_reference_validator.models import ReferenceContent
from linkml_reference_validator.validation.supporting_text_validator import (
    SupportingTextValidator,
)

#: Reference prefixes whose cached ``title`` is the paper's own title.
TITLE_SEARCHABLE_PREFIXES = frozenset({"PMID", "DOI"})

_MARKER = "_ai_gene_review_title_matching"
_ORIGINAL_ATTR = "_ai_gene_review_original_searchable_texts"


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
        >>> uninstall_title_matching()
        >>> SupportingTextValidator.searchable_texts(ref)
        ['Body.']
    """
    if getattr(SupportingTextValidator, _MARKER, False):
        return
    # Fails fast at ``.__func__`` if upstream removes the method or stops making it a
    # classmethod, rather than silently doing nothing.
    original_descriptor = SupportingTextValidator.__dict__["searchable_texts"]
    original = SupportingTextValidator.searchable_texts.__func__  # type: ignore[attr-defined]

    def searchable_texts(
        cls: type, reference: ReferenceContent, *args, **kwargs
    ) -> list[str]:
        texts = original(cls, reference, *args, **kwargs)
        prefix = (reference.reference_id or "").partition(":")[0].upper()
        title = (reference.title or "").strip()
        if title and prefix in TITLE_SEARCHABLE_PREFIXES and title not in texts:
            return [*texts, title]
        return texts

    searchable_texts.__doc__ = original.__doc__
    setattr(SupportingTextValidator, _ORIGINAL_ATTR, original_descriptor)
    SupportingTextValidator.searchable_texts = classmethod(searchable_texts)  # type: ignore[method-assign,assignment]
    setattr(SupportingTextValidator, _MARKER, True)


def uninstall_title_matching() -> None:
    """Restore the library's own ``searchable_texts``. A no-op when not installed."""
    if not getattr(SupportingTextValidator, _MARKER, False):
        return
    SupportingTextValidator.searchable_texts = getattr(
        SupportingTextValidator, _ORIGINAL_ATTR
    )  # type: ignore[method-assign]
    delattr(SupportingTextValidator, _ORIGINAL_ATTR)
    delattr(SupportingTextValidator, _MARKER)
