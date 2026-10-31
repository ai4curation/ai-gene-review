"""Export reviewed rows and primary-cache access, without consulting GOA as evidence."""

from pathlib import Path
import hashlib
import json
from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[4]
PANEL = [("ARATH", "IAA12"), ("ARATH", "IAA17"), ("ARATH", "IAA19"), ("MARPO", "MpIAA")]


def main():
    reader = YAML(typ="safe")
    writer = YAML()
    writer.width = 100
    writer.representer.ignore_aliases = lambda *args: True
    for organism, gene in PANEL:
        folder = ROOT / "genes" / organism / gene
        review = reader.load(folder / f"{gene}-ai-review.yaml")
        out = folder / f"{gene}-source-analysis"
        out.mkdir(exist_ok=True)
        rows = []
        pmids = set()
        for number, annotation in enumerate(review["existing_annotations"]):
            evidence = annotation["review"].get("supported_by", [])
            rows.append(
                {
                    "row_zero_based": number,
                    "term": annotation["term"],
                    "evidence": annotation["evidence_type"],
                    "original_reference": annotation["original_reference_id"],
                    "source_entities": annotation.get("supporting_entities", []),
                    "negated": annotation.get("negated", False),
                    "action": annotation["review"]["action"],
                    "reason": annotation["review"].get("reason", ""),
                    "assessed_support": evidence,
                }
            )
            pmids.update(
                item["reference_id"].split(":")[1]
                for item in evidence
                if item["reference_id"].startswith("PMID:")
            )
        with (out / "annotation-audit.yaml").open("w") as stream:
            writer.dump({"gene": gene, "accession": review["id"], "rows": rows}, stream)
        access = []
        for pmid in sorted(pmids):
            path = ROOT / "publications" / f"PMID_{pmid}.md"
            raw = path.read_bytes()
            meta = reader.load(raw.decode().split("---", 2)[1])
            access.append(
                {
                    "pmid": pmid,
                    "title": meta["title"],
                    "full_text_available": meta["full_text_available"],
                    "sha256": hashlib.sha256(raw).hexdigest(),
                }
            )
        (out / "publication-access.json").write_text(
            json.dumps(access, indent=2) + "\n"
        )


if __name__ == "__main__":
    main()
