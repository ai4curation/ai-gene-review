"""Apply the bounded PR6198 evidence follow-up; run only against the frozen baseline."""

from copy import deepcopy
from pathlib import Path
import hashlib
import json
import yaml

A = Path(__file__).resolve().parent
ROOT = A.parents[4]
OLD = A.parents[1] / "new-member-consultation"
BASE = json.loads((A / "baseline.json").read_text())
GENES = [("BORPE", f"BP{n}") for n in range(3757, 3762)] + [("PSEAE", "ttg2D")]
OUTER = (
    "We demonstrate that OmpF3–MlaA simultaneously recruits apo MlaC and phospholipids, "
    "thus greatly enhancing lipid transfer to MlaC in solution."
)
CARGO = (
    "Native and\ndenaturing mass spectrometry experiments confirm that Ttg2D, produced both\n"
    "heterologously and homologously and isolated from the periplasm, can carry two\n"
    "diacyl glycerophospholipids as well as one cardiolipin."
)
LOCATION = (
    "Under these conditions, the mature Ttg2DPae could be purified from the periplasm in "
    "sufficient amount and purity"
)
SUMMARIES = {
    "BP3757": [
        "The PROSITE-supported ATP-binding site refines nucleotide binding to the existing ATP-binding term.",
        "The ABC ATP-binding motif supports the nucleotide-binding component of the conserved MlaF ATPase role.",
        "Specific MlaF classification and ABC catalytic architecture support inferred ATP hydrolysis in the native Mla locus.",
    ],
    "BP3758": [
        "Five RuleBase-supported transmembrane helices and MlaE-specific signatures support inner-membrane localization.",
        "The cognate MlaE permease contributes to intermembrane phospholipid transfer rather than acting as a soluble carrier.",
        "MlaE-specific signatures and neighboring MlaF/MlaD support membership in the Mla ABC complex without assuming MlaB.",
    ],
    "BP3759": [
        "MlaD-specific signatures and the cognate locus support phospholipid binding inferred from characterized orthologs.",
        "The MlaD component supplies a lipid-binding interface within the intermembrane phospholipid-transfer pathway.",
    ],
    "BP3760": [
        "MlaA-specific architecture, a lipoprotein signal and cognate locus support inferred outer-membrane localization.",
        "The MlaA ortholog contributes the outer-membrane loading interface; direct loading evidence comes from E. coli.",
    ],
}


def walk(obj):
    if isinstance(obj, dict):
        yield obj
        for val in obj.values():
            yield from walk(val)
    elif isinstance(obj, list):
        for val in obj:
            yield from walk(val)


def row(go, label, reference, summary, reason, support, qualifier="enables"):
    return {
        "term": {"id": go, "label": label},
        "evidence_type": "IDA",
        "original_reference_id": reference,
        "qualifier": qualifier,
        "review": {
            "summary": summary,
            "action": "NEW",
            "reason": reason,
            "supported_by": support,
        },
    }


