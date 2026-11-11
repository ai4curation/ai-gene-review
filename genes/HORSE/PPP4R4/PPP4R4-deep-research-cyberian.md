---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:11:26.564293'
end_time: '2026-10-26T03:22:47.204666'
duration_seconds: 680.64
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: PPP4R4
  gene_symbol: PPP4R4
  uniprot_accession: A0A9L0S961
  protein_description: 'RecName: Full=Serine/threonine-protein phosphatase 4 regulatory
    subunit 4 {ECO:0000256|ARBA:ARBA00068938};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: ARM-like. (IPR011989); ARM-type_fold. (IPR016024); HEAT_type_2.
    (IPR021133); PPP4R4. (IPR039918)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3302
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 41
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0S961
- **Protein Description:** RecName: Full=Serine/threonine-protein phosphatase 4 regulatory subunit 4 {ECO:0000256|ARBA:ARBA00068938};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ARM-like. (IPR011989); ARM-type_fold. (IPR016024); HEAT_type_2. (IPR021133); PPP4R4. (IPR039918)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PPP4R4" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PPP4R4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PPP4R4** (gene ID: PPP4R4, UniProt: A0A9L0S961) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PPP4R4 (Serine/threonine-protein phosphatase 4 regulatory subunit 4) in the horse, *Equus caballus* (UniProt A0A9L0S961)

## 1. Introduction and summary

UniProt A0A9L0S961 is an unreviewed (TrEMBL), computationally predicted horse protein of 865 amino acids. Ensembl predicted it from the Thoroughbred reference genome (gene ENSECAG00000019485, chromosome 24), and automatic rules name it "Serine/threonine-protein phosphatase 4 regulatory subunit 4" [uniprot-A0A9L0S961-entry; wade-2009-horse-genome-abstract]. The entry has no gene name, but its domain content (an ARM/HEAT-repeat α-solenoid, two PROSITE HEAT repeats at residues 213–290, and the family signature IPR039918/PTHR21467 "PPP4R4") places it in the PPP4R4 family [uniprot-A0A9L0S961-entry]. I aligned it against human PPP4R4 (UniProt Q6NUP7, 873 aa): the two proteins are about 94% identical along their whole length. Every residue shown experimentally to be needed for the human protein to bind the phosphatase is conserved in the horse protein, and all length differences fall in the C-terminal tail ([notes/sequence-comparison.md]; [uniprot-Q6NUP7-entry]). The identity check therefore passes. The gene symbol PPP4R4 matches the protein description, the organism is right, and the domains agree with the literature on mammalian PP4R4. No literature exists on horse PPP4R4 itself, so everything below about function is inferred from orthologs, mainly human with some mouse data.

PP4R4 was first described by Chen and colleagues in 2008. Before that it was known only as the uncharacterised brain cDNA KIAA1622 [chen-2008-pp4r4-fulltext; nagase-2000-kiaa-abstract]. It is a non-catalytic regulatory subunit of protein phosphatase 4 (PP4), a Ser/Thr phosphatase in the PP2A subfamily. Its sequence is distantly similar to the HEAT-repeat A ("scaffolding") subunit of PP2A. It binds the PP4 catalytic subunit PP4c (PPP4C) directly and selectively, with no detectable binding to PP2Ac, PP6c or PP1c. Its binding surface is analogous to the PP2Ac–PP2A A interface. Together they form a stable heterodimer, PP4c·PP4R4, that is separate from the other known PP4 holoenzymes (PP4c·PP4R1, PP4c·PP4R2·PP4R3α/β, and α4-bound PP4c). Unlike PP2A A, PP4R4 does not appear to recruit a third subunit [chen-2008-pp4r4-fulltext]. Tagged PP4R4 is found only in the cytoplasm, and the PP4c·PP4R4 complex shows lower phosphatase activity in vitro than the PP4c·PP4R2·PP4R3A complex [chen-2008-pp4r4-fulltext]. Endogenous PP4R4 is scarce in common cell lines but enriched in brain, where it co-precipitates with endogenous PP4c [chen-2008-pp4r4-fulltext; hpa-PPP4R4-record]. No physiological substrates are known, and no biological process has been tied to PP4R4 by direct experiment. Its main function is best described as a cytosolic PP4 regulatory (targeting) subunit that forms a dedicated PP4c·PP4R4 phosphatase complex. Its substrates and its pathway are still unknown.

