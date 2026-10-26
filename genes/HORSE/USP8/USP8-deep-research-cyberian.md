---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:44:19.765249'
end_time: '2026-10-26T03:52:08.423054'
duration_seconds: 468.66
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: USP8
  gene_symbol: USP8
  uniprot_accession: A0A9L0T7K6
  protein_description: 'RecName: Full=Ubiquitin carboxyl-terminal hydrolase {ECO:0000256|PROSITE-ProRule:PRU10092};
    EC=3.4.19.12 {ECO:0000256|PROSITE-ProRule:PRU10092};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the peptidase C19 family.
  protein_domains: Papain-like_cys_pep_sf. (IPR038765); Peptidase_C19_UCH. (IPR001394);
    Rhodanese-like_dom. (IPR001763); Rhodanese-like_dom_sf. (IPR036873); Ub_carboxyl-term_hydrolase.
    (IPR050185)
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
citation_count: 67
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0T7K6
- **Protein Description:** RecName: Full=Ubiquitin carboxyl-terminal hydrolase {ECO:0000256|PROSITE-ProRule:PRU10092}; EC=3.4.19.12 {ECO:0000256|PROSITE-ProRule:PRU10092};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the peptidase C19 family.
- **Key Domains:** Papain-like_cys_pep_sf. (IPR038765); Peptidase_C19_UCH. (IPR001394); Rhodanese-like_dom. (IPR001763); Rhodanese-like_dom_sf. (IPR036873); Ub_carboxyl-term_hydrolase. (IPR050185)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "USP8" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'USP8' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **USP8** (gene ID: USP8, UniProt: A0A9L0T7K6) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# USP8 (Ubiquitin carboxyl-terminal hydrolase 8) in the horse, *Equus caballus* — UniProt A0A9L0T7K6

## 1. Introduction and summary

UniProt entry A0A9L0T7K6 is an unreviewed (TrEMBL) protein of 1,112 residues predicted from the Thoroughbred reference genome. It is annotated as a ubiquitin carboxyl-terminal hydrolase (EC 3.4.19.12) of the peptidase C19 (ubiquitin-specific protease, USP) family. It has a rhodanese-like domain (residues 195–313) and a C-terminal USP catalytic domain (residues 776–1108), with predicted catalytic Cys785 and His1066 [uniprot-2026-A0A9L0T7K6-entry]. The entry has no gene name, but its domain content (an N-terminal USP8_dimer/MIT-like domain, a WW_USP8 region, rhodanese, and USP) and its PANTHER subfamily (PTHR21646:SF27, "Ubiquitin carboxyl-terminal hydrolase 8") identify it as USP8 [uniprot-2026-A0A9L0T7K6-entry]. I aligned it with human USP8 (P40818; 1,118 aa) [uniprot-2026-P40818-human-usp8-entry]. The two are about 91% identical across the full length, and every functional motif characterised in the human and mouse proteins is conserved in the horse sequence (see `SEQUENCE_ANALYSIS.md`). The symbol "USP8" is therefore not ambiguous here: A0A9L0T7K6 is the horse ortholog of the well-studied mammalian deubiquitinase USP8, also known as UBPY.

No experimental study of horse USP8 itself could be found. Searches combining USP8/UBPY with horse, equine or *Equus* found only a comparative review of Cushing's disease in animals. That review discusses USP8 for humans and dogs but reports no USP8 data for horses [massardi-2025-cushing-animals]. Everything below about function is therefore inferred from orthology, mainly from human and mouse work. Given the 91% identity and the conservation of catalytic and regulatory motifs, this inference is strong for the core biochemistry. It is weaker for tissue-specific and disease-related roles.

USP8 is a cysteine protease that removes ubiquitin from proteins. It hydrolyses the isopeptide (and linear peptide) bond after the C-terminal Gly76 of ubiquitin. It acts on both monoubiquitinated substrates and K48- and K63-linked polyubiquitin chains [naviglio-1998-ubpy-growth; row-2006-ubpy-endosomal-ubiquitin]. Its best-supported role is at the early endosome. There it binds the ESCRT-0 complex (HRS–STAM) and ESCRT-III CHMP proteins, and it controls the ubiquitination of internalised membrane receptors (EGFR, MET, Frizzled, Smoothened and others) and of the sorting machinery itself. This decides whether receptors go to the lysosome for degradation or back to the cell surface [mizuno-2005-ubpy-egfr-endosomes; row-2006-ubpy-endosomal-ubiquitin; row-2007-ubpy-mit-chmp; niendorf-2007-usp8-knockout; dufner-2019-usp8-review]. Its activity is held back by phosphorylation-dependent binding of 14-3-3 proteins. In humans, mutations that disrupt this binding activate USP8 and cause Cushing's disease [mizuno-2007-ubpy-14-3-3; reincke-2015-usp8-cushing; ma-2015-usp8-cushing].

