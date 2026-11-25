---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:43:59.403979'
end_time: '2026-10-26T01:56:29.490297'
duration_seconds: 750.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: CTDSP2
  gene_symbol: CTDSP2
  uniprot_accession: F7A4N8
  protein_description: 'SubName: Full=CTD small phosphatase 2 {ECO:0000313|Ensembl:ENSECAP00000016443.3};'
  gene_info: Name=CTDSP2 {ECO:0000313|VGNC:VGNC:16932};
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: Not specified in UniProt
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
citation_count: 63
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** F7A4N8
- **Protein Description:** SubName: Full=CTD small phosphatase 2 {ECO:0000313|Ensembl:ENSECAP00000016443.3};
- **Gene Information:** Name=CTDSP2 {ECO:0000313|VGNC:VGNC:16932};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Not specified in UniProt

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CTDSP2" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CTDSP2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CTDSP2** (gene ID: CTDSP2, UniProt: F7A4N8) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# CTDSP2 (Small CTD Phosphatase 2, SCP2/OS4) in the Horse: Function, Localization and Pathways of UniProt F7A4N8

## 1. Introduction and Summary

CTDSP2 (carboxy-terminal domain RNA polymerase II polypeptide A small phosphatase 2) belongs to a family of three small vertebrate CTD phosphatases. Its paralogues are CTDSP1/SCP1 and CTDSPL/SCP3. The family was defined as Mg2+-dependent phosphatases that prefer the phospho-Ser5 mark in the heptad repeats (YSPTSPS) of the C-terminal domain (CTD) of the largest RNA polymerase II subunit [yeo-2003-scp-ctd-phosphatase-abstract; zhang-2006-scp1-ctd-structure-abstract]. The human gene was first cloned as *OS4*, a highly conserved gene co-amplified with *CDK4* on 12q13-q15 in sarcomas [su-1997-os4-sarcoma-abstract]. Its Xenopus orthologue was isolated because it could induce a secondary dorsal axis [zohn-2001-xenopus-os4-abstract]. Two decades of work in human cells, Xenopus, zebrafish and mouse show that CTDSP2 is a nuclear protein serine/threonine phosphatase (EC 3.1.3.16) with several substrates. It dephosphorylates RNAPII CTD Ser5 and acts as a co-repressor recruited by REST/NRSF to silence neuronal genes in non-neuronal cells [yeo-2005-scp-neuronal-silencing-abstract]. It limits steroid-receptor-driven promoter clearance [thompson-2006-scp2-androgen-abstract]. It dephosphorylates the C-terminal SXS motif and the linker region of receptor-regulated Smads, which attenuates BMP–Smad1 signalling and enhances TGF-β–Smad2/3 signalling [knockaert-2006-scp-smad1-bmp-abstract; sapkota-2006-scp-smad-linker-abstract; wrighton-2006-scp-smad2-3-linker-abstract]. It restrains the G1/S transition by promoting hypophosphorylation of pRb and induction of p21Cip1/Waf1 [zhu-2012-mir26-host-genes-prb-fulltext; kloet-2015-ctdsp2-foxo-ras-p21-fulltext; krasnov-2019-scp-nsclc-fulltext]. *CTDSP2* also hosts an intronic miR-26 locus, and in zebrafish this microRNA represses its own host transcript to allow neurogenesis [zhu-2012-mir26-host-genes-prb-fulltext; dill-2012-mir26b-ctdsp2-abstract].

One identity issue must be stated first. The horse gene symbol *CTDSP2* (VGNC:16932) is assigned correctly, and the full-length horse CTDSP2 isoforms are almost identical to human CTDSP2. The specific UniProt entry F7A4N8, however, is a 174-residue product of an alternatively spliced Ensembl transcript (ENSECAT00000020049). It keeps only the N-terminal ~84 residues of CTDSP2 and then runs into an unrelated 90-residue tail. It lacks the entire FCP1/HAD catalytic domain, including the DXDXT nucleophile motif (Section 2; SEQUENCE_ANALYSIS.md). NCBI RefSeq, by contrast, models the horse protein as a 271-residue isoform (XP_023499666) that is 98.5% identical to human CTDSP2. No horse-specific experimental literature on CTDSP2 was found (a PubMed search for "CTDSP2 horse" returned no records). The alias SCP2 is itself ambiguous, because it is also the official symbol of the unrelated lipid-transfer protein sterol carrier protein-2 [suo-2023-scp2-sterol-carrier-alias-abstract]. Literature retrieved under that alias was screened, and papers about sterol carrier protein-2 were excluded. Everything below about catalytic and pathway function therefore applies to the full-length horse CTDSP2 gene product by orthology. It cannot be assumed for the truncated F7A4N8 polypeptide, which is predicted to be catalytically inactive and may not accumulate as a stable protein.

## 2. Gene Identity, Orthology and the Nature of the F7A4N8 Isoform