for org, gene in GENES:
    p = ROOT / "genes" / org / gene / f"{gene}-ai-review.yaml"
    relative = str(p.relative_to(ROOT))
    assert hashlib.sha256(p.read_bytes()).hexdigest() == BASE["review_sha256"][relative]
    d = yaml.safe_load(p.read_text())
    for annotation, summary in zip(d.get("existing_annotations", []), SUMMARIES.get(gene, [])):
        annotation["review"]["summary"] = summary
    for ref in d["references"]:
        if ref["id"].startswith("GO_REF:"):
            ref["reference_review"]["relevance"] = "LOW"
    for item in walk(d):
        if item.get("supporting_text") == "significant enrichment of PG over PE":
            item["supporting_text"] = OUTER
        if item.get("supporting_text") == "one cardiolipin":
            item["supporting_text"] = CARGO
    if org == "BORPE":
        raw = (p.parent / f"{gene}-uniprot.txt").read_text()
        if gene == "BP3757":
            quote = raw[raw.index("FT   DOMAIN"):raw.index("SQ   SEQUENCE")].strip()
            sections = ["FT:DOMAIN", "FT:BINDING"]
        elif gene == "BP3758":
            quote = raw[raw.index("FT   TRANSMEM"):raw.index("SQ   SEQUENCE")].strip()
            sections = ["FT:TRANSMEM"]
        else:
            signature = {"BP3759": "IPR030970", "BP3760": "IPR007428", "BP3761": "IPR008869"}[gene]
            quote = next(line for line in raw.splitlines() if line.startswith("DR   InterPro;") and signature in line)
            sections = ["DR:InterPro"]
        rid = f"file:{org}/{gene}/{gene}-uniprot.txt"
        for item in walk(d):
            if item.get("reference_id") == rid:
                item["supporting_text"] = quote
                item["record_section"] = sections
        ref = next(r for r in d["references"] if r["id"] == rid)
        ref["findings"].append({"statement": "Target feature/signature evidence used for the conserved-function inference, not a target biochemical assay.", "supporting_text": quote})
    if gene == "ttg2D":
        d["existing_annotations"] = [
            row(
                "GO:0005543", "phospholipid binding", "PMID:33837253",
                "Target crystallography and mass spectrometry demonstrate phospholipid binding by PAO1 Ttg2D.",
                "The protein itself binds phospholipid. The study combines a mature-target structure with cargo recovered from His-tagged Ttg2D expressed in a PAO1 deletion strain and purified from its periplasm, plus in vitro cardiolipin loading. Diverse PG/PE/cardiolipin cargo supports phospholipid binding without a claim of exclusive headgroup specificity. The zero-row source contains no competing parent or descendant annotation; this molecular-function proposal does not infer a process from necessity or claim measured membrane-to-membrane flux.",
                [{"reference_id": "PMID:33837253", "supporting_text": CARGO}],
            ),
            row(
                "GO:0030288", "outer membrane-bounded periplasmic space", "PMID:33837253",
                "His-tagged Ttg2D with its own export signal was recovered from the periplasm of a PAO1 complementing strain.",
                "The native-host periplasmic purification is direct localization evidence for the tagged, complementing target, not solely a signal-peptide prediction. The homologous expression context and engineered tag are explicit; this does not assert untagged endogenous abundance or whole-pathway directional flux. No cellular-component row exists in the source, and this location is not redundant with the separately proposed molecular-function binding term.",
                [{"reference_id": "PMID:33837253", "supporting_text": LOCATION}],
                "located_in",
            ),
        ]
        ref = next(r for r in d["references"] if r["id"] == "PMID:33837253")
        ref["findings"].append({"statement": "The complementing tagged target was directly recovered from the PAO1 periplasm; the crystallographic preparation was separately produced in E. coli.", "supporting_text": LOCATION})
    elif gene == "BP3761":
        proof_ref = "file:" + str((OLD / "bp3761-structure-proof.json").relative_to(ROOT))
        ligand_ref = "file:" + str((OLD / "11HY-nonpolymer_entity-4.json").relative_to(ROOT))
        d["references"].append({
            "id": ligand_ref,
            "title": "RCSB PDB 11HY deposited phosphatidylethanolamine ligand entity",
            "findings": [{"statement": "The target-matched recombinant crystal structure contains a DPPE phosphatidylethanolamine ligand; the companion 11IF deposition independently contains the same ligand class.", "supporting_text": "DI-PALMITOYL-3-SN-PHOSPHATIDYLETHANOLAMINE"}],
            "reference_review": {"relevance": "HIGH", "correctness": "VERIFIED", "review_notes": "Primary deposited structure record, not a peer-reviewed article or native transport measurement. Construct-to-target sequence identity is separately verified in the preserved structure proof."},
        })
        d["existing_annotations"] = [row(
            "GO:0008429", "phosphatidylethanolamine binding", ligand_ref,
            "Two exact mature-target structures contain a bound phosphatidylethanolamine ligand.",
            "Deposited structures 11HY and 11IF contain the exact Q7VSZ6 mature interval 27–207 preceded by the MAHHHHHH construct tag, each bound to PEF (DPPE). This is direct structural evidence of phosphatidylethanolamine binding by the target and supports the specific ligand-class term rather than a redundant phospholipid-binding parent. It does not establish preferential or exclusive PE binding, native occupancy, transport kinetics or net flux. There are no source annotations or other new MF rows with an ancestor/descendant relationship. The deposition is marked To be published; that limits publication status, not the observed ligand-bound structure.",
            [{"reference_id": ligand_ref, "supporting_text": "DI-PALMITOYL-3-SN-PHOSPHATIDYLETHANOLAMINE"}, {"reference_id": proof_ref}],
        )]
        d["core_functions"][0]["molecular_function"] = {"id": "GO:0008429", "label": "phosphatidylethanolamine binding"}
        d["core_functions"][0]["supported_by"].append(deepcopy(d["existing_annotations"][0]["review"]["supported_by"][0]))
    p.write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))
    notes = p.parent / f"{gene}-notes.md"
    extra = "Replaced generic summaries and downgraded method-only GO_REF relevance; added exact target feature/signature quotations without changing source rows, actions or evidence tiers."
    if gene == "BP3760":
        extra += " Corrected all four PG/PE cargo quotations to the actual E. coli MlaA-assisted MlaC loading sentence; target localization/participation remains inferred from specific architecture and locus, not directly assayed."
    if gene == "BP3761":
        extra = "Added one IDA NEW GO:0008429 for directly observed PE binding in exact mature-target structures 11HY/11IF and refined the corresponding core. No selectivity, native occupancy or flux claim; no redundant GO:0005543 parent row."
    if gene == "ttg2D":
        extra = "Added IDA NEW GO:0005543 and GO:0030288 from direct target cargo and PAO1 tagged-complement periplasmic recovery; expanded the truncated cardiolipin quote. The crystallographic sample was heterologously expressed. No direct native directional-flux claim."
    notes.write_text(notes.read_text() + "\n\n## PR6198 evidence follow-up (2026-11-07)\n\n" + extra + " The earlier no-NEW tally is historical, not a policy barring evidence-supported additions. Prior receipts and provider attempts remain unchanged; the additive consultation records the new decisions.\n")
    print(relative)