## 2. Gene identity, evolutionary conservation and domain architecture

The horse gene model (Ensembl ENSECAG00000006611, chromosome 1) comes from the EquCab genome assembly [wade-2009-horse-genome; uniprot-2026-A0A9L0T7K6-entry]. The protein-existence level is "inferred from homology", and all functional annotations in the entry are automatic transfers (ARBA rules, PROSITE ProRules) [uniprot-2026-A0A9L0T7K6-entry]. My alignment shows the first 36 residues identical to human USP8. The divergence that exists sits mostly in the long disordered, charged segments between the structured domains, which UniProt marks as MobiDB-lite disordered regions (121–179, 411–640, 678–748) [uniprot-2026-A0A9L0T7K6-entry].

Mammalian USP8 is a multidomain protein, and each module has a defined interaction role [dufner-2019-usp8-review].

Moving from the N terminus, the first module was characterised in two ways. Crystallography showed that it forms a homodimer with a new fold of two helix-swapped five-helix bundles [avvakumov-2006-usp8-structure], and functional work showed that the same region acts as a microtubule-interacting-and-transport (MIT) domain. This MIT domain binds ESCRT-III CHMP proteins (CHMP1A and CHMP1B, which AMSH also binds, and preferentially CHMP7) and is needed to bring USP8 to endosomes, though not for catalysis [row-2007-ubpy-mit-chmp]. The central region carries two atypical SH3-binding motifs with the consensus PX(V/I)(D/N)RXXKP, which bind the SH3 domain of STAM/Hbp, a subunit of ESCRT-0 [kato-2000-ubpy-stam-sh3]. Both are conserved in the horse protein, as PQIDRTKKP at residue 405 and PTVNRENKP at residue 737 (own analysis). They flank the 14-3-3 binding motif RSYSSP [dufner-2019-usp8-review], which lies at horse residues 714–719. Next comes a rhodanese-like domain whose primordial active site is distorted and probably not catalytic. This domain binds the E3 ligase NRDP1/RNF41 through a conserved peptide loop [avvakumov-2006-usp8-structure], and together with the catalytic domain it mediates binding and stabilisation of NRDP1 [wu-2004-usp8-nrdp1]. The C-terminal USP domain has the conserved fingers–palm–thumb architecture and a zinc-ribbon subdomain. In the crystal, however, its active site and ubiquitin-binding pocket are closed and autoinhibited, which suggests that substrate binding triggers a conformational change [avvakumov-2006-usp8-structure]. The catalytic Cys box (…LGNTCYMNSILQCL…) and His box (…GHYTAY…) are fully conserved in horse as Cys785 and His1066, matching human Cys786 and His1067 (own analysis).

The 14-3-3 binding motif, and the exon encoding it, are described as identically conserved across species [ma-2015-usp8-cushing]. The horse sequence fits this: the motif and its flanks (…KLKRSYSSPDITQ…) match human exactly. This conservation matters because the motif is the main regulatory switch of the enzyme (Section 5).

## 3. Catalytic activity and substrate specificity

USP8 is a thiol-dependent ubiquitin isopeptidase. Human UBPY was first described as a growth-regulated enzyme that cleaves both linear and isopeptide-linked ubiquitin chains, both as a recombinant protein and when immunoprecipitated from cells [naviglio-1998-ubpy-growth]. Later work showed that it removes ubiquitin from monoubiquitinated receptor tyrosine kinases and trims K48- and K63-linked polyubiquitin to shorter forms in vitro [row-2006-ubpy-endosomal-ubiquitin]. A kinetic survey of twelve USPs found that USP enzymes, USP8 included, can hydrolyse all ubiquitin linkage types with only modest preferences, and that intramolecular domains and binding partners change both turnover (k_cat) and ubiquitin affinity (K_M) [faesen-2011-usp-linkage]. USP8 can also show linkage preference in cells: it preferentially removes non-canonical K6-linked chains from the E3 ligase parkin [durcan-2014-usp8-parkin]. On endosomes it removes K63-linked chains, the main signal for endocytic sorting [endo-2024-usp8-endosomal-stress].

Specificity for particular substrates comes mostly from recruitment, not from the catalytic domain's linkage selectivity. STAM binding stimulates USP8 deubiquitinating activity, while the CHMP proteins it binds do not [row-2007-ubpy-mit-chmp]. The demonstrated substrates of mammalian USP8 fall into three groups. The first is internalised membrane receptors, namely EGFR [mizuno-2005-ubpy-egfr-endosomes; alwan-2007-ubpy-egfr-degradation], the Wnt receptor Frizzled [mukai-2010-ubpy-frizzled] and the Hedgehog transducer Smoothened [xia-2012-usp8-smoothened]. The second is the endocytic machinery itself. This includes the adaptor Eps15 [mizuno-2006-ubpy-endosome-ubiquitination]; the ESCRT-0 subunits STAM and HRS, which become unstable when USP8 is lost [row-2006-ubpy-endosomal-ubiquitin; niendorf-2007-usp8-knockout]; and the ESCRT-III subunit CHMP1B [crespo-2018-usp8-chmp1b]. The third is E3 ubiquitin ligases and their partners, including NRDP1/RNF41 [wu-2004-usp8-nrdp1], parkin [durcan-2014-usp8-parkin] and the Ras exchange factor Ras-GRF1/CDC25Mm [gnesutta-2001-mouse-ubpy-rasgrf1].

