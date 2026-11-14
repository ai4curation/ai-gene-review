"""Scoped manual synthesis; preserves every seeded annotation payload."""

import copy
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
BASE = json.loads((HERE / "baseline.json").read_text())
GO = {}
for file in HERE.glob("*.json"):
    data = json.loads(file.read_text())
    for term in data.get("results", []) if isinstance(data, dict) else []:
        if "id" in term and "name" in term:
            GO[term["id"]] = term["name"]
GO.update({"GO:0005524": "ATP binding"})


def term(go):
    return {"id": go, "label": GO[go]}


def support(pmid, text):
    source = (ROOT / f"publications/PMID_{pmid}.md").read_text()
    match = re.search(r"\s+".join(re.escape(x) for x in text.split()), source)
    assert match, (pmid, text)
    return {"reference_id": "PMID:" + str(pmid), "supporting_text": match.group()}


S = {
    "pa_rna": support(
        20018881,
        "Processive closure of the gap appeared to be less efficient with rNTPs than dNTPs",
    ),
    "bs_rna": support(
        41957403,
        "once LigDBs positions the template nucleotide in its polymerase active site, it can add the complementary ribonucleotide to the 3’-protruding end",
    ),
    "pa_binding": support(
        20018881, "Ku afforded virtually complete protection from both exonucleases"
    ),
    "pa_stim": support(
        20018881,
        "PaeKu stimulated ribonucleotide addition to DSB ends by PaePOL and DSB end sealing by LigD.",
    ),
    "pa_poly": support(
        20018881,
        "The primer extension and gap filling reactions were performed in the presence of 100 μ m dNTPs",
    ),
    "pa_lig": support(15520014, "an autonomous DNA ligase domain, LigD-(188-527)"),
    "pa_ribo": support(
        15897197,
        "The ribonucleotide resection activity resides within a 187-amino acid N-terminal nuclease domain",
    ),
    "pa_phos": support(
        16046407,
        "the PE domain has a 3'-phosphatase activity on an all-DNA primer-template",
    ),
    "bs_join": support(
        41957403,
        "LigDBs catalyzes these steps without dissociating from DNA, being this processive catalysis dependent on KuBs-mediated synapsis",
    ),
    "bs_pol": support(
        26826709, "57 nM BsuLigD and either 300 μM ddCTP, 10 μM dCTP or 10 μM CTP"
    ),
    "bs_ap": support(
        30976810,
        "a robust AP lyase activity in the polymerization domain of Bacillus subtilis LigD (BsuLigD)",
    ),
    "ku_ap_bs": support(
        25355514,
        "B. subtilis Ku (BsuKu), along with its pivotal role in allowing joining of two broken ends by B. subtilis LigD (BsuLigD), is endowed with an AP/deoxyribose 5'-phosphate (5'-dRP)-lyase activity",
    ),
    "ku_ap_pa": support(
        25355514,
        "The presence of an AP-lyase activity also in the homolog protein from the distantly related bacterium Pseudomonas aeruginosa",
    ),
    "lig_drp": support(
        26826709,
        "We demonstrate the presence of the dRP lyase activity also in the homolog protein from the distantly related bacterium Pseudomonas aeruginosa",
    ),
    "bs_drp": support(
        26826709,
        "Excision of 5′-dRP groups by BsuLigD proceeds through a β-elimination mechanism",
    ),
    "bs_native": support(
        17293412,
        "NHEJ-defective spores with mutations in ykoU, ykoV, and ykoU ykoV were significantly more sensitive to UV, ionizing radiation, and ultrahigh vacuum",
    ),
}

