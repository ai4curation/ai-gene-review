#!/usr/bin/env python3
"""Audit and repair BioReason-Pro SFT prediction reviews.

The repair is intentionally conservative. It only changes an assessment when an
exact current-GOA/AIGR join makes the existing category internally inconsistent,
or when the prediction is covered by a small, explicit biological override below.
Manual rationale text is retained for deterministic reclassifications. Raw model
GO identifiers and labels are never rewritten.

By default this audits the ARGO139 cohort's HuggingFace catalogue subset (ARGO95)
without writing files. Pass ``--apply`` to persist the reported repairs.
"""

from __future__ import annotations

import argparse
import copy
import csv
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, MutableMapping

import yaml as pyyaml
from ruamel.yaml import YAML

from ai_gene_review.bioreason_ontology import FROZEN_GO_ADAPTER, get_go_adapter


DEFAULT_COHORT = Path("projects/BIOREASON_COMPARISON/genes.csv")
DEFAULT_SOURCE_VERSION = "wanglab/protein_catalogue"
DEFAULT_ONTOLOGY_ADAPTER = FROZEN_GO_ADAPTER
ONTOLOGY_PAIR_AUDIT = (
    Path(__file__).resolve().parents[1]
    / "projects"
    / "BIOREASON_COMPARISON"
    / "argo95-ontology-pair-adjudication.tsv"
)

POSITIVE_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE"}
NEGATIVE_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
INCORRECT_ASSESSMENTS = {"NPI", "PLI", "REP"}
EXPECTED_CONFIDENCE = {
    "COR": 2,
    "CNN": 2,
    "LSP": 2,
    "UNC": 1,
    "PLI": 0,
    "NPI": 0,
    "REP": 0,
}

CURRENT_AUDIT_PREFIX = "Current-snapshot audit"
RETAINED_RATIONALE_PREFIX = "Retained biological rationale."
ONTOLOGY_NOTE_MARKER = "[ONTOLOGY_LABEL_AUDIT]"
ONTOLOGY_ADJUDICATION_MARKER = "[FROZEN_ONTOLOGY_ADJUDICATION]"


@dataclass(frozen=True)
class ManualOverride:
    """A manually adjudicated correction that cannot be inferred from exact joins."""

    assessment: str | None = None
    error_type: str | None = None
    set_error_type: bool = False
    summary: str | None = None
    replace_category_mentions: bool = False


@dataclass(frozen=True)
class OntologyPairDecision:
    """Manual judgment of a raw GO ID/label pair against the frozen ontology."""

    assessment: str
    error_type: str | None
    canonical_label: str
    basis: str


