---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:53:34.346166'
end_time: '2026-10-26T01:02:47.709108'
duration_seconds: 553.36
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: RBM41
  gene_symbol: RBM41
  uniprot_accession: A0A9L0IK51
  protein_description: 'RecName: Full=RNA-binding protein 41 {ECO:0000256|ARBA:ARBA00067964};
    AltName: Full=RNA-binding motif protein 41 {ECO:0000256|ARBA:ARBA00075590};'
  gene_info: Name=RBM41 {ECO:0000313|Ensembl:ENSEASP00005041268.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Not specified in UniProt
  protein_domains: Nucleotide-bd_a/b_plait_sf. (IPR012677); RBD_domain_sf. (IPR035979);
    RBM41/RNPC3. (IPR045164); RRM_dom. (IPR000504); RRM_1 (PF00076)
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
citation_count: 55
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0IK51
- **Protein Description:** RecName: Full=RNA-binding protein 41 {ECO:0000256|ARBA:ARBA00067964}; AltName: Full=RNA-binding motif protein 41 {ECO:0000256|ARBA:ARBA00075590};
- **Gene Information:** Name=RBM41 {ECO:0000313|Ensembl:ENSEASP00005041268.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Nucleotide-bd_a/b_plait_sf. (IPR012677); RBD_domain_sf. (IPR035979); RBM41/RNPC3. (IPR045164); RRM_dom. (IPR000504); RRM_1 (PF00076)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "RBM41" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'RBM41' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **RBM41** (gene ID: RBM41, UniProt: A0A9L0IK51) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# RBM41 (RNA-binding motif protein 41) in the donkey, *Equus asinus* (UniProt A0A9L0IK51)

## Introduction and summary

RBM41 is a small, nuclear RNA-binding protein of the RBM41/RNPC3 family. Its best-supported job is as a protein component of the **minor (U12-dependent) spliceosome**, the machinery that removes the rare U12-type introns from pre-mRNA. The donkey protein, A0A9L0IK51, is a computationally predicted, unreviewed TrEMBL entry made from the donkey reference genome. Its only functional annotation is the generic statement "May bind RNA", plus electronically inferred Gene Ontology terms for the U12-type spliceosomal complex, U12 snRNA binding, pre-mRNA intronic binding and mRNA splicing via spliceosome [uniprot-A0A9L0IK51-entry; wang-2020-donkey-genomes-abstract]. No experimental study of donkey RBM41 exists, so this report infers its function from the human ortholog (Q96IZ5). The two proteins are nearly identical, so that inference is strong (see the identity section below).

The key experimental work on RBM41 is a 2024 study from the Frilander laboratory [norppa-2024-rbm41-65k-fulltext]. It showed that human RBM41 is a paralog of the U11/U12-65K protein (RNPC3). Its C-terminal RNA recognition motif (RRM) binds the 3′-terminal stem-loops of U12 snRNA and U6atac snRNA. In cells, RBM41 associates with U12, U4atac and U6atac snRNAs but not with U11 snRNA. Rather than joining the intron-recognising U11/U12 di-snRNP, RBM41 is part of a separate **U12 mono-snRNP** together with ZCRB1 (U11/U12-31K). Its conserved N-terminal region contacts the DEAH-box helicase DHX8, it binds excised U12-type intron lariats, and it is enriched in **Cajal bodies**. Together these results place RBM41 in the post-catalytic, disassembly and recycling steps of the minor spliceosome cycle [norppa-2024-rbm41-65k-fulltext]. RBM41 is not needed for cell viability. Knocking it out has a weak but statistically significant effect on 3′ splice site choice at a subset of U12-type introns [norppa-2024-rbm41-65k-fulltext].

RBM41 is not an enzyme, transporter or signalling molecule. It is best described as an RNA-binding adaptor or snRNP protein. Its "substrate" is a structured RNA: the 3′ stem-loop of U12 snRNA, and with somewhat lower affinity the 3′ stem-loop of U6atac snRNA. A separate, more recent cancer-biology report claims that RBM41 also binds a stem-loop in the NDRG1 3′ UTR and slows that pre-mRNA's maturation in colorectal cancer cells [rbm41-2026-colorectal-ndrg1-fulltext]. That claim comes from a single laboratory and is treated here as provisional.

## Identity verification and orthology

The gene symbol, protein name, organism and domain content in the UniProt record all agree. A0A9L0IK51 is annotated as "RNA-binding protein 41 / RNA-binding motif protein 41", with gene name RBM41 from the Ensembl donkey gene model ENSEASG00005025098, located on chromosome X [uniprot-A0A9L0IK51-entry]. The human gene is also on the X chromosome: the knockout study had to edit all three X copies in HEK293 cells [norppa-2024-rbm41-65k-fulltext]. Single-cell allelic expression data list human RBM41 among genes that probably escape X-inactivation, so it may be expressed at higher levels in females [wainer-2019-x-escape-fulltext]. Whether this holds in equids is unknown. The donkey protein carries the family signature IPR045164 (RBM41/RNPC3), sits in the PANTHER subfamily PTHR16105:SF2 ("RNA-binding protein 41"), and has a single PROSITE RRM at residues 333–411 [uniprot-A0A9L0IK51-entry]. Human RBM41 (413 residues) likewise has a single annotated RRM near its C-terminus at positions 309–387 [norppa-2024-rbm41-65k-fulltext].

To confirm orthology, I made a global alignment of the donkey (432 aa) and human (413 aa) sequences (BLOSUM62). Of 408 aligned positions, 391 are identical, which is about 95% of the human protein length. The main difference is a 24-residue segment in the donkey model (residues 174–197, around the sequence QAYHKKTSADKYMTSMKRKIKLGT) that is missing from the human canonical isoform. It may represent an alternatively included exon or a gene-model artefact. Human UniProt records three splice isoforms of RBM41 [uniprot-Q96IZ5-human-RBM41-entry]. The RRM residues shown to be needed for snRNA binding in human cells (Tyr312, Gln352 and Phe354) correspond exactly to Tyr336, Gln376 and Phe378 in the donkey protein [uniprot-A0A9L0IK51-summary; norppa-2024-rbm41-65k-fulltext]. I found no literature on a different gene sharing the RBM41 symbol, so there is no ambiguity in what the symbol refers to.

## Domain architecture and evolutionary relationship to U11/U12-65K

RBM41 has two parts: a long N-terminal region with no recognised domains, and a C-terminal RRM. In human RBM41, the N-terminal region (about residues 1–258) is highly conserved among animal orthologs and is predicted by AlphaFold to be mostly helical. It shares no sequence similarity with the N-terminus of its paralog, U11/U12-65K [norppa-2024-rbm41-65k-fulltext]. The similarity between the two proteins is confined to the C-terminal RRM and an N-terminal extension of that RRM [norppa-2024-rbm41-65k-fulltext]. In 65K, this extension is a non-canonical helix that stabilises the RRM and is needed for U12 snRNA binding [netter-2009-65k-rrm-expansion-abstract]. Because RBM41 conserves it, the same structural solution probably supports RBM41's RNA binding. An NMR structure of the RBM41 RRM was deposited by a structural genomics consortium (PDB 2CPX), and the 65K C-terminal RRM structure is 5OBN [norppa-2024-rbm41-65k-fulltext; norppa-2018-65k-ighd-abstract]. The donkey sequence also has a short disordered, polar-rich region (residues 248–267) just before the RRM [uniprot-A0A9L0IK51-entry].

The paralog 65K is a well-defined bridge. Its N-terminal region binds the U11-59K protein (PDCD7), and its C-terminal RRM binds the U12 snRNA 3′ terminal stem-loop, so it holds the U11 and U12 snRNPs together in the di-snRNP [benecke-2005-65k-bridge-abstract]. Missense mutations in the 65K C-terminal RRM that cause isolated growth hormone deficiency destabilise the domain and weaken U12 snRNA binding [norppa-2018-65k-ighd-abstract]. RBM41 shares the RNA-binding half of this arrangement but has replaced the U11-binding half with an unrelated module.

Evolutionary analysis supports a minor-spliceosome role. Across 167 eukaryotic proteomes, the presence or absence of RBM41 tracks that of minor-spliceosome-specific proteins, with CENATAC, U11-48K (SNRNP48) and U11/U12-31K (ZCRB1) among the strongest co-occurring proteins. However, RBM41 is lost more often than several other minor-spliceosome components [norppa-2024-rbm41-65k-fulltext]. An independent phylogenomic reconstruction of the spliceosome of the last eukaryotic common ancestor reached the same conclusion before RBM41 had been tested biochemically. In that reconstruction, RBM41 was the sister paralog of RNPC3 in the RRM tree. Its presence/absence pattern matched those of minor-spliceosome orthologous groups, a pattern first described in the phylogenetic-profiling work that identified CENATAC [vosseberg-2023-spliceosome-origin-fulltext; dewolf-2021-cenatac-abstract]. The authors noted that if RBM41 belonged to the minor spliceosome, the RNPC3–RBM41 split would be the only gene duplication inside the minor-spliceosome-specific protein set. They also found an RBM41 ortholog in the lycophyte *Selaginella moellendorffii*, which shows the paralog pair is ancient and not a vertebrate innovation [vosseberg-2023-spliceosome-origin-fulltext]. The family looks different in insects. *Drosophila* CG44249 ("Miso") has a single C-terminal RRM and is 31% identical to human RNPC3 and 27% identical to RBM41. Miso binds both U11 and U12 snRNAs and is needed for minor-intron splicing in the ovary, so it behaves more like 65K than like RBM41 [miso-2025-drosophila-minor-splicing-fulltext]. In mammals, including equids, the two paralogs coexist and have split their roles.

## Molecular function: RNA binding to the U12 and U6atac 3′ stem-loops

The molecular function of RBM41 is sequence- and structure-specific RNA binding. Two independent high-throughput in vitro studies, RNAcompete [ray-2013-rnacompete-abstract] and RNA Bind-n-Seq [dominguez-2018-rbns-abstract], produced nearly identical RBM41 consensus motifs that sit preferentially in the loop of a stem-loop. Norppa and colleagues noticed that these motifs closely match the loop sequences of the U12 and U6atac snRNA 3′-terminal stem-loops [norppa-2024-rbm41-65k-fulltext]. Their electrophoretic mobility-shift assays confirmed that a recombinant RBM41 RRM fragment (residues 267–413) binds U12 and U6atac hairpins but not a control hairpin. The measured affinities were Kd ≈ 2.14 µM for the U12 hairpin and ≈ 3.78 µM for U6atac. The 65K C-terminal RRM bound the same RNAs about twofold more tightly (1.04 µM and 2.07 µM) [norppa-2024-rbm41-65k-fulltext].

In cells, RNA immunoprecipitation of tagged or endogenous RBM41 recovered U12, U4atac and U6atac snRNAs but not U11 snRNA. Under the same conditions, 65K strongly recovered both U11 and U12 [norppa-2024-rbm41-65k-fulltext]. These snRNA interactions depended on the RRM. Alanine substitutions at Gln352 or Phe354 of the conserved RNP "YQF" triad, or deletion of the RRM, abolished them, whereas the isolated C-terminal fragment (259–413) was enough to bind [norppa-2024-rbm41-65k-fulltext]. Because the U12 3′ stem-loop is also needed for U12 snRNA stability, and a disease-linked mutation that disrupts it (84C>U, which causes early-onset cerebellar ataxia [elsaid-2017-rnu12-ataxia-abstract]) causes overtrimming that removes the 65K/RBM41 binding site, this RNA element is a functionally important binding platform [norppa-2021-u12-stem-loop-abstract; norppa-2024-rbm41-65k-fulltext]. All of the RRM residues involved are conserved in the donkey protein, so donkey RBM41 is expected to bind RNA with the same specificity.

## Complex membership and place in the minor spliceosome cycle

The central conclusion of the human work is that RBM41 and 65K bind the same RNA element but act at different stages. In glycerol gradients of HeLa nuclear extract, RBM41 sedimented with a U12 mono-snRNP, together with U11/U12-31K (ZCRB1), and separately from the 65K-containing U11/U12 di-snRNP [norppa-2024-rbm41-65k-fulltext]. In BioID proximity labelling, 65K labelled all eight di-snRNP-specific proteins (top hits PDCD7, ZMAT5, SNRNP48 and SNRNP35). RBM41 labelled only ZCRB1 from that set, and this interaction required RBM41 to bind U12 snRNA [norppa-2024-rbm41-65k-fulltext]. A 2025 review of minor spliceosome diseases now describes this U12 mono-snRNP, containing RBM41 and ZCRB1, as the only characterised post-catalytic minor spliceosome subcomplex, and as a likely product of spliceosome disassembly [genotype-2025-minor-spliceosome-diseases-fulltext].

The N-terminal region of RBM41 connects it to the late stages of splicing. One of RBM41's top BioID partners was DHX8, the DEAH-box helicase that releases mature mRNA from the major spliceosome. This interaction required the conserved N-terminus and not the RRM, and was confirmed by co-immunoprecipitation [norppa-2024-rbm41-65k-fulltext]. The yeast ortholog of DHX8, Prp22, was first shown to be needed to release spliced mRNA from the spliceosome after exon ligation [company-1991-prp22-abstract]. The RBM41–DHX8 link therefore points to the mRNA-release and intron-lariat stages. RBM41, whether tagged or endogenous, preferentially co-precipitated excised U12-type intron lariats but not U2-type lariats. A helicase-dead DHX8 (K594A) trapped lariats of both intron types, which suggests DHX8 also acts in the minor spliceosome [norppa-2024-rbm41-65k-fulltext]. RBM41 is not visible in the cryo-EM structures of earlier minor spliceosome complexes, namely the activated Bact complex and the fully assembled pre-B complex, in which the U12 snRNP is engaged through 65K [bai-2021-activated-minor-spliceosome-abstract; bai-2024-minor-spliceosome-u12-intron-abstract]. This fits a stage-specific role.

The authors' model is that 65K holds the U12 3′ stem-loop through intron recognition, assembly and activation. It is then exchanged for RBM41 during or after the catalytic steps. RBM41 stays on the post-spliceosomal U12 mono-snRNP and travels with it to Cajal bodies, where the U11/U12 di-snRNP is presumably rebuilt [norppa-2024-rbm41-65k-fulltext]. This fits the general view of Cajal bodies as sites where snRNPs are assembled, matured and regenerated after splicing [stanek-2016-cajal-bodies-abstract]. ZCRB1, RBM41's partner in the mono-snRNP, has itself turned out to matter biologically. Partial loss of ZCRB1 causes mis-splicing of minor introns, defective ciliogenesis and increased WNT signalling in human cells and zebrafish, which shows that this snRNP has physiological consequences [zcrb1-2026-ciliogenesis-abstract; zcrb1-2026-ciliogenesis-fulltext]. The 3′ stem-loop of U12 therefore acts as a dynamic docking site that is handed between paralogous proteins over the splicing cycle. Exactly when the exchange happens is still uncertain. The bias towards alternative 3′ splice sites in knockout cells might indicate an exchange before the second catalytic step, but the proximity data did not support that interpretation [norppa-2024-rbm41-65k-fulltext].

## Subcellular localisation

All direct evidence places RBM41 in the nucleus. Endogenous human RBM41 accumulates in Cajal bodies, where it colocalises with coilin-GFP in HEK293 cells, and coilin was a major BioID partner of RBM41 [norppa-2024-rbm41-65k-fulltext]. Localisation to nuclear bodies required an intact RRM. RRM point mutants and the RRM-deletion construct did not form nuclear foci, which suggests that RBM41 is recruited to Cajal bodies as part of its snRNP and not independently [norppa-2024-rbm41-65k-fulltext]. The RBM41-positive nuclear bodies did not colocalise with endogenous 65K, consistent with 65K visiting Cajal bodies only transiently [norppa-2024-rbm41-65k-fulltext]. An independent study in HT29 colorectal cancer cells also found RBM41 mainly in the nucleus [rbm41-2026-colorectal-ndrg1-fulltext]. The Human Protein Atlas, using high-throughput antibody imaging of cell lines, classifies RBM41 as localised to nuclear speckles and the cytosol and as broadly expressed across tissues with low tissue specificity [hpa-RBM41-record]. Nuclear speckles store splicing factors, so a speckle signal is not inconsistent with a splicing role. The Cajal body result from the targeted study, which checked that the signal depended on the RRM, is the more specific evidence. Any cytosolic pool has no assigned function and may reflect antibody or cell-line effects. Overall, RBM41 is expected to act in the nucleoplasm, within spliceosomal and post-spliceosomal snRNP complexes and in Cajal bodies. The GO cellular component term "U12-type spliceosomal complex" on the donkey entry is consistent with this [uniprot-A0A9L0IK51-entry].

## Biological roles, phenotypes and a proposed non-spliceosomal function

Loss of RBM41 is tolerated at the cellular level. RBM41-null HEK293 lines were viable and grew normally, which matches genome-wide essentiality screens in haploid human cells [norppa-2024-rbm41-65k-fulltext; blomen-2015-gene-essentiality-abstract]. RNA-seq of three knockout lines found only modest changes. A small number of U12-type introns showed increased or decreased retention (for example NOL11). Of 37 significant alternative splicing events in U12-intron-containing genes, alternative 3′ splice site use was enriched about threefold, and most of these events changed the choice of 3′ splice site at U12-type introns [norppa-2024-rbm41-65k-fulltext]. The authors suggest that RBM41 may have a weak kinetic effect on minor splicing and a larger role in disassembly, and that its conservation may reflect advantages in particular cell types or whole organisms [norppa-2024-rbm41-65k-fulltext]. They also mention earlier evidence that RBM41 translation is regulated through alternative 3′ UTR isoforms during neuronal development [norppa-2024-rbm41-65k-fulltext].

A 2026 study in colorectal cancer proposes a different, gene-specific function [rbm41-2026-colorectal-ndrg1-fulltext]. It reports that RBM41 is overexpressed in colorectal tumours and that knocking it down reduces proliferation and triggers apoptosis and stalled autophagic flux. Mechanistically, the authors used RIP-qPCR and RNA pull-downs to conclude that nuclear RBM41 binds a GCAAUGA-containing stem-loop in the NDRG1 3′ UTR and impairs processing of the NDRG1 pre-mRNA, which lowers levels of this tumour suppressor [rbm41-2026-colorectal-ndrg1-fulltext]. A correction to the article has been published [rbm41-2026-colorectal-ndrg1-correction-abstract]. The finding is compatible with RBM41's preference for loops in stem-loops, but it has not been independently replicated, does not use transcriptome-wide binding data such as CLIP, and does not test any link to the minor spliceosome. It should therefore be treated as a hypothesis, not a core function. None of these phenotypic data come from equids. Curated interaction databases also list many binary interactions for human RBM41, mostly from high-throughput yeast two-hybrid screens. Examples include coiled-coil proteins such as GOLGA2, TRAF2 and RINT1, the RNA-binding proteins HNRNPC and RALYL, and the SARS-CoV-2 nsp13 helicase [uniprot-Q96IZ5-human-RBM41-entry]. None has been validated in a functional study, so they are not used for annotation here.

## Synthesis for functional annotation of donkey RBM41

Based on the near-identity of the donkey and human proteins and the conservation of every residue shown to matter, donkey A0A9L0IK51 can be annotated with reasonable confidence as follows. It is a U12 snRNA-binding protein (molecular function: U12 snRNA binding and, with lower affinity, U6atac snRNA binding, through its C-terminal RRM). It is a component of the minor (U12-type) spliceosome and of the post-spliceosomal U12 mono-snRNP (cellular component: U12-type spliceosomal complex, nucleus and Cajal body). It acts in mRNA splicing via the minor spliceosome, mainly in the post-catalytic disassembly and snRNP recycling steps, with a minor effect on U12-type 3′ splice site selection [norppa-2024-rbm41-65k-fulltext; genotype-2025-minor-spliceosome-diseases-fulltext]. The electronic GO term "pre-mRNA intronic binding" on the donkey entry fits the association with excised U12-type intron lariats, although direct binding of RBM41 to intron RNA, as opposed to binding through the snRNP, has not been shown [uniprot-A0A9L0IK51-entry; norppa-2024-rbm41-65k-fulltext].

## Open Questions

Several questions remain open, and following them up would sharpen the annotation. First, the exact point at which 65K is exchanged for RBM41 on the U12 3′ stem-loop is unknown. Cryo-EM structures of post-catalytic minor spliceosome complexes (C*, P and ILS stages) and of the isolated U12 mono-snRNP would show whether RBM41 binds the spliceosome before exon ligation or only after release, and how its N-terminal helical region contacts DHX8. Second, it is not clear whether the RBM41–DHX8 interaction is direct, and whether RBM41 actively promotes mRNA release or lariat-spliceosome disassembly or only marks the recycled U12 snRNP. In vitro reconstitution or acute degron depletion, rather than stable knockout, would help. Third, the organismal role is untested. No knockout of an RBM41 ortholog in a vertebrate has been described in the sources reviewed here, and since RBM41 is X-linked in both human and donkey, sex-specific or tissue-specific phenotypes (for example in neurons, given its 3′ UTR-regulated translation) are worth examining. Fourth, the donkey gene model contains a 24-residue segment absent from human canonical RBM41. Whether this is a real equid-specific exon, an alternatively spliced isoform, or an annotation artefact should be checked against donkey RNA-seq. Finally, the proposed NDRG1 3′ UTR binding and pro-tumorigenic role in colorectal cancer needs independent replication, transcriptome-wide CLIP data, and a test of whether the effect is direct or a consequence of altered minor splicing. The Human Protein Atlas places RBM41 in nuclear speckles and the cytosol, while the targeted study found it in Cajal bodies. Colocalisation with markers of both structures across cell types, and in equine cells, would clarify where it resides. Probable escape from X-inactivation also raises the question of whether RBM41 dosage differs between the sexes. A general question also remains about how RBM41's in vitro preference for stem-loop motifs separates snRNA targets from possible mRNA targets in the cell.

## References

- **[norppa-2024-rbm41-65k]** Norppa AJ, Chowdhury I, van Rooijen LE, Ravantti JJ, Snel B, et al. (Frilander MJ, corresponding). "Distinct functions for the paralogous RBM41 and U11/U12-65K proteins in the minor spliceosome." *Nucleic Acids Research* 2024 Apr 24. PMID: 38499487; PMCID: PMC11039992; DOI: 10.1093/nar/gkae070. https://doi.org/10.1093/nar/gkae070 (files: `citations/norppa-2024-rbm41-65k-fulltext.txt`, `-abstract.md`, `-summary.md`)
- **[genotype-2025-minor-spliceosome-diseases]** Norppa AJ, Shcherbii MV, Frilander MJ. "Connecting genotype and phenotype in minor spliceosome diseases." *RNA* 2025;31(3):284–299. PMID: 39761998; PMCID: PMC11874965; DOI: 10.1261/rna.080337.124.
- **[miso-2025-drosophila-minor-splicing]** Taira Y, Zhu L, Fukunaga R. "RNA-binding protein Miso/CG44249 is crucial for minor splicing during oogenesis in Drosophila." *RNA* 2025 May 16. PMID: 40169226; PMCID: PMC12084885; DOI: 10.1261/rna.080311.124.
- **[rbm41-2026-colorectal-ndrg1]** Liu Y, et al. "RNA binding motif protein RBM41 promotes colorectal tumorigenesis by impeding the maturation of NDRG1 pre-mRNA." *Cell Death Discovery* 2026;12(1):276. PMID: 42323368; PMCID: PMC13283208; DOI: 10.1038/s41420-026-03197-6.
- **[rbm41-2026-colorectal-ndrg1-correction]** "Correction: RNA binding motif protein RBM41 promotes colorectal tumorigenesis by impeding the maturation of NDRG1 pre-mRNA." *Cell Death Discovery* 2026. PMID: 42869877; PMCID: PMC13661604; DOI: 10.1038/s41420-026-03341-2.
- **[benecke-2005-65k-bridge]** Benecke H, Lührmann R, Will CL. "The U11/U12 snRNP 65K protein acts as a molecular bridge, binding the U12 snRNA and U11-59K protein." *EMBO Journal* 2005 Sep 7. PMID: 16096647; PMCID: PMC1201347; DOI: 10.1038/sj.emboj.7600765.
- **[norppa-2018-65k-ighd]** Norppa AJ, Kauppala TM, Heikkinen HA, Verma B, Iwaï H, et al. "Mutations in the U11/U12-65K protein associated with isolated growth hormone deficiency lead to structural destabilization and impaired binding of U12 snRNA." *RNA* 2018 Mar. PMID: 29255062; PMCID: PMC5824358; DOI: 10.1261/rna.062844.117.
- **[norppa-2021-u12-stem-loop]** Norppa AJ, Frilander MJ. "The integrity of the U12 snRNA 3' stem-loop is necessary for its overall stability." *Nucleic Acids Research* 2021;49(5):2835–2847. PMID: 33577674; DOI: 10.1093/nar/gkab048.
- **[ray-2013-rnacompete]** Ray D, et al. "A compendium of RNA-binding motifs for decoding gene regulation." *Nature* 2013 Jul 11. PMID: 23846655.
- **[dominguez-2018-rbns]** Dominguez D, et al. "Sequence, Structure, and Context Preferences of Human RNA Binding Proteins." *Molecular Cell* 2018 Jun 7. PMID: 29883606.
- **[bai-2021-activated-minor-spliceosome]** Bai R, Wan R, Wang L, Xu K, Zhang Q, Lei J, Shi Y. "Structure of the activated human minor spliceosome." *Science* 2021 Mar 19. PMID: 33509932.
- **[bai-2024-minor-spliceosome-u12-intron]** Bai R, Yuan M, Zhang P, Luo T, Shi Y, Wan R. "Structural basis of U12-type intron engagement by the fully assembled human minor spliceosome." *Science* 2024;383(6688):1245–1252. PMID: 38484052; DOI: 10.1126/science.adn7272.
- **[wang-2020-donkey-genomes]** Wang C, et al. "Donkey genomes provide new insights into domestication and selection for coat color." *Nature Communications* 2020;11:6014. PMID: 33293529.
- **[uniprot-A0A9L0IK51]** UniProtKB A0A9L0IK51 (A0A9L0IK51_EQUAS), RNA-binding protein 41, *Equus asinus*; entry version 12 (10-JUN-2026). https://rest.uniprot.org/uniprotkb/A0A9L0IK51.txt (file: `citations/uniprot-A0A9L0IK51-entry.txt`)
- **[uniprot-Q96IZ5]** UniProtKB Q96IZ5 (RBM41_HUMAN), RNA-binding protein 41, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/Q96IZ5.txt (file: `citations/uniprot-Q96IZ5-human-RBM41-entry.txt`)
- **[vosseberg-2023-spliceosome-origin]** Vosseberg J, Stolker D, von der Dunk SHA, Snel B. "Integrating Phylogenetics With Intron Positions Illuminates the Origin of the Complex Spliceosome." *Molecular Biology and Evolution* 2023;40(1):msad011. PMID: 36631250; PMCID: PMC9887622; DOI: 10.1093/molbev/msad011.
- **[dewolf-2021-cenatac]** de Wolf B, Oghabian A, Akinyi MV, Hanks S, Tromer EC, van Hooff JJE, et al. (Snel B, Frilander MJ, Kops GJPL). "Chromosomal instability by mutations in the novel minor spliceosome component CENATAC." *EMBO Journal* 2021;40(14):e106536. PMID: 34009673; PMCID: PMC8280824; DOI: 10.15252/embj.2020106536.
- **[netter-2009-65k-rrm-expansion]** Netter C, Weber G, Benecke H, Wahl MC. "Functional stabilization of an RNA recognition motif by a noncanonical N-terminal expansion." *RNA* 2009;15(7):1305–1313. PMID: 19447915; PMCID: PMC2704084; DOI: 10.1261/rna.1359909.
- **[company-1991-prp22]** Company M, Arenas J, Abelson J. "Requirement of the RNA helicase-like protein PRP22 for release of messenger RNA from spliceosomes." *Nature* 1991;349(6309):487–493. PMID: 1992352; DOI: 10.1038/349487a0.
- **[stanek-2016-cajal-bodies]** Staněk D. "Cajal bodies and snRNPs - friends with benefits." *RNA Biology* 2017;14(6):671–679. PMID: 27627834; PMCID: PMC5519240; DOI: 10.1080/15476286.2016.1231359.
- **[zcrb1-2026-ciliogenesis]** Pirzada MUR, Powell-Rodgers G, Richee J, Norppa AJ, et al. "Loss of U11/U12 spliceosome gene ZCRB1 leads to aberrant ciliogenesis and WNT signaling." *Life Science Alliance* 2026;9(8):e202503607. PMID: 42203510; PMCID: PMC13216214; DOI: 10.26508/lsa.202503607.
- **[elsaid-2017-rnu12-ataxia]** Elsaid MF, Chalhoub N, Ben-Omran T, Kumar P, Kamel H, Ibrahim K, et al. "Mutation in noncoding RNA RNU12 causes early onset cerebellar ataxia." *Annals of Neurology* 2017;81(1):68–78. PMID: 27863452; DOI: 10.1002/ana.24826.
- **[blomen-2015-gene-essentiality]** Blomen VA, Májek P, Jae LT, Bigenzahn JW, Nieuwenhuis J, et al. (Brummelkamp TR). "Gene essentiality and synthetic lethality in haploid human cells." *Science* 2015;350(6264):1092–1096. PMID: 26472760; DOI: 10.1126/science.aac7557.
- **[wainer-2019-x-escape]** Wainer Katsir K, Linial M. "Human genes escaping X-inactivation revealed by single cell expression data." *BMC Genomics* 2019;20(1):201. PMID: 30871455; PMCID: PMC6419355; DOI: 10.1186/s12864-019-5507-6.
- **[hpa-RBM41-record]** Human Protein Atlas, RBM41 (ENSG00000089682), retrieved via https://www.proteinatlas.org/api/search_download.php?search=RBM41 (file: `citations/hpa-RBM41-record.json`).


## Citations

1. bai-2021-activated-minor-spliceosome-abstract.md
2. bai-2021-activated-minor-spliceosome-summary.md
3. bai-2024-minor-spliceosome-u12-intron-abstract.md
4. bai-2024-minor-spliceosome-u12-intron-summary.md
5. benecke-2005-65k-bridge-abstract.md
6. benecke-2005-65k-bridge-summary.md
7. blomen-2015-gene-essentiality-abstract.md
8. blomen-2015-gene-essentiality-summary.md
9. company-1991-prp22-abstract.md
10. company-1991-prp22-summary.md
11. dewolf-2021-cenatac-abstract.md
12. dewolf-2021-cenatac-summary.md
13. dominguez-2018-rbns-abstract.md
14. dominguez-2018-rbns-summary.md
15. elsaid-2017-rnu12-ataxia-abstract.md
16. elsaid-2017-rnu12-ataxia-summary.md
17. genotype-2025-minor-spliceosome-diseases-abstract.md
18. genotype-2025-minor-spliceosome-diseases-fulltext.txt
19. genotype-2025-minor-spliceosome-diseases-summary.md
20. hpa-RBM41-record.json
21. hpa-RBM41-summary.md
22. miso-2025-drosophila-minor-splicing-abstract.md
23. miso-2025-drosophila-minor-splicing-fulltext.txt
24. miso-2025-drosophila-minor-splicing-summary.md
25. netter-2009-65k-rrm-expansion-abstract.md
26. netter-2009-65k-rrm-expansion-summary.md
27. norppa-2018-65k-ighd-abstract.md
28. norppa-2018-65k-ighd-summary.md
29. norppa-2021-u12-stem-loop-abstract.md
30. norppa-2021-u12-stem-loop-summary.md
31. norppa-2024-rbm41-65k-abstract.md
32. norppa-2024-rbm41-65k-fulltext.txt
33. norppa-2024-rbm41-65k-summary.md
34. ray-2013-rnacompete-abstract.md
35. ray-2013-rnacompete-summary.md
36. rbm41-2026-colorectal-ndrg1-abstract.md
37. rbm41-2026-colorectal-ndrg1-correction-abstract.md
38. rbm41-2026-colorectal-ndrg1-fulltext.txt
39. rbm41-2026-colorectal-ndrg1-summary.md
40. stanek-2016-cajal-bodies-abstract.md
41. stanek-2016-cajal-bodies-summary.md
42. uniprot-A0A9L0IK51-entry.txt
43. uniprot-A0A9L0IK51-summary.md
44. uniprot-Q96IZ5-human-RBM41-entry.txt
45. vosseberg-2023-spliceosome-origin-abstract.md
46. vosseberg-2023-spliceosome-origin-fulltext.txt
47. vosseberg-2023-spliceosome-origin-summary.md
48. wainer-2019-x-escape-abstract.md
49. wainer-2019-x-escape-fulltext.txt
50. wainer-2019-x-escape-summary.md
51. wang-2020-donkey-genomes-abstract.md
52. wang-2020-donkey-genomes-summary.md
53. zcrb1-2026-ciliogenesis-abstract.md
54. zcrb1-2026-ciliogenesis-fulltext.txt
55. zcrb1-2026-ciliogenesis-summary.md