"""Check source preservation across the recovery and current-GOA repairs."""
from collections import Counter
from datetime import datetime, timezone
import json
import hashlib
from pathlib import Path
import subprocess

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FIELDS = ("term", "evidence_type", "original_reference_id", "isoform", "negated", "qualifier")
IDENTITY_MIGRATIONS = {
    "genes/worm/csr-1/csr-1-ai-review.yaml":
        "genes/worm/csr-1/csr-1-provenance/identity-migration-manifest.json",
}

def signature(annotation):
    return json.dumps({k: annotation[k] for k in FIELDS if k in annotation}, sort_keys=True)


def make_signature(term_id, term_label, evidence_type, original_reference_id, qualifier=None):
    annotation = {
        "term": {"id": term_id, "label": term_label},
        "evidence_type": evidence_type,
        "original_reference_id": original_reference_id,
    }
    if qualifier:
        annotation["qualifier"] = qualifier
    return signature(annotation)


# Explicit current-GOA source refreshes. Keep these as narrow signature-level
# exceptions so unrelated source loss still fails loudly.
EXPECTED_RETIREMENTS = {
    "genes/yeast/APJ1/APJ1-ai-review.yaml": Counter([
        make_signature("GO:0051082", "unfolded protein binding", "IBA", "GO_REF:0000033"),
        make_signature("GO:0008270", "zinc ion binding", "IEA", "GO_REF:0000043"),
        make_signature("GO:0046872", "metal ion binding", "IEA", "GO_REF:0000043"),
        make_signature("GO:0051082", "unfolded protein binding", "IEA", "GO_REF:0000002"),
        make_signature("GO:0051082", "unfolded protein binding", "IMP", "PMID:11923285"),
    ]),
    "genes/yeast/CPS1/CPS1-ai-review.yaml": Counter([
        make_signature(
            "GO:0051603", "proteolysis involved in protein catabolic process",
            "IBA", "GO_REF:0000033",
        ),
        make_signature("GO:0004180", "carboxypeptidase activity", "IEA", "GO_REF:0000043"),
        make_signature("GO:0006508", "proteolysis", "IEA", "GO_REF:0000043"),
        make_signature("GO:0008233", "peptidase activity", "IEA", "GO_REF:0000043"),
        make_signature("GO:0046872", "metal ion binding", "IEA", "GO_REF:0000043"),
        make_signature(
            "GO:0051603", "proteolysis involved in protein catabolic process",
            "IMP", "PMID:2026161",
        ),
    ]),
    "genes/yeast/HSC82/HSC82-ai-review.yaml": Counter([
        make_signature("GO:0051082", "unfolded protein binding", "IBA", "GO_REF:0000033"),
        make_signature("GO:0000166", "nucleotide binding", "IEA", "GO_REF:0000043"),
        make_signature("GO:0005524", "ATP binding", "IEA", "GO_REF:0000120"),
        make_signature("GO:0051082", "unfolded protein binding", "IEA", "GO_REF:0000120"),
        make_signature("GO:0005515", "protein binding", "IPI", "PMID:15699485"),
        make_signature("GO:0005515", "protein binding", "IPI", "PMID:16554755"),
        make_signature("GO:0005515", "protein binding", "IPI", "PMID:19536198"),
        make_signature("GO:0005515", "protein binding", "IPI", "PMID:21734642"),
        make_signature("GO:0005515", "protein binding", "IPI", "PMID:31454312"),
        make_signature("GO:0005515", "protein binding", "IPI", "PMID:37070168"),
        make_signature("GO:0051082", "unfolded protein binding", "IDA", "PMID:9465043"),
    ]),
    "genes/yeast/HSP82/HSP82-ai-review.yaml": Counter([
        make_signature("GO:0000166", "nucleotide binding", "IEA", "GO_REF:0000043"),
        make_signature("GO:0005515", "protein binding", "IPI", "PMID:16554755"),
        make_signature("GO:0005515", "protein binding", "IPI", "PMID:19536198"),
        make_signature("GO:0005515", "protein binding", "IPI", "PMID:21734642"),
        make_signature("GO:0005515", "protein binding", "IPI", "PMID:31454312"),
        make_signature("GO:0005524", "ATP binding", "IEA", "GO_REF:0000120"),
        make_signature("GO:0051082", "unfolded protein binding", "IBA", "GO_REF:0000033"),
        make_signature("GO:0051082", "unfolded protein binding", "IDA", "PMID:10564510"),
        make_signature("GO:0051082", "unfolded protein binding", "IEA", "GO_REF:0000120"),
    ]),
    "genes/yeast/SSQ1/SSQ1-ai-review.yaml": Counter([
        make_signature("GO:0000166", "nucleotide binding", "IEA", "GO_REF:0000043",
                       qualifier="enables"),
        make_signature("GO:0005524", "ATP binding", "IEA", "GO_REF:0000120",
                       qualifier="enables"),
        make_signature("GO:0016787", "hydrolase activity", "IEA", "GO_REF:0000043",
                       qualifier="enables"),
        make_signature("GO:0005515", "protein binding", "IPI", "PMID:16554755",
                       qualifier="enables"),
        make_signature("GO:0005515", "protein binding", "IPI", "PMID:19536198",
                       qualifier="enables"),
        make_signature("GO:0051082", "unfolded protein binding", "IDA", "PMID:11601843",
                       qualifier="enables"),
    ]),
    "genes/yeast/YAR1/YAR1-ai-review.yaml": Counter([
        make_signature("GO:0033309", "SBF transcription complex", "IBA", "GO_REF:0000033"),
        make_signature("GO:0051082", "unfolded protein binding", "IDA", "PMID:26112308"),
        make_signature("GO:0051082", "unfolded protein binding", "IMP", "PMID:22570489"),
    ]),
}


