#!/usr/bin/env python3
"""Find literature-based annotations whose cited paper may be about a different gene.

UniProt lists the papers it used for each entry (``RX   PubMed=`` lines). When an
experimental or author-statement GOA row (EXP, IDA, IPI, IMP, IGI, IEP, TAS, NAS)
cites a paper that the annotated protein's own entry does not cite, but another
reviewed UniProt entry does, the paper may have studied that
other protein: a paralog, a protein sharing a gene symbol, or a different gene
altogether. ``genes/human/CSGALNACT1`` is the motivating case: ten rows cite
PMID:11514575, which cloned chondroitin synthase CHSY1 (Q86X52), and only CHSY1's
entry cites it.

The output is a ranked lead list for review, never a verdict. UniProt does not cite
every relevant paper, and a paper can study several genes. Two confounders are
removed or penalised:

- An entry for the *same gene* in the same species (an unreviewed or secondary entry
  annotated while the reviewed one cites the paper) is not a different gene, so such
  citing entries are dropped.
- A paper that names the annotated gene in its cached title or abstract probably did
  study it (papers on several paralogs are common), so the lead is penalised.

Leads rank higher for a paralog in the same species, another gene in the same
species, the same-named gene in another species (an annotation transferred across
species with a direct evidence code), few citing entries, and an abstract that does
not name the annotated gene. Papers cited by many reviewed entries are treated as
large-scale and skipped, as are bare protein-binding rows.

>>> own = GeneRecord("P1", "9606", frozenset({"PTHR1"}), frozenset({"ABC1"}), frozenset())
>>> other = CitingEntry("P2", "ABC2", "9606", frozenset({"PTHR1"}))
>>> score_lead(own, [other], abstract_names_gene=False)
(6, 'same_taxon_paralog;few_citing_entries;gene_not_named_in_abstract')
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import unicodedata
import urllib.parse
from collections import Counter
from dataclasses import dataclass, replace
from functools import cache
from pathlib import Path
import sys
from typing import Any, Iterable, NamedTuple

import yaml

from ai_gene_review.evidence import (
    LITERATURE_EVIDENCE_CODES as LITERATURE_CODES,
    source_evidence_code,
)

from ai_gene_review.tools.function_requirements import REPO_ROOT, _get, _write_tsv

PUBLICATIONS_DIR = REPO_ROOT / "publications"

REPORT_DIR = REPO_ROOT / "reports" / "wrong-gene-leads"
CACHE_DIR = REPO_ROOT / ".cache" / "wrong-gene-leads"
UNIPROT_STREAM = "https://rest.uniprot.org/uniprotkb/stream"

# Low-throughput experimental codes, plus author statements (TAS, NAS) that cite a
# paper: both are curated from a specific publication, so both can be attached to
# the wrong gene. High-throughput papers are skipped.
# A paper cited by more reviewed entries than this, after entries for the annotated
# gene itself are dropped, is treated as large-scale.
MAX_CITING_ENTRIES = 20
BATCH_SIZE = 40
# Bare protein binding is removed by policy regardless of gene, so it is skipped.
SKIPPED_TERMS = frozenset({"GO:0005515"})
# Protein names with only this evidence are unvetted predictions (ARBA rules,
# submitter text), so they are not used to decide whether an abstract names a gene.
UNVETTED_NAME_EVIDENCE = ("ECO:0000256|ARBA", "ECO:0000313")
# PomBase gene names and synonyms, keyed by UniProt accession. UniProt's GN lines
# omit old genetic names that fission yeast papers use (glu3 for idh1).
POMBASE_NAMES = (
    REPO_ROOT
    / "projects/PROTNLM_EVALUATION/pombe-benchmark/snapshot/pombase-identifiers.tsv"
)
POMBE_TAXON = "284812"
# A range such as AKR1C1-AKR1C4 or AKR1C1-4 is expanded only up to this many names.
MAX_RANGE = 20
# A row whose source gave the same term from the same paper to at least this many
# gene folders here is a complex-wide or list annotation (every subunit of a
# complex, every protein of a proteomics list), not a single-gene claim.
SHARED_ANNOTATION_GENES = 4
ShareKey = tuple[str, str, str]


@dataclass(frozen=True)
class GeneRecord:
    """What the annotated protein's own UniProt entry says about it."""

    accession: str
    taxon: str
    panther_families: frozenset[str]
    gene_names: frozenset[str]
    cited_pmids: frozenset[str]
    protein_names: frozenset[str] = frozenset()


@dataclass(frozen=True)
class CitingEntry:
    """A reviewed UniProt entry that cites a given paper."""

    accession: str
    gene: str
    taxon: str
    panther_families: frozenset[str]
    protein_names: frozenset[str] = frozenset()


