from pathlib import Path
from copy import deepcopy
import yaml

p = Path("modules/bacterial_nonhomologous_end_joining.yaml")
d = yaml.safe_load(p.read_text())
m = d["module"]


def T(i, label):
    return {"id": i, "label": label}


def evidence(n, s, q):
    text = (Path("publications") / f"PMID_{n}.md").read_text()
    assert " ".join(q.split()) in " ".join(text.split()), (n, q)
    meta = yaml.safe_load(text.split("---", 2)[1])
    return {
        "source_id": f"PMID:{n}",
        "title": meta["title"],
        "statement": s,
        "supporting_text": q,
    }


review = evidence(
    "34901162",
    "Review of comparative LigD architecture establishes that processing-domain content and order vary by lineage.",
    "B. subtilis LigD lacks the PE domain, with only the LIG domain at the N-terminus and the POL domain at the C-terminus",
)
complexity = evidence(
    "30746801",
    "Comparative review covers bacterial systems of different complexity; the canonical fused-LigD boundary does not encompass every bacterial NHEJ architecture.",
    "Bacterial NHEJ is performed by sets of proteins of growing complexity from Bacillus subtilis and Mycobacterium tuberculosis to Streptomyces and Sinorhizobium meliloti.",
)
distribution = evidence(
    "33078828",
    "Comparative genomic analysis supports sporadic bacterial distribution rather than universal presence or an asserted bacterial ancestral state.",
    "Our results show that this pathway is sporadically distributed across the phylogeny.",
)
recruit = evidence(
    "12215643",
    "Biochemical recruitment and ligation stimulation support coupling Ku-bound DNA ends to the sealing enzyme.",
    "bacterial Ku specifically recruits DNA ligase to DNA ends and stimulates DNA ligation.",
)
lig = evidence(
    "16023671",
    "The isolated mycobacterial ligase domain seals a DNA substrate modelling a broken duplex.",
    "The ligase domain catalysed the sealing of nicked double-stranded DNA designed to mimic a DSB",
)
dnapol = evidence(
    "16023671",
    "The mycobacterial POL domain extends DNA using a template.",
    "The polymerase domain can also extend DNA in a template-dependent manner.",
)
pae_dnapol = evidence(
    "20018881",
    "Pseudomonas POL fills short gaps with deoxynucleotides; distinguish this DNA activity from ribonucleotide addition.",
    "The kinetic profile of the 3-nucleotide gap filling with dNMPs highlighted the same themes, especially faster gap closure on the 5′-phosphate DNA",
)
ribo = evidence(
    "20018881",
    "Pseudomonas Ku stimulates repair-associated ribonucleotide addition and full-length LigD joining.",
    "Pseudomonas Ku stimulates POL-catalyzed ribonucleotide addition to a plasmid DSB end and promotes plasmid end joining by full-length Pseudomonas LigD.",
)
bs_ribo = evidence(
    "41957403",
    "Bacillus LigD couples AP-site processing, nucleotide insertion and ligation under Ku-mediated synapsis in the tested reconstitution. This is substrate- and construct-specific.",
    "LigDBs catalyzes these steps without dissociating from DNA, being this processive catalysis dependent on KuBs-mediated synapsis.",
)
pe = evidence(
    "16046407",
    "Pseudomonas PE directly removes a blocking phosphate from an all-DNA primer-template; this is distinct from terminal-ribonucleotide trimming.",
    "the PE domain has a 3'-phosphatase activity on an all-DNA primer-template",
)
kuap = evidence(
    "25355514",
    "AP lyase is measured in Bacillus Ku and also Pseudomonas Ku; it is not a universal family grant or a native BER process assertion.",
    "The presence of an AP-lyase activity also in the homolog protein from the distantly related bacterium Pseudomonas aeruginosa",
)
ligap = evidence(
    "30976810",
    "Bacillus POL cleaves AP sites near recessed ends and couples the reaction to joining under defined nucleotide and metal conditions.",
    "a robust AP lyase activity in the polymerization domain of Bacillus subtilis LigD",
)
for e in [review, complexity, distribution, pe, kuap, ligap, bs_ribo]:
    d["evidence"].append(e)
