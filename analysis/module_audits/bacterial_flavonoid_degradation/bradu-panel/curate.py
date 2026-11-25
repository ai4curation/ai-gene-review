"""Curate the frozen BRADU seed; never fetch or modify machine sources."""

import json
from pathlib import Path
import yaml

OUT = Path("analysis/module_audits/bacterial_flavonoid_degradation/bradu-panel")
BASE = json.loads(
    Path(
        ".cache/module-audit-logs/flavonoid-20261106/bradu-seed-baseline.json"
    ).read_text()
)
AN = "file:analysis/module_audits/bacterial_flavonoid_degradation/bradu-panel/source-evidence.md"
DATA = json.loads((OUT / "sequence-comparison.json").read_text())
LABELS = {
    "GO:0016709": "oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen",
    "GO:0016702": "oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of two atoms of oxygen",
    "GO:0016787": "hydrolase activity",
    "GO:0051537": "2 iron, 2 sulfur cluster binding",
    "GO:0003824": "catalytic activity",
}


def term(i):
    return {"id": i, "label": LABELS[i]}


def sup(r, q, section=None):
    x = {"reference_id": r, "supporting_text": q}
    if section:
        x["record_section"] = [section]
    return x


def ptitle(n):
    return yaml.safe_load(
        Path(f"publications/PMID_{n}.md").read_text().split("---")[1]
    )["title"]


def review(action, summary, reason, support, repl=None):
    x = {
        "action": action,
        "summary": summary,
        "reason": reason,
        "supported_by": support,
    }
    if repl:
        x["proposed_replacement_terms"] = [term(repl)]
    return x


