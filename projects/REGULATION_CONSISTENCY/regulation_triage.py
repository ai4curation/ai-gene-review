#!/usr/bin/env python3
"""Triage GO "regulation of X" annotations: consistency, sign conflicts, meaning.

Three analyses, all deterministic from public inputs plus the review corpus:

1. **GOA triage** (one species GAF, default goa_human). For every gene and every
   biological process X that is the target of a ``regulates`` /
   ``positively_regulates`` / ``negatively_regulates`` edge, classify the
   gene's relationship to X:

   - which regulation signs are annotated (``+``, ``-``, ``0`` = unsigned);
   - whether the gene is *also* annotated as a participant in X (X itself, or
     an is_a/part_of descendant of X that is not itself a regulation term);
   - which evidence codes / qualifiers support the regulation rows.

   Each (gene, X) pair gets one or more flags (see ``FLAGS``).

2. **Meaning heuristics** for each regulation row: rule-based guess at what the
   annotation is actually asserting (participant mis-filed as regulator,
   transcriptional/indirect effect, perturbation readout, direct regulator).
   These are hypotheses to be calibrated against (3), not ground truth.

3. **Review mine**: every ``*-ai-review.yaml`` under ``genes/`` is scanned for
   existing-annotation rows on regulation terms. Actions are tallied, and every
   MODIFY on a regulation term is classified by *where the replacement points*
   (to the participant term X, the opposite sign, a signed child of an unsigned
   term, another regulation term, or elsewhere). The replacement is a
   reviewer's retroactive statement of what the original annotation meant.

Usage::

    uv run python projects/REGULATION_CONSISTENCY/regulation_triage.py \
        --obo go.obo --gaf goa_human.gaf.gz --genes-dir genes \
        --out-dir projects/REGULATION_CONSISTENCY/results

``go.obo`` must be the full GO (not go-basic): go-basic omits the regulates
relations this analysis depends on.
"""

from __future__ import annotations

import argparse
import csv
import gzip
from collections import Counter, defaultdict
from pathlib import Path

import yaml

try:
    from yaml import CSafeLoader as Loader
except ImportError:  # pragma: no cover
    from yaml import SafeLoader as Loader  # type: ignore[assignment]

REG_RELS = {"regulates": "0", "positively_regulates": "+", "negatively_regulates": "-"}
EXPERIMENTAL = {
    "EXP",
    "IDA",
    "IPI",
    "IMP",
    "IGI",
    "IEP",
    "HTP",
    "HDA",
    "HMP",
    "HGI",
    "HEP",
}
PERTURBATION = {"IMP", "IGI", "IEP", "HMP", "HGI", "HEP"}
PHYLO = {"IBA", "IBD", "IKR", "IRD"}
# MF roots whose descendants mark a gene as a plausible *direct* regulator.
REGULATOR_MF = {
    "GO:0098772": "molecular function regulator activity",
    "GO:0140110": "transcription regulator activity",
}
TF_MF = "GO:0140110"
BROAD_TARGET_DESCENDANTS = 500

FLAGS = {
    "PARTICIPANT_AND_REGULATOR": "gene annotated both to X (or a part/subtype) and to a regulation of X",
    "BIDIRECTIONAL": "gene annotated to both positive and negative regulation of X",
    "UNSIGNED_REDUNDANT": "unsigned 'regulation of X' alongside a signed one for the same X",
    "REGULATOR_ONLY": "regulation of X only; no participant annotation",
}


# --------------------------------------------------------------------------- ontology


