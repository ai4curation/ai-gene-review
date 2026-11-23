"""Apply localized, manually adjudicated PR6196 follow-up decisions to frozen baselines."""

import copy
import hashlib
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
A = Path(__file__).resolve().parent
BASE = json.loads((A / "baseline.json").read_text())


def norm(s):
    return " ".join(s.split())


def quote(pmid, text):
    assert norm(text) in norm((ROOT / f"publications/PMID_{pmid}.md").read_text()), (
        pmid,
        text,
    )
    return {"reference_id": f"PMID:{pmid}", "supporting_text": text}


MG = quote(
    6251075,
    "Studies with the phosphorothioate derivatives of ATP (ATP alpha S and ATP beta S) in the presence of Mg2+, Mn2+, or Co2+ indicate that a divalent ion is bound to the nucleotide during the reaction and provide information on the stereochemistry of the metal-nucleotide binding site.",
)
MG_STRUCT = quote(
    7629147,
    "Recently, the x-ray structure of the Escherichia coli AdoMet synthetase was solved, and the positions of the two Mg2+ binding sites were identified.",
)
ATP = quote(
    10551856,
    "Initially the sulfur of methionine displaces the intact tripolyphosphate chain (PPP(i)) from ATP, and subsequently PPP(i) is hydrolyzed to PP(i) and P(i) before product release.",
)
DEP = quote(
    8572314,
    "We report optimization of this reaction for assay of cobalamin-dependent methionine synthase to give an economical method for determining enzyme activity that does not require the use of radioactive compounds.",
)
BOUND = quote(
    2271698,
    "Enzyme-bound methylcobalamin then donates its methyl group to homocysteine to generate methionine and cob(I)alamin.",
)
REACTION = quote(
    9201956,
    "Methionine synthase (MetH) catalyzes the transfer of a methyl group from bound methylcobalamin to homocysteine, yielding enzyme-bound cob(I)alamin and methionine. The cofactor is then remethylated by methyltetrahydrofolate.",
)
ZN = quote(
    9398304,
    "Further evidence that zinc is required for catalytic activity comes from experiments in which the zinc is removed from MetH(2-1227).",
)
PASTED = "The cached abstract explicitly treats both enzyme types but does not resolve each folate glutamyl-chain length; the exact MetE substrate distinction is established by the independent full-text source."

AUTHORED_KEYS = {
    "description",
    "summary",
    "reason",
    "statement",
    "review_notes",
    "question",
    "justification",
    "gap_statement",
    "significance",
    "comment",
}
PMIDS = sorted(
    {
        ref["id"].split(":")[1]
        for d in BASE["reviews"].values()
        for ref in d["document"].get("references", [])
        if ref["id"].startswith("PMID:")
    },
    key=len,
    reverse=True,
)
PATTERN = re.compile(r"(?:PMID\s*:?\s*)?(?<!\d)(" + "|".join(PMIDS) + r")(?!\d)")


def fix_citations(obj, events, path=""):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in AUTHORED_KEYS and isinstance(value, str):

                def replace(match):
                    before = value[match.start() - 1] if match.start() else ""
                    after = value[match.end()] if match.end() < len(value) else ""
                    return (
                        (" " if before.isalnum() else "")
                        + "PMID:"
                        + match.group(1)
                        + (" " if after.isalpha() else "")
                    )

                updated = PATTERN.sub(replace, value)
                if updated != value:
                    events.append(
                        {"field": path + "/" + key, "before": value, "after": updated}
                    )
                    obj[key] = updated
            elif key not in {
                "supporting_text",
                "title",
                "original_reference_id",
                "reference_id",
                "id",
                "supporting_entities",
            }:
                fix_citations(value, events, path + "/" + key)
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            fix_citations(value, events, path + f"/{index}")


