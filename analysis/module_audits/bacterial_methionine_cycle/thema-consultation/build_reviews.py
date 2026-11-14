"""Apply independently adjudicated Thermotoga reviews to frozen seeded payloads."""

import copy
import json
from pathlib import Path

import yaml

A = Path(__file__).resolve().parent
ROOT = A.parents[3]
TERMS = {}
for path in [A / "go-terms.json", A / "additional-terms-ancestors.json", A / "ancestor-terms.json"]:
    d = json.loads(path.read_text())
    d = d.get("response", d)
    TERMS.update({x["id"]: x["name"] for x in d["results"]})


def term(id):
    return {"id": id, "label": TERMS[id]}


def support(ref, quote=None):
    d = {"reference_id": ref}
    if quote:
        d["supporting_text"] = quote
    return d


def review(action, summary, reason, refs, replacements=None):
    d = {"action": action, "summary": summary, "reason": reason, "supported_by": refs}
    if replacements:
        d["proposed_replacement_terms"] = [term(x) for x in replacements]
    return d


def add_ref(d, pmid, findings, access=None):
    meta = yaml.safe_load((ROOT / "publications" / f"PMID_{pmid}.md").read_text().split("---", 2)[1])
    r = {"id": f"PMID:{pmid}", "title": meta["title"], "publication_type": meta.get("publication_type", "PRIMARY_RESEARCH"),
         "full_text_unavailable": not meta.get("full_text_available", False),
         "reference_review": {"relevance": "HIGH", "correctness": "VERIFIED", "review_notes": access or "Primary source read with target and assay scope distinguished."},
         "findings": [{"statement": f} for f in findings]}
    index = next((i for i, x in enumerate(d["references"]) if x["id"] == r["id"]), None)
    if index is None:
        d["references"].append(r)
    else:
        d["references"][index] = r


