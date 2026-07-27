#!/usr/bin/env python3
"""Committed invariant checks for the AGFG2 review. Run before every commit.

    python audit_claims.py            # gate: exit 1 on any problem
    python audit_claims.py --self-test  # break-test each check; each must fire

Each check exists because the corresponding failure has shipped somewhere in this
campaign. Where a check has two directions, both are implemented and both are
break-tested, because a guard that advertises N directions and implements fewer
goes silent exactly when the missing direction becomes needed.

Checks
------
A  every `supporting_text` is a verbatim substring of its source. For `PMID:` refs
   CI does this too, but for `file:` refs **nothing** does — that is the one place in
   the document where an invented quotation survives every automated gate. Fails if
   it finds zero `file:` quotes to check (a checker that silently checks nothing).
B  `existing_annotations` reconciles against the GOA TSV: every distinct GOA row has
   an entry, and every non-NEW entry corresponds to a GOA row. Both directions.
C  `supporting_entities` and `propagation_review.source_entities` are exactly the
   GOA WITH/FROM tokens for that row, in order. Built from the TSV, not by hand.
D  raw-vs-parsed reconciliation of quote-bearing keys, using a duplicate-rejecting
   loader. A duplicate mapping key is silently dropped by PyYAML, so the data is
   gone before any quote gate runs; and a YAML alias silently multiplies instead.
E  the residue claims in the YAML agree with `arfgap_domain.json`, keyed on the
   accession and the residue number — stable entities, not the prose around them.
F  every ACCEPT/NEW term appears in `core_functions`, and every `core_functions`
   term is backed by an ACCEPT or NEW row. Both directions.
G  hedge sweep: for each retracted or hedged claim, assert no structured slot states
   it flatly. Anchored on GO ids and accessions, which do not get reworded.
H  numbers asserted in the YAML prose match the JSON they came from.
"""

from __future__ import annotations

import argparse
import csv
import json
import pathlib
import re
import sys
from collections import Counter

HERE = pathlib.Path(__file__).parent
GENE_DIR = HERE.parent
REPO = HERE.parents[3]
REVIEW = GENE_DIR / "AGFG2-ai-review.yaml"
GOA = GENE_DIR / "AGFG2-goa.tsv"
PUBS = REPO / "publications"
GENES = REPO / "genes"

import yaml  # noqa: E402