MANUAL_OVERRIDES: dict[tuple[str, str, str], ManualOverride] = {
    # cts2 is a GH18 pseudoenzyme: the catalytic glutamate is replaced by Asn.
    ("SCHPO", "cts2", "GO:0004568"): ManualOverride(
        assessment="NPI",
        error_type="PSEUDOENZYME_OVERANNOTATION",
        set_error_type=True,
        summary=(
            "Refuted despite its presence in GOA. The current AIGR review recommends "
            "REMOVE because cts2 lacks the conserved catalytic glutamate required for "
            "GH18 chitinase activity (E166 is replaced by Asn). The SFT call therefore "
            "recapitulates invalid phylogenetic propagation to a pseudo-chitinase and is "
            "NPI, not CNN."
        ),
    ),
    ("SCHPO", "cts2", "GO:0034232"): ManualOverride(
        assessment="NPI",
        error_type="PSEUDOENZYME_OVERANNOTATION",
        set_error_type=True,
        summary=(
            "Incorrect, not less precise: this term is more specific than the GOA chitin "
            "catabolic-process term, and both depend on chitinase catalysis. Because cts2 "
            "lacks the essential GH18 catalytic glutamate, fungal-type cell-wall chitin "
            "catabolism is refuted along with the catalytic premise."
        ),
    ),
    # The current AIGR retains the directly assayed reductase activity as non-core.
    ("ECOLI", "DnaJ", "GO:0015035"): ManualOverride(
        assessment="CNN",
        error_type=None,
        set_error_type=True,
        summary=(
            "Correct but not novel. GOA contains direct experimental evidence for DnaJ "
            "protein-disulfide reductase activity (PMID:11732919), and the current AIGR "
            "review retains it as KEEP_AS_NON_CORE. The activity is secondary and its "
            "physiological importance is uncertain, but those caveats do not make the "
            "experimentally demonstrated prediction incorrect."
        ),
    ),
    ("ECOLI", "DnaJ", "GO:0003756"): ManualOverride(
        error_type="CURATION_MISTAKE",
        set_error_type=True,
    ),
    # The worm HSP-90 protein itself was used in the cited interaction assay.
    ("worm", "hsp-90", "GO:0035259"): ManualOverride(
        assessment="CNN",
        error_type=None,
        set_error_type=True,
        summary=(
            "Correct but not novel. Current GOA records an exact IPI annotation from "
            "PMID:26593036, and the AIGR review ACCEPTS it because the experiment used "
            "C. elegans HSP-90 binding to a glucocorticoid receptor. The receptor is not "
            "claimed to be a worm ortholog, so this is not a taxon-constraint violation."
        ),
    ),
    # True paralog/subfamily substrate or biological-role misassignments.
    ("SCHPO", "alo1", "GO:0050105"): ManualOverride(
        assessment="PLI",
        error_type="PARALOG_OVERANNOTATION",
        set_error_type=True,
        replace_category_mentions=True,
    ),
    ("SCHPO", "alo1", "GO:0019853"): ManualOverride(
        assessment="PLI",
        error_type="PARALOG_OVERANNOTATION",
        set_error_type=True,
        replace_category_mentions=True,
    ),
    ("DROME", "LysB", "GO:0045824"): ManualOverride(
        assessment="PLI",
        error_type="PARALOG_OVERANNOTATION",
        set_error_type=True,
        replace_category_mentions=True,
    ),
    ("DROME", "LysB", "GO:0050829"): ManualOverride(
        assessment="PLI",
        error_type="PARALOG_OVERANNOTATION",
        set_error_type=True,
        replace_category_mentions=True,
    ),
    ("SCHPO", "SPAC8E11.10", "GO:0019677"): ManualOverride(
        assessment="PLI",
        error_type="PARALOG_OVERANNOTATION",
        set_error_type=True,
        replace_category_mentions=True,
    ),
    # These existing paralog tags describe other error mechanisms.
    ("BACSU", "comK", "GO:0005524"): ManualOverride(
        error_type=None,
        set_error_type=True,
    ),
    ("BACSU", "fliY", "GO:0030428"): ManualOverride(
        error_type="NAMING_INCONSISTENCY",
        set_error_type=True,
    ),
    ("DROME", "LysB", "GO:0004568"): ManualOverride(
        error_type=None,
        set_error_type=True,
    ),
    ("ECOLI", "DnaK", "GO:0008270"): ManualOverride(
        error_type=None,
        set_error_type=True,
    ),
    ("yeast", "HSP60", "GO:0005829"): ManualOverride(
        error_type="LOCALIZATION_DEFAULT",
        set_error_type=True,
    ),
    # Generic protein binding plus FREQUENCY_BIAS is a REP call, not a CNN call.
    ("DROME", "Git", "GO:0005515"): ManualOverride(
        assessment="REP",
        error_type="FREQUENCY_BIAS",
        set_error_type=True,
        replace_category_mentions=True,
    ),
    # RidA repeats overgeneralized GOA records rather than reflecting bad experiments.
    ("ECOLI", "RidA", "GO:0051082"): ManualOverride(
        error_type="CURATION_MISTAKE",
        set_error_type=True,
        summary=(
            "Unfolded protein binding is not a constitutive property of native RidA. "
            "RidA acquires holdase activity only after HOCl-mediated N-chlorination "
            "(PMID:25517874), and the AIGR review therefore marks the unconditional "
            "GO annotation as MARK_AS_OVER_ANNOTATED. The experiment itself is valid; "
            "the error is the curation-level loss of the required stress-dependent "
            "modification context, so CURATION_MISTAKE is more accurate than "
            "EXPERIMENTAL_MISTAKE."
        ),
    ),
    ("ECOLI", "RidA", "GO:0016020"): ManualOverride(
        error_type="CURATION_MISTAKE",
        set_error_type=True,
    ),
    # The generic transcription role is supported, but the hypoxia-specific claim is unresolved.
    ("human", "VEGFA", "GO:0061419"): ManualOverride(
        assessment="UNC",
        error_type=None,
        set_error_type=True,
        summary=(
            "Uncertain rather than refuted. Current GOA and the AIGR support VEGFA in "
            "positive regulation of RNA polymerase II transcription, but they do not "
            "resolve whether that role is specifically executed in response to hypoxia. "
            "The prior causal-reversal rationale was too strong because VEGFA signaling "
            "can activate downstream transcription; the narrower hypoxia context still "
            "requires expert confirmation."
        ),
    ),
    # Malformed ID/label pairs whose canonical GO IDs change the biological call.
    ("ARATH", "ETR1", "GO:0009731"): ManualOverride(
        assessment="NPI",
        error_type="NAMING_INCONSISTENCY",
        set_error_type=True,
        summary=(
            "The raw label describes ethylene detection, but the supplied GO:0009731 "
            "identifier is detection of sucrose stimulus. ETR1 is an ethylene receptor, "
            "not a sucrose sensor. The malformed pair is NPI when assessed by its GO ID; "
            "the raw label remains preserved for provenance."
        ),
    ),
    ("ARATH", "COP1", "GO:0060928"): ManualOverride(
        assessment="NPI",
        error_type="TAXON_CONSTRAINT_VIOLATION",
        set_error_type=True,
        summary=(
            "The raw label describes flavonoid biosynthesis, but GO:0060928 is "
            "atrioventricular node cell development. That animal cardiac-development "
            "term is taxonomically impossible for Arabidopsis COP1, so the malformed "
            "pair is NPI when assessed by its GO ID."
        ),
    ),
    ("BACSU", "fliY", "GO:0009374"): ManualOverride(
        assessment="NPI",
        error_type="NAMING_INCONSISTENCY",
        set_error_type=True,
        summary=(
            "The raw label says flagellar switch complex, but GO:0009374 is biotin "
            "binding. FliY is a flagellar switch phosphatase with no established biotin "
            "binding activity. The malformed pair is therefore NPI by its GO ID."
        ),
    ),
    ("BACSU", "sigK", "GO:0031381"): ManualOverride(
        assessment="NPI",
        error_type="TAXON_CONSTRAINT_VIOLATION",
        set_error_type=True,
        summary=(
            "The raw label says bacterial RNA polymerase holoenzyme, but GO:0031381 is "
            "viral RNA-directed RNA polymerase complex. A Bacillus sporulation sigma "
            "factor is not part of a viral polymerase complex, so the pair is NPI."
        ),
    ),
    ("ECOLI", "DnaJ", "GO:0006267"): ManualOverride(
        assessment="NPI",
        error_type="TAXON_CONSTRAINT_VIOLATION",
        set_error_type=True,
        summary=(
            "The raw label says DNA replication initiation, but GO:0006267 is nuclear "
            "pre-replicative-complex assembly. DnaJ has a secondary role in bacterial "
            "replication-complex remodeling, but E. coli has neither a nucleus nor the "
            "eukaryotic pre-replicative complex described by this GO ID."
        ),
    ),
    ("ECOLI", "DnaK", "GO:0070828"): ManualOverride(
        assessment="NPI",
        error_type="TAXON_CONSTRAINT_VIOLATION",
        set_error_type=True,
        summary=(
            "The raw label describes an unfolded-protein response, but GO:0070828 is "
            "heterochromatin organization. E. coli DnaK is a heat-shock chaperone and "
            "does not organize eukaryotic heterochromatin, so the pair is NPI."
        ),
    ),
    ("ECOLI", "mrdA", "GO:0008696"): ManualOverride(
        assessment="NPI",
        error_type="NAMING_INCONSISTENCY",
        set_error_type=True,
        summary=(
            "The raw label describes a D,D-peptidase, but GO:0008696 is "
            "4-amino-4-deoxychorismate lyase activity. MrdA/PBP2 is a peptidoglycan "
            "D,D-transpeptidase, not a chorismate-pathway lyase; the malformed pair is NPI."
        ),
    ),
    ("worm", "hsf-1", "GO:0061067"): ManualOverride(
        assessment="NPI",
        error_type="NAMING_INCONSISTENCY",
        set_error_type=True,
        summary=(
            "The raw label claims positive regulation of dauer development, whereas "
            "GO:0061067 is negative regulation. The original rationale supports the "
            "opposite direction and therefore cannot validate the supplied GO ID."
        ),
    ),
    ("worm", "hsp-90", "GO:1903615"): ManualOverride(
        assessment="NPI",
        error_type="NAMING_INCONSISTENCY",
        set_error_type=True,
        summary=(
            "The raw label describes activation of a serine/threonine phosphatase, but "
            "GO:1903615 is the obsolete tyrosine-phosphatase regulation term. Evidence "
            "for the PPH-5 serine/threonine phosphatase does not support that GO ID."
        ),
    ),
    # FREQUENCY_BIAS denotes the REP category. Remove speculative tags from NPI calls.
    ("AGKCO", "fibrolase", "GO:0005509"): ManualOverride(
        error_type=None, set_error_type=True
    ),
    ("AGKCO", "fibrolase", "GO:0000287"): ManualOverride(
        error_type=None, set_error_type=True
    ),
    ("ECOLI", "CnoX", "GO:0061077"): ManualOverride(
        assessment="LSP",
        error_type=None,
        set_error_type=True,
        summary=(
            "Less precise, not refuted. GOA and the AIGR directly support CnoX in "
            "protein refolding (GO:0042026): CnoX preserves substrates and hands them "
            "to the GroEL/DnaK foldases. The supplied historical chaperone-mediated "
            "protein-folding concept is broader and misses that specific handoff and "
            "refolding role."
        ),
    ),
    ("ECOLI", "Skp", "GO:0061077"): ManualOverride(
        assessment="CNN",
        error_type=None,
        set_error_type=True,
        summary=(
            "Correct but not novel under the curated reference. The replacement protein "
            "folding term (GO:0006457) has IBA, IDA, and IMP annotations in current GOA, "
            "and the AIGR accepts it. Skp acts as a holdase/carrier before OMP folding, "
            "but that mechanistic qualification does not justify overruling the positive "
            "experimental curation."
        ),
    ),
    ("ECOLI", "Spy", "GO:0014070"): ManualOverride(
        assessment="COR",
        error_type=None,
        set_error_type=True,
        summary=(
            "Correct novel biological response. Tannin, an organic cyclic polyphenol, "
            "strongly induces spy; Spy protects proteins during tannin stress, and spy-null "
            "cells are tannin-sensitive (PMID:21317898). The concept is supported but is "
            "absent as an exact term from current GOA. Its obsolete ontology status is "
            "reported separately from the COR assessment."
        ),
    ),
    ("ECOLI", "SlyD", "GO:0044008"): ManualOverride(
        error_type=None, set_error_type=True
    ),
    ("ECOLI", "CpxP", "GO:0044183"): ManualOverride(
        assessment="UNC",
        error_type=None,
        set_error_type=True,
        summary=(
            "Uncertain rather than refuted. CpxP has reported mild protein-chaperone "
            "activity, but its established core roles are CpxA inhibition and delivery "
            "of misfolded substrates to DegP. The available evidence does not establish "
            "a general protein-folding chaperone function, yet it also does not support "
            "a confident NPI call."
        ),
    ),
    ("ECOLI", "CpxP", "GO:0061077"): ManualOverride(
        assessment="UNC",
        error_type=None,
        set_error_type=True,
        summary=(
            "Uncertain rather than refuted. CpxP binds misfolded periplasmic proteins "
            "and has mild chaperone activity, but direct participation in productive "
            "protein folding is not established. Its adaptor role in DegP degradation "
            "does not by itself prove or disprove this broader process prediction."
        ),
    ),
    ("ECOLI", "CpxP", "GO:0014070"): ManualOverride(
        assessment="UNC",
        error_type=None,
        set_error_type=True,
        summary=(
            "Uncertain. CpxP is experimentally involved in envelope-stress responses, "
            "but the current evidence does not isolate an organic cyclic compound as "
            "the causal stimulus. Absence of an exact GOA annotation is not biological "
            "refutation, so NPI was too strong."
        ),
    ),
    ("ECOLI", "DnaK", "GO:0016021"): ManualOverride(
        error_type=None, set_error_type=True
    ),
    ("SCHPO", "tam10", "GO:0005515"): ManualOverride(
        assessment="REP",
        error_type="FREQUENCY_BIAS",
        set_error_type=True,
        summary=(
            "Generic protein binding is a high-frequency, uninformative default for an "
            "uncharacterized protein with no established interaction. This is REP rather "
            "than an evidence-refuted gene-specific mechanism."
        ),
    ),
    ("human", "FXN", "GO:0030307"): ManualOverride(
        error_type=None, set_error_type=True
    ),
    ("human", "FXN", "GO:0008284"): ManualOverride(
        error_type=None, set_error_type=True
    ),
    ("human", "NFE2L2", "GO:1903079"): ManualOverride(
        error_type=None, set_error_type=True
    ),
    ("human", "NFE2L2", "GO:0005794"): ManualOverride(
        error_type=None, set_error_type=True
    ),
    ("human", "NFE2L2", "GO:0090575"): ManualOverride(
        error_type=None, set_error_type=True
    ),
    ("human", "NFE2L2", "GO:0005813"): ManualOverride(
        error_type=None, set_error_type=True
    ),
    ("human", "CYCS", "GO:0032991"): ManualOverride(
        assessment="REP",
        error_type="FREQUENCY_BIAS",
        set_error_type=True,
        replace_category_mentions=True,
    ),
    ("human", "KEAP1", "GO:0034451"): ManualOverride(
        error_type=None, set_error_type=True
    ),
    ("human", "VEGFA", "GO:0032991"): ManualOverride(
        error_type=None, set_error_type=True
    ),
}