The review by Dufner and Knobeloch also lists ERBB2, PAR2, the potassium channel KCa3.1, ENaC, LDLR and LRIG1 among membrane proteins whose trafficking or stability depends on USP8 [dufner-2019-usp8-review].

## 4. Endosomal sorting: the canonical function

The best-established role of USP8 is in the endosomal sorting of ubiquitinated cargo. Mizuno et al. showed that UBPY deubiquitinates EGFR in vitro, binds EGFR after EGF stimulation, and accumulates on endosomes. They also showed that a catalytically inactive mutant localises to EGFR-positive endosomes [mizuno-2005-ubpy-egfr-endosomes]. When USP8 is inactivated, ubiquitinated proteins pile up on abnormal clusters of multivesicular endosomes [mizuno-2006-ubpy-endosome-ubiquitination; row-2006-ubpy-endosomal-ubiquitin]. The steady-state amount of ubiquitin on endosomes therefore depends on USP8.

Whether USP8 speeds or slows EGFR degradation has been disputed. Mizuno et al. found that USP8 knockdown accelerated EGF-induced EGFR degradation and concluded that USP8 slows downregulation [mizuno-2005-ubpy-egfr-endosomes]. Row et al. found the opposite: UBPY knockdown strongly blocked degradation of acutely stimulated EGFR and MET [row-2006-ubpy-endosomal-ubiquitin]. Alwan and van Leeuwen used three dominant-negative constructs and supported the view that UBPY-mediated deubiquitination promotes EGFR degradation [alwan-2007-ubpy-egfr-degradation]. The Dufner and Knobeloch review suggests that some of the conflict comes from the massive global ubiquitination and proteolytic stress caused by depleting USP8 or overexpressing an inactive enzyme, and from differences between cell types [dufner-2019-usp8-review].

The current model brings these results together. Ubiquitin has to be removed from cargo before it enters intralumenal vesicles, and USP8 works at the hand-off from ubiquitin-binding ESCRT-0 to ESCRT-III, which does not bind ubiquitin. In this step the ESCRT accessory protein HD-PTP/PTPN23 recruits UBPY to EGFR through CHMP4B and STAM2. UBPY binding to the STAM2 SH3 domain displaces ESCRT-0 from HD-PTP, and the deubiquitinated EGFR is released to ESCRT-III [ali-2013-ubpy-hdptp]. USP8 also removes the ubiquitin that EGF induces on CHMP1B, which may let CHMP1B assemble into membrane-associated ESCRT-III polymers [crespo-2018-usp8-chmp1b].

USP8 also protects the sorting machinery itself. It opposes AIP4/Itch-mediated ubiquitination of ESCRT-0, which promotes CXCR4 trafficking without changing CXCR4's own ubiquitination [berlin-2010-usp8-cxcr4]. More recent work places USP8 upstream of endosome maturation as well. Rabex5 recruits USP8 to Rab5-positive endosomes, where USP8 displaces Rabex5 and promotes recruitment of the Rab7 GEF Mon1/SAND-1. Without USP8, cells accumulate enlarged early endosomes and form only rudimentary lysosomes [miao-2024-usp8-endosome-maturation].

For some receptors, removing ubiquitin sends them back to the surface rather than on to degradation. Frizzled deubiquitinated by USP8 recycles to the plasma membrane, which raises Wnt responsiveness [mukai-2010-ubpy-frizzled]. In Drosophila, USP8 removes ubiquitin from Smoothened, keeping it at the cell surface and out of early endosomes, which increases Hedgehog signalling [xia-2012-usp8-smoothened]. USP8 therefore acts as a rheostat: the balance between ubiquitination and deubiquitination of a receptor sets how strongly the cell responds to its ligand [mukai-2010-ubpy-frizzled].

A newer finding is that USP8 keeps K63-linked ubiquitin from building up on endosomes. If such chains accumulate, they recruit the decoders TAB2/3 and p62, which inappropriately switch on the TAK1–NF-κB and Keap1–Nrf2 pathways. Oxidative stress can mimic this by suppressing USP8 activity [endo-2024-usp8-endosomal-stress].

## 5. Regulation: 14-3-3 binding, phosphorylation, proteolytic processing and the cell cycle