class Ontology:
    """Minimal GO graph: names, namespaces, is_a/part_of parents, regulation edges."""

    def __init__(self) -> None:
        self.name: dict[str, str] = {}
        self.namespace: dict[str, str] = {}
        self.parents: dict[str, set[str]] = defaultdict(set)  # is_a + part_of
        self.isa: dict[str, set[str]] = defaultdict(set)
        self.reg: dict[str, set[tuple[str, str]]] = defaultdict(
            set
        )  # term -> {(sign, target)}
        self.alt: dict[str, str] = {}
        self._anc: dict[str, frozenset[str]] = {}
        self._children: dict[str, set[str]] | None = None
        self._desc: dict[str, frozenset[str]] = {}

    @classmethod
    def from_obo(cls, path: Path) -> "Ontology":
        onto = cls()
        cur: dict | None = None

        def commit(t: dict | None) -> None:
            if not t or "id" not in t or t.get("obsolete"):
                return
            tid = t["id"]
            onto.name[tid] = t.get("name", "")
            onto.namespace[tid] = t.get("namespace", "")
            for alt in t.get("alt", ()):
                onto.alt[alt] = tid
            for rel, tgt in t.get("rels", ()):
                if rel in ("is_a", "part_of"):
                    onto.parents[tid].add(tgt)
                if rel == "is_a":
                    onto.isa[tid].add(tgt)
                if rel in REG_RELS:
                    onto.reg[tid].add((REG_RELS[rel], tgt))

        with path.open(encoding="utf-8") as fh:
            for raw in fh:
                line = raw.strip()
                if line == "[Term]":
                    commit(cur)
                    cur = {"rels": []}
                    continue
                if line.startswith("["):
                    commit(cur)
                    cur = None
                    continue
                if cur is None or not line:
                    continue
                key, _, val = line.partition(": ")
                if key == "id":
                    cur["id"] = val
                elif key == "name":
                    cur["name"] = val
                elif key == "namespace":
                    cur["namespace"] = val
                elif key == "is_obsolete" and val == "true":
                    cur["obsolete"] = True
                elif key == "alt_id":
                    cur.setdefault("alt", []).append(val)
                elif key == "is_a":
                    cur["rels"].append(("is_a", val.split()[0]))
                elif key == "relationship":
                    parts = val.split()
                    if len(parts) >= 2:
                        cur["rels"].append((parts[0], parts[1]))
            commit(cur)
        # Inherit a regulation edge through is_a for regulation-named terms lacking
        # a direct one (e.g. "regulation of X by Y").
        for tid in list(onto.name):
            if tid not in onto.reg and "regulation of" in onto.name[tid]:
                for anc in onto.isa_ancestors(tid):
                    if anc != tid and anc in onto.reg:
                        onto.reg[tid] |= onto.reg[anc]
                        break
        return onto

    def canon(self, tid: str) -> str:
        return self.alt.get(tid, tid)

    def ancestors(self, tid: str) -> frozenset[str]:
        """Reflexive is_a/part_of ancestors."""
        if tid in self._anc:
            return self._anc[tid]
        seen = {tid}
        stack = list(self.parents.get(tid, ()))
        while stack:
            p = stack.pop()
            if p not in seen:
                seen.add(p)
                stack.extend(self.parents.get(p, ()))
        out = frozenset(seen)
        self._anc[tid] = out
        return out

    def isa_ancestors(self, tid: str) -> list[str]:
        """Breadth-first is_a ancestors (nearest first)."""
        out, frontier, seen = [], [tid], {tid}
        while frontier:
            nxt = []
            for t in frontier:
                for p in sorted(self.isa.get(t, ())):
                    if p not in seen:
                        seen.add(p)
                        out.append(p)
                        nxt.append(p)
            frontier = nxt
        return out

    def is_reg(self, tid: str) -> bool:
        return tid in self.reg

    def reg_targets(self, tid: str) -> set[tuple[str, str]]:
        return self.reg.get(tid, set())


# --------------------------------------------------------------------------- GOA triage


def load_gaf(
    path: Path, onto: Ontology
) -> dict[str, dict[str, list[tuple[str, str, str]]]]:
    """gene symbol -> term -> [(evidence, qualifier, reference)] for non-NOT rows."""
    genes: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("!"):
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) < 15 or "NOT" in f[3].split("|"):
                continue
            term = onto.canon(f[4])
            if term not in onto.name:
                continue
            genes[f[2]][term].append((f[6], f[3], f[5]))
    return genes


def evidence_class(codes: set[str]) -> str:
    if codes & (EXPERIMENTAL - PERTURBATION):
        return "direct_experimental"
    if codes & PERTURBATION:
        return "perturbation_only"
    if codes & PHYLO:
        return "phylogenetic"
    if codes & {"ISS", "ISO", "ISA", "ISM", "RCA"}:
        return "sequence_or_ortholog"
    if codes & {"TAS", "NAS", "IC"}:
        return "author_or_curator_statement"
    if "IEA" in codes:
        return "electronic"
    return "other"