def parse_uniprot_flatfile(text: str) -> GeneRecord:
    """Read accession, taxon, PANTHER families, gene names and cited PMIDs.

    >>> r = parse_uniprot_flatfile(
    ...     "AC   Q8TDX6; Q8N1A2;\\nGN   Name=CSGALNACT1; Synonyms=CSGALNACT;\\n"
    ...     "OX   NCBI_TaxID=9606;\\nRX   PubMed=11788602;\\n"
    ...     "DR   PANTHER; PTHR12369:SF11; X; 1.\\nDR   PANTHER; PTHR12369; Y; 1.\\n")
    >>> r.accession, r.taxon, sorted(r.gene_names), sorted(r.panther_families), sorted(r.cited_pmids)
    ('Q8TDX6', '9606', ['CSGALNACT', 'CSGALNACT1'], ['PTHR12369'], ['11788602'])
    """
    accession = ""
    taxon = ""
    families: set[str] = set()
    gn_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("AC   ") and not accession:
            accession = line[5:].split(";")[0].strip()
        elif line.startswith("OX   ") and not taxon:
            m = re.search(r"NCBI_TaxID=(\d+)", line)
            taxon = m.group(1) if m else ""
        elif line.startswith("GN   "):
            gn_lines.append(line[5:])
        elif line.startswith("DR   PANTHER; "):
            families.add(line.split(";")[1].strip().split(":")[0])
    # GN entries wrap across lines (a synonym list can continue on the next line),
    # so parse the joined block with evidence braces removed.
    gn = re.sub(r"\{[^}]*\}", "", " ".join(gn_lines))
    names: set[str] = set()
    for m in re.finditer(r"(?:Name|Synonyms|OrderedLocusNames|ORFNames)=([^;]+)", gn):
        names.update(n.strip() for n in m.group(1).split(","))
    pmids = frozenset(re.findall(r"PubMed=(\d+)", text))
    return GeneRecord(
        accession,
        taxon,
        frozenset(families),
        frozenset(n for n in names if n),
        pmids,
        parse_protein_names(text),
    )


def parse_protein_names(text: str) -> frozenset[str]:
    """Curated recommended and alternative protein names from ``DE`` lines.

    Submitted names (``SubName``) and names whose only evidence is an ARBA rule or
    submitter text are unvetted, so they are left out.

    >>> sorted(parse_protein_names(
    ...     "DE   RecName: Full=Aurora kinase C;\\nDE            EC=2.7.11.1;\\n"
    ...     "DE   AltName: Full=Aurora 3 {ECO:0000303};\\nDE            Short=ARK-3;\\n"))
    ['ARK-3', 'Aurora 3', 'Aurora kinase C']
    >>> sorted(parse_protein_names(
    ...     "DE   RecName: Full=Glutamine synthetase {ECO:0000256|ARBA:ARBA00012937};\\n"
    ...     "DE   SubName: Full=Heat shock protein 70 {ECO:0000313|EMBL:CAA1};\\n"))
    []
    """
    names = set()
    for line in text.splitlines():
        if line.startswith("DE   ") and "SubName:" not in line:
            for m in re.finditer(r"(?:Full|Short)=([^;{]+)(\{[^}]*\})?", line):
                evidence = [
                    e.strip() for e in (m.group(2) or "").strip("{}").split(",")
                ]
                if m.group(2) and all(
                    e.startswith(UNVETTED_NAME_EVIDENCE) for e in evidence
                ):
                    continue
                names.add(m.group(1).strip())
    return frozenset(n for n in names if n and "uncharacterized" not in n.lower())


def parse_protein_names_field(field: str) -> frozenset[str]:
    """Protein names from UniProt's TSV ``Protein names`` column.

    The recommended name comes first and each alternative name follows in
    parentheses; names may themselves contain parentheses.

    >>> sorted(parse_protein_names_field("Tubulin alpha chain (EC 3.6.5.-) (Alpha-tubulin 2)"))
    ['Alpha-tubulin 2', 'EC 3.6.5.-', 'Tubulin alpha chain']
    >>> sorted(parse_protein_names_field(
    ...     "Guanine nucleotide-binding protein G(i) subunit alpha-1 (Adenylate cyclase-inhibiting G alpha protein (Gi)) (Gi1)"))
    ['Adenylate cyclase-inhibiting G alpha protein (Gi)', 'Gi1', 'Guanine nucleotide-binding protein G(i) subunit alpha-1']
    """
    names: list[str] = []
    depth = 0
    current = ""
    for ch in field:
        # A top-level " (" opens an alternative name; other parentheses belong
        # to the name being read.
        if ch == "(" and depth == 0 and current.endswith(" "):
            names.append(current)
            current = ""
            depth = 1
            continue
        if ch == "(" and depth:
            depth += 1
        elif ch == ")" and depth:
            depth -= 1
            if depth == 0:
                names.append(current)
                current = ""
                continue
        current += ch
    names.append(current)
    return frozenset(n.strip() for n in names if n.strip())


def _fold(text: str) -> str:
    """Drop diacritics, so "Spätzle" reads "Spatzle".

    >>> _fold("Spätzle")
    'Spatzle'
    """
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch))


def _norm(token: str) -> str:
    """Upper-case and strip non-alphanumerics, so ``GDI/D4`` matches ``GDID4``."""
    return re.sub(r"[^A-Z0-9]", "", _fold(token).upper())


_RANGE = re.compile(r"([A-Z0-9]*[A-Z])(\d+)[-\u2013](?:\1)?(\d+)")