UniProt F7A4N8 is an unreviewed TrEMBL entry (protein existence level 4, "predicted"). Its sequence comes from the Thoroughbred reference genome [wade-2009-horse-genome-abstract] via Ensembl gene ENSECAG00000018788 on horse chromosome 6. The entry carries no family or domain annotation beyond a disordered, low-complexity region at residues 111-135. I compared it with reviewed human CTDSP2 (UniProt O14595, 271 aa) and with all three horse Ensembl transcripts (SEQUENCE_ANALYSIS.md). F7A4N8 residues 1-84 are identical to human CTDSP2 at 81 of 84 positions. At residue 85, human CTDSP2 continues into the segment that leads to the FCP1 homology domain (human residues 97-255). That domain holds the catalytic Asp107 (the aspartyl-phosphate nucleophile), Asp109 (the proton donor) and Asp218, which together coordinate Mg2+ in the crystal structure of the human catalytic domain (PDB 2Q5E) [almo-2007-structural-genomics-phosphatases-abstract]. F7A4N8 contains none of this. The exon structure shows why. ENSECAT00000020049 uses an upstream alternative 3' splice acceptor that extends one internal exon by about 270 nt of intronic sequence, and the open reading frame ends inside this extension. Several exons follow the stop codon, so the transcript has the features of a nonsense-mediated decay substrate. That is my inference; no transcript-level experiment on the horse gene exists.

The horse gene also encodes full-length products. The Ensembl canonical transcript (ENSECAT00000107019, 312 aa, including an N-terminal extension of uncertain validity) contains the complete FCP1 domain with the DLDET catalytic motif. Its catalytic region is virtually identical to human CTDSP2. A third isoform (252 aa) has a small internal deletion inside the FCP1 domain. NCBI's independent gene annotation agrees with the full-length interpretation. RefSeq predicts horse CTDSP2 isoform X1 (XP_023499666.1, 271 aa), which has exactly the length of human CTDSP2 and is identical to it at 267 of 271 positions. It also predicts isoform X2 (XP_023499667.1, 258 aa), which lacks a 13-residue segment equivalent to human residues 55-67 but keeps the whole catalytic domain. No RefSeq or GenBank model corresponds to the 174-residue F7A4N8 product (SEQUENCE_ANALYSIS.md). The truncated form therefore appears only in the Ensembl gene build, and the 271-residue isoform X1 is the best representative of the horse CTDSP2 enzyme. The gene symbol is therefore unambiguous, and the horse *CTDSP2* locus is the true orthologue of human *CTDSP2*/*OS4*. Literature on this gene from human, mouse, Xenopus and zebrafish applies to the horse gene. What differs is the gene product represented by F7A4N8. Sequence evidence suggests it cannot carry out the phosphatase reactions described below. Its N-terminal segment is a basic, Cys-containing, non-catalytic region that is conserved across species.

## 3. Catalytic Mechanism and Substrate Specificity

The SCP family belongs to the FCP/SCP branch of the haloacid dehalogenase (HAD) superfamily. These are Mg2+-dependent phosphoserine/phosphothreonine-specific protein phosphatases [zhang-2006-scp1-ctd-structure-abstract]. Within that branch, SCP1, SCP2 and SCP3 form a small-CTD-phosphatase subfamily defined by the DXDX(T/V) motif, together with more distant members such as TIMM50 and UBLCP1. Mutagenesis showed that the DXDX motif is what mediates phosphatase activity [r-2014-scp1-review-fulltext]. The reaction is protein-O-phospho-L-serine (or -threonine) + H2O → protein-L-serine (or -threonine) + phosphate. It proceeds through an aspartyl-phosphate intermediate on the first Asp of the DXDX(T/V) motif. A substrate-trapping mutation at this residue (D96N in SCP1) gives a dominant-negative enzyme. This mutant made it possible to crystallize SCP1 bound to mono- and diphosphorylated CTD heptad peptides, which revealed the residues that confer the preference for phospho-Ser5 [zhang-2006-scp1-ctd-structure-abstract]. The equivalent catalytic aspartates in CTDSP2 (Asp107, Asp109) and the Mg2+ ligand Asp218 come from the human CTDSP2 catalytic-domain structure solved by structural genomics [almo-2007-structural-genomics-phosphatases-abstract]. The importance of the motif is underlined by a de novo human variant, p.T111N, found in two unrelated probands with hemifacial microsomia. It changes the conserved threonine of the DLDET motif and was predicted to be damaging [xia-2025-ctdsp2-zebrafish-p53-fulltext].