def load_ontology_pair_decisions(
    path: Path = ONTOLOGY_PAIR_AUDIT,
) -> dict[tuple[str, str, str, str], OntologyPairDecision]:
    """Load changed judgments from the committed blinded pair-adjudication table."""
    decisions: dict[tuple[str, str, str, str], OntologyPairDecision] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["change_required"] != "true":
                continue
            key = (row["species"], row["gene"], row["go_id"], row["raw_label"])
            decisions[key] = OntologyPairDecision(
                assessment=row["recommended_assessment"],
                error_type=row["recommended_error_type"] or None,
                canonical_label=row["canonical_label"],
                basis=row["recommendation_basis"],
            )
    return decisions


ONTOLOGY_PAIR_DECISIONS = load_ontology_pair_decisions()


@dataclass(frozen=True)
class LabelCheck:
    status: str
    canonical_label: str | None


@dataclass
class RepairStats:
    files_seen: int = 0
    files_changed: int = 0
    predictions_seen: int = 0
    predictions_changed: int = 0
    confidence_changes: int = 0
    error_type_changes: int = 0
    label_notes_changed: int = 0
    assessment_before: Counter[str] = field(default_factory=Counter)
    assessment_after: Counter[str] = field(default_factory=Counter)
    assessment_changes: Counter[tuple[str, str]] = field(default_factory=Counter)
    label_statuses: Counter[str] = field(default_factory=Counter)
    remaining_conflicts: Counter[str] = field(default_factory=Counter)