EXPECTED_LABEL_REFRESHES = {
    "genes/yeast/NAP1/NAP1-ai-review.yaml": Counter([
        (
            make_signature(
                "GO:0140597", "protein carrier chaperone", "IDA", "PMID:31062022"
            ),
            make_signature(
                "GO:0140597", "protein carrier activity", "IDA", "PMID:31062022",
                qualifier="enables",
            ),
        ),
    ]),
}


def source_assertions(review):
    return Counter(signature(a) for a in review.get("existing_annotations") or []
                   if (a.get("review") or {}).get("action") != "NEW")


def without_qualifier(serialized):
    fields = json.loads(serialized)
    fields.pop("qualifier", None)
    return json.dumps(fields, sort_keys=True)


def qualifier_backfill_matches(missing_exact, surplus_current):
    """Find missing frozen signatures preserved with only a new qualifier.

    Older seeded reviews omitted qualifiers that are now backfilled by a force
    fetch. A missing frozen assertion without qualifier is therefore preserved
    when a surplus current assertion has the same term/evidence/reference/isoform/NOT
    fields plus any qualifier.
    """
    current_with_qualifiers = Counter()
    for serialized, count in surplus_current.items():
        if "qualifier" not in json.loads(serialized):
            continue
        current_with_qualifiers[without_qualifier(serialized)] += count

    matches = Counter()
    for serialized, count in missing_exact.items():
        if "qualifier" in json.loads(serialized):
            continue
        key = without_qualifier(serialized)
        matched = min(count, current_with_qualifiers[key])
        if matched:
            matches[serialized] = matched
            current_with_qualifiers[key] -= matched
    return matches


def label_refresh_matches(path, missing, current):
    """Find explicitly registered same-term label refreshes."""
    expected = EXPECTED_LABEL_REFRESHES.get(path, Counter())
    matches = Counter()
    for pair, count in expected.items():
        before, after = pair
        matched = min(count, missing[before], current[after])
        if matched:
            matches[before] = matched
    return matches


def verify_identity_migration(path, commit, before, after):
    """Require baseline-identical archives and exact fetched replacements and seed.

    This is deliberately registered only for CSR-1's verified NHR-47/LARP-1
    identity mix-up. A manifest alone cannot create an exception for another gene.
    """
    manifest_path = IDENTITY_MIGRATIONS[path]
    manifest = json.loads((ROOT / manifest_path).read_text())
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    def hashed_file(file_path, expected):
        content = (ROOT / file_path).read_bytes()
        check(hashlib.sha256(content).hexdigest() == expected, f"Hash mismatch: {file_path}")
        return content

    check(manifest["operation"] == "verified_input_identity_correction", "Wrong migration operation")
    check(before["id"] == manifest["old_review_id"] == "Q21992", "Unexpected old CSR review identity")
    check(manifest["old_source_id"] == "Q17370", "Unexpected archived source identity")
    check(after["id"] == manifest["correct_canonical_accession"] == "H2KZD5", "Unexpected replacement identity")
    prefix = "genes/worm/csr-1/csr-1"
    original_paths = {prefix + suffix for suffix in ("-ai-review.yaml", "-uniprot.txt", "-goa.tsv")}
    check({x["canonical_path"] for x in manifest["original_files"]} == original_paths,
          "Missing or extra archived canonical files")
    for entry in manifest["original_files"]:
        archived = hashed_file(entry["archived_path"], entry["sha256"])
        baseline = subprocess.check_output(["git", "show", f"{commit}:{entry['canonical_path']}"], cwd=ROOT)
        check(archived == baseline, f"Archive differs from frozen baseline: {entry['canonical_path']}")
        if entry["canonical_path"] == path:
            check(source_assertions(yaml.load(archived, Loader=yaml.CSafeLoader)) == source_assertions(before),
                  "Original source assertions changed in archive")
    expected_replacements = {prefix + suffix for suffix in ("-uniprot.txt", "-goa.tsv")}
    check({x["canonical_path"] for x in manifest["replacement_files"]} == expected_replacements,
          "Missing or extra replacement source files")
    for entry in manifest["replacement_files"]:
        fetched = hashed_file(entry["fetched_path"], entry["sha256"])
        canonical = hashed_file(entry["canonical_path"], entry["sha256"])
        check(canonical == fetched, f"Canonical source differs from fetch: {entry['canonical_path']}")
    seed_entry = manifest["replacement_seed"]
    seed = yaml.load(hashed_file(seed_entry["path"], seed_entry["sha256"]), Loader=yaml.CSafeLoader)
    check(seed["id"] == "H2KZD5", "Seed has wrong identity")
    check(all(a["review"]["action"] == "PENDING" for a in seed["existing_annotations"]),
          "Seed is not the original unreviewed source snapshot")
    expected = source_assertions(seed)
    check(sum(expected.values()) == seed_entry["source_assertions"] == 21, "Wrong replacement source count")
    check(sum(source_assertions(before).values()) == manifest["retired_original_source_assertions"] == 16,
          "Wrong original source count")
    return expected, dict(manifest=manifest_path, archived_original_source_assertions=16,
                          replacement_source_assertions=21, errors=errors)