The first defined substrate was the RNAPII CTD. SCPs preferentially remove phosphate from Ser5 rather than Ser2. For SCP1, the preferred substrate is RNAPII phosphorylated by TFIIH, and the activity is stimulated by the RAP74 subunit of TFIIF [yeo-2003-scp-ctd-phosphatase-abstract]. The wider substrate range found later is notable because it consists largely of proline-directed phosphosites, which match the Ser-Pro context of CTD Ser5. These substrates include the C-terminal SXS motif of Smad1 [knockaert-2006-scp-smad1-bmp-abstract], the MAPK/CDK-targeted linker regions of Smad1, Smad2 and Smad3 [sapkota-2006-scp-smad-linker-abstract; wrighton-2006-scp-smad2-3-linker-abstract], GSK-3β sites in Snail [wu-2009-scp-snail-abstract], the Pin1-recognized Ser518 of the tumour suppressor PML (shown for SCP1 and reported also for SCP2 and SCP3; dephosphorylation blocks KLHL20-mediated ubiquitination and degradation of PML and thereby restrains mTOR–HIF signalling) [lin-2014-scp-pml-ccrcc-abstract], and the ERK/Pin1 phosphodegron of REST (shown for CTDSP1) [nesti-2014-ctdsp1-rest-stability-abstract; burkholder-2018-scp1-rest-abstract]. Reviews list additional SCP substrates, including AKT1, TWIST1, c-MYC, Ras-family proteins, CDCA3, p21 and PML. For many of these, evidence that CTDSP2 itself acts on them is indirect [puzanov-2021-scp-oncogenesis-review-abstract]. For CTDSP2 specifically, direct experimental support exists for the RNAPII CTD (by family membership and promoter Ser5 kinetics) [yeo-2003-scp-ctd-phosphatase-abstract; thompson-2006-scp2-androgen-abstract], for Smad1 and Smad2/3 [knockaert-2006-scp-smad1-bmp-abstract; sapkota-2006-scp-smad-linker-abstract; wrighton-2006-scp-smad2-3-linker-abstract], and for phosphatase-dependent reduction of pRb phosphorylation in cells [kloet-2015-ctdsp2-foxo-ras-p21-fulltext; krasnov-2019-scp-nsclc-fulltext].

## 4. Nuclear Function in RNA Polymerase II Transcription and Neuronal Gene Silencing

In its best-established role, CTDSP2 represses transcription by acting on the RNAPII CTD at specific promoters. Expressing an SCP inhibits activated transcription from several promoters, whereas a phosphatase-dead mutant enhances it. This led to the proposal that SCPs gate the transition from initiation and capping (marked by Ser5 phosphorylation) to processive elongation [yeo-2003-scp-ctd-phosphatase-abstract]. Yeo and colleagues then showed that the repressor REST/NRSF recruits SCP1-3 to RE-1-containing neuronal genes in non-neuronal cells, and that their expression is restricted to non-neuronal tissues. Phosphatase-inactive SCPs interfered with REST-mediated silencing and promoted neuronal differentiation of P19 embryonal carcinoma cells. RNAi against the single Drosophila SCP unmasked neuronal gene expression in S2 cells, which shows the mechanism is evolutionarily conserved [yeo-2005-scp-neuronal-silencing-abstract]. In this model CTDSP2 is a catalytic effector of the REST co-repressor machinery. It keeps RNAPII at neuronal genes in a Ser5-hypophosphorylated, non-productive state.

CTDSP2 also restrains signal-induced transcription by nuclear hormone receptors. SCP2 was identified as an androgen receptor (AR)-interacting protein. SCP1, SCP2 and SCP3 each attenuated AR transactivation, and they were recruited to the PSA promoter in an androgen- and AR-dependent manner. Silencing SCP2 increased AR and glucocorticoid receptor loading at PSA regulatory elements. It also led to earlier and stronger recruitment and cycling of RNAPII, and Ser5 CTD phosphorylation appeared significantly earlier at the promoter. The authors concluded that SCP2 acts in promoter clearance during steroid-activated transcription [thompson-2006-scp2-androgen-abstract]. Together these studies place CTDSP2 on chromatin at selected promoters, brought there by sequence-specific transcription factors (REST, AR), where it limits Ser5 phosphorylation of RNAPII.

## 5. Role in TGF-β/BMP–Smad Signalling

The second major pathway role of CTDSP2 is as a nuclear Smad phosphatase. Receptor-regulated Smads are activated when TGF-β or BMP receptors phosphorylate their C-terminal SXS motif. Their activity is also tuned by MAPK, CDK and GSK3 phosphorylation of the linker region. Knockaert and colleagues showed that Xenopus SCP2/Os4 inhibits BMP activity in presumptive ectoderm and causes neuralization. In embryos, SCP2/Os4 and human SCP1-3 selectively dephosphorylated Smad1 over Smad2, inhibited BMP/Smad1-dependent transcription and induced a secondary dorsal axis. In human cells, depleting SCP1 and SCP2 increased the extent and duration of BMP-induced Smad1 C-terminal phosphorylation and strengthened endogenous BMP target-gene responses [knockaert-2006-scp-smad1-bmp-abstract]. This gave a mechanism for the axis-inducing activity originally reported for XOs4. Zohn and colleagues had concluded that XOs4 did not inhibit BMP signalling in dissociated animal caps and attributed its effects to mesoderm induction [zohn-2001-xenopus-os4-abstract]. The later Smad1-phosphatase data therefore revise that earlier view.

Two studies published in the same period extended the substrate range to the Smad linker. SCP1-3 dephosphorylated the linker regions of Smad1, Smad2 and Smad3 in vitro, in mammalian cells and in Xenopus. SCP1/2 knockdown increased BMP-dependent phosphorylation of both the Smad1 linker and C-terminus, but increased only the linker (inhibitory) phosphorylation of Smad2/3, not the C-terminal (activating) phosphorylation. The functional result was asymmetric: SCPs enhance TGF-β transcriptional responses and reset Smad1 to its basal unphosphorylated state [sapkota-2006-scp-smad-linker-abstract]. Independently, a functional genomic screen found SCP1 to be a Smad2/3 linker and N-terminal phosphatase, with SCP2 and SCP3 (but not FCP1) showing the same activity. Depleting SCP1/2/3 enhanced linker phosphorylation [wrighton-2006-scp-smad2-3-linker-abstract]. CTDSP2 thus sits at a point of cross-talk between growth-factor kinase signalling and TGF-β-family signalling. In the nucleus it removes inhibitory linker marks and terminates BMP–Smad1 activation.

