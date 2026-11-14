"""Apply native-context MYCS2 methionine-synthase reviews to frozen seeds."""

import copy
import json
from pathlib import Path

import yaml

A = Path(__file__).resolve().parent
ROOT = A.parents[3]
TERMS = {}
for path in [A / "go-terms.json", A / "additional-terms-ancestors.json"]:
    d = json.loads(path.read_text())["response"]
    TERMS.update({x["id"]: x["name"] for x in d["results"]})


def term(id):
    return {"id": id, "label": TERMS[id]}


def support(ref, quote=None):
    d = {"reference_id": ref}
    if quote:
        d["supporting_text"] = quote
    return d


def decision(action, summary, reason, refs, replacements=None):
    row = {"action": action, "summary": summary, "reason": reason, "supported_by": refs}
    if replacements:
        row["proposed_replacement_terms"] = [term(x) for x in replacements]
    return row


def add_publication(d, pmid, statement, notes):
    meta = yaml.safe_load((ROOT / "publications" / f"PMID_{pmid}.md").read_text().split("---", 2)[1])
    d["references"].append({"id": f"PMID:{pmid}", "title": meta["title"], "publication_type": meta.get("publication_type", "PRIMARY_RESEARCH"),
        "full_text_unavailable": not meta.get("full_text_available", False), "findings": [{"statement": statement}],
        "reference_review": {"relevance": "HIGH", "correctness": "VERIFIED", "review_notes": notes}})