class OntologyLabelChecker:
    """Resolve canonical GO labels and aliases through one cached OAK adapter."""

    def __init__(self, adapter_spec: str = DEFAULT_ONTOLOGY_ADAPTER):
        self.adapter_spec = adapter_spec
        self.adapter = get_go_adapter(adapter_spec)
        self._cache: dict[tuple[str, str], LabelCheck] = {}

    @staticmethod
    def _normalize(label: str) -> str:
        return " ".join(label.split()).casefold()

    def check(self, go_id: str, raw_label: str) -> LabelCheck:
        key = (go_id, raw_label)
        if key in self._cache:
            return self._cache[key]

        canonical = self.adapter.label(go_id)
        if canonical is None:
            result = LabelCheck("UNRESOLVED", None)
        elif self._normalize(raw_label) == self._normalize(canonical):
            result = LabelCheck("MATCH", canonical)
        else:
            aliases = {
                self._normalize(alias)
                for alias in self.adapter.entity_aliases(go_id)
                if alias
            }
            status = "ALIAS" if self._normalize(raw_label) in aliases else "MISMATCH"
            result = LabelCheck(status, canonical)

        self._cache[key] = result
        return result


def load_goa_terms(goa_file: Path) -> set[str]:
    """Return exact GO identifiers in a local GOA TSV."""
    terms: set[str] = set()
    if not goa_file.exists():
        return terms
    with goa_file.open() as handle:
        for line in handle:
            parts = line.rstrip("\n").split("\t")
            if len(parts) > 4 and re.fullmatch(r"GO:\d{7}", parts[4]):
                terms.add(parts[4])
    return terms


def load_aigr_term_actions(review_file: Path) -> dict[str, set[str]]:
    """Return every AIGR action for each GO ID without flattening mixed decisions."""
    actions: dict[str, set[str]] = defaultdict(set)
    if not review_file.exists():
        return actions

    yaml = YAML(typ="safe")
    with review_file.open() as handle:
        doc = yaml.load(handle) or {}
    for annotation in doc.get("existing_annotations", []):
        go_id = annotation.get("term", {}).get("id", "")
        action = annotation.get("review", {}).get("action", "")
        if go_id.startswith("GO:") and action:
            actions[go_id].add(action)
    return actions


def load_aigr_core_terms(review_file: Path) -> set[str]:
    """Return GO IDs used in AIGR core functions."""
    terms: set[str] = set()
    if not review_file.exists():
        return terms

    yaml = YAML(typ="safe")
    with review_file.open() as handle:
        doc = yaml.load(handle) or {}
    def add_term_values(value: Any) -> None:
        values = value if isinstance(value, list) else [value]
        for term in values:
            if isinstance(term, dict) and term.get("id", "").startswith("GO:"):
                terms.add(term["id"])

    for core_function in doc.get("core_functions", []):
        for slot in (
            "molecular_function",
            "contributes_to_molecular_function",
            "directly_involved_in",
            "occurs_in",
            "locations",
            "in_complex",
        ):
            add_term_values(core_function.get(slot))
    return terms