d["description"] = (
    "A bacterial Ku–LigD implementation of double-strand-break repair in which Ku binds and aligns broken duplex ends and a fused LigD protein seals compatible termini with ATP. Depending on end chemistry and the domains present, repair can additionally involve deoxynucleotide or ribonucleotide addition, 3-prime-phosphate removal, or abasic-site processing. These processing activities are conditional and are not all conserved in every LigD or required for every break. The scope excludes homologous recombination, single-strand annealing, eukaryotic NHEJ, split-protein implementations and alternative backup-ligase routes."
)
d["notes"] = (
    "Bacteria is the taxonomic envelope of this implementation, not a claim of universal occurrence. The panel samples Pseudomonadota, Actinomycetota and Bacillota. Bacillus LigD lacks PE despite sharing PTHR42705:SF2 with PE-containing proteins, so the phosphatase participant is function- and domain-qualified. Ku can itself catalyze AP-site chemistry in measured exemplars; it is not universally an inert scaffold. Required Ku and fused-LigD roles define the modeled canonical route, not the necessity of those proteins for every end-joining event in each organism. KT2440 Cas9 repair can be LigD-independent, and PA14 backup-route findings are not automatically native PAO1 evidence. Family/PTN provenance is distinct from exact member placement: the KT2440 accessions are absent from the sampled trees. Optional chemistry records capabilities, while substrate-specific necessity and compatible native partners must be supplied by the evidence-backed capacity scenarios."
)
m["context"]["evidence"] = [distribution, complexity]
ku = m["parts"][0]["node"]
proc = m["parts"][1]["node"]
seal = m["parts"][2]["node"]
ku["description"] = (
    "Ku binds and protects duplex ends, promotes their alignment and recruits a repair ligase. AP-site chemistry observed for particular Ku proteins is represented separately as a conditional processing capability."
)
ku["evidence"] = [recruit, deepcopy(ku["evidence"][1]), kuap]
ka = ku["annotons"][0]
ka["function"] = {
    "preferred_term": "DNA end binding",
    "term": T("GO:0045027", "DNA end binding"),
    "substrates": [{"preferred_term": "double-strand-break duplex DNA end"}],
    "evidence": [recruit],
}
kf = ka["participant"]["family"]
prior = kf.pop("ancestral_nodes")
kf.setdefault("evidence", []).extend(prior[0]["evidence"])
kf["description"] = (
    "Prokaryotic-type Ku proteins with independently supported DNA-end binding. PTN002222140 carries the broader GO:0003690 duplex-binding assertion; it is not presented as an observed gain of GO:0045027."
)
kf["representative_members"].append(
    {
        "preferred_term": "Bacillus subtilis Ku",
        "term": T("UniProtKB:O34859", "Ku"),
        "description": "Strain168 Ku; native stress studies and biochemical end-joining/AP-site processing evidence. The2026 reconstitution uses an N-terminally shortened construct.",
    }
)
pol, phos = proc.pop("annotons")
for a in [pol, seal["annotons"][0]]:
    a["participant"]["family"]["representative_members"].append(
        {
            "preferred_term": "Bacillus subtilis LigD",
            "term": T("UniProtKB:O34398", "LigD"),
            "description": "Strain168 ligd (also written ligD), a fused N-terminal LIG/C-terminal POL enzyme lacking PE.",
        }
    )
