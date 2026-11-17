"""Check Neisseria seed claims, frozen sources and independent sequence bridge."""

import gzip
import hashlib
import io
import json
from collections import Counter
from pathlib import Path

import yaml
from Bio import SeqIO

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    baseline = json.loads((HERE / "seed-baseline.json").read_text())
    root_baseline = json.loads((HERE.parent / "baseline.json").read_text())
    sources = (
        root_baseline["protected_files_sha256"] | baseline["protected_files_sha256"]
    )
    counts = Counter()
    row_count = 0
    per_gene = []
    for path, old in baseline["reviews"].items():
        new = yaml.safe_load((ROOT / path).read_text())
        before = old["document"]["existing_annotations"]
        after = new["existing_annotations"]

        def strip(rows):
            return [{k: v for k, v in row.items() if k != "review"} for row in rows]

        assert strip(before) == strip(after), path
        assert new["status"] == "COMPLETE", path
        actions = Counter(row["review"]["action"] for row in after)
        assert not (set(actions) & {"NEW", "PENDING"}), path
        counts.update(actions)
        row_count += len(after)
        per_gene.append({"path": path, "rows": len(after), "actions": dict(actions)})
    for path, expected in sources.items():
        assert sha(ROOT / path) == expected, path
    identity = HERE.parent / "literature-consultation/identity"
    receipt = json.loads((identity / "results.json").read_text())
    archive = (
        ROOT
        / ".cache/module-audit-logs/lps-20261107/literature-consultation/AEQZ01.dat.gz"
    )
    assert sha(archive) == receipt["source"]["sha256"]
    cds = []
    for record in SeqIO.parse(
        io.StringIO(gzip.decompress(archive.read_bytes()).decode()), "embl"
    ):
        for feature in record.features:
            if feature.type == "CDS" and "translation" in feature.qualifiers:
                cds.append((record.id, feature.qualifiers))
    matches = []
    for bridge in receipt["bridges"]:
        u = json.loads((identity / f"{bridge['uniprot']}.json").read_text())
        sequence = u["sequence"]["value"]
        hits = [(contig, q) for contig, q in cds if q["translation"][0] == sequence]
        assert len(hits) == 1
        contig, q = hits[0]
        assert contig == bridge["H44_contig"]
        assert q["protein_id"] == [bridge["H44_protein"]]
        assert q["locus_tag"] == [bridge["H44_locus"]]
        matches.append(
            {
                "accession": bridge["uniprot"],
                "identical_residues": len(sequence),
                "strain_scope": "Natural CDS identity, not phenotype or construct identity",
            }
        )
    result = {
        "status": "PASS",
        "ordered_seed_rows": row_count,
        "new_rows": 0,
        "protected_sources": len(sources),
        "actions": dict(counts),
        "genes": per_gene,
        "independent_identity_matches": matches,
        "seed_baseline_sha256": sha(HERE / "seed-baseline.json"),
        "literature_identity_receipt_sha256": sha(identity / "results.json"),
    }
    (HERE / "preservation.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