## 2. Identity, gene structure and evolutionary conservation

Human PP4R4 is encoded at 14q32.13. The gene spans about 133 kb, produces alternatively spliced transcripts, and is conserved across Metazoa [chen-2008-pp4r4-fulltext]. UniProt lists two human isoforms: the 873-residue canonical form and a truncated variant that diverges after residue 98 [uniprot-Q6NUP7-entry]. In GWAS and DNA methylation studies, the human locus is mostly mentioned because it lies next to the SERPINA gene cluster. For example, a COPD meta-analysis reported a "PPP4R4/SERPINA1" association signal, which the authors attributed to known SERPINA1 variants [busch-2017-copd-gwas-abstract]. Such associations say nothing about PPP4R4 function. The horse gene lies on equine chromosome 24 [uniprot-A0A9L0S961-entry], consistent with the extensive human–horse synteny reported for the horse genome [wade-2009-horse-genome-abstract].

Horse A0A9L0S961 has 865 residues and aligns end to end with human isoform 1 without insertions. I counted 822 identical positions. The horse sequence has four short deletions, totalling eight residues, in the C-terminal ~130 residues; three of them fall in segments annotated as intrinsically disordered [notes/sequence-comparison.md; uniprot-Q6NUP7-entry]. The N-terminal and central HEAT/ARM region, which carries the PP4c-binding determinants, is almost invariant. The only notable divergence is at the very C-terminus. Human PP4R4 ends …KATLKSRKSNP, whereas the horse gene model ends …KATFLNI, so the last eight or so residues differ. This could be a real divergence in the last exon or an artefact of the gene prediction [notes/sequence-comparison.md]. This degree of conservation, and the fact that the horse model is annotated by PANTHER subfamily PTHR21467:SF0 and FunFam 1.25.10.10:FF:000097, makes it very likely that the horse protein is the true one-to-one ortholog of human PP4R4 and shares its biochemical properties [uniprot-A0A9L0S961-entry].

## 3. Domain architecture: a PP2A A-like HEAT-repeat solenoid

The human protein has three canonical HEAT repeats plus further lower-confidence repeats found by repeat-detection software. Among all HEAT-repeat proteins, it is most similar to the PP2A scaffolding A subunit (PPP2R1A, 15 HEAT repeats): about 19% identity and 40% similarity over 492 residues. Threading predicted a three-dimensional fold close to that of PP2A A [chen-2008-pp4r4-fulltext]. PP4R4 is also similar to the earlier-known PP4 subunit PP4R1, which has 13 HEAT repeats (22% identity over 265 residues) [chen-2008-pp4r4-fulltext]. The horse protein carries the same features: InterPro ARM-like (IPR011989) and ARM-type fold (IPR016024) signatures, Gene3D 1.25.10.10 (the α-α superhelix), and two PROSITE HEAT repeats at the same positions as in human (213–250 and 252–290). These sit alongside a coiled-coil keyword and C-terminal disordered regions (713–766 and 820–865) [uniprot-A0A9L0S961-entry]. Chen and colleagues noted a large insertion in PP4R4 that separates the regions corresponding to the PP2Ac-contacting HEAT repeats of PP2A A, and suggested it may contribute to PP4c specificity [chen-2008-pp4r4-fulltext]. The C-terminal part of the protein, used to raise antibodies, has no significant similarity to any other human protein [chen-2008-pp4r4-fulltext]. It probably holds the regulatory or targeting functions unique to PP4R4, but this has not been tested.

## 4. Molecular function: a specific, non-catalytic partner of PP4c