class DupRejectingLoader(yaml.SafeLoader):
    """SafeLoader that raises on a duplicated mapping key instead of keeping the last."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r} at line {key_node.start_mark.line + 1}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


DupRejectingLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


def load(text: str) -> dict:
    return yaml.load(text, Loader=DupRejectingLoader)


def walk_quotes(obj, path="") -> list[tuple[str, str, str]]:
    """Yield (path, reference_id, supporting_text) from ANY nesting level.

    Deliberately not restricted to `review.supported_by`: the repo's own quote
    checker does not walk `provenance` or `knowledge_gaps[].provenance`, and quotes
    have shipped unchecked there.
    """
    out = []
    if isinstance(obj, dict):
        if "supporting_text" in obj and isinstance(obj.get("supporting_text"), str):
            ref = obj.get("reference_id")
            out.append((path, ref, obj["supporting_text"]))
        for k, v in obj.items():
            out.extend(walk_quotes(v, f"{path}/{k}"))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out.extend(walk_quotes(v, f"{path}/{i}"))
    return out


def resolve_reference(ref: str | None, parent_path: str, doc: dict) -> pathlib.Path | None:
    """Map a reference id to the file whose text must contain the quote.

    `findings[].supporting_text` has no `reference_id` of its own — it inherits the
    enclosing `references[].id`. Handling that is what makes the check cover the
    `findings` quotes as well as `supported_by`.
    """
    if ref is None:
        m = re.match(r"^/references/(\d+)/findings/\d+$", parent_path)
        if not m:
            return None
        ref = doc["references"][int(m.group(1))]["id"]
    if ref.startswith("PMID:"):
        return PUBS / f"PMID_{ref.split(':', 1)[1]}.md"
    if ref.startswith("file:"):
        return GENES / ref.split(":", 1)[1]
    return None


def norm(s: str) -> str:
    """Collapse whitespace only. Characters are NOT normalised on purpose: a
    hyphen/en-dash swap is exactly the silent `file:`-quote failure this catches."""
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- checks

def check_a_quotes(text: str, problems: list[str]) -> None:
    doc = load(text)
    quotes = walk_quotes(doc)
    n_file = n_pmid = 0
    for path, ref, quote in quotes:
        target = resolve_reference(ref, path, doc)
        if target is None:
            continue
        if not target.exists():
            problems.append(f"A: {path}: source file missing: {target}")
            continue
        body = norm(target.read_text())
        if norm(quote) not in body:
            problems.append(f"A: {path}: quote not verbatim in {target.name}: {quote[:90]!r}")
        if (ref or "").startswith("file:"):
            n_file += 1
        else:
            n_pmid += 1
    # A checker that finds nothing to check is the vacuity hole; fail loudly.
    if n_file == 0:
        problems.append("A: zero file: quotes were checked — the check is vacuous")
    if n_pmid == 0:
        problems.append("A: zero PMID quotes were checked — the check is vacuous")


def goa_rows() -> list[dict]:
    with GOA.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def check_b_coverage(text: str, problems: list[str]) -> None:
    doc = load(text)
    rows = goa_rows()
    goa_keys = Counter(
        (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["QUALIFIER"], r["WITH/FROM"])
        for r in rows
    )
    entries = doc["existing_annotations"]
    yaml_keys = Counter()
    for e in entries:
        if e["review"]["action"] == "NEW":
            continue
        yaml_keys[(
            e["term"]["id"], e["evidence_type"], e["original_reference_id"],
            e.get("qualifier", ""), "|".join(e.get("supporting_entities") or []),
        )] += 1
    missing = goa_keys - yaml_keys
    extra = yaml_keys - goa_keys
    if missing:
        problems.append(f"B: GOA rows with no review entry: {sorted(missing)}")
    if extra:
        problems.append(f"B: non-NEW review entries not in GOA: {sorted(extra)}")
    n_new = sum(1 for e in entries if e["review"]["action"] == "NEW")
    if len(entries) - n_new != sum(goa_keys.values()):
        problems.append(
            f"B: entry count does not reconcile: {len(entries)} entries "
            f"({n_new} NEW) vs {sum(goa_keys.values())} GOA rows"
        )


def check_c_source_entities(text: str, problems: list[str]) -> None:
    doc = load(text)
    by_key = {}
    for r in goa_rows():
        by_key[(r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"])] = [
            t for t in r["WITH/FROM"].split("|") if t
        ]
    seen_any = False
    for i, e in enumerate(doc["existing_annotations"]):
        if e["review"]["action"] == "NEW":
            continue
        key = (e["term"]["id"], e["evidence_type"], e["original_reference_id"])
        expected = by_key.get(key)
        if expected is None:
            problems.append(f"C: entry {i} ({key}) has no matching GOA row")
            continue
        got = list(e.get("supporting_entities") or [])
        if got != expected:
            problems.append(
                f"C: entry {i} {key[0]}: supporting_entities {got} != GOA WITH/FROM {expected}"
            )
        pr = e["review"].get("propagation_review")
        if expected and pr is None:
            problems.append(f"C: entry {i} {key[0]}: WITH/FROM present but no propagation_review")
            continue
        if pr is not None:
            seen_any = True
            src = [s["source_id"] for s in (pr.get("source_entities") or [])]
            if src != expected:
                problems.append(
                    f"C: entry {i} {key[0]}: source_entities {src} != GOA WITH/FROM {expected}"
                )
            # Assert presence, don't merely validate on match: a guard that
            # `continue`s when the id is absent passes when the entity is deleted.
            for tok in expected:
                if tok not in src:
                    problems.append(f"C: entry {i} {key[0]}: source_entities is missing {tok}")
    if not seen_any:
        problems.append("C: no propagation_review was inspected — the check is vacuous")


def check_d_raw_vs_parsed(text: str, problems: list[str]) -> None:
    try:
        doc = load(text)
    except yaml.constructor.ConstructorError as exc:
        problems.append(f"D: duplicate YAML key: {exc}")
        return
    parsed = len(walk_quotes(doc))
    # Match both `- supporting_text:` and `supporting_text:` forms; PyYAML puts an
    # anchor on the list-item line and the keys on the following lines, so a
    # `^\s*- ` anchor alone undercounts.
    raw = len(re.findall(r"^\s*(?:-\s*)?supporting_text:", text, re.M))
    aliases = len(re.findall(r"^\s*-?\s*\*id\d+", text, re.M))
    anchors = len(re.findall(r"&id\d+", text))
    if anchors or aliases:
        problems.append(
            f"D: YAML anchors/aliases present ({anchors} anchors, {aliases} aliases); "
            f"they multiply quotes on parse and make raw counts meaningless"
        )
    if raw != parsed:
        problems.append(f"D: raw supporting_text count {raw} != parsed {parsed}")


def check_e_residues(text: str, problems: list[str]) -> None:
    site = json.loads((HERE / "arfgap_domain.json").read_text())
    body = norm(text)
    # Select on stable entities (accession + residue), never on the prose.
    expect_arg = site["proteins"]["O95081"]["site"]["catalytic_arg"]
    asp = site["arf_contacting_asp_alignment"]["O95081"]
    if expect_arg != 75:
        problems.append(f"E: computed catalytic Arg is {expect_arg}, YAML says 75")
    if f"Arg{expect_arg}" not in body and f"R{expect_arg}Q" not in body:
        problems.append(f"E: YAML does not mention the computed Arg{expect_arg}")
    expected_asp = f"{asp['residue']}{asp['position']}"
    if expected_asp != "T89":
        problems.append(f"E: computed Asp-site residue is {expected_asp}, YAML says T89")
    if "Thr89" not in body:
        problems.append("E: YAML does not mention the computed Thr89")
    # The whole argument depends on the panel discriminating; assert it here so a
    # future rerun that stops discriminating breaks the audit rather than the prose.
    agfg = ["O95081", "P52594", "Q80WC7", "Q8K2K6", "E1JHR0"]
    non_agfg = ["Q8N6T3", "Q9ULH1", "Q8TDY4", "Q8IYB5"]
    for a in agfg:
        if a not in site["arf_contacting_asp_alignment"]:
            problems.append(f"E: {a} absent from the Asp alignment — panel incomplete")
        elif site["arf_contacting_asp_alignment"][a]["is_asp"]:
            problems.append(f"E: AGFG protein {a} HAS the Arf-contacting Asp; "
                            f"the discrimination claim is false")
    for a in non_agfg:
        if a not in site["arf_contacting_asp_alignment"]:
            problems.append(f"E: {a} absent from the Asp alignment — panel incomplete")
        elif not site["arf_contacting_asp_alignment"][a]["is_asp"]:
            problems.append(f"E: non-AGFG ArfGAP {a} LACKS the Arf-contacting Asp; "
                            f"the discrimination claim is false")


# An ACCEPT/NEW term may legitimately be absent from `core_functions`, but only for a
# stated reason. An enumerated exemption list carrying a reason per case is used rather
# than a blanket relaxation, so the next such case has to be argued rather than absorbed.
CORE_FUNCTION_EXEMPT = {
    "GO:0044794": (
        "virus-co-opted role: the schema defines core_functions as the core *evolved* "
        "functions of the gene, CD4 levels were only ever measured in the presence of "
        "Nef or Vpu, and the in-repo APOE review keeps this same term as contextual "
        "rather than core"
    ),
}


def check_f_core_functions(text: str, problems: list[str]) -> None:
    doc = load(text)
    kept = {
        e["term"]["id"]
        for e in doc["existing_annotations"]
        if e["review"]["action"] in {"ACCEPT", "NEW"}
    }
    cf_terms = set()
    for cf in doc.get("core_functions") or []:
        for slot in ("molecular_function", "contributes_to_molecular_function", "in_complex"):
            t = cf.get(slot)
            if t:
                cf_terms.add(t["id"])
        for slot in ("directly_involved_in", "locations", "anatomical_locations"):
            for t in cf.get(slot) or []:
                cf_terms.add(t["id"])
    if not kept:
        problems.append("F: no ACCEPT/NEW rows found — the check is vacuous")
    if not cf_terms:
        problems.append("F: core_functions declares no terms — the check is vacuous")
    for t in sorted(kept - cf_terms):
        if t in CORE_FUNCTION_EXEMPT:
            continue
        problems.append(f"F: {t} is ACCEPT/NEW but absent from core_functions")
    for t in sorted(cf_terms - kept):
        problems.append(f"F: {t} is in core_functions but no row ACCEPTs or proposes it")
    # The exemption list must not rot: an exemption for a term that is no longer ACCEPT/NEW,
    # or that IS in core_functions after all, is a stale licence and must be removed.
    for t in sorted(CORE_FUNCTION_EXEMPT):
        if t not in kept:
            problems.append(
                f"F: {t} is exempted from core_functions but is not an ACCEPT/NEW row — "
                f"stale exemption"
            )
        elif t in cf_terms:
            problems.append(
                f"F: {t} is exempted from core_functions but IS in core_functions — "
                f"the exemption is unnecessary and should be removed"
            )


# Flat assertions of claims the review deliberately hedges. Anchored on the GO id,
# which does not get reworded, and phrased as the *conclusion's shape* rather than a
# single literal, since a literal pin is defeated by the first paraphrase. This check
# matches fixed patterns and cannot catch every paraphrase; prose surfaces still need
# re-reading when a claim is withdrawn.
#
# An earlier version of this list forbade the string `located_in` whenever GO:0033093
# was hedged. That was a badly-scoped rule: `located_in` is a legitimate qualifier on
# unrelated rows, so the guard fired on correct content. A guard that forbids
# legitimate practice gets worked around rather than obeyed. The Weibel-Palade-body
# location claim is instead covered by the structured-slot sweep below, which is where
# it would actually have to be asserted to do damage.
HEDGES = [
    ("GO:0005096", r"\bAGFG2 (?:is|acts as) an? (?:Arf )?GTPase[- ]activat"),
    ("GO:0005096", r"AGFG2 (?:has|possesses) (?:Arf )?GAP activity"),
    ("GO:0005096", r"AGFG2 (?:hydrolyses|hydrolyzes|stimulates hydrolysis of) GTP"),
]
STRUCTURED_SLOTS = (
    "molecular_function", "contributes_to_molecular_function", "directly_involved_in",
    "locations", "anatomical_locations", "in_complex", "substrates", "action",
    "root_cause", "source_status", "description",
)


def check_g_hedges(text: str, problems: list[str]) -> None:
    doc = load(text)
    body = norm(text)
    for anchor, forbidden in HEDGES:
        if re.search(forbidden, body, re.I):
            problems.append(
                f"G: prose hedges {anchor} but a flat assertion matching {forbidden!r} is present"
            )
    # The hedged MF must not appear in ANY structured slot, and the sweep covers
    # locations too, not only the MF slots.
    flat = []

    def collect(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in STRUCTURED_SLOTS:
                    flat.append((f"{path}/{k}", v))
                collect(v, f"{path}/{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                collect(v, f"{path}/{i}")

    collect(doc)
    if not flat:
        problems.append("G: no structured slots were inspected — the check is vacuous")
    for path, v in flat:
        blob = json.dumps(v)
        for banned in ("GO:0005096", "GO:0033093", "GO:0005515", "GO:0060090"):
            if banned in blob and path.split("/")[-1] in {
                "molecular_function", "contributes_to_molecular_function",
                "directly_involved_in", "locations", "in_complex",
            }:
                problems.append(
                    f"G: {banned} appears in structured slot {path}, but the review "
                    f"hedges or declines it"
                )


NUMBER_WORDS = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
    8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
}


def _states_number(body: str, n: int, suffix: str) -> bool:
    """True if the number is stated, in digit OR word form, with its context word.

    Three things this gets right that the obvious version does not:

    * a number spelled as a word evades every digit grep, so both forms count;
    * ``str(n) in body`` is meaningless for a small number — "9" occurs inside
      "PMID:9303539" — so a **context suffix is mandatory**, not optional. Without it
      the check passes vacuously for every single-digit value;
    * the digit form needs a **left boundary**. A plain substring test lets
      ``"4 amphibians"`` match inside ``"14 amphibians"``, so a stale prose value whose
      last digits happen to equal the true value would pass. Binding single-digit
      quantities widens that hole, which is why the boundary is enforced here rather
      than left as a latent one.
    """
    assert suffix, "a bare digit test is vacuous; give the context word"
    if re.search(rf"(?<!\d){re.escape(str(n))}{re.escape(suffix)}", body):
        return True
    w = NUMBER_WORDS.get(n)
    return bool(w) and re.search(
        rf"\b{re.escape(w)}{re.escape(suffix)}", body, re.I
    ) is not None


def check_h_numbers(text: str, problems: list[str]) -> None:
    body = norm(text)
    prov = json.loads((HERE / "provenance.json").read_text())
    site = json.loads((HERE / "arfgap_domain.json").read_text())
    lit = json.loads((HERE / "litsearch.json").read_text())
    node = json.loads((HERE / "node_reach.json").read_text())

    ident = site["identity_vs_AGFG2"]
    # (computed value, mandatory context suffix, what it is)
    bindings = [
        (prov["projection"]["PMID:19946888"]["n_annotations"], " annotations",
         "PMID:19946888 annotation count"),
        (prov["projection"]["PMID:19946888"]["n_entities"], " distinct gene products",
         "PMID:19946888 entity count"),
        (prov["interpro2go"]["IPR001164"]["n_proteins"], " proteins",
         "IPR001164 protein count"),
        (prov["family_census"]["reviewed_members_in_cached_csv"], " reviewed",
         "PTHR46134 reviewed-member count"),
        (node["nodes"]["PTN002919572"]["n_entities"], " gene products",
         "PTN002919572 entity count"),
        (lit["queries"]["agfg1_acrosome_control"]["count"], " hits",
         "acrosome positive-control hit count"),
    ]
    for value, suffix, what in bindings:
        if not _states_number(body, value, suffix):
            problems.append(f"H: {what} {value}{suffix} not stated in the YAML")
    for acc in ("Q80WC7", "Q8K2K6"):
        v = ident[acc]["full_length_pct"]
        if f"{v}%" not in body:
            problems.append(f"H: computed identity {v}% for {acc} not stated in the YAML")

    # Term-usage counts and the IntAct partner count: both are claims the review makes in
    # prose that used to rest only on an ad-hoc query. Bound to committed JSON here so
    # they are evidence in the repository rather than in a transcript.
    terms = json.loads((HERE / "term_checks.json").read_text())["extra"]
    intact = json.loads((HERE / "intact.json").read_text())
    usage_bindings = [
        (terms["human_usage_GO_0044794"]["n_annotations"], " human annotations",
         "GO:0044794 human annotation count"),
        (terms["human_usage_GO_0044794"]["n_entities"], " entities",
         "GO:0044794 human entity count"),
        (intact["n_human_partners_with_coip_or_pulldown"], " protein interaction partners",
         "IntAct human co-IP/pulldown partner count"),
    ]
    # The clade-census numbers the *review document* states in prose. These are the ones a
    # curator reads, and until now only the RESULTS.md copies were gated — the same class of
    # coverage gap fixed on the other artifact, left standing one file away. `_states_number`
    # requires a context suffix, which is what makes binding the single-digit 1 and 4 safe.
    dist = json.loads((HERE / "distribution.json").read_text())["census"]
    usage_bindings += [
        (dist["Actinopterygii (bony fish)"]["AGFG2"]["total"], " ray-finned fish",
         "agfg2 Actinopterygii census, as stated in the YAML"),
        (dist["Sauropsida (reptiles+birds)"]["AGFG2"]["total"], " sauropsids",
         "agfg2 Sauropsida census, as stated in the YAML"),
        (dist["Amphibia"]["AGFG2"]["total"], " amphibians",
         "agfg2 Amphibia census, as stated in the YAML"),
        (dist["Aves"]["AGFG2"]["total"], " avian agfg2",
         "agfg2 Aves census, as stated in the YAML"),
        (dist["Aves"]["AGFG1_control"]["total"], " avian agfg1",
         "agfg1 Aves control, as stated in the YAML"),
    ]
    for value, suffix, what in usage_bindings:
        if not _states_number(body, value, suffix):
            problems.append(f"H: {what} {value}{suffix} not stated in the YAML")
    # The GO:0046784 zero is only readable against a non-zero control from the same call
    # pattern; assert the control rather than trusting it.
    if terms["human_usage_GO_0046784"]["n_annotations"] != 0:
        problems.append(
            "H: the YAML says GO:0046784 carries zero human annotations, but "
            f"term_checks.json records {terms['human_usage_GO_0046784']['n_annotations']}"
        )
    if terms["human_usage_GO_0045055"]["n_annotations"] == 0:
        problems.append(
            "H: the GO:0046784 zero has no non-zero control — GO:0045055 also returned 0, "
            "so the query pattern cannot be trusted"
        )


#: Set by the self-test to feed check I a mutated report. Check I reads RESULTS.md
#: through this indirection so the break-test can operate on the same representation
#: the check reads — a detector and a mutator that see different artifacts make the
#: verification structurally blind.
RESULTS_MD_OVERRIDE: str | None = None


def _read_results_md() -> str | None:
    if RESULTS_MD_OVERRIDE is not None:
        return RESULTS_MD_OVERRIDE
    md = HERE / "RESULTS.md"
    return md.read_text() if md.exists() else None


CENSUS_HEADER = "| clade (NCBI taxon) | `agfg2` | `agfg1` (control) |"


def _parse_census_table(raw: str) -> list[dict]:
    """Parse the clade-census table out of the EMITTED RESULTS.md.

    Asserting over the file that ships, rather than over the structure that produced it,
    is what makes a silently dropped or reformatted row detectable.
    """
    lines = raw.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == CENSUS_HEADER)
    except StopIteration:
        return []
    rows = []
    for line in lines[start + 2:]:                  # +2 skips the |---|---| separator
        s = line.strip()
        if not s.startswith("|"):
            break
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) != 3:
            break
        clade, a2, a1 = cells

        def num(c: str) -> int | None:
            c = c.replace("*", "").strip()
            return int(c) if c.isdigit() else None

        rows.append({"clade_cell": clade, "agfg2": num(a2), "agfg1": num(a1)})
    return rows


def _check_census_table(raw: str, dist: dict, problems: list[str]) -> None:
    rows = _parse_census_table(raw)
    census = dist["census"]
    if not rows:
        problems.append("I: the clade-census table was not found in RESULTS.md")
        return
    # A dropped row is the failure this exists to catch, so reconcile the sets of clades
    # rather than only the cells of the rows that happen to be present.
    json_keys = {k.split()[0].rstrip(","): k for k in census}
    # Keying on the first whitespace token would silently COLLIDE if two clades shared it,
    # shrinking expected_cells and weakening the coverage floor. Not reachable with the
    # current five labels, but a silent shrink is exactly what this counter exists to
    # prevent, so it is asserted rather than assumed.
    if len(json_keys) != len(census):
        problems.append(
            f"I: two clade labels in distribution.json share a first token, so the "
            f"census key set collapsed from {len(census)} to {len(json_keys)}"
        )
    table_keys = {r["clade_cell"].split(",")[0].strip(): r for r in rows}
    missing = sorted(set(json_keys) - set(table_keys))
    extra = sorted(set(table_keys) - set(json_keys))
    if missing:
        problems.append(f"I: clade-census table is missing rows for {missing}")
    if extra:
        problems.append(f"I: clade-census table has rows not in distribution.json: {extra}")
    # Two counters, and both count COMPARISONS ATTEMPTED, never failures found. An earlier
    # version incremented `checked` inside the taxon-id failure branch, so taxon-id failures
    # inflated the value-cell count and could offset a genuinely lost row (one deleted row
    # -2, two missing taxon ids +2, back to parity). A coverage floor that a failure can
    # satisfy is not a floor.
    checked = 0
    taxon_checked = 0
    for short, key in json_keys.items():
        row = table_keys.get(short)
        if row is None:
            continue
        for label, expected in (("agfg2", census[key]["AGFG2"]["total"]),
                                ("agfg1", census[key]["AGFG1_control"]["total"])):
            got = row[label]
            if got != expected:
                problems.append(
                    f"I: clade-census table {short}/{label} says {got}, "
                    f"distribution.json says {expected}"
                )
            checked += 1
        tx = census[key].get("taxon_id")
        if tx is not None:
            taxon_checked += 1
            if str(tx) not in row["clade_cell"]:
                problems.append(
                    f"I: clade-census table row for {short} does not carry its taxon id {tx}"
                )
    expected_cells = 2 * len(json_keys)
    if checked < expected_cells:
        problems.append(
            f"I: only {checked} of {expected_cells} census value cells were compared — "
            f"the table check has lost coverage"
        )
    expected_taxa = sum(1 for k in json_keys if census[json_keys[k]].get("taxon_id"))
    if taxon_checked < expected_taxa:
        problems.append(
            f"I: only {taxon_checked} of {expected_taxa} census taxon ids were compared — "
            f"the table check has lost coverage"
        )


def check_i_results_md(text: str, problems: list[str]) -> None:
    """RESULTS.md is cited as evidence, so its numbers are bound to the JSON too.

    This is the surface most often missed in this campaign, *precisely because* it is
    cited as evidence rather than read as prose. `text` is unused: the check is about
    the report file, and it runs in the same harness so it cannot be forgotten.
    """
    raw = _read_results_md()
    if raw is None:
        problems.append("I: RESULTS.md is missing")
        return
    body = norm(raw)
    prov = json.loads((HERE / "provenance.json").read_text())
    site = json.loads((HERE / "arfgap_domain.json").read_text())
    node = json.loads((HERE / "node_reach.json").read_text())
    lit = json.loads((HERE / "litsearch.json").read_text())
    dist = json.loads((HERE / "distribution.json").read_text())

    bindings = [
        (prov["projection"]["PMID:19946888"]["n_annotations"], " annotations",
         "PMID:19946888 annotation count"),
        (prov["family_census"]["reviewed_members_in_cached_csv"], " reviewed",
         "PTHR46134 reviewed-member count"),
        (node["nodes"]["PTN002919572"]["n_entities"], " |",
         "PTN002919572 entity count (table cell)"),
        (lit["n_cited_checked"], "** references relied",
         "count of references swept for retractions"),
        (lit["queries"]["arfgap_activity_control"]["count"], " |",
         "ArfGAP-activity positive-control count (table cell)"),
        (dist["census"]["Aves"]["AGFG2"]["total"], "** avian `agfg2`",
         "the avian agfg2/agfg1 asymmetry"),
    ]
    # The clade census is a TABLE, so it is verified by parsing the emitted table and
    # comparing cell by cell against the JSON, not by suffix-matching a hand-picked
    # subset. Suffix bookkeeping bound 4 of 10 cells and silently lost coverage when the
    # table was reformatted; a parser cannot lose cells without the row count changing.
    _check_census_table(raw, dist, problems)
    intact = json.loads((HERE / "intact.json").read_text())
    md_intact = [
        (intact["total_records"], " records", "IntAct total record count"),
        (intact["n_protein_protein_records"], " are protein–protein",
         "IntAct protein-protein record count"),
        (intact["n_distinct_partners"], " distinct partners", "IntAct distinct partner count"),
        (intact["n_human_partners_with_coip_or_pulldown"], " human partners",
         "IntAct human co-IP/pulldown partner count"),
    ]
    bindings += md_intact
    for value, suffix, what in bindings:
        if not _states_number(body, value, suffix):
            problems.append(f"I: RESULTS.md does not state {what} as {value}{suffix}")
    # The residue table must agree with the computation it reports. Accept either the
    # one-letter or the three-letter notation: the check binds the *value*, and pinning
    # one notation would fail on a legitimate rewording rather than on a wrong number.
    three = {"D": "Asp", "T": "Thr", "A": "Ala", "S": "Ser", "N": "Asn", "E": "Glu"}
    for acc in ("O95081", "Q8N6T3"):
        asp = site["arf_contacting_asp_alignment"][acc]
        one_letter = f"{asp['residue']}{asp['position']}"
        long_form = f"{three.get(asp['residue'], asp['residue'])}{asp['position']}"
        if one_letter not in body and long_form not in body:
            problems.append(
                f"I: RESULTS.md does not state the computed Asp site for {acc} as "
                f"{one_letter} or {long_form}"
            )
    arg = site["proteins"]["O95081"]["site"]["catalytic_arg"]
    if f"R{arg} present" not in body:
        problems.append(f"I: RESULTS.md does not state 'R{arg} present' for AGFG2")


CHECKS = {
    "A": check_a_quotes,
    "B": check_b_coverage,
    "C": check_c_source_entities,
    "D": check_d_raw_vs_parsed,
    "E": check_e_residues,
    "F": check_f_core_functions,
    "G": check_g_hedges,
    "H": check_h_numbers,
    "I": check_i_results_md,
}


def run(text: str) -> list[str]:
    problems: list[str] = []
    for name, fn in CHECKS.items():
        # A check that raises would abort every later check, including the
        # self-test baseline; collect instead of raising.
        try:
            fn(text, problems)
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{name}: check itself failed: {type(exc).__name__}: {exc}")
    return problems


# ---------------------------------------------------------------- self-test

def _mutate_quote(t: str) -> str:
    m = re.search(r"(supporting_text: )(\S.*)$", t, re.M)
    assert m, "no supporting_text to mutate"
    return t[: m.start(2)] + "THIS SENTENCE IS NOT IN ANY SOURCE" + t[m.end(2):]


def _mutate_drop_row(t: str) -> str:
    d = load(t)
    n_before = len(d["existing_annotations"])
    d["existing_annotations"] = [
        e for e in d["existing_annotations"] if e["term"]["id"] != "GO:0045109"
    ]
    assert len(d["existing_annotations"]) == n_before - 1, "mutation removed nothing"
    return yaml.safe_dump(d, sort_keys=False)


def _mutate_source_entity(t: str) -> str:
    d = load(t)
    for e in d["existing_annotations"]:
        if e["term"]["id"] == "GO:0001675":
            before = list(e["supporting_entities"])
            e["supporting_entities"] = before[:1]
            pr = e["review"]["propagation_review"]
            pr["source_entities"] = pr["source_entities"][:1]
            assert e["supporting_entities"] != before, "mutation removed nothing"
            return yaml.safe_dump(d, sort_keys=False)
    raise AssertionError("GO:0001675 row not found — fixture has drifted")


def _mutate_duplicate_key(t: str) -> str:
    anchor = "gene_symbol: AGFG2\n"
    assert anchor in t, "anchor for duplicate-key mutation is absent"
    return t.replace(anchor, anchor + "gene_symbol: AGFG2\n", 1)


def _mutate_residue(t: str) -> str:
    assert "Thr89" in t, "Thr89 absent — fixture has drifted"
    return t.replace("Thr89", "Thr999")


def _mutate_drop_cf_term(t: str) -> str:
    d = load(t)
    cf = d["core_functions"][0]
    before = json.dumps(cf)
    cf.pop("locations", None)
    assert json.dumps(cf) != before, "mutation changed nothing"
    return yaml.safe_dump(d, sort_keys=False)


def _mutate_add_cf_term(t: str) -> str:
    d = load(t)
    cf = d["core_functions"][0]
    before = json.dumps(cf)
    cf["molecular_function"] = {"id": "GO:0005096", "label": "GTPase activator activity"}
    assert json.dumps(cf) != before, "mutation changed nothing"
    return yaml.safe_dump(d, sort_keys=False)


def _mutate_exemption_unnecessary(t: str) -> str:
    """Put an exempted term back into core_functions: the exemption is then a stale
    licence and must be reported, not silently tolerated."""
    d = load(t)
    cf = d["core_functions"][0]
    before = json.dumps(cf)
    cf.setdefault("directly_involved_in", []).append(
        {"id": "GO:0044794", "label": "host-mediated activation of viral process"}
    )
    assert json.dumps(cf) != before, "mutation changed nothing"
    return yaml.safe_dump(d, sort_keys=False)


def _mutate_exemption_stale(t: str) -> str:
    """Change an exempted row's action away from NEW: the exemption then covers a row
    that no longer needs it."""
    d = load(t)
    for e in d["existing_annotations"]:
        if e["term"]["id"] == "GO:0044794":
            before = e["review"]["action"]
            assert before == "NEW", f"fixture drifted: action is {before}"
            e["review"]["action"] = "UNDECIDED"
            return yaml.safe_dump(d, sort_keys=False)
    raise AssertionError("GO:0044794 row not found — fixture has drifted")


def _mutate_yaml_census_number(t: str) -> str:
    """Break one of the clade-census numbers stated in the REVIEW DOCUMENT, not in
    RESULTS.md — the copy a curator actually reads."""
    anchor = "72 ray-finned fish"
    assert anchor in t, f"{anchor!r} absent from the YAML — fixture has drifted"
    out = t.replace(anchor, "999 ray-finned fish")
    assert out != t, "mutation changed nothing"
    return out


def _mutate_left_digit_boundary(t: str) -> str:
    """Prefix a digit to a bound value: '4 amphibians' -> '14 amphibians'.

    Without a left boundary this passes a plain substring test, so a stale prose value
    whose trailing digits equal the true value slips through. The mutation is deliberately
    the *smallest* one that a boundary-less matcher cannot distinguish from correct text.
    """
    anchor = "and 4\n      amphibians"
    alt = "and 4 amphibians"
    if anchor in t:
        return t.replace(anchor, "and 14\n      amphibians")
    assert alt in t, "neither wrapped nor unwrapped '4 amphibians' found — fixture drifted"
    return t.replace(alt, "and 14 amphibians")


def _mutate_number(t: str) -> str:
    """Change every occurrence of a number H binds, choosing one that does not appear
    inside any `file:` quote, so the mutation exercises H rather than A."""
    assert "60678 proteins" in t, "'60678 proteins' absent — fixture has drifted"
    out = t.replace("60678", "999")
    assert out != t, "mutation changed nothing"
    return out


def _mutate_number_as_word(t: str) -> str:
    """The word form must count as stated, so spelling a bound number out must NOT
    trip H. This is the happy-direction test: a check can be wrong about success as
    easily as about failure."""
    assert "All 6 reviewed members" in t, "anchor for the word-form test has drifted"
    out = t.replace("All 6 reviewed members", "All six reviewed members")
    assert out != t, "mutation changed nothing"
    return out


BREAK_TESTS = [
    # (label, mutator, check that must fire, substring expected in the message)
    ("A: fabricated quote", _mutate_quote, "A", "not verbatim"),
    ("B: dropped a GOA row", _mutate_drop_row, "B", "no review entry"),
    ("C: truncated source_entities", _mutate_source_entity, "C", "WITH/FROM"),
    ("D: duplicate YAML key", _mutate_duplicate_key, "D", "duplicate YAML key"),
    ("E: residue disagrees with computation", _mutate_residue, "E", "Thr89"),
    ("F: ACCEPT term missing from core_functions", _mutate_drop_cf_term, "F",
     "absent from core_functions"),
    ("F: core_functions term with no ACCEPT/NEW row", _mutate_add_cf_term, "F",
     "no row ACCEPTs"),
    ("F: exemption unnecessary (term is in core_functions after all)",
     _mutate_exemption_unnecessary, "F", "exemption is unnecessary"),
    ("F: exemption stale (exempted row is no longer ACCEPT/NEW)",
     _mutate_exemption_stale, "F", "stale exemption"),
    ("G: hedged MF asserted in a structured slot", _mutate_add_cf_term, "G",
     "structured slot"),
    ("H: prose number contradicts the JSON", _mutate_number, "H", "not stated"),
    ("H: a YAML census number contradicts distribution.json",
     _mutate_yaml_census_number, "H", "ray-finned fish"),
    ("H: a bound value with a digit prefixed ('4' -> '14') is NOT accepted",
     _mutate_left_digit_boundary, "H", "amphibians"),
]

# The happy direction. A guard can be wrong about success as easily as about failure,
# and a legitimate-practice false positive is what gets a guard worked around rather
# than obeyed — so each of these mutations is legal content that must NOT fire.
NO_FIRE_TESTS = [
    ("H: a bound number spelled as a word is still 'stated'", _mutate_number_as_word, "H"),
]


def self_test(text: str) -> int:
    baseline = run(text)
    if baseline:
        print("SELF-TEST ABORTED: the unmutated file already has problems:")
        for p in baseline:
            print("   ", p)
        return 1
    print("baseline: clean\n")
    failures = 0
    for label, mutate, check, expect in BREAK_TESTS:
        mutated = mutate(text)
        # 1. the mutation applied
        if mutated == text:
            print(f"  FAIL  {label}: mutation was a no-op")
            failures += 1
            continue
        problems = run(mutated)
        hits = [p for p in problems if p.startswith(f"{check}:")]
        # 2. the right guard fired
        if not hits:
            print(f"  FAIL  {label}: check {check} did not fire "
                  f"(other problems: {problems})")
            failures += 1
            continue
        # 3. with the expected message
        if not any(expect in h for h in hits):
            print(f"  FAIL  {label}: check {check} fired but not with {expect!r}: {hits}")
            failures += 1
            continue
        print(f"  ok    {label} -> {hits[0][:110]}")

    # Check I reads RESULTS.md, not the YAML, so its break-tests must mutate that file's
    # text. Patching the module global the check resolves at call time keeps detector and
    # mutator on the same artifact, and the patch is asserted to be visible before use.
    global RESULTS_MD_OVERRIDE
    original = _read_results_md()
    assert original is not None, "RESULTS.md is missing; check I cannot be break-tested"

    # Each mutation must be as FINE as the claim it certifies, and must replace EVERY
    # occurrence — a `count=1` replace left a second copy of "R75 present" standing, so
    # the check correctly did not fire and the break-test read as a guard failure. The
    # taxon-id fixture likewise had to be narrowed: dropping the whole clade label made
    # the row read as missing/extra instead of as missing-a-taxon-id, which is a coarser
    # mutation than the distinction under test.
    md_break_tests = [
        ("I: a residue in RESULTS.md contradicts the JSON",
         [("R75 present", "R999 present")], "R75 present"),
        ("I: a census table CELL contradicts the JSON",
         [("| **72** | 50 |", "| **72** | 51 |")], "agfg1"),
        ("I: a census table ROW is deleted",
         [("| Amphibia, 8292 | **4** | 28 |\n", "")], "missing rows"),
        ("I: a census table row loses its taxon id (label intact)",
         [("| Aves, 8782 (⊂ Sauropsida)", "| Aves, (⊂ Sauropsida)")], "taxon id"),
        # The exact scenario that defeated the old counter: one deleted row (-2 value
        # cells) plus two rows missing their taxon ids (+2 under the old accounting) landed
        # back at parity and suppressed the coverage message. With the counters separated,
        # the value-cell floor must still report 8 of 10.
        ("I: a deleted row is NOT offset by taxon-id failures (counter integrity)",
         [("| Amphibia, 8292 | **4** | 28 |\n", ""),
          ("| Aves, 8782 (⊂ Sauropsida)", "| Aves, (⊂ Sauropsida)"),
          ("| Mammalia, 40674", "| Mammalia,")],
         "8 of 10 census value cells"),
    ]
    for label, pairs, expect in md_break_tests:
        missing_anchor = [o for o, _ in pairs if o not in original]
        if missing_anchor:
            print(f"  FAIL  {label}: anchor(s) {missing_anchor!r} drifted out of RESULTS.md")
            failures += 1
            continue
        mutated_md = original
        for o, n in pairs:                        # every occurrence, not just the first
            mutated_md = mutated_md.replace(o, n)
        if mutated_md == original:
            print(f"  FAIL  {label}: mutation was a no-op")
            failures += 1
            continue
        RESULTS_MD_OVERRIDE = mutated_md
        try:
            assert _read_results_md() == mutated_md, "the override did not take effect"
            hits = [p for p in run(text) if p.startswith("I:")]
        finally:
            RESULTS_MD_OVERRIDE = None
        if not hits:
            print(f"  FAIL  {label}: check I did not fire")
            failures += 1
        elif not any(expect in h for h in hits):
            print(f"  FAIL  {label}: fired but not with {expect!r}: {hits}")
            failures += 1
        else:
            print(f"  ok    {label} -> {hits[0][:110]}")

    for label, mutate, check in NO_FIRE_TESTS:
        mutated = mutate(text)
        if mutated == text:
            print(f"  FAIL  {label}: mutation was a no-op")
            failures += 1
            continue
        hits = [p for p in run(mutated) if p.startswith(f"{check}:")]
        if hits:
            print(f"  FAIL  {label}: check {check} fired on legitimate content: {hits}")
            failures += 1
        else:
            print(f"  ok    {label} (correctly silent)")

    print()
    n_break = len(BREAK_TESTS) + len(md_break_tests)
    total = n_break + len(NO_FIRE_TESTS)
    if failures:
        print(f"{failures} of {total} self-test(s) failed")
    else:
        print(f"all {n_break} break-tests fired for the right reason and "
              f"all {len(NO_FIRE_TESTS)} no-fire test(s) stayed silent")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--file", default=str(REVIEW),
                    help="review YAML to audit (used to run against a staged copy)")
    args = ap.parse_args()
    text = pathlib.Path(args.file).read_text()
    if args.self_test:
        return self_test(text)
    problems = run(text)
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print(f"all {len(CHECKS)} checks passed on {args.file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