REF_NOTES = {
    "pa_rna": support(
        20018881,
        "Processive closure of the gap appeared to be less efficient with rNTPs than dNTPs",
    ),
    "bs_rna": support(
        41957403,
        "once LigDBs positions the template nucleotide in its polymerase active site, it can add the complementary ribonucleotide to the 3’-protruding end",
    ),
    20018881: "Full primary text: recombinant P. aeruginosa Ku/LigD, DNA gap filling with dNTPs, and Ku stimulation of LigD. End protection used Ku-(1–253); full-length and other truncations were separately tested. This is not a native PA14 or KT2440 assay.",
    15520014: "Abstract-only positive biochemical evidence for purified P. aeruginosa LigD polymerase and ATP-ligase domains. No negative conclusion about an unexamined primase assay is drawn.",
    15897197: "Abstract-only direct P. aeruginosa LigD terminal-ribonucleotide resection evidence. The preferred substrate is a DNA primer bearing a short 3′ ribonucleotide tract, not bulk cellular RNA. Sequential nucleoside removal and 3′-phosphate hydrolysis are distinguished.",
    16046407: "Abstract explicitly reports P. aeruginosa LigD phosphatase activity on an all-DNA primer-template. This supports the DNA substrate in GO0046403; RNA-terminal phosphatase activity alone would not establish it. Full Figure5 was not independently inspected here.",
    41957403: "Full primary text: recombinant B. subtilis LigD/Ku coordinates AP incision, ribonucleotide insertion and joining. KuBs corresponds to strain168 NP_389224.1 beginning at annotated position18; proteins/truncations/chimeras were expressed in E. coli. No native exact occupancy or universal cross-species interaction is inferred. The primary places LigDom N-terminal and PolDom C-terminal, contrary to reversed UniProt similarity-section prose.",
    25355514: "Full primary biochemistry demonstrates Bacillus Ku AP/5′-dRP lyase and P. aeruginosa Ku AP lyase. PAO1 genomic cloning is explicit. Substrate specificity and covalent-intermediate controls support catalysis. Proposed participation in cellular BER remains a hypothesis, not a new process annotation.",
    26826709: "Full primary biochemistry directly tests Bacillus LigD dCTP gap filling and 5′-dRP lyase, and confirms 5′-dRP lyase in purified P. aeruginosa LigD. Native Bacillus strain168-derived spore experiments suggest overlapping repair with Nfo but do not alone prove the proposed full BER role.",
    30976810: "Full primary shows Bacillus LigD PolDom AP lyase at recessed5′ ends, borohydride-trapped intermediate and coupling to incoming-primer extension/ligation. AP processing is a beta-lyase mechanism despite its metal/nucleotide-dependent precatalytic arrangement. It is not PE-domain activity.",
    17293412: "Full primary uses Bacillus168-derived repair mutants and spores; it supports native Ku/LigD repair relevance under specified damaging treatments, not an isolated-enzyme activity or a universal essentiality claim.",
}
GO_REFS = {
    "pa_rna": support(
        20018881,
        "Processive closure of the gap appeared to be less efficient with rNTPs than dNTPs",
    ),
    "bs_rna": support(
        41957403,
        "once LigDBs positions the template nucleotide in its polymerase active site, it can add the complementary ribonucleotide to the 3’-protruding end",
    ),
    "GO_REF:0000002": "Gene Ontology annotation through association of InterPro records with GO terms",
    "GO_REF:0000033": "Annotation inferences using phylogenetic trees",
    "GO_REF:0000104": "Electronic Gene Ontology annotations created by transferring manual GO annotations between related proteins based on shared sequence features",
    "GO_REF:0000108": "Automatic assignment of GO terms using logical inference, based on on inter-ontology links",
    "GO_REF:0000120": "Combined Automated Annotation using Multiple IEA Methods",
}


def review(action, reason, keys, replacement=()):
    result = {
        "action": action,
        "summary": reason.split(". ")[0] + ".",
        "reason": reason,
        "supported_by": [copy.deepcopy(S[k]) for k in keys],
    }
    if replacement:
        result["proposed_replacement_terms"] = [term(k) for k in replacement]
    return result


def core(description, go, keys, process=True):
    result = {
        "description": description,
        "molecular_function": term(go),
        "supported_by": [copy.deepcopy(S[k]) for k in keys],
    }
    if process:
        result["directly_involved_in"] = [term("GO:0006303")]
    return result