def token_forms(token: str) -> set[str]:
    """The normalised names a whitespace token can stand for.

    Besides the whole token, each part between slashes or hyphens counts
    ("lsd1+/fas2+", "c-Abl", "Cds1p-dependent"), a protein suffix ``p`` is dropped
    from a name ending in a digit (the yeast convention, "Cds1p"; for any species,
    since the wanted names it could produce are at least three characters), and a
    numbered range of at most ``MAX_RANGE`` names is expanded ("AKR1C1-AKR1C4",
    "AKR1C1-4"). A span written between two different genes ("Smad1-Smad5") is
    expanded too, so interior members count as named.

    >>> sorted(token_forms("lsd1+/fas2+"))
    ['FAS2', 'LSD1', 'LSD1FAS2']
    >>> sorted(token_forms("Cds1p-dependent"))
    ['CDS1', 'CDS1P', 'CDS1PDEPENDENT', 'DEPENDENT']
    >>> sorted(token_forms("(AKR1C1-AKR1C3)"))
    ['AKR1C1', 'AKR1C1AKR1C3', 'AKR1C2', 'AKR1C3']
    """
    raw = _fold(token).strip("()[]{},.;:'\"")
    forms = {_norm(raw)} | {_norm(part) for part in re.split(r"[/\-\u2013]", raw)}
    m = _RANGE.fullmatch(raw.upper())
    if m:
        start, end = int(m.group(2)), int(m.group(3))
        if start < end and end - start < MAX_RANGE:
            forms |= {f"{m.group(1)}{n}" for n in range(start, end + 1)}
    forms |= {f[:-1] for f in forms if re.fullmatch(r"[A-Z][A-Z0-9]*\dP", f)}
    return {f for f in forms if f}


def same_gene_symbol(symbol: str, names: Iterable[str]) -> bool:
    """Whether a gene symbol is one of ``names``, ignoring case and punctuation.

    UniProt writes mouse and rat symbols in title case (``Arhgdib``) and human
    symbols in upper case (``ARHGDIB``).

    >>> same_gene_symbol("Arhgdib", {"ARHGDIB", "GDIR2"}), same_gene_symbol("Arhgdia", {"ARHGDIB"})
    (True, False)
    """
    return _norm(symbol) in {_norm(n) for n in names}


def _phrase(text: str) -> str:
    """Lower-case and turn punctuation into spaces, so "Filamin-C" reads "filamin c"."""
    return (
        " " + " ".join(re.sub(r"[^a-z0-9,]+", " ", _fold(text).lower()).split()) + " "
    )


class NameForm(NamedTuple):
    """One form of a protein name to look for in an abstract.

    ``word`` marks the bare X of a one-word "Protein X" name when X is a plain
    alphabetic word. Such names are often ordinary words ("Protein similar",
    "Protein rolled", "Protein Tube"), so X counts only when written capitalised
    and not at the start of a sentence. An X with a digit, a hyphen or an inner
    capital ("jagged-1", "FAM10A1", "GrpE") cannot be prose and is matched as an
    ordinary phrase.
    """

    text: str
    word: bool = False


def protein_name_forms(name: str) -> set[NameForm]:
    """A protein name plus the shorter forms papers use for it.

    A one-word "Protein X" name (common for fly and plant genes) is also matched as
    X, and a trailing one-word qualifier after a comma is dropped.

    >>> sorted(f.text for f in protein_name_forms("Protein breathless"))
    ['Protein breathless', 'breathless']
    >>> sorted(f.text for f in protein_name_forms("Very long-chain acyl-CoA dehydrogenase, mitochondrial"))
    ['Very long-chain acyl-CoA dehydrogenase', 'Very long-chain acyl-CoA dehydrogenase, mitochondrial']
    >>> sorted(f.text for f in protein_name_forms("Protein kinase C"))
    ['Protein kinase C']
    >>> sorted(protein_name_forms("Protein jagged-1"))
    [NameForm(text='Protein jagged-1', word=False), NameForm(text='jagged-1', word=False)]
    """
    forms = {NameForm(name)}
    m = re.fullmatch(r"Protein (\S+)", name)
    if m:
        short = _fold(m.group(1))
        forms.add(NameForm(m.group(1), word=short.isalpha() and short[1:].islower()))
    base, sep, tail = name.rpartition(", ")
    if sep and " " not in tail:
        forms.add(NameForm(base))
    return forms


def _capitalised_words(text: str) -> set[str]:
    """Capitalised words that do not start a sentence, split at slashes and hyphens.

    Any token ending in ".", "!", "?" or ":" counts as a sentence end, so a word
    after "et al." or "Fig." is skipped, and so is the first word of an abstract
    after a title ending in ".". Both errors keep leads rather than hiding them, so
    the check is not exhaustive. A Title-Case title is skipped entirely
    (``_skip_title_case_title``).

    >>> sorted(_capitalised_words("Similar results. We find that Similar and Tango-bound Spätzle act."))
    ['Similar', 'Spatzle', 'Tango']
    """
    words: set[str] = set()
    previous = "."
    for token in _fold(text).split():
        if not previous.endswith((".", "!", "?", ":")):
            for part in re.split(r"[/\-\u2013]", token):
                part = part.strip("()[]{},.;:'\"")
                if part[:1].isupper() and part[1:].islower():
                    words.add(part)
        previous = token
    return words