PP4R4 was found by single-step FLAG affinity purification and mass spectrometry of PP4c from HEK293 cells. It was detected reproducibly across six biological replicates, together with the known subunits PP4R1, PP4R2, PP4R3A/B and α4/IGBP1 [chen-2008-pp4r4-fulltext]. Reciprocal and targeted experiments then established specificity. HA-PP4R4 co-purified with FLAG-PP4c but not with FLAG-PP1c, PP2Acα, PP2Acβ or PP6c. Endogenous PP4R4 was recovered with FLAG-PP4c but not with FLAG-PP2Acα. In mouse brain lysate, antibodies to PP4R4 co-immunoprecipitated endogenous PP4c but not PP2A [chen-2008-pp4r4-fulltext]. Several independent proteome-scale studies support the PP4R4–PPP4C interaction, including the human phosphatase interactome and the BioPlex AP-MS networks; IntAct and GO cite these as further physical-interaction evidence [stdenis-2016-phosphatase-interactome-abstract; huttlin-2017-bioplex-abstract; huttlin-2021-bioplex-abstract; schaffer-2025-cell-maps-abstract; uniprot-Q6NUP7-entry].

Mutational analysis showed that PP4R4 binds PP4c through a surface equivalent to the one PP2A A uses to bind PP2Ac. In PP2A A, Arg-418 and Val-533 contact the catalytic subunit and are often mutated in lung and colon cancers. They correspond to Arg-501 and Val-616 in PP4R4. The R501W and V616D substitutions abolished PP4c binding and V616A weakened it [chen-2008-pp4r4-fulltext]. On the catalytic side, the PP4c substitutions E64K and E277K (at the predicted A-subunit interface) abolished PP4R4 binding, and N76D, R107E and E39K reduced it. None of these affected α4 binding, which shows the mutant proteins were not grossly misfolded [chen-2008-pp4r4-fulltext]. The binding modes still differ among PP4 subunits. PP4R1, although also a HEAT-repeat protein, still bound the E277K mutant normally, and PP4R2 tolerated E64K while being abolished by E39K. So α4, PP4R1, PP4R2 and PP4R4 each contact PP4c in a different way [chen-2008-pp4r4-fulltext]. PP4R4 binding does not need PP4c catalytic activity, because the phosphatase-dead mutants H56Q and R86A bound as well as wild type [chen-2008-pp4r4-fulltext]. Arg-501 is conserved in the horse protein. In canonical human Q6NUP7, the residue at position 616 is aspartate, so "Val-616" from Chen et al. (numbered on NP_478144) probably corresponds to a nearby valine in the conserved segment …ELTHDPV618ANV…, which is identical in horse [notes/sequence-comparison.md].

The PP2A analogy breaks down on scaffolding. PP2A A links the catalytic subunit to B-type regulatory subunits. PP4R4 was not found in AP-MS of PP4R1, PP4R2 or PP4R3A/B. None of those subunits was found in PP4R4 purifications or co-immunoprecipitations. And no new high-confidence third subunit co-purified with PP4R4 [chen-2008-pp4r4-fulltext]. Chen et al. therefore concluded that PP4c·PP4R4 is an independent heterodimeric holoenzyme rather than a scaffold for further subunits, and later reviews and experimental papers have adopted this four-complex model of PP4 (PP4C/PP4R1, PP4C/PP4R2/PP4R3A, PP4C/PP4R2/PP4R3B, and PP4C/PP4R4) [park-2020-pp4-review-fulltext; yang-2026-fbxo42-pp4-fulltext; lyons-2021-pp4-methylation-fulltext; hwang-2016-lcmt1-pp4-fulltext].

## 5. Effect on catalytic activity and substrate specificity