USP8 activity is regulated by phosphorylation. Mizuno et al. identified 14-3-3 ε, γ and ζ as UBPY partners that bind the phosphorylated motif RSYS*SP. The phospho-serine was numbered Ser680 in their construct, corresponding to Ser718 of human P40818 and Ser717 of horse A0A9L0T7K6. Mutating this serine increased activity toward polyubiquitin and EGFR, and adding 14-3-3ε inhibited UBPY in vitro. During M phase UBPY is dephosphorylated at this site and released from 14-3-3, which raises its activity during cell division [mizuno-2007-ubpy-14-3-3]. Ma et al. describe this site as S718 of human USP8 and summarise the same mechanism [ma-2015-usp8-cushing].

Inactivating 14-3-3 binding also makes USP8 more susceptible to proteolytic cleavage. Cleavage produces a C-terminal fragment of about 40 kDa that contains the catalytic domain and is constitutively active [reincke-2015-usp8-cushing; dufner-2019-usp8-review]. This processing also happens normally: USP8 is cleaved in a caspase-dependent way when the T-cell receptor is stimulated, and it binds Gads and 14-3-3β in the TCR signalosome [dufner-2015-usp8-tcells]. After EGF stimulation, USP8 is also a substrate of Src-family kinases [alwan-2007-ubpy-egfr-degradation].

The cell-cycle link goes back to the discovery of the enzyme. UBPY levels rise with growth stimulation and fall with contact inhibition, and blocking UBPY accumulation prevents fibroblasts from entering S phase [naviglio-1998-ubpy-growth]. During cytokinesis, UBPY moves to the midbody, deubiquitinates the v-SNARE VAMP8, and is required for cytokinesis to complete [mukai-2008-ubpy-cytokinesis]. These observations fit the UniProt keyword "Cell cycle" and the GO term "midbody" transferred to the horse entry [uniprot-2026-A0A9L0T7K6-entry].

## 6. Subcellular localization

The horse entry's predicted localisations (cytoplasm/cytosol, endosome membrane as a peripheral membrane protein, plasma membrane, nucleus and midbody) are all transferred from mammalian experimental data [uniprot-2026-A0A9L0T7K6-entry]. Experimental work places USP8 mainly in the cytosol, from which it is recruited to early endosomes. Three things drive this recruitment: its MIT domain [row-2007-ubpy-mit-chmp], ESCRT-0 [mizuno-2005-ubpy-egfr-endosomes] and the Rab5 exchange factor Rabex5 [miao-2024-usp8-endosome-maturation]. The endosomal pool is easiest to see with catalytically inactive USP8, which becomes trapped on these membranes [mizuno-2005-ubpy-egfr-endosomes; row-2006-ubpy-endosomal-ubiquitin]. USP8 also localises to the midbody late in cytokinesis [mukai-2008-ubpy-cytokinesis]. It is found in the nucleus as well, and in USP8-mutant corticotroph adenomas the protein is strongly nuclear, but few nuclear functions have yet been defined [dufner-2019-usp8-review].

So the main site of action for horse USP8 is expected to be the cytosolic face of early and sorting endosomes, with additional pools at the plasma membrane, the midbody and the nucleus.

## 7. Physiological roles and disease relevance, with comments on the horse

USP8 is essential in mammals. Usp8 knockout mice die as embryos. Inducible deletion in adult mice causes fatal liver failure, with loss of EGFR, MET and ERBB3, enlarged ubiquitin-rich early endosomes, and reduced HRS and STAM2. Immortalised cells stop proliferating after Usp8 is deleted [niendorf-2007-usp8-knockout]. Deleting USP8 only in T cells disrupts thymocyte maturation through a Foxo1–IL-7Rα pathway and causes colitis [dufner-2015-usp8-tcells].

In humans, somatic gain-of-function mutations in the exon encoding the 14-3-3 motif cause a large share of ACTH-secreting pituitary corticotroph adenomas, the cause of Cushing's disease. One study found them in 4 of 10 adenomas [reincke-2015-usp8-cushing]. A larger study found them in 67 of 108 ACTH-secreting adenomas and in none of 150 other adenoma types [ma-2015-usp8-cushing]. The mutations block 14-3-3 binding, increase cleavage and activity, stabilise EGFR, and drive POMC expression and ACTH secretion. Blocking USP8 or EGFR reduces ACTH secretion in primary tumour cells [reincke-2015-usp8-cushing; ma-2015-usp8-cushing].

This is directly relevant to horses, because equine Cushing's disease, now called pituitary pars intermedia dysfunction (PPID), affects roughly 20–25% of older horses. The disease mechanism differs from the human one, however. Equine PPID is attributed to neurodegenerative loss of hypothalamic dopaminergic inhibition over the melanotropes of the pars intermedia, not to a primary corticotroph adenoma of the anterior lobe [massardi-2025-cushing-animals]. The same review notes that USP8 mutations have not been found in canine ACTH-secreting adenomas, although dog tumours show increased nuclear USP8. It reports no studies of USP8 in equine PPID [massardi-2025-cushing-animals]. Any role for USP8 in horse pituitary disease is therefore untested.