def triage_goa(onto: Ontology, genes: dict, out_dir: Path) -> dict:
    regulator_mf_desc: set[str] = set()
    for t in onto.name:
        anc = onto.ancestors(t)
        if any(r in anc for r in REGULATOR_MF):
            regulator_mf_desc.add(t)
    tf_desc = {t for t in onto.name if TF_MF in onto.ancestors(t)}
    # Broad grouping targets (biological_process, metabolic process, ...) make
    # almost every gene a "participant"; for those only a direct annotation counts.
    n_desc: Counter = Counter()
    for t in onto.name:
        if onto.namespace.get(t) == "biological_process":
            for a in onto.ancestors(t):
                n_desc[a] += 1

    pair_rows = []
    row_rows = []
    flag_counts: Counter = Counter()
    meaning_counts: Counter = Counter()
    meaning_by_evidence: Counter = Counter()
    n_reg_rows = n_bp_rows = 0
    genes_with_reg = 0
    sign_combo_counts: Counter = Counter()
    qualifier_counts: Counter = Counter()

    for gene, terms in sorted(genes.items()):
        bp = {
            t: v
            for t, v in terms.items()
            if onto.namespace.get(t) == "biological_process"
        }
        mf = {t for t in terms if onto.namespace.get(t) == "molecular_function"}
        n_bp_rows += sum(len(v) for v in bp.values())
        is_regulator_mf = bool(mf & regulator_mf_desc)
        is_tf = bool(mf & tf_desc)
        # participant terms: non-regulation BP terms, expanded to is_a/part_of ancestors
        participant_closure: dict[str, set[str]] = defaultdict(set)
        for t in bp:
            if onto.is_reg(t):
                continue
            for a in onto.ancestors(t):
                participant_closure[a].add(t)
        by_target: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
        for t, rows in bp.items():
            for sign, target in onto.reg_targets(t):
                by_target[target][sign].append((t, rows))
        if by_target:
            genes_with_reg += 1
        for target, signs in sorted(by_target.items()):
            sset = set(signs)
            participant_terms = sorted(participant_closure.get(target, ()))
            if n_desc[target] > BROAD_TARGET_DESCENDANTS:
                participant_terms = [p for p in participant_terms if p == target]
            flags = []
            if participant_terms:
                flags.append("PARTICIPANT_AND_REGULATOR")
            else:
                flags.append("REGULATOR_ONLY")
            if {"+", "-"} <= sset:
                flags.append("BIDIRECTIONAL")
            if "0" in sset and sset & {"+", "-"}:
                flags.append("UNSIGNED_REDUNDANT")
            for fl in flags:
                flag_counts[fl] += 1
            sign_combo_counts["".join(sorted(sset))] += 1
            reg_codes: set[str] = set()
            for sign, items in signs.items():
                for term, rows in items:
                    codes = {r[0] for r in rows}
                    quals = {r[1] for r in rows}
                    refs = sorted({r[2] for r in rows})
                    reg_codes |= codes
                    for q in quals:
                        qualifier_counts[q] += 1
                    n_reg_rows += len(rows)
                    ev = evidence_class(codes)
                    meaning = classify_meaning(
                        sign,
                        bool(participant_terms),
                        ev,
                        is_regulator_mf,
                        is_tf,
                        target,
                        onto,
                    )
                    meaning_counts[meaning] += 1
                    meaning_by_evidence[(meaning, ev)] += 1
                    row_rows.append(
                        {
                            "gene": gene,
                            "reg_term": term,
                            "reg_label": onto.name[term],
                            "sign": sign,
                            "target": target,
                            "target_label": onto.name.get(target, ""),
                            "evidence": ",".join(sorted(codes)),
                            "evidence_class": ev,
                            "qualifiers": ",".join(sorted(quals)),
                            "references": ",".join(refs[:5]),
                            "also_participant": "yes" if participant_terms else "no",
                            "regulator_mf": "yes" if is_regulator_mf else "no",
                            "tf_mf": "yes" if is_tf else "no",
                            "meaning_guess": meaning,
                        }
                    )
            pair_rows.append(
                {
                    "gene": gene,
                    "target": target,
                    "target_label": onto.name.get(target, ""),
                    "signs": "".join(sorted(sset)),
                    "flags": ",".join(flags),
                    "participant_terms": ",".join(participant_terms[:5]),
                    "reg_evidence": ",".join(sorted(reg_codes)),
                }
            )

    write_tsv(out_dir / "goa_pairs.tsv", pair_rows)
    # Review queue: pairs with a consistency flag beyond plain REGULATOR_ONLY.
    write_tsv(
        out_dir / "triage_queue.tsv",
        [r for r in pair_rows if r["flags"] != "REGULATOR_ONLY"],
    )
    write_tsv(out_dir / "goa_regulation_rows.tsv", row_rows)

    # Hot spots: targets with most bidirectional genes; genes with most conflicts.
    bidir_by_target: Counter = Counter()
    pr_by_target: Counter = Counter()
    bidir_by_gene: Counter = Counter()
    for r in pair_rows:
        if "BIDIRECTIONAL" in r["flags"]:
            bidir_by_target[(r["target"], r["target_label"])] += 1
            bidir_by_gene[r["gene"]] += 1
        if "PARTICIPANT_AND_REGULATOR" in r["flags"]:
            pr_by_target[(r["target"], r["target_label"])] += 1
    return {
        "genes_total": len(genes),
        "genes_with_regulation_annotation": genes_with_reg,
        "bp_annotation_rows": n_bp_rows,
        "regulation_annotation_rows": n_reg_rows,
        "gene_target_pairs": len(pair_rows),
        "flag_counts": dict(flag_counts.most_common()),
        "sign_combinations": dict(sign_combo_counts.most_common()),
        "regulation_row_qualifiers": dict(qualifier_counts.most_common()),
        "meaning_guess_counts": dict(meaning_counts.most_common()),
        "meaning_guess_by_evidence": {
            f"{m}|{e}": n
            for (m, e), n in sorted(meaning_by_evidence.items(), key=lambda x: -x[1])
        },
        "top_bidirectional_targets": [
            {"id": t, "label": lab, "genes": n}
            for (t, lab), n in bidir_by_target.most_common(25)
        ],
        "top_participant_and_regulator_targets": [
            {"id": t, "label": lab, "genes": n}
            for (t, lab), n in pr_by_target.most_common(25)
        ],
        "top_bidirectional_genes": [
            {"gene": g, "targets": n} for g, n in bidir_by_gene.most_common(25)
        ],
    }