for row in BASE:
    g = row["gene"]
    p = Path(row["path"])
    d = yaml.safe_load(row["seed_text"])
    u = f"file:BRADU/{g}/{g}-uniprot.txt"
    s = DATA[g]

    def us(q):
        return sup(u, q, "DR:InterPro")

    aline = next(
        line[2:]
        for line in (OUT / "source-evidence.md").read_text().splitlines()
        if line.startswith("- " + g + " versus")
    )
    ass = sup(AN, aline)
    domain = {
        "bll6421": "InterPro; IPR001509; Epimerase_deHydtase.",
        "bll6422": "InterPro; IPR011234; Fumarylacetoacetase-like_C.",
        "bll6423": "InterPro; IPR013096; Cupin_2.",
        "bll6425": "InterPro; IPR050493; FAD-dep_Monooxygenase_BioMet.",
        "bll6426": "InterPro; IPR017941; Rieske_2Fe-2S.",
        "bll6427": "InterPro; IPR004360; Glyas_Fos-R_dOase_dom.",
        "bll6428": "InterPro; IPR050261; FrsA_esterase-like.",
    }[g]
    support = [us(domain), ass]
    bios = {
        "bll6421": "Bll6421 is a Rossmann-fold epimerase/dehydratase-family protein in a conserved aromatic-compound catabolic locus of Bradyrhizobium diazoefficiens USDA 110. It is related to Herbaspirillum FdeJ, but neither a nucleotide-sugar substrate nor the proposed oxaloacetate-releasing flavonoid-intermediate reaction has been established for this protein. Its physiological substrate and molecular function remain unresolved.",
        "bll6422": "Bll6422 is a fumarylacetoacetate-hydrolase-fold enzyme candidate in a conserved aromatic-compound catabolic locus of Bradyrhizobium diazoefficiens USDA 110. It is related to FdeI proteins; the fold accommodates several reaction classes, and the proposed late flavonoid-intermediate decarboxylation and dehydration reactions remain unassigned experimentally. Its native substrate and reaction are unknown.",
        "bll6423": "Bll6423 is a cupin type-2 protein in a conserved aromatic-compound catabolic locus of Bradyrhizobium diazoefficiens USDA 110. It is related to Herbaspirillum FdeH. Cupins in the related Variovorax isoflavone pathway catalyze downstream intermediate conversion, but the substrate and biochemical contribution of Bll6423 have not been established; it is not known to be an obligatory ring-cleavage partner.",
        "bll6425": "Bll6425 is a predicted FAD-dependent, NAD(P)H-utilizing monooxygenase of Bradyrhizobium diazoefficiens USDA 110, encoded in an aromatic-compound catabolic locus related to the Herbaspirillum fde locus. Sequence and domain evidence support the oxygen-incorporating reaction class. Its physiological substrate, hydroxylation position and NADH-versus-NADPH preference are unresolved; related flavonoid monooxygenases differ in substrate range.",
        "bll6426": "Bll6426 is a small Rieske [2Fe-2S]-binding protein of Bradyrhizobium diazoefficiens USDA 110 encoded in an aromatic-compound catabolic locus. It is related to FdeD, with a plausible electron-carrier role, but its donor, acceptor and physiological requirement are unknown. A specific electron-transfer partnership with the neighboring monooxygenase Bll6425 has not been demonstrated.",
        "bll6427": "Bll6427 is a metal-binding VOC-superfamily protein of Bradyrhizobium diazoefficiens USDA 110. Whole-protein similarity to Herbaspirillum FdeC and conserved catabolic-locus context support an inferred aromatic-ring dioxygenase activity. Its physiological substrate, cleavage position and metal identity are untested. The shared glyoxalase-I signature also produces a lactoylglutathione-lyase prediction whose substrate specificity remains unresolved.",
        "bll6428": "Bll6428 is an alpha/beta-fold hydrolase of the FrsA-like family in an aromatic-compound catabolic locus of Bradyrhizobium diazoefficiens USDA 110. It is closely related to Herbaspirillum FdeB, but exact ester-versus-carbon-carbon bond specificity and the proposed flavonoid-derived lactone substrate remain unresolved. Its S9-like catalytic-domain annotation does not independently establish physiological peptide hydrolysis.",
    }
    d["description"] = bios[g]
    d["status"] = "COMPLETE"
    d.setdefault("existing_annotations", [])
    d.setdefault("references", [])
    for a in d["existing_annotations"]:
        i = a["term"]["id"]
        if g == "bll6422":
            a["review"] = review(
                "ACCEPT",
                "FAH-family architecture supports an enzyme, without resolving the reaction class.",
                "The target has the N-terminal FAA_hydro_N and C-terminal FAH domains and strong full-length similarity to Hsero_1011. This supports catalytic activity, but this superfamily includes hydrolases, hydratases and decarboxylases. KEGG late-pathway assignments are hypotheses rather than independent biochemical evidence, so GO:0003824 is as specific as currently justified.",
                support,
            )
        if g == "bll6425":
            if i == "GO:0004497":
                a["review"] = review(
                    "MODIFY",
                    "Retain monooxygenation and refine the supported donor/oxygen-incorporation class.",
                    "The PAINT IBD at PTN002492679 asserts monooxygenase activity and is not rejected. The exact target FAD-dependent monooxygenase domain, near-full-length similarity to HERSS FdeE, and NAD(P)H-linked chemistry of characterized FdeE/IfcA support the existing GO:0016709 descendant. This is granularity, not evolutionary loss; substrate specificity and NADPH exclusivity are not transferred. The lineage loss check found no IRD/IKR.",
                    support,
                    "GO:0016709",
                )
                a["review"]["propagation_review"] = {
                    "root_cause": "TERM_SCOPING_PROBLEM",
                    "failure_modes": ["GRANULARITY_MISMATCH"],
                    "source_entities": [
                        {
                            "source_id": "PANTHER:PTN002492679",
                            "comment": "Cached IBD GO:0004497, seed UniProtKB:Q9HWG9. Broad activity retained; only resolution changes.",
                        },
                        {
                            "source_id": "UniProtKB:Q9HWG9",
                            "comment": "Actual PAINT seed, not replaced by HERSS experimental support.",
                        },
                    ],
                }
            elif i == "GO:0016709":
                a["review"] = review(
                    "ACCEPT",
                    "Conserved flavoprotein monooxygenase architecture supports the NAD(P)H-dependent reaction class.",
                    "The reaction-class inference combines target domains with 54.2% aligned identity to the experimentally characterized FdeE over 99.7% of target residues. HERSS FdeE and Variovorax IfcA establish this class but differ in substrate range; no exact naringenin or isoflavone substrate, hydroxylation position, or exclusive NADPH preference is asserted for USDA110.",
                    support
                    + [
                        sup(
                            "PMID:39107441",
                            "Like LjF8H33 and RgF8H25, it showed an absolute requirement for NADPH, while the addition of FAD to the reaction mixture containing the NADPH coenzyme did not result in changes in activity, as also was described for LjF8H33.",
                        )
                    ],
                )
            else:
                a["review"] = review(
                    "ACCEPT",
                    "The target carries the conserved FAD-binding domain of flavoprotein monooxygenases.",
                    "IPR002938 and the FAD/NAD-binding architecture independently support flavin-cofactor binding. This is an inference from the target sequence, not an experimental measurement of BRADU flavin occupancy.",
                    [us("InterPro; IPR002938; FAD-bd."), ass],
                )
        if g == "bll6426":
            a["review"] = review(
                "ACCEPT",
                "Rieske architecture supports [2Fe-2S] cluster binding.",
                "The compact target has Rieske domain and superfamily classifications and curated sequence-based ligand features. These support the cofactor-binding function without identifying an electron donor or acceptor. Autonomous NADPH-dependent HERSS FdeE activity does not exclude another physiological role for FdeD, but it prevents an obligatory FdeD-to-FdeE assignment from locus adjacency alone.",
                support,
            )
        if g == "bll6427":
            if i == "GO:0004462":
                a["review"] = review(
                    "UNDECIDED",
                    "Glyoxalase-I substrate specificity is unresolved in this FdeC-related VOC protein.",
                    "IPR018146 is a glyoxalase-I signature, and glyoxalase I genuinely belongs to the VOC superfamily. This is not the unrelated glyoxalase-II fold error found in the HERSS submitter record. Whole-protein similarity to FdeC and catabolic-locus context favor a ring-cleavage role, but neither evidence proves absence of lactoylglutathione-lyase activity. No target assay or discriminatory substrate analysis resolves the competing assignments.",
                    support + [us("InterPro; IPR018146; Glyoxalase_1_CS.")],
                )
            else:
                a["review"] = review(
                    "ACCEPT",
                    "Metal-dependent VOC catalytic architecture supports broad metal-ion binding.",
                    "Both the glyoxalase-I interpretation and the FdeC-like extradiol-dioxygenase interpretation entail a metal-dependent catalytic scaffold. The conserved VOC domain and signature support the broad binding claim, while neither iron identity nor stoichiometry is established for this target.",
                    support,
                )
        if g == "bll6428":
            if i in ["GO:0006508", "GO:0008236"]:
                a["review"] = review(
                    "MARK_AS_OVER_ANNOTATED",
                    "The S9-like catalytic fold does not establish peptide-bond hydrolysis.",
                    "The source maps a catalytic-domain signature shared with non-peptidase hydrolases. Family-level FrsA-like architecture and 81.0% aligned identity to FdeB favor a small-molecule hydrolase in this catabolic locus. These are reasons to regard physiological peptidase/proteolysis specificity as over-annotation, not a negative peptide assay or demonstrated evolutionary loss. The exact native bond and substrate remain untested.",
                    support,
                )
            elif i == "GO:0016787":
                a["review"] = review(
                    "ACCEPT",
                    "Broad hydrolysis is supported without choosing an untested substrate or bond class.",
                    "The PAINT IBD PTN007719808 is grounded in the FrsA seed P04335 and agrees with target alpha/beta-hydrolase and FrsA-like family architecture. The lineage loss check found no IRD/IKR. Family members include ester and carbon-carbon hydrolases, so the broad parent remains the most secure shared activity; it is not refined solely from KEGG R13077.",
                    support,
                )
            else:
                a["review"] = review(
                    "UNDECIDED",
                    "Ester versus carbon-carbon hydrolysis is not resolved by the available family evidence.",
                    "FrsA-like classification and FdeB locus homology make ester hydrolysis plausible, but do not distinguish it from carbon-carbon hydrolysis in this mixed hydrolase family. KEGG R13077 is a predicted lactone reaction, not an independently measured USDA110 substrate. Retain uncertainty rather than accept ARBA specificity from the family label or reject a chemically plausible reaction.",
                    support,
                )
    if g == "bll6427":
        d["existing_annotations"].append(
            {
                "term": term("GO:0016702"),
                "evidence_type": "ISS",
                "original_reference_id": "PMID:27059806",
                "supporting_entities": ["UniProtKB:D8J0W7"],
                "qualifier": "enables",
                "review": review(
                    "NEW",
                    "Infer an oxygen-incorporating ring-cleavage activity from the FdeC homolog and target architecture.",
                    "The target aligns to genetically characterized HERSS FdeC with 59.9% identity across 96.8% of its residues, shares the VOC scaffold, and occupies the corresponding conserved catabolic locus. FdeC-mutant accumulation of the hydroxylated precursor supports oxygenolytic ring cleavage together with its extradiol architecture. This supports a reaction-class ISS inference without requiring a purified BRADU assay. It does not establish exact substrate, product, metal, or native pathway flux, nor refute the unresolved glyoxalase-I prediction. No original row or proposed term is an ancestor or descendant of this dioxygenase class.",
                    support
                    + [
                        sup(
                            "PMID:27059806",
                            "that is subsequently dioxygenated and cleaved at the A-ring by the FdeC dioxygenase, since the latter compound accumulated in the fdeC strain.",
                        )
                    ],
                ),
            }
        )
    core = {
        "bll6422": (
            "GO:0003824",
            "Inferred catalytic activity of a FAH-fold enzyme; substrate and reaction class unresolved.",
        ),
        "bll6425": (
            "GO:0016709",
            "Inferred NAD(P)H-dependent flavin monooxygenation; aromatic substrate and hydroxylation position unresolved.",
        ),
        "bll6426": (
            "GO:0051537",
            "Rieske [2Fe-2S] cofactor binding in a putative electron carrier with unknown physiological partners.",
        ),
        "bll6427": (
            "GO:0016702",
            "Inferred oxygenolytic aromatic-ring cleavage by a FdeC-related VOC protein; exact substrate and metal unresolved.",
        ),
        "bll6428": (
            "GO:0016787",
            "Hydrolysis by a FrsA-like alpha/beta-hydrolase; physiological bond class and substrate unresolved.",
        ),
    }
    if g in core:
        i, desc = core[g]
        d["core_functions"] = [
            {
                "description": desc,
                "molecular_function": term(i),
                "supported_by": support,
            }
        ]
        if g == "bll6427":
            d["core_functions"][0]["supported_by"] += d["existing_annotations"][-1][
                "review"
            ]["supported_by"][-1:]
    refs = [
        {
            "id": u,
            "title": f"Frozen UniProtKB {row['accession']} record for USDA110 {g}",
            "findings": [
                {
                    "statement": "Target domain classification supports the family-level inference.",
                    "record_section": ["DR:InterPro"],
                    "supporting_text": domain,
                }
            ],
        },
        {
            "id": AN,
            "title": "BRADU frozen-sequence comparison and primary-source boundaries",
            "findings": [
                {
                    "statement": "Sequence comparison identifies the related HERSS locus protein without proving identical specificity.",
                    "supporting_text": aline,
                }
            ],
        },
    ]
    for n in ["23125118", "27059806", "39107441", "38707841"]:
        refs.append(
            {
                "id": "PMID:" + n,
                "title": ptitle(n),
                "reference_review": {
                    "relevance": "MEDIUM",
                    "correctness": "VERIFIED",
                    "review_notes": "Comparative evidence; this paper does not assay the USDA110 target. HERSS genetics and purified FdeE, and Variovorax Ifc activities, must retain their strain and substrate limits.",
                },
            }
        )
    d["references"] += refs
    d["knowledge_gaps"] = [
        {
            "gap_statement": f"The physiological substrate and native catabolic contribution of USDA110 {g} remain unresolved.",
            "gap_kind": ["BIOLOGY"],
            "status": "OPEN",
            "boundary": "Conserved locus and protein-family evidence support a candidate relationship to Fde proteins; they do not demonstrate a naringenin-specific route, interchangeable Ifc activity, or every predicted late reaction.",
            "significance": "Substrate divergence and uncertain partners prevent assigning complete native pathway capability.",
            "resolution": "Compare target activity on defined flavonoid/isoflavone and alternative family substrates, then connect product identification to native gene perturbation and metabolite profiles.",
            "provenance": [
                sup(AN, "although their functions in these organisms remain unknown")
            ],
        }
    ]
    if g in ["bll6421", "bll6423"]:
        d["knowledge_gaps"][0]["gap_statement"] = (
            f"The molecular activity and native substrate of {g} are unknown despite conserved family and locus membership."
        )
    d["suggested_questions"] = [
        {
            "question": "Does this USDA110 locus act on naringenin, isoflavones, another aromatic substrate, or multiple substrates under different conditions?"
        }
    ]
    p.write_text(yaml.safe_dump(d, sort_keys=False, width=95, allow_unicode=True))
    notes = f"""# {g} review notes\n\n## 2026-11-06 annotation review\n\nIdentity: {row["accession"]}, frozen official USDA110 taxon224911 record; retain locus symbol {g}. The 2013 paper's Bradyrhizobium japonicum USDA110 name is the historical name of this strain. It describes related operon organization, explicitly leaving function unknown.\n\n{aline}\n\n{bios[g]}\n\nReviewed every seeded annotation; preserved each non-review payload and ordering. No new biological-process assertion: candidate locus membership is useful context, but the actual work of this protein in a USDA110 flavonoid reaction remains inferential and competing substrate/partner roles are not resolved. This is not a universal demand for direct assays; reaction-class inference is accepted where sequence, architecture and characterized homolog chemistry agree. No BP comparator query was used to manufacture a gap.\n\nResearch: genuine default-provider Falcon request (`just deep-research BRADU {g} --provider falcon`) failed with HTTP403 authentication error. No provider research file was created. Manual assessment uses frozen target record, primary PMID23125118, PMID27059806, PMID39107441 and PMID38707841 and the scoped source evidence and sequence comparison in `analysis/module_audits/bacterial_flavonoid_degradation/bradu-panel/`. These primaries are comparative, never target enzyme assays. Existing source files were not refreshed.\n\nCore synthesis retains only supported reaction classes/cofactor properties. No precise molecular-function core is supplied for uncharacterized cupin/epimerase candidates solely to fill the module.\n"""
    if g in ["bll6425", "bll6428"]:
        notes += "\nPAINT: normal lineage-loss query found no IRD/IKR. Cached IBD and actual seed were inspected; broad family function is retained and no evolutionary loss is claimed.\n"
    (p.parent / (g + "-notes.md")).write_text(notes)
print("Curated", len(BASE), "genes")