def auto_assess(
    go_id: str,
    goa_terms: set[str],
    aigr_actions: dict[str, set[str]],
    aigr_core: set[str],
) -> tuple[str, int, str]:
    """Create a schema-valid initial assessment from exact local evidence."""
    actions = aigr_actions.get(go_id, set())

    if actions and actions <= NEGATIVE_ACTIONS:
        return (
            "NPI",
            0,
            "The exact AIGR actions are "
            f"{', '.join(sorted(actions))}; the prediction reproduces an annotation "
            "that the current review rejects or marks as over-annotated.",
        )
    if actions & POSITIVE_ACTIONS:
        return (
            "CNN",
            2,
            "The exact term is already present in AIGR with a positive action "
            f"({', '.join(sorted(actions & POSITIVE_ACTIONS))}). Correct but not novel.",
        )
    if go_id in goa_terms:
        if actions == {"MODIFY"}:
            return (
                "LSP",
                2,
                "The term is in GOA, but AIGR recommends MODIFY to a more appropriate "
                "term. It is retained as a less-precise prediction.",
            )
        return ("CNN", 2, "The exact term is present in current GOA. Correct but not novel.")
    if go_id in aigr_core:
        return (
            "COR",
            2,
            "The term is absent from current GOA but present in AIGR core functions. "
            "It is treated as a correct candidate relative to the local review.",
        )
    return (
        "UNC",
        1,
        "The term is absent from current GOA and is not resolved by an exact AIGR "
        "action or core-function match.",
    )


def deterministic_reclassification(
    go_id: str,
    current_assessment: str,
    goa_terms: set[str],
    actions: set[str],
) -> tuple[str, str] | None:
    """Return a correction only for an exact, unambiguous contradiction."""
    if actions and actions <= NEGATIVE_ACTIONS:
        if current_assessment in {"PLI", "REP"}:
            return None
        if go_id == "GO:0005515":
            return (
                "REP",
                "all exact AIGR actions reject or over-annotate generic protein binding",
            )
        if current_assessment != "NPI":
            return (
                "NPI",
                "all exact AIGR actions are negative "
                f"({', '.join(sorted(actions))})",
            )
        return None

    if actions & POSITIVE_ACTIONS and current_assessment in {"NPI", "UNC"}:
        return (
            "CNN",
            "the current AIGR contains a positive exact action "
            f"({', '.join(sorted(actions & POSITIVE_ACTIONS))})",
        )

    if go_id in goa_terms and current_assessment == "COR":
        return ("CNN", "the exact GO ID is already present in current local GOA")

    return None


def _plain_summary(summary: Any) -> str:
    """Remove earlier machine-added audit wrappers while retaining manual text."""
    text = str(summary or "").strip()
    if text.startswith(CURRENT_AUDIT_PREFIX) and RETAINED_RATIONALE_PREFIX in text:
        text = text.split(RETAINED_RATIONALE_PREFIX, 1)[1].strip()
    if ONTOLOGY_NOTE_MARKER in text:
        text = text.split(ONTOLOGY_NOTE_MARKER, 1)[0].rstrip()
    return text


def _without_ontology_note(summary: Any) -> str:
    """Remove only a prior ontology note, preserving assessment audit text."""
    text = str(summary or "").strip()
    if ONTOLOGY_NOTE_MARKER in text:
        text = text.split(ONTOLOGY_NOTE_MARKER, 1)[0].rstrip()
    return text


def _with_scalar_style(old_value: Any, new_value: str) -> Any:
    """Keep folded/literal scalar style when round-tripping hand-written YAML."""
    if type(old_value) is str:
        return new_value
    try:
        return type(old_value)(new_value)
    except (TypeError, ValueError):
        return new_value


def reclassified_summary(summary: Any, old: str, new: str, reason: str) -> Any:
    retained = _plain_summary(summary)
    updated = (
        f"{CURRENT_AUDIT_PREFIX} reclassified {old} to {new} because {reason}. "
        "This exact-join decision supersedes conflicting conclusions in the earlier "
        "rationale."
    )
    if retained:
        updated += f" {RETAINED_RATIONALE_PREFIX} {retained}"
    return _with_scalar_style(summary, updated)


def apply_label_note(
    review: MutableMapping[str, Any],
    go_id: str,
    raw_label: str,
    label_check: LabelCheck,
) -> bool:
    """Flag a malformed raw pair in the rationale without changing the raw term."""
    old_summary = review.get("summary", "")
    base = _without_ontology_note(old_summary)

    if label_check.status == "MISMATCH":
        note = (
            f"{ONTOLOGY_NOTE_MARKER} Raw model pair mismatch: {go_id} resolves to "
            f"'{label_check.canonical_label}', not '{raw_label}'. The raw ID and label "
            "are retained for provenance; the assessment applies to the GO ID and "
            "explicitly flags the label error."
        )
    elif label_check.status == "UNRESOLVED":
        note = (
            f"{ONTOLOGY_NOTE_MARKER} {go_id} does not resolve in the configured current "
            f"GO ontology. The raw model label '{raw_label}' is retained for provenance "
            "and the unresolved identifier is explicitly flagged."
        )
    else:
        note = ""

    updated = base if not note else f"{base} {note}" if base else note
    if str(old_summary).strip() == updated:
        return False
    review["summary"] = _with_scalar_style(old_summary, updated)
    return True


def set_error_type(review: MutableMapping[str, Any], error_type: str | None) -> bool:
    """Set or remove error_type while retaining the surrounding key order."""
    current = review.get("error_type")
    if error_type is None:
        if "error_type" not in review:
            return False
        del review["error_type"]
        return True
    if current == error_type:
        return False
    if "error_type" in review:
        review["error_type"] = error_type
    elif hasattr(review, "insert") and "summary" in review:
        review.insert(list(review).index("summary"), "error_type", error_type)
    else:
        review["error_type"] = error_type
    return True


