"""Query building, term selection, and signal extraction for litscan."""

from __future__ import annotations

import re
from typing import Iterable

# Single tokens too generic to query a module on by themselves. The module match
# index is full of these (e.g. "cilium", "complex", "pathway"); a term made up
# only of these would flood Europe PMC, so it is dropped from the query.
GENERIC_TERMS: frozenset[str] = frozenset(
    {
        "acid",
        "activity",
        "assembly",
        "binding",
        "biogenesis",
        "biosynthesis",
        "carrier",
        "catalytic",
        "cell",
        "cellular",
        "chaperone",
        "chaperonin",
        "channel",
        "complex",
        "component",
        "core",
        "cycle",
        "cytoplasm",
        "cytosol",
        "degradation",
        "domain",
        "enzyme",
        "factor",
        "family",
        "folding",
        "function",
        "gene",
        "generic",
        "import",
        "machinery",
        "membrane",
        "metabolic",
        "metabolism",
        "module",
        "organelle",
        "pathway",
        "process",
        "protein",
        "proteins",
        "reaction",
        "receptor",
        "regulation",
        "regulatory",
        "response",
        "subunit",
        "subunits",
        "synthesis",
        "system",
        "transport",
        "transporter",
        "unit",
        "units",
        # ubiquitous cofactors / small molecules: present in most metabolic
        # modules, so non-discriminating and far too broad to query on.
        "adp",
        "amp",
        "atp",
        "bicarbonate",
        "co2",
        "coa",
        "gdp",
        "glucose",
        "glycine",
        "gmp",
        "gtp",
        "h2o",
        "nad",
        "nadh",
        "nadp",
        "nadph",
        "nh3",
        "o2",
        "oxygen",
        "phosphate",
        "pi",
        "pyruvate",
        "pyrophosphate",
        "water",
    }
)

# Leading organism qualifiers stripped from module terms so a symbol like
# "human PEX3" queries as "PEX3" (which is how papers actually name it).
_ORGANISM_PREFIXES: frozenset[str] = frozenset(
    {
        "human",
        "mouse",
        "rat",
        "yeast",
        "arabidopsis",
        "drosophila",
        "zebrafish",
        "bovine",
        "plant",
        "fungal",
        "bacterial",
    }
)

# Always-on hard exclusions (empirically the dominant litscan false positives):
# notices, bacterial taxonomy descriptions, and plant gene-family surveys.
EXCLUDED_TITLE_TERMS: tuple[str, ...] = (
    "TITLE:corrigendum",
    "TITLE:erratum",
    "TITLE:correction",
    "TITLE:retraction",
    "TITLE:withdrawn",
    'TITLE:"gen. nov."',
    'TITLE:"sp. nov."',
    'TITLE:"genome-wide identification"',
)

# Membership-novelty signals for the module-member job (job C).
MEMBERSHIP_SIGNALS: dict[str, tuple[str, ...]] = {
    # Deliberately specific: bare "we identify / identification of" is dropped
    # because it fires on every clinical-genetics "we identified N genes" abstract.
    "new_member": (
        "novel component",
        "new component",
        "novel subunit",
        "new subunit",
        "novel member",
        "new member",
        "additional subunit",
        "previously unknown subunit",
        "newly identified subunit",
        "a new subunit of",
        "novel factor",
    ),
    "assembly": (
        "assembly factor",
        "assembly intermediate",
        "is required for assembly",
        "required for the assembly",
        "assembly of the",
    ),
    "interaction": (
        "interacts directly with",
        "directly interacts",
        "binds directly to",
        "associates with the",
        "is a component of",
        "part of the",
        "interaction partner",
        "protein partner",
        "protein partners",
    ),
    "structure": (
        "cryo-em structure",
        "crystal structure",
        "structural basis",
        "structure of the",
        "structure reveals",
    ),
}


def _tokens(term: str) -> list[str]:
    return [t for t in re.split(r"[^a-z0-9]+", term.casefold()) if t]


def is_distinctive(term: str) -> bool:
    """True if ``term`` is a good Europe PMC query term for a module.

    A good query term is a short named entity (a gene symbol, complex name, or
    named pathway/metabolite) that plausibly appears verbatim in a title or
    abstract -- not a long descriptive ontology label. So we require 1-4 tokens,
    reject descriptive-label punctuation (parentheses, commas, ``e.g.``), and
    require at least one non-generic token.

    >>> is_distinctive("BBSome")
    True
    >>> is_distinctive("intraciliary transport")
    True
    >>> is_distinctive("Calvin-Benson")
    True
    >>> is_distinctive("complex")
    False
    >>> is_distinctive("protein folding chaperone")
    False
    >>> is_distinctive("GTP-dependent recruitment of the BBSome to the ciliary membrane")
    False
    >>> is_distinctive("ciliary GPCR cargo (e.g. SSTR3, MCHR1, NPY2R)")
    False
    """
    t = term.strip()
    if len(t) < 3 or len(t) > 40:
        return False
    if any(c in t for c in "(),"):
        return False
    if "e.g" in t.casefold():
        return False
    tokens = _tokens(t)
    if not tokens or len(tokens) > 4:
        return False
    return any(tok not in GENERIC_TERMS and len(tok) >= 3 for tok in tokens)