def main():
    changed = []
    citations = []
    action_changes = []
    for path, saved in BASE["reviews"].items():
        before = saved["document"]
        doc = copy.deepcopy(before)
        parts = Path(path).parts
        org, gene = parts[1:3]
        key = f"{org}/{gene}"
        if key == "ECOLI/cheR":
            continue  # Main-only reused review remains owned by PR6100.
        changes = []
        for row in doc["existing_annotations"]:
            tid, review = row["term"]["id"], row["review"]
            if key == "ECOLI/metK":
                if tid == "GO:0000287":
                    review["supported_by"] = [MG, MG_STRUCT]
                    review["reason"] = (
                        "The purified-enzyme metal-nucleotide experiments in PMID:6251075 explicitly test magnesium, and the structural evidence summarized in PMID:7629147 identifies two Mg2+ sites. Magnesium binding is an integral catalytic cofactor function of methionine adenosyltransferase, so ACCEPT is appropriate. Activity with alternative metals in vitro does not establish their exclusive or equivalent physiological use."
                    )
                elif tid == "GO:0005524":
                    review["supported_by"] = [ATP]
                    review["reason"] = (
                        "ATP is the substrate whose adenosyl group is transferred to methionine; PMID:10551856 explicitly describes ATP engagement and tripolyphosphate cleavage. Binding it is integral to the core reaction, rather than a peripheral property. This conclusion does not rely on the residual activity of cysteine mutants or on a metal-binding rationale."
                    )
                elif tid == "GO:0030955":
                    review["reason"] = (
                        "PMID:7629147 links Glu42, potassium binding and monovalent-cation activation to SAM-synthesis turnover. This is a central catalytic cofactor interaction, not a separate sensor function or a peripheral activity; accept the precise binding claim alongside the complete catalytic reaction."
                    )
                if tid in {"GO:0000287", "GO:0005524", "GO:0030955"}:
                    review["action"] = "ACCEPT"
                    changes.append(
                        "Attach substrate/cofactor-specific evidence and classify integral catalytic binding as core."
                    )
                if tid == "GO:0042802":
                    review["reason"] += (
                        " The ontology check confirms GO:0051289 protein homotetramerization is a biological process, whereas GO:0042803 is the molecular activity of forming each observed homodimer; it does not deny the complete dimer-of-dimers tetramer."
                    )
                    changes.append(
                        "Make the checked MF/BP distinction for dimer and tetramer explicit."
                    )
            if key == "ECOLI/metH":
                review["reason"] = review["reason"].replace(PASTED, "").strip()
                if row["original_reference_id"] == "PMID:8572314" and tid in {
                    "GO:0031419",
                    "GO:0008705",
                    "GO:0071265",
                }:
                    review["supported_by"] = [
                        DEP,
                        BOUND if tid == "GO:0031419" else REACTION,
                    ]
                    review["reason"] += (
                        " PMID:8572314 explicitly assays the cobalamin-dependent enzyme; its separate cobalamin-independent assay extension is not evidence for this MetH claim."
                    )
                    changes.append(
                        "Replace the MetE-side quote with the cobalamin-dependent assay and claim-specific MetH mechanism."
                    )
                if tid == "GO:0035999":
                    review["reason"] = (
                        "MetH directly consumes 5-methyltetrahydrofolate and regenerates tetrahydrofolate while producing methionine. This performs the methyl-transfer/regeneration work included in the folate cycle; PMID:9201956 supports that chemistry. The judgement does not depend on MetE's folate glutamyl-chain preference."
                    )
                    changes.append(
                        "Replace pasted MetE prose with the actual folate-cycle reaction rationale."
                    )
                if tid == "GO:0031419":
                    review["action"] = "ACCEPT"
                    review["reason"] = review["reason"].replace(
                        "Retain the precise cofactor-binding property alongside the complete catalytic core",
                        "Accept this central catalytic cofactor-binding function alongside the complete reaction",
                    )
                    if BOUND not in review["supported_by"]:
                        review["supported_by"].append(BOUND)
                    changes.append(
                        "Retain cobalamin binding as a central, mechanistically evidenced MetH activity."
                    )
                if tid == "GO:0008270":
                    review["action"] = "ACCEPT"
                    review["supported_by"].append(ZN)
                    review["reason"] += (
                        " Zinc activates the homocysteine substrate and is required for this catalytic half-reaction, so this precise binding function is core rather than peripheral."
                    )
                    changes.append(
                        "Classify directly established catalytic zinc binding as core."
                    )
            if key == "THEMA/mtaD" and review["action"] == "MODIFY":
                review["proposed_replacement_terms"] = [
                    t
                    for t in review["proposed_replacement_terms"]
                    if t["id"] in {"GO:0050270", "GO:0090614"}
                ]
                tail = (
                    review["reason"][
                        review["reason"].find(" The source is ancestral") :
                    ]
                    if " The source is ancestral" in review["reason"]
                    else ""
                )
                review["summary"] = (
                    "Refine to the supported SAH/MTA functions and separate measured side activities."
                )
                review["reason"] = (
                    "The general hydrolytic deamination claim is correct. Refine to SAH and MTA deaminase functions, supported by PMID:17603473 and the target row of PMID:23968233 Table 1. Adenosine and 5′-deoxyadenosine deamination are real measured activities, but no native utilization or distinct secondary physiological function is established. Under ENZYME_SPECIFICITY they belong to the MARK_AS_OVER_ANNOTATED tier (in-vitro activity, physiological relevance unknown), not coequal positive replacement terms. The 2013 efficiencies favor SAH/MTA, but the 2007 assay gives a smaller separation; no universal numerical cutoff or disproven activity is claimed. The bounded database search did not identify a separately established native adenosine deaminase, which is not proof of genomic absence and does not justify a REMOVE/noise judgement. Retain the measurements in findings and notes without inventing new rows."
                    + tail
                )
                changes.append(
                    "Narrow five replacement lists to SAH/MTA; retain measured side activities as explicitly MAOA-tier findings."
                )
            if key == "ECOLI/mmuM":
                if tid == "GO:0033528":
                    review["reason"] = (
                        "The unresolved question is whether the native E. coli context supports the S-methylmethionine cycle asserted at PAINT node PTN001843930; the underlying IBD evidence has not been completely adjudicated. The defined cycle requires a SAM-to-SMM leg as well as MmuM-mediated homocysteine methylation. PMID:9882684 demonstrates imported-SMM utilization, not the complementary endogenous leg. This is lack of demonstration, not evidence that E. coli cannot perform that leg. The official tree verifies Q47690 leaf PTN001078917 descends from the source node, but ancestry and a genuine catalytic reaction alone do not settle the native cycle context. Therefore retain UNDECIDED rather than infer a loss or assert that the experimentally demonstrated methyl transfer is absent."
                    )
                    changes.append(
                        "Clarify that unadjudicated native cycle/IBD scope, not a demonstrated missing reaction, motivates UNDECIDED."
                    )
                if tid == "GO:0008270":
                    review["action"] = "ACCEPT"
                    review["reason"] += (
                        " The target-identical metallated structure places zinc in the substrate-binding active-site pocket, making this a core mechanistic property rather than a peripheral binding observation. Native occupancy and a separate regulatory metal role are not inferred."
                    )
                    changes.append(
                        "Classify the target-identical active-site zinc-binding structure as core."
                    )
            if key == "ECOLI/metE" and tid == "GO:0008270":
                review["action"] = "ACCEPT"
                review["reason"] += (
                    " Zinc removal abolishes catalytic activity and reconstitution restores it in PMID:8823155; its substrate-activating binding role is core, not peripheral."
                )
                changes.append(
                    "Classify directly measured catalytic zinc binding as core."
                )
            if key == "PSEPK/metH":
                if tid == "GO:0005829":
                    rid = "file:analysis/module_audits/bacterial_methionine_cycle/review-followup/metH-source-observation.md"
                    text = "The frozen Q88KB5 record has five DOMAIN feature intervals spanning the four functional modules; it has no annotated SIGNAL or TRANSMEM feature."
                    assert text in (A / "metH-source-observation.md").read_text()
                    review["supported_by"] = [
                        {"reference_id": rid, "supporting_text": text},
                        {
                            "reference_id": "file:PSEPK/metH/metH-uniprot.txt",
                            "record_section": ["CC:DOMAIN"],
                            "supporting_text": "Modular enzyme with four functionally distinct domains.",
                        },
                    ]
                    changes.append(
                        "Replace self-identical support with independently recorded target feature observations and the curated domain statement."
                    )
                if tid in {"GO:0008270", "GO:0031419"}:
                    review["action"] = "ACCEPT"
                    review["reason"] = (
                        "The specific PIRNR/PIRSR-supported target cofactor assignment and the complete MetH architecture support "
                        + (
                            "zinc binding at the homocysteine-activation site"
                            if tid == "GO:0008270"
                            else "bound methylcobalamin as the methyl-transfer intermediate"
                        )
                        + ". This is a conserved catalytic role and is core, not peripheral. Direct E. coli mechanism is comparator evidence, not a native KT2440 cofactor-occupancy measurement."
                    )
                    changes.append(
                        "Classify specifically inferred catalytic MetH cofactor binding as core, retaining the native-assay limit."
                    )
            if key == "PSEPK/metK" and tid in {"GO:0000287", "GO:0005524"}:
                review["action"] = "ACCEPT"
                review["summary"] = (
                    "The target's catalytic MetK substrate/cofactor binding is core."
                )
                review["reason"] += (
                    " These HAMAP-supported catalytic substrate/cofactor contacts are integral to the conserved reaction rather than peripheral; ACCEPT reflects that role without claiming a direct KT2440 assay."
                )
                changes.append(
                    "Classify HAMAP-supported catalytic ATP/magnesium binding as core."
                )
            if key == "ECOLI/luxS" and tid == "GO:0005506":
                review["action"] = "ACCEPT"
                review["reason"] = (
                    "The reviewed target UniProt record assigns an Fe cofactor by similarity, and PMID:12705835 establishes catalytic metal involvement and Fe2+ preference for the studied LuxS enzyme. The accessible abstract does not identify its source organism, so it is mechanistic comparator evidence, not a claimed E. coli native occupancy assay. Together with the specific target LuxS assignment this supports the conserved catalytic iron-binding role. A catalytic cofactor is core rather than peripheral; the existence of active metal-substituted preparations does not imply equal physiological use of every metal."
                )
                review["supported_by"].append(
                    quote(
                        12705835,
                        "Comparison of the catalytic properties and stability of the metal-substituted LuxS with those of the native enzyme revealed that the native metal ion is Fe(2+).",
                    )
                )
                changes.append(
                    "Classify inferred catalytic iron binding as core, with explicit organism/access limits for the newly read primary comparator."
                )
        if key == "ECOLI/metH":
            ref = next(r for r in doc["references"] if r["id"] == "PMID:8572314")
            ref["findings"] = [
                {
                    "statement": "The paper directly describes an assay of the cobalamin-dependent methionine synthase; its separate MetE assay extension is not support for MetH.",
                    "supporting_text": DEP["supporting_text"],
                }
            ]
            ref["reference_review"]["review_notes"] = (
                "The cached primary abstract explicitly distinguishes the cobalamin-dependent assay from its extension to cobalamin-independent methionine synthase. The former is relevant to MetH; the abstract is not a direct structural occupancy measurement, so independent bound-cofactor kinetics are cited for cobalamin binding."
            )
        if key == "ECOLI/luxS":
            source = (ROOT / "publications/PMID_12705835.md").read_text()
            title = yaml.safe_load(source.split("---", 2)[1])["title"]
            doc["references"].append(
                {
                    "id": "PMID:12705835",
                    "title": title,
                    "full_text_unavailable": True,
                    "findings": [
                        {
                            "statement": "Metal-substitution studies support catalytic Fe2+ in the studied LuxS protein. The accessible abstract does not specify its source organism; target transfer remains qualified.",
                            "supporting_text": "Comparison of the catalytic properties and stability of the metal-substituted LuxS with those of the native enzyme revealed that the native metal ion is Fe(2+).",
                        }
                    ],
                    "reference_review": {
                        "relevance": "HIGH",
                        "correctness": "VERIFIED",
                        "review_notes": "Newly fetched normal cache is abstract-only and preserved. The metal-substitution and catalytic conclusion is explicit; no E. coli-specific strain or complete construct is inferred from this abstract.",
                    },
                }
            )
        if key == "PSEPK/metH":
            doc["references"].append(
                {
                    "id": "file:analysis/module_audits/bacterial_methionine_cycle/review-followup/metH-source-observation.md",
                    "title": "Independent inspection of the frozen KT2440 MetH domain/topology annotations",
                    "findings": [
                        {
                            "statement": "The specific target architecture supports a cytosolic inference but is not an experimental localization measurement.",
                            "supporting_text": "The frozen Q88KB5 record has five DOMAIN feature intervals spanning the four functional modules; it has no annotated SIGNAL or TRANSMEM feature.",
                        }
                    ],
                }
            )
        events = []
        fix_citations(doc, events)
        if events:
            changes.append(
                "Repair malformed PMID references in authored prose; source payloads, quotations and fetched titles remain unchanged."
            )
            citations.extend({"review": path, **x} for x in events)
        if doc == before:
            continue
        for i, (old, new) in enumerate(
            zip(
                before["existing_annotations"], doc["existing_annotations"], strict=True
            )
        ):
            assert {k: v for k, v in old.items() if k != "review"} == {
                k: v for k, v in new.items() if k != "review"
            }
            if old["review"]["action"] != new["review"]["action"]:
                action_changes.append(
                    {
                        "review": path,
                        "row": i,
                        "term": new["term"]["id"],
                        "before": old["review"]["action"],
                        "after": new["review"]["action"],
                    }
                )
        file = ROOT / path
        file.write_text(
            yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100)
        )
        notes = file.parent / f"{gene}-notes.md"
        # Always append to the pre-follow-up notes, so reruns are deterministic.
        original = (A / "prior-notes" / f"{org}-{gene}.md").read_text()
        notes.write_text(
            original.rstrip()
            + "\n\n## PR6196 evidence follow-up, 2026-11-07\n\n"
            + "\n".join("- " + x for x in dict.fromkeys(changes))
            + "\n\nSource adjudication and additive receipt: analysis/module_audits/bacterial_methionine_cycle/review-followup/. Original rows, qualifiers and prior audit artifacts are preserved.\n"
        )
        changed.append(
            {
                "organism": org,
                "gene": gene,
                "review": path,
                "before_sha256": saved["sha256"],
                "after_sha256": hashlib.sha256(file.read_bytes()).hexdigest(),
                "changes": list(dict.fromkeys(changes)),
            }
        )
    (A / "changed-genes.json").write_text(json.dumps(changed, indent=2) + "\n")
    (A / "action-changes.json").write_text(json.dumps(action_changes, indent=2) + "\n")
    (A / "citation-prose-changes.json").write_text(
        json.dumps(citations, indent=2) + "\n"
    )
    print([(x["organism"], x["gene"]) for x in changed])


if __name__ == "__main__":
    main()
