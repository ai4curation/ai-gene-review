---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:52:11.880442'
end_time: '2026-10-26T04:11:05.420660'
duration_seconds: 1133.54
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: ZDHHC23
  gene_symbol: ZDHHC23
  uniprot_accession: A0A9L0T4E4
  protein_description: 'RecName: Full=Palmitoyltransferase {ECO:0000256|RuleBase:RU079119};
    EC=2.3.1.225 {ECO:0000256|RuleBase:RU079119};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the DHHC palmitoyltransferase family.
  protein_domains: Palmitoyltrfase_DHHC. (IPR001594); PFA4/ZDH16/20/ERF2-like. (IPR039859);
    DHHC (PF01529)
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
citation_count: 91
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0T4E4
- **Protein Description:** RecName: Full=Palmitoyltransferase {ECO:0000256|RuleBase:RU079119}; EC=2.3.1.225 {ECO:0000256|RuleBase:RU079119};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the DHHC palmitoyltransferase family.
- **Key Domains:** Palmitoyltrfase_DHHC. (IPR001594); PFA4/ZDH16/20/ERF2-like. (IPR039859); DHHC (PF01529)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ZDHHC23" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ZDHHC23' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ZDHHC23** (gene ID: ZDHHC23, UniProt: A0A9L0T4E4) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ZDHHC23 (UniProt A0A9L0T4E4) in the Horse: A Golgi-Resident DHHC Protein S-Palmitoyltransferase

## 1. Introduction and Summary

The horse protein A0A9L0T4E4 is an unreviewed, automatically annotated TrEMBL entry described only as "Palmitoyltransferase" (EC 2.3.1.225). It was predicted from the Thoroughbred reference genome and has no gene name in UniProt. It is assigned to the DHHC palmitoyltransferase family, carries the DHHC (PF01529) and PFA4/ZDH16/20/ERF2-like (IPR039859) signatures, and falls in the PANTHER subfamily PTHR22883:SF475, "Palmitoyltransferase ZDHHC23" [uniprot-A0A9L0T4E4-entry; wade-2009-horse-genome-abstract]. Ensembl places it at horse chromosome 19 as the canonical product of gene ENSECAG00000014382, which carries the VGNC-approved symbol ZDHHC23 [ensembl-ENSECAG00000014382-entry]. This confirms that the gene symbol "ZDHHC23" matches the protein described in the task. Our own pairwise alignment shows about 92% identity with human ZDHHC23 (Q8IYP9) over the aligned region, with the DHHC cysteine-rich domain and all transmembrane segments essentially invariant ([notes/sequence_analysis.md]; [uniprot-Q8IYP9-entry]). The symbol is therefore not ambiguous here. Nothing in the literature describes experiments on the horse protein itself, so every functional statement below is inferred by orthology from human, mouse and rat ZDHHC23 (rat ZDHHC23 was originally named NIDD) and from the general enzymology of the DHHC family.

In summary, ZDHHC23 is a polytopic integral membrane enzyme of the Golgi and trans-Golgi network (TGN). It transfers a palmitoyl (C16:0) group from palmitoyl-CoA onto cysteine thiols of protein substrates, forming a thioester (S-palmitoylation/S-acylation), via an autoacylated intermediate on the cysteine of its DHHC motif [uniprot-Q8IYP9-entry; rana-2018-dhhc-structure-abstract]. Its best-supported substrate is the pore-forming α-subunit of the large-conductance Ca²⁺- and voltage-activated K⁺ (BK, KCNMA1) channel. Here ZDHHC23 and ZDHHC22 together are the only enzymes that palmitoylate a cysteine cluster in the intracellular S0–S1 loop, which controls exit of the channel from the TGN and its coupling to β1 subunits. This has been shown by siRNA screens in cells and by a Zdhhc23 knockout mouse [tian-2012-acyl-transferases-bk-fulltext; duncan-2019-bk-beta1-sacylation-fulltext]. A second, older line of work identified rodent ZDHHC23 as NIDD, a PDZ-ligand-bearing protein that binds neuronal nitric oxide synthase (nNOS/NOS1), targets it to the synaptic membrane and increases its activity [saitoh-2004-nidd-nnos-abstract]. Newer reports name further substrates, mostly from cancer, pain and metabolic-disease models: GFAP, the demethylase PHF2, TDP-43, NAT10 and T-bet [fan-2024-gfap-zdhhc23-pain-fulltext; jeong-2023-phf2-hcc-srebp1c-fulltext; xu-2026-tdp43-sacylation-abstract; wang-2026-nat10-exosomal-mash-abstract; xin-2025-tbet-methionine-gastric-abstract]. These have less mechanistic support. Cell-based chemoproteomics shows that ZDHHC23 forms autoacylated intermediates with monounsaturated C18 fatty acids as well as palmitate, so its acyl-donor specificity is broader than the C16:0 reaction in the database annotation [wu-2026-chemoproteomics-isomer-sacylation-fulltext]. The subfamily is ancient. Its Drosophila member, GABPI, has lost the catalytic cysteine and works as a Golgi-targeting "pilot" for a glycosyltransferase. This raises the possibility that vertebrate ZDHHC23 has, or once had, roles that do not depend on catalysis [johswich-2009-drosophila-dhhc-pilot-fulltext; uniprot-Q9VQK9-entry; notes/sequence_analysis.md].

## 2. Gene Identity, Structure and Isoforms in the Horse

The horse ZDHHC23 gene spans about 12.5 kb on the reverse strand of chromosome 19 and is annotated with seven protein-coding transcripts that encode 397–448 residues [ensembl-ENSECAG00000014382-entry]. UniProt A0A9L0T4E4 is the 448-residue product of the Ensembl canonical transcript ZDHHC23-201 [uniprot-A0A9L0T4E4-entry]. Compared with human ZDHHC23 (409 residues), it lacks six N-terminal residues. It is nearly identical through the cytoplasmic N-terminal region, the four transmembrane helices before the DHHC domain, the DHHC cysteine-rich domain and the three helices after it ([notes/sequence_analysis.md]; [uniprot-Q8IYP9-entry]). The sequence around the catalytic motif (…CAKCQLVRPARAWHCRICGICVRRMDHHCVWINSCVGESNHQAF…) is identical in horse, human, mouse and rat. In the horse protein the DHHC tetrapeptide sits at residues 280–283, which places the catalytic cysteine at Cys283. This corresponds to human Cys289, annotated as the S-palmitoyl-cysteine intermediate [notes/sequence_analysis.md; uniprot-Q8IYP9-entry].