pol["function"]["substrates"] = [
    {"preferred_term": "gapped or incompatible DNA end with a template"},
    {"preferred_term": "deoxyribonucleoside triphosphate"},
]
pol["function"]["products"] = [
    {"preferred_term": "DNA end extended with deoxyribonucleotides"}
]
pol["function"]["evidence"] = [dnapol, pae_dnapol]
pol["role_description"] = (
    "Template-directed deoxynucleotide addition fills a DNA gap before sealing. Ribonucleotide transfer is represented separately."
)
# Broad-node provenance supports the observed claim, not an unexamined universal POL grant.
pf = pol["participant"]["family"]
pa = pf.pop("ancestral_nodes")
pf.setdefault("evidence", []).extend(pa[0]["evidence"])
pf["description"] = (
    "Fused LigD proteins carrying an independently supported POL domain. PTN001627042 records GO:0003887 but also spans SF3; the family review leaves that whole-node scope unresolved. The named SF2 exemplars have supporting architecture and biochemical evidence."
)
pol["participant"]["required_function"] = deepcopy(pol["function"])
pol["participant"]["required_function"].pop("substrates", None)
pol["participant"]["required_function"].pop("products", None)
phos["participant"]["required_function"] = {
    "preferred_term": "polynucleotide 3-prime-phosphatase activity",
    "term": T("GO:0046403", "polynucleotide 3'-phosphatase activity"),
}
phos["participant"]["required_domain"] = {
    "preferred_term": "LigD phosphoesterase domain",
    "description": "The PE domain is required in addition to SF2 membership. The cited UniProt classification snapshots identify it as InterPro IPR014144; no whole-SF2 PE grant is made.",
}
phos["participant"]["description"] = (
    "PE-containing LigD subset. Bacillus LigD is excluded from this role because it lacks PE, while remaining a ligase/polymerase exemplar."
)
phos["function"]["evidence"] = [pe]
phos["function"]["substrates"] = [
    {"preferred_term": "DNA end with a blocking 3-prime phosphate"}
]
phos["role_description"] = (
    "Produces a ligatable 3-prime hydroxyl on a blocked DNA terminus when a competent PE domain is present; separate terminal-ribonucleotide trimming chemistry is not conflated with this reaction."
)
rna = deepcopy(pol)
rna["id"] = "ligd_ribonucleotide_transfer"
rna["label"] = "LigD repair-associated ribonucleotide transfer"
rf = rna["participant"]["family"]
rf["representative_members"] = [
    x for x in rf["representative_members"] if x["term"]["id"] != "UniProtKB:Q88HU3"
]
rf.pop("evidence", None)
rf["description"] = (
    "Fused LigD POL-containing proteins with measured repair-associated ribonucleotide incorporation. The minimal shared claim includes single-nucleotide transfer; it is not a universal transcription or de novo priming assertion."
)
rna["function"] = {
    "preferred_term": "repair-associated ribonucleotidyl transfer",
    "term": T("GO:0016779", "nucleotidyltransferase activity"),
    "substrates": [
        {"preferred_term": "ribonucleoside triphosphate"},
        {"preferred_term": "repair-primer 3-prime hydroxyl at a templated DNA end"},
    ],
    "products": [{"preferred_term": "repair end extended by a ribonucleotide"}],
    "evidence": [ribo, bs_ribo],
}
rna["participant"]["required_function"] = {
    "preferred_term": "repair-associated ribonucleotidyl transfer",
    "term": T("GO:0016779", "nucleotidyltransferase activity"),
}
rna["role_description"] = (
    "Adds a ribonucleotide at a repair end. Pseudomonas and mycobacterial proteins also support RNA-tract extension; the directly measured Bacillus single-insertion claim is retained at the shared transferase genus."
)
apfun = {
    "preferred_term": "AP-site beta-elimination",
    "term": T(
        "GO:0140078",
        "class I DNA-(apurinic or apyrimidinic site) endonuclease activity",
    ),
    "substrates": [
        {"preferred_term": "abasic site near a broken DNA end in a supported geometry"}
    ],
    "products": [{"preferred_term": "DNA incised by beta-elimination at the AP site"}],
}
kap = deepcopy(ka)
kap["id"] = "ku_ap_site_processing"
kap["label"] = "Ku AP-site processing"
kap["function"] = deepcopy(apfun)
kap["function"]["evidence"] = [kuap]
kap["participant"]["family"]["representative_members"] = [
    x
    for x in kf["representative_members"]
    if x["term"]["id"] in ["UniProtKB:Q9I1W5", "UniProtKB:O34859"]
]
kap["participant"]["family"].pop("evidence", None)
kap["participant"]["family"]["description"] = (
    "Ku proteins with measured AP beta-elimination, represented by Bacillus and Pseudomonas. SF1 binding evidence alone does not establish catalysis."
)
kap["participant"]["required_function"] = {
    "preferred_term": "AP-site beta-elimination",
    "term": apfun["term"],
}
kap["role_description"] = (
    "Cleaves an AP site on an experimentally supported substrate; do not assign this chemistry to every Ku or infer general native BER participation."
)
lap = deepcopy(pol)
lap["id"] = "ligd_ap_site_processing"
lap["label"] = "LigD POL AP-site processing"
lap["function"] = deepcopy(apfun)
lap["function"]["evidence"] = [ligap, bs_ribo]
lap["participant"]["family"]["representative_members"] = [
    x
    for x in pol["participant"]["family"]["representative_members"]
    if x["term"]["id"] == "UniProtKB:O34398"
]
lap["participant"]["family"].pop("evidence", None)
lap["participant"]["family"]["description"] = (
    "Experimentally supported AP-processing LigD POL subset, represented by Bacillus. This activity is independent of possessing a PE domain."
)
lap["participant"]["required_function"] = {
    "preferred_term": "AP-site beta-elimination",
    "term": apfun["term"],
}
lap["role_description"] = (
    "Processes an AP site near a recessed 5-prime end under the assayed metal/nucleotide conditions, before nucleotide addition and Ku-dependent joining."
)


