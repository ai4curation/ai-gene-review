"""Deterministic source closure; builds only its owned directory before sealing."""
import argparse
import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
AUDIT = HERE.parent
MODULE = "modules/bacterial_nitrogen_regulatory_pts.yaml"
FINAL_MODULE = "3cf1c871d03fd2464ec2b33be5ab695ca705f74f787546067d5ba8d4eeb36a60"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def write(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def relative(path):
    return str(path.relative_to(ROOT))


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def forbidden(path):
    return "__pycache__" in Path(path).parts or path.endswith(".pyc")


def resolve(ref, citing):
    if ref.startswith("PMID:"):
        return ROOT / f"publications/PMID_{ref[5:]}.md"
    if ref.startswith("Reactome:"):
        return ROOT / f"reactome/{ref.split(':', 1)[1]}.md"
    if ref.startswith("file:"):
        name = ref[5:]
        return next((p for p in (ROOT / name, ROOT / "genes" / name, citing.parent / name)
                     if p.is_file()), ROOT / name)
    return None


def citations(value):
    if isinstance(value, str) and (re.fullmatch(r"PMID:\d+", value)
                                   or value.startswith(("file:", "Reactome:"))):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from citations(item)
    elif isinstance(value, list):
        for item in value:
            yield from citations(item)


def quotes(value, ref=None, location="$"):
    if isinstance(value, dict):
        ref = value.get("reference_id", value.get("source_id", ref))
        if "findings" in value:
            ref = value.get("id", ref)
        if value.get("supporting_text"):
            yield ref, value["supporting_text"], location
        for key, item in value.items():
            yield from quotes(item, ref, location + "." + key)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from quotes(item, ref, location + f"[{index}]")


def source_kind(path):
    if path.name in ("before.json", "seed-baseline.json", "module-before.yaml.txt"):
        return "historical_snapshot_boundary"
    if "deep-research" in path.name or path.name.endswith("-uniprot.txt"):
        return "provider_or_raw_record_boundary"
    if path.parts[-2] in ("publications", "reactome") or "literature-acquisition" in str(path):
        return "primary_or_review_text_boundary"
    return "curated_or_analysis"


def roots():
    result = [ROOT / MODULE]
    for org, genes in (("ECOLI", ("ptsP", "ptsO", "ptsN", "ptsI", "ptsH")),
                       ("PSEPK", ("ptsP", "ptsH", "ptsN")),
                       ("CAUVN", ("ptsP", "ptsH", "ptsN")), ("BACSU", ("ptsH",))):
        for gene in genes:
            folder = ROOT / "genes" / org / gene
            result += [folder / f"{gene}-ai-review.yaml", folder / f"{gene}-notes.md"]
    for family in ("PTHR46244", "PTHR33705", "PTHR47738"):
        result.append(ROOT / "interpro/panther" / family / f"{family}-review.yaml")
    return result


def build():
    assert not (HERE / "handoff.json").exists(), "Frozen output; use a new additive directory"
    assert digest(ROOT / MODULE) == FINAL_MODULE
    inputs, release_checks, supersessions = {}, [], []

    def add(path):
        assert path.is_file(), str(path)
        key = relative(path)
        assert not forbidden(key), key
        inputs[key] = digest(path)

    allowed = {}
    for row in read(AUDIT / "helper-formatting-20261107/successor.json")["scripts"]:
        assert digest(ROOT / row["original_archive"]) == row["original_sha256"]
        assert digest(ROOT / row["path"]) == row["current_sha256"]
        allowed[(row["path"], row["original_sha256"])] = row["original_archive"]
        supersessions.append({"path": row["path"], "before": row["original_sha256"],
                              "after": row["current_sha256"], "archive": row["original_archive"],
                              "reason": "Root-authorized AST-checked formatting-only helper successor"})
    module_successor = read(AUDIT / "module-finalization-20261107/successor.json")
    assert digest(ROOT / module_successor["preserved_baseline"]) == module_successor["before_sha256"]
    allowed[(MODULE, module_successor["before_sha256"])] = module_successor["preserved_baseline"]
    supersessions.append({"path": MODULE, "before": module_successor["before_sha256"],
                          "after": FINAL_MODULE, "archive": module_successor["preserved_baseline"],
                          "reason": "Reviewed final module changes; explicit parsed-field comparison"})

    for manifest in sorted(AUDIT.rglob("handoff.json")):
        if HERE in manifest.parents:
            continue
        data = read(manifest)
        add(manifest)
        for section in ("files", "source_dependencies", "gene_consistency_inputs"):
            mapping = data.get(section, {})
            if not isinstance(mapping, dict):
                continue
            for name, expected in sorted(mapping.items()):
                assert isinstance(expected, str) and len(expected) == 64, (manifest, name)
                path = ROOT / name
                add(path)
                current = digest(path)
                archive = None
                if current != expected:
                    archive = allowed[(name, expected)]
                    assert digest(ROOT / archive) == expected
                    add(ROOT / archive)
                release_checks.append({"manifest": relative(manifest), "section": section,
                                       "path": name, "expected": expected, "current": current,
                                       "archive_if_superseded": archive})

    final_capacity_path = AUDIT / "module-finalization-20261107/capacity/results.json"
    final_capacity = read(final_capacity_path)
    assert final_capacity["result"] == "PASS"
    assert final_capacity["module_sha256"] == FINAL_MODULE
    add(final_capacity_path)
    for name, expected in sorted(final_capacity["source_dependencies"].items()):
        add(ROOT / name)
        assert digest(ROOT / name) == expected, name
        release_checks.append({"manifest": relative(final_capacity_path),
                               "section": "source_dependencies", "path": name,
                               "expected": expected, "current": expected,
                               "archive_if_superseded": None})

    # Historic private preflight aliases have byte-identical durable copies.
    aliases = []
    old_prefix = ".cache/module-audit-logs/nitrogen-pts-20261107/triage/"
    old = AUDIT / "prior-triage-20261107/annotation-consultation-20261107/artifact-hashes.json"
    for name, expected in sorted(read(old).items()):
        assert name.startswith(old_prefix)
        path = AUDIT / "prior-triage-20261107" / name.removeprefix(old_prefix)
        assert digest(path) == expected, name
        add(path)
        aliases.append({"historical_private_path": name, "durable_path": relative(path),
                        "sha256": expected, "equivalence": "byte-identical"})

    # Preserve every additive audit artifact, never generated bytecode or shared metadata.
    for path in sorted(AUDIT.rglob("*")):
        if path.is_file() and HERE not in path.parents:
            assert not forbidden(str(path)), path
            add(path)
    for folder in (ROOT / "history/modules/bacterial_nitrogen_regulatory_pts",):
        for path in folder.glob("*.yaml"):
            add(path)
    for name in (MODULE, MODULE.replace(".yaml", ".html")):
        path = ROOT / name
        if path.exists():
            add(path)

    graph, quote_checks, boundaries, seen = [], [], [], set()
    queue = roots()
    while queue:
        path = queue.pop(0)
        if path in seen:
            continue
        seen.add(path)
        add(path)
        kind = source_kind(path)
        text = path.read_text()
        if kind != "curated_or_analysis":
            if "deep-research" in path.name:
                boundaries.append({"path": relative(path), "role": "provider bibliography not adopted wholesale",
                                   "bibliography_PMID_leads": sorted(set(re.findall(r"PMID[: _]*(\d{5,9})", text))),
                                   "bibliography_URLs": sorted(set(re.findall(r"https?://[^\s<>\])]+", text))),
                                   "closure_claim": "Report bytes retained; bibliography not recursively closed or endorsed"})
            continue
        data = yaml.safe_load(text) if path.suffix in (".yaml", ".yml") else None
        refs = set(citations(data)) if data is not None else set()
        refs.update("PMID:" + n for n in re.findall(r"PMID(?:_|:|\s+)(\d{5,9})", text))
        if path.suffix == ".md":
            refs.update("file:" + n for n in re.findall(r"file:([^\s`\]\)]+)", text))
            for target in re.findall(r"(?:analysis|acquisition-20261107)/[^\s`<>]+?\.(?:json|yaml|md|txt|log)", text):
                candidate = ROOT / target if target.startswith("analysis/") else AUDIT / target
                assert candidate.is_file(), (path, target)
                refs.add("file:" + relative(candidate))
            for paragraph in text.split("\n\n"):
                context_paths = re.findall(r"analysis/[^\s`<>]+?\.(?:json|yaml|md|txt|log)", paragraph)
                for short in re.findall(r"`([^/` ]+\.(?:json|yaml|md|txt|log))`", paragraph):
                    candidates = [path.parent / short]
                    candidates.extend((ROOT / anchor).parent / short for anchor in context_paths)
                    found = {candidate for candidate in candidates if candidate.is_file()}
                    if len(found) == 1:
                        refs.add("file:" + relative(found.pop()))
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if not target.startswith(("http:", "https:", "#")):
                    target = target.split("#")[0]
                    candidate = path.parent / target
                    if candidate.is_file():
                        refs.add("file:" + relative(candidate.resolve()))
        for ref in sorted(refs):
            source = resolve(ref, path)
            assert source and source.is_file(), (relative(path), ref)
            graph.append({"from": relative(path), "reference": ref, "to": relative(source),
                          "source_kind": source_kind(source)})
            queue.append(source)
        if data is not None:
            for ref, quote, location in quotes(data):
                source = resolve(ref or "", path)
                assert source and source.is_file(), (path, ref)
                assert norm(quote) in norm(source.read_text()), (path, location, ref, quote)
                add(source)
                quote_checks.append({"from": relative(path), "location": location,
                                     "reference": ref, "to": relative(source), "quote": quote})

    direct_pmids = {edge["reference"][5:] for edge in graph
                    if edge["reference"].startswith("PMID:")}
    for boundary in boundaries:
        leads = set(boundary["bibliography_PMID_leads"])
        boundary["independently_cited_in_curated_roots"] = sorted(leads & direct_pmids)
        boundary["not_adopted_as_curated_PMID_evidence"] = sorted(leads - direct_pmids)
    external = []
    for path in roots():
        text = path.read_text()
        for ref in sorted(set(re.findall(r"GO_REF:\d+", text))):
            external.append({"from": relative(path), "reference": ref,
                             "role": "annotation-method identifier, not experimental support"})
    write("external-method-references.json", external)

    publication_ledger = []
    for name in sorted(inputs):
        if name.startswith("publications/PMID_") and name.endswith(".md"):
            text = (ROOT / name).read_text()
            meta = yaml.safe_load(text.split("---", 2)[1])
            publication_ledger.append({"path": name, "title": meta.get("title"),
                                       "full_text_available": meta.get("full_text_available"),
                                       "extraction_method": meta.get("full_text_extraction_method"),
                                       "publication_type": meta.get("publication_type"),
                                       "limit": "Cache flag is not proof all Methods/Results are present; see scoped assay ledger."})
    write("inputs.json", dict(sorted(inputs.items())))
    write("release-preservation.json", release_checks)
    write("supersessions.json", supersessions)
    write("private-aliases.json", aliases)
    write("source-graph.json", graph)
    write("quote-checks.json", quote_checks)
    write("bibliography-boundaries.json", boundaries)
    write("publication-access.json", publication_ledger)
    write("summary.json", {"status": "PASS", "inputs": len(inputs), "release_entries": len(release_checks),
                           "citation_edges": len(graph), "quoted_occurrences": len(quote_checks),
                           "publications": len(publication_ledger), "provider_boundaries": len(boundaries),
                           "supersessions": len(supersessions), "private_aliases": len(aliases),
                           "module_sha256": FINAL_MODULE})


def check():
    inputs = read(HERE / "inputs.json")
    for name, expected in inputs.items():
        assert not forbidden(name), name
        assert digest(ROOT / name) == expected, name
    for edge in read(HERE / "source-graph.json"):
        assert edge["from"] in inputs and edge["to"] in inputs, edge
        assert resolve(edge["reference"], ROOT / edge["from"]) == ROOT / edge["to"], edge
    for item in read(HERE / "quote-checks.json"):
        assert norm(item["quote"]) in norm((ROOT / item["to"]).read_text()), item
    for item in read(HERE / "release-preservation.json"):
        target = item["archive_if_superseded"] or item["path"]
        assert digest(ROOT / target) == item["expected"], item
    for item in read(HERE / "private-aliases.json"):
        assert digest(ROOT / item["durable_path"]) == item["sha256"], item
    seal = HERE / "handoff.json"
    if seal.exists():
        for name, expected in read(seal)["files"].items():
            assert digest(ROOT / name) == expected, name
    print(json.dumps(read(HERE / "summary.json"), indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true")
    args = parser.parse_args()
    if args.build:
        build()
    check()
