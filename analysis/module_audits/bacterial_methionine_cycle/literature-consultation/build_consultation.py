"""Build and check module-ready reference and evidence objects without editing curation."""

import hashlib
import json
from pathlib import Path

import yaml

from ai_gene_review.datamodel.gene_review_model import EvidenceItem, Reference
from ai_gene_review.validation.supporting_text import build_supporting_text_validator

A = Path(__file__).resolve().parent
REPO = A.parents[3]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(name, obj):
    (A / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def publication(pmid):
    path = REPO / "publications" / f"PMID_{pmid}.md"
    text = path.read_text()
    return yaml.safe_load(text.split("---", 2)[1]), path


def evidence(pmid, statement, quote=None, notes=None):
    meta, _ = publication(pmid)
    row = {"source_id": f"PMID:{pmid}", "title": meta["title"],
           "statement": statement, "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"}
    if quote:
        row["supporting_text"] = quote
    if notes:
        row["notes"] = notes
    return row


STEPS = {
    "sam_synthesis": [evidence("6251075",
        "Purified E. coli MetK catalyzes methionine adenosylation and bound tripolyphosphate hydrolysis; divalent metal and monovalent-cation context matters.",
        "the purified enzyme catalyzes a tripolyphosphatase reaction",
        "Abstract-only primary; do not assume the historical engineered expression strain is identical to every current K-12 reference sequence.")],
    "sah_producing_methylation": [evidence("15916610",
        "E. coli CheR provides a concrete receptor-methylation realization of the distributed SAM-consuming activity; the main review and curated reaction connect this methyl transfer to SAH production.",
        "rates of assisted methylation and demethylation",
        "Reuse main CheR science byte-identically while #6100 owns follow-up. The substrate-specific CheR family is not a universal requirement for bacterial methyl transfer.")],
    "sam_consumption_boundary": [evidence("36891755",
        "Require the actual SAM-to-SAH methyl-transfer reaction: SAM binding, a methyltransferase fold, radical SAM cleavage, or other alkyl transfer does not establish this module role.",
        "Not all enzymes, however, utilize SAM to catalyze methylation reactions.")],
    "direct_sah_hydrolysis": [evidence("33339190",
        "SAH hydrolase reversibly produces adenosine and homocysteine; net hydrolytic flux depends on product clearance, while bound NAD participates in internal redox chemistry.",
        "the equilibrium of the reaction is shifted far towards SAH synthesis",
        "Use this mechanistic review for directionality/context, not proof of activity in an untested homolog.")],
    "pfs_nucleosidase": [evidence("21166890",
        "The Pfs/MtnN branch cleaves SAH to adenine and S-ribosylhomocysteine, requiring the subsequent LuxS step to regenerate homocysteine.",
        "MTA/SAH nucleosidase to produce S-ribosylhomocysteine")],
    "luxs_srh_cleavage": [evidence("11489131",
        "LuxS uses S-ribosylhomocysteine and releases homocysteine plus the precursor of AI-2. The catalytic route is supported independently of downstream signaling phenotypes.",
        "The substrate for LuxS is S-ribosylhomocysteine",
        "Accessible primary abstract names shared biochemical intermediates in E. coli and other bacteria; no universal quorum-sensing requirement follows.")],
    "sah_deamination": [evidence("17603473",
        "T. maritima MSB8 TM_0936/Q9X034 deaminates SAH to SIH. Purified-protein assays and product identity support this reaction, and the exact 2PLM polymer matches current Q9X034.",
        "the purified product of the SAH deamination reaction",
        "Measured enzyme capacity; native SAH flux is not established, and an alternative adenosine-deaminase physiological role remains possible.")],
    "sih_hydrolysis": [evidence("17603473",
        "The matched T. maritima TM_0172/O51933 enzyme releases homocysteine from SIH or SAH approximately equally, supporting two biochemically available entry substrates.",
        "Tm0172 catalyses the formation of homocysteine from either SIH",
        "The paired deamination/hydrolysis route is a capacity inference; the paper explicitly does not confirm native pathway flux. Do not substitute an archaeal hydrolase or assert exclusive SIH specificity.")],
    "canonical_mete": [evidence("8823155",
        "Canonical E. coli MetE directly transfers methyl from methyltetrahydrofolate to homocysteine and requires catalytic zinc; this is distinct from compact MesD/MesB proteins.",
        "the transfer of a methyl group from methyltetrahydrofolate to homocysteine.",
        "Abstract-only direct enzymology; target-specific zinc-loss/reconstitution evidence does not establish every homolog's donor specificity."),
        evidence("15502870", "E. coli canonical MetE can be reversibly inactivated by oxidative glutathionylation; activity availability depends on redox conditions rather than sequence presence alone.",
        "the purified enzyme is inactivated by oxidized glutathione")],
    "canonical_meth": [evidence("9201956",
        "MetH transfers methyl from enzyme-bound methylcobalamin to homocysteine, then uses methyltetrahydrofolate to regenerate methylcobalamin. Cobalamin is a catalytic intermediary, unlike the externally supplied methylcobalamin substrate in the MesB assay.",
        "The cofactor is then remethylated by methyltetrahydrofolate.",
        "Abstract-only modular enzymology; do not use fragment activity as proof that every split protein pairing is functional.")],
    "meth_mete_cofactor_context": [evidence("33468593",
        "In native M. smegmatis mc²155, endogenous cobalamin suppresses MetE and conditions MetH essentiality; B12-deficient backgrounds permit a different route. Neither enzyme is universally essential.",
        "transcription and translation of metE are strongly attenuated by endogenous cobalamin",
        "Use MYCS2 accessions and distinguish this strain from M. tuberculosis. The 2022 correction changes authorship/acknowledgment information."),
        evidence("18840283", "In the tested ADP1 medium, lack of B12 prevents MetH from rescuing loss of the compact synthase, demonstrating a cofactor gate beyond gene presence.",
        "coenzyme-B12 is neither synthesized by A. baylyi nor provided in the experimental media")],
    "mesd_mesx": [evidence("33534785",
        "MesD and MesX form a folate- and cobalamin-independent methionine-synthesis alternative in the characterized S. koreensis DSMZ15582 system. Oxygen is required in the tested complementation context and the physiological methyl donor remains unidentified.",
        "MesD requires an uncharacterized protein family (DUF1852) and oxygen for activity.",
        "Actual cloned loci are Ga0059261_2929 and Ga0059261_2928; no exact current UniProt pair was established for that strain. Do not label these as KT2440 or ADP1 assays."),
        evidence("18319726", "Native ADP1 ACIAD3523/Q6F6Z8 and ACIAD3524/Q6F6Z7 provide a matched genetic pair: loss causes methionine auxotrophy and ACIAD3524 complementation restores prototrophy.",
        "the ACIAD3524 mutant is auxotrophic for methionine",
        "The 2008 article calls the compact synthase metE; 33534785 distinguishes it as MesD. This is not purified ADP1 donor chemistry or an ADP1 oxygen-dependence test.")],
    "mesb_external_corrinoid": [evidence("32034217",
        "Purified D. mccartyi CBDB1 cbdbA481/A0A916P3S8 uses methylcobalamin to methylate homocysteine and fails the tested folate-donor reaction. The physiological corrinoid-protein donor remains unestablished.",
        "the physiological methyl donor might not be soluble methyl(III)cobalamin.",
        "AcsCD donation is hypothesized, not a demonstrated native interface. No complete native cycle is inferred from this partial catalytic exemplar.")],
    "additional_methyl_donor_boundary": [evidence("42570567",
        "X. campestris pv. campestris XC1 uses MesD, S-methylmethionine-dependent MmuM, and split MetHaHb under different donor/cofactor contexts. Thus the represented alternatives must not be described as exhaustive for Bacteria.",
        "MmuM enables XC1 to use plant-derived S-methylmethionine",
        "Abstract only; electronic publication 2026-08-07. Exact XC1 accession/sequence and full-text scope remain unresolved; do not substitute a different Xanthomonas strain.")],
    "sahh_structural_scope": [evidence("42509803",
        "The SAH-hydrolase review summarizes internal NAD redox cycling and variable substrate recognition. Its generalization of pronounced SIH preference to Thermotoga must be reconciled with the target's approximately equal SAH/SIH activity in primary17603473.",
        "redox cycling of the noncovalently bound cofactor NAD+",
        "Do not use broad motif/evolutionary synthesis to infer loss of directly measured SAH activity or to create an unobserved loss node.")],
}

ledger = json.loads((A / "preflight/reference-ledger.json").read_text())
manual = {row["pmid"]: row for row in ledger}
pmids = sorted({e["source_id"].split(":")[1] for values in STEPS.values() for e in values} | {"18953685"})
references = []
for pmid in pmids:
    meta, _ = publication(pmid)
    findings = [{"statement": e["statement"]} for values in STEPS.values() for e in values if e["source_id"] == f"PMID:{pmid}"]
    notes = manual.get(pmid, {}).get("access_scope", "Normal publication cache read; assay and target bounds recorded in step evidence.")
    if pmid == "18953685":
        findings = [{"statement": "The indexed catalytic section supports coupling of methionine adenosylation to bound tripolyphosphate hydrolysis; mammalian isoenzyme regulation is not a universal bacterial mechanism."}]
    if pmid == "33339190":
        notes = "Full review read, emphasizing reversible chemistry, product removal, NAD-dependent internal redox and bacterial/archaeal structural distinctions; descriptions of common routes are not an exhaustive bacterial inventory."
    if pmid == "42509803":
        notes = "Full 2026 review read. Mechanistic NAD discussion is usable; the broad Thermotoga SIH-preference/evolutionary synthesis is not a target assay and is not used to deny its directly measured SAH hydrolysis."
        findings.append({"statement": "The review includes Thermotoga in its generalization of marked preference for hypoxanthine-containing SIH substrates.",
            "finding_review": {"finding_status": "DISPUTED", "review_notes": "The target-specific primary reports approximately equal activity on SIH and SAH; this review generalization cannot establish loss of SAH activity. The general NAD mechanism is retained.",
            "supported_by": [{"reference_id": "PMID:17603473"}]}})
    references.append({"id": f"PMID:{pmid}", "title": meta["title"],
        "publication_type": "REVIEW" if pmid in {"21166890", "18953685", "36891755", "33339190", "42509803"} else meta.get("publication_type", "PRIMARY_RESEARCH"),
        "full_text_unavailable": not meta.get("full_text_available", False), "findings": findings,
        "reference_review": {"relevance": "HIGH", "correctness": "VERIFIED", "review_notes": notes}})

validator, _ = build_supporting_text_validator(REPO / "publications")
checks = []
for ref in references:
    Reference.model_validate(ref)
for step, values in STEPS.items():
    for row in values:
        EvidenceItem.model_validate(row)
        if row.get("supporting_text"):
            result = validator.validate(row["supporting_text"], row["source_id"], expected_title=row["title"])
            assert result.is_valid, (step, result)
            checks.append({"step": step, "reference": row["source_id"], "valid": True})

(A / "module-evidence.yaml").write_text(yaml.safe_dump({"references": references, "step_evidence": STEPS}, sort_keys=False, allow_unicode=True, width=100))
receipt = json.loads((A / "preflight-copy-receipt.json").read_text())
for row in receipt["copies"]:
    assert digest(REPO / row["to"]) == row["sha256"], row["to"]
proof = {"reference_schema_count": len(references), "evidence_schema_count": sum(map(len, STEPS.values())),
         "production_quote_checks": checks, "preflight_copies_exact": len(receipt["copies"]),
         "manually_read_reviews": 5, "full_reviews_available_and_read": 4,
         "partial_review": "18953685 indexed catalytic section, normal cache abstract only",
         "publication_inputs": {str(publication(pmid)[1].relative_to(REPO)): digest(publication(pmid)[1]) for pmid in pmids}}
dump("validation.json", proof)
print(json.dumps({k: v for k, v in proof.items() if k not in {"publication_inputs", "production_quote_checks"}}))
