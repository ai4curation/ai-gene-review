---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:12:23.241243'
end_time: '2026-10-25T23:21:15.675839'
duration_seconds: 532.43
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: ATG4C
  gene_symbol: ATG4C
  uniprot_accession: A0A9L0IIU3
  protein_description: 'RecName: Full=Cysteine protease {ECO:0000256|RuleBase:RU363115};
    EC=3.4.22.- {ECO:0000256|RuleBase:RU363115};'
  gene_info: Name=ATG4C {ECO:0000313|Ensembl:ENSEASP00005037695.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the peptidase C54 family.
  protein_domains: ATG4_LIR. (IPR046793); Papain-like_cys_pep_sf. (IPR038765); Peptidase_C54.
    (IPR005078); Peptidase_C54_cat. (IPR046792); ATG4_LIR (PF20166)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3301
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 57
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0IIU3
- **Protein Description:** RecName: Full=Cysteine protease {ECO:0000256|RuleBase:RU363115}; EC=3.4.22.- {ECO:0000256|RuleBase:RU363115};
- **Gene Information:** Name=ATG4C {ECO:0000313|Ensembl:ENSEASP00005037695.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the peptidase C54 family.
- **Key Domains:** ATG4_LIR. (IPR046793); Papain-like_cys_pep_sf. (IPR038765); Peptidase_C54. (IPR005078); Peptidase_C54_cat. (IPR046792); ATG4_LIR (PF20166)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ATG4C" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ATG4C' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ATG4C** (gene ID: ATG4C, UniProt: A0A9L0IIU3) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ATG4C (Cysteine protease ATG4C; UniProt A0A9L0IIU3) in the donkey, *Equus asinus*

## 1. Introduction and summary

UniProt entry A0A9L0IIU3 is an unreviewed (TrEMBL) protein of 458 amino acids. It was predicted from the donkey reference genome and comes from the Ensembl gene ENSEASG00005008203 on donkey chromosome 16. UniProt names it "Cysteine protease", gene symbol *ATG4C*, and places it in peptidase family C54 [uniprot-A0A9L0IIU3-entry]. The genome comes from the donkey genome assemblies of Wang et al. (2020), a study of domestication and coat colour that reported no functional work on autophagy genes [wang-2020-donkey-genomes-abstract]. No study has examined this protein in donkey tissue. Its function therefore has to be inferred from orthology. That inference is unusually strong here. The donkey sequence has the same length as human ATG4C (Q96DT6), with no gaps, and is 95.0% identical (435/458 residues). The entry carries the NCBI Gene/CTD cross-reference 84938, the identifier of human *ATG4C*, and is assigned to the ATG4C-specific PANTHER subfamily PTHR22624:SF38 [uniprot-A0A9L0IIU3-entry; uniprot-Q96DT6-entry]. The identity check required by the brief is therefore satisfied. The symbol is not ambiguous, the domains (Peptidase_C54 catalytic domain, papain-like cysteine peptidase superfamily, ATG4 LIR motif) are those of the ATG4 family, and the literature on mammalian ATG4C (also called autophagin-3) applies directly.

ATG4C is one of four mammalian paralogues (ATG4A–D) of yeast Atg4. Atg4 is a cysteine protease with two jobs in the ubiquitin-like ATG8 conjugation system [kirisako-2000-apg8-reversible-abstract; tamargo-gomez-2023-atg4c-invivo-fulltext]. The first is "priming". ATG4 cleaves the C-terminal extension from newly made ATG8-family proteins (LC3A/B/C, GABARAP, GABARAPL1, GABARAPL2) to expose a glycine. That glycine is then conjugated to phosphatidylethanolamine (PE) on the phagophore. The second is "delipidation". ATG4 hydrolyses the amide bond between that glycine and PE, releasing ATG8 from membranes so it can be reused [kirisako-2000-apg8-reversible-abstract; tanida-2004-atg4b-delipidation-abstract]. Within the family, ATG4C is a weak priming enzyme on soluble substrates [li-2011-kinetics-abstract]. On membrane-anchored, lipidated ATG8s, however, it is about as active as the other isoforms [kauffman-2018-delipidation-abstract]. Mouse genetics show that ATG4C does make a measurable contribution to ATG8 delipidation in vivo, most clearly when ATG4D is absent. Its loss also causes tissue-specific changes in LC3 lipidation in diaphragm, brain and spleen, a poor response to prolonged fasting, and changes in lymphocyte numbers [tamargo-gomez-2023-atg4c-invivo-fulltext]. The enzyme works in the cytoplasm, on the cytosolic face of phagophore, autophagosome and autolysosome membranes [uniprot-Q96DT6-entry; tamargo-gomez-2023-atg4c-invivo-fulltext]. Overall, donkey ATG4C is best described as a mostly redundant ATG8-deconjugating enzyme and a minor priming protease in macroautophagy.

## 2. Gene identity, sequence conservation and domain architecture

The donkey and human ATG4C sequences differ at only 23 positions, scattered across the protein. Every catalytically important motif is identical. The catalytic cysteine sits in the motif TTDCGWGC (residues 104–111), which places the nucleophile at Cys111. The motif IYMDPHY (residues 342–348) contains the other two triad residues, Asp345 and His347. Human UniProt annotates these same positions: Cys111 as the nucleophile, and Asp345 and His347 as active-site residues assigned by similarity to ATG4B [uniprot-Q96DT6-entry]. Because the donkey protein aligns with human ATG4C without gaps, the numbering carries over directly (sequence comparison performed in this study from the two UniProt FASTA records [uniprot-A0A9L0IIU3-entry; uniprot-Q96DT6-entry]).

The Peptidase_C54 domain (Pfam PF03416; InterPro IPR005078/IPR046792) is a papain-like fold. Its structure is known from crystal structures of the paralogue ATG4B. Free ATG4B has a Cys–His–Asp triad. Its active site is blocked by two elements: a "regulatory loop" over the entrance and the N-terminal tail over the exit [kumanomidou-2006-atg4b-structure-abstract]. When LC3 binds, its Phe119 lifts the regulatory loop, which opens a groove that guides the LC3 C-terminal tail into the active site. At the same time the N-terminal tail comes away from the catalytic core. This exposes a large flat surface that has been proposed to let the enzyme reach membrane-anchored LC3-PE [satoo-2009-atg4b-lc3-structure-abstract]. The donkey entry also has an ATG4_LIR element (PF20166; IPR046793) [uniprot-A0A9L0IIU3-entry]. LC3-interacting region (LIR) motifs of this kind were characterised in ATG4B. There, a C-terminal LIR binds the HP1 and HP2 hydrophobic pockets of LC3/GABARAP proteins. It is needed for efficient binding and cleavage, and for stabilising unlipidated GABARAP and GABARAPL1 [skytte-rasmussen-2017-atg4b-lir-abstract]. LIR-dependent recognition matters most for lipidated substrates. In a reconstituted system, recognition of membrane-anchored, but not soluble, ATG8s depended on a C-terminal LIR motif, in vitro and in cells [kauffman-2018-delipidation-abstract]. Its presence in donkey ATG4C therefore fits a role in delipidation. No ATG4C-specific structure has been published, so this structural picture is inferred from ATG4B.

## 3. Catalytic activity and substrate specificity

### 3.1 The two reactions

The two ATG4 reactions were first described in budding yeast. There, Atg4 removes the C-terminal arginine of Atg8 to expose Gly116, which is then conjugated to PE. Atg4 also cleaves Atg8 off PE again, and this reversible modification controls whether Atg8 is bound to membranes [kirisako-2000-apg8-reversible-abstract]. In mammals, ATG4B was shown to cleave the C-termini of LC3, GABARAP and GATE-16 (GABARAPL2) and to delipidate LC3- and GABARAP-phospholipid conjugates, and both activities depend on its catalytic cysteine [tanida-2004-atg4b-delipidation-abstract]. UniProt gives the delipidation reaction for donkey ATG4C, by automatic annotation, as Rhea:67548: a [protein]-C-terminal glycyl-phosphatidylethanolamide plus water gives a [protein]-C-terminal glycine plus a 1,2-diacyl-sn-glycero-3-phosphoethanolamine. For the human orthologue the same reaction is supported by experimental evidence [uniprot-A0A9L0IIU3-entry; uniprot-Q96DT6-entry]. The priming reaction is a peptide-bond hydrolysis. That is why the protein is classified as a cysteine-type endopeptidase (EC 3.4.22.-).

### 3.2 ATG4C is a weak priming protease

The first full kinetic comparison of the four human ATG4s used four representative ATG8 substrates. ATG4B had the broadest and highest activity, followed by ATG4A. ATG4C and ATG4D showed minimal activity, close to that of the catalytically dead ATG4B C74S mutant. GATE-16/GABARAPL2 was the best substrate overall [li-2011-kinetics-abstract]. UniProt's Km values for human ATG4C come from this study: 47.5 µM for LC3B and 12.4 µM for GABARAPL2 [uniprot-Q96DT6-entry]. The lower Km for GABARAPL2 fits the later evidence from cells that ATG4C's residual priming activity acts mainly on GABARAP-subfamily proteins (Section 4).

### 3.3 Delipidation is shared by all ATG4s, including ATG4C

The view of ATG4C as a nearly inactive enzyme changed when it was tested on membrane-bound substrates. In a fully reconstituted delipidation assay, ATG4B was orders of magnitude faster than the other isoforms at processing soluble, unprimed substrate. On lipid-attached substrates, by contrast, all four ATG4s reached similar enzymatic activity. This led to a model in which ATG4B performs rapid priming, while delipidation is inherently slow and shared by all four homologues [kauffman-2018-delipidation-abstract]. Durgan et al. (2021) confirmed that all four ATG4s delipidate ATG8s from PE liposomes, to varying degrees. They noted that full-length ATG4C and ATG4D purified from mammalian cells are active, whereas the bacterially expressed proteins used in earlier studies are not [durgan-2021-noncanonical-fulltext]. This suggests that the low activity of ATG4C in earlier in vitro work may partly reflect how the protein was produced. Durgan et al. also found that ATG8 proteins can be conjugated to phosphatidylserine (PS) during non-canonical autophagy (CASM). PS adducts were removed preferentially by ATG4D, and partly by ATG4B. ATG4C showed no comparable PS preference, so its delipidation activity appears to act mainly on ATG8–PE [durgan-2021-noncanonical-abstract; durgan-2021-noncanonical-fulltext].

### 3.4 Deconjugation of ATG8–protein adducts

ATG8 proteins can also become covalently attached to other proteins, a modification called "ATG8ylation" or "LC3ylation". ATG4 proteases reverse these conjugates, acting like deubiquitinases [agrotis-2019-counteract-abstract; nguyen-2021-phagophore-abstract; nguyen-2021-atg4s-review-abstract]. These studies treated ATG4 proteases as a group. It has not been shown how much ATG4C specifically contributes to removing ATG8–protein conjugates.

## 4. Role in macroautophagy: evidence from cells

CRISPR knockouts in human cell lines show where ATG4C sits in the family hierarchy. Cells lacking ATG4B had severe defects in priming most LC3-subfamily proteins, yet still showed some GABARAP-subfamily lipidation. That residual priming did not depend only on ATG4A. In ATG4A/B double-knockout HeLa cells, siRNA depletion of both ATG4C and ATG4D was enough to completely block GABARAPL1 and GABARAPL2 lipidation. ATG4D was the larger contributor, but the complete block when both were removed showed that ATG4C also plays a part. This residual ATG4C/D activity did not depend on caspase-3 [agrotis-2019-redundancy-fulltext]. The same study found that ATG4-mediated delipidation is not essential for autophagosome formation, SQSTM1 turnover, or autophagosome–lysosome fusion when pre-primed LC3B is supplied at high levels. Even with ATG4C and ATG4D knocked down in ATG4A/B double-knockout cells, SQSTM1 rose only modestly [agrotis-2019-redundancy-fulltext]. In cell lines, then, ATG4C is a redundant back-up protease for GABARAP priming, and its delipidation activity matters less than it does for ATG8 recycling in tissues.

The ATG4 family also has a non-catalytic role. During PINK1/Parkin mitophagy, ATG4s promote phagophore growth independently of their protease activity and of ATG8 lipidation. They do this by supporting ATG9A vesicle trafficking to mitochondria (together with proximity partners such as LRBA and ARFIP2) and by promoting ER–phagophore contacts during the lipid-transfer phase [nguyen-2021-phagophore-abstract; nguyen-2021-atg4s-review-abstract]. Citing that work, the human UniProt entry states that ATG4C, unlike the other family members, is only weakly or not involved in this phagophore-growth function [uniprot-Q96DT6-entry]. The protease function therefore seems to be ATG4C's main contribution, not this structural or trafficking role.

## 5. Physiological function: evidence from mouse genetics

The first *Atg4c* knockout mouse paper (Mariño et al. 2007) reported reduced diaphragm autophagy during starvation and greater susceptibility to chemically induced fibrosarcoma [marino-2007-atg4c-ko-withdrawn-abstract]. It was withdrawn in 2019 [marino-2019-withdrawal-atg4c-ko-abstract]. UniProt also notes that the 2003 paper first describing the human autophagins (including ATG4C/autophagin-3), with their tissue expression and activity, was retracted over image-duplication concerns [marino-2003-autophagins-withdrawn-abstract; uniprot-Q96DT6-entry]. Neither withdrawn paper is used as evidence in this report.

The same group later produced and analysed a new *Atg4c*-null mouse [tamargo-gomez-2023-atg4c-invivo-fulltext]. In this model, atg4c⁻/⁻ mice developed normally, were fertile, and showed no compensating rise in *Atg4a*, *Atg4b* or *Atg4d* mRNA. MEFs from these mice had normal autophagic flux, normal SQSTM1 levels and normal LC3/GABARAP puncta. In tissues, however, there were tissue-specific changes in LC3A and LC3B lipidation, mainly in diaphragm, brain and spleen. In the diaphragm, fasting-induced autophagic flux was reduced. After fasting, the mutant mice failed to show the increases in O₂ consumption, CO₂ production, energy expenditure, locomotor activity and respiratory rate seen in wild-type mice. Analysis of public expression datasets showed that ATG4C is expressed at low levels in most tissues compared with ATG4B and ATG4D. It is, however, the most highly expressed ATG4 in B lymphocytes, dendritic cells and basophils. Consistent with this, atg4c⁻/⁻ mice had fewer circulating cytotoxic T cells, B cells and NK cells, more apoptosis in the spleen, more LC3-positive structures in the spleen, and more chemically induced fibrosarcomas with reduced lymphoid infiltration. The authors were careful to note that these immune phenotypes may involve functions of ATG4C outside autophagy [tamargo-gomez-2023-atg4c-invivo-fulltext].

The clearest mechanistic result came from compound mutants [tamargo-gomez-2023-atg4c-invivo-fulltext]. Loss of *Atg4c* on top of *Atg4b* loss did not change mATG8 priming or lipidation beyond the *Atg4b*⁻/⁻ phenotype. This fits ATG4C's minor role in priming. By contrast, atg4c/atg4d double-knockout tissues had more lipidated mATG8s than atg4d⁻/⁻ tissues, especially LC3A and GABARAPL2. In mKeima-LC3B assays, double-knockout cells had a lower acidic-to-neutral fluorescence ratio than atg4d⁻/⁻ cells. This means more LC3B remained on the cytosolic face of autolysosomes, because it had not been delipidated. SNAP-LC3B membrane-integration assays showed more LAMP1⁺ structures carrying LC3B in double-knockout MEFs than in atg4d⁻/⁻ MEFs. Finally, MEFs that express ATG4C as their only ATG4 ("ATG4C-only" MEFs) brought LC3B delipidation back to the level of atg4d⁻/⁻ cells, whereas quadruple-knockout cells could not delipidate at all. The authors concluded that ATG4C contributes to mATG8 delipidation in vivo, especially in the absence of ATG4D [tamargo-gomez-2023-atg4c-invivo-fulltext]. This agrees with the in vitro finding that all ATG4s can act on lipidated substrates [kauffman-2018-delipidation-abstract].

There is supporting evidence from another livestock mammal. In pig oocytes and early parthenogenetic embryos, ATG4C is highly expressed. Knocking it down by siRNA under serum-free conditions lowered LC3 signal, mitochondrial content, expression of zygotic-genome-activation genes, and blastocyst rates [yuan-2024-porcine-atg4c-abstract]. This suggests that ATG4C supports autophagy in early development in a non-model ungulate. However, this is a knockdown study with mostly correlative read-outs.

## 6. Subcellular localisation

UniProt annotates donkey ATG4C to the cytoplasm, based on automatic rules [uniprot-A0A9L0IIU3-entry]. The human entry assigns the same location by similarity to mouse ATG4C (Q8BGE6) [uniprot-Q96DT6-entry]. The enzyme's substrates set where it works. Pro-ATG8s are cleaved in the cytosol. ATG8–PE conjugates are delipidated on the cytosolic leaflet of phagophore, autophagosome and autolysosome membranes. The reporter assays in atg4c/atg4d-deficient cells show this directly: when delipidation fails, LC3B builds up on the cytosolic face of LAMP1-positive autolysosomes [tamargo-gomez-2023-atg4c-invivo-fulltext]. The structural model in which ATG4B's N-terminal tail comes away to expose a membrane-facing surface [satoo-2009-atg4b-lc3-structure-abstract], together with the LIR-dependent recognition of membrane-anchored substrates [kauffman-2018-delipidation-abstract], suggests that ATG4C works at the membrane surface while remaining a soluble cytosolic protein. A recent report links ATG4 proteases to the cytoskeletal adaptors OBSL1 and OBSCN. Loss of this interaction affects autophagy and mitophagy and leads, under stress, to ATG4 depletion and accumulation of LC3-II [actis-dato-2025-atg4-obscurin-abstract]. This points to possible cytoskeletal anchoring, but it has not been shown for ATG4C in particular.

## 7. Regulation

No regulatory mechanism has been shown for ATG4C specifically. Two mechanisms have been characterised for other ATG4s. First, Scherz-Shouval et al. showed that starvation-induced H₂O₂ is required for autophagy. It directly oxidises a cysteine near the catalytic site of human ATG4 (the isoform called HsAtg4A in that paper), and a mutant at this regulatory cysteine blocked autophagosome formation. This supports a model in which local oxidation inhibits delipidation at autophagosome-forming sites [scherz-shouval-2007-ros-atg4-abstract]. Second, ULK1 phosphorylates ATG4B on Ser316, which inhibits its catalytic activity, and the phosphatase PP2A–PPP2R3B reverses this. This phospho-switch coordinates priming and delipidation [pengo-2017-atg4b-phosphoswitch-abstract; pengo-2017-atg4b-phosphoswitch-fulltext]. The catalytic core of ATG4C, with its cysteines, is conserved, so similar redox control is plausible. Whether ATG4C carries an equivalent ULK1 site has not been tested. The ATG4 in-cell redundancy studies also showed that caspase-3, which activates ATG4D in vitro, is not required for ATG4C's residual activity [agrotis-2019-redundancy-fulltext].

## 8. Synthesis: predicted function of donkey ATG4C

Together, these lines of evidence give a consistent picture for the donkey protein. A0A9L0IIU3 is the one-to-one orthologue of mammalian ATG4C, with a fully conserved Cys111–Asp345–His347 catalytic triad and an ATG4-type LIR motif [uniprot-A0A9L0IIU3-entry; uniprot-Q96DT6-entry]. Its primary molecular function should be hydrolysis of the amide bond between the C-terminal glycine of ATG8-family proteins (LC3s, GABARAPs) and PE, which is the delipidation (ATG8–PE deconjugation) reaction. It should also have a weaker endopeptidase activity that primes pro-ATG8s, preferring GABARAP-subfamily substrates such as GABARAPL2 [li-2011-kinetics-abstract; kauffman-2018-delipidation-abstract; agrotis-2019-redundancy-fulltext]. It works in the cytosol on the membranes of the macroautophagy pathway. There it backs up ATG4D in recycling ATG8 from autolysosome and autophagosome membranes, and it backs up ATG4B and ATG4D in priming [tamargo-gomez-2023-atg4c-invivo-fulltext]. Physiologically, it is likely to matter most where it is relatively highly expressed (lymphoid and other immune cells in mice; oocytes and early embryos in pigs) and under prolonged nutrient stress in tissues such as the diaphragm [tamargo-gomez-2023-atg4c-invivo-fulltext; yuan-2024-porcine-atg4c-abstract]. The TreeGrafter-inferred GO annotations on the donkey entry for aggrephagy, mitophagy and "piecemeal microautophagy of the nucleus" are broad family-level propagations [uniprot-A0A9L0IIU3-entry]. In particular, the mitophagy-related phagophore-growth function described for the ATG4 family seems to involve ATG4C only weakly [uniprot-Q96DT6-entry; nguyen-2021-phagophore-abstract].

## Open Questions

There is no experimental data on ATG4C in donkeys or any other equid. The most direct follow-up would be to measure *ATG4C* transcript levels across donkey tissues and blood cell types (for example from existing donkey RNA-seq) and to test whether the strong immune-cell expression seen in mice also holds in equids. Biochemically, it would help to measure the kinetics of recombinant full-length ATG4C made in mammalian cells, not bacteria, because the activity difference noted by Durgan et al. [durgan-2021-noncanonical-fulltext] suggests the earlier "minimal activity" values [li-2011-kinetics-abstract] may underestimate its intrinsic activity. No ATG4C structure exists. Experimental structures alone or bound to LC3/GABARAP, perhaps starting from the AlphaFold model listed in the donkey entry, would show whether the regulatory loop and N-terminal tail behave as in ATG4B and would define the role of its LIR motif. How ATG4C is regulated (redox-sensitive cysteines, phosphorylation by ULK1 or other kinases, and binding partners such as OBSL1/OBSCN) remains unknown [scherz-shouval-2007-ros-atg4-abstract; pengo-2017-atg4b-phosphoswitch-abstract; actis-dato-2025-atg4-obscurin-abstract]. The immune phenotypes of *Atg4c*-null mice may come from autophagy-independent functions [tamargo-gomez-2023-atg4c-invivo-fulltext], and how much ATG4C contributes to removing ATG8–protein (ATG8ylation) conjugates [agrotis-2019-counteract-abstract] is not known. Finally, the 23 amino-acid differences between donkey and human ATG4C, which lie outside the catalytic motifs, are unlikely to affect catalysis. Whether any of them affect regulatory sites has not been examined.

## References

- **[uniprot-A0A9L0IIU3-entry]** UniProtKB/TrEMBL entry A0A9L0IIU3_EQUAS, "Cysteine protease" (gene ATG4C), *Equus asinus*; entry version 14 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0IIU3.txt
- **[uniprot-Q96DT6-entry]** UniProtKB/Swiss-Prot entry Q96DT6, ATG4C_HUMAN, Cysteine protease ATG4C, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/Q96DT6.txt
- **[wang-2020-donkey-genomes]** Wang C, Li H, Guo Y, et al. Donkey genomes provide new insights into domestication and selection for coat color. Nat Commun. 2020;11(1):6014. PMID:33293529; PMCID:PMC7723042; DOI:10.1038/s41467-020-19813-7.
- **[kirisako-2000-apg8-reversible]** Kirisako T, et al. The reversible modification regulates the membrane-binding state of Apg8/Aut7 essential for autophagy and the cytoplasm to vacuole targeting pathway. J Cell Biol. 2000;151(2):263-76. PMID:11038174; PMCID:PMC2192639; DOI:10.1083/jcb.151.2.263.
- **[tanida-2004-atg4b-delipidation]** Tanida I, Sou YS, Ezaki J, Minematsu-Ikeguchi N, Ueno T, Kominami E. HsAtg4B/HsApg4B/autophagin-1 cleaves the carboxyl termini of three human Atg8 homologues and delipidates microtubule-associated protein light chain 3- and GABAA receptor-associated protein-phospholipid conjugates. J Biol Chem. 2004;279(35):36268-76. PMID:15187094; DOI:10.1074/jbc.M401461200.
- **[kumanomidou-2006-atg4b-structure]** Kumanomidou T, et al. The crystal structure of human Atg4b, a processing and de-conjugating enzyme for autophagosome-forming modifiers. J Mol Biol. 2006;355(4):612-8. PMID:16325851; DOI:10.1016/j.jmb.2005.11.018.
- **[satoo-2009-atg4b-lc3-structure]** Satoo K, Noda NN, Kumeta H, Fujioka Y, Mizushima N, Ohsumi Y, Inagaki F. The structure of Atg4B-LC3 complex reveals the mechanism of LC3 processing and delipidation during autophagy. EMBO J. 2009;28(9):1341-50. PMID:19322194; PMCID:PMC2683054; DOI:10.1038/emboj.2009.80.
- **[scherz-shouval-2007-ros-atg4]** Scherz-Shouval R, Shvets E, Fass E, Shorer H, Gil L, Elazar Z. Reactive oxygen species are essential for autophagy and specifically regulate the activity of Atg4. EMBO J. 2007;26(7):1749-60. PMID:17347651; PMCID:PMC1847657; DOI:10.1038/sj.emboj.7601623.
- **[li-2011-kinetics]** Li M, Hou Y, Wang J, Chen X, Shao ZM, Yin XM. Kinetics comparisons of mammalian Atg4 homologues indicate selective preferences toward diverse Atg8 substrates. J Biol Chem. 2011;286(9):7327-38. PMID:21177865; PMCID:PMC3044989; DOI:10.1074/jbc.M110.199059.
- **[li-2017-atg4-activity-methods]** Li M, et al. Measurement of the Activity of the Atg4 Cysteine Proteases. Methods Enzymol. 2017;587:207-225. PMID:28253956; PMCID:PMC5582973; DOI:10.1016/bs.mie.2016.10.024.
- **[skytte-rasmussen-2017-atg4b-lir]** Skytte Rasmussen M, Mouilleron S, Kumar Shrestha B, et al. ATG4B contains a C-terminal LIR motif important for binding and efficient cleavage of mammalian orthologs of yeast Atg8. Autophagy. 2017;13(5):834-853. PMID:28287329; PMCID:PMC5446077; DOI:10.1080/15548627.2017.1287651.
- **[pengo-2017-atg4b-phosphoswitch]** Pengo N, Agrotis A, Prak K, Jones J, Ketteler R. A reversible phospho-switch mediated by ULK1 regulates the activity of autophagy protease ATG4B. Nat Commun. 2017;8(1):294. PMID:28821708; PMCID:PMC5562857; DOI:10.1038/s41467-017-00303-2.
- **[kauffman-2018-delipidation]** Kauffman KJ, et al. Delipidation of mammalian Atg8-family proteins by each of the four ATG4 proteases. Autophagy. 2018;14(6):992-1010. PMID:29458288; PMCID:PMC6103404; DOI:10.1080/15548627.2018.1437341.
- **[agrotis-2019-redundancy]** Agrotis A, et al. Redundancy of human ATG4 protease isoforms in autophagy and LC3/GABARAP processing revealed in cells. Autophagy. 2019;15(6):976-997. PMID:30661429; PMCID:PMC6526816; DOI:10.1080/15548627.2019.1569925.
- **[agrotis-2019-counteract]** Agrotis A, von Chamier L, Oliver H, Kiso K, Singh T, Ketteler R. Human ATG4 autophagy proteases counteract attachment of ubiquitin-like LC3/GABARAP proteins to other cellular proteins. J Biol Chem. 2019;294(34):12610-12621. PMID:31315929; PMCID:PMC6709618; DOI:10.1074/jbc.AC119.009977.
- **[nguyen-2020-atg4a-insufficiency]** Nguyen N, et al. The insufficiency of ATG4A in macroautophagy. J Biol Chem. 2020;295(39):13584-13600. PMID:32732290; PMCID:PMC7521654; DOI:10.1074/jbc.RA120.013897. (Consulted for background only; not cited in the text.)
- **[nguyen-2021-phagophore]** Nguyen TN, Padman BS, Zellner S, et al. ATG4 family proteins drive phagophore growth independently of the LC3/GABARAP lipidation system. Mol Cell. 2021;81(9):2013-2030.e9. PMID:33773106; DOI:10.1016/j.molcel.2021.03.001.
- **[nguyen-2021-atg4s-review]** Nguyen TN, Padman BS, Lazarou M. ATG4s: above and beyond the Atg8-family protein lipidation system. Autophagy. 2021;17(9):2648-2650. PMID:34308753; PMCID:PMC8496545; DOI:10.1080/15548627.2021.1953263.
- **[durgan-2021-noncanonical]** Durgan J, Lystad AH, Sloan K, et al. Non-canonical autophagy drives alternative ATG8 conjugation to phosphatidylserine. Mol Cell. 2021;81(9):2031-2040.e8. PMID:33909989; PMCID:PMC8122138; DOI:10.1016/j.molcel.2021.03.020.
- **[tamargo-gomez-2023-atg4c-invivo]** Tamargo-Gómez I, Martínez-García GG, Suárez MF, et al. Analysis of ATG4C function in vivo. Autophagy. 2023;19(11):2912-2933. PMID:37459465; PMCID:PMC10549197; DOI:10.1080/15548627.2023.2234799.
- **[yuan-2024-porcine-atg4c]** Yuan X, Yang T, Xu T, et al. Expression pattern of ATG4C and its effect on early embryonic development of porcine oocytes. Theriogenology. 2024;225:9-15. PMID:38781849; DOI:10.1016/j.theriogenology.2024.05.029.
- **[actis-dato-2025-atg4-obscurin]** Actis Dato V, Fujita K, Lange S. Novel links of ATG4 proteases to cytoskeletal adapters of the obscurin protein family. Autophagy. 2025;21(12):3433-3435. PMID:41094724; PMCID:PMC12758351; DOI:10.1080/15548627.2025.2572530.
- **[marino-2003-autophagins-withdrawn]** Mariño G, et al. Human autophagins, a family of cysteine proteinases potentially implicated in cell degradation by autophagy. J Biol Chem. 2003. PMID:12446702; DOI:10.1074/jbc.M208247200. RETRACTED (withdrawal PMID:30808002).
- **[marino-2007-atg4c-ko-withdrawn]** Mariño G, Salvador-Montoliu N, Fueyo A, Knecht E, Mizushima N, López-Otín C. Tissue-specific autophagy alterations and increased tumorigenesis in mice deficient in Atg4C/autophagin-3. J Biol Chem. 2007;282(25):18573-18583. PMID:17442669; DOI:10.1074/jbc.M701194200. RETRACTED.
- **[marino-2019-withdrawal-atg4c-ko]** Withdrawal: Tissue-specific autophagy alterations and increased tumorigenesis in mice deficient in Atg4C/autophagin-3. J Biol Chem. 2019;294(4):1435. PMID:30808006; PMCID:PMC6349109; DOI:10.1074/jbc.W118.007329.


## Citations

1. actis-dato-2025-atg4-obscurin-abstract.md
2. actis-dato-2025-atg4-obscurin-fulltext.txt
3. actis-dato-2025-atg4-obscurin-summary.md
4. agrotis-2019-counteract-abstract.md
5. agrotis-2019-counteract-fulltext.txt
6. agrotis-2019-counteract-summary.md
7. agrotis-2019-redundancy-abstract.md
8. agrotis-2019-redundancy-fulltext.txt
9. agrotis-2019-redundancy-summary.md
10. donkey.fa
11. durgan-2021-noncanonical-abstract.md
12. durgan-2021-noncanonical-fulltext.txt
13. durgan-2021-noncanonical-summary.md
14. human.fa
15. kauffman-2018-delipidation-abstract.md
16. kauffman-2018-delipidation-summary.md
17. kirisako-2000-apg8-reversible-abstract.md
18. kirisako-2000-apg8-reversible-fulltext.txt
19. kirisako-2000-apg8-reversible-summary.md
20. kumanomidou-2006-atg4b-structure-abstract.md
21. kumanomidou-2006-atg4b-structure-summary.md
22. li-2011-kinetics-abstract.md
23. li-2011-kinetics-summary.md
24. li-2017-atg4-activity-methods-abstract.md
25. li-2017-atg4-activity-methods-summary.md
26. marino-2003-autophagins-withdrawn-abstract.md
27. marino-2003-autophagins-withdrawn-summary.md
28. marino-2007-atg4c-ko-withdrawn-abstract.md
29. marino-2007-atg4c-ko-withdrawn-summary.md
30. marino-2019-withdrawal-atg4c-ko-abstract.md
31. marino-2019-withdrawal-atg4c-ko-summary.md
32. nguyen-2020-atg4a-insufficiency-abstract.md
33. nguyen-2020-atg4a-insufficiency-summary.md
34. nguyen-2021-atg4s-review-abstract.md
35. nguyen-2021-atg4s-review-summary.md
36. nguyen-2021-phagophore-abstract.md
37. nguyen-2021-phagophore-summary.md
38. pengo-2017-atg4b-phosphoswitch-abstract.md
39. pengo-2017-atg4b-phosphoswitch-fulltext.txt
40. pengo-2017-atg4b-phosphoswitch-summary.md
41. satoo-2009-atg4b-lc3-structure-abstract.md
42. satoo-2009-atg4b-lc3-structure-summary.md
43. scherz-shouval-2007-ros-atg4-abstract.md
44. scherz-shouval-2007-ros-atg4-summary.md
45. skytte-rasmussen-2017-atg4b-lir-abstract.md
46. skytte-rasmussen-2017-atg4b-lir-summary.md
47. tamargo-gomez-2023-atg4c-invivo-abstract.md
48. tamargo-gomez-2023-atg4c-invivo-fulltext.txt
49. tamargo-gomez-2023-atg4c-invivo-summary.md
50. tanida-2004-atg4b-delipidation-abstract.md
51. tanida-2004-atg4b-delipidation-summary.md
52. uniprot-A0A9L0IIU3-entry.txt
53. uniprot-Q96DT6-entry.txt
54. wang-2020-donkey-genomes-abstract.md
55. wang-2020-donkey-genomes-summary.md
56. yuan-2024-porcine-atg4c-abstract.md
57. yuan-2024-porcine-atg4c-summary.md