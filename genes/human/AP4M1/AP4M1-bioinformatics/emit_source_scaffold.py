"""Print, for every seeded row that needs a propagation_review, the exact ordered
`supporting_entities` list as it appears in the seeded YAML, so that
`source_entities` ids are copied from the seed rather than retyped."""
from pathlib import Path
import yaml

REVIEW = Path(__file__).parent.parent / "AP4M1-ai-review.yaml"
NEEDS = {"IBA", "ISS", "ISO", "IEA", "IC"}

doc = yaml.safe_load(REVIEW.read_text())
for e in doc["existing_annotations"]:
    se = e.get("supporting_entities")
    if not se or e["evidence_type"] not in NEEDS:
        continue
    print(f"### {e['term']['id']} {e['term']['label']} | {e['evidence_type']} | {e['original_reference_id']}")
    for s in se:
        print(f"      - source_id: {s}")