The orthologs differ only at the extreme C-terminus, after the conserved sequence "…RRLLCGLIVDT". Rat NIDD/Zdhhc23 and mouse Zdhhc23 end in a tail terminating in –PAEDIV [uniprot-Q76IC6-entry; notes/sequence_analysis.md]. This –EDIV motif is the PDZ-binding motif that Saitoh and colleagues showed is needed to bind the nNOS PDZ domain [saitoh-2004-nidd-nnos-abstract]. The canonical horse isoform A0A9L0T4E4 replaces this tail with an unrelated 45-residue extension and therefore lacks the PDZ ligand. The canonical human isoform also lacks it, ending in "GLLG". However, the horse Ensembl isoform ENSECAP00000025325 (435 residues) ends in –HPAEDIV and so keeps the rodent-type PDZ ligand ([ensembl-ENSECAG00000014382-entry]; [notes/sequence_analysis.md]). The pattern suggests alternative 3′ exon usage in the horse. The enzymatic core is common to all isoforms, but the ability to bind PDZ proteins such as nNOS probably depends on which isoform is expressed. This matters when the UniProt entry is used for functional annotation. Catalytic and Golgi-localization annotations transfer well to A0A9L0T4E4. A direct nNOS-binding annotation is better attached to the EDIV-containing isoform.

## 3. Catalytic Mechanism and Domain Architecture

DHHC proteins were established as the mammalian protein acyltransferases when Fukata and colleagues cloned 23 mammalian DHHC genes and showed that different subsets palmitoylate PSD-95 and other substrates selectively [fukata-2004-psd95-palmitoylating-abstract]. Crystal structures of human DHHC20 and zebrafish DHHC15 established the shared catalytic logic, which applies to ZDHHC23. The active site sits at the membrane–cytosol interface. The enzyme takes up palmitoyl-CoA, first forms a covalent acyl-enzyme intermediate on the DHHC cysteine, and then transfers the acyl chain to a substrate cysteine by thioester exchange. The fatty-acyl chain is buried in a cavity formed by the transmembrane helices, and the dimensions of this cavity set the preferred acyl chain length [rana-2018-dhhc-structure-abstract; rana-2019-dhhc-mechanism-review-abstract]. Because the active site is close to the membrane, membrane-proximal cysteines in substrates are favoured [rana-2018-dhhc-structure-abstract]. This fits the ZDHHC23 target cysteines in the BK channel S0–S1 loop, which lies just after the first transmembrane segment of that channel [tian-2012-acyl-transferases-bk-fulltext]. Work in yeast showed that the reaction can be split into substrate binding, which does not need the DHHC cysteine, and DHHC-dependent acylation [hou-2009-dhhc-overlapping-specificity-abstract]. This explains why catalytically dead DHHC proteins can still bind substrates. Consistent with these principles, the catalytic activity assigned to A0A9L0T4E4 (Rhea:36683; L-cysteinyl-[protein] + hexadecanoyl-CoA → S-hexadecanoyl-L-cysteinyl-[protein] + CoA) is inferred from the family rule. For human ZDHHC23 this activity has direct experimental support [uniprot-A0A9L0T4E4-entry; uniprot-Q8IYP9-entry; tian-2012-acyl-transferases-bk-fulltext]. An in vitro palmitoylation assay with ZDHHC23 and PHF2 independently showed that ZDHHC23 has palmitoyltransferase activity [jeong-2023-phf2-hcc-srebp1c-fulltext]. The acyl-donor range of ZDHHC23 has recently been probed directly. Wu et al. overexpressed Flag-tagged zDHHC23 in HepG2 cells and labelled the cells metabolically with alkyne-tagged C18:1 fatty acids that differ in double-bond position (Δ6, Δ9, Δ11). They detected autoacylated zDHHC23 intermediates, the first step of the ping-pong reaction, with all three probes. Δ11 gave the fewest intermediates, and Δ6 and Δ9 were used about equally well [wu-2026-chemoproteomics-isomer-sacylation-fulltext]. In covalent docking of these acyl chains onto the AlphaFold model of human zDHHC23 at the catalytic Cys289, the thioester carbonyl formed a hydrogen bond with His287 of the DHHC motif. This is the histidine thought to activate the acyl-enzyme intermediate for transfer to substrate. The bond was weaker for the poorly used Δ11 isomer [wu-2026-chemoproteomics-isomer-sacylation-fulltext]. ZDHHC23 is therefore better described as a protein S-acyltransferase that can use palmitoyl-CoA and at least some C18 monounsaturated acyl-CoAs, as is common in the family [mesquita-2024-s-acylation-review-abstract]. The EC 2.3.1.225 annotation of A0A9L0T4E4 captures only the palmitate reaction.

Within the family, ZDHHC23 is unusual in several respects. It has a long cytoplasmic N-terminal region (about 87 residues in human) that contains a conserved "LCCCEY" cysteine cluster, and a predicted disordered segment just before the DHHC domain [uniprot-Q8IYP9-entry; notes/sequence_analysis.md]. Its transmembrane topology is also atypical. UniProt predicts seven transmembrane helices for human ZDHHC23 [uniprot-Q8IYP9-entry]. Reviews of the family place zDHHC23 with zDHHC13 and zDHHC17 as the members predicted to have six transmembrane domains, unlike the canonical four [malgapo-2021-substrate-recruitment-review-fulltext; wu-2026-chemoproteomics-isomer-sacylation-fulltext]. Rat NIDD was originally described with five [saitoh-2004-nidd-nnos-abstract]. The Drosophila member of the subfamily has been characterized experimentally as a six-pass protein [kraft-2011-gabpi-domains-abstract]. None of these topologies has been confirmed experimentally for a vertebrate ZDHHC23. The AlphaFold model of the horse protein (AF-A0A9L0T4E4-F1) has a mean pLDDT of 71.6. About 60% of residues are modelled with confident or very high confidence, and about 27% with very low confidence [alphafold-A0A9L0T4E4-entry]. This fits a well-defined membrane and DHHC core flanked by disordered termini and linkers, but it does not settle the number of membrane-spanning helices. ZDHHC23 does not appear among the family members that contain a C-terminal dilysine ER-retention signal, a feature that sends DHHC4 and DHHC6 to the ER [gorleku-2011-dhhc-er-sorting-abstract]. This is consistent with its post-ER localization.

## 4. Subcellular Localization