def main():
    commit = json.loads((HERE / "baseline.json").read_text())["commit"]
    # Main can advance while these independent recovery PRs are reviewed. Limit
    # this session's check to its explicit audit records, rather than comparing
    # unrelated new or subsequently curated genes with the old baseline.
    audited_paths = set()
    for directory in (HERE, ROOT / "projects/TREEGRAFTER/rereview-2026-09-20"):
        for batch in directory.glob("*.yaml"):
            data = yaml.load(batch.read_text(), Loader=yaml.CSafeLoader) or {}
            audited_paths.update(record["gene_file"] for record in data.get("genes", []))
    manifest = json.loads((HERE / "recovery-batches.json").read_text())
    packaged_paths = {
        f"genes/{gene}/{gene.split('/')[-1]}-ai-review.yaml"
        for batch in manifest["batches"] for gene in batch.get("genes", [])
    }
    audited_paths.update(packaged_paths)
    paths = subprocess.check_output(["git", "diff", "--name-only", commit], cwd=ROOT, text=True).splitlines()
    selected = set(paths) & audited_paths
    # A standalone tracker/batch checkout cannot reproduce the assembled recovery.
    # Refuse to replace its preserved report with an empty or partial success.
    absent = packaged_paths - selected
    if not selected or absent:
        raise SystemExit(
            "Incomplete recovery checkout; preserved report was not overwritten. "
            f"Expected {len(packaged_paths)} packaged reviews; found {len(selected)}. "
            f"Missing: {', '.join(sorted(absent))}"
        )
    results = []
    for path in paths:
        if path not in audited_paths:
            continue
        before = yaml.load(subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT), Loader=yaml.CSafeLoader)
        after = yaml.load((ROOT / path).read_text(), Loader=yaml.CSafeLoader)
        old = source_assertions(before)
        current = Counter(signature(a) for a in after.get("existing_annotations") or [])
        result = dict(gene_file=path, original_non_new_annotations=sum(old.values()))
        expected = old
        if path in IDENTITY_MIGRATIONS and after.get("id") != before.get("id"):
            expected, migration = verify_identity_migration(path, commit, before, after)
            result["identity_migration"] = migration
        missing_exact = expected - current
        surplus_current = current - expected
        qualifier_backfills = qualifier_backfill_matches(missing_exact, surplus_current)
        missing_after_backfills = missing_exact - qualifier_backfills
        label_refreshes = label_refresh_matches(path, missing_after_backfills, current)
        missing_after_refreshes = missing_after_backfills - label_refreshes
        expected_retirements = EXPECTED_RETIREMENTS.get(path, Counter())
        matched_retirements = expected_retirements & missing_after_refreshes
        missing = missing_after_refreshes - matched_retirements
        stale_retirements = expected_retirements - missing_after_refreshes

        result["missing_source_assertions"] = dict(missing)
        if qualifier_backfills:
            result["qualifier_backfills"] = dict(qualifier_backfills)
        if label_refreshes:
            result["label_refreshes"] = dict(label_refreshes)
        if matched_retirements:
            result["expected_retirements"] = dict(matched_retirements)
        if stale_retirements:
            result["unexpected_expected_retirements"] = dict(stale_retirements)
        results.append(result)
    report = dict(baseline_commit=commit, checked_at=datetime.now(timezone.utc).isoformat(), genes=results)
    (HERE / "source-preservation-check.json").write_text(json.dumps(report, indent=2) + "\n")
    missing = sum(sum(r["missing_source_assertions"].values()) for r in results)
    migration_errors = sum(len(r.get("identity_migration", {}).get("errors", [])) for r in results)
    retirement_errors = sum(len(r.get("unexpected_expected_retirements", {})) for r in results)
    migrations = sum("identity_migration" in r for r in results)
    retirement_errors = sum(len(r.get("unexpected_expected_retirements", {})) for r in results)
    print(f"Checked {len(results)} changed gene reviews; {missing} missing or mutated source assertions; "
          f"{migrations} archived identity migration(s), {migration_errors} migration errors, "
          f"{retirement_errors} stale expected retirement(s)")
    if missing or migration_errors or retirement_errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