PP4R4 has no catalytic activity itself. Its effect on PP4c was measured with complexes co-expressed in insect cells and purified through a tag on the regulatory subunit, which excludes free catalytic subunit. On the generic substrate 6,8-difluoro-4-methylumbelliferyl phosphate (DiFMUP), PP4c·PP4R4 consistently had about half the activity of PP4c·PP4R2·PP4R3A. The same difference (about two-fold, at equal PP4c amounts) was seen with the protein substrate γH2AX (phospho-Ser139 H2AX) in acid-extracted histones [chen-2008-pp4r4-fulltext]. PP4R2 also reduced PP4c activity on DiFMUP in a dose-dependent way, so the difference reflects regulatory subunits generally damping the broad activity of free PP4c, not PP4R2 acting as an activator. The authors proposed this may reflect a shift from a highly active, unspecific phosphatase to a more selective holoenzyme [chen-2008-pp4r4-fulltext]. MGI has annotated these data to the GO terms "protein phosphatase inhibitor activity" and "protein serine/threonine phosphatase inhibitor activity" (IDA, PMID 18715871) [uniprot-Q6NUP7-entry]. That reading goes further than the paper's own interpretation. The authors present PP4R4 as a targeting/regulatory subunit and explicitly consider, without endorsing, the idea that it acts as an inhibitor. A more conservative description is "protein phosphatase regulator activity", which PAN-GO also assigns by phylogenetic inference (IBA) [uniprot-Q6NUP7-entry; chen-2008-pp4r4-fulltext].

The substrate specificity of PP4c·PP4R4 is unknown. The authors judged that γH2AX is probably not a physiological target, because PP4R4 is cytoplasmic and H2AX is chromatin-bound. In line with this, knocking down PP4R4 with two independent siRNAs did not raise γH2AX levels or cause the S–G2/M accumulation seen after PP4c knockdown [chen-2008-pp4r4-fulltext]. Structural studies have since defined how the PP4R2·PP4R3A complex recognises its substrates, through proline-rich motifs [yang-2026-fbxo42-pp4-fulltext]. No comparable substrate-docking mechanism or motif has been reported for PP4R4. The other cytoplasmic complex, PP4C/PP4R1, has a confirmed cytoplasmic substrate: it binds and dephosphorylates phosphofructokinase-1 (PFKM and PFKP), and losing the complex raises PFK-1 activity. The same authors state that a cellular function for PP4R4 has still not been reported [park-2023-pp4-pfk1-fulltext]. So although the cytoplasm contains both PP4R1- and PP4R4-containing complexes, only the PP4R1 complex has a known substrate. Whether PP4R4 shares or competes for such cytosolic metabolic substrates has not been tested. A 2020 review noted that no endogenous inhibitor proteins of PP4C/PP4R4 have been found either, whereas PP4IP, DHX38 and TIPRL are known to act on the PP4R2/PP4R3 complexes [park-2020-pp4-review-fulltext].

## 6. Subcellular localisation

Experimental and database evidence both place PP4R4 in the cytoplasm, mainly the cytosol. HA-tagged PP4R4 transfected into Vero cells, and stably expressed in HEK293 cells, gave exclusively cytoplasmic staining. This contrasts with the mainly nuclear PP4R2 and PP4R3 and with PP4c, which is both nuclear and cytoplasmic [chen-2008-pp4r4-fulltext]. Blocking CRM1-dependent nuclear export with leptomycin B did not move PP4R4 into the nucleus, so the protein probably does not shuttle [chen-2008-pp4r4-fulltext]. The Human Protein Atlas places PPP4R4 mainly in the cytosol, with additional staining at the primary cilium and basal body [hpa-PPP4R4-record]. That ciliary/basal-body signal comes from antibody-based imaging alone and has not been confirmed independently. A separate study probed the C-terminal tripeptide of human PP4R4. When the native C-terminus was fused to EGFP in COS7 cells, the fusion stayed evenly cytosolic, so the wild-type tail is not a peroxisomal targeting signal. A rare human variant, rs576288488 (P873L), changes the tail to SNL, which becomes a functional PTS1: it directs the reporter to PMP70-positive peroxisomes and increases binding to PEX5 [chong-2019-pts1-variants-fulltext]. This finding concerns a human variant, not normal PP4R4 biology, and the horse C-terminus (…LNI) does not match the PTS1 consensus either [notes/sequence-comparison.md]. Later papers likewise describe PP4R1 and PP4R4 as the two cytoplasmic PP4 regulatory subunits, in contrast to the nuclear PP4R2 and PP4R3α/β [park-2023-pp4-pfk1-fulltext]. The horse UniProt entry's "Cytoplasm" annotation was transferred automatically from this body of evidence [uniprot-A0A9L0S961-entry]. PP4R4 therefore most likely recruits a pool of PP4c to cytoplasmic substrates. This is a separate role from the nuclear and centrosomal jobs of the PP4R2·PP4R3 and PP4R1 complexes in DNA repair, chromatin regulation and centrosome maturation [chen-2008-pp4r4-fulltext; cohen-2005-pp4-review-abstract].