def _skip_title_case_title(text: str) -> str:
    """Drop a leading Title-Case title, whose capitals say nothing about names.

    ``abstract_text`` puts the title first, as its own paragraph. A title in which
    most words of four or more letters are capitalised is dropped, together with
    the copy of it that many cached abstracts repeat at the start of the body.

    >>> _skip_title_case_title("Interaction between SWP9 and Polar Tube Proteins\\n\\nThe body.")
    'The body.'
    >>> _skip_title_case_title("Polar Tube Proteins.\\n\\nPolar Tube\\nProteins. The body.")
    'The body.'
    >>> _skip_title_case_title("Breathless signalling in the trachea\\n\\nThe body.")
    'Breathless signalling in the trachea\\n\\nThe body.'
    """
    title, sep, body = text.partition("\n\n")
    words = [w for w in title.split() if len(w) >= 4 and w.isalpha()]
    if not (sep and words and sum(w[0].isupper() for w in words) > len(words) / 2):
        return text
    # Drop the repeated title from the body, matching it word by word across
    # line breaks. Only word positions matter downstream, so words are rejoined.
    title_words = [w.strip(".") for w in title.split()]
    body_words = body.split()
    n = len(title_words)
    if [w.strip(".") for w in body_words[:n]] == title_words:
        return " ".join(body_words[n:])
    return body


def _names_protein(text: str, name: str) -> bool:
    """Whether a protein name occurs in phrase-normalised text.

    A name whose last word is a short qualifier ("Aurora kinase C") also matches an
    enumeration of the family ("aurora kinases A, B, and C").

    >>> t = _phrase("The aurora kinases A, B, and C are serine/threonine kinases.")
    >>> _names_protein(t, "Aurora kinase C"), _names_protein(t, "Aurora kinase D")
    (True, False)
    >>> _names_protein(_phrase("expression of Filamin C in muscle"), "Filamin-C")
    True
    """
    words = _phrase(name).replace(",", " ").split()
    if len(" ".join(words)) < 6:
        return False
    if " " + " ".join(words) + " " in text.replace(",", " ").replace("  ", " "):
        return True
    if len(words) >= 2 and len(words[-1]) <= 2:
        stem = r"\s+".join(re.escape(w) for w in words[:-1])
        # _phrase leaves single spaces between words and keeps commas attached,
        # so each listed item is a whole 1-2 character word, e.g. "a, b, and c".
        item = r"[a-z0-9]{1,2},? (?:(?:and|or) )?"
        pattern = rf" {stem}s? (?:{item})*{re.escape(words[-1])},? "
        return re.search(pattern, text) is not None
    return False


# A PubMed author list: comma-separated "Surname INITIALS" items, the first one
# often carrying an affiliation marker, e.g. "Faiyaz ul Haque M(1), King LM, Cohn DH."
_AUTHOR = re.compile(
    r"[^\W\d][\w'.\- ]* [A-Z]{1,4}(?: (?:Jr|Sr|2nd|3rd|4th|II|III|IV))?"
    r"(?:\(\d+(?:,\d+)*\))*"
)
# A group author in a byline ("ADHR Consortium", "GTEx Consortium").
_GROUP_WORDS = (
    r"Consortium|Collaborators|Investigators|Committee|Collective Author|Group|"
    r"Network|Team|Study|Studies|Project|Program|Programme|Initiative"
)
_GROUP_TAIL = r"\b[\w'.\- ]*(?:\(\d+(?:,\d+)*\))*"
# A group author in a byline ("ADHR Consortium", "GTEx Consortium"); "Collective
# Author" is NCBI's placeholder for an unnamed group. The group word must be
# capitalised, so a sentence such as "In the pilot study, ..." is not a byline.
_GROUP_AUTHOR = re.compile(rf"(?:The )?[\w'.\- ]*\b(?:{_GROUP_WORDS}){_GROUP_TAIL}")
# PubMed puts a group author after a semicolon. There, and only there, an
# unambiguous group word may be lower case ("Lambert JC; GERAD consortium").
_GROUP_AFTER_SEMICOLON = re.compile(
    rf"(?:The )?[\w'.\- ]*\b(?i:Consortium|Collaborators|Investigators|Committee|"
    rf"Collective Author){_GROUP_TAIL}"
)


def _is_author_list(paragraph: str) -> bool:
    """Whether a paragraph is a PubMed author list.

    Each comma-separated item is tested on its own, which keeps a long byline that
    ends in a consortium name from backtracking through every split.

    >>> _is_author_list("Faiyaz ul Haque M(1), King LM, Superti-Furga A, Cohn DH.")
    True
    >>> _is_author_list("Ke Y(1)(2), Butt AG, et al.")
    True
    >>> _is_author_list("Rousset R(1), Mack JA, Wharton KA Jr, Scott MP.")
    True
    >>> _is_author_list("Smith J, Lee K, ADHR Consortium.")
    True
    >>> _is_author_list("Cook LS, Brooks-Wilson A; Ovarian Cancer Association Consortium.")
    True
    >>> _is_author_list("Brandstatter I(1), Kieber JJ; New Collective Author.")
    True
    >>> _is_author_list("Harold D, Lambert JC; GERAD consortium.")
    True
    >>> _is_author_list("ENaC is regulated by Nedd4-2, which binds PY motifs.")
    False
    >>> _is_author_list("In the pilot study, cells were analyzed by FACS.")
    False
    >>> _is_author_list("In the consortium analysis, samples were typed by PCR.")
    False
    """
    # PubMed separates a trailing group author with a semicolon:
    # "... Brooks-Wilson A; Ovarian Cancer Association Consortium."
    parts = re.split(r"([,;]) ", paragraph.rstrip("."))
    # parts alternates item, separator, item, ...; pair each item with the
    # separator before it.
    items = list(zip(parts[::2], [None, *parts[1::2]]))
    if items[-1][0] in {"et al", "et al."}:
        items = items[:-1]
    people = [
        item
        for item, sep in items
        if not _GROUP_AUTHOR.fullmatch(item)
        and not (sep == ";" and _GROUP_AFTER_SEMICOLON.fullmatch(item))
    ]
    # A byline names at least one person; a lone group name is not enough to
    # tell it from a sentence.
    return bool(people) and all(_AUTHOR.fullmatch(i) for i in people)