def _rank(term: str) -> tuple[int, int, int]:
    """Rank key (higher = preferred): proper-noun terms, then shorter terms."""
    has_proper = any(any(c.isupper() for c in word) for word in term.split())
    tokens = _tokens(term)
    return (1 if has_proper else 0, -len(tokens), -len(term))


def _strip_organism_prefix(term: str) -> str:
    """Drop a leading organism qualifier from a term.

    >>> _strip_organism_prefix("human PEX3")
    'PEX3'
    >>> _strip_organism_prefix("BBSome")
    'BBSome'
    """
    parts = term.split()
    if len(parts) >= 2 and parts[0].casefold() in _ORGANISM_PREFIXES:
        return " ".join(parts[1:])
    return term


def select_query_terms(terms: Iterable[str], max_terms: int = 10) -> list[str]:
    """Pick the best module query terms: named entities first, deduped."""
    seen: set[str] = set()
    kept: list[str] = []
    for raw in terms:
        term = _strip_organism_prefix(raw)
        key = term.casefold()
        if key in seen or not is_distinctive(term):
            continue
        seen.add(key)
        kept.append(term)
    kept.sort(key=_rank, reverse=True)
    return kept[:max_terms]


def build_query(chosen_terms: list[str], date_from: str, date_to: str) -> str:
    """Assemble a Europe PMC query from already-selected terms.

    >>> build_query(["BBSome"], "2026-01-01", "2026-06-19")
    'SRC:MED AND FIRST_PDATE:[2026-01-01 TO 2026-06-19] AND (TITLE_ABS:"BBSome") NOT (TITLE:corrigendum OR TITLE:erratum OR TITLE:correction OR TITLE:retraction OR TITLE:withdrawn OR TITLE:"gen. nov." OR TITLE:"sp. nov." OR TITLE:"genome-wide identification")'
    """
    if not chosen_terms:
        raise ValueError("no distinctive terms to build a query from")
    term_clause = " OR ".join(f'TITLE_ABS:"{t}"' for t in chosen_terms)
    excluded = " OR ".join(EXCLUDED_TITLE_TERMS)
    return (
        f"SRC:MED AND FIRST_PDATE:[{date_from} TO {date_to}] "
        f"AND ({term_clause}) NOT ({excluded})"
    )


def build_module_query(
    terms: Iterable[str], date_from: str, date_to: str, *, max_terms: int = 10
) -> str:
    """Select query terms for a module and assemble its Europe PMC query.

    >>> build_module_query(["BBSome", "complex"], "2026-01-01", "2026-06-19")
    'SRC:MED AND FIRST_PDATE:[2026-01-01 TO 2026-06-19] AND (TITLE_ABS:"BBSome") NOT (TITLE:corrigendum OR TITLE:erratum OR TITLE:correction OR TITLE:retraction OR TITLE:withdrawn OR TITLE:"gen. nov." OR TITLE:"sp. nov." OR TITLE:"genome-wide identification")'
    """
    return build_query(
        select_query_terms(terms, max_terms=max_terms), date_from, date_to
    )


_ABBREV_SENTINEL = {
    "e.g.": "e<DOT>g<DOT>",
    "i.e.": "i<DOT>e<DOT>",
    "sp.": "sp<DOT>",
    "vs.": "vs<DOT>",
    "Fig.": "Fig<DOT>",
}


def split_sentences(text: str) -> list[str]:
    """Split text into sentences, protecting a few common abbreviations."""
    normalized = re.sub(r"\s+", " ", text).strip()
    if not normalized:
        return []
    for original, sentinel in _ABBREV_SENTINEL.items():
        normalized = normalized.replace(original, sentinel)
    out = []
    for part in re.split(r"(?<=[.!?])\s+", normalized):
        for original, sentinel in _ABBREV_SENTINEL.items():
            part = part.replace(sentinel, original)
        part = part.strip()
        if part:
            out.append(part)
    return out


def extract_signal_sentences(
    text: str, signal_groups: dict[str, tuple[str, ...]], max_signals: int = 6
) -> list[dict[str, object]]:
    """Return sentences containing any signal phrase, tagged with categories."""
    signals: list[dict[str, object]] = []
    seen: set[str] = set()
    for sentence in split_sentences(text):
        low = sentence.casefold()
        categories = [
            category
            for category, phrases in signal_groups.items()
            if any(phrase in low for phrase in phrases)
        ]
        if not categories:
            continue
        key = re.sub(r"[^a-z0-9]+", " ", low).strip()
        if key in seen:
            continue
        seen.add(key)
        signals.append({"categories": categories, "sentence": sentence})
        if len(signals) >= max_signals:
            break
    return signals