## 7. Expression, stability and regulation

Endogenous PP4R4 is a low-abundance protein in HEK293, 293T and U2OS cells and was not detected in HeLa cells. Expressed-sequence-tag counts in 2008 were an order of magnitude lower than for other PP4 subunits, and about half of the ESTs came from hippocampus or other brain libraries [chen-2008-pp4r4-fulltext]. RT-PCR-ELISA data from the Kazusa project and in situ hybridisation from the Allen Brain Atlas, as summarised by Chen et al., show the highest mRNA levels in striatum (caudate nucleus), amygdala, hippocampus and thalamus [chen-2008-pp4r4-fulltext]. Current Human Protein Atlas data agree: PPP4R4 RNA is "tissue enhanced" in brain (15.1 nTPM) and testis (7.5 nTPM). In single-cell data it is "group enriched" in inhibitory and excitatory neurons, astrocytes, Bergmann glia, oligodendrocyte precursors and ependymal (ciliated) cells [hpa-PPP4R4-record]. Isolated high-throughput reports describe PPP4R4 transcripts rising in bovine theca and granulosa cells after the luteinising-hormone surge, but these have not been followed up mechanistically [christenson-2013-lh-surge-abstract].

PP4R4 depends on PP4c for its stability. Knocking down PP4c greatly reduced PP4R4 protein, whereas knocking down PP4R4 did not change PP4c levels [chen-2008-pp4r4-fulltext]. This fits a common pattern among PPP regulatory subunits, which are degraded when not bound in a holoenzyme. Lyons et al., however, found a more complicated picture. PP4c is carboxyl-methylated by LCMT1. In LCMT1-hypomorphic HEK293T cells, PP4R4 protein rose about three-fold without any increase in PP4R4 incorporated into PP4 holoenzymes, and PP4R4 binding to PP4c was largely insensitive to the loss of C-terminal methylation. PP4R1 binding, in contrast, depended strongly on methylation [lyons-2021-pp4-methylation-fulltext]. Hwang et al. had earlier shown that PP4 holoenzymes depend on methylation to different degrees but could not test PP4R4 for lack of a suitable antibody [hwang-2016-lcmt1-pp4-fulltext]. More recently, the SCF ubiquitin ligase substrate receptor FBXO42 was shown to ubiquitinate PP4 complexes and to control how regulatory and catalytic subunits assemble, restraining PP4 activity [yang-2026-fbxo42-pp4-abstract]. Whether PP4R4-containing complexes are FBXO42 targets has not been reported; the authors list PP4R4-dependent substrates among the possible contributors to phenotypes after PP4C depletion [yang-2026-fbxo42-pp4-fulltext].

## 8. Pathways and biological role: what can and cannot be inferred