# Paragraphs of a PubMed text record that are bibliographic, not the abstract.
_RECORD_PARAGRAPH = re.compile(
    r"^(?:\d+\. \S|Author information:|Collaborators:|DOI:|PMID:|PMCID:|Copyright|©|"
    r"Comment in|Comment on|Erratum in|Update of|Conflict of interest)"
)


def strip_bibliographic(text: str) -> str:
    """Drop citation, author, affiliation and identifier paragraphs.

    These repeat surnames and institutions, so a gene symbol that is also a
    surname ("Mak") would otherwise read as the gene being named.

    >>> strip_bibliographic("1. Nat Genet. 1998.\\n\\nTitle.\\n\\nMak T(1), Lee AB.\\n\\n"
    ...                     "Author information:\\n(1)Mak Lab.\\n\\nBody text.\\n\\nPMID: 1")
    'Title.\\n\\nBody text.'
    """
    kept = []
    for para in re.split(r"\n\s*\n", text):
        flat = " ".join(para.split())
        if flat and not _RECORD_PARAGRAPH.match(flat) and not _is_author_list(flat):
            kept.append(para.strip())
    return "\n\n".join(kept)


def abstract_text(path: Path) -> str:
    """The title and abstract of a cached publication, without bibliographic text.

    The title comes from the front matter (or the ``# `` heading). The abstract is
    read from:

    - ``## Abstract``, up to the next section heading;
    - ``## Content`` in an abstract-only record (front matter
      ``content_type: abstract_only``);
    - ``## Content`` in a full-text record that opens with the PubMed text block,
      up to the block's ``DOI:``/``PMCID:``/``PMID:`` trailer, after which the
      article body starts.

    Other full-text ``## Content`` records do not mark where their abstract ends,
    so only the title is used for them.

    >>> import tempfile
    >>> with tempfile.TemporaryDirectory() as tmp:
    ...     p = Path(tmp) / "PMID_1.md"
    ...     _ = p.write_text("---\\ntitle: T\\nauthors:\\n- Mak T\\n---\\n\\n# T\\n"
    ...                      "**Authors:** Mak T\\n\\n## Abstract\\n\\nA\\n\\n## Methods\\nM")
    ...     q = Path(tmp) / "PMID_2.md"
    ...     _ = q.write_text("---\\ntitle: T\\ncontent_type: abstract_only\\n---\\n"
    ...                      "## Content\\n\\nMak T(1).\\n\\nB")
    ...     r = Path(tmp) / "PMID_3.md"
    ...     _ = r.write_text("---\\ncontent_type: full_text_xml\\n---\\n# T\\n## Content\\n\\n"
    ...                      "1. J. 2000.\\n\\nC\\n\\nDOI: 10.1/x\\nPMID: 3\\n\\nBody")
    ...     s = Path(tmp) / "PMID_4.md"
    ...     _ = s.write_text("---\\ntitle: T\\ncontent_type: full_text_xml\\n---\\n"
    ...                      "## Content\\n\\nAbstract and body")
    ...     abstract_text(p), abstract_text(q), abstract_text(r), abstract_text(s)
    ('T\\n\\nA', 'T\\n\\nB', 'T\\n\\nC', 'T')
    """
    text = path.read_text(errors="replace")
    meta: dict[str, Any] = {}
    if text.startswith("---\n"):
        front, _, text = text[4:].partition("\n---\n")
        loaded = yaml.safe_load(front)
        meta = loaded if isinstance(loaded, dict) else {}
    title = str(meta.get("title") or "")
    if not title and (m := re.search(r"(?m)^# (.+)$", text)):
        title = m.group(1).strip()
    body = ""
    for heading in ("## Abstract", "## Content"):
        start = text.find(heading)
        if start < 0:
            continue
        start += len(heading)
        end = text.find("\n## ", start)
        body = text[start : end if end >= 0 else None]
        if heading == "## Content" and meta.get("content_type") != "abstract_only":
            trailer = re.search(r"(?m)^(?:DOI|PMCID|PMID): ", body)
            # The PubMed text block opens with a numbered citation line carrying
            # the year ("1. Proc Natl Acad Sci U S A. 1999 May 25;..."). Without
            # it the trailer search could run into a full text's references.
            pubmed_block = re.match(r"\s*\d+\. \S[^\n]*\b(?:19|20)\d\d\b", body)
            body = body[: trailer.start()] if trailer and pubmed_block else ""
        break
    parts = [title, strip_bibliographic(body)]
    return "\n\n".join(p for p in parts if p)