def part(order, id, label, a, ev):
    return {
        "order": order,
        "role": label,
        "optional": True,
        "node": {
            "id": id,
            "label": label,
            "module_type": "REACTION",
            "description": a["role_description"],
            "evidence": ev,
            "annotons": [a],
        },
    }


proc["description"] = (
    "Independent conditional end-processing capabilities. A repair event uses only the chemistry required by its substrate and available in the participating proteins; neither a PE domain nor AP lyase activity is universal."
)
proc["evidence"] = [review, dnapol, pe, ligap]
proc["parts"] = [
    part(1, "ligd_dna_gap_filling", "DNA gap filling", pol, [dnapol, pae_dnapol]),
    part(
        2,
        "ligd_rna_end_extension",
        "Repair-associated ribonucleotide addition",
        rna,
        [ribo, bs_ribo],
    ),
    part(3, "ligd_phosphate_healing", "3-prime-phosphate removal", phos, [pe]),
    part(4, "ku_abasic_processing", "Ku-dependent AP-site processing", kap, [kuap]),
    part(
        5,
        "ligd_abasic_processing",
        "LigD-dependent AP-site processing",
        lap,
        [ligap, bs_ribo],
    ),
]
m["parts"][1]["role"] = "conditional DNA-end processing"
seal["evidence"] = [lig, recruit]
seal["annotons"][0]["function"]["evidence"] = [lig]
for c in m["connections"]:
    if c["source"] == "ku_end_recognition" and c["target"] == "ligd_end_processing":
        c["evidence"] = [ribo, bs_ribo]
        c["description"] = (
            "Ku-bound ends provide the substrate context for the applicable remodeling activity. These edges do not require all processing reactions or establish identical regulatory effects across species."
        )
    elif c["source"] == "ku_end_recognition":
        c["evidence"] = [recruit, lig]
    else:
        c["evidence"] = [ligap, bs_ribo, pe]
        c["description"] = (
            "When end chemistry demands processing, the applicable reaction prepares a substrate before final sealing; abasic-site cleavage can additionally require nucleotide insertion."
        )
        c["chaining_note"] = (
            "Substrate-dependent coupling is directly reconstituted for Bacillus AP-bearing ends (PMID:30976810,41957403); Pseudomonas PE produces the3-primehydroxyl needed for subsequent repair (PMID:16046407). This is not a claim that every listed chemistry forms a single obligatory linear chain."
        )
m["knowledge_gaps"].extend(
    [
        {
            "gap_statement": "Family membership does not establish compatible native partners, the chemistry of a particular break or that all optional activities occur in one event.",
            "boundary": "Evaluate compatible-end, gap, phosphate-blocked and AP-bearing scenarios with explicit evidence-qualified capability requirements; Boolean core satisfaction alone does not prove repair of each substrate.",
            "gap_kind": ["BIOLOGY"],
        },
        {
            "gap_statement": "Ku effects on LigD polymerization vary with assay, construct and substrate, and alternate routes can repair DNA in the absence of canonical LigD.",
            "boundary": "Keep the2026CDC1551LigD construct separate from H37Rv, the truncatedBacillusKu construct separate from nativeoccupancy, and nativeKT2440/PA14 observations separate from PAO1biochemistry. No universal activation sign or obligatory gene dependence is asserted.",
            "gap_kind": ["BIOLOGY"],
        },
    ]
)
p.write_text(yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100))
print(p)