Several other roles described in other organisms are plausibly conserved in the horse but have not been examined there: parkin-dependent mitophagy [durcan-2014-usp8-parkin], Wnt and Hedgehog receptor trafficking [mukai-2010-ubpy-frizzled; xia-2012-usp8-smoothened], and control of NF-κB and Nrf2 signalling from endosomes [endo-2024-usp8-endosomal-stress].

## 8. Open Questions

The most basic gap is that no experiment has been reported on horse USP8 at all. The gene model has not even been curated with a gene symbol in UniProt. It would be useful to confirm expression and splicing in equine tissues, especially the pituitary pars intermedia, liver and immune cells, and to check whether the N-terminal and disordered-region differences from human change the interaction motifs.

A second question is whether *USP8* takes part in equine PPID. Sequencing the 14-3-3-motif exon in pars intermedia adenomas and hyperplasias from PPID horses, and staining for nuclear USP8 as has been done in dogs, would test whether the human mechanism contributes in the horse. Because equine PPID is mainly dopaminergic and neurodegenerative, a negative result would be informative too.

Third, the dispute over whether USP8 promotes or opposes EGFR degradation [mizuno-2005-ubpy-egfr-endosomes; row-2006-ubpy-endosomal-ubiquitin; alwan-2007-ubpy-egfr-degradation] is still not fully resolved. Acute, specific inhibition (chemical or degron-based) instead of chronic depletion would separate direct cargo deubiquitination from secondary collapse of ESCRT-0.

Fourth, the nuclear pool of USP8 and its substrates are poorly understood [dufner-2019-usp8-review]. So is the protease responsible for USP8 cleavage, along with how the ~40 kDa fragment is regulated in normal physiology [dufner-2015-usp8-tcells; reincke-2015-usp8-cushing].

Finally, the closed, autoinhibited crystal structure of the catalytic domain [avvakumov-2006-usp8-structure] raises the question of how STAM binding, 14-3-3 release and cleavage each open the active site. Structures of full-length or partner-bound USP8 would help answer it.

## 9. References