## 6. Cell-Cycle Control, Growth Signalling and Developmental Phenotypes

Several independent studies link CTDSP2 to the G1/S checkpoint. CTDSP1, CTDSP2 and CTDSPL rise in quiescent cells and fall during proliferation, both in serum-stimulated primary fibroblasts and in regenerating mouse liver. Together with their intronic miR-26a/b, they reduce pRb phosphorylation and block G1/S progression [zhu-2012-mir26-host-genes-prb-fulltext]. Kloet and colleagues found *CTDSP2* in a core set of genes regulated by FOXO transcription factors and by PI3K-PKB/Akt, and validated it as a direct FOXO target. Inducible wild-type CTDSP2, but not a phosphatase-dead mutant, reduced S-phase entry and Rb phosphorylation in U2OS and RPE cells. It also produced a phosphatase-dependent change in cell-cycle gene expression, most strongly induction of the CDK inhibitor p21Cip1/Waf1 and of E2F7 [kloet-2015-ctdsp2-foxo-ras-p21-fulltext]. p21 was partly required for the arrest and reduced cyclin E–CDK2 activity. The proposed route to p21 is unexpected: CTDSP2 increases Ras-GTP levels. Inhibiting either p53 or MEK blunted p21 induction by CTDSP2, and depleting endogenous CTDSP2 lowered Ras activity [kloet-2015-ctdsp2-foxo-ras-p21-abstract; kloet-2015-ctdsp2-foxo-ras-p21-fulltext]. The direct phosphoprotein substrate responsible for Ras activation was not identified.

In A549 lung adenocarcinoma cells, overexpressing any of the three CTDSPs slowed growth, induced senescence and increased the active, hypophosphorylated form of Rb at Ser807/811, Ser780 and Ser795. CTDSPs and *RB1* were concordantly downregulated in primary non-small-cell lung cancers [krasnov-2019-scp-nsclc-abstract]. This anti-proliferative activity depends on context. In Caki-1 renal carcinoma cells, CTDSP1 and CTDSPL inhibited growth but CTDSP2 did not, although low expression of all three was associated with poor survival in TCGA data [krasnov-2023-scp-ccrcc-abstract]. The oncology picture is also mixed. *CTDSP2/OS4* is co-amplified with *CDK4* in sarcomas [su-1997-os4-sarcoma-abstract] and appears as a fusion partner (CTDSP2::GLI1) in glial tumours [kanathanavanich-2024-ctdsp2-gli1-fusion-abstract]. Being part of these 12q amplicons and rearrangements probably reflects genomic position next to known drivers rather than oncogenic activity of CTDSP2 itself.

Vertebrate genetics adds an in vivo developmental role. In mouse embryonic cortex, Ctdsp2 and its intronic miR-26 both promote neural progenitor proliferation [zhang-2018-mir26-ctdsp-emx2-abstract]. CRISPR knockout of *ctdsp2* in zebrafish caused craniofacial cartilage dysplasia that resembles hemifacial microsomia. It was accompanied by abnormal proliferation and apoptosis of cranial neural crest cells in the pharyngeal arches, impaired chondrocyte differentiation and upregulation of p53-pathway genes. Both *ctdsp2* mRNA injection and *tp53* knockout rescued the cartilage phenotype [xia-2025-ctdsp2-zebrafish-p53-fulltext]. The direction of the p53 effect here (loss of ctdsp2 activates p53) appears opposite to the p53-dependent p21 induction caused by CTDSP2 overexpression in human cells [kloet-2015-ctdsp2-foxo-ras-p21-fulltext]. This suggests that CTDSP2 dosage feeds into p53 signalling in a cell-type-dependent way.

## 7. Regulation of CTDSP2 Expression: FOXO, c-Myc and the Intronic miR-26 Feedback Loop

Growth signalling regulates *CTDSP2* expression. FOXO factors activate it, and PI3K-PKB/Akt signalling therefore represses it [kloet-2015-ctdsp2-foxo-ras-p21-abstract]. c-Myc lowers it, together with the other CTDSPs and their intronic miRNAs [zhu-2012-mir26-host-genes-prb-fulltext]. Expression is also controlled by the intronic microRNA. In the human genome the three miR-26 loci lie in introns of *CTDSPL* (miR-26a-1), *CTDSP2* (miR-26a-2) and *CTDSP1* (miR-26b) [zhu-2012-mir26-host-genes-prb-fulltext]. In zebrafish, *ctdsp2* hosts miR-26b, which targets the ctdsp2 transcript itself. In neural stem cells this negative feedback loop is held inactive because miR-26b processing is blocked at the precursor stage. During neurogenesis, mature miR-26b is produced, suppresses Ctdsp2 protein and is required for neuronal differentiation in vivo [dill-2012-mir26b-ctdsp2-abstract; han-2012-mir26b-ctdsp2-preview-abstract]. Later work in mouse ES cells showed that the miR-26 family also directly targets *Rest*, which derepresses REST-silenced neuronal genes and miRNAs [sauer-2021-mir26-rest-abstract]. The host-gene/miRNA module thus switches off both the REST scaffold and its CTDSP effector at the onset of neurogenesis. This fits the original observation that SCP expression is restricted to non-neuronal tissues [yeo-2005-scp-neuronal-silencing-abstract]. Whether the alternatively spliced horse transcript behind F7A4N8 represents an extra layer of regulation, such as unproductive splicing coupled to NMD, has not been studied.