for gene in ["mtaD", "ahcY"]:
    seed = json.loads((A.parent / "new-member-seeds" / f"THEMA-{gene}.json").read_text())
    d = copy.deepcopy(seed["review"])
    d["status"] = "COMPLETE"
    gene_path = ROOT / "genes" / "THEMA" / gene
    uni = f"file:THEMA/{gene}/{gene}-uniprot.txt"
    scope = "file:THEMA/mtaD/mtaD-source-analysis/23968233-scope.md"
    if gene == "mtaD":
        d["description"] = "Tm0936/MtaD is a zinc-dependent deaminase from Thermotoga maritima MSB8 that converts S-adenosylhomocysteine to S-inosylhomocysteine and 5′-methylthioadenosine to 5′-methylthioinosine. It also deaminates adenosine and 5′-deoxyadenosine in purified-protein assays. Its measured substrate profile favors the sulfur-containing adenosine derivatives in the 2013 comparison. Coupling SAH deamination to the organism's SIH-hydrolyzing AhcY can regenerate homocysteine, although the dominant native substrate and flux through that route remain unresolved. AMP and SAM were not substrates in the original assay."
        primary = support("PMID:17603473", "the purified product of the SAH deamination reaction")
        extra = support(scope, "This extends the directly measured target substrate profile to 5′-deoxyadenosine")
        functions = ["GO:0050270", "GO:0090614", "GO:0004000", "GO:0090613"]
        for a in d["existing_annotations"]:
            id = a["term"]["id"]
            if id in {"GO:0016787", "GO:0016810", "GO:0016814", "GO:0019239"}:
                reason = "The general hydrolytic deamination claim is correct. Primary17603473 and the target row in Table1 of23968233 resolve SAH, MTA, adenosine and 5′-deoxyadenosine activities, so refine to all four supported specific activities rather than discard a true broad annotation. The latter two are measured capacities, not established dominant physiological substrates."
                if a["evidence_type"] == "IBA":
                    reason += " The source is ancestral PTN005182504; Q9X034 among its descendant evidence is legitimate target experimental grounding, not circularity. The PAINT-loss check found no applicable loss; this refinement does not dispute the ancestral deaminase assignment."
                a["review"] = review("MODIFY", "Resolve the measured deaminase substrate profile.", reason, [primary, extra], functions)
                if a["evidence_type"] == "IBA":
                    a["review"]["propagation_review"] = {"root_cause": "TERM_SCOPING_PROBLEM", "failure_modes": ["GRANULARITY_MISMATCH"],
                        "source_entities": [{"source_id": "PANTHER:PTN005182504", "source_status": "SUPPORTS_TRANSFER", "comment": "The ancestral deaminase assertion is biologically sound; direct target substrate assays permit refinement. Q9X034 as descendant evidence is legitimate, not circular. No loss or altered node placement is asserted."}]}
            elif id == "GO:0050270":
                a["review"] = review("ACCEPT", "Directly demonstrated SAH deamination.", "The reaction produces SIH and is independently supported by17603473. Full23968233 Results/Table1 explicitly include purified Tm0936 (sg-8), so the IDA reference is not a wrong-target transfer. Its SAH activity cannot be generalized to all neighboring deaminase subgroups. Native pathway flux remains distinct from the measured reaction.", [primary, extra])
            else:
                a["review"] = review("ACCEPT", "Directly demonstrated MTA deamination.", "Purified Tm0936 deaminates MTA in both primary studies. Retain this substrate-specific chemistry without asserting that its product follows an experimentally established native methionine-salvage route.", [support(uni, "Catalyzes the deamination of 5-methylthioadenosine"), extra])
        d["core_functions"] = []
        for id, desc in [("GO:0050270", "Deaminates SAH to SIH; the chemical capacity is established while native route flux remains unconfirmed."), ("GO:0090614", "Deaminates MTA to methylthioinosine, a second directly measured substrate reaction."), ("GO:0004000", "Deaminates adenosine in vitro; its relative physiological contribution remains unresolved."), ("GO:0090613", "Deaminates 5′-deoxyadenosine in the purified-target substrate panel; native contribution is unestablished.")]:
            if id in {"GO:0004000", "GO:0090613"}:
                continue
            d["core_functions"].append({"description": desc, "molecular_function": term(id), "supported_by": [extra] if id == "GO:0090613" else [primary, extra]})
        d["references"].append({"id": scope, "title": "Target-specific substrate scope from full PMID23968233", "findings": [{"statement": "Tm0936 is directly assayed on four adenosine derivatives; Table1 catalytic efficiencies are distinct from docking ranks."}]})
        add_ref(d, "23968233", ["Tm0936 is the assayed sg-8 target; Table1 reports SAH, MTA, adenosine and 5′-deoxyadenosine activity. Neighboring subgroups have different profiles."], "Normal cache remains abstract-only; full author-hosted publisher PDF was acquired and read, with exact bytes/provenance in thema-consultation and a durable target-scope note.")
        d["suggested_questions"] = [{"question": "Which measured adenosine derivative supplies most native Tm0936 flux, and is SIH passed to AhcY during methionine recycling?"}]
    else:
        d["description"] = "AhcY/TM_0172 is a soluble NAD-dependent adenosylhomocysteinase from Thermotoga maritima MSB8. It reversibly hydrolyzes S-adenosylhomocysteine to adenosine and homocysteine and also hydrolyzes S-inosylhomocysteine to inosine and homocysteine. Both substrates were processed approximately equally in the direct comparative assay. The internal NAD cofactor supports the redox-assisted carbon–sulfur bond cleavage. Its SIH activity can complete the chemical sequence initiated by MtaD-mediated SAH deamination; the contribution of that sequence to native metabolic flux has not been established."
        primary = support("PMID:17603473", "Tm0172 catalyses the formation of homocysteine from either SIH")
        for a in d["existing_annotations"]:
            id = a["term"]["id"]
            if id == "GO:0004013":
                a["review"] = review("ACCEPT", "Target SAH-hydrolase activity is directly demonstrated.", "TM_0172 was purified and assayed on SAH and SIH in17603473. The measured SAH reaction directly corroborates the ancestral PTN000602759 inference and HAMAP-derived electronic annotation. A review's broad motif-based SIH-preference generalization does not override these target-specific results. The PAINT-loss check found no loss on this lineage.", [primary])
            elif id == "GO:0005737":
                a["review"] = review("MODIFY", "Refine the soluble cytoplasmic enzyme to cytosol.", "The HAMAP-supported cytoplasmic assignment, soluble metabolic enzyme architecture, and existing cytosol IBA support the more precise location. This is a localization inference, not a target fractionation experiment.", [support(uni, "SUBCELLULAR LOCATION: Cytoplasm")], ["GO:0005829"])
            elif id == "GO:0005829":
                a["review"] = review("ACCEPT", "Cytosolic location is a supported conserved-function inference.", "The ancestral PTN000602759 cytosol assertion fits the soluble NAD-dependent enzyme and HAMAP cytoplasmic assignment. No target-specific export, membrane anchoring, or lineage loss is established. Keep the inference distinct from experimentally measured localization.", [support(uni, "SUBCELLULAR LOCATION: Cytoplasm")])
            elif id == "GO:0033353":
                a["review"] = review("ACCEPT", "SAH hydrolysis supplies the homocysteine-recycling step.", "The gene product performs the SAH-to-homocysteine chemistry of the cycle, directly supporting inferred participation rather than mere necessity. Retain the PTN000602759 process inference without claiming a complete native cycle flux experiment. Unconfirmed use of the separate MtaD/SIH route does not refute the measured direct SAH reaction.", [primary])
            else:
                a["review"] = review("ACCEPT", "Homocysteine is a direct reaction product.", "The enzyme itself forms homocysteine from SAH and SIH in the purified-target assay, so the homocysteine biosynthetic process is direct catalytic participation, not an indirect phenotype.", [primary])
        ntr = "S-inosyl-L-homocysteine hydrolase activity"
        d["core_functions"] = [{"description": "Hydrolyzes SAH to adenosine and homocysteine as a directly demonstrated capacity consistent with methionine-cycle recycling.", "molecular_function": term("GO:0004013"), "directly_involved_in": [term("GO:0033353"), term("GO:0071269")], "locations": [term("GO:0005829")], "supported_by": [primary]},
            {"description": "Hydrolyzes SIH to inosine and homocysteine; a biochemical alternative entry substrate, without claiming established native MtaD–AhcY flux.", "proposed_molecular_function": ntr, "directly_involved_in": [term("GO:0071269")], "locations": [term("GO:0005829")], "supported_by": [primary]}]
        d["proposed_new_terms"] = [{"proposed_name": ntr, "proposed_definition": "Catalysis of the reaction: S-inosyl-L-homocysteine + H2O = inosine + L-homocysteine.", "proposed_parent": term("GO:0046508"), "justification": "The direct target assay establishes this carbon–sulfur bond hydrolysis. GO0004013 instead specifies the adenine-containing SAH substrate; fresh QuickGO searches found no SIH-specific hydrolase term. This proposal supports the existing core activity without manufacturing a new GOA row.", "supported_by": [primary]}]
        d["suggested_questions"] = [{"question": "How much native homocysteine production derives from direct SAH hydrolysis versus prior SAH deamination to SIH?"}]
    add_ref(d, "17603473", ["Matched T. maritima TM_0936 and TM_0172 enzymes support SAH deamination followed by SIH hydrolysis in vitro; native pathway use remains unconfirmed."])
    d["references"].append({"id": uni, "title": f"UniProt record for Thermotoga maritima {gene} ({d['id']})", "reference_review": {"relevance": "HIGH", "correctness": "VERIFIED", "review_notes": "Immutable target identity, curated/source-attributed chemistry and family context; predictions are distinguished from target assays."}, "findings": []})
    (gene_path / f"{gene}-ai-review.yaml").write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))
    notes = f"# {gene} review notes\n\n2026-11-07: Reviewed all {len(d['existing_annotations'])} seeded annotations, preserving their payloads/order and adding no rows. Read full17603473 and the source-scoped literature consultation. "
    if gene == "mtaD":
        notes += "Full23968233 was recovered from the author archive while its protected normal abstract cache was preserved. Its target Table1 includes 5′-deoxyadenosine as well as SAH, MTA and adenosine; all four specific activities are retained by refinement of existing broad rows. The core synthesis emphasizes SAH/MTA, while the physiological importance of the weaker adenosine/5′-deoxyadenosine capacities remains unresolved. No invented native salvage process was added. The official2PLM/Q9X034 identity is exact406aa.\n\n"
    else:
        notes += "Direct SAH and SIH hydrolysis are both supported. A proposed SIH-specific molecular-function term is linked to the core; no extra annotation row was created. Cytosol and cycle participation remain explicitly inferred; native MtaD-linked flux remains unresolved.\n\n"
    notes += "Actual configured Falcon research attempt failed with HTTP403 authentication failure; no provider report was fabricated. Manual primary-source review supplied the evidence. PAINT-loss command completed and found no applicable loss; source-node reasoning uses phylogeny, not donor counts. Fresh QuickGO definitions/queries and exact logs are archived under the thema consultation. Raw UniProt, GOA, publication caches and seed receipts remain immutable.\n"
    (gene_path / f"{gene}-notes.md").write_text(notes)