def named_in_abstract(
    pmid: str,
    names: Iterable[str],
    publications_dir: Path = PUBLICATIONS_DIR,
    protein_names: Iterable[str | NameForm] = (),
) -> bool | None:
    """Whether the cached title or abstract names the gene or its protein.

    Returns None when the paper is not cached. Gene names are matched against the
    forms of each whitespace token (``token_forms``: slash and hyphen parts, a
    dropped ``p`` suffix, expanded ranges), after normalisation; names shorter than
    three characters are ignored. Protein names are expanded to their short forms
    (``protein_name_forms``) unless already given as ``NameForm`` values, and
    matched as phrases, or as a capitalised word for a one-word short form.

    >>> import tempfile
    >>> tmp = tempfile.TemporaryDirectory()
    >>> d = Path(tmp.name)
    >>> _ = (d / "PMID_1.md").write_text("title: X\\n## Abstract\\nGFP-tagged GDI/D4 was diffuse; aurora kinases A, B, and C.\\n## Full Text\\nCSGALNACT1")
    >>> named_in_abstract("1", ["GDID4"], d), named_in_abstract("1", ["CSGALNACT1"], d), named_in_abstract("2", ["X"], d)
    (True, False, None)
    >>> named_in_abstract("1", ["AURKC"], d, ["Aurora kinase C"])
    True
    >>> tmp.cleanup()
    """
    path = publications_dir / f"PMID_{pmid}.md"
    if not path.exists():
        return None
    text = abstract_text(path)
    tokens = {form for tok in text.split() for form in token_forms(tok)}
    wanted = {_norm(n) for n in names}
    if {w for w in wanted if len(w) >= 3} & tokens:
        return True
    forms: set[NameForm] = set()
    for n in protein_names:
        forms |= {n} if isinstance(n, NameForm) else protein_name_forms(n)
    phrased = _phrase(text)
    words = (
        _capitalised_words(_skip_title_case_title(text))
        if any(f.word for f in forms)
        else set()
    )
    return any(
        _fold(f.text).capitalize() in words
        if f.word
        else _names_protein(phrased, f.text)
        for f in forms
    )


def gene_specific_names(
    own: GeneRecord, citing: Iterable[CitingEntry]
) -> set[NameForm]:
    """The forms of the annotated protein's names that no citing entry for another gene shares.

    Family-level names are often shared verbatim by paralogs ("Tubulin alpha
    chain"). An abstract using such a name does not say which paralog it studied,
    so it must not cancel the paralog signal. Both sides are expanded to their
    short forms first, so "Malate dehydrogenase, cytoplasmic" and "..., mitochondrial"
    share "Malate dehydrogenase". An ortholog with the same gene symbol sharing the
    name is the expected case, so it does not count.

    >>> own = GeneRecord("P1", "1", frozenset(), frozenset(), frozenset(),
    ...                  frozenset({"Tubulin alpha chain", "Alpha-tubulin 1"}))
    >>> other = CitingEntry("P2", "TUA2", "1", frozenset(), frozenset({"Tubulin alpha chain"}))
    >>> sorted(f.text for f in gene_specific_names(own, [other]))
    ['Alpha-tubulin 1']
    >>> mouse = CitingEntry("P3", "Tua1", "2", frozenset(), frozenset({"Tubulin alpha chain"}))
    >>> own = GeneRecord("P1", "1", frozenset(), frozenset({"TUA1"}), frozenset(),
    ...                  frozenset({"Tubulin alpha chain"}))
    >>> sorted(f.text for f in gene_specific_names(own, [mouse]))
    ['Tubulin alpha chain']
    """
    shared = {
        _phrase(f.text)
        for c in citing
        if not same_gene_symbol(c.gene, own.gene_names)
        for n in c.protein_names
        for f in protein_name_forms(n)
    }
    return {
        f
        for n in own.protein_names
        for f in protein_name_forms(n)
        if _phrase(f.text) not in shared
    }


def score_lead(
    own: GeneRecord,
    citing: list[CitingEntry],
    abstract_names_gene: bool | None,
    shared_genes: int = 1,
) -> tuple[int, str]:
    """Score how likely the cited paper is about one of the citing entries instead.

    A paralog in the same species +3, another gene in the same species +2, the
    same-named gene in another species +2, three or fewer citing entries +1, and an
    abstract that does not name the annotated gene +2 (or -3 if it does). A row
    whose source gave it to ``SHARED_ANNOTATION_GENES`` or more local genes -2.
    """
    reasons = []
    score = 0
    same_taxon = [c for c in citing if c.taxon == own.taxon]
    if any(c.panther_families & own.panther_families for c in same_taxon):
        score += 3
        reasons.append("same_taxon_paralog")
    elif same_taxon:
        score += 2
        reasons.append("same_taxon_other_gene")
    if any(
        c.taxon != own.taxon and same_gene_symbol(c.gene, own.gene_names)
        for c in citing
    ):
        score += 2
        reasons.append("same_gene_other_species")
    if len(citing) <= 3:
        score += 1
        reasons.append("few_citing_entries")
    if abstract_names_gene is False:
        score += 2
        reasons.append("gene_not_named_in_abstract")
    elif abstract_names_gene:
        score -= 3
        reasons.append("gene_named_in_abstract")
    if shared_genes >= SHARED_ANNOTATION_GENES:
        score -= 2
        reasons.append("shared_by_many_genes")
    return score, ";".join(reasons)


def _share_key(row: dict[str, str]) -> ShareKey:
    return (
        row.get("REFERENCE") or "",
        row.get("GO TERM") or "",
        row.get("ASSIGNED BY") or "",
    )


def shared_annotation_counts(gene_dirs: Iterable[Path]) -> Counter[ShareKey]:
    """How many of the given gene folders carry each (reference, GO term, assigned-by) row.

    Only the folders passed in are counted, so a sweep of one species or one gene
    sees fewer shared rows than the default sweep of every folder. Only literature
    references are counted; GO_REF rows are shared by design.
    """
    counts: Counter[ShareKey] = Counter()
    for gene_dir in gene_dirs:
        keys: set[ShareKey] = set()
        for goa in gene_dir.glob("*-goa.tsv"):
            with goa.open() as fh:
                for row in csv.DictReader(fh, delimiter="\t"):
                    key = _share_key(row)
                    if key[0].startswith("PMID:"):
                        keys.add(key)
        counts.update(keys)
    return counts


