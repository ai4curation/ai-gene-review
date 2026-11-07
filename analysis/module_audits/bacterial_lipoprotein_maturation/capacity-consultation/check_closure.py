"""Verify released review manifests and current module reference/source closure."""

import hashlib
import json

import yaml

from check_capacity import AUDIT, BASE, MODULE, ROOT, refs_in, resolve


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm(text):
    return " ".join(text.split())


def main():
    manifests = [
        AUDIT / "released-ecoli-bacsu-handoff.json",
        BASE / "psepk-consultation/handoff.yaml", BASE / "lnb-consultation/handoff.json",
        BASE / "lnsab-consultation/handoff.json", BASE / "lit-consultation/handoff.yaml",
        BASE / "lhat-reuse-consultation/handoff.yaml", BASE / "family-consultation/handoff.json",
    ]
    all_inputs = json.loads((AUDIT / "source-hashes.json").read_text())
    receipts = []
    for path in manifests:
        doc = yaml.safe_load(path.read_text())
        files = doc.get("files", doc.get("files_sha256", {}))
        assert isinstance(files, dict) and files
        external = doc.get("consumed_external_sources_sha256", doc.get("unchanged_dependency_sha256", {}))
        for name, expected in {**files, **external}.items():
            assert sha(ROOT / name) == expected, name
            all_inputs[name] = expected
        all_inputs[str(path.relative_to(ROOT))] = sha(path)
        receipts.append({"manifest": str(path.relative_to(ROOT)), "sha256": sha(path),
                         "verified_files": len(files), "verified_external_sources": len(external)})
    for family in ["PTHR30589", "PTHR33695", "PTHR38686", "PTHR40042"]:
        path = ROOT / f"interpro/panther/{family}/{family}-review.yaml"
        doc = yaml.safe_load(path.read_text())
        all_inputs[str(path.relative_to(ROOT))] = sha(path)
        for ref in refs_in(doc):
            source = resolve(ref)
            all_inputs[str(source.relative_to(ROOT))] = sha(source)
    module = yaml.safe_load(MODULE.read_text())
    assert module["status"] == "COMPLETE"
    references = []
    for ref in module["references"]:
        source = resolve(ref["id"])
        text = norm(source.read_text())
        for finding in ref.get("findings", []):
            if finding.get("supporting_text"):
                assert norm(finding["supporting_text"]) in text, (ref["id"], finding)
        references.append({"id": ref["id"], "type": ref["publication_type"],
                           "findings": len(ref.get("findings", [])), "source_sha256": sha(source),
                           "manually_assessed": bool(ref.get("reference_review"))})
    assert len(references) == 11
    assert sum(r["type"] == "REVIEW" for r in references) == 3
    assert sum(r["type"] == "PRIMARY_RESEARCH" for r in references) == 8
    assert sum(r["findings"] for r in references) == 23
    assert all(r["manually_assessed"] for r in references)
    quotes = [
        ("PMID:42580408", "both recombinant LnsA and LnsB are required, along with a phospholipid donor source", "Both partners required in Sa purified system."),
        ("PMID:42580408", "S. epidermidis LnsA was unable to partner with S. aureus LnsB", "Measured reciprocal-pair failure; not generic family incompatibility."),
        ("PMID:42580408", "S. epidermidis LnsA was catalytically competent with S. epidermidis LnsB", "Matched Se pair works in Sa host; not purified Se donor assay."),
        ("PMID:39495918", "we purified Lpp(K58A)-Strep from the Δlnt strain carrying pBF9343_0945", "Purified reporter, not purified Lnb."),
        ("PMID:34253723", "These data prove that the acyl chain transferred by Lit comes from the sn-2 position of the DAG in the BLP substrate.", "Intramolecular relocation retains two chains."),
        ("PMID:40626731", "The wild-type preparation containing B. anthracis (LhaTBa) did not modify DA-LP* substrate", "Assay-specific negative constrains universal activity; no accession or PAINT placement invented."),
        ("PMID:40626731", "the integral membrane protein YpjA to transfer the ester-linked acetyl group from Ac-HepG to an amide-linked bond", "Lipid-carrier donor, not direct acetyl-CoA."),
    ]
    quote_receipt = []
    for ref, quote, interpretation in quotes:
        source = resolve(ref)
        assert norm(quote) in norm(source.read_text()), (ref, quote)
        quote_receipt.append({"reference_id": ref, "supporting_text": quote,
                              "interpretation": interpretation, "source_sha256": sha(source)})
    for relative in ["src/ai_gene_review/render_modules.py", "src/ai_gene_review/module_qc.py", "pyproject.toml", "uv.lock"]:
        all_inputs[relative] = sha(ROOT / relative)
    assert sha(MODULE) == "5eb2bc3fa15bc15ceca023e6928f5092665f5e65c9334ca7c49b8dc3a8a41e57"
    receipt = {"result": "PASS", "module_sha256": sha(MODULE), "released_manifests": receipts,
               "references": references, "mechanistic_quotes": quote_receipt,
               "input_files": len(all_inputs), "full_corpus_validation": False}
    (AUDIT / "closure-results.json").write_text(json.dumps(receipt, indent=2) + "\n")
    (AUDIT / "final-input-hashes.json").write_text(json.dumps(all_inputs, indent=2) + "\n")
    print(json.dumps({"result": "PASS", "released_manifests": len(receipts),
                      "references": len(references), "findings": 23, "input_files": len(all_inputs)}))


if __name__ == "__main__":
    main()