PP4 as a whole is an essential phosphatase in development, centrosome maturation, spliceosome assembly, NF-κB and TOR signalling, the DNA damage response and chromatin regulation [cohen-2005-pp4-review-abstract; park-2020-pp4-review-fulltext]. Nearly all of these functions have been traced to the PP4R1 or PP4R2·PP4R3 holoenzymes, not to PP4R4 [cohen-2005-pp4-review-abstract; park-2020-pp4-review-fulltext; chen-2008-pp4r4-fulltext]. Loss-of-function experiments on PP4R4 in cultured cells showed no cell-cycle or DNA-damage phenotype [chen-2008-pp4r4-fulltext]. Assigning the general PP4 pathways to PPP4R4 by "guilt by association" would therefore be unjustified. The evidence most strongly supports the following picture. PPP4R4 defines a distinct, cytosolic PP4 holoenzyme that is enriched in the nervous system (and to a lesser extent the testis), where it presumably directs PP4c to as-yet-unidentified cytoplasmic phosphoproteins. Chen et al. explicitly suggested that it "performs cell- or tissue-specific functions and is involved in cognitive processes", but this remains a hypothesis [chen-2008-pp4r4-fulltext]. For the horse ortholog, near-identical sequence and conserved PP4c-binding residues make it reasonable to transfer the molecular-function annotation (PP4c binding / protein phosphatase regulator activity), the complex membership (PPP4C–PPP4R4 serine/threonine phosphatase complex) and the cytoplasmic/cytosolic localisation. Transferring any specific biological process would be speculative.

## Open Questions

The main gap is that no physiological substrate of PP4c·PP4R4 is known, in horse or any other species. Unbiased phosphoproteomics after PP4R4 deletion in neurons or brain tissue, or proximity labelling (BioID/TurboID) of PP4R4 in neural cells, would be the most direct ways to find substrates and the pathway they belong to. A second question is structural. No experimental structure of PP4c·PP4R4 exists, and an AlphaFold-Multimer or cryo-EM model of the heterodimer would show whether the PP2A A-like solenoid leaves a groove for docking substrates or a third subunit, and what the PP4R4-specific insertion and the disordered C-terminal tail contribute. Third, it is unresolved whether PP4R4 truly inhibits PP4c or simply narrows its specificity. The GO "phosphatase inhibitor activity" annotations should be reconsidered against the original authors' more cautious interpretation, ideally with assays on candidate protein substrates. Fourth, the Human Protein Atlas report of PPP4R4 at the primary cilium and basal body, together with its single-cell enrichment in ciliated ependymal cells, deserves orthogonal validation, because it could point to a cytoplasmic, cilium-associated pool of PP4. Fifth, the regulation of PP4R4 abundance needs to be explained: it depends on PP4c, yet rises when PP4c methylation falls, and it is unknown whether FBXO42 or other ubiquitin ligases act on PP4c·PP4R4. Sixth, no knockout phenotype in mouse (or any mammal) was found in the literature searched here, and organismal studies, particularly behavioural and neuroanatomical ones, would test the proposed neural role. Finally, for the horse specifically, the Ensembl gene model (865 aa) should be checked against equine RNA-seq. The C-terminal deletions and the divergent final residues (…FLNI instead of …SNP) relative to human could be real or could be annotation artefacts, and equine brain and testis expression data would confirm whether the tissue distribution is conserved.

## References