* **uniprot-2026-A0A9L0T7K6-entry** — UniProt Consortium. UniProtKB/TrEMBL entry A0A9L0T7K6 (A0A9L0T7K6_HORSE), Ubiquitin carboxyl-terminal hydrolase, *Equus caballus*; entry version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0T7K6.txt
* **uniprot-2026-P40818-human-usp8-entry** — UniProt Consortium. UniProtKB/Swiss-Prot entry P40818 (UBP8_HUMAN), Ubiquitin carboxyl-terminal hydrolase 8. https://rest.uniprot.org/uniprotkb/P40818.txt
* **ali-2013-ubpy-hdptp** — Ali N, Zhang L, Taylor S, Mironov A, Urbé S, Woodman P. (2013). Recruitment of UBPY and ESCRT exchange drive HD-PTP-dependent sorting of EGFR to the MVB. Current Biology 23:453-461. PMID: 23477725; DOI: 10.1016/j.cub.2013.02.033. https://pubmed.ncbi.nlm.nih.gov/23477725/
* **alwan-2007-ubpy-egfr-degradation** — Alwan HA, van Leeuwen JE. (2007). UBPY-mediated epidermal growth factor receptor (EGFR) de-ubiquitination promotes EGFR degradation. J Biol Chem 282:1658-1669. PMID: 17121848; DOI: 10.1074/jbc.m604711200. https://pubmed.ncbi.nlm.nih.gov/17121848/
* **avvakumov-2006-usp8-structure** — Avvakumov GV, Walker JR, Xue S, Finerty PJ, Mackenzie F, Newman EM, Dhe-Paganon S. (2006). Amino-terminal dimerization, NRDP1-rhodanese interaction, and inhibited catalytic domain conformation of the ubiquitin-specific protease 8 (USP8). J Biol Chem 281:38061-38070. PMID: 17035239; DOI: 10.1074/jbc.m606704200. https://pubmed.ncbi.nlm.nih.gov/17035239/
* **berlin-2010-usp8-cxcr4** — Berlin I, Higginbotham KM, Dise RS, Sierra MI, Nash PD. (2010). The deubiquitinating enzyme USP8 promotes trafficking and degradation of the chemokine receptor 4 at the sorting endosome. J Biol Chem 285:37895-37908. PMID: 20876529; PMCID: PMC2988392; DOI: 10.1074/jbc.m110.129411. https://pubmed.ncbi.nlm.nih.gov/20876529/
* **crespo-2018-usp8-chmp1b** — Crespo-Yàñez X, Aguilar-Gurrieri C, Jacomin AC, Journet A, Mortier M, Taillebourg E, Soleilhac E, Weissenhorn W, Fauvarque MO. (2018). CHMP1B is a target of USP8/UBPY regulated by ubiquitin during endocytosis. PLoS Genetics 14:e1007456. PMID: 29933386; PMCID: PMC6033466; DOI: 10.1371/journal.pgen.1007456. https://pubmed.ncbi.nlm.nih.gov/29933386/
* **dufner-2015-usp8-tcells** — Dufner A, Kisser A, Niendorf S, et al., Knobeloch KP. (2015). The ubiquitin-specific protease USP8 is critical for the development and homeostasis of T cells. Nature Immunology 16:950-960. PMID: 26214742; DOI: 10.1038/ni.3230. https://pubmed.ncbi.nlm.nih.gov/26214742/
* **dufner-2019-usp8-review** — Dufner A, Knobeloch KP. (2019). Ubiquitin-specific protease 8 (USP8/UBPy): a prototypic multidomain deubiquitinating enzyme with pleiotropic functions. Biochem Soc Trans 47:1867-1879. PMID: 31845722; PMCID: PMC6925526; DOI: 10.1042/bst20190527. https://pubmed.ncbi.nlm.nih.gov/31845722/
* **durcan-2014-usp8-parkin** — Durcan TM, Tang MY, Pérusse JR, et al., Fon EA. (2014). USP8 regulates mitophagy by removing K6-linked ubiquitin conjugates from parkin. EMBO J 33:2473-2491. PMID: 25216678; PMCID: PMC4283406; DOI: 10.15252/embj.201489729. https://pubmed.ncbi.nlm.nih.gov/25216678/
* **endo-2024-usp8-endosomal-stress** — Endo A, Fukushima T, Takahashi C, et al., Komada M. (2024). USP8 prevents aberrant NF-κB and Nrf2 activation by counteracting ubiquitin signals from endosomes. J Cell Biol 223:e202306013. PMID: 38180476; PMCID: PMC10783432; DOI: 10.1083/jcb.202306013. https://pubmed.ncbi.nlm.nih.gov/38180476/
* **faesen-2011-usp-linkage** — Faesen AC, Luna-Vargas MP, Geurink PP, et al., Sixma TK. (2011). The differential modulation of USP activity by internal regulatory domains, interactors and eight ubiquitin chain types. Chem Biol 18:1550-1561. PMID: 22195557; DOI: 10.1016/j.chembiol.2011.10.017. https://pubmed.ncbi.nlm.nih.gov/22195557/
* **gnesutta-2001-mouse-ubpy-rasgrf1** — Gnesutta N, Ceriani M, Innocenti M, et al., Martegani E. (2001). Cloning and characterization of mouse UBPy, a deubiquitinating enzyme that interacts with the ras guanine nucleotide exchange factor CDC25(Mm)/Ras-GRF1. J Biol Chem 276:39448-39454. PMID: 11500497; DOI: 10.1074/jbc.m103454200. https://pubmed.ncbi.nlm.nih.gov/11500497/
* **kato-2000-ubpy-stam-sh3** — Kato M, Miyazawa K, Kitamura N. (2000). A deubiquitinating enzyme UBPY interacts with the Src homology 3 domain of Hrs-binding protein via a novel binding motif PX(V/I)(D/N)RXXKP. J Biol Chem 275:37481-37487. PMID: 10982817; DOI: 10.1074/jbc.m007251200. https://pubmed.ncbi.nlm.nih.gov/10982817/
* **ma-2015-usp8-cushing** — Ma ZY, Song ZJ, Chen JH, et al., Zhao Y. (2015). Recurrent gain-of-function USP8 mutations in Cushing's disease. Cell Research 25:306-317. PMID: 25675982; PMCID: PMC4349249; DOI: 10.1038/cr.2015.20. https://pubmed.ncbi.nlm.nih.gov/25675982/
* **massardi-2025-cushing-animals** — Massardi E, Gaudenzi G, Carra S, Oldani M, Rybinska I, Persani L, Vitale G. (2025). Cushing's Disease in the Animal Kingdom: Translational Insights for Human Medicine. Int J Mol Sci 26:8626. PMID: 40943544; PMCID: PMC12429187; DOI: 10.3390/ijms26178626. https://pubmed.ncbi.nlm.nih.gov/40943544/
* **miao-2024-usp8-endosome-maturation** — Miao Y, Du Y, Wang B, et al., Ding M. (2024). Spatiotemporal recruitment of the ubiquitin-specific protease USP8 directs endosome maturation. eLife 13:RP96353. PMID: 39576689; PMCID: PMC11584181; DOI: 10.7554/elife.96353. https://pubmed.ncbi.nlm.nih.gov/39576689/
* **mizuno-2005-ubpy-egfr-endosomes** — Mizuno E, Iura T, Mukai A, Yoshimori T, Kitamura N, Komada M. (2005). Regulation of epidermal growth factor receptor down-regulation by UBPY-mediated deubiquitination at endosomes. Mol Biol Cell 16:5163-5174. PMID: 16120644; DOI: 10.1091/mbc.e05-06-0560. https://pubmed.ncbi.nlm.nih.gov/16120644/
* **mizuno-2006-ubpy-endosome-ubiquitination** — Mizuno E, Kobayashi K, Yamamoto A, Kitamura N, Komada M. (2006). A deubiquitinating enzyme UBPY regulates the level of protein ubiquitination on endosomes. Traffic 7:1017-1031. PMID: 16771824; DOI: 10.1111/j.1600-0854.2006.00452.x. https://pubmed.ncbi.nlm.nih.gov/16771824/
* **mizuno-2007-ubpy-14-3-3** — Mizuno E, Kitamura N, Komada M. (2007). 14-3-3-dependent inhibition of the deubiquitinating activity of UBPY and its cancellation in the M phase. Exp Cell Res 313:3624-3634. PMID: 17720156; DOI: 10.1016/j.yexcr.2007.07.028. https://pubmed.ncbi.nlm.nih.gov/17720156/
* **mukai-2008-ubpy-cytokinesis** — Mukai A, Mizuno E, Kobayashi K, Matsumoto M, Nakayama KI, Kitamura N, Komada M. (2008). Dynamic regulation of ubiquitylation and deubiquitylation at the central spindle during cytokinesis. J Cell Sci 121:1325-1333. PMID: 18388320; DOI: 10.1242/jcs.027417. https://pubmed.ncbi.nlm.nih.gov/18388320/
* **mukai-2010-ubpy-frizzled** — Mukai A, Yamamoto-Hino M, Awano W, Watanabe W, Komada M, Goto S. (2010). Balanced ubiquitylation and deubiquitylation of Frizzled regulate cellular responsiveness to Wg/Wnt. EMBO J 29:2114-2125. PMID: 20495530; PMCID: PMC2905240; DOI: 10.1038/emboj.2010.100. https://pubmed.ncbi.nlm.nih.gov/20495530/
* **naviglio-1998-ubpy-growth** — Naviglio S, Mattecucci C, Matoskova B, Nagase T, Nomura N, Di Fiore PP, Draetta GF. (1998). UBPY: a growth-regulated human ubiquitin isopeptidase. EMBO J 17:3241-3250. PMID: 9628861; PMCID: PMC1170662; DOI: 10.1093/emboj/17.12.3241. https://pubmed.ncbi.nlm.nih.gov/9628861/
* **niendorf-2007-usp8-knockout** — Niendorf S, Oksche A, Kisser A, Löhler J, Prinz M, Schorle H, Feller S, Lewitzky M, Horak I, Knobeloch KP. (2007). Essential role of ubiquitin-specific protease 8 for receptor tyrosine kinase stability and endocytic trafficking in vivo. Mol Cell Biol 27:5029-5039. PMID: 17452457; PMCID: PMC1951504; DOI: 10.1128/mcb.01566-06. https://pubmed.ncbi.nlm.nih.gov/17452457/
* **reincke-2015-usp8-cushing** — Reincke M, Sbiera S, Hayakawa A, et al., Komada M. (2015). Mutations in the deubiquitinase gene USP8 cause Cushing's disease. Nature Genetics 47:31-38. PMID: 25485838; DOI: 10.1038/ng.3166. https://pubmed.ncbi.nlm.nih.gov/25485838/
* **row-2006-ubpy-endosomal-ubiquitin** — Row PE, Prior IA, McCullough J, Clague MJ, Urbé S. (2006). The ubiquitin isopeptidase UBPY regulates endosomal ubiquitin dynamics and is essential for receptor down-regulation. J Biol Chem 281:12618-12624. PMID: 16520378; DOI: 10.1074/jbc.m512615200. https://pubmed.ncbi.nlm.nih.gov/16520378/
* **row-2007-ubpy-mit-chmp** — Row PE, Liu H, Hayes S, Welchman R, Charalabous P, Hofmann K, Clague MJ, Sanderson CM, Urbé S. (2007). The MIT domain of UBPY constitutes a CHMP binding and endosomal localization signal required for efficient epidermal growth factor receptor degradation. J Biol Chem 282:30929-30937. PMID: 17711858; DOI: 10.1074/jbc.m704009200. https://pubmed.ncbi.nlm.nih.gov/17711858/
* **wade-2009-horse-genome** — Wade CM, Giulotto E, Sigurdsson S, et al., Lindblad-Toh K. (2009). Genome sequence, comparative analysis, and population genetics of the domestic horse. Science 326:865-867. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158. https://pubmed.ncbi.nlm.nih.gov/19892987/
* **wu-2004-usp8-nrdp1** — Wu X, Yen L, Irwin L, Sweeney C, Carraway KL. (2004). Stabilization of the E3 ubiquitin ligase Nrdp1 by the deubiquitinating enzyme USP8. Mol Cell Biol 24:7748-7757. PMID: 15314180; PMCID: PMC506982; DOI: 10.1128/mcb.24.17.7748-7757.2004. https://pubmed.ncbi.nlm.nih.gov/15314180/
* **xia-2012-usp8-smoothened** — Xia R, Jia H, Fan J, Liu Y, Jia J. (2012). USP8 promotes smoothened signaling by preventing its ubiquitination and changing its subcellular localization. PLoS Biology 10:e1001238. PMID: 22253573; PMCID: PMC3254663; DOI: 10.1371/journal.pbio.1001238. https://pubmed.ncbi.nlm.nih.gov/22253573/