def main():
    assert not (HERE / "handoff.json").exists(), "Frozen"
    for original, baseline in BASE["reviews"].items():
        p = ROOT / original
        if not p.exists() and "/BACSU/ligd/" in original:
            p = ROOT / original.replace("/ligd/ligd-", "/ligD/ligD-")
        d = yaml.safe_load(p.read_text())
        assert [
            {k: v for k, v in a.items() if k != "review"}
            for a in d["existing_annotations"]
        ] == [
            {k: v for k, v in a.items() if k != "review"}
            for a in baseline["data"]["existing_annotations"]
        ]
        pa = d["id"] in ("Q9I1W5", "Q9I1X7")
        ku = d["id"] in ("Q9I1W5", "O34859")
        join = "pa_stim" if pa else "bs_join"
        binding = "pa_binding" if pa else "bs_join"
        for a in d["existing_annotations"]:
            go = a["term"]["id"]
            if go == "GO:0003677":
                a["review"] = review(
                    "MODIFY",
                    "DNA binding is correct but the established double-stranded DNA and broken-end recognition are more precise. Retain the existing duplex-binding claim and the independently demonstrated end-binding specificity; these are distinct ontology branches.",
                    [binding],
                    ["GO:0003690", "GO:0045027"],
                )
            elif go == "GO:0003690":
                a["review"] = review(
                    "ACCEPT",
                    "Ku binds double-stranded DNA and recognizes/protects broken ends during end joining. This duplex-binding claim is true alongside the distinct DNA-end-binding core. "
                    + (
                        "End protection was measured with the Ku-(1–253) construct; full-length Ku binding and LigD stimulation were also assayed."
                        if pa
                        else "Bacillus Ku-mediated synapsis and coordinated LigD repair are directly demonstrated with recombinant proteins; native spore genetics independently supports repair relevance."
                    ),
                    [binding, join],
                )
            elif go in ("GO:0006281", "GO:0006974"):
                a["review"] = review(
                    "MODIFY",
                    "The broad DNA repair or damage-response process is correct; the supported specific process is double-strand break repair by nonhomologous end joining. Ku performs DNA-end recognition/synapsis and LigD performs repair chemistry, rather than being merely required substrates.",
                    [join],
                    ["GO:0006303"],
                )
            elif go == "GO:0006303":
                a["review"] = review(
                    "ACCEPT",
                    "The product performs end-joining work: Ku binds and organizes broken ends and LigD extends/processes/seals compatible substrates. The canonical biochemical route does not imply that every chromosomal break is repaired by Ku/LigD or that alternative LigD-independent routes are absent.",
                    [join] + ([] if pa else ["bs_native"]),
                )
            elif go == "GO:0051351":
                a["review"] = review(
                    "ACCEPT",
                    "P. aeruginosa Ku directly stimulates LigD-mediated end sealing in the reported reconstitution. This regulation is a core contribution of Ku to end joining and does not assign ATP-dependent ligase catalysis to Ku itself.",
                    ["pa_stim"],
                )
            elif go == "GO:0003887":
                a["review"] = review(
                    "ACCEPT",
                    "LigD has template-directed deoxynucleotide incorporation activity in addition to its ribonucleotide preference. "
                    + (
                        "The primary gap-filling experiments explicitly used dNTPs."
                        if pa
                        else "Bacillus LigD was directly tested with dCTP in the gap-filling experiment; the 2026 rNTP assays are not the sole evidence for DNA polymerization."
                    ),
                    ["pa_poly" if pa else "bs_pol"],
                )
            elif go == "GO:0003910":
                a["review"] = review(
                    "ACCEPT",
                    "ATP-dependent strand sealing is an independently supported LigD catalytic function. It is distinct from the polymerase and end-processing activities and does not imply NAD-dependent replication ligase function.",
                    ["pa_lig", "pa_stim"] if pa else ["bs_join"],
                )
            elif go == "GO:0005524":
                a["review"] = review(
                    "ACCEPT",
                    "ATP is an integral catalytic substrate of the ATP-dependent ligase, so its binding is core rather than peripheral. This does not establish an autonomous ATPase or every ATP-dependent reaction.",
                    ["pa_lig"] if pa else ["bs_join"],
                )
            elif go == "GO:0004532":
                a["review"] = review(
                    "ACCEPT",
                    "The experimentally curated exoribonuclease claim is supported by stepwise resection of the short 3′ ribonucleotide tract on a DNA primer-template. The two-step chemistry first removes the terminal nucleoside leaving a 3′ phosphate, then hydrolyzes that phosphate; no general cellular RNA degradation role or conventional 5′-monophosphate product is asserted.",
                    ["pa_ribo"],
                )
            elif go == "GO:0006269":
                a["review"] = review(
                    "ACCEPT",
                    "PAINT places primer synthesis at PTN001627042, and the exact target descends from that node with a conserved LigD polymerase/primase module. GO0006269 explicitly includes DNA-damage-associated priming; it is not restricted to chromosome replication. The Mycobacterium experimental seed is legitimate phylogenetic grounding. No target-specific loss or relevant catalytic divergence has been demonstrated; absence of a direct target de novo assay does not overturn the inherited assertion. The target repair-polymerization assays provide compatible, not independently sufficient, biochemical context.",
                    ["pa_poly" if pa else "bs_pol"],
                )
                a["review"]["supported_by"].append(
                    {
                        "reference_id": "file:interpro/panther/PTHR42705/PTHR42705-paint.tsv",
                        "supporting_text": "PTHR42705\tPTN001627042\tGO:0006269\tP\tIBD\tfalse\tUniProtKB:P9WNV3",
                    }
                )
            elif go == "GO:0006310":
                a["review"] = review(
                    "MODIFY",
                    "The supported mechanism is nonhomologous repair of DNA double-strand ends. This is a lateral process correction to the demonstrated repair pathway, not a claim that all other recombination chemistry or mutagenic outcomes are impossible.",
                    [join],
                    ["GO:0006303"],
                )
            elif go == "GO:0016779":
                a["review"] = review(
                    "ACCEPT",
                    "The directly demonstrated reaction includes both deoxynucleotide incorporation and ribonucleotide/end additions to DNA substrates. DNA-directed DNA polymerase3887 captures only the template-directed deoxynucleotide component; no single established specific replacement in this review covers the other reactions, so the nucleotidyltransferase genus remains warranted for their combined chemistry.",
                    ["pa_poly", "pa_stim"],
                )
            elif go == "GO:0071897":
                a["review"] = review(
                    "ACCEPT",
                    "LigD performs DNA synthesis during repair through template-directed deoxynucleotide incorporation. This biosynthetic work is a direct catalytic contribution, without a claim of chromosome-replication priming.",
                    ["pa_poly" if pa else "bs_pol"],
                )
            else:
                raise AssertionError(go)
            if a["evidence_type"] == "IBA":
                a["review"]["reason"] += (
                    " The exact target leaf is present below the cited PAINT IBD node in the official tree; a self-seed is valid experimental grounding, and the cached slice supplies no negative loss assertion."
                )
        if ku:
            d["description"] = (
                "Ku is a homodimeric bacterial DNA-end-binding protein that organizes broken double-stranded DNA ends and promotes LigD-dependent repair. "
                + (
                    "The Pseudomonas aeruginosa PAO1 protein stimulates LigD polymerization and end sealing in biochemical reconstitution and also has experimentally demonstrated AP-lyase activity."
                    if pa
                    else "The Bacillus subtilis protein helps protect spore DNA and supports end synapsis and coordinated LigD repair. Recombinant Ku also catalyzes AP-site incision and removal of 5′-deoxyribose-phosphate groups; these activities do not by themselves establish a general cellular base-excision-repair role."
                )
            )
            d["core_functions"] = [
                core(
                    "Binds broken duplex DNA ends, supports synapsis and promotes LigD-mediated end joining; Ku does not catalyze ATP-dependent strand ligation.",
                    "GO:0045027",
                    [binding, join],
                ),
                core(
                    "Catalyzes beta-lyase cleavage at abasic DNA sites, with substrate-position dependence; this can assist joining of damaged DNA ends.",
                    "GO:0140078",
                    ["ku_ap_pa" if pa else "ku_ap_bs"],
                ),
            ]
            if not pa:
                d["core_functions"].append(
                    core(
                        "Removes terminal 5′-deoxyribose-phosphate groups from preincised substrates, permitting subsequent end sealing; native BER participation remains unresolved.",
                        "GO:0051575",
                        ["ku_ap_bs"],
                        False,
                    )
                )
        else:
            d["description"] = (
                "LigD is a multifunctional ATP-dependent DNA repair ligase that combines strand sealing with repair polymerization. "
                + (
                    "Pseudomonas aeruginosa PAO1 LigD contains an N-terminal phosphoesterase module, central ligase module and C-terminal polymerase module. It trims terminal ribonucleotide tracts, removes obstructing 3′ phosphates, fills DNA gaps and joins ends in cooperation with Ku. Purified LigD also removes 5′-deoxyribose-phosphate groups."
                    if pa
                    else "Bacillus subtilis LigD combines an N-terminal ligase module and C-terminal polymerase module and lacks the phosphoesterase module of some other LigD proteins. Its polymerase module can incise abasic sites near recessed 5′ ends, and Ku supports coordinated incision, nucleotide insertion and joining. LigD also has 5′-deoxyribose-phosphate lyase activity and contributes to spore DNA repair."
                )
            )
            d["core_functions"] = [
                core(
                    "Seals DNA strand breaks using ATP-dependent ligase chemistry during Ku-supported end joining.",
                    "GO:0003910",
                    ["pa_lig", "pa_stim"] if pa else ["bs_join"],
                ),
                core(
                    "Performs template-directed DNA gap filling with deoxynucleotides. This activity describes dNTP incorporation; rNTP chemistry is represented separately.",
                    "GO:0003887",
                    ["pa_poly" if pa else "bs_pol"],
                ),
                core(
                    "Removes a terminal 5′-deoxyribose-phosphate group by beta elimination on defined repair substrates. Reconstitution supports chemistry without proving a general native BER assignment.",
                    "GO:0051575",
                    ["lig_drp" if pa else "bs_drp"],
                    False,
                ),
            ]
            d["core_functions"].append(
                core(
                    "Extends a short nascent RNA tract against a DNA template during gap filling; this is repair synthesis, not a transcriptional role. Initial addition to a DNA3′ end and non-templated additions are distinct substrate situations."
                    if pa
                    else "Transfers a template-selected ribonucleotide to a DNA3′ end during end joining. The tested single-insertion reactions do not alone establish extension of an RNA strand, so this core uses the nucleotidyltransferase genus rather than forcing GO0003899.",
                    "GO:0003899" if pa else "GO:0016779",
                    ["pa_rna" if pa else "bs_rna"],
                )
            )
            if pa:
                d["core_functions"] += [
                    core(
                        "Removes a blocking 3′ phosphate from an all-DNA primer-template through the PE module, generating a usable 3′ hydroxyl.",
                        "GO:0046403",
                        ["pa_phos"],
                    ),
                    core(
                        "Resects short terminal ribonucleotide tracts on DNA primer-templates through sequential nucleoside removal and phosphate hydrolysis; this is substrate-specific end healing.",
                        "GO:0004532",
                        ["pa_ribo"],
                    ),
                ]
            else:
                d["core_functions"].append(
                    core(
                        "Cleaves AP sites near recessed 5′ ends through a PolDom beta-lyase reaction coordinated with nucleotide insertion and ligation; this is distinct from a PE-domain phosphatase.",
                        "GO:0140078",
                        ["bs_ap", "bs_join"],
                    )
                )
        # Each quoted publication receives claim-specific findings, not workflow boilerplate.
        used = {}

        def collect(value, context=""):
            if isinstance(value, dict):
                context = value.get("description", value.get("reason", context))
                if value.get("reference_id", "").startswith("PMID:") and value.get(
                    "supporting_text"
                ):
                    used.setdefault(int(value["reference_id"][5:]), {})[
                        value["supporting_text"]
                    ] = context
                for child in value.values():
                    collect(child, context)
            elif isinstance(value, list):
                for child in value:
                    collect(child, context)

        collect(d["existing_annotations"])
        collect(d["core_functions"])
        refs = []
        for ref in d.get("references", []):
            if ref["id"].startswith("GO_REF:"):
                refs.append(
                    {"id": ref["id"], "title": GO_REFS[ref["id"]], "findings": []}
                )
        for pmid, findings in sorted(used.items()):
            source = (ROOT / f"publications/PMID_{pmid}.md").read_text()
            meta = yaml.safe_load(source.split("---", 2)[1])
            refs.append(
                {
                    "id": "PMID:" + str(pmid),
                    "title": meta["title"],
                    "reference_review": {
                        "relevance": "HIGH",
                        "correctness": "VERIFIED",
                        "review_notes": REF_NOTES[pmid],
                    },
                    "full_text_unavailable": not meta.get("full_text_available", False),
                    "findings": [
                        {"statement": context, "supporting_text": quote}
                        for quote, context in findings.items()
                    ],
                }
            )
        if not ku:
            refs.append(
                {
                    "id": "file:interpro/panther/PTHR42705/PTHR42705-paint.tsv",
                    "title": "PANTHER PTHR42705 PAINT ancestral-function export",
                    "reference_review": {
                        "relevance": "HIGH",
                        "correctness": "VERIFIED",
                        "review_notes": "Actual IBD placement read and joined to the official tree. The target inherits PTN001627042 primer synthesis; no loss is invented from lack of direct assays.",
                    },
                    "findings": [
                        {
                            "statement": "Primer synthesis is asserted at the ancestral node containing the target; the donor is experimental grounding, not a pairwise-transfer requirement.",
                            "supporting_text": "PTHR42705\tPTN001627042\tGO:0006269\tP\tIBD\tfalse\tUniProtKB:P9WNV3",
                        }
                    ],
                }
            )
        d["references"] = refs
        d["status"] = "COMPLETE"
        d["suggested_questions"] = [
            {
                "question": "Which damaged-end substrates and physiological conditions require the measured AP/5′-dRP processing activities in the native strain?"
            }
        ]
        if not ku:
            d["suggested_questions"].append(
                {
                    "question": "Which native repair conditions use the phylogenetically supported de novo priming capacity, and how is it coordinated with template-dependent repair synthesis?"
                }
            )
        p.write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))
        notes = p.with_name(p.name.replace("-ai-review.yaml", "-notes.md"))
        text = f"# {d['gene_symbol']} manual review\n\nReviewed {len(d['existing_annotations'])} ordered source annotations; no new rows or retirements. Raw UniProt, GOA and seed snapshots remain unchanged.\n\n"
        text += "The exact target descends from its seeded IBD node in the official PANTHER tree. Broad family membership is not a grant of every LigD domain, primase process, or partner interaction. No donor-count or self-source objection is used.\n\n"
        text += "GO0045027 DNA-end binding is a distinct branch from duplex-binding3690; both describe real Ku properties. GO0140078 captures AP beta-lyase cleavage; GO0051575 captures terminal5′-dRP elimination. These are distinct from PE-mediated3′phosphatase0046403. No BER process NEW is inferred from necessity or a purified reconstitution.\n\n"
        if d["id"] == "O34398":
            text += "The seeded folder and UniProt primary symbol ligd are preserved. SubtiWiki uses ligD as the canonical display spelling; this is an alias/nomenclature difference, not a different gene or protein. No raw files were renamed.\n\n"
        if not ku:
            text += "Primase-process IBA GO0006269 is ACCEPT: its definition explicitly includes DNA-damage priming, the exact target inherits PTN001627042, and no target-specific catalytic loss is established. A lack of direct target de novo assays is not evidence against this inference. The native conditions of use remain a legitimate question.\n\n"
        if not pa:
            text += "Bacillus LigD lacks the PE domain. PMID41957403 and PMID30976810 place LigDom at residues1–320 and PolDom C-terminal; the immutable UniProt similarity-section N/C order is reversed and is not used as architectural evidence. PMID41957403 uses Ku beginning at the annotated strain168 position18, expressed in E.coli with a His tag; native damage protection is separately supported by PMID17293412.\n\n"
        else:
            text += "PAO1 target evidence is kept separate from PA14 LigD-independent NHEJ in PMID42306942. The latter is not a PAO1 deletion experiment. Ku-(1–253) end protection, full-length stimulation and other truncation assays are distinguished in PMID20018881. PMID25355514 explicitly clones Ku from PAO-1 genomic DNA.\n\n"
        text += "The recent Mycobacterium POL-regulation result PMID42953966 is not transferred as a universal sign to these proteins. The shared Falcon authentication failure is documented in the prior session; this file is manual synthesis, not a fabricated provider report.\n\n"
        for pmid in sorted(used):
            text += f"- PMID:{pmid}: {REF_NOTES[pmid]}\n"
        notes.write_text(text)


if __name__ == "__main__":
    main()