- [chen-2008-pp4r4] Chen GI, Tisayakorn S, Jorgensen C, D'Ambrosio LM, Goudreault M, Gingras AC. PP4R4/KIAA1622 forms a novel stable cytosolic complex with phosphoprotein phosphatase 4. *J Biol Chem* 2008;283(43):29273-84. PMID: 18715871; PMCID: PMC2662017; DOI: 10.1074/jbc.M803443200. https://pmc.ncbi.nlm.nih.gov/articles/PMC2662017/ (files: chen-2008-pp4r4-fulltext.txt, -abstract.md, -summary.md)
- [park-2020-pp4-review] Park J, Lee DH. Functional roles of protein phosphatase 4 in multiple aspects of cellular physiology: a friend and a foe. *BMB Rep* 2020;53(4):181-190. PMID: 32192570; PMCID: PMC7196183; DOI: 10.5483/BMBRep.2020.53.4.019.
- [cohen-2005-pp4-review] Cohen PT, Philp A, Vázquez-Martin C. Protein phosphatase 4--from obscurity to vital functions. *FEBS Lett* 2005;579(15):3278-86. PMID: 15913612; DOI: 10.1016/j.febslet.2005.04.070.
- [lyons-2021-pp4-methylation] Lyons SP, Greiner EC, Cressey LE, Adamo ME, Kettenbach AN. Regulation of PP2A, PP4, and PP6 holoenzyme assembly by carboxyl-terminal methylation. *Sci Rep* 2021;11(1):23031. PMID: 34845248; PMCID: PMC8630191; DOI: 10.1038/s41598-021-02456-z.
- [hwang-2016-lcmt1-pp4] Hwang J, Lee JA, Pallas DC. Leucine Carboxyl Methyltransferase 1 (LCMT-1) Methylates Protein Phosphatase 4 (PP4) and Protein Phosphatase 6 (PP6) and Differentially Regulates the Stable Formation of Different PP4 Holoenzymes. *J Biol Chem* 2016;291(40):21008-21019. PMID: 27507813; PMCID: PMC5076511; DOI: 10.1074/jbc.M116.739920.
- [yang-2026-fbxo42-pp4] Yang H, Smith P, et al., D'Angiolella V. Pervasive phenotypic effects of FBXO42 are promoted by regulation of PP4 phosphatase. *EMBO J* 2026;45(4):1332-1361. PMID: 41484364; PMCID: PMC12909836; DOI: 10.1038/s44318-025-00675-y.
- [park-2023-pp4-pfk1] Park J, Lee DH. Protein phosphatase 4 dephosphorylates phosphofructokinase-1 to regulate its enzymatic activity. *BMB Rep* 2023;56(11):618-623. PMID: 37605615; PMCID: PMC10689085; DOI: 10.5483/BMBRep.2023-0065.
- [chong-2019-pts1-variants] Chong CS, Kunze M, Hochreiter B, Krenn M, Berger J, Maurer-Stroh S. Rare Human Missense Variants can affect the Function of Disease-Relevant Proteins by Loss and Gain of Peroxisomal Targeting Motifs. *Int J Mol Sci* 2019;20(18):4609. PMID: 31533369; PMCID: PMC6770196; DOI: 10.3390/ijms20184609.
- [stdenis-2016-phosphatase-interactome] St-Denis N, Gupta GD, Lin ZY, et al., Gingras AC. Phenotypic and Interaction Profiling of the Human Phosphatases Identifies Diverse Mitotic Regulators. *Cell Rep* 2016;17(9):2488-2501. PMID: 27880917; DOI: 10.1016/j.celrep.2016.10.078.
- [huttlin-2017-bioplex] Huttlin EL, et al. Architecture of the human interactome defines protein communities and disease networks. *Nature* 2017;545(7655):505-509. PMID: 28514442; PMCID: PMC5531611; DOI: 10.1038/nature22366.
- [huttlin-2021-bioplex] Huttlin EL, et al. Dual proteome-scale networks reveal cell-specific remodeling of the human interactome. *Cell* 2021;184(11):3022-3040.e28. PMID: 33961781; PMCID: PMC8165030; DOI: 10.1016/j.cell.2021.04.011.
- [schaffer-2025-cell-maps] Schaffer LV, et al. Multimodal cell maps as a foundation for structural and functional genomics. *Nature* 2025;642(8066):222-231. PMID: 40205054; PMCID: PMC12137143; DOI: 10.1038/s41586-025-08878-3.
- [nagase-2000-kiaa] Nagase T, Kikuno R, Nakayama M, Hirosawa M, Ohara O. Prediction of the coding sequences of unidentified human genes. XVIII. The complete sequences of 100 new cDNA clones from brain which code for large proteins in vitro. *DNA Res* 2000;7(4):273-81. PMID: 10997877; DOI: 10.1093/dnares/7.4.271.
- [wade-2009-horse-genome] Wade CM, Giulotto E, Sigurdsson S, et al., Lindblad-Toh K. Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 2009;326(5954):865-7. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158.
- [busch-2017-copd-gwas] Busch R, Hobbs BD, Zhou J, et al. Genetic Association and Risk Scores in a Chronic Obstructive Pulmonary Disease Meta-analysis of 16,707 Subjects. *Am J Respir Cell Mol Biol* 2017;57(1):35-46. PMID: 28170284; PMCID: PMC5516277; DOI: 10.1165/rcmb.2016-0331OC.
- [christenson-2013-lh-surge] Christenson LK, Gunewardena S, Hong X, Spitschak M, Baufeld A, Vanselow J. Research resource: preovulatory LH surge effects on follicular theca and granulosa transcriptomes. *Mol Endocrinol* 2013;27(7):1153-71. PMID: 23716604; PMCID: PMC3706842; DOI: 10.1210/me.2013-1093.
- [uniprot-A0A9L0S961-entry] UniProtKB/TrEMBL A0A9L0S961_HORSE, entry version 13 (10-Jun-2026). https://rest.uniprot.org/uniprotkb/A0A9L0S961.txt
- [uniprot-Q6NUP7-entry] UniProtKB/Swiss-Prot Q6NUP7 (PP4R4_HUMAN). https://rest.uniprot.org/uniprotkb/Q6NUP7.txt (GO annotations cross-checked via QuickGO, https://www.ebi.ac.uk/QuickGO/)
- [hpa-PPP4R4-record] Human Protein Atlas, PPP4R4 (ENSG00000119698). https://www.proteinatlas.org/ENSG00000119698
- [notes/sequence-comparison.md] Own pairwise alignment of A0A9L0S961 vs Q6NUP7 (Biopython, BLOSUM62), this work.