## Citations

1. ali-2013-ubpy-hdptp-abstract.md
2. ali-2013-ubpy-hdptp-summary.md
3. alwan-2007-ubpy-egfr-degradation-abstract.md
4. alwan-2007-ubpy-egfr-degradation-summary.md
5. avvakumov-2006-usp8-structure-abstract.md
6. avvakumov-2006-usp8-structure-summary.md
7. berlin-2010-usp8-cxcr4-abstract.md
8. berlin-2010-usp8-cxcr4-summary.md
9. crespo-2018-usp8-chmp1b-abstract.md
10. crespo-2018-usp8-chmp1b-fulltext.txt
11. crespo-2018-usp8-chmp1b-summary.md
12. dufner-2015-usp8-tcells-abstract.md
13. dufner-2015-usp8-tcells-summary.md
14. dufner-2019-usp8-review-abstract.md
15. dufner-2019-usp8-review-fulltext.txt
16. dufner-2019-usp8-review-summary.md
17. durcan-2014-usp8-parkin-abstract.md
18. durcan-2014-usp8-parkin-summary.md
19. endo-2024-usp8-endosomal-stress-abstract.md
20. endo-2024-usp8-endosomal-stress-fulltext.txt
21. endo-2024-usp8-endosomal-stress-summary.md
22. faesen-2011-usp-linkage-abstract.md
23. faesen-2011-usp-linkage-summary.md
24. gnesutta-2001-mouse-ubpy-rasgrf1-abstract.md
25. gnesutta-2001-mouse-ubpy-rasgrf1-summary.md
26. kato-2000-ubpy-stam-sh3-abstract.md
27. kato-2000-ubpy-stam-sh3-summary.md
28. ma-2015-usp8-cushing-abstract.md
29. ma-2015-usp8-cushing-fulltext.txt
30. ma-2015-usp8-cushing-summary.md
31. massardi-2025-cushing-animals-abstract.md
32. massardi-2025-cushing-animals-fulltext.txt
33. massardi-2025-cushing-animals-summary.md
34. miao-2024-usp8-endosome-maturation-abstract.md
35. miao-2024-usp8-endosome-maturation-fulltext.txt
36. miao-2024-usp8-endosome-maturation-summary.md
37. mizuno-2005-ubpy-egfr-endosomes-abstract.md
38. mizuno-2005-ubpy-egfr-endosomes-summary.md
39. mizuno-2006-ubpy-endosome-ubiquitination-abstract.md
40. mizuno-2006-ubpy-endosome-ubiquitination-summary.md
41. mizuno-2007-ubpy-14-3-3-abstract.md
42. mizuno-2007-ubpy-14-3-3-summary.md
43. mukai-2008-ubpy-cytokinesis-abstract.md
44. mukai-2008-ubpy-cytokinesis-summary.md
45. mukai-2010-ubpy-frizzled-abstract.md
46. mukai-2010-ubpy-frizzled-summary.md
47. naviglio-1998-ubpy-growth-abstract.md
48. naviglio-1998-ubpy-growth-summary.md
49. niendorf-2007-usp8-knockout-abstract.md
50. niendorf-2007-usp8-knockout-summary.md
51. reincke-2015-usp8-cushing-abstract.md
52. reincke-2015-usp8-cushing-summary.md
53. row-2006-ubpy-endosomal-ubiquitin-abstract.md
54. row-2006-ubpy-endosomal-ubiquitin-summary.md
55. row-2007-ubpy-mit-chmp-abstract.md
56. row-2007-ubpy-mit-chmp-summary.md
57. uniprot-2026-A0A9L0T7K6-entry-summary.md
58. uniprot-2026-A0A9L0T7K6-entry.txt
59. uniprot-2026-P40818-human-usp8-entry-summary.md
60. uniprot-2026-P40818-human-usp8-entry.txt
61. wade-2009-horse-genome-abstract.md
62. wade-2009-horse-genome-summary.md
63. wu-2004-usp8-nrdp1-abstract.md
64. wu-2004-usp8-nrdp1-summary.md
65. xia-2012-usp8-smoothened-abstract.md
66. xia-2012-usp8-smoothened-fulltext.txt
67. xia-2012-usp8-smoothened-summary.md