## 8. Subcellular Localization

The evidence consistently places CTDSP2 in the nucleus, specifically on chromatin at regulated promoters. SCPs were described as a family of nuclear phosphatases that act on nuclear, receptor-activated Smad1 [knockaert-2006-scp-smad1-bmp-abstract]. ChIP showed SCP2 recruited to the PSA promoter in an androgen- and AR-dependent manner [thompson-2006-scp2-androgen-abstract]. SCPs are recruited by REST to RE-1-containing neuronal genes [yeo-2005-scp-neuronal-silencing-abstract]. A family member co-localizes with Snail in the nucleus [wu-2009-scp-snail-abstract]. The SCP-stabilized tumour suppressor PML is also a nuclear protein [lin-2014-scp-pml-ccrcc-abstract]. These locations fit its main substrates, which are chromatin-engaged RNAPII and nuclear phospho-Smads. The Ras-activating function in the FOXO study [kloet-2015-ctdsp2-foxo-ras-p21-fulltext] implies a possible non-nuclear or indirect action, but no cytoplasmic or membrane pool of CTDSP2 has been shown. The localization of the truncated F7A4N8 product is unknown. It contains the conserved N-terminus but no catalytic domain, and no study has addressed it.

## 9. Open Questions

The most immediate question for this UniProt entry is whether F7A4N8 exists as a protein. The ENSECAT00000020049 transcript should be checked against horse RNA-seq for junction support of the intron-extending acceptor, and tested for NMD sensitivity. Proteomic evidence for the unique 90-residue tail would settle whether a polypeptide accumulates. If it does, it could compete with full-length CTDSP2 for partners that bind its N-terminus. A second question is what the conserved N-terminal ~85 residues do. This region is nearly invariant between horse and human. It may mediate recruitment by REST, AR or other partners, but this has not been mapped for CTDSP2. Third, the direct substrate behind Ras activation and p21 induction by CTDSP2 is unknown, and so is the reason ctdsp2 loss activates p53 in zebrafish neural crest. Phosphoproteomics after acute CTDSP2 depletion would address both. Fourth, CTDSP1, CTDSP2 and CTDSPL overlap heavily, so most loss-of-function studies (such as SCP1/2 double knockdown) cannot assign non-redundant functions. The unique craniofacial phenotype of the zebrafish *ctdsp2* knockout and the human p.T111N variant suggest that CTDSP2 has dose-sensitive roles that are worth testing in mammalian models. It is also unclear which of the many family-level substrates, such as PML S518, Snail and the REST degron, CTDSP2 acts on at physiological levels rather than only on overexpression, because most of these studies focused on SCP1 [lin-2014-scp-pml-ccrcc-abstract; nesti-2014-ctdsp1-rest-stability-abstract]. Finally, no equine experimental data exist at all. Expression data (Bgee lists high expression in synovial membrane) could be followed up in the context of equine joint biology and TGF-β/BMP signalling in cartilage, given the chondrocyte phenotype in zebrafish.

## 10. References