## Citations

1. busch-2017-copd-gwas-abstract.md
2. busch-2017-copd-gwas-summary.md
3. chen-2008-pp4r4-abstract.md
4. chen-2008-pp4r4-fulltext.txt
5. chen-2008-pp4r4-summary.md
6. chong-2019-pts1-variants-abstract.md
7. chong-2019-pts1-variants-fulltext.txt
8. chong-2019-pts1-variants-summary.md
9. christenson-2013-lh-surge-abstract.md
10. cohen-2005-pp4-review-abstract.md
11. cohen-2005-pp4-review-summary.md
12. hpa-PPP4R4-record.json
13. huttlin-2017-bioplex-abstract.md
14. huttlin-2021-bioplex-abstract.md
15. huttlin-bioplex-summary.md
16. hwang-2016-lcmt1-pp4-abstract.md
17. hwang-2016-lcmt1-pp4-fulltext.txt
18. hwang-2016-lcmt1-pp4-summary.md
19. lyons-2021-pp4-methylation-abstract.md
20. lyons-2021-pp4-methylation-fulltext.txt
21. lyons-2021-pp4-methylation-summary.md
22. nagase-2000-kiaa-abstract.md
23. nagase-2000-kiaa-summary.md
24. park-2020-pp4-review-abstract.md
25. park-2020-pp4-review-fulltext.txt
26. park-2020-pp4-review-summary.md
27. park-2023-pp4-pfk1-abstract.md
28. park-2023-pp4-pfk1-fulltext.txt
29. park-2023-pp4-pfk1-summary.md
30. schaffer-2025-cell-maps-abstract.md
31. stdenis-2016-phosphatase-interactome-abstract.md
32. stdenis-2016-phosphatase-interactome-summary.md
33. uniprot-A0A9L0S961-entry.txt
34. uniprot-A0A9L0S961-sequence.fasta
35. uniprot-Q6NUP7-entry.txt
36. uniprot-Q6NUP7-sequence.fasta
37. wade-2009-horse-genome-abstract.md
38. wade-2009-horse-genome-summary.md
39. yang-2026-fbxo42-pp4-abstract.md
40. yang-2026-fbxo42-pp4-fulltext.txt
41. yang-2026-fbxo42-pp4-summary.md