def classify_meaning(
    sign: str,
    participant: bool,
    ev: str,
    regulator_mf: bool,
    tf: bool,
    target: str,
    onto: Ontology,
) -> str:
    """Rule-based guess at what a 'regulation of X' row asserts.

    Ordered rules; first match wins. These are hypotheses to be calibrated
    against reviewer MODIFY targets, not ground truth.

    The GAF qualifier (involved_in vs acts_upstream_of*) is deliberately not
    used: it tracks each group's annotation policy rather than the biology
    (MGI and TAIR mark most IMP/IGI process rows acts_upstream*, human GOA
    about 5%), so it carries no information about what the row means.

    >>> o = Ontology(); o.name["GO:1"] = "x"
    >>> classify_meaning("+", True, "direct_experimental", False, False, "GO:1", o)
    'participant_misfiled_as_regulator'
    >>> classify_meaning("-", False, "perturbation_only", False, False, "GO:1", o)
    'perturbation_readout'
    """
    if participant and sign in ("+", "0") and not regulator_mf:
        return "participant_misfiled_as_regulator"
    if participant:
        return "participant_with_feedback_or_modulation"
    if tf and "transcription" not in onto.name.get(target, ""):
        return "indirect_via_gene_expression"
    if ev == "perturbation_only":
        return "perturbation_readout"
    if regulator_mf:
        return "direct_regulator_candidate"
    if ev in ("electronic", "phylogenetic", "sequence_or_ortholog"):
        return "propagated_unclassified"
    return "unclassified"


# --------------------------------------------------------------------------- review mine


def classify_replacement(onto: Ontology, orig: str, repl: str) -> str:
    """Where does a reviewer's replacement for a regulation term point?

    The categories, in priority order:
    participant: replacement is the regulated process X or a part/subtype of it;
    sign_flip: replacement regulates the same/related X with the opposite sign;
    signed_refinement: unsigned -> signed for the same/related X;
    same_sign_refinement: same sign, more specific X;
    generalised: replacement is an ancestor of the original regulation term;
    other_regulation: some other regulation term; other: anything else.
    """
    orig, repl = onto.canon(orig), onto.canon(repl)
    if repl not in onto.name or orig not in onto.name:
        return "unresolvable"
    otg = onto.reg_targets(orig)
    targets = {t for _, t in otg}
    osigns = {s for s, _ in otg}
    if not onto.is_reg(repl):
        anc = onto.ancestors(repl)
        if targets & anc:
            return "participant"
        if onto.namespace.get(repl) != "biological_process":
            return "other_aspect"
        return "other_process"
    rtg = onto.reg_targets(repl)
    related = any(
        rt == t or t in onto.ancestors(rt) or rt in onto.ancestors(t)
        for _, rt in rtg
        for t in targets
    )
    rsigns = {s for s, _ in rtg}
    if related:
        if ({"+"} == osigns and "-" in rsigns) or ({"-"} == osigns and "+" in rsigns):
            return "sign_flip"
        if osigns == {"0"} and rsigns & {"+", "-"}:
            return "signed_refinement"
        if repl in onto.ancestors(orig):
            return "generalised"
        return "same_sign_refinement"
    if repl in onto.ancestors(orig):
        return "generalised"
    return "other_regulation"