@cache
def pombase_names(path: Path = POMBASE_NAMES) -> dict[str, frozenset[str]]:
    """PomBase gene names and synonyms keyed by UniProt accession.

    Several PomBase genes can share one accession (the histone H4 genes), so their
    names are pooled. Returns an empty map, with a warning, when the snapshot is
    not present.
    """
    if not path.exists():
        print(f"warning: {path} not found; no PomBase synonyms used", file=sys.stderr)
        return {}
    names: dict[str, frozenset[str]] = {}
    with path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            found = {row["gene_name"] or "", *(row["synonyms"] or "").split(",")}
            acc = row["external_id"]
            names[acc] = names.get(acc, frozenset()) | {
                n.strip() for n in found if n.strip()
            }
    return names


def candidate_rows(gene_dir: Path) -> tuple[GeneRecord, list[dict[str, str]]] | None:
    """Literature-based GOA rows citing a PMID that the gene's own UniProt entry does not."""
    uniprot = list(gene_dir.glob("*-uniprot.txt"))
    goa = list(gene_dir.glob("*-goa.tsv"))
    if not uniprot or not goa:
        return None
    own = parse_uniprot_flatfile(uniprot[0].read_text(errors="replace"))
    if own.taxon == POMBE_TAXON:
        own = replace(
            own, gene_names=own.gene_names | pombase_names().get(own.accession, set())
        )
    rows = []
    with goa[0].open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            ref = row.get("REFERENCE") or ""
            if (
                source_evidence_code(row.get("GO EVIDENCE CODE"), row.get("ECO ID"))
                in LITERATURE_CODES
                and ref.startswith("PMID:")
                and ref[5:] not in own.cited_pmids
                and row.get("GO TERM") not in SKIPPED_TERMS
                and not (row.get("QUALIFIER") or "").startswith("NOT")
            ):
                rows.append(row)
    return own, rows


def parse_citing_tsv(text: str, pmids: Iterable[str]) -> dict[str, list[CitingEntry]]:
    """Map each queried PMID to the entries in a UniProt TSV result that cite it.

    >>> tsv = ("Entry\\tProtein names\\tGene Names (primary)\\tOrganism (ID)\\tPubMed ID\\tPANTHER\\n"
    ...        "Q86X52\\tChondroitin sulfate synthase 1 (EC 2.4.1.175)\\tCHSY1\\t9606\\t11514575; 10231032\\tPTHR12369:SF42;PTHR12369;\\n")
    >>> out = parse_citing_tsv(tsv, ["11514575", "9113980"])
    >>> [c.accession for c in out["11514575"]], out["9113980"]
    (['Q86X52'], [])
    >>> sorted(out["11514575"][0].protein_names)
    ['Chondroitin sulfate synthase 1', 'EC 2.4.1.175']
    """
    wanted = set(pmids)
    out: dict[str, list[CitingEntry]] = {p: [] for p in wanted}
    for row in csv.DictReader(text.splitlines(), delimiter="\t"):
        families = frozenset(f.split(":")[0] for f in row["PANTHER"].split(";") if f)
        entry = CitingEntry(
            row["Entry"],
            row["Gene Names (primary)"],
            row["Organism (ID)"],
            families,
            parse_protein_names_field(row["Protein names"]),
        )
        for pmid in {p.strip() for p in row["PubMed ID"].split(";")} & wanted:
            out[pmid].append(entry)
    return out


def fetch_citing_entries(
    pmids: Iterable[str], cache_dir: Path = CACHE_DIR
) -> dict[str, list[CitingEntry]]:
    """Reviewed UniProt entries citing each requested PMID, fetched in batches and cached.

    UniProt's ``lit_pubmed:`` search matches an entry's own references (its
    ``RX   PubMed=`` lines), not the computationally mapped bibliography, so the
    result is comparable with the flat file's citations.
    """
    wanted = set(pmids)
    # v2 adds protein names; the version keeps an older cache from being misread.
    cache = cache_dir / "citing-entries-v2.json"
    stored: dict[str, list[dict[str, Any]]] = (
        json.loads(cache.read_text()) if cache.exists() else {}
    )
    need = sorted(wanted - set(stored))
    fields = (
        "accession,protein_name,gene_primary,organism_id,lit_pubmed_id,xref_panther"
    )
    for i in range(0, len(need), BATCH_SIZE):
        batch = need[i : i + BATCH_SIZE]
        query = (
            "reviewed:true AND (" + " OR ".join(f"lit_pubmed:{p}" for p in batch) + ")"
        )
        params = urllib.parse.urlencode(
            {"query": query, "fields": fields, "format": "tsv"}
        )
        for pmid, entries in parse_citing_tsv(
            _get(f"{UNIPROT_STREAM}?{params}", "text/plain"), batch
        ).items():
            stored[pmid] = [
                {
                    "accession": e.accession,
                    "gene": e.gene,
                    "taxon": e.taxon,
                    "panther": sorted(e.panther_families),
                    "protein_names": sorted(e.protein_names),
                }
                for e in entries
            ]
        # Write a sibling file and rename it, so an interrupted run never leaves
        # an unreadable cache behind.
        cache.parent.mkdir(parents=True, exist_ok=True)
        partial = cache.with_suffix(f".{os.getpid()}.tmp")
        partial.write_text(json.dumps(stored))
        partial.replace(cache)
    return {
        p: [
            CitingEntry(
                e["accession"],
                e["gene"],
                e["taxon"],
                frozenset(e["panther"]),
                frozenset(e["protein_names"]),
            )
            for e in v
        ]
        for p, v in stored.items()
        if p in wanted
    }