native = support("PMID:33468593", "transcription and translation of metE are strongly attenuated by endogenous cobalamin")
for gene in ["metE", "metH"]:
    seed = json.loads((A.parent / "new-member-seeds" / f"MYCS2-{gene}.json").read_text())
    d = copy.deepcopy(seed["review"])
    d["status"] = "COMPLETE"
    p = ROOT / "genes" / "MYCS2" / gene
    uni = f"file:MYCS2/{gene}/{gene}-uniprot.txt"
    if gene == "metE":
        d["description"] = "MetE/MSMEG_6638 is the full-length, cobalamin-independent methionine synthase of Mycolicibacterium smegmatis mc²155. Its folate- and homocysteine-binding architecture supports zinc-dependent transfer of a methyl group from methyltetrahydrofolate to homocysteine, producing methionine. Unlike compact MesD or MesB proteins, it contains the canonical N-terminal folate-associated and C-terminal catalytic domains. Endogenous cobalamin represses its expression through a riboswitch, favoring the alternative MetH route; when cobalamin synthesis is disabled, MetE can sustain methionine biosynthesis."
        chemistry = support(uni, "Reaction=5-methyltetrahydropteroyltri-L-glutamate + L-homocysteine")
        zinc = support(uni, "Name=Zn(2+)")
        for row in d["existing_annotations"]:
            id = row["term"]["id"]
            if id == "GO:0003871":
                row["review"] = decision("ACCEPT", "Canonical cobalamin-independent folate-dependent methionine synthesis.", "The 771-residue target has both canonical MetE domains and HAMAP MF_00172-supported chemistry. Native33468593 shows the MetE-dependent route operates when endogenous B12 is absent. This combines conserved reaction inference with target genetic/regulatory evidence; it is not a purified-target kinetic or donor-specificity experiment, nor the compact MesD family.", [chemistry, native])
            elif id == "GO:0008270":
                row["review"] = decision("ACCEPT", "Catalytic zinc binding is a supported conserved-function inference.", "Canonical MetE binds zinc to activate homocysteine; target HAMAP/PIRSR support and conserved architecture corroborate that role. Direct zinc-loss/reconstitution evidence is from E. coli8823155, not a target assay. UniProt's one-versus-two zinc stoichiometry statements are unresolved, but both support the binding claim; no specific stoichiometry is asserted.", [zinc, support("PMID:8823155", "zinc is required for catalysis")])
            elif id == "GO:0008652":
                row["review"] = decision("MODIFY", "Refine amino-acid biosynthesis to L-methionine biosynthesis.", "The enzyme directly performs the terminal homocysteine methylation step. The already present L-methionine biosynthetic term is the supported specific descendant; the broader process is true rather than peripheral or false.", [chemistry, native], ["GO:0071265"])
            else:
                row["review"] = decision("ACCEPT", "Direct catalytic participation in L-methionine biosynthesis.", "MetE supplies the methyl-transfer chemistry rather than merely affecting a downstream growth phenotype. Native mc²155 cofactor-context experiments support use of this route when MetH cannot operate; this does not imply that MetE is always expressed or universally essential.", [chemistry, native])
        d["core_functions"] = [{"description": "Methylates homocysteine using methyltetrahydrofolate without cobalamin; the target's native contribution is conditioned by B12-responsive expression.", "molecular_function": term("GO:0003871"), "directly_involved_in": [term("GO:0071265")], "supported_by": [chemistry, native]}]
        add_publication(d, "8823155", "Purified E. coli canonical MetE requires catalytic zinc; this supports conserved chemistry, not a measured MYCS2 stoichiometry.", "Accessible primary abstract; homolog enzymology is explicitly distinguished from target assay evidence.")
        d["suggested_questions"] = [{"question": "What is the target's catalytic versus structural zinc stoichiometry, given the conflicting one- and two-zinc predictions in UniProt?"}]
    else:
        d["description"] = "MetH/MSMEG_4185 is the cobalamin-dependent methionine synthase of Mycolicibacterium smegmatis mc²155. It transfers methyl groups from methyltetrahydrofolate to homocysteine through an enzyme-bound cobalamin intermediate, producing methionine and tetrahydrofolate. Its modular protein contains homocysteine-, folate-, cobalamin- and SAM-associated regions; zinc supports activation of homocysteine. In the native strain, endogenous cobalamin suppresses the alternative MetE route, making MetH necessary under the tested conditions. Disabling cobalamin synthesis relieves that dependence by permitting MetE use."
        chemistry = support(uni, "Reaction=(6S)-5-methyl-5,6,7,8-tetrahydrofolate + L-homocysteine")
        curated = support(uni, "DR   InterPro; IPR011822; MetH.")
        zinc = support(uni, "Name=Zn(2+)")
        for row in d["existing_annotations"]:
            id = row["term"]["id"]
            if id == "GO:0005829":
                row["review"] = decision("ACCEPT", "Soluble cytosolic remethylase location is a supported inference.", "The full-length soluble metabolic-enzyme architecture and conserved MetH assignment support cytosol. The native genetic study assays function, not fractionation, so this remains a conserved localization inference rather than a direct target-localization result.", [curated, native])
            elif id in {"GO:0008168", "GO:0016740"}:
                row["review"] = decision("MODIFY", "Refine general transfer chemistry to methionine synthase activity.", "The specific GO0008705 activity is already present and captures the established folate-to-homocysteine methyl transfer through bound cobalamin. General methyltransferase/transferase terms are true, but the specific descendant is warranted.", [chemistry, native], ["GO:0008705"])
            elif id == "GO:0008270":
                row["review"] = decision("ACCEPT", "Catalytic zinc binding is integral to the remethylase.", "The target carries curated PIRNR/PROSITE zinc-cofactor assignments within the homocysteine-binding domain. This supports a conserved catalytic binding function, without claiming target metal occupancy measurements.", [zinc])
            elif id == "GO:0008705":
                row["review"] = decision("ACCEPT", "Cobalamin-dependent methionine synthase chemistry is supported.", "The complete four-domain target and native33468593 route-dependence data support the inherited MetH function. Homolog primary9201956 resolves the methylcobalamin intermediate and folate-driven cofactor regeneration. Native viability dependence is context-specific and is not a purified-target reaction assay.", [chemistry, native, support("PMID:9201956", "The cofactor is then remethylated by methyltetrahydrofolate.")])
            elif id == "GO:0031419":
                row["review"] = decision("ACCEPT", "Cobalamin binding supports the catalytic intermediate.", "The target's cobalamin-binding domain and PIRSR-supported cofactor assignment match native dependence on endogenous B12. Binding is central to catalysis, not a peripheral broad annotation.", [support(uni, "The B12-binding domain binds the cofactor."), native])
            elif id == "GO:0042558":
                row["review"] = decision("MODIFY", "Refine pteridine metabolism to the directly used tetrahydrofolate pool.", "The enzyme consumes methylated tetrahydrofolate and returns tetrahydrofolate; the existing GO0046653 term is the supported specific descendant. This does not assert folate synthesis or all pteridine metabolism.", [chemistry], ["GO:0046653"])
            elif id == "GO:0046653":
                row["review"] = decision("ACCEPT", "Tetrahydrofolate participates directly in the reaction.", "MetH demethylates the folate donor as it regenerates methylcobalamin, so it performs tetrahydrofolate metabolic chemistry. This is direct catalytic participation, not an indirect cofactor phenotype.", [chemistry])
            elif id == "GO:0046872":
                row["review"] = decision("MODIFY", "Refine general metal binding to catalytic zinc binding.", "The existing GO0008270 term names the target's supported catalytic metal binding. Cobalt within the separately bound cobalamin is not used to invent an additional free-cobalt-binding activity.", [zinc], ["GO:0008270"])
            elif id == "GO:0050667":
                row["review"] = decision("MODIFY", "Resolve homocysteine metabolism to its direct consumption.", "The measured class of remethylase reaction consumes L-homocysteine. Current GO0043418 is an is_a/part_of descendant of this metabolic term and names the supported catabolic direction; its product is methionine, not transsulfuration products.", [chemistry], ["GO:0043418"])
            elif id == "GO:0071265":
                row["review"] = decision("ACCEPT", "Direct terminal reaction of methionine biosynthesis.", "MetH directly produces methionine from homocysteine. Native mc²155 experiments support use of this route under B12-replete conditions; the dependence changes when B12 synthesis is disabled and MetE becomes available.", [chemistry, native])
            else:
                row["review"] = decision("ACCEPT", "Remethylation can regenerate methionine from its derivatives.", "Current GO0071267 includes regeneration from methionine derivatives and is not restricted to the MTA-specific salvage pathway. MetH performs the terminal remethylation when homocysteine arises from SAM turnover, supporting inferred salvage participation. No upstream MTA chemistry, traced native whole-cycle flux, or universal necessity is claimed.", [chemistry, native])
        d["core_functions"] = [{"description": "Transfers methyl from methyltetrahydrofolate to homocysteine through bound cobalamin, supporting methionine production and regeneration when cofactor and substrate are available.", "molecular_function": term("GO:0008705"), "directly_involved_in": [term("GO:0071265"), term("GO:0043418"), term("GO:0046653")], "locations": [term("GO:0005829")], "supported_by": [chemistry, native]}]
        add_publication(d, "9201956", "Canonical MetH uses a methylcobalamin intermediate and distinct substrate/cofactor modules; this is homolog mechanistic evidence.", "Abstract-only modular enzymology; source fragments and residues are not presented as assayed MYCS2 constructs.")
        d["suggested_questions"] = [{"question": "How do native cobalamin availability and MetE derepression divide remethylation flux between the two synthases across growth contexts?"}]
    add_publication(d, "33468593", "Native M. smegmatis mc²155 cobalamin synthesis suppresses MetE and conditions dependence on MetH; B12-deficient backgrounds change route availability.", "Full source read. MYCS2 mc²155 and reference CP000480.1 are explicit; the main text names MSMEG_4185, while MetE identity combines the named native gene with the official reference-genome entry MSMEG_6638. No ADP1 or M. tuberculosis phenotype is assigned to these targets. The authorship correction35289639 does not change the functional result.")
    d["references"].append({"id": uni, "title": f"UniProt record for Mycolicibacterium smegmatis {gene} ({d['id']})", "reference_review": {"relevance": "HIGH", "correctness": "VERIFIED", "review_notes": "Immutable strain/locus and domain/cofactor classifications support conserved-function inference; automatic assertions are not described as target measurements."}, "findings": []})
    (p / f"{gene}-ai-review.yaml").write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))
    notes = f"# {gene} review notes\n\n2026-11-07: All {len(d['existing_annotations'])} seeded rows reviewed, with original ordered payloads and qualifiers preserved and no NEW rows. Full33468593 provides the native mc²155 cofactor/regulatory evidence; ADP1 studies18319726/18840283 do not establish these targets. Official UniProt identity and the paper's CP000480.1 reference-genome context support the source-to-protein bridge; the main text explicitly names MSMEG_4185, whereas the MetE locus mapping relies additionally on the official reference entry.\n\n"
    notes += "The real Falcon attempt returned HTTP403 authentication failure; no provider report was invented. PAINT-loss commands completed but the target accession is absent from its cached tree, so no resolved target loss claim is made. These seeds contain no IBA rows. Fresh QuickGO definitions and applicable ancestry are archived locally. Primary kinetics/cofactor experiments from homologs are separated from native target genetic evidence.\n\n"
    if gene == "metE":
        notes += "Canonical771aa two-domain MetE is distinguished from compact MesD/MesB. Zinc binding is supported; one-versus-two stoichiometry predictions remain unresolved and are not asserted as measurements.\n"
    else:
        notes += "GO0071267 salvage includes regeneration from derivatives, so inferred terminal remethylation is retained without claiming upstream MTA chemistry or a complete traced native SAM-cycle experiment. General metal binding is refined to zinc, and homocysteine metabolism to its directly supported consumption. Cobalamin/riboswitch context prevents a universal-essentiality claim.\n"
    (p / f"{gene}-notes.md").write_text(notes)
