"""Verify the saved QuickGO evidence offline; no network or writes."""
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).absolute().parent


def derive():
    sources = []
    payloads = {}
    for name in ("terms.json", "is-a-ancestors.json"):
        raw = (BASE / name).read_bytes()
        receipt = json.loads((BASE / (name + ".receipt.json")).read_text())
        digest = hashlib.sha256(raw).hexdigest()
        assert receipt["status"] == 200
        assert receipt["sha256"] == digest and receipt["bytes"] == len(raw)
        assert receipt["url"].startswith("https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/")
        assert receipt["final_url"] == receipt["url"]
        assert receipt["start"].startswith("2026-10-25T09:21:")
        assert receipt["end"].startswith("2026-10-25T09:21:")
        if name == "is-a-ancestors.json":
            assert receipt["url"].endswith("/ancestors?relations=is_a")
        payload = json.loads(raw)
        assert payload["numberOfHits"] == len(payload["results"]) == 7
        payloads[name] = payload["results"]
        sources.append({"file": name, "sha256": digest, "receipt": receipt})
    terms = payloads["terms.json"]
    tm = {x["id"]: x for x in terms}
    am = {x["id"]: x for x in payloads["is-a-ancestors.json"]}
    ids = ["GO:0006679", "GO:0006682", "GO:0046513", "GO:0030148"]
    edges = []
    for parent in ["GO:0046513", "GO:0030148"]:
        for i, child in enumerate(tm[parent].get("children", [])):
            if child["id"] in ids and child["relation"] == "is_a":
                edges.append({"subject": child["id"], "relation": "is_a", "object": parent,
                              "source_file": "terms.json",
                              "json_pointer": f"/results/{terms.index(tm[parent])}/children/{i}"})
    assert {(e["subject"],e["relation"],e["object"]) for e in edges} == {
        ("GO:0006679", "is_a", "GO:0046513"),
        ("GO:0006682", "is_a", "GO:0046513"),
        ("GO:0046513", "is_a", "GO:0030148")}
    for term in ids:
        assert tm[term]["aspect"] == am[term]["aspect"] == "biological_process"
        assert tm[term]["isObsolete"] is am[term]["isObsolete"] is False
        assert tm[term]["name"] == am[term]["name"]
    for term, other in [(ids[0],ids[1]),(ids[1],ids[0])]:
        assert {"GO:0046513", "GO:0030148"} <= set(am[term]["ancestors"])
        assert other not in am[term]["ancestors"]
    projection = json.loads((BASE / "projection.json").read_text())
    assert projection["sources"] == sources
    assert projection["ontology_release"] is None
    assert projection["direct_edges"] == edges
    assert projection["terms"] == [{k: tm[t][k] for k in ["id", "name", "aspect", "isObsolete", "definition"]} for t in ids]
    assert projection["complete_returned_is_a_ancestor_lists"] == {t: am[t]["ancestors"] for t in ids}
    return {"status": "PASS", "raw_responses": len(sources), "typed_direct_edges": edges,
            "both_branches_have_ceramide_and_sphingolipid_is_a_ancestors": True,
            "branches_are_mutually_non_ancestral": True,
            "scope": "saved ontology evidence only; no network, gene biology or schema test"}


if __name__ == "__main__":
    print(json.dumps(derive(), indent=2))