def mine_reviews(onto: Ontology, genes_dir: Path, out_dir: Path) -> tuple[dict, dict]:
    action_reg: Counter = Counter()
    action_nonreg: Counter = Counter()
    action_reg_by_sign: Counter = Counter()
    action_reg_by_ev: Counter = Counter()
    modify_kind: Counter = Counter()
    pair_actions: Counter = Counter()
    modify_rows = []
    pair_rows = []
    decisions: dict[tuple[str, str, str], tuple[str, str]] = {}
    n_files = 0
    for path in sorted(genes_dir.glob("*/*/*-ai-review.yaml")):
        try:
            doc = yaml.load(path.read_text(encoding="utf-8"), Loader=Loader)
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        n_files += 1
        species = path.parent.parent.name
        rows = doc.get("existing_annotations") or []
        bp_rows = []
        for ann in rows:
            if not isinstance(ann, dict):
                continue
            term = (ann.get("term") or {}).get("id")
            review = ann.get("review") or {}
            action = review.get("action")
            if not term or not action:
                continue
            term = onto.canon(term)
            if onto.namespace.get(term) != "biological_process":
                continue
            ev = ann.get("evidence_type", "")
            negated = bool(ann.get("negated"))
            bp_rows.append((term, action, ev, negated))
            if negated:
                continue
            if onto.is_reg(term):
                action_reg[action] += 1
                kinds = [
                    classify_replacement(onto, term, (r or {}).get("id", ""))
                    for r in (review.get("proposed_replacement_terms") or [])
                    if (r or {}).get("id", "").startswith("GO:")
                ]
                decisions[(species, path.parent.name, term)] = (
                    action,
                    kinds[0] if kinds else "",
                )
                for sign, _ in onto.reg_targets(term):
                    action_reg_by_sign[(sign, action)] += 1
                action_reg_by_ev[(evidence_class({ev}), action)] += 1
                if action == "MODIFY":
                    for rep in review.get("proposed_replacement_terms") or []:
                        rid = (rep or {}).get("id")
                        if not rid or not rid.startswith("GO:"):
                            kind = "new_term_request" if rid else "missing"
                        else:
                            kind = classify_replacement(onto, term, rid)
                        modify_kind[kind] += 1
                        modify_rows.append(
                            {
                                "species": species,
                                "gene": path.parent.name,
                                "evidence": ev,
                                "original": term,
                                "original_label": onto.name.get(term, ""),
                                "replacement": rid or "",
                                "replacement_label": (rep or {}).get("label", ""),
                                "kind": kind,
                            }
                        )
            else:
                action_nonreg[action] += 1
        # Within-review X + RoX pairs: what did the reviewer do with each side?
        by_term: dict[str, set[str]] = defaultdict(set)
        for term, action, _, negated in bp_rows:
            if not negated:
                by_term[term].add(action)
        part_terms = [t for t in by_term if not onto.is_reg(t)]
        for term, actions in by_term.items():
            for sign, target in onto.reg_targets(term):
                parts = [p for p in part_terms if target in onto.ancestors(p)]
                if not parts:
                    continue
                part_actions = set().union(*(by_term[p] for p in parts))
                key = (sign, best_action(actions), best_action(part_actions))
                pair_actions[key] += 1
                pair_rows.append(
                    {
                        "species": species,
                        "gene": path.parent.name,
                        "reg_term": term,
                        "reg_label": onto.name.get(term, ""),
                        "sign": sign,
                        "reg_actions": ",".join(sorted(actions)),
                        "participant_terms": ",".join(sorted(parts)[:5]),
                        "participant_actions": ",".join(sorted(part_actions)),
                    }
                )
    write_tsv(out_dir / "review_regulation_modifications.tsv", modify_rows)
    write_tsv(out_dir / "review_participant_and_regulator_pairs.tsv", pair_rows)
    return decisions, {
        "review_files": n_files,
        "actions_on_regulation_terms": dict(action_reg.most_common()),
        "actions_on_other_bp_terms": dict(action_nonreg.most_common()),
        "actions_by_sign": {
            f"{s}|{a}": n for (s, a), n in sorted(action_reg_by_sign.items())
        },
        "actions_by_evidence_class": {
            f"{e}|{a}": n
            for (e, a), n in sorted(action_reg_by_ev.items(), key=lambda x: -x[1])
        },
        "modify_replacement_kinds": dict(modify_kind.most_common()),
        "participant_and_regulator_pairs": len(pair_rows),
        "pair_action_combinations": {
            f"sign={s} reg={ra} participant={pa}": n
            for (s, ra, pa), n in pair_actions.most_common(30)
        },
    }