def apply_manual_override(
    species: str,
    gene: str,
    go_id: str,
    review: MutableMapping[str, Any],
) -> tuple[bool, bool]:
    """Apply one explicit override and return review/error-type change flags."""
    override = MANUAL_OVERRIDES.get((species, gene, go_id))
    if override is None:
        return False, False

    assessment_changed = False
    summary_changed = False
    old_assessment = review.get("assessment", "")
    if override.assessment and override.assessment != old_assessment:
        review["assessment"] = override.assessment
        assessment_changed = True
        if override.summary is not None:
            old_summary = review.get("summary", "")
            updated_summary = _with_scalar_style(old_summary, override.summary)
            if updated_summary != old_summary:
                review["summary"] = updated_summary
                summary_changed = True
        elif override.replace_category_mentions:
            old_summary = review.get("summary", "")
            updated = re.sub(
                rf"\b{re.escape(old_assessment)}\b",
                override.assessment,
                str(old_summary),
            )
            review["summary"] = _with_scalar_style(old_summary, updated)
    elif (
        override.summary is not None
        and _without_ontology_note(review.get("summary", "")) != override.summary
    ):
        review["summary"] = _with_scalar_style(review.get("summary", ""), override.summary)
        summary_changed = True

    error_changed = False
    if override.set_error_type:
        error_changed = set_error_type(review, override.error_type)
    return assessment_changed or summary_changed, error_changed


ONTOLOGY_BASIS_TEXT = {
    "CANONICAL_TAXON_VIOLATION": (
        "The canonical GO term is taxonomically incompatible with this gene product."
    ),
    "CANONICAL_ID_DENOTES_DIFFERENT_FUNCTION": (
        "The canonical GO ID denotes a different, unsupported function from the raw label."
    ),
    "CANONICAL_LOCATION_CONTRADICTED": (
        "The location denoted by the supplied GO ID is contradicted by the current reference."
    ),
    "CANONICAL_FUNCTION_CONTRADICTED": (
        "The function denoted by the supplied GO ID is contradicted by the current reference."
    ),
    "SUPPORTED_CONCEPT_REQUIRES_CURRENT_OR_MORE_PRECISE_TERM": (
        "The intended concept is supported, but the supplied ID is obsolete or requires "
        "a current or more precise term."
    ),
    "CANONICAL_TERM_SUPPORTED_AND_ABSENT_FROM_GOA": (
        "The canonical GO term is supported and absent as an exact ID from the frozen GOA."
    ),
    "CANONICAL_TERM_SUPPORTED_AS_NOT_NOVEL": (
        "The canonical GO concept is supported and already established in GOA, the "
        "AIGR, or UniProt, so it is correct but not novel."
    ),
    "CANONICAL_TERM_NOT_RESOLVED_BY_CURRENT_EVIDENCE": (
        "The canonical GO term is not resolved by the current reference evidence."
    ),
    "ONTOLOGY_STATUS_ONLY_RETAINS_RUBRIC_ASSESSMENT": (
        "The raw and canonical labels denote the same biological concept. Ontology "
        "status is flagged separately, so the biological novelty and precision "
        "assessment is retained."
    ),
    "ONTOLOGY_STATUS_ONLY_SUPPORTED_AS_NOT_NOVEL": (
        "The raw and canonical labels denote the same biological concept, and the "
        "replacement concept is already supported by GOA and the AIGR. The prediction "
        "is correct but not novel; ontology status is flagged separately."
    ),
}


def apply_ontology_pair_decision(
    species: str,
    gene: str,
    go_id: str,
    raw_label: str,
    review: MutableMapping[str, Any],
) -> tuple[bool, bool]:
    """Apply a frozen ontology-pair judgment and quarantine raw-label rationale."""
    decision = ONTOLOGY_PAIR_DECISIONS.get((species, gene, go_id, raw_label))
    if decision is None:
        return False, False

    old_assessment = str(review.get("assessment") or "")
    assessment_changed = old_assessment != decision.assessment
    if assessment_changed:
        review["assessment"] = decision.assessment

    error_changed = set_error_type(review, decision.error_type)
    base = _without_ontology_note(review.get("summary", ""))
    historical_marker = (
        " Historical rationale about the intended raw label is retained below "
        "for provenance, not as support for the canonical GO ID: "
    )
    if base.startswith(ONTOLOGY_ADJUDICATION_MARKER):
        historical = (
            base.split(historical_marker, 1)[1]
            if historical_marker in base
            else ""
        )
    else:
        historical = _plain_summary(base)

    canonical = decision.canonical_label or "unresolved in the frozen ontology"
    basis = ONTOLOGY_BASIS_TEXT[decision.basis]
    updated = (
        f"{ONTOLOGY_ADJUDICATION_MARKER} Assessed the supplied GO ID rather than "
        f"the intended raw label: {go_id} is '{canonical}'. {basis} The pair is "
        f"classified {decision.assessment}; the raw source pair remains unchanged."
    )
    if historical:
        updated += historical_marker + historical
    if base != updated:
        old_summary = review.get("summary", "")
        review["summary"] = _with_scalar_style(old_summary, updated)
        assessment_changed = True

    return assessment_changed, error_changed


