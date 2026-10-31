---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:31:35.520153'
end_time: '2026-10-25T23:41:38.240754'
duration_seconds: 602.72
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: FBXL20
  gene_symbol: FBXL20
  uniprot_accession: A0A9L0IQA3
  protein_description: 'RecName: Full=F-box/LRR-repeat protein 20 {ECO:0000256|ARBA:ARBA00074033};
    AltName: Full=F-box and leucine-rich repeat protein 20 {ECO:0000256|ARBA:ARBA00080489};'
  gene_info: Name=FBXL20 {ECO:0000313|Ensembl:ENSEASP00005039961.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Not specified in UniProt
  protein_domains: F-box_dom. (IPR001810); FBXL15_LRR. (IPR057207); Leu-rich_rpt.
    (IPR001611); Leu-rich_rpt_Cys-con_subtyp. (IPR006553); LRR_dom_sf. (IPR032675)
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
citation_count: 54
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0IQA3
- **Protein Description:** RecName: Full=F-box/LRR-repeat protein 20 {ECO:0000256|ARBA:ARBA00074033}; AltName: Full=F-box and leucine-rich repeat protein 20 {ECO:0000256|ARBA:ARBA00080489};
- **Gene Information:** Name=FBXL20 {ECO:0000313|Ensembl:ENSEASP00005039961.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** F-box_dom. (IPR001810); FBXL15_LRR. (IPR057207); Leu-rich_rpt. (IPR001611); Leu-rich_rpt_Cys-con_subtyp. (IPR006553); LRR_dom_sf. (IPR032675)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "FBXL20" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'FBXL20' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **FBXL20** (gene ID: FBXL20, UniProt: A0A9L0IQA3) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# FBXL20 (F-box/LRR-repeat protein 20) in the donkey, *Equus asinus* (UniProt A0A9L0IQA3)

## Introduction and summary

FBXL20, known in rodents as SCRAPPER, is the substrate-recognition subunit of an SCF (SKP1–CUL1–F-box) E3 ubiquitin ligase. Its role is to select particular proteins for K48-linked polyubiquitination and so commit them to degradation by the proteasome. The donkey protein considered here, A0A9L0IQA3, is an unreviewed computational entry derived from the Ensembl annotation of the donkey reference genome [wang-2020-donkey-genomes-abstract], and it has never been studied directly. Every functional statement in this report is therefore an inference from orthologues in rat, mouse, human and *C. elegans*. The inference is unusually secure, because apart from a divergent N-terminal stretch of 15–27 residues the donkey sequence is identical to human FBXL20 across the whole F-box, the leucine-rich-repeat (LRR) solenoid and the C-terminus. From the motif FSNSDEAV onward, 421 of 421 residues match, and the protein ends in the same CIIL prenylation signal (see `SEQUENCE_NOTES.md`).

The best-established function of FBXL20 lies at the synapse. The founding study identified SCRAPPER as a synapse-localized E3 ligase that binds and ubiquitinates the presynaptic active-zone protein RIM1. In Scrapper-knockout neurons RIM1 persisted longer and carried less ubiquitin, and miniature excitatory postsynaptic currents (mEPSCs) became more frequent; re-expressing SCRAPPER or knocking down RIM1 rescued the phenotype. SCRAPPER is therefore the predominant ligase that limits RIM1 abundance and so tunes synaptic vesicle release [yao-2007-scrapper-rim1-abstract; dobie-2007-scrapper-trashes-rim-abstract].

Work outside the nervous system, largely in cancer cell lines, has added further substrates. These include the class III PI3-kinase Vps34, which FBXL20 degrades after DNA damage [xiao-2015-fbxl20-vps34-fulltext]; the PP2A regulatory subunit PR55α [madduri-2021-fbxl20-pr55a-fulltext]; the pro-apoptotic BCL-2 family proteins PUMA and BAX [manne-2021-fbxl20-puma-bax-fulltext]; and the costimulatory receptor 4-1BB [sun-2022-fbxl20-41bb-abstract]. FBXL20 is itself transcriptionally induced by p53 [xiao-2015-fbxl20-vps34-fulltext; madduri-2021-fbxl20-pr55a-fulltext] and repressed post-transcriptionally by at least two microRNAs [eisfeld-2012-mir3151-baalc-abstract; wu-2021-fbxl20-mir195-ovarian-abstract]. Structurally, FBXL20 belongs to the lipid-anchored FBXL2/FBXL20 subfamily. Its C-terminal CaaX motif is expected to be prenylated, which would tether the ligase to membranes and bias it toward substrates that reside on or near them [skaar-2013-fbox-substrate-recruitment-fulltext; kuchay-2019-ggtase3-fulltext].

## Identity verification and domain architecture

UniProt describes the donkey protein as F-box/LRR-repeat protein 20, encoded by FBXL20 on donkey chromosome 13 and 448 amino acids long. Its annotation is wholly computational. It records an F-box at residues 34–80, twelve cysteine-containing LRRs (SMART LRR_CC) and membership of PANTHER subfamily PTHR13318:SF47 ("F-box/LRR-repeat protein 20"). The statements that it binds SKP1 and CUL1 and resides in the cytoplasm were transferred by automatic rules from the reviewed human entry, Q96IG2.

My own sequence comparison (`SEQUENCE_NOTES.md`) found the donkey protein to be 97.2% identical to human FBXL20 and 97.0% identical to mouse Fbxl20 in a global alignment. All of the differences fall within the first 27 residues. Human and mouse begin with MRRDVNGVTKSRFEM, whereas the donkey model begins with an unrelated 27-residue extension, MRSVLVPQLPSMQAVIFKATAHLGIGM. This most likely reflects a different choice of start codon or first exon in the donkey gene model rather than a genuine biological difference, although I have not checked it against transcript evidence.

The gene symbol is not ambiguous. Every paper retrieved uses FBXL20 and SCRAPPER as names for the same orthologous gene [takagi-2012-scrapper-ltp-fulltext; koga-2017-scrapper-acc-abstract; yao-2011-scrapper-behavior-fulltext], and no unrelated gene sharing the symbol was found.

The domain layout agrees with published descriptions. Human FBXL20 has been described as a 438-residue protein with an F-box, leucine-rich repeats and a C-terminal CAAX prenylation site for membrane anchoring [xiao-2015-fbxl20-vps34-fulltext]. Its closest paralog, FBXL2, is 78% identical in my alignment and ends in CVIL, and a review of substrate recruitment by F-box proteins treats the two as a pair whose CAAX motifs are isoprenylated to direct them to membranes [skaar-2013-fbox-substrate-recruitment-fulltext]. In this architecture the F-box binds SKP1 to join the SCF core, while the curved LRR solenoid provides the surface that engages substrates. Consistent with this division of labour, the LRR region of FBXL20 was implicated in binding Vps34 [xiao-2015-fbxl20-vps34-fulltext].

## Molecular function: SCF E3 ligase substrate adaptor

FBXL20 has no catalytic activity of its own. As the F-box component of a cullin-RING ligase it supplies substrate specificity, while ubiquitin transfer from the E2 enzyme is carried out by the RING subunit RBX1 bound to CUL1. CUL1 acts as a scaffold that also binds SKP1, and SKP1 in turn bridges CUL1 to the F-box protein, which recruits the substrate through its protein-interaction domain [xiao-2015-fbxl20-vps34-fulltext; skaar-2013-fbox-substrate-recruitment-fulltext]. FBXL20 has been shown to assemble into such a complex with Skp1 and Cullin1 [xiao-2015-fbxl20-vps34-fulltext]. Its molecular function is best described as that of a ubiquitin-ligase substrate adaptor, contributing to ubiquitin-protein transferase activity (GO:0004842) within the SCF complex.

Like many F-box proteins, FBXL20 preferentially recognizes phosphorylated substrates, and the priming kinase differs from substrate to substrate. After DNA damage, CDK1 phosphorylates Vps34 on Thr159. A phospho-mimetic T159E mutant was still ubiquitinated and degraded by FBXL20, whereas a T159A mutant resisted degradation even though it could still bind, which led the authors to propose that phosphorylated T159 forms part of a degron [xiao-2015-fbxl20-vps34-fulltext]. In breast cancer cells, AKT1 phosphorylation of PUMA at Ser10 and of BAX at Ser184 was required for FBXL20 to recognize and degrade them. FBXL20 bound the BH3 domain of PUMA, recombinant FBXL20 bound GST-PUMA and GST-BAX directly in vitro, and an F-box-deleted mutant could not lower PUMA or BAX levels [manne-2021-fbxl20-puma-bax-fulltext].

For two further substrates the evidence is less detailed. FBXL20 knockdown reduced ubiquitination of PR55α (PPP2R2A) and roughly doubled its half-life, from about 6 h to about 12 h [madduri-2021-fbxl20-pr55a-fulltext]; fittingly, UniProt lists PPP2R2A among the binary interactors of human FBXL20. Separately, a BioID proximity screen identified FBXL20 as the E3 that polyubiquitinates the intracellular domain of 4-1BB (CD137), with a preference for its mature N-glycosylated form [sun-2022-fbxl20-41bb-abstract].

## Neuronal function: presynaptic RIM1 turnover and control of vesicle release

The earliest and most physiological evidence for FBXL20 function comes from neurons. Yao and colleagues identified SCRAPPER as a synapse-localized SCF E3 ligase that binds and ubiquitinates RIM1, an active-zone scaffold that interacts with Rab3 and Munc13 and governs the probability of vesicle release [eto-2020-scrapper-glutamate-gaba-fulltext]. In Scrapper-knockout neurons RIM1 had a longer half-life and was less ubiquitinated, and mEPSC frequency was raised, as a defect in RIM1 degradation would predict. RIM1 overexpression reproduced this phenotype, and re-expression of SCRAPPER or knockdown of RIM1 reversed it. Proteasome inhibitors normally produce a rapid rise in RIM1 levels and release probability, and this acute effect was abolished when SCRAPPER was impaired. Together these findings make SCRAPPER-dependent ubiquitination the link between the proteasome and presynaptic tuning [yao-2007-scrapper-rim1-abstract]. An accompanying commentary described SCRAPPER as targeting "a set of presynaptic proteins including RIM1α", implying that RIM1 is unlikely to be its only synaptic substrate [dobie-2007-scrapper-trashes-rim-abstract].

Later studies of knockout mice extended this picture to synaptic plasticity. At hippocampal CA3–CA1 synapses, Scrapper-knockout slices showed weaker long-term depression and stronger long-term potentiation, indicating that SCRAPPER sets the thresholds for bidirectional plasticity, a form of metaplasticity [takagi-2012-scrapper-ltp-fulltext]. In the anterior cingulate cortex, loss of SCRAPPER selectively increased miniature and spontaneous glutamate release while leaving evoked release unchanged, and it abolished presynaptic LTP [koga-2017-scrapper-acc-abstract]. Imaging mass spectrometry detected higher glutamate and GABA levels in several brain regions of knockout mice, among them the cortex, thalamus, midbrain and cerebellar cortex [eto-2020-scrapper-glutamate-gaba-fulltext]. Knockout brains also showed spongiform neurodegeneration and shrunken neurons [yao-2008-scrapper-ims-abstract]. At the behavioural level, heterozygous knockout mice were impaired in contextual but not cued fear conditioning and showed anxiety-related changes, and homozygous knockouts were lethal on a C57BL/6J background [yao-2011-scrapper-behavior-fulltext].

The FBXL20–RIM axis appears to be conserved across animals. In *C. elegans*, CFL-1, an LRR F-box protein highly homologous to FBXL20, interacts genetically with UNC-10, the worm orthologue of RIM, in controlling the defecation rhythm and dauer formation in response to daumone [kim-2017-cfl1-celegans-fulltext].

Studies in disease models support a role for FBXL20 dosage in neuronal excitability, although they rely on correlation or overexpression. In tissue from patients with temporal-lobe epilepsy and in a pilocarpine rat model, FBXL20 was reduced and RIM1 increased, and lentiviral overexpression of FBXL20 reduced seizures [fu-2016-fbxl20-epilepsy-abstract]. In rats exposed to chronic mild stress, hippocampal FBXL20 rose. The authors proposed that it promotes ubiquitination of VGLUT1 and VAMP1, and knocking FBXL20 down improved both synaptic and behavioural deficits [wang-2024-fbxl20-depression-abstract]. Until direct ubiquitination is demonstrated, VGLUT1 and VAMP1 are best regarded as candidate substrates.

## Subcellular localization

The donkey UniProt entry assigns FBXL20 to the cytoplasm, a statement carried over from the human entry with evidence code ECO:0000250 (by similarity). The experimental and structural evidence points to something more specific: a cytosolic protein that associates with membranes and, in neurons, concentrates at synapses. SCRAPPER was originally described as synapse-localized [yao-2007-scrapper-rim1-abstract], and later work placed it in presynaptic terminals, neuronal cell bodies and dendrites of the hippocampus and cortex [koga-2017-scrapper-acc-abstract]. It is expressed throughout the brain, with high mRNA and protein levels in neuron-rich regions such as the hippocampus, cerebellum and olfactory bulb [eto-2020-scrapper-glutamate-gaba-fulltext]. In human cortical neurons, FBXL20 immunoreactivity was observed both at membranes and in the cytoplasm [fu-2016-fbxl20-epilepsy-abstract].

Membrane association is attributed to the C-terminal CaaX motif, CIIL in both donkey and human, which acts as a prenylation signal for membrane anchoring [xiao-2015-fbxl20-vps34-fulltext]. A review states that CAAX-dependent membrane localization of FBXL20 is required for RIM1 degradation [skaar-2013-fbox-substrate-recruitment-fulltext].

The paralog FBXL2 has been characterized in far more detail, and the findings for it provide testable predictions for FBXL20, though none has yet been tested in FBXL20 itself. FBXL2 is geranylgeranylated on the cysteine of its CVIL motif [wang-2005-fbl2-geranylgeranylated-abstract]. The enzyme responsible is a dedicated prenyltransferase, GGTase3, composed of PTAR1 and RabGGTB, which recognizes the LRR domain of FBXL2 in addition to its CaaX tail; the structural study notes that FBXL20, the neuronal paralog, ends in the same kind of motif [kuchay-2019-ggtase3-fulltext]. FBXL2 is also palmitoylated on Cys417 and Cys419, just upstream of the CaaX. Cycles of palmitoylation and depalmitoylation, together with the solubilizing chaperone PDE6δ, determine which membrane compartment FBXL2 reaches and which substrates it degrades there [liang-2023-palmitoylation-pde6d-fulltext]. The C-R-C-C-I-I-L tail of donkey FBXL20 conserves the equivalent cysteines. It is therefore reasonable, though not yet demonstrated, to predict that FBXL20 is likewise geranylgeranylated, probably by GGTase3, then palmitoylated and trafficked to particular membranes.

## Pathways and regulation: p53, autophagy, apoptosis and PP2A signalling

Outside neurons, FBXL20 has been placed downstream of the tumour suppressor p53. DNA damage induces FBXL20 mRNA and protein in a p53-dependent manner. Together with CDK-mediated phosphorylation of Vps34, this triggers SCF(FBXL20)-dependent degradation of Vps34, which suppresses autophagy and slows the endocytic degradation of EGFR. The authors describe this as a p53-controlled checkpoint on autophagy and receptor trafficking [xiao-2015-fbxl20-vps34-fulltext]. FBXL20 knockdown raised Vps34 levels selectively, leaving its complex partners Beclin1, Vps15 and Atg14L unchanged [xiao-2015-fbxl20-vps34-fulltext].

A second p53-dependent pathway acts through PP2A. p53 maintains FBXL20 expression, and FBXL20 in turn limits the PP2A regulatory subunit PR55α, so that loss of p53 stabilizes PR55α. Elevated PR55α dephosphorylates c-Myc at Thr58, a modification that would otherwise promote c-Myc degradation, and so stabilizes c-Myc. In pancreatic cancer, low FBXL20 mRNA is associated with poor patient survival [madduri-2021-fbxl20-pr55a-fulltext].

In breast cancer cells FBXL20 opposes apoptosis by degrading PUMA and BAX after their phosphorylation by AKT1. FBXL20 is itself subject to regulated turnover: when AKT is inhibited, GSK3α/β becomes active and promotes degradation of FBXL20 by another F-box protein, FBXO31. AKT and GSK3 thus form a switch that decides between survival and death, and FBXL20 depletion sensitized cancer cells to chemotherapy [manne-2021-fbxl20-puma-bax-fulltext].

FBXL20 is also regulated post-transcriptionally. In cytogenetically normal acute myeloid leukaemia, FBXL20 was validated as a direct target of miR-3151, a microRNA encoded within an intron of BAALC whose high expression predicts poor outcome [eisfeld-2012-mir3151-baalc-abstract]. In ovarian cancer cells, miR-195-5p binds the FBXL20 3′ UTR, and FBXL20 overexpression promoted proliferation and suppressed apoptosis [wu-2021-fbxl20-mir195-ovarian-abstract]. Weaker evidence connects FBXL20 overexpression in colorectal cells with greater invasiveness and reduced E-cadherin, but direct ubiquitination of E-cadherin was not shown [zhu-2014-fbxl20-ecadherin-abstract].

Taken together, these studies portray FBXL20 as a membrane-tethered SCF adaptor whose substrates vary with cellular context. Two of the best-characterized substrates in cell lines, Vps34 and BAX, function at membranes, which fits a ligase anchored there by its lipid tail.

## Relevance to the donkey and evolutionary considerations

No study has examined FBXL20 in any equid. Because the donkey and human proteins are identical across the entire F-box, LRR solenoid and CaaX tail, results from rodent and human systems can be transferred to the donkey protein with high confidence at the level of molecular function and cellular location. That covers assembly into the SCF complex, recognition of phosphorylated substrates through the LRR region, presynaptic and membrane localization, and the turnover of RIM1 that controls vesicle release. Phenotypic and disease associations transfer less securely.

The FBXL2/FBXL20 subfamily is distributed across animals, as shown by the worm homologue CFL-1 and its genetic interaction with the RIM orthologue [kim-2017-cfl1-celegans-fulltext], so the neuronal FBXL20–RIM axis probably predates the vertebrates. On this basis, reasonable GO-style annotations for the donkey protein, all inferred by orthology (ISS or IBA), would be: the SCF ubiquitin ligase complex as its cellular component; ubiquitin-protein transferase activity, in its role as a substrate adaptor, as its molecular function; SCF-dependent proteasomal ubiquitin-dependent protein catabolic process and regulation of synaptic vesicle exocytosis (or presynaptic protein catabolism that modulates synaptic transmission) as its biological processes; and cytosol, presynapse and membrane as its locations.

## Open Questions

The first question concerns the donkey gene model itself. Its 27-residue N-terminus differs from every other mammalian orthologue examined, and donkey RNA-seq or Iso-Seq data are needed to decide whether this is a genuine alternative first exon or an annotation artefact.

Second, prenylation of FBXL20 rests on its CaaX motif and on analogy with FBXL2 rather than on direct measurement. Biochemical studies should establish whether FBXL20 is geranylgeranylated rather than farnesylated, whether GGTase3 carries out the modification, and whether the cysteines adjacent to the CaaX are palmitoylated as they are in FBXL2. The answers would also clarify how FBXL20 is targeted to synaptic membranes.

Third, no experimental structure of FBXL20 exists. A cryo-EM or crystal structure of SCF(FBXL20) bound to a phosphodegron peptide, such as Vps34 pT159 or PUMA pS10, would reveal how it recognizes substrates and why it accepts phosphorylation by such different kinases. The GGTase3–FBXL2 structure offers a template.

Fourth, the degron that SCRAPPER recognizes in RIM1, including any requirement for phosphorylation, has not been defined. Other proposed synaptic substrates, namely VGLUT1, VAMP1 and the "set of presynaptic proteins" mentioned in the commentary, still require direct ubiquitination assays.

Fifth, it is not known whether the substrates identified in cancer cell lines (Vps34, PUMA, BAX, PR55α and 4-1BB) are also targeted in neurons or normal tissues. Conditional knockouts could test, for example, whether FBXL20 controls autophagic flux in neurons. Whether the miR-3151 and miR-195-5p regulatory links operate in neurons is equally unknown.

Sixth, the division of labour between FBXL20 and FBXL2 remains unclear. The two are 78% identical and both lipid-anchored, so they may share or partition substrates, and double-knockout or domain-swap experiments would help resolve this.

Finally, nothing is known about FBXL20 expression or variation in donkeys or horses. Population-genomic analyses of donkey genomes could ask whether the gene has been under selection, for instance in relation to behavioural traits during domestication.

## References

* **dobie-2007-scrapper-trashes-rim**: Dobie F(1), Craig AM. A fight for neurotransmission: SCRAPPER trashes RIM. Cell. 2007 Sep 7;130(5):775-7. doi: 10.1016/j.cell.2007.08.020. PMID: 17803899; PMCID: PMC2821330; DOI: 10.1016/j.cell.2007.08.020; https://pubmed.ncbi.nlm.nih.gov/17803899/ (local files: dobie-2007-scrapper-trashes-rim-abstract.md, dobie-2007-scrapper-trashes-rim-summary.md)
* **eisfeld-2012-mir3151-baalc**: Eisfeld AK(1), Marcucci G, Maharry K, Schwind S, Radmacher MD, Nicolet D, Becker H, Mrózek K, Whitman SP, Metzeler KH, Mendler JH, Wu YZ, Liyanarachchi S, Patel R, Baer MR, Powell BL, Carter TH, Moore JO, Kolitz JE, Wetzler M, Caligiuri MA, Larson RA, Tanner SM, de la Chapelle A, Bloomfield CD. miR-3151 interplays with its host gene BAALC and independently affects outcome of patients with cytogenetically normal acute myeloid leukemia. Blood. 2012 Jul 12;120(2):249-58. doi: 10.1182/blood-2012-02-408492. Epub 2012 Apr 23. PMID: 22529287; PMCID: PMC3398762; DOI: 10.1182/blood-2012-02-408492; https://pubmed.ncbi.nlm.nih.gov/22529287/ (local files: eisfeld-2012-mir3151-baalc-abstract.md, eisfeld-2012-mir3151-baalc-summary.md)
* **eto-2020-scrapper-glutamate-gaba**: Eto F(1)(2)(3), Sato S(2)(4), Setou M(2)(4)(5), Yao I(6)(7)(8)(9). Region-specific effects of Scrapper on the abundance of glutamate and gamma-aminobutyric acid in the mouse brain. Sci Rep. 2020 May 4;10(1):7435. doi: 10.1038/s41598-020-64277-w. PMID: 32366828; PMCID: PMC7198594; DOI: 10.1038/s41598-020-64277-w; https://pubmed.ncbi.nlm.nih.gov/32366828/ (local files: eto-2020-scrapper-glutamate-gaba-abstract.md, eto-2020-scrapper-glutamate-gaba-fulltext.txt, eto-2020-scrapper-glutamate-gaba-summary.md)
* **fu-2016-fbxl20-epilepsy**: Fu P(1), Wen Y(1), Xiong Y(2), Zhang Y(2), Zhang H(3), Xie Y(1), Shi Q(4). Abnormal Expression of FBXL20 in Refractory Epilepsy Patients and a Pilocarpine-Induced Rat Model. Neurochem Res. 2016 Nov;41(11):3020-3031. doi: 10.1007/s11064-016-2021-y. Epub 2016 Aug 8. PMID: 27502938; DOI: 10.1007/s11064-016-2021-y; https://pubmed.ncbi.nlm.nih.gov/27502938/ (local files: fu-2016-fbxl20-epilepsy-abstract.md, fu-2016-fbxl20-epilepsy-summary.md)
* **kim-2017-cfl1-celegans**: Kim SM(1), Hwang SY(2). CFL-1, a novel F-box protein with leucine-rich repeat may interact with UNC-10 for the regulation of defecation and daumone response in Caenorhabditis elegans. Anim Cells Syst (Seoul). 2017 May 17;21(3):185-189. doi: 10.1080/19768354.2017.1325779. eCollection 2017. PMID: 30460068; PMCID: PMC6138319; DOI: 10.1080/19768354.2017.1325779; https://pubmed.ncbi.nlm.nih.gov/30460068/ (local files: kim-2017-cfl1-celegans-abstract.md, kim-2017-cfl1-celegans-fulltext.txt, kim-2017-cfl1-celegans-summary.md)
* **koga-2017-scrapper-acc**: Koga K(1)(2)(3), Yao I(4)(5), Setou M(5)(6)(7)(8)(9), Zhuo M(10)(2). SCRAPPER Selectively Contributes to Spontaneous Release and Presynaptic Long-Term Potentiation in the Anterior Cingulate Cortex. J Neurosci. 2017 Apr 5;37(14):3887-3895. doi: 10.1523/JNEUROSCI.0023-16.2017. Epub 2017 Mar 14. PMID: 28292828; PMCID: PMC6596717; DOI: 10.1523/JNEUROSCI.0023-16.2017; https://pubmed.ncbi.nlm.nih.gov/28292828/ (local files: koga-2017-scrapper-acc-abstract.md, koga-2017-scrapper-acc-summary.md)
* **kuchay-2019-ggtase3**: Kuchay S(1)(2)(3)(4), Wang H(5)(6), Marzio A(1)(3), Jain K(1)(3), Homer H(1)(3), Fehrenbacher N(1)(3), Philips MR(1)(3), Zheng N(7)(8), Pagano M(9)(10)(11). GGTase3 is a newly identified geranylgeranyltransferase targeting a ubiquitin ligase. Nat Struct Mol Biol. 2019 Jul;26(7):628-636. doi: 10.1038/s41594-019-0249-3. Epub 2019 Jun 17. PMID: 31209342; PMCID: PMC6609460; DOI: 10.1038/s41594-019-0249-3; https://pubmed.ncbi.nlm.nih.gov/31209342/ (local files: kuchay-2019-ggtase3-abstract.md, kuchay-2019-ggtase3-fulltext.txt, kuchay-2019-ggtase3-summary.md)
* **liang-2023-palmitoylation-pde6d**: Liang D(1), Jiang L(1), Bhat SA(1), Missiroli S(2), Perrone M(2), Lauriola A(3), Adhikari R(1), Gudur A(1), Vasi Z(1), Ahearn I(4), Guardavaccaro D(3), Giorgi C(2), Philips M(5), Kuchay S(6). Palmitoylation and PDE6δ regulate membrane-compartment-specific substrate ubiquitylation and degradation. Cell Rep. 2023 Jan 31;42(1):111999. doi: 10.1016/j.celrep.2023.111999. Epub 2023 Jan 19. PMID: 36662618; PMCID: PMC9988375; DOI: 10.1016/j.celrep.2023.111999; https://pubmed.ncbi.nlm.nih.gov/36662618/ (local files: liang-2023-palmitoylation-pde6d-abstract.md, liang-2023-palmitoylation-pde6d-fulltext.txt, liang-2023-palmitoylation-pde6d-summary.md)
* **madduri-2021-fbxl20-pr55a**: Madduri LSV(1), Brandquist ND(1), Palanivel C(1), Talmon GA(2), Baine MJ(3), Zhou S(1), Enke CA(1), Johnson KR(4), Ouellette MM(5), Yan Y(6). p53/FBXL20 axis negatively regulates the protein stability of PR55α, a regulatory subunit of PP2A Ser/Thr phosphatase. Neoplasia. 2021 Dec;23(12):1192-1203. doi: 10.1016/j.neo.2021.10.002. Epub 2021 Oct 30. PMID: 34731788; PMCID: PMC8570931; DOI: 10.1016/j.neo.2021.10.002; https://pubmed.ncbi.nlm.nih.gov/34731788/ (local files: madduri-2021-fbxl20-pr55a-abstract.md, madduri-2021-fbxl20-pr55a-fulltext.txt, madduri-2021-fbxl20-pr55a-summary.md)
* **manne-2021-fbxl20-puma-bax**: Manne RK(1), Agrawal Y(1), Malonia SK(2), Banday S(2), Edachery S(3), Patel A(4), Kumar A(4), Shetty P(3), Santra MK(5). FBXL20 promotes breast cancer malignancy by inhibiting apoptosis through degradation of PUMA and BAX. J Biol Chem. 2021 Oct;297(4):101253. doi: 10.1016/j.jbc.2021.101253. Epub 2021 Sep 26. PMID: 34587475; PMCID: PMC8507197; DOI: 10.1016/j.jbc.2021.101253; https://pubmed.ncbi.nlm.nih.gov/34587475/ (local files: manne-2021-fbxl20-puma-bax-abstract.md, manne-2021-fbxl20-puma-bax-fulltext.txt, manne-2021-fbxl20-puma-bax-summary.md)
* **skaar-2013-fbox-substrate-recruitment**: Skaar JR(1), Pagan JK, Pagano M. Mechanisms and function of substrate recruitment by F-box proteins. Nat Rev Mol Cell Biol. 2013 Jun;14(6):369-81. doi: 10.1038/nrm3582. Epub 2013 May 9. PMID: 23657496; PMCID: PMC3827686; DOI: 10.1038/nrm3582; https://pubmed.ncbi.nlm.nih.gov/23657496/ (local files: skaar-2013-fbox-substrate-recruitment-abstract.md, skaar-2013-fbox-substrate-recruitment-fulltext.txt, skaar-2013-fbox-substrate-recruitment-summary.md)
* **sun-2022-fbxl20-41bb**: Sun R(1), Lim SO(1)(2)(3). FBXL20-mediated ubiquitination triggers the proteasomal degradation of 4-1BB. FEBS J. 2022 Aug;289(15):4549-4563. doi: 10.1111/febs.16383. Epub 2022 Feb 11. PMID: 35112462; DOI: 10.1111/febs.16383; https://pubmed.ncbi.nlm.nih.gov/35112462/ (local files: sun-2022-fbxl20-41bb-abstract.md, sun-2022-fbxl20-41bb-summary.md)
* **takagi-2012-scrapper-ltp**: Takagi H(1), Setou M, Ito S, Yao I. SCRAPPER regulates the thresholds of long-term potentiation/depression, the bidirectional synaptic plasticity in hippocampal CA3-CA1 synapses. Neural Plast. 2012;2012:352829. doi: 10.1155/2012/352829. Epub 2012 Dec 20. PMID: 23316391; PMCID: PMC3539422; DOI: 10.1155/2012/352829; https://pubmed.ncbi.nlm.nih.gov/23316391/ (local files: takagi-2012-scrapper-ltp-abstract.md, takagi-2012-scrapper-ltp-fulltext.txt, takagi-2012-scrapper-ltp-summary.md)
* **wang-2005-fbl2-geranylgeranylated**: Wang C(1), Gale M Jr, Keller BC, Huang H, Brown MS, Goldstein JL, Ye J. Identification of FBL2 as a geranylgeranylated cellular protein required for hepatitis C virus RNA replication. Mol Cell. 2005 May 13;18(4):425-34. doi: 10.1016/j.molcel.2005.04.004. PMID: 15893726; DOI: 10.1016/j.molcel.2005.04.004; https://pubmed.ncbi.nlm.nih.gov/15893726/ (local files: wang-2005-fbl2-geranylgeranylated-abstract.md, wang-2005-fbl2-geranylgeranylated-summary.md)
* **wang-2020-donkey-genomes**: Wang C(#)(1)(2), Li H(#)(3), Guo Y(#)(4), Huang J(#)(1), Sun Y(#)(1), Min J(#)(4), Wang J(#)(1), Fang X(4), Zhao Z(5), Wang S(5), Zhang Y(5), Liu Q(4), Jiang Q(1), Wang X(1), Guo Y(1), Yang C(1), Wang Y(3), Tian F(3), Zhuang G(1), Fan Y(1), Gao Q(1), Li Y(2), Ju Z(1), Li J(1), Li R(1), Hou M(1), Yang G(6), Liu G(2), Liu W(2), Guo J(7), Pan S(7), Fan G(7), Zhang W(1), Zhang R(2), Yu J(3), Zhang X(3), Yin Q(4), Ji C(3), Jin Y(4), Yue G(4), Liu M(8), Xu J(9), Liu S(10), Jordana J(10), Noce A(10)(11)(12), Amills M(10)(11), Wu DD(13)(14), Li S(15), Zhou X(16)(17), Zhong J(18)(19). Donkey genomes provide new insights into domestication and selection for coat color. Nat Commun. 2020 Dec 8;11(1):6014. doi: 10.1038/s41467-020-19813-7. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7; https://pubmed.ncbi.nlm.nih.gov/33293529/ (local files: wang-2020-donkey-genomes-abstract.md, wang-2020-donkey-genomes-summary.md)
* **wang-2024-fbxl20-depression**: Wang W(1), Li Y(1), Wang L(2), Chen X(1), Lan T(1), Wang C(1), Chen S(3), Yu S(4). FBXL20 promotes synaptic impairment in depression disorder via degrading vesicle-associated proteins. J Affect Disord. 2024 Mar 15;349:132-144. doi: 10.1016/j.jad.2024.01.055. Epub 2024 Jan 9. PMID: 38211741; DOI: 10.1016/j.jad.2024.01.055; https://pubmed.ncbi.nlm.nih.gov/38211741/ (local files: wang-2024-fbxl20-depression-abstract.md, wang-2024-fbxl20-depression-summary.md)
* **wu-2021-fbxl20-mir195-ovarian**: Wu D(1), Liu C(1), Hong L(2). F-Box and Leucine-Rich Repeat Protein 20 (FBXL20), Negatively Regulated by microRNA (miR)-195-5p, Accelerates the Malignant Progression of Ovarian Cancer. Mol Biotechnol. 2021 Dec;63(12):1235-1243. doi: 10.1007/s12033-021-00375-y. Epub 2021 Aug 2. PMID: 34338995; DOI: 10.1007/s12033-021-00375-y; https://pubmed.ncbi.nlm.nih.gov/34338995/ (local files: wu-2021-fbxl20-mir195-ovarian-abstract.md, wu-2021-fbxl20-mir195-ovarian-summary.md)
* **xiao-2015-fbxl20-vps34**: Xiao J(1), Zhang T(1), Xu D(1), Wang H(1), Cai Y(1), Jin T(1), Liu M(1), Jin M(2), Wu K(1), Yuan J(3). FBXL20-mediated Vps34 ubiquitination as a p53 controlled checkpoint in regulating autophagy and receptor degradation. Genes Dev. 2015 Jan 15;29(2):184-96. doi: 10.1101/gad.252528.114. PMID: 25593308; PMCID: PMC4298137; DOI: 10.1101/gad.252528.114; https://pubmed.ncbi.nlm.nih.gov/25593308/ (local files: xiao-2015-fbxl20-vps34-abstract.md, xiao-2015-fbxl20-vps34-fulltext.txt, xiao-2015-fbxl20-vps34-summary.md)
* **yao-2007-scrapper-rim1**: Yao I(1), Takagi H, Ageta H, Kahyo T, Sato S, Hatanaka K, Fukuda Y, Chiba T, Morone N, Yuasa S, Inokuchi K, Ohtsuka T, Macgregor GR, Tanaka K, Setou M. SCRAPPER-dependent ubiquitination of active zone protein RIM1 regulates synaptic vesicle release. Cell. 2007 Sep 7;130(5):943-57. doi: 10.1016/j.cell.2007.06.052. PMID: 17803915; PMCID: PMC3049808; DOI: 10.1016/j.cell.2007.06.052; https://pubmed.ncbi.nlm.nih.gov/17803915/ (local files: yao-2007-scrapper-rim1-abstract.md, yao-2007-scrapper-rim1-summary.md)
* **yao-2008-scrapper-ims**: Yao I(1), Sugiura Y, Matsumoto M, Setou M. In situ proteomics with imaging mass spectrometry and principal component analysis in the Scrapper-knockout mouse brain. Proteomics. 2008 Sep;8(18):3692-701. doi: 10.1002/pmic.200701121. PMID: 18780397; DOI: 10.1002/pmic.200701121; https://pubmed.ncbi.nlm.nih.gov/18780397/ (local files: yao-2008-scrapper-ims-abstract.md, yao-2008-scrapper-ims-summary.md)
* **yao-2011-scrapper-behavior**: Yao I(1), Takao K, Miyakawa T, Ito S, Setou M. Synaptic E3 ligase SCRAPPER in contextual fear conditioning: extensive behavioral phenotyping of Scrapper heterozygote and overexpressing mutant mice. PLoS One. 2011 Feb 24;6(2):e17317. doi: 10.1371/journal.pone.0017317. PMID: 21390313; PMCID: PMC3044740; DOI: 10.1371/journal.pone.0017317; https://pubmed.ncbi.nlm.nih.gov/21390313/ (local files: yao-2011-scrapper-behavior-abstract.md, yao-2011-scrapper-behavior-fulltext.txt, yao-2011-scrapper-behavior-summary.md)
* **zhu-2014-fbxl20-ecadherin**: Zhu J(1), Deng S(1), Duan J(2), Xie X(1), Xu S(1), Ran M(1), Dai X(1), Pu Y(3), Zhang X(3). FBXL20 acts as an invasion inducer and mediates E-cadherin in colorectal adenocarcinoma. Oncol Lett. 2014 Jun;7(6):2185-2191. doi: 10.3892/ol.2014.2031. Epub 2014 Apr 3. PMID: 24932313; PMCID: PMC4049678; DOI: 10.3892/ol.2014.2031; https://pubmed.ncbi.nlm.nih.gov/24932313/ (local files: zhu-2014-fbxl20-ecadherin-abstract.md, zhu-2014-fbxl20-ecadherin-summary.md)

Database records: UniProtKB A0A9L0IQA3 (https://rest.uniprot.org/uniprotkb/A0A9L0IQA3.txt); UniProtKB Q96IG2 human FBXL20 (https://rest.uniprot.org/uniprotkb/Q96IG2.txt); UniProtKB Q9CZV8 mouse Fbxl20; UniProtKB Q9UKC9 human FBXL2. Sequence comparison: SEQUENCE_NOTES.md (own analysis).


## Citations

1. dobie-2007-scrapper-trashes-rim-abstract.md
2. dobie-2007-scrapper-trashes-rim-summary.md
3. eisfeld-2012-mir3151-baalc-abstract.md
4. eisfeld-2012-mir3151-baalc-summary.md
5. eto-2020-scrapper-glutamate-gaba-abstract.md
6. eto-2020-scrapper-glutamate-gaba-fulltext.txt
7. eto-2020-scrapper-glutamate-gaba-summary.md
8. fu-2016-fbxl20-epilepsy-abstract.md
9. fu-2016-fbxl20-epilepsy-summary.md
10. kim-2017-cfl1-celegans-abstract.md
11. kim-2017-cfl1-celegans-fulltext.txt
12. kim-2017-cfl1-celegans-summary.md
13. koga-2017-scrapper-acc-abstract.md
14. koga-2017-scrapper-acc-summary.md
15. kuchay-2019-ggtase3-abstract.md
16. kuchay-2019-ggtase3-fulltext.txt
17. kuchay-2019-ggtase3-summary.md
18. liang-2023-palmitoylation-pde6d-abstract.md
19. liang-2023-palmitoylation-pde6d-fulltext.txt
20. liang-2023-palmitoylation-pde6d-summary.md
21. madduri-2021-fbxl20-pr55a-abstract.md
22. madduri-2021-fbxl20-pr55a-fulltext.txt
23. madduri-2021-fbxl20-pr55a-summary.md
24. manne-2021-fbxl20-puma-bax-abstract.md
25. manne-2021-fbxl20-puma-bax-fulltext.txt
26. manne-2021-fbxl20-puma-bax-summary.md
27. skaar-2013-fbox-substrate-recruitment-abstract.md
28. skaar-2013-fbox-substrate-recruitment-fulltext.txt
29. skaar-2013-fbox-substrate-recruitment-summary.md
30. sun-2022-fbxl20-41bb-abstract.md
31. sun-2022-fbxl20-41bb-summary.md
32. takagi-2012-scrapper-ltp-abstract.md
33. takagi-2012-scrapper-ltp-fulltext.txt
34. takagi-2012-scrapper-ltp-summary.md
35. wang-2005-fbl2-geranylgeranylated-abstract.md
36. wang-2005-fbl2-geranylgeranylated-summary.md
37. wang-2020-donkey-genomes-abstract.md
38. wang-2020-donkey-genomes-summary.md
39. wang-2024-fbxl20-depression-abstract.md
40. wang-2024-fbxl20-depression-summary.md
41. wu-2021-fbxl20-mir195-ovarian-abstract.md
42. wu-2021-fbxl20-mir195-ovarian-summary.md
43. xiao-2015-fbxl20-vps34-abstract.md
44. xiao-2015-fbxl20-vps34-fulltext.txt
45. xiao-2015-fbxl20-vps34-summary.md
46. yao-2007-scrapper-rim1-abstract.md
47. yao-2007-scrapper-rim1-summary.md
48. yao-2008-scrapper-ims-abstract.md
49. yao-2008-scrapper-ims-summary.md
50. yao-2011-scrapper-behavior-abstract.md
51. yao-2011-scrapper-behavior-fulltext.txt
52. yao-2011-scrapper-behavior-summary.md
53. zhu-2014-fbxl20-ecadherin-abstract.md
54. zhu-2014-fbxl20-ecadherin-summary.md