- [almo-2007-structural-genomics-phosphatases] Almo SC, Bonanno JB, Sauder JM, Emtage S, Dilorenzo TP, Malashkevich V, et al.. Structural genomics of protein phosphatases. Journal of structural and functional genomics 2007;8(2-3):121-40. PMID: 18058037; PMCID: PMC4163028; DOI: 10.1007/s10969-007-9036-1. https://pubmed.ncbi.nlm.nih.gov/18058037/
- [burkholder-2018-scp1-rest] Burkholder NT, Mayfield JE, Yu X, Irani S, Arce DK, Jiang F, et al.. Phosphatase activity of small C-terminal domain phosphatase 1 (SCP1) controls the stability of the key neuronal regulator RE1-silencing transcription factor (REST). The Journal of biological chemistry 2018;293(43):16851-16861. PMID: 30217818; PMCID: PMC6204920; DOI: 10.1074/jbc.RA118.004722. https://pubmed.ncbi.nlm.nih.gov/30217818/
- [dill-2012-mir26b-ctdsp2] Dill H, Linder B, Fehr A, Fischer U. Intronic miR-26b controls neuronal differentiation by repressing its host transcript, ctdsp2. Genes & development 2012;26(1):25-30. PMID: 22215807; PMCID: PMC3258962; DOI: 10.1101/gad.177774.111. https://pubmed.ncbi.nlm.nih.gov/22215807/
- [han-2012-mir26b-ctdsp2-preview] Han J, Denli AM, Gage FH. The enemy within: intronic miR-26b represses its host gene, ctdsp2, to regulate neurogenesis. Genes & development 2012;26(1):6-10. PMID: 22215805; PMCID: PMC3258967; DOI: 10.1101/gad.184416.111. https://pubmed.ncbi.nlm.nih.gov/22215805/
- [kanathanavanich-2024-ctdsp2-gli1-fusion] Kanathanavanich M, Koga S, Stone SL, Roth J, Abdullaev Z, O'Rourke DM, et al.. CTDSP2::GLI1 fusion in glioblastoma: A diagnostic challenge through tumor heterogeneity. Journal of neuropathology and experimental neurology 2024;83(12):1076-1080. PMID: 38981111; PMCID: PMC12104509; DOI: 10.1093/jnen/nlae073. https://pubmed.ncbi.nlm.nih.gov/38981111/
- [kloet-2015-ctdsp2-foxo-ras-p21] Kloet DE, Polderman PE, Eijkelenboom A, Smits LM, van Triest MH, van den Berg MC, et al.. FOXO target gene CTDSP2 regulates cell cycle progression through Ras and p21(Cip1/Waf1). The Biochemical journal 2015;469(2):289-98. PMID: 25990325; PMCID: PMC4613505; DOI: 10.1042/BJ20140831. https://pubmed.ncbi.nlm.nih.gov/25990325/
- [knockaert-2006-scp-smad1-bmp] Knockaert M, Sapkota G, Alarcón C, Massagué J, Brivanlou AH. Unique players in the BMP pathway: small C-terminal domain phosphatases dephosphorylate Smad1 to attenuate BMP signaling. Proceedings of the National Academy of Sciences of the United States of America 2006;103(32):11940-5. PMID: 16882717; PMCID: PMC1567677; DOI: 10.1073/pnas.0605133103. https://pubmed.ncbi.nlm.nih.gov/16882717/
- [krasnov-2019-scp-nsclc] Krasnov GS, Puzanov GA, Afanasyeva MA, Dashinimaev EB, Vishnyakova KS, Beniaminov AD, et al.. Tumor suppressor properties of the small C-terminal domain phosphatases in non-small cell lung cancer. Bioscience reports 2019;39(12). PMID: 31774910; PMCID: PMC6911153; DOI: 10.1042/BSR20193094. https://pubmed.ncbi.nlm.nih.gov/31774910/
- [krasnov-2023-scp-ccrcc] Krasnov GS, Puzanov GA, Dashinimaev EB, Vishnyakova KS, Kondratieva TT, Chegodaev YS, et al.. Tumor Suppressor Properties of Small C-Terminal Domain Phosphatases in Clear Cell Renal Cell Carcinoma. International journal of molecular sciences 2023;24(16). PMID: 37629167; PMCID: PMC10455398; DOI: 10.3390/ijms241612986. https://pubmed.ncbi.nlm.nih.gov/37629167/
- [lin-2014-scp-pml-ccrcc] Lin YC, Lu LT, Chen HY, Duan X, Lin X, Feng XH, et al.. SCP phosphatases suppress renal cell carcinoma by stabilizing PML and inhibiting mTOR/HIF signaling. Cancer research 2014;74(23):6935-46. PMID: 25293974; DOI: 10.1158/0008-5472.CAN-14-1330. https://pubmed.ncbi.nlm.nih.gov/25293974/
- [nesti-2014-ctdsp1-rest-stability] Nesti E, Corson GM, McCleskey M, Oyer JA, Mandel G. C-terminal domain small phosphatase 1 and MAP kinase reciprocally control REST stability and neuronal differentiation. Proceedings of the National Academy of Sciences of the United States of America 2014;111(37):E3929-36. PMID: 25197063; PMCID: PMC4169941; DOI: 10.1073/pnas.1414770111. https://pubmed.ncbi.nlm.nih.gov/25197063/
- [puzanov-2021-scp-oncogenesis-review] Puzanov GA, Senchenko VN. [SCP Phosphatases and Oncogenesis]. Molekuliarnaia biologiia 2021;55(4):531-542. PMID: 34432772; DOI: 10.31857/S0026898421040091. https://pubmed.ncbi.nlm.nih.gov/34432772/
- [r-2014-scp1-review] R HR, Kim H, Noh K, Kim YJ. The diverse roles of RNA polymerase II C-terminal domain phosphatase SCP1. BMB reports 2014;47(4):192-6. PMID: 24755554; PMCID: PMC4163886; DOI: 10.5483/bmbrep.2014.47.4.060. https://pubmed.ncbi.nlm.nih.gov/24755554/
- [sapkota-2006-scp-smad-linker] Sapkota G, Knockaert M, Alarcón C, Montalvo E, Brivanlou AH, Massagué J. Dephosphorylation of the linker regions of Smad1 and Smad2/3 by small C-terminal domain phosphatases has distinct outcomes for bone morphogenetic protein and transforming growth factor-beta pathways. The Journal of biological chemistry 2006;281(52):40412-9. PMID: 17085434; DOI: 10.1074/jbc.M610172200. https://pubmed.ncbi.nlm.nih.gov/17085434/
- [sauer-2021-mir26-rest] Sauer M, Was N, Ziegenhals T, Wang X, Hafner M, Becker M, et al.. The miR-26 family regulates neural differentiation-associated microRNAs and mRNAs by directly targeting REST. Journal of cell science 2021;134(12). PMID: 34151974; PMCID: PMC11443607; DOI: 10.1242/jcs.257535. https://pubmed.ncbi.nlm.nih.gov/34151974/
- [su-1997-os4-sarcoma] Su YA, Lee MM, Hutter CM, Meltzer PS. Characterization of a highly conserved gene (OS4) amplified with CDK4 in human sarcomas. Oncogene 1997;15(11):1289-94. PMID: 9315096; DOI: 10.1038/sj.onc.1201294. https://pubmed.ncbi.nlm.nih.gov/9315096/
- [suo-2023-scp2-sterol-carrier-alias] Suo Q, Sun X, Zhang Y, Wang Y, Liu K, Yang H, et al.. [Prokaryotic expression, polyclonal antibody preparation, spatio-temporal expression profile and functional analysis of c-Myc of Helicoverpa armigera (Lepidoptera: Noctuidae)]. Sheng wu gong cheng xue bao = Chinese journal of biotechnology 2023;39(7):2730-2742. PMID: 37584128; DOI: 10.13345/j.cjb.220764. https://pubmed.ncbi.nlm.nih.gov/37584128/
- [thompson-2006-scp2-androgen] Thompson J, Lepikhova T, Teixido-Travesa N, Whitehead MA, Palvimo JJ, Jänne OA. Small carboxyl-terminal domain phosphatase 2 attenuates androgen-dependent transcription. The EMBO journal 2006;25(12):2757-67. PMID: 16724108; PMCID: PMC1500849; DOI: 10.1038/sj.emboj.7601161. https://pubmed.ncbi.nlm.nih.gov/16724108/
- [wade-2009-horse-genome] Wade CM, Giulotto E, Sigurdsson S, Zoli M, Gnerre S, Imsland F, et al.. Genome sequence, comparative analysis, and population genetics of the domestic horse. Science (New York, N.Y.) 2009;326(5954):865-7. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158. https://pubmed.ncbi.nlm.nih.gov/19892987/
- [wrighton-2006-scp-smad2-3-linker] Wrighton KH, Willis D, Long J, Liu F, Lin X, Feng XH. Small C-terminal domain phosphatases dephosphorylate the regulatory linker regions of Smad2 and Smad3 to enhance transforming growth factor-beta signaling. The Journal of biological chemistry 2006;281(50):38365-75. PMID: 17035229; DOI: 10.1074/jbc.M607246200. https://pubmed.ncbi.nlm.nih.gov/17035229/
- [wu-2009-scp-snail] Wu Y, Evers BM, Zhou BP. Small C-terminal domain phosphatase enhances snail activity through dephosphorylation. The Journal of biological chemistry 2009;284(1):640-648. PMID: 19004823; PMCID: PMC2610500; DOI: 10.1074/jbc.M806916200. https://pubmed.ncbi.nlm.nih.gov/19004823/
- [xia-2025-ctdsp2-zebrafish-p53] Xia X, Song W, Zhang F, Fan Y, Zhang B, Chen X. ctdsp2 Knockout Induces Zebrafish Craniofacial Dysplasia via p53 Signaling Activation. International journal of molecular sciences 2025;26(3). PMID: 39941065; PMCID: PMC11818092; DOI: 10.3390/ijms26031297. https://pubmed.ncbi.nlm.nih.gov/39941065/
- [yeo-2003-scp-ctd-phosphatase] Yeo M, Lin PS, Dahmus ME, Gill GN. A novel RNA polymerase II C-terminal domain phosphatase that preferentially dephosphorylates serine 5. The Journal of biological chemistry 2003;278(28):26078-85. PMID: 12721286; DOI: 10.1074/jbc.M301791200. https://pubmed.ncbi.nlm.nih.gov/12721286/
- [yeo-2005-scp-neuronal-silencing] Yeo M, Lee SK, Lee B, Ruiz EC, Pfaff SL, Gill GN. Small CTD phosphatases function in silencing neuronal gene expression. Science (New York, N.Y.) 2005;307(5709):596-600. PMID: 15681389; DOI: 10.1126/science.1100801. https://pubmed.ncbi.nlm.nih.gov/15681389/
- [zhang-2006-scp1-ctd-structure] Zhang Y, Kim Y, Genoud N, Gao J, Kelly JW, Pfaff SL, et al.. Determinants for dephosphorylation of the RNA polymerase II C-terminal domain by Scp1. Molecular cell 2006;24(5):759-770. PMID: 17157258; PMCID: PMC2859291; DOI: 10.1016/j.molcel.2006.10.027. https://pubmed.ncbi.nlm.nih.gov/17157258/
- [zhang-2018-mir26-ctdsp-emx2] Zhang H, Zhang L, Sun T. Cohesive Regulation of Neural Progenitor Development by microRNA miR-26, Its Host Gene Ctdsp and Target Gene Emx2 in the Mouse Embryonic Cerebral Cortex. Frontiers in molecular neuroscience 2018;11:44. PMID: 29515367; PMCID: PMC5825903; DOI: 10.3389/fnmol.2018.00044. https://pubmed.ncbi.nlm.nih.gov/29515367/
- [zhu-2012-mir26-host-genes-prb] Zhu Y, Lu Y, Zhang Q, Liu JJ, Li TJ, Yang JR, et al.. MicroRNA-26a/b and their host genes cooperate to inhibit the G1/S transition by activating the pRb protein. Nucleic acids research 2012;40(10):4615-25. PMID: 22210897; PMCID: PMC3378857; DOI: 10.1093/nar/gkr1278. https://pubmed.ncbi.nlm.nih.gov/22210897/
- [zohn-2001-xenopus-os4] Zohn IE, Brivanlou AH. Expression cloning of Xenopus Os4, an evolutionarily conserved gene, which induces mesoderm and dorsal axis. Developmental biology 2001;239(1):118-31. PMID: 11784023; DOI: 10.1006/dbio.2001.0420. https://pubmed.ncbi.nlm.nih.gov/11784023/