def remaining_conflicts(
    go_id: str,
    review: MutableMapping[str, Any],
    goa_terms: set[str],
    actions: set[str],
) -> Iterable[str]:
    assessment = review.get("assessment", "")
    confidence = review.get("confidence_score")
    if EXPECTED_CONFIDENCE.get(assessment) != confidence:
        yield "assessment_confidence"
    if assessment == "COR" and go_id in goa_terms:
        yield "COR_in_current_GOA"
    if assessment == "CNN" and go_id not in goa_terms:
        rationale = str(review.get("summary", "")).lower()
        non_novel_markers = (
            "training data",
            "already annotated",
            "already in goa",
            "in goa",
            "not novel",
            "curated annotation",
            "curated review",
            "well-established",
        )
        if not any(marker in rationale for marker in non_novel_markers):
            yield "CNN_without_GOA_or_non_novel_basis"
    if actions and actions <= NEGATIVE_ACTIONS and assessment in {"COR", "CNN", "LSP", "UNC"}:
        yield "nonnegative_assessment_vs_negative_AIGR"
    if actions & POSITIVE_ACTIONS and assessment in {"NPI", "UNC"}:
        yield "NPI_or_UNC_vs_positive_AIGR"
    error_type = review.get("error_type")
    if error_type and assessment not in INCORRECT_ASSESSMENTS:
        yield "error_type_on_nonincorrect_assessment"
    if error_type == "PARALOG_OVERANNOTATION" and assessment != "PLI":
        yield "paralog_error_without_PLI"
    if assessment == "PLI" and error_type != "PARALOG_OVERANNOTATION":
        yield "PLI_without_paralog_error"
    if error_type == "FREQUENCY_BIAS" and assessment != "REP":
        yield "frequency_bias_without_REP"


def repair_document(
    doc: MutableMapping[str, Any],
    species: str,
    gene: str,
    goa_terms: set[str],
    aigr_actions: dict[str, set[str]],
    aigr_core: set[str],
    source_version: str,
    label_checker: OntologyLabelChecker | None,
    stats: RepairStats,
) -> bool:
    """Repair matching predictions in one round-trip-loaded document."""
    document_changed = False

    for prediction in doc.get("predictions", []):
        if prediction.get("source_version") != source_version:
            continue
        stats.predictions_seen += 1
        prediction_changed = False
        term = prediction.get("predicted_term", {})
        go_id = term.get("id", "")
        raw_label = term.get("label", "")
        review = prediction.setdefault("review", {})

        initial_assessment = review.get("assessment", "")
        stats.assessment_before[initial_assessment] += 1

        if "Requires manual assessment" in str(review.get("summary", "")):
            assessment, confidence, summary = auto_assess(
                go_id, goa_terms, aigr_actions, aigr_core
            )
            review["assessment"] = assessment
            review["confidence_score"] = confidence
            review["summary"] = _with_scalar_style(review.get("summary", ""), summary)
            prediction_changed = True

        current_assessment = review.get("assessment", "")
        decision = deterministic_reclassification(
            go_id,
            current_assessment,
            goa_terms,
            aigr_actions.get(go_id, set()),
        )
        if decision is not None:
            new_assessment, reason = decision
            review["assessment"] = new_assessment
            review["summary"] = reclassified_summary(
                review.get("summary", ""), current_assessment, new_assessment, reason
            )
            prediction_changed = True

        before_override = review.get("assessment", "")
        pair_key = (species, gene, go_id, raw_label)
        if pair_key in ONTOLOGY_PAIR_DECISIONS:
            assessment_changed, error_changed = apply_ontology_pair_decision(
                species, gene, go_id, raw_label, review
            )
        else:
            assessment_changed, error_changed = apply_manual_override(
                species, gene, go_id, review
            )
        prediction_changed |= assessment_changed or error_changed
        if error_changed:
            stats.error_type_changes += 1

        final_assessment = review.get("assessment", "")
        if final_assessment != initial_assessment:
            stats.assessment_changes[(initial_assessment, final_assessment)] += 1
        elif assessment_changed and before_override != final_assessment:
            stats.assessment_changes[(before_override, final_assessment)] += 1

        expected_confidence = EXPECTED_CONFIDENCE.get(final_assessment)
        if expected_confidence is None:
            stats.remaining_conflicts["unknown_assessment"] += 1
        elif review.get("confidence_score") != expected_confidence:
            review["confidence_score"] = expected_confidence
            stats.confidence_changes += 1
            prediction_changed = True

        if final_assessment not in INCORRECT_ASSESSMENTS:
            if set_error_type(review, None):
                stats.error_type_changes += 1
                prediction_changed = True
        elif final_assessment == "REP" and not review.get("error_type"):
            if set_error_type(review, "FREQUENCY_BIAS"):
                stats.error_type_changes += 1
                prediction_changed = True

        if label_checker is not None:
            check = label_checker.check(go_id, raw_label)
            stats.label_statuses[check.status] += 1
            if apply_label_note(review, go_id, raw_label, check):
                stats.label_notes_changed += 1
                prediction_changed = True

        stats.assessment_after[review.get("assessment", "")] += 1
        for conflict in remaining_conflicts(
            go_id, review, goa_terms, aigr_actions.get(go_id, set())
        ):
            stats.remaining_conflicts[conflict] += 1

        if prediction_changed:
            stats.predictions_changed += 1
            document_changed = True

    return document_changed


def load_cohort(cohort_file: Path) -> set[tuple[str, str]]:
    with cohort_file.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not {"species", "symbol"} <= set(reader.fieldnames):
            raise ValueError(f"Cohort must contain species and symbol columns: {cohort_file}")
        return {(row["species"], row["symbol"]) for row in reader}


def iter_sft_files(
    genes_root: Path,
    cohort: set[tuple[str, str]] | None,
) -> Iterable[tuple[str, str, Path]]:
    for path in sorted(genes_root.glob("*/*/*-sft-predictions.yaml")):
        species = path.parent.parent.name
        gene = path.parent.name
        if cohort is None or (species, gene) in cohort:
            yield species, gene, path


class _FoldedString(str):
    """Marker type for readable folded summary scalars in focused YAML rewrites."""


class _ReviewDumper(pyyaml.SafeDumper):
    pass


def _represent_folded_string(
    dumper: pyyaml.SafeDumper,
    value: _FoldedString,
) -> pyyaml.nodes.ScalarNode:
    return dumper.represent_scalar("tag:yaml.org,2002:str", value, style=">")


_ReviewDumper.add_representer(_FoldedString, _represent_folded_string)


