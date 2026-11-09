"""Verify source preservation, ordered row payloads and ImuA identity corroboration."""

from collections import Counter
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import re
import unicodedata

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def sha(path):
    return sha256(path.read_bytes()).hexdigest()


def sequence_record(text):
    header, body = text.split("SQ   SEQUENCE", 1)[1].split("\n", 1)
    length, mass = re.search(r"(\d+) AA;\s+(\d+) MW", header).groups()
    sequence = "".join(re.findall(r"[A-Z]+", body.split("//", 1)[0]))
    return sequence, int(length), int(mass)


def identity_checks(sequence, length, mass):
    assert len(sequence) == length == 290
    assert mass == 30274 and round(mass / 1000, 1) == 30.3
    assert sequence[70:72] == "RT"
    assert len(sequence[222:290]) == 68 and 290 == len(sequence)


def payloads(document):
    return [
        {k: v for k, v in row.items() if k != "review"}
        for row in document["existing_annotations"]
    ]


def main():
    baseline = yaml.safe_load((HERE / "baseline.yaml").read_text())
    rows = 0
    counts = Counter()
    changes = []
    reviewed = {}
    for rel, frozen in baseline["reviews"].items():
        old = frozen["document"]
        new = yaml.safe_load((ROOT / rel).read_text())
        assert payloads(old) == payloads(new), rel
        for i, (a, b) in enumerate(zip(old["existing_annotations"], new["existing_annotations"], strict=True)):
            before, after = a["review"]["action"], b["review"]["action"]
            if before == "NEW":
                assert after == "NEW", f"Historical proposal changed: {rel}:{i}"
            if before != after:
                assert after != "NEW"
                changes.append({"review": rel, "row": i, "term": a["term"]["id"], "before": before, "after": after})
            assert not b.get("retired")
            counts[after] += 1
        rows += len(payloads(new))
        reviewed[rel] = {"sha256": sha(ROOT / rel), "rows": len(payloads(new)), "changed": sha(ROOT / rel) != frozen["sha256"]}
    for rel, expected in baseline["protected"].items():
        assert sha(ROOT / rel) == expected, f"Protected source changed: {rel}"
    uni = ROOT / "genes/MYXXD/MXAN_3991/MXAN_3991-uniprot.txt"
    paper = ROOT / "publications/PMID_38591662.md"
    seq, length, mass = sequence_record(uni.read_text())
    identity_checks(seq, length, mass)
    primary = unicodedata.normalize("NFKC", paper.read_text())
    assert "R71 and T72 of ImuA were potential active site residues" in primary
    assert "minimal self‐interaction motif of ImuA lies between residues 223 and 290" in primary
    assert "An ImuA monomer is calculated to be 30.3 kDa" in primary
    faults = []
    for label, bad_seq, bad_len, bad_mass in [
        ("changed_residue_71", seq[:70] + "A" + seq[71:], length, mass),
        ("truncated_sequence", seq[:-1], length - 1, mass),
        ("wrong_record_mass", seq, length, mass + 1000),
    ]:
        try:
            identity_checks(bad_seq, bad_len, bad_mass)
        except AssertionError:
            faults.append(label)
        else:
            raise AssertionError(f"Fault not rejected: {label}")
    exemplar = next(iter(baseline["reviews"].values()))["document"]
    corrupt = deepcopy(exemplar)
    corrupt["existing_annotations"].pop()
    assert payloads(exemplar) != payloads(corrupt)
    faults.append("deleted_annotation")
    out = {
        "status": "PASS", "reviews": reviewed, "ordered_rows_preserved": rows,
        "protected_sources": len(baseline["protected"]), "action_totals": dict(counts),
        "action_changes": changes, "new_rows": 0, "retirements": 0,
        "identity_corroboration": {
            "source_sha256": {str(uni.relative_to(ROOT)): sha(uni), str(paper.relative_to(ROOT)): sha(paper)},
            "sequence_sha256": sha256(seq.encode()).hexdigest(),
            "length": length, "source_record_mass_Da": mass, "rounded_mass_kDa": round(mass / 1000, 1),
            "residues_71_72": seq[70:72], "interaction_interval": [223, 290],
            "interval_sequence": seq[222:290], "interval_length": 68,
            "interpretation": "Independent corroboration of the prior primary promoter/CDS identity bridge; not a complete experimental-construct sequence match.",
        },
        "sensitivity_faults_rejected": faults,
        "limitations": "No DnaE2 catalytic-site alignment was performed or inferred. Mapping overreach is distinguished from unresolved target nuclease activity. Identity and payload checks do not establish biological causality.",
    }
    (HERE / "results.yaml").write_text(yaml.safe_dump(out, sort_keys=False, width=100))
    print(f"PASS: {rows} ordered rows; {len(baseline['protected'])} protected sources; identity corroboration and four sensitivity controls")


if __name__ == "__main__":
    main()