ACTION_RANK = [
    "ACCEPT",
    "KEEP_AS_NON_CORE",
    "NEW",
    "TOO_GENERAL",
    "MODIFY",
    "MARK_AS_OVER_ANNOTATED",
    "UNDECIDED",
    "PENDING",
    "REMOVE",
]


def best_action(actions: set[str]) -> str:
    """Most-retaining action in a set (so a term kept by any row counts as kept).

    >>> best_action({"REMOVE", "KEEP_AS_NON_CORE"})
    'KEEP_AS_NON_CORE'
    """
    for a in ACTION_RANK:
        if a in actions:
            return a
    return sorted(actions)[0] if actions else ""


def calibrate(rows_tsv: Path, decisions: dict, species: str) -> dict:
    """Cross-tabulate GOA meaning guesses against reviewer decisions on the same row.

    A heuristic is useful only if reviewers who read the evidence act on its
    buckets differently, e.g. ``participant_misfiled_as_regulator`` should be
    enriched for MODIFY-to-participant and ``perturbation_readout`` for
    KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED.
    """
    table: dict[str, Counter] = defaultdict(Counter)
    with rows_tsv.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            dec = decisions.get((species, row["gene"], row["reg_term"]))
            if not dec:
                continue
            action, kind = dec
            label = f"MODIFY->{kind}" if action == "MODIFY" and kind else action
            table[row["meaning_guess"]][label] += 1
    out = {}
    for meaning, counts in sorted(table.items(), key=lambda x: -sum(x[1].values())):
        n = sum(counts.values())
        out[meaning] = {"n": n, **{k: round(v / n, 3) for k, v in counts.most_common()}}
    return out


# --------------------------------------------------------------------------- io


def write_tsv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        if not rows:
            fh.write("")
            return
        w = csv.DictWriter(
            fh, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n"
        )
        w.writeheader()
        w.writerows(rows)


def ontology_summary(onto: Ontology) -> dict:
    bp = [t for t in onto.name if onto.namespace[t] == "biological_process"]
    reg = [t for t in bp if onto.is_reg(t)]
    signs = Counter(s for t in reg for s, _ in onto.reg_targets(t))
    return {
        "bp_terms": len(bp),
        "regulation_terms": len(reg),
        "regulation_term_fraction": round(len(reg) / len(bp), 3),
        "regulation_edges_by_sign": dict(signs),
    }


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--obo", type=Path, required=True)
    ap.add_argument("--gaf", type=Path, required=True)
    ap.add_argument("--genes-dir", type=Path, default=Path("genes"))
    ap.add_argument("--out-dir", type=Path, required=True)
    ap.add_argument(
        "--species-dir", default="human", help="genes/<dir> matching the GAF species."
    )
    ap.add_argument("--skip-reviews", action="store_true")
    args = ap.parse_args()

    onto = Ontology.from_obo(args.obo)
    summary: dict = {"inputs": {"obo": args.obo.name, "gaf": args.gaf.name}}
    summary["ontology"] = ontology_summary(onto)
    genes = load_gaf(args.gaf, onto)
    summary["goa"] = triage_goa(onto, genes, args.out_dir)
    if not args.skip_reviews:
        decisions, summary["reviews"] = mine_reviews(onto, args.genes_dir, args.out_dir)
        summary["calibration"] = calibrate(
            args.out_dir / "goa_regulation_rows.tsv", decisions, args.species_dir
        )
    with (args.out_dir / "summary.yaml").open("w", encoding="utf-8") as fh:
        yaml.safe_dump(summary, fh, sort_keys=False, width=100)
    print(yaml.safe_dump(summary, sort_keys=False, width=100))


if __name__ == "__main__":
    main()