def _plain_data(value: Any) -> Any:
    """Convert round-trip YAML containers to standard Python containers."""
    if isinstance(value, MutableMapping):
        return {str(key): _plain_data(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_plain_data(item) for item in value]
    if isinstance(value, str):
        return str(value)
    if isinstance(value, bool):
        return bool(value)
    if isinstance(value, int):
        return int(value)
    if isinstance(value, float):
        return float(value)
    return value


def render_review_block(review: MutableMapping[str, Any]) -> list[str]:
    """Render one review mapping without reformatting the rest of the document."""
    plain_review = _plain_data(review)
    plain_review["summary"] = _FoldedString(str(plain_review.get("summary", "")))
    rendered = pyyaml.dump(
        {"review": plain_review},
        Dumper=_ReviewDumper,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
        width=100,
    )
    return [f"  {line}\n" for line in rendered.rstrip("\n").splitlines()]


def rewrite_prediction_reviews(
    original_text: str,
    doc: MutableMapping[str, Any],
    changed_indexes: set[int],
) -> str:
    """Splice only changed review blocks into an SFT YAML document."""
    if not changed_indexes:
        return original_text

    lines = original_text.splitlines(keepends=True)
    try:
        predictions_line = next(
            index for index, line in enumerate(lines) if line.rstrip("\r\n") == "predictions:"
        )
    except StopIteration as error:
        raise ValueError("Prediction review YAML has no predictions key") from error

    starts = [
        index
        for index, line in enumerate(lines[predictions_line + 1 :], predictions_line + 1)
        if line.startswith("- source_method:")
    ]
    predictions = doc.get("predictions", [])
    if len(starts) != len(predictions):
        raise ValueError(
            f"Found {len(starts)} prediction blocks but parsed {len(predictions)} predictions"
        )

    for prediction_index in sorted(changed_indexes, reverse=True):
        block_start = starts[prediction_index]
        block_end = (
            starts[prediction_index + 1]
            if prediction_index + 1 < len(starts)
            else len(lines)
        )
        original_block_end = block_end
        try:
            review_start = next(
                index
                for index in range(block_start, block_end)
                if lines[index].rstrip("\r\n") == "  review:"
            )
        except StopIteration as error:
            raise ValueError(f"Prediction {prediction_index} has no review block") from error

        trailing_blank_lines: list[str] = []
        while block_end > review_start and not lines[block_end - 1].strip():
            trailing_blank_lines.insert(0, lines[block_end - 1])
            block_end -= 1
        replacement = render_review_block(predictions[prediction_index]["review"])
        lines[review_start:original_block_end] = replacement + trailing_blank_lines

    return "".join(lines)


def print_stats(stats: RepairStats, apply: bool) -> None:
    mode = "APPLY" if apply else "DRY RUN"
    print(f"Mode: {mode}")
    print(f"Files matched: {stats.files_seen}")
    print(f"Files {'modified' if apply else 'requiring changes'}: {stats.files_changed}")
    print(f"Predictions audited: {stats.predictions_seen}")
    print(f"Predictions changed: {stats.predictions_changed}")
    print(f"Confidence scores normalized: {stats.confidence_changes}")
    print(f"Error types changed: {stats.error_type_changes}")
    print(f"Ontology notes changed: {stats.label_notes_changed}")
    print("Assessment distribution before:", dict(stats.assessment_before))
    print("Assessment distribution after:", dict(stats.assessment_after))
    print(
        "Assessment changes:",
        {f"{old}->{new}": count for (old, new), count in stats.assessment_changes.items()},
    )
    print("Ontology label status:", dict(stats.label_statuses))
    print("Remaining deterministic conflicts:", dict(stats.remaining_conflicts))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write reported repairs")
    parser.add_argument("--genes-root", type=Path, default=Path("genes"))
    parser.add_argument("--cohort", type=Path, default=DEFAULT_COHORT)
    parser.add_argument(
        "--all-sft",
        action="store_true",
        help="Ignore --cohort and inspect every SFT review file",
    )
    parser.add_argument("--source-version", default=DEFAULT_SOURCE_VERSION)
    parser.add_argument("--ontology-adapter", default=DEFAULT_ONTOLOGY_ADAPTER)
    parser.add_argument(
        "--skip-ontology",
        action="store_true",
        help="Skip GO ID/label validation (not suitable for the benchmark repair)",
    )
    args = parser.parse_args()

    cohort = None if args.all_sft else load_cohort(args.cohort)
    label_checker = (
        None if args.skip_ontology else OntologyLabelChecker(args.ontology_adapter)
    )
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 100
    stats = RepairStats()

    for species, gene, path in iter_sft_files(args.genes_root, cohort):
        original_text = path.read_text()
        doc = yaml.load(original_text) or {}
        matching = [
            prediction
            for prediction in doc.get("predictions", [])
            if prediction.get("source_version") == args.source_version
        ]
        if not matching:
            continue

        stats.files_seen += 1
        goa_terms = load_goa_terms(path.parent / f"{gene}-goa.tsv")
        review_file = path.parent / f"{gene}-ai-review.yaml"
        actions = load_aigr_term_actions(review_file)
        core_terms = load_aigr_core_terms(review_file)
        original_reviews = [
            copy.deepcopy(prediction.get("review", {}))
            for prediction in doc.get("predictions", [])
        ]
        changed = repair_document(
            doc,
            species,
            gene,
            goa_terms,
            actions,
            core_terms,
            args.source_version,
            label_checker,
            stats,
        )
        if changed:
            stats.files_changed += 1
            if args.apply:
                changed_indexes = {
                    index
                    for index, prediction in enumerate(doc.get("predictions", []))
                    if original_reviews[index] != prediction.get("review", {})
                }
                path.write_text(
                    rewrite_prediction_reviews(original_text, doc, changed_indexes)
                )

    print_stats(stats, args.apply)
    return 1 if stats.remaining_conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