Most DHHC enzymes sit in the ER and/or Golgi, and only a few reach the plasma membrane or endosomes [ohno-2006-dhhc-localization-abstract; gorleku-2011-dhhc-er-sorting-abstract]. For ZDHHC23, the most direct evidence comes from Tian et al. In HEK293 cells, overexpressed zDHHC23 overlapped mainly with the cis-Golgi marker GM130 (Pearson's R ≈ 0.71) and, to a lesser degree, with the TGN marker TGN38 (R ≈ 0.38) [tian-2012-acyl-transferases-bk-fulltext]. Endogenous Zdhhc23 in mouse aortic vascular smooth muscle cells, detected with an antibody validated by loss of signal in Zdhhc23⁻/⁻ cells, was perinuclear and intracellular, "consistent with Golgi and ER localization" [duncan-2019-bk-beta1-sacylation-fulltext]. The Golgi localization is conserved in evolution. Large yellow croaker zDHHC23 co-localized with TGN38 and not with the ER marker calnexin in fish macrophages [dai-2024-zdhhc23-large-yellow-croaker-fulltext]. These data support the UniProt annotation of A0A9L0T4E4 as a Golgi apparatus membrane, multi-pass protein [uniprot-A0A9L0T4E4-entry; uniprot-Q8IYP9-entry].

Two other localization claims need caution. First, rat NIDD co-fractionated with nNOS in synaptosomes, synaptic plasma membranes, lipid rafts and postsynaptic density fractions, and its mRNA is found in dendrites [saitoh-2004-nidd-nnos-abstract]. This points to a neuronal, PDZ-dependent pool near synapses, perhaps limited to the EDIV-containing isoform. Second, immunohistochemistry and immunofluorescence in glioma and hepatoma tissue reported ZDHHC23 signal in the nucleus as well as the cytoplasm, and in the hepatoma study ZDHHC23 co-localized with nuclear PHF2 [chen-2019-dhhc-glioma-stem-cells-fulltext; jeong-2023-phf2-hcc-srebp1c-fulltext]. A nuclear pool would be very unusual for a polytopic DHHC enzyme, and these observations relied on commercial antibodies without knockout validation. The GO annotation "endoplasmic reticulum" (IBA) on A0A9L0T4E4 rests on phylogenetic inference [uniprot-A0A9L0T4E4-entry]. It is reasonable given the biosynthetic route of the enzyme, but the experimental evidence favours the Golgi/TGN as the site where ZDHHC23 acts.

## 5. Substrates and Substrate Specificity

### 5.1 The BK channel α-subunit (KCNMA1): the best-validated substrate

The strongest evidence for a ZDHHC23 substrate concerns the BK channel. Tian et al. screened siRNAs against every zDHHC with an imaging assay based on a YFP fusion of the S0–S1 loop of the BK α-subunit, whose palmitoylation at Cys53, Cys54 and Cys56 sends it to the plasma membrane. Only knockdown of zDHHC22 or zDHHC23 reduced surface expression [tian-2012-acyl-transferases-bk-fulltext]. In the full-length ZERO splice variant, where the S0–S1 cysteines are the only palmitoylation sites, knocking down either enzyme reduced [³H]palmitate incorporation and cell-surface expression to about the level of the C53:54:56A mutant. The knockdowns had no further effect on that mutant, and knocking down both enzymes was not additive. Overexpression of zDHHC23 increased surface delivery of the S0–S1 reporter by about 144%, whereas zDHHC4 or zDHHC17 had no effect [tian-2012-acyl-transferases-bk-fulltext]. The study also showed site specificity within one protein. Cysteines in the alternatively spliced STREX insert in the BK C-terminus are palmitoylated by a different set of enzymes (zDHHC3, 5, 7, 9 and 17), not by zDHHC23 [tian-2012-acyl-transferases-bk-fulltext]. Depalmitoylation of the S0–S1 loop is carried out by the cytosolic thioesterases LYPLA1 and LYPLAL1. Together the transferases and thioesterases form a reversible cycle that acts as a checkpoint for exit of the channel from the TGN [tian-2012-acyl-transferases-bk-fulltext]. Later work completed this site-specific map. The S0–S1 loop is "largely S-acylated by zDHHC23" and deacylated by Lypla1, which leads to retention of the channel in the TGN. The STREX domain, by contrast, is acylated by enzymes that include zDHHC17 but not zDHHC23, and is deacylated by ABHD17a [mcclafferty-2020-abhd17a-bk-fulltext]. Reviews have consistently read the non-additive knockdowns to mean that zDHHC22 and zDHHC23 act in the same pathway, with zDHHC23 playing the primary role in S0–S1 palmitoylation [malgapo-2021-substrate-recruitment-review-fulltext; cassinelli-2022-vgic-palmitoylation-review-fulltext].

Duncan et al. extended this work to native tissue. Aortic smooth muscle cells from Zdhhc23⁻/⁻ mice had about 60% less endogenous BK α-subunit S-acylation, measured by acyl-RAC, with the remainder attributed to Zdhhc22 [duncan-2019-bk-beta1-sacylation-fulltext]. In these cells the regulatory β1 subunit is abundant. It rescued surface expression of non-acylated α-subunits, so loss of Zdhhc23 did not reduce surface channel numbers. However, it lowered BK currents by weakening the β1-induced leftward shift in voltage dependence. ZDHHC23 knockdown did not alter S-acylation of the β1 subunit itself [duncan-2019-bk-beta1-sacylation-fulltext]. ZDHHC23-mediated S0–S1 acylation thus has two context-dependent outputs: TGN exit and surface delivery when β1 is absent, and α/β1 functional coupling when β1 is present.

### 5.2 Other reported substrates

Several later studies proposed further substrates. In each case, ZDHHC23 was identified by screening panels of zDHHCs for an effect on palmitoylation of a protein of interest. In spinal astrocytes, overexpression of ZDHHC5, 12, 21 or 23 increased palmitoylation of the intermediate-filament protein GFAP, measured by acyl-biotin exchange. A Cys291Ala mutant reduced GFAP palmitoylation, and ZDHHC23 was the isoform up-regulated in a neuropathic cancer-pain model [fan-2024-gfap-zdhhc23-pain-fulltext]. In hepatoma cells, an siRNA screen of 23 ZDHHCs identified ZDHHC23 as the main enzyme that palmitoylates the histone demethylase PHF2 at Cys23. ZDHHC23 bound wild-type PHF2 but not the C23A mutant, and PHF2 palmitoylation led to its ubiquitination and proteasomal degradation [jeong-2023-phf2-hcc-srebp1c-fulltext]. Xu et al. reported that zDHHC23 S-acylates TDP-43, mainly at Cys244, and that this modification keeps TDP-43 condensates liquid-like by limiting their aberrant interaction with PARP1 and PARylated proteins [xu-2026-tdp43-sacylation-abstract]. Other abstracts report that ZDHHC23 palmitoylates the RNA acetyltransferase NAT10 in hepatocytes, promoting its nuclear export and loading into exosomes [wang-2026-nat10-exosomal-mash-abstract], and the Th1 transcription factor T-bet in T cells, promoting its degradation [xin-2025-tbet-methionine-gastric-abstract]. In an unbiased but overexpression-based chemoproteomic screen, proteins whose C18:1Δ9 labelling increased with zDHHC23 were enriched for nucleoplasmic annotations (42%, compared with 22% for the Δ6 probe) [wu-2026-chemoproteomics-isomer-sacylation-fulltext]. Taken together, ZDHHC23 may act on soluble and nucleocytoplasmic proteins as well as on integral membrane channels. Most of these are recent single reports, and several are available only as abstracts. Their mechanistic standard, for example catalytically dead DHHS controls and genetic loss-of-function in vivo, is generally below that of the BK channel work.

### 5.3 Evidence for selectivity

Negative results also help define what ZDHHC23 does not modify. Phosphatidylinositol 4-kinase IIα, which is palmitoylated at the TGN by DHHC3 and DHHC7, did not co-immunoprecipitate with DHHC23 [lu-2012-pi4k2a-palmitoylation-abstract]. As noted above, the BK STREX insert and the β1 subunit are not ZDHHC23 targets [tian-2012-acyl-transferases-bk-fulltext; duncan-2019-bk-beta1-sacylation-fulltext]. Together with general evidence that DHHC enzymes show partial but real substrate preferences [fukata-2004-psd95-palmitoylating-abstract; greaves-2011-dhhc-review-abstract; hou-2009-dhhc-overlapping-specificity-abstract], these results argue that ZDHHC23 is not a promiscuous enzyme. Its preference for membrane-proximal cysteine clusters such as the BK S0–S1 loop fits the structural model of an interfacial active site [rana-2018-dhhc-structure-abstract]. The molecular basis of its selectivity, including any role for its long N-terminal cytoplasmic region, is unknown [tian-2012-acyl-transferases-bk-fulltext].

## 6. Interaction with nNOS and Neural Functions

Before its enzymatic activity was known, rat ZDHHC23 was cloned as NIDD, an "nNOS-interacting DHHC domain-containing protein with dendritic mRNA". Its C-terminal –EDIV tail binds the PDZ domain of nNOS directly, as shown by pull-downs, PDZ-deletion mutants and co-sedimentation in COS-7 cells. In rat brain, NIDD and nNOS co-enrich in synaptic plasma membrane, lipid raft and postsynaptic density fractions and co-localize in cultured cortical neurons, and co-expression increases NO production by nNOS [saitoh-2004-nidd-nnos-abstract]. The authors proposed that NIDD regulates NO signalling at postsynaptic sites by recruiting nNOS to the membrane [saitoh-2004-nidd-nnos-abstract]. The abstract of that study does not report palmitoylation of nNOS. An authoritative review of ion-channel S-acylation later summarized the finding as showing that mammalian zDHHC23 "can bind and regulate, but does not S-acylate" nNOS [shipston-2014-ion-channel-sacylation-fulltext]. On this reading, the nNOS function of NIDD is a scaffolding role based on PDZ binding, separate from its catalytic activity. UniProt annotates the NOS1 interaction of human ZDHHC23 only by similarity to rat (ECO:0000250) [uniprot-Q8IYP9-entry]. As noted in Section 2, the canonical horse isoform lacks the PDZ ligand needed for this interaction, but another horse isoform keeps it [notes/sequence_analysis.md].

Rodent studies have repeatedly linked NIDD to the nNOS axis in neural injury and pain. NIDD mRNA is expressed in nociceptive dorsal root ganglion neurons and in dorsal horn neurons, and the number of NIDD-positive neurons rises in neuropathic and inflammatory pain models together with changes in nNOS [chen-2008-nidd-pain-drg-abstract]. NIDD is up-regulated with nNOS after sciatic nerve transection [cheng-2007-nidd-axotomy-abstract]. In the DBA/2J glaucoma model it co-localizes with nNOS in retinal Müller glia, and NOS inhibition, which protects retinal ganglion cells, also lowers NIDD expression [chen-2013-nnos-nidd-retina-abstract]. Separately, Fan et al. placed ZDHHC23 in spinal astrocytes in a cancer-pain model. There, ZDHHC23-dependent GFAP palmitoylation promotes astrocyte activation, secretion of IL-6, CXCL10 and GM-CSF, and STAT3 Tyr705 phosphorylation, forming a feed-forward loop. Blocking GFAP palmitoylation with a competitive peptide reduced pain and morphine tolerance [fan-2024-gfap-zdhhc23-pain-fulltext]. These studies are correlational or based on overexpression. Still, they consistently point to a role for ZDHHC23 in neural and glial responses to injury. The BK channel substrate also fits this picture, since BK channels are major regulators of neuronal and smooth-muscle excitability [tian-2012-acyl-transferases-bk-fulltext; duncan-2019-bk-beta1-sacylation-fulltext].

## 7. Evolutionary Conservation and a Non-Catalytic Ancestral Role

ZDHHC23 is conserved across vertebrates. The large yellow croaker has a zDHHC23 that clusters with other teleost orthologs, has a conserved DHHC domain and transmembrane architecture predicted to resemble the human protein, and localizes to the Golgi [dai-2024-zdhhc23-large-yellow-croaker-fulltext]. The subfamily also extends to insects. Drosophila GABPI (CG17257; UniProt Q9VQK9, entry name ZDH23_DROME) falls in the same PANTHER subfamily (PTHR22883:SF475) as horse A0A9L0T4E4 [uniprot-Q9VQK9-entry; uniprot-A0A9L0T4E4-entry]. In our local alignment, GABPI shares about 34% identity with the horse protein over 333 aligned residues. The shared region includes the N-terminal LCCCEY cysteine cluster, the transmembrane segments and the cysteine-rich domain. GABPI, however, carries DHHS in place of the DHHC tetrapeptide [notes/sequence_analysis.md]. A review of ion-channel S-acylation also describes GABPI as the Drosophila zDHHC23 orthologue [shipston-2014-ion-channel-sacylation-fulltext].

GABPI was found by expression cloning. It is required for the activity of the glycolipid-specific β1,4-N-acetylgalactosaminyltransferase β4GalNAcTB. Without GABPI, inactive β4GalNAcTB is trapped in the ER. Co-expression gives active enzyme that co-localizes with GABPI in the Golgi, and GABPI carrying an ER-retention signal holds active β4GalNAcTB in the ER [johswich-2009-drosophila-dhhc-pilot-fulltext]. Because the catalytic cysteine is absent, GABPI is not thought to be an acyltransferase. Mutating the DHHS region did not affect its function [johswich-2009-drosophila-dhhc-pilot-fulltext]. Instead, two lumenal loops between transmembrane domains 3–4 and 5–6, which carry conserved residues, are essential for activation of β4GalNAcTB, and the four C-terminal transmembrane helices are needed to target it to the Golgi [kraft-2011-gabpi-domains-abstract; uniprot-Q9VQK9-entry]. The authors noted that GABPI orthologues are present in arthropods and vertebrates but not in nematodes [johswich-2009-drosophila-dhhc-pilot-fulltext].

These observations have two implications for the horse protein. First, the vertebrate lineage has kept a fully catalytic DHHC motif, and vertebrate ZDHHC23 has demonstrated acyltransferase activity [tian-2012-acyl-transferases-bk-fulltext; jeong-2023-phf2-hcc-srebp1c-fulltext; wu-2026-chemoproteomics-isomer-sacylation-fulltext]. Catalysis is therefore the main function to annotate. Second, the subfamily has a recurring ability to act as a Golgi-resident partner that escorts or activates other membrane proteins independently of catalysis. This is seen in the fly chaperone role, in the PDZ-based scaffolding of nNOS by rodent NIDD, and in the macrophage phenotypes in fish that may not depend on catalysis [johswich-2009-drosophila-dhhc-pilot-fulltext; shipston-2014-ion-channel-sacylation-fulltext; dai-2024-zdhhc23-large-yellow-croaker-fulltext]. Whether mammalian ZDHHC23 also has a glycosyltransferase-pilot activity has not been tested.

## 8. Physiological Pathways and Disease Associations

The best-defined physiological pathway for ZDHHC23 is control of vascular smooth muscle excitability through BK channels. In aortic smooth muscle, Zdhhc23-dependent S-acylation of the α-subunit S0–S1 loop is needed for full functional coupling with β1 and for normal BK current density [duncan-2019-bk-beta1-sacylation-fulltext]. Because BK channels in smooth muscle provide negative feedback on Ca²⁺ entry, this links ZDHHC23 to the regulation of vascular tone, although blood-pressure phenotypes of the knockout were not reported in the papers reviewed here. The general importance of S-acylation cycles in signalling, metabolism and cardiovascular and neural physiology is set out in recent authoritative reviews [mesquita-2024-s-acylation-review-abstract; greaves-2011-dhhc-review-abstract].

A larger body of work comes from oncology and inflammation, and much of it is expression-based. In gliomas, ZDHHC23 expression rises with tumour grade and marks proneural, CD133⁺ glioma stem cells at the invasive leading edge. ZDHHC23 co-immunoprecipitates with ZDHHC18 and binds the BMI1 E3 ligase RNF144A, and ZDHHC18 competes for RNF144A, thereby controlling BMI1 polyubiquitination and the switch between proneural and mesenchymal states [chen-2019-dhhc-glioma-stem-cells-fulltext]. In hepatocellular carcinoma, palmitate-driven, ZDHHC23-mediated palmitoylation of PHF2 triggers PHF2 degradation, which relieves repression of SREBP1c and increases lipogenesis. ZDHHC23 expression correlates with HCC stage [jeong-2023-phf2-hcc-srebp1c-fulltext]. Reported effects on NAT10 export in fatty-liver fibrosis and on T-bet stability in anti-tumour Th1 immunity extend this list [wang-2026-nat10-exosomal-mash-abstract; xin-2025-tbet-methionine-gastric-abstract]. In a teleost fish, zDHHC23 is induced in macrophages by bacterial infection and promotes M2 (anti-inflammatory) polarization. The authors suggest this may reflect a non-catalytic role, but they did not test catalytic mutants [dai-2024-zdhhc23-large-yellow-croaker-fulltext]. Expression-based association studies add Crohn's disease, where ZDHHC23 is down-regulated in mucosa across several cohorts [zhou-2025-crohn-palmitoylation-genes-fulltext], and non-MYCN-amplified neuroblastoma. In the neuroblastoma study, which is a preprint, zDHHC23 is a hypoxia-responsive prognostic marker, and its interactome loses association with the 26S proteasome and the TIM23 mitochondrial import complex under hypoxia [oswald-2025-zdhhc23-hypoxia-neuroblastoma-abstract]. These findings place ZDHHC23 in protein stability and degradation pathways (BMI1, PHF2, T-bet), in phase separation (TDP-43) and in protein trafficking (NAT10, BK). The common thread is the generic effect of S-acylation on membrane association and protein turnover, not one dedicated signalling pathway.

For the horse, no studies of ZDHHC23 function, variation or phenotype were found. Bgee RNA-seq calls show that the horse gene is expressed widely. The highest expression scores are in the inner cell mass and trophectoderm of the early embryo and in skeletal muscle (gluteus medius, triceps brachii). Expression is also detected in oviduct and bronchial epithelium, kidney, testis, leukocytes, liver, retina, prefrontal cortex and cerebellum [bgee-ENSECAG00000014382-expression]. This broad pattern fits the expression of BK channels in muscle, airway, renal and neural tissues, but whether ZDHHC23 modifies BK channels in equine tissues is untested. The near-identity of the horse catalytic core and the conservation of zDHHC23 from fish to mammals [dai-2024-zdhhc23-large-yellow-croaker-fulltext; notes/sequence_analysis.md] support transferring the core annotations to A0A9L0T4E4: molecular function protein-cysteine S-palmitoyltransferase activity (GO:0019706), cellular component Golgi membrane/trans-Golgi network, and biological processes protein palmitoylation and protein localization to plasma membrane (exemplified by BK channels) [uniprot-A0A9L0T4E4-entry; tian-2012-acyl-transferases-bk-fulltext].

## 9. Open Questions

The most immediate question for the horse is which ZDHHC23 isoforms are expressed in which tissues. The canonical A0A9L0T4E4 isoform lacks the C-terminal –EDIV PDZ ligand that mediates binding to nNOS in rodents, while another annotated horse isoform (ENSECAP00000025325) keeps it [notes/sequence_analysis.md; saitoh-2004-nidd-nnos-abstract]. Equine RNA-seq or long-read transcript data could show whether the PDZ-binding form predominates in brain and smooth muscle, and therefore whether the nNOS-targeting function applies to horses. The same question applies to human ZDHHC23, whose canonical isoform also lacks the motif. Whether NIDD/ZDHHC23 actually palmitoylates nNOS, or only anchors it through a PDZ interaction, has not been resolved.

Mechanistically, the basis of ZDHHC23 substrate selectivity is unknown. This includes the roles of its long cytoplasmic N-terminus, its disordered pre-DHHC segment, its disputed six- or seven-helix topology, and the structural basis of its acyl-chain preferences. ZDHHC23 can use C18:1 donors in cells, but its in vivo acyl profile on endogenous substrates such as the BK channel has not been measured [tian-2012-acyl-transferases-bk-fulltext; rana-2018-dhhc-structure-abstract; uniprot-Q8IYP9-entry; malgapo-2021-substrate-recruitment-review-fulltext; wu-2026-chemoproteomics-isomer-sacylation-fulltext]. An experimental or high-quality predicted structure combined with substrate-docking studies would help. The many recently reported substrates (GFAP, PHF2, TDP-43, NAT10, T-bet) should be checked with catalytically dead mutants (DHHS), knockout tissues and site-specific acyl-PEG exchange. Their apparent nuclear and nucleocytoplasmic locations also need to be reconciled with the Golgi/TGN localization of the enzyme [jeong-2023-phf2-hcc-srebp1c-fulltext; xu-2026-tdp43-sacylation-abstract; tian-2012-acyl-transferases-bk-fulltext]. Antibody-based reports of nuclear ZDHHC23 should be repeated with knockout-validated reagents.

Physiologically, the cardiovascular and neural phenotypes of Zdhhc23 knockout mice beyond smooth muscle BK currents, such as blood pressure, nociception and synaptic NO signalling, are not well described in the literature reviewed here [duncan-2019-bk-beta1-sacylation-fulltext]. How ZDHHC22 and ZDHHC23 divide the work of S0–S1 acylation in different tissues is also unclear. In horses, given the importance of vascular and airway smooth muscle physiology and of neuropathic pain in equine medicine, studies of ZDHHC23 expression and BK channel S-acylation in equine tissues would be a natural follow-up. Finally, the proposed non-catalytic immunomodulatory roles of zDHHC23 seen in fish macrophages need direct testing with catalytic mutants [dai-2024-zdhhc23-large-yellow-croaker-fulltext]. Given that the Drosophila subfamily member GABPI is a catalytically dead Golgi "pilot" for a glycolipid glycosyltransferase, it would be informative to ask whether vertebrate ZDHHC23 also escorts or activates partner enzymes in the secretory pathway. The lumenal loops that are essential in GABPI are a natural place to start mutagenesis [johswich-2009-drosophila-dhhc-pilot-fulltext; kraft-2011-gabpi-domains-abstract]. The hypoxia-regulated interactions of ZDHHC23 with the proteasome and the TIM23 complex reported in neuroblastoma cells also need peer-reviewed confirmation [oswald-2025-zdhhc23-hypoxia-neuroblastoma-abstract].

## References

- **[uniprot-A0A9L0T4E4-entry]** UniProt Consortium. UniProtKB/TrEMBL entry A0A9L0T4E4 (A0A9L0T4E4_HORSE), "Palmitoyltransferase", *Equus caballus*; entry version 15 (02-Sep-2026). https://rest.uniprot.org/uniprotkb/A0A9L0T4E4.txt
- **[uniprot-Q8IYP9-entry]** UniProt Consortium. UniProtKB/Swiss-Prot entry Q8IYP9 (ZDH23_HUMAN), Palmitoyltransferase ZDHHC23, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/Q8IYP9.txt
- **[uniprot-Q76IC6-entry]** UniProt Consortium. UniProtKB/Swiss-Prot entry Q76IC6 (ZDH23_RAT), Palmitoyltransferase ZDHHC23, *Rattus norvegicus*. https://rest.uniprot.org/uniprotkb/Q76IC6.txt
- **[ensembl-ENSECAG00000014382-entry]** Ensembl. Gene ENSECAG00000014382 (ZDHHC23, VGNC:25198), *Equus caballus*. https://rest.ensembl.org/lookup/id/ENSECAG00000014382?expand=1
- **[notes/sequence_analysis.md]** Sequence comparison performed for this report (Biopython global alignment of A0A9L0T4E4 vs Q8IYP9; C-terminal comparison of horse Ensembl isoforms vs rat Q76IC6 and mouse Q5Y5T3). Script: notes/align.py.
- **[uniprot-Q9VQK9-entry]** UniProt Consortium. UniProtKB/Swiss-Prot entry Q9VQK9 (ZDH23_DROME), Protein beta4GalNAcTB pilot (GABPI), *Drosophila melanogaster*. https://rest.uniprot.org/uniprotkb/Q9VQK9.txt
- **[alphafold-A0A9L0T4E4-entry]** AlphaFold Protein Structure Database. Model AF-A0A9L0T4E4-F1, version 6. https://alphafold.ebi.ac.uk/api/prediction/A0A9L0T4E4
- **[bgee-ENSECAG00000014382-expression]** Bgee. Expression calls for horse ZDHHC23 (ENSECAG00000014382) by anatomical entity. https://www.bgee.org/api/?page=gene&action=expression&gene_id=ENSECAG00000014382&species_id=9796&cond_param=anat_entity&display_type=json
- **[wade-2009-horse-genome]** Wade CM, Giulotto E, Sigurdsson S, et al. (2009). Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 326:865-867. PMID:19892987; PMCID:PMC3785132; DOI:10.1126/science.1178158
- **[saitoh-2004-nidd-nnos]** Saitoh F, Tian QB, Okano A, Sakagami H, Kondo H, Suzuki T. (2004). NIDD, a novel DHHC-containing protein, targets neuronal nitric-oxide synthase (nNOS) to the synaptic membrane through a PDZ-dependent interaction and regulates nNOS activity. *J Biol Chem* 279:29461-29468. PMID:15105416; DOI:10.1074/jbc.m401471200
- **[tian-2012-acyl-transferases-bk]** Tian L, McClafferty H, Knaus HG, Ruth P, Shipston MJ. (2012). Distinct acyl protein transferases and thioesterases control surface expression of calcium-activated potassium channels. *J Biol Chem* 287:14718-14725. PMID:22399288; PMCID:PMC3340283; DOI:10.1074/jbc.m111.335547
- **[duncan-2019-bk-beta1-sacylation]** Duncan PJ, Bi D, McClafferty H, Chen L, Tian L, Shipston MJ. (2019). S-Acylation controls functional coupling of BK channel pore-forming α-subunits and β1-subunits. *J Biol Chem* 294:12066-12076. PMID:31213527; PMCID:PMC6690687; DOI:10.1074/jbc.ra119.009065
- **[lu-2012-pi4k2a-palmitoylation]** Lu D, Sun HQ, Wang H, Barylko B, Fukata Y, Fukata M, Albanesi JP, Yin HL. (2012). Phosphatidylinositol 4-kinase IIα is palmitoylated by Golgi-localized palmitoyltransferases in cholesterol-dependent manner. *J Biol Chem* 287:21856-21865. PMID:22535966; PMCID:PMC3381148; DOI:10.1074/jbc.m112.348094
- **[chen-2019-dhhc-glioma-stem-cells]** Chen X, Hu L, Yang H, Ma H, Ye K, Zhao C, Zhao Z, Dai H, Wang H, Fang Z. (2019). DHHC protein family targets different subsets of glioma stem cells in specific niches. *J Exp Clin Cancer Res* 38:25. PMID:30658672; PMCID:PMC6339410; DOI:10.1186/s13046-019-1033-2
- **[fan-2024-gfap-zdhhc23-pain]** Fan X, Zhang S, Sun S, Bi W, Li S, Wang W, Chen X, Fang Z. (2024). GFAP palmitoylcation mediated by ZDHHC23 in spinal astrocytes contributes to the development of neuropathic pain. *Reg Anesth Pain Med* 49:821-830. PMID:38050183; PMCID:PMC11671973; DOI:10.1136/rapm-2023-104980
- **[jeong-2023-phf2-hcc-srebp1c]** Jeong DW, Park JW, Kim KS, et al. (2023). Palmitoylation-driven PHF2 ubiquitination remodels lipid metabolism through the SREBP1c axis in hepatocellular carcinoma. *Nat Commun* 14:6370. PMID:37828054; PMCID:PMC10570296; DOI:10.1038/s41467-023-42170-0
- **[xu-2026-tdp43-sacylation]** Xu W, Li H, Zhang W, Bai G, Shen C, Zhang K. (2026). S-acylation of TDP43 regulates its condensation in amyotrophic lateral sclerosis. *Mol Cell* 86:2191-2206.e8. PMID:42127907
- **[wang-2026-nat10-exosomal-mash]** Wang Y, Wu L, Li Z, et al. (2026). Palmitoylation-mediated exosomal trafficking of nuclear protein NAT10 potentiates liver fibrosis in MASH. *Hepatology*. PMID:42103688; DOI:10.1097/hep.0000000000001785
- **[xin-2025-tbet-methionine-gastric]** Xin L, Xu HS, Fan LJ, et al. (2025). Methionine Restriction Exerts Anti-Tumor Immunity via Joint Intervention of T-Bet Palmitoylation in Gastric Cancer. *Biotechnol J* 20:e202400574. PMID:39989253; DOI:10.1002/biot.202400574
- **[dai-2024-zdhhc23-large-yellow-croaker]** Dai T, Zhao Z, Zhu T, Fei C, Nie L, Chen J. (2024). The anti-inflammatory role of zDHHC23 through the promotion of macrophage M2 polarization and macrophage necroptosis in large yellow croaker (*Larimichthys crocea*). *Front Immunol* 15:1401626. PMID:38868779; PMCID:PMC11167447; DOI:10.3389/fimmu.2024.1401626
- **[chen-2008-nidd-pain-drg]** Chen ML, Cheng C, Lv QS, et al. (2008). Altered gene expression of NIDD in dorsal root ganglia and spinal cord of rats with neuropathic or inflammatory pain. *J Mol Histol* 39:125-133. PMID:17899403; DOI:10.1007/s10735-007-9144-z
- **[cheng-2007-nidd-axotomy]** Cheng C, Chen M, Shi S, et al. (2007). Effect of peripheral axotomy on gene expression of NIDD in rat neural tissues. *J Mol Neurosci* 32:199-206. PMID:17873365; DOI:10.1007/s12031-007-0035-2
- **[chen-2013-nnos-nidd-retina]** Chen C, Xu Y, Zhang J, Zhu J, Zhang J, Hu N, Guan H. (2013). Altered expression of nNOS/NIDD in the retina of a glaucoma model of DBA/2J mice and the intervention by nNOS inhibition. *J Mol Neurosci* 51:47-56. PMID:23297011; DOI:10.1007/s12031-012-9943-x
- **[fukata-2004-psd95-palmitoylating]** Fukata M, Fukata Y, Adesnik H, Nicoll RA, Bredt DS. (2004). Identification of PSD-95 palmitoylating enzymes. *Neuron* 44:987-996. PMID:15603741; DOI:10.1016/j.neuron.2004.12.005
- **[ohno-2006-dhhc-localization]** Ohno Y, Kihara A, Sano T, Igarashi Y. (2006). Intracellular localization and tissue-specific distribution of human and yeast DHHC cysteine-rich domain-containing proteins. *Biochim Biophys Acta* 1761:474-483. PMID:16647879; DOI:10.1016/j.bbalip.2006.03.010
- **[rana-2018-dhhc-structure]** Rana MS, Kumar P, Lee CJ, Verardi R, Rajashankar KR, Banerjee A, Banerjee A. (2018). Fatty acyl recognition and transfer by an integral membrane S-acyltransferase. *Science* 359:eaao6326. PMID:29326245; PMCID:PMC6317078; DOI:10.1126/science.aao6326
- **[rana-2019-dhhc-mechanism-review]** Rana MS, Lee CJ, Banerjee A. (2019). The molecular mechanism of DHHC protein acyltransferases. *Biochem Soc Trans* 47:157-167. PMID:30559274; DOI:10.1042/bst20180429
- **[mesquita-2024-s-acylation-review]** S Mesquita F, Abrami L, Linder ME, Bamji SX, Dickinson BC, van der Goot FG. (2024). Mechanisms and functions of protein S-acylation. *Nat Rev Mol Cell Biol* 25:488-509. PMID:38355760; PMCID:PMC12010433; DOI:10.1038/s41580-024-00700-8
- **[greaves-2011-dhhc-review]** Greaves J, Chamberlain LH. (2011). DHHC palmitoyl transferases: substrate interactions and (patho)physiology. *Trends Biochem Sci* 36:245-253. PMID:21388813; DOI:10.1016/j.tibs.2011.01.003
- **[gorleku-2011-dhhc-er-sorting]** Gorleku OA, Barns AM, Prescott GR, Greaves J, Chamberlain LH. (2011). Endoplasmic reticulum localization of DHHC palmitoyltransferases mediated by lysine-based sorting signals. *J Biol Chem* 286:39573-39584. PMID:21926431; PMCID:PMC3234780; DOI:10.1074/jbc.m111.272369
- **[hou-2009-dhhc-overlapping-specificity]** Hou H, John Peter AT, Meiringer C, Subramanian K, Ungermann C. (2009). Analysis of DHHC acyltransferases implies overlapping substrate specificity and a two-step reaction mechanism. *Traffic* 10:1061-1073. PMID:19453970; DOI:10.1111/j.1600-0854.2009.00925.x
- **[wu-2026-chemoproteomics-isomer-sacylation]** Wu P, Nie W, Wu Y, Huang X, Wan Q, Li S, Chen S. (2026). Enzyme-centric chemoproteomics reveals isomer-specific S-acylation modification networks. *Nat Commun* 17:5661. PMID:42031719; PMCID:PMC13316068; DOI:10.1038/s41467-026-72237-7
- **[mcclafferty-2020-abhd17a-bk]** McClafferty H, Runciman H, Shipston MJ. (2020). Site-specific deacylation by ABHD17a controls BK channel splice variant activity. *J Biol Chem* 295:16487-16496. PMID:32913120; PMCID:PMC7864050; DOI:10.1074/jbc.ra120.015349
- **[shipston-2014-ion-channel-sacylation]** Shipston MJ. (2014). Ion channel regulation by protein S-acylation. *J Gen Physiol* 143:659-678. PMID:24821965; PMCID:PMC4035745; DOI:10.1085/jgp.201411176
- **[malgapo-2021-substrate-recruitment-review]** Malgapo MIP, Linder ME. (2021). Substrate recruitment by zDHHC protein acyltransferases. *Open Biol* 11:210026. PMID:33878949; PMCID:PMC8059564; DOI:10.1098/rsob.210026
- **[cassinelli-2022-vgic-palmitoylation-review]** Cassinelli S, Viñola-Renart C, Benavente-Garcia A, Navarro-Pérez M, Capera J, Felipe A. (2022). Palmitoylation of Voltage-Gated Ion Channels. *Int J Mol Sci* 23:9357. PMID:36012639; PMCID:PMC9409123; DOI:10.3390/ijms23169357
- **[johswich-2009-drosophila-dhhc-pilot]** Johswich A, Kraft B, Wuhrer M, Berger M, Deelder AM, Hokke CH, Gerardy-Schahn R, Bakker H. (2009). Golgi targeting of Drosophila melanogaster beta4GalNAcTB requires a DHHC protein family-related protein as a pilot. *J Cell Biol* 184:173-183. PMID:19139268; PMCID:PMC2615082; DOI:10.1083/jcb.200801071
- **[kraft-2011-gabpi-domains]** Kraft B, Johswich A, Kauczor G, Scharenberg M, Gerardy-Schahn R, Bakker H. (2011). "Add-on" domains of Drosophila β1,4-N-acetylgalactosaminyltransferase B in the stem region and its pilot protein. *Cell Mol Life Sci* 68:4091-4100. PMID:21598021; PMCID:PMC11114974; DOI:10.1007/s00018-011-0725-3
- **[zhou-2025-crohn-palmitoylation-genes]** Zhou Y, Zhao Y. (2025). S-palmitoylation-related genes in Crohn's disease: Bioinformatic identification and validation. *Biomol Biomed* 26:973-985. PMID:41364644; PMCID:PMC12873759; DOI:10.17305/bb.2025.13221
- **[oswald-2025-zdhhc23-hypoxia-neuroblastoma]** Oswald SO, Daly LA, Clarke K, Brownridge PJ, Pizer B, Prior IA, Sée V, Eyers CE. (2025). Hypoxia-induced regulation of zDHHC23 opens avenues for new biomarkers for NON MYCN-amplified neuroblastoma. bioRxiv preprint. DOI:10.1101/2025.11.03.686197


## Citations

1. alphafold-A0A9L0T4E4-entry.json
2. alphafold-A0A9L0T4E4-summary.md
3. bgee-ENSECAG00000014382-expression-summary.md
4. bgee-ENSECAG00000014382-expression.json
5. cassinelli-2022-vgic-palmitoylation-review-abstract.md
6. cassinelli-2022-vgic-palmitoylation-review-fulltext.txt
7. cassinelli-2022-vgic-palmitoylation-review-summary.md
8. chen-2008-nidd-pain-drg-abstract.md
9. chen-2008-nidd-pain-drg-summary.md
10. chen-2013-nnos-nidd-retina-abstract.md
11. chen-2013-nnos-nidd-retina-summary.md
12. chen-2019-dhhc-glioma-stem-cells-abstract.md
13. chen-2019-dhhc-glioma-stem-cells-fulltext.txt
14. chen-2019-dhhc-glioma-stem-cells-summary.md
15. cheng-2007-nidd-axotomy-abstract.md
16. cheng-2007-nidd-axotomy-summary.md
17. dai-2024-zdhhc23-large-yellow-croaker-abstract.md
18. dai-2024-zdhhc23-large-yellow-croaker-fulltext.txt
19. dai-2024-zdhhc23-large-yellow-croaker-summary.md
20. duncan-2019-bk-beta1-sacylation-abstract.md
21. duncan-2019-bk-beta1-sacylation-fulltext.txt
22. duncan-2019-bk-beta1-sacylation-summary.md
23. ensembl-ENSECAG00000014382-entry.json
24. ensembl-ENSECAG00000014382-summary.md
25. fan-2024-gfap-zdhhc23-pain-abstract.md
26. fan-2024-gfap-zdhhc23-pain-fulltext.txt
27. fan-2024-gfap-zdhhc23-pain-summary.md
28. fukata-2004-psd95-palmitoylating-abstract.md
29. fukata-2004-psd95-palmitoylating-summary.md
30. gorleku-2011-dhhc-er-sorting-abstract.md
31. gorleku-2011-dhhc-er-sorting-summary.md
32. greaves-2011-dhhc-review-abstract.md
33. greaves-2011-dhhc-review-summary.md
34. hou-2009-dhhc-overlapping-specificity-abstract.md
35. hou-2009-dhhc-overlapping-specificity-summary.md
36. jeong-2023-phf2-hcc-srebp1c-abstract.md
37. jeong-2023-phf2-hcc-srebp1c-fulltext.txt
38. jeong-2023-phf2-hcc-srebp1c-summary.md
39. johswich-2009-drosophila-dhhc-pilot-abstract.md
40. johswich-2009-drosophila-dhhc-pilot-fulltext.txt
41. johswich-2009-drosophila-dhhc-pilot-summary.md
42. kraft-2011-gabpi-domains-abstract.md
43. kraft-2011-gabpi-domains-summary.md
44. lu-2012-pi4k2a-palmitoylation-abstract.md
45. lu-2012-pi4k2a-palmitoylation-summary.md
46. malgapo-2021-substrate-recruitment-review-abstract.md
47. malgapo-2021-substrate-recruitment-review-fulltext.txt
48. malgapo-2021-substrate-recruitment-review-summary.md
49. mcclafferty-2020-abhd17a-bk-abstract.md
50. mcclafferty-2020-abhd17a-bk-fulltext.txt
51. mcclafferty-2020-abhd17a-bk-summary.md
52. mesquita-2024-s-acylation-review-abstract.md
53. mesquita-2024-s-acylation-review-summary.md
54. ohno-2006-dhhc-localization-abstract.md
55. ohno-2006-dhhc-localization-summary.md
56. oswald-2025-zdhhc23-hypoxia-neuroblastoma-abstract.md
57. oswald-2025-zdhhc23-hypoxia-neuroblastoma-summary.md
58. rana-2018-dhhc-structure-abstract.md
59. rana-2018-dhhc-structure-summary.md
60. rana-2019-dhhc-mechanism-review-abstract.md
61. rana-2019-dhhc-mechanism-review-summary.md
62. saitoh-2004-nidd-nnos-abstract.md
63. saitoh-2004-nidd-nnos-summary.md
64. shipston-2014-ion-channel-sacylation-abstract.md
65. shipston-2014-ion-channel-sacylation-fulltext.txt
66. shipston-2014-ion-channel-sacylation-summary.md
67. tian-2012-acyl-transferases-bk-abstract.md
68. tian-2012-acyl-transferases-bk-fulltext.txt
69. tian-2012-acyl-transferases-bk-summary.md
70. uniprot-A0A9L0T4E4-entry.txt
71. uniprot-A0A9L0T4E4-summary.md
72. uniprot-Q76IC6-entry.txt
73. uniprot-Q76IC6-summary.md
74. uniprot-Q8IYP9-entry.txt
75. uniprot-Q8IYP9-summary.md
76. uniprot-Q9VQK9-entry.txt
77. uniprot-Q9VQK9-summary.md
78. wade-2009-horse-genome-abstract.md
79. wade-2009-horse-genome-summary.md
80. wang-2026-nat10-exosomal-mash-abstract.md
81. wang-2026-nat10-exosomal-mash-summary.md
82. wu-2026-chemoproteomics-isomer-sacylation-abstract.md
83. wu-2026-chemoproteomics-isomer-sacylation-fulltext.txt
84. wu-2026-chemoproteomics-isomer-sacylation-summary.md
85. xin-2025-tbet-methionine-gastric-abstract.md
86. xin-2025-tbet-methionine-gastric-summary.md
87. xu-2026-tdp43-sacylation-abstract.md
88. xu-2026-tdp43-sacylation-summary.md
89. zhou-2025-crohn-palmitoylation-genes-abstract.md
90. zhou-2025-crohn-palmitoylation-genes-fulltext.txt
91. zhou-2025-crohn-palmitoylation-genes-summary.md