ReviewKey = tuple[str, str, str, str]


def _review_index(gene_dir: Path) -> dict[ReviewKey, tuple[str, bool]]:
    """Map (term, evidence, reference, isoform) to (action, has WRONG_GENE_PRODUCT).

    NOT rows are left out, because they are never candidate rows; the isoform
    keeps isoform-specific rows that share a term and reference apart.
    """
    paths = list(gene_dir.glob("*-ai-review.yaml"))
    if not paths:
        return {}
    review = (
        yaml.load(
            paths[0].read_text(), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader)
        )
        or {}
    )
    index = {}
    for a in review.get("existing_annotations") or []:
        if a.get("negated"):
            continue
        r = a.get("review") or {}
        key = (
            str((a.get("term") or {}).get("id")),
            str(a.get("evidence_type")),
            str(a.get("original_reference_id")),
            str(a.get("isoform") or ""),
        )
        wrong_gene = any(
            d.get("defect_type") == "WRONG_GENE_PRODUCT"
            for d in r.get("source_defects") or []
        )
        index[key] = (str(r.get("action") or ""), wrong_gene)
    return index


def find_leads(
    gene_dirs: Iterable[Path],
    citing: dict[str, list[CitingEntry]] | None = None,
    cache_dir: Path = CACHE_DIR,
    publications_dir: Path = PUBLICATIONS_DIR,
) -> list[dict[str, Any]]:
    """Ranked wrong-gene leads for the GOA rows in the given gene folders.

    ``citing`` maps PMIDs to the entries citing them; when omitted it is fetched
    from UniProt for every candidate PMID.
    """
    gene_dirs = sorted(gene_dirs)
    shared = shared_annotation_counts(gene_dirs)
    candidates = [(d, c) for d in gene_dirs if (c := candidate_rows(d)) and c[1]]
    if citing is None:
        citing = fetch_citing_entries(
            {r["REFERENCE"][5:] for _, (_, rows) in candidates for r in rows}, cache_dir
        )
    leads: list[dict[str, Any]] = []
    for gene_dir, (own, rows) in candidates:
        index: dict[ReviewKey, tuple[str, bool]] | None = None
        for row in rows:
            # Drop the gene itself: the same accession, or the same-named gene in
            # the same species (a secondary entry for one gene is not a wrong gene).
            others = [
                c
                for c in citing.get(row["REFERENCE"][5:], [])
                if c.accession != own.accession
                and not (
                    c.taxon == own.taxon and same_gene_symbol(c.gene, own.gene_names)
                )
            ]
            if not others or len(others) > MAX_CITING_ENTRIES:
                continue
            if index is None:
                index = _review_index(gene_dir)
            product = row["GENE PRODUCT ID"]
            isoform = product if "-" in product else ""
            action, wrong_gene = index.get(
                (row["GO TERM"], row["GO EVIDENCE CODE"], row["REFERENCE"], isoform),
                ("", False),
            )
            score, reasons = score_lead(
                own,
                others,
                named_in_abstract(
                    row["REFERENCE"][5:],
                    own.gene_names,
                    publications_dir,
                    gene_specific_names(own, others),
                ),
                shared[_share_key(row)],
            )
            leads.append(
                {
                    "gene": f"{gene_dir.parent.name}/{gene_dir.name}",
                    "accession": own.accession,
                    "go_id": row["GO TERM"],
                    "go_label": row["GO NAME"],
                    "evidence": row["GO EVIDENCE CODE"],
                    "reference": row["REFERENCE"],
                    "assigned_by": row["ASSIGNED BY"],
                    "score": score,
                    "reasons": reasons,
                    "citing_entries": ";".join(
                        f"{c.accession}:{c.gene}" for c in others
                    ),
                    "review_action": action,
                    "wrong_gene_defect": wrong_gene,
                }
            )
    leads.sort(key=lambda r: (-r["score"], r["gene"], r["go_id"]))
    return leads


def main(argv: list[str] | None = None) -> None:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--genes-root", type=Path, default=REPO_ROOT / "genes")
    parser.add_argument("--out-dir", type=Path, default=REPORT_DIR)
    args = parser.parse_args(argv)
    leads = find_leads(args.genes_root.glob("*/*"))
    _write_tsv(args.out_dir / "leads.tsv", leads)
    reviewed = [r for r in leads if r["review_action"]]
    agreed = [
        r for r in reviewed if r["wrong_gene_defect"] or r["review_action"] == "REMOVE"
    ]
    print(f"{len(leads)} leads in {len({r['gene'] for r in leads})} genes")
    print(
        f"{len(reviewed)} on reviewed rows; {len(agreed)} already REMOVE or WRONG_GENE_PRODUCT"
    )
    for score, n in sorted(Counter(r["score"] for r in leads).items(), reverse=True):
        print(f"score {score}: {n}")


if __name__ == "__main__":
    main()