Database sources: UniProtKB F7A4N8 (https://rest.uniprot.org/uniprotkb/F7A4N8) and O14595 (https://rest.uniprot.org/uniprotkb/O14595); Ensembl gene ENSECAG00000018788 (https://rest.ensembl.org/lookup/id/ENSECAG00000018788); NCBI RefSeq XP_023499666.1 and XP_023499667.1 (https://www.ncbi.nlm.nih.gov/protein/XP_023499666.1). Sequence comparisons are in SEQUENCE_ANALYSIS.md.


## Citations

1. almo-2007-structural-genomics-phosphatases-abstract.md
2. almo-2007-structural-genomics-phosphatases-summary.md
3. burkholder-2018-scp1-rest-abstract.md
4. burkholder-2018-scp1-rest-summary.md
5. dill-2012-mir26b-ctdsp2-abstract.md
6. dill-2012-mir26b-ctdsp2-summary.md
7. han-2012-mir26b-ctdsp2-preview-abstract.md
8. han-2012-mir26b-ctdsp2-preview-summary.md
9. kanathanavanich-2024-ctdsp2-gli1-fusion-abstract.md
10. kanathanavanich-2024-ctdsp2-gli1-fusion-summary.md
11. kloet-2015-ctdsp2-foxo-ras-p21-abstract.md
12. kloet-2015-ctdsp2-foxo-ras-p21-fulltext.txt
13. kloet-2015-ctdsp2-foxo-ras-p21-summary.md
14. knockaert-2006-scp-smad1-bmp-abstract.md
15. knockaert-2006-scp-smad1-bmp-summary.md
16. krasnov-2019-scp-nsclc-abstract.md
17. krasnov-2019-scp-nsclc-fulltext.txt
18. krasnov-2019-scp-nsclc-summary.md
19. krasnov-2023-scp-ccrcc-abstract.md
20. krasnov-2023-scp-ccrcc-fulltext.txt
21. krasnov-2023-scp-ccrcc-summary.md
22. lin-2014-scp-pml-ccrcc-abstract.md
23. lin-2014-scp-pml-ccrcc-summary.md
24. nesti-2014-ctdsp1-rest-stability-abstract.md
25. nesti-2014-ctdsp1-rest-stability-summary.md
26. puzanov-2021-scp-oncogenesis-review-abstract.md
27. puzanov-2021-scp-oncogenesis-review-summary.md
28. r-2014-scp1-review-abstract.md
29. r-2014-scp1-review-fulltext.txt
30. r-2014-scp1-review-summary.md
31. sapkota-2006-scp-smad-linker-abstract.md
32. sapkota-2006-scp-smad-linker-summary.md
33. sauer-2021-mir26-rest-abstract.md
34. sauer-2021-mir26-rest-summary.md
35. su-1997-os4-sarcoma-abstract.md
36. su-1997-os4-sarcoma-summary.md
37. suo-2023-scp2-sterol-carrier-alias-abstract.md
38. suo-2023-scp2-sterol-carrier-alias-summary.md
39. thompson-2006-scp2-androgen-abstract.md
40. thompson-2006-scp2-androgen-summary.md
41. wade-2009-horse-genome-abstract.md
42. wade-2009-horse-genome-summary.md
43. wrighton-2006-scp-smad2-3-linker-abstract.md
44. wrighton-2006-scp-smad2-3-linker-summary.md
45. wu-2009-scp-snail-abstract.md
46. wu-2009-scp-snail-summary.md
47. xia-2025-ctdsp2-zebrafish-p53-abstract.md
48. xia-2025-ctdsp2-zebrafish-p53-fulltext.txt
49. xia-2025-ctdsp2-zebrafish-p53-summary.md
50. yeo-2003-scp-ctd-phosphatase-abstract.md
51. yeo-2003-scp-ctd-phosphatase-summary.md
52. yeo-2005-scp-neuronal-silencing-abstract.md
53. yeo-2005-scp-neuronal-silencing-summary.md
54. zhang-2006-scp1-ctd-structure-abstract.md
55. zhang-2006-scp1-ctd-structure-summary.md
56. zhang-2018-mir26-ctdsp-emx2-abstract.md
57. zhang-2018-mir26-ctdsp-emx2-fulltext.txt
58. zhang-2018-mir26-ctdsp-emx2-summary.md
59. zhu-2012-mir26-host-genes-prb-abstract.md
60. zhu-2012-mir26-host-genes-prb-fulltext.txt
61. zhu-2012-mir26-host-genes-prb-summary.md
62. zohn-2001-xenopus-os4-abstract.md
63. zohn-2001-xenopus-os4-summary.md