---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T02:59:28.708950'
end_time: '2026-10-26T03:11:23.365367'
duration_seconds: 714.66
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: OLFML2A
  gene_symbol: OLFML2A
  uniprot_accession: A0A9L0SKW1
  protein_description: 'SubName: Full=Olfactomedin like 2A {ECO:0000313|Ensembl:ENSECAP00000076704.1};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: Olfac-like_dom. (IPR003112); Olfactomedin-like_domain. (IPR050605);
    OLF (PF02191)
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
citation_count: 77
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0SKW1
- **Protein Description:** SubName: Full=Olfactomedin like 2A {ECO:0000313|Ensembl:ENSECAP00000076704.1};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Olfac-like_dom. (IPR003112); Olfactomedin-like_domain. (IPR050605); OLF (PF02191)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "OLFML2A" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'OLFML2A' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **OLFML2A** (gene ID: OLFML2A, UniProt: A0A9L0SKW1) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# OLFML2A (Olfactomedin-like 2A, photomedin-1) in the horse, *Equus caballus* — UniProt A0A9L0SKW1

## 1. Introduction and summary

A0A9L0SKW1 is an unreviewed, computationally predicted 599-residue horse protein named "Olfactomedin like 2A". It comes from the Ensembl gene model ENSECAG00000023908 on horse chromosome 25, built on the Thoroughbred reference genome [uniprot-A0A9L0SKW1-entry; wade-2009-horse-genome-abstract]. The identity checks support assigning it to OLFML2A. PANTHER places the sequence in subfamily PTHR23192:SF29 ("Olfactomedin-like protein 2A"), and it carries a C-terminal olfactomedin (OLF) domain (Pfam PF02191, PROSITE PS51132) [uniprot-A0A9L0SKW1-entry]. I aligned it to the reviewed human OLFML2A (Q68BL7, photomedin-1) myself: 547 of 598 aligned residues are identical (91.5%), and the OLF domain differs at only one of 259 positions. The horse sequence also has the two N-terminal CXCXC cysteine clusters (starting at residues 21 and 60) that are characteristic of the OLFML2 (photomedin) subfamily [uniprot-Q68BL7-human-OLFML2A-entry; furutani-2005-photomedins-abstract]. There is no ambiguity about the gene symbol. However, I found no study of OLFML2A in the horse. Everything below about function is therefore inferred from orthology with the mouse and human proteins and from what is known about the olfactomedin family as a whole.

On that evidence, horse OLFML2A is most likely a secreted, O-glycosylated, disulfide-linked homodimeric glycoprotein of the extracellular matrix (ECM). It contains no enzymatic or transport domain. Its best-supported molecular activity is binding to sulfated glycosaminoglycans, with a preference for chondroitin sulfate-E and heparin, which suggests it anchors to or organises proteoglycan-rich matrices [furutani-2005-photomedins-abstract; tomarev-2009-olfactomedin-review-fulltext]. In rodents the protein is expressed in specific places: the outer segments of retinal photoreceptors and the major processes of kidney podocytes [furutani-2005-photomedins-abstract; sistani-2013-podocyte-abstract]. Ocular expression has also been found in primates and fish [perezibave-2016-primates-abstract; garzarodriguez-2019-gar-abstract]. Recent cancer studies, mostly of triple-negative breast cancer and glioma cell lines, link OLFML2A to proliferation, epithelial–mesenchymal transition (EMT) and Wnt/β-catenin signalling [ma-2021-glioma-wnt-abstract; gao-2022-tnbc-genechip-abstract; ding-2025-tnbc-ezh2-abstract]. These are downstream, mostly correlative effects rather than a defined biochemical mechanism. The normal physiological function of OLFML2A remains, as one review put it, "still not clear" [tomarev-2009-olfactomedin-review-fulltext].

## 2. Gene and protein identity, and the quality of the horse gene model

The horse entry is supported only by genome annotation (protein existence level 4, "predicted"). Its only Gene Ontology annotation is "extracellular region", assigned automatically from the subcellular-location keyword [uniprot-A0A9L0SKW1-entry]. Its domain features are an OLF domain at residues 341–599 and two disordered, low-complexity regions (162–236 and 269–354) rich in basic, acidic, Ser/Thr and Pro residues [uniprot-A0A9L0SKW1-entry]. The reviewed human orthologue has the same layout: a 27-residue signal peptide, a coiled coil at residues 157–183, an OLF domain at 394–652 and an internal disulfide between Cys395 and Cys582 [uniprot-Q68BL7-human-OLFML2A-entry]. In mouse, the full-length photomedin-1 open reading frame encodes 681 residues. It consists of a signal sequence, two tandem CXCXCX9C motifs, a putative coiled coil, a Ser/Thr-rich region and the C-terminal OLF domain [perezibave-2016-primates-fulltext]. The Ser/Thr-rich stretch in front of the OLF domain is unique to the OLFML2 proteins within the olfactomedin family [tomarev-2009-olfactomedin-review-fulltext]. The horse sequence keeps this stretch (…PTPTPTPTTTTSPMSTEPP…).

My alignment shows two differences between the horse model and the human reference. First, the horse protein starts with "MDSQVFGDMD", which lines up with residue 28 of human OLFML2A (DSKVFGDLD), immediately after the human signal-peptide cleavage site [uniprot-Q68BL7-human-OLFML2A-entry]. The predicted horse protein therefore has no signal peptide. Second, it lacks about 22 residues that the human protein has between the cysteine-rich region and the coiled coil. The most parsimonious reading is that the Ensembl model is missing the first coding exon and may represent an alternative splice form. Human OLFML2A has three annotated isoforms [uniprot-Q68BL7-human-OLFML2A-entry]. If so, the native horse protein would, like its orthologues, have an N-terminal signal sequence and enter the secretory pathway. Note also that UniProt's "Secreted" annotation for this entry is automatic (ARBA) and is not based on a signal peptide in the predicted sequence [uniprot-A0A9L0SKW1-entry].

Ensembl data on the whole horse gene settle the signal-peptide question. Ensembl annotates horse OLFML2A (VGNC:21026) on chromosome 25 at 29,333,131–29,361,802 on the forward strand, with six protein-coding transcripts of 599 to 662 residues. These map to five UniProt entries, one of which is A0A9L0SKW1 (transcript ENSECAT00000146926) [ensembl-ENSECAG00000023908-summary; ensembl-ENSECAG00000023908-proteins]. Ensembl Compara calls the gene a one-to-one orthologue of human OLFML2A (ENSG00000185585, about 88% identity) and mouse Olfml2a (ENSMUSG00000046618, about 78–80% identity) [ensembl-ENSECAG00000023908-orthologues]. One of the other horse transcripts, ENSECAT00000148204, encodes the 618-residue UniProt entry A0A9L0R1T7. It begins MAAAALPPRP…, much like the human precursor, and has a SignalP-predicted signal peptide (residues 1–34) followed by …ADSKVFGDMD… [uniprot-A0A9L0R1T7-horse-isoform-entry; ensembl-ENSECAG00000023908-proteins]. This confirms that the horse gene does encode a classical secretory signal sequence. A0A9L0SKW1 therefore represents an N-terminally truncated transcript model, not the main secreted precursor. Its remaining sequence, including the olfactomedin domain, matches the signal-peptide-containing isoform.

## 3. The olfactomedin family and the structural basis of OLFML2A function

Olfactomedin-domain proteins share a C-terminal domain of about 250 residues, which is thought to mediate protein–protein interactions. Most members also have N-terminal cysteines that form intermolecular disulfides and so drive oligomerisation [anholt-2014-olfactomedin-review-fulltext]. Comprehensive phylogenetic analysis divided the family into seven subfamilies. The trees built from OLF domains alone and from the flanking non-OLF regions have nearly the same topology. This means the OLF domain coevolved with its partner domains, so subfamily membership is a reasonable guide to architecture and function [zeng-2005-olfactomedin-phylogeny-abstract]. A later metazoan-wide survey extended the classification to nine subfamilies [li-2019-olfactomedin-evolution-abstract]. OLFML2A and OLFML2B (photomedin-1 and -2) are more closely related to each other than to any other member, share 69% identity in their OLF domains and together form subfamily IV [tomarev-2009-olfactomedin-review-fulltext]. Studies in primates and spotted gar confirm clear one-to-one orthology of OLFML2A across vertebrates and point to purifying selection, consistent with a conserved function [perezibave-2016-primates-abstract; garzarodriguez-2019-gar-abstract]. The near-identity of the horse and human OLF domains fits this pattern.

No structure of OLFML2A has been solved. Structures of other family members provide a model. The OLF domain of gliomedin folds as a five-bladed β-propeller with twisted, non-five-fold symmetry, and its conserved top face is proposed as the ligand-binding surface [han-2015-gliomedin-propeller-abstract]. Full-length olfactomedin-1 assembles into a disulfide-linked, V-shaped tetramer. Its N-terminal domains form the base of the V, parallel disulfide-linked coiled coils form the arms, and dimers of OLF β-propellers sit at the tips with their top faces exposed. Calcium stabilises the assembly. The authors suggest this architecture clusters receptors and that it "sheds light on the conformation of several other olfactomedin domain family members" [pronker-2015-olfactomedin1-structure-abstract]. OLFML2A has the same basic plan: N-terminal cysteine motifs, a coiled coil and a C-terminal OLF domain [furutani-2005-photomedins-abstract]. By analogy, though this has not been tested, it is plausible that horse OLFML2A forms a parallel coiled-coil-mediated dimer that presents two OLF propellers for binding partners.

## 4. Molecular function: a glycosaminoglycan-binding extracellular matrix glycoprotein

The key biochemical study of OLFML2A is the characterisation of the mouse photomedins by Furutani and colleagues. They found photomedin-1 in a large computational and expression screen of RIKEN mouse cDNAs designed to find new ECM proteins [furutani-2005-photomedins-abstract]. Recombinant photomedin-1 was secreted as a disulfide-bonded dimer carrying O-linked carbohydrate chains, and after secretion it was cleaved in the middle of the molecule [furutani-2005-photomedins-abstract]. A review of that work adds that the N-terminal region is needed for dimerisation and that the released C-terminal fragment, which contains an intact OLF domain, cannot dimerise [tomarev-2009-olfactomedin-review-fulltext]. UniProt maps the likely cleavage site to Lys-295 of human OLFML2A, by similarity to mouse, and records that the protein is O-glycosylated but not N-glycosylated [uniprot-Q68BL7-human-OLFML2A-entry]. The reviewed mouse entry attributes these properties to the Furutani study with experimental evidence codes: homodimer formation, heparin and chondroitin sulfate-E binding, secretion, cleavage at Lys-301 and O-glycosylation. Its curated Gene Ontology annotations from MGI are extracellular matrix (IDA), extracellular matrix binding (IDA), identical protein binding (IPI) and extracellular matrix organization (IDA) [uniprot-Q8BHP7-mouse-Olfml2a-entry]. When tested against a panel of ECM components including several glycosaminoglycans, the photomedins bound chondroitin sulfate-E and heparin preferentially. The authors concluded that photomedins are extracellular OLF-domain proteins "capable of binding to proteoglycans containing these glycosaminoglycan chains" [furutani-2005-photomedins-abstract].

OLFML2A should therefore be classed as a structural or adaptor ECM protein, not an enzyme, transporter or receptor. Its best-supported molecular function is binding to highly sulfated glycosaminoglycans: heparin/heparan sulfate-like chains and the 4,6-disulfated chondroitin sulfate-E. Within the matrix it probably acts as a bridging or organising component. A dimeric OLFML2A held together by its N-terminal region could link proteoglycans or other ligands through its two OLF domains. Cleavage after secretion would split it into monomeric OLF-domain fragments and so may be a way to regulate this bridging. This is inference from the mouse biochemistry and family structures and has not been shown directly. No protein ligand of the OLF domain of OLFML2A has been identified. In the related subfamily I, OLFM2 hetero-associates with OLFM1 and OLFM3 but not with more distant members such as myocilin or gliomedin [sultana-2011-olfm2-eye-abstract]. A similar question, whether OLFML2A and OLFML2B form heteromers, has not been investigated.

## 5. Localization: extracellular, at specialised cell surfaces in retina and kidney

Experimentally, OLFML2A is a secreted protein [furutani-2005-photomedins-abstract], and it is found in a few highly polarised cell compartments. In mouse retina, photomedin-1 is selectively expressed in the photoreceptor outer segments, whereas photomedin-2 is found in all retinal neurons [furutani-2005-photomedins-abstract]. A later review describes the two adult retinal patterns as mutually exclusive. Olfml2a is mainly in the photoreceptor layer, while Olfml2b is in the ganglion cell and inner nuclear layers, photoreceptor inner segments and retinal pigment epithelium [tomarev-2009-olfactomedin-review-fulltext]. Expression in the eye is conserved. OLFML2A transcripts and protein were detected in human cornea, lens and retina and in baboon cornea, lens, iris and retina [perezibave-2016-primates-abstract]. In spotted gar retina, OLFML2A/B immunoreactivity was found in the photoreceptor layer and the outer and inner nuclear layers [garzarodriguez-2019-gar-abstract]. Taken together, the outer-segment localisation and the CS-E/heparin binding suggest a role in the interphotoreceptor matrix, a proteoglycan-rich extracellular compartment around the outer segments. No study has tested that link directly.

In the kidney, glomerular transcriptome profiling unexpectedly identified Olfml2a as a podocyte-specific gene. Immunofluorescence and immunoelectron microscopy placed the protein in podocyte major (primary) processes, where it colocalised with vimentin throughout podocyte development [sistani-2013-podocyte-abstract]. During glomerulogenesis it appears at the vesicle stage, is seen in invading endothelial cells at the S-shaped stage and is later restricted to the basal side of maturing podocytes [uniprot-Q68BL7-human-OLFML2A-entry]. OLFML2A is also found in human glomerular crescents together with podocyte markers, where it was used as evidence that podocytes contribute to crescent formation [sistani-2013-podocyte-abstract]. In pig embryos, OLFML2A mRNA and protein are expressed specifically in mammary placodes, and expression-network analysis enriched it for ECM organisation [liu-2025-pig-teats-abstract]. In cancer cell lines and tumours, immunohistochemistry often reports cytoplasmic staining [ding-2025-tnbc-ezh2-fulltext]. That may simply be protein in transit through the secretory pathway and does not by itself point to an intracellular function. Expression outside the eye and kidney is broader than these two sites suggest. By Northern-type analysis, cited with experimental evidence in the mouse UniProt entry, photomedin-1 is expressed in lung, eye, testis, uterus and ovary, and at lower levels in heart, skeletal muscle, mammary gland, skin and prostate [uniprot-Q8BHP7-mouse-Olfml2a-entry]. Human Protein Atlas transcriptomics agree with this, showing low tissue specificity in bulk RNA. At single-cell resolution, OLFML2A is enriched in Schwann cells, lymphatic endothelial cells, smooth-muscle and mural cells, pericytes, fibroblasts and breast myoepithelial cells. Single-nucleus data from brain show enrichment in vascular smooth muscle cells, pericytes and fibroblasts. It is not detected in blood immune cells, and the protein has been detected in plasma by mass spectrometry [hpa-ENSG00000185585-OLFML2A-summary]. This profile, dominated by mesenchymal, perivascular and glial cells that make basement membranes, fits an ECM-secreting role. HPA's antibody-based location in cultured cells (nucleoplasm, vesicles and Golgi) [hpa-ENSG00000185585-OLFML2A-summary] reflects protein in the secretory pathway in fixed cells; the nuclear signal is unvalidated and is not evidence of a nuclear function. Overall, the evidence places horse OLFML2A in the extracellular region and extracellular matrix, close to the basal or specialised surfaces of the cells that make it.

## 6. Pathways and biological processes: developmental and disease associations

No canonical signalling pathway has been mechanistically tied to OLFML2A in normal physiology. Most of the pathway-level data come from human cancer cell lines. In glioma, OLFML2A expression rises with tumour grade. Knocking it down reduced proliferation and increased apoptosis, and it also inhibited Wnt/β-catenin signalling by raising amyloid precursor protein (APP), lowering stabilised β-catenin and repressing MYC, CD44 and CSNK2A2 [ma-2021-glioma-wnt-abstract]. In triple-negative breast cancer (TNBC) cells, OLFML2A was reported to act downstream of c-Fos/AP-1 and to be required for the anti-tumour effects of the AP-1 inhibitor T-5224 [zhao-2021-tnbc-t5224-abstract]. Silencing OLFML2A caused S-phase arrest, apoptosis and reduced EMT, with transcriptome-wide effects on cell-cycle, p53, integrin, HGF and NGF signalling [gao-2022-tnbc-genechip-abstract]. A later knockout/overexpression study reported G1 arrest and reduced xenograft growth, and proposed an OLFML2A–EZH2 axis based on proteomics and co-immunoprecipitation [ding-2025-tnbc-ezh2-abstract; ding-2025-tnbc-ezh2-fulltext]. Further TNBC studies link OLFML2A to EMT markers and to growth suppression by herbal extracts [chen-2026-konjac-tnbc-emt-abstract; wu-2019-amorphophalli-tnbc-abstract]. In acute myeloid leukaemia, OLFML2A is described as overexpressed and as a marker of adverse prognosis [lu-2023-aml-prognosis-abstract; lu-2026-aml-all-abstract]. The 2023 abstract is internally inconsistent about which direction of survival is associated with high expression [lu-2023-aml-prognosis-abstract]. It is not clear how a secreted ECM protein would bind the nuclear methyltransferase EZH2 or control β-catenin stability directly. The more parsimonious reading is that these effects are indirect, for example through changes in cell–matrix or integrin signalling, which is consistent with the integrin pathway changes after knockdown [gao-2022-tnbc-genechip-abstract]. Many of these studies come from a few groups and use one TNBC cell line (MDA-MB-231), so they should be treated as preliminary.

Genetic association studies in livestock and humans provide further, weaker hints. In Meishan and Erhualian pigs, fine-mapping, TWAS and placode RNA-seq identified OLFML2A as the likely causal gene at a major QTL for teat number, with higher placode expression in high-teat-number embryos [liu-2025-pig-teats-abstract]. This is an intriguing developmental link, through epithelial–stromal ECM interactions, that could be relevant to other domestic mammals such as the horse. In Holstein cattle OLFML2A was nominated as a candidate gene for milk fat yield [pedrosa-2021-holstein-abstract]. A small Korean intracranial-aneurysm GWAS fine-mapped a variant near OLFML2A, but it did not replicate [hong-2022-intracranial-aneurysm-abstract]. A related name causes confusion: OLFM2, a subfamily I protein, regulates TGF-β-induced smooth-muscle differentiation through SRF [shi-2014-olfm2-smc-abstract]. That work concerns a different gene and should not be transferred to OLFML2A.

## 7. Synthesis: predicted function of horse A0A9L0SKW1

Putting the evidence together, horse A0A9L0SKW1 is the orthologue of mammalian OLFML2A/photomedin-1. Its OLF domain is essentially identical to the human one, it has the subfamily-defining N-terminal cysteine motifs and Ser/Thr-rich linker, and its predicted N-terminus is probably truncated. It is best annotated as a secreted extracellular matrix glycoprotein. Its proposed molecular activity is binding to sulfated glycosaminoglycans (chondroitin sulfate-E and heparin) and, by extension, to proteoglycans [furutani-2005-photomedins-abstract]. It probably forms disulfide-linked dimers via its N-terminal region and is processed by proteolysis after secretion [furutani-2005-photomedins-abstract; tomarev-2009-olfactomedin-review-fulltext]. It probably acts in the extracellular space next to photoreceptor outer segments and at the basal side of podocyte major processes [furutani-2005-photomedins-abstract; sistani-2013-podocyte-abstract], and possibly in the stroma of developing epithelial appendages such as mammary placodes [liu-2025-pig-teats-abstract]. Its biological role is most plausibly structural or adaptor-like, organising the matrix and modulating cell–matrix interactions. It has no enzymatic or transport function. Its effects on Wnt/β-catenin, AP-1, EZH2 and cell-cycle pathways in tumour cells are best treated as context-dependent consequences, not as its core function [ma-2021-glioma-wnt-abstract; zhao-2021-tnbc-t5224-abstract; ding-2025-tnbc-ezh2-abstract].

## Open Questions

The first open question concerns the horse gene models. The gene has six annotated transcripts, and only one of them (A0A9L0R1T7) encodes a signal peptide. Equine RNA-seq or Iso-Seq data should show which transcript is the dominant secreted isoform, and whether the truncated A0A9L0SKW1 model, which lacks a signal peptide, is real or an annotation artefact. No phenotype records for Olfml2a were returned by the IMPC genotype–phenotype resource when this report was written [impc-olfml2a-query]. Biochemically, no protein ligand of the OLFML2A OLF domain is known. Affinity purification from retina or kidney, or proximity labelling in the ECM, could identify partners. These experiments could also test whether OLFML2A, like olfactomedin-1, forms higher-order calcium-stabilised assemblies and whether it hetero-oligomerises with OLFML2B. The glycosaminoglycan-binding specificity should be measured quantitatively, for example with glycan arrays and surface plasmon resonance, and mapped to the OLF domain or the basic disordered regions. The protease responsible for cleavage after secretion, and the purpose of that cleavage, are unknown. Physiologically, no knockout phenotype for Olfml2a has been reported in the literature reviewed here. A mouse or zebrafish loss-of-function model, analysed for photoreceptor outer-segment and interphotoreceptor-matrix integrity, podocyte process architecture and mammary/teat development, would test the hypotheses suggested by the expression data. For the horse in particular, it would be useful to examine OLFML2A expression in equine retina and kidney, and to look for association of the chromosome 25 locus with ocular, renal or conformational traits, in the way the pig teat-number QTL was studied. Finally, the cancer-related mechanisms, especially the reported links to EZH2 and β-catenin, need independent replication and an explanation that fits an extracellular location.

## References

* **[anholt-2014-olfactomedin-review]** Anholt RR et al. Olfactomedin proteins: central players in development and disease. *Frontiers in cell and developmental biology (2014) 2:6*. PMID: 25364714. DOI: [10.3389/fcell.2014.00006](https://doi.org/10.3389/fcell.2014.00006). PMCID: PMC4206993.
* **[chen-2026-konjac-tnbc-emt]** Chen Y, Yu Q, Ding H et al. Konjac petroleum ether extract inhibits triple-negative breast cancer cell migration and invasion by attenuating OLFML2A-mediated epithelial-mesenchymal transition. *Frontiers in pharmacology (2026) 17:1734640*. PMID: 42222147. DOI: [10.3389/fphar.2026.1734640](https://doi.org/10.3389/fphar.2026.1734640). PMCID: PMC13219017.
* **[ding-2025-tnbc-ezh2]** Ding H, Chen Y, Yu Q et al. OLFML2A mediates cell cycle regulation in triple-negative breast cancer via EZH2. *Frontiers in oncology (2025) 15:1750297*. PMID: 41607539. DOI: [10.3389/fonc.2025.1750297](https://doi.org/10.3389/fonc.2025.1750297). PMCID: PMC12834820.
* **[ding-2026-hnrnpc-esophageal]** Ding G, He J, Chen Y et al. Heterogeneous nuclear ribonucleoprotein C deficiency compromises extracellular matrix-receptor interaction and induces apoptosis in esophageal cancer by targeting transcripts with complex structures. *Biochimica et biophysica acta. Molecular basis of disease (2026) 1872:168267*. PMID: 42002088. DOI: [10.1016/j.bbadis.2026.168267](https://doi.org/10.1016/j.bbadis.2026.168267).
* **[furutani-2005-photomedins]** Furutani Y, Manabe R, Tsutsui K et al. Identification and characterization of photomedins: novel olfactomedin-domain-containing proteins with chondroitin sulphate-E-binding activity. *The Biochemical journal (2005) 389:675-84*. PMID: 15836428. DOI: [10.1042/BJ20050120](https://doi.org/10.1042/BJ20050120). PMCID: PMC1180717.
* **[gao-2022-tnbc-genechip]** Gao X, Yang Z, Xu C et al. GeneChip expression profiling identified OLFML2A as a potential therapeutic target in TNBC cells. *Annals of translational medicine (2022) 10:274*. PMID: 35433966. DOI: [10.21037/atm-22-757](https://doi.org/10.21037/atm-22-757). PMCID: PMC9011253.
* **[garzarodriguez-2019-gar]** Garza-Rodríguez ML, González-Álvarez R, Mendoza Alfaro RE et al. Olfactomedin-like 2 A and B (OLFML2A and OLFML2B) profile expression in the retina of spotted gar (Lepisosteus oculatus) and bioinformatics mining. *Fish physiology and biochemistry (2019) 45:1575-1587*. PMID: 31111317. DOI: [10.1007/s10695-019-00647-0](https://doi.org/10.1007/s10695-019-00647-0).
* **[han-2015-gliomedin-propeller]** Han H, Kursula P et al. The olfactomedin domain from gliomedin is a β-propeller with unique structural properties. *The Journal of biological chemistry (2015) 290:3612-21*. PMID: 25525261. DOI: [10.1074/jbc.M114.627547](https://doi.org/10.1074/jbc.M114.627547). PMCID: PMC4319027.
* **[hong-2022-intracranial-aneurysm]** Hong EP, Youn DH, Kim BJ et al. Fine-mapping of intracranial aneurysm susceptibility based on a genome-wide association study. *Scientific reports (2022) 12:2717*. PMID: 35177760. DOI: [10.1038/s41598-022-06755-x](https://doi.org/10.1038/s41598-022-06755-x). PMCID: PMC8854430.
* **[li-2019-olfactomedin-evolution]** Li Q, Liu A, Gu X et al. Olfactomedin domain-containing proteins: evolution, functional divergence, expression patterns and damaging SNPs. *Molecular genetics and genomics : MGG (2019) 294:875-885*. PMID: 30915543. DOI: [10.1007/s00438-019-01549-9](https://doi.org/10.1007/s00438-019-01549-9).
* **[liu-2025-pig-teats]** Liu CX, Huang RH, Zhou WD et al. The candidate gene OLFML2A possibly contributed to the variation of total number of teats in Meishan and Erhualian pigs by influencing the formation of mammary placodes. *Animal : an international journal of animal bioscience (2025) 19:101552*. PMID: 40499407. DOI: [10.1016/j.animal.2025.101552](https://doi.org/10.1016/j.animal.2025.101552).
* **[lu-2023-aml-prognosis]** Lu X, Li Y, Yang Y et al. OLFML2A Overexpression Predicts an Unfavorable Prognosis in Patients with AML. *Journal of oncology (2023) 2023:6017852*. PMID: 36873740. DOI: [10.1155/2023/6017852](https://doi.org/10.1155/2023/6017852). PMCID: PMC9977544.
* **[lu-2026-aml-all]** Lu X, Li J, Zhao X et al. OLFML2A expression in acute myeloid leukemia, with exploratory findings in acute lymphoblastic leukemia: Prognostic significance and re-analysis of public single-cell transcriptomic data. *Oncology letters (2026) 32:466*. PMID: 42639436. DOI: [10.3892/ol.2026.15821](https://doi.org/10.3892/ol.2026.15821). PMCID: PMC13501490.
* **[ma-2021-glioma-wnt]** Ma S, Duan L, Dong H et al. OLFML2A Downregulation Inhibits Glioma Proliferation Through Suppression of Wnt/β-Catenin Signaling. *Frontiers in oncology (2021) 11:717917*. PMID: 34650914. DOI: [10.3389/fonc.2021.717917](https://doi.org/10.3389/fonc.2021.717917). PMCID: PMC8506028.
* **[pedrosa-2021-holstein]** Pedrosa VB, Schenkel FS, Chen SY et al. Genomewide Association Analyses of Lactation Persistency and Milk Production Traits in Holstein Cattle Based on Imputed Whole-Genome Sequence Data. *Genes (2021) 12:*. PMID: 34828436. DOI: [10.3390/genes12111830](https://doi.org/10.3390/genes12111830). PMCID: PMC8624223.
* **[perezibave-2016-primates]** Pérez-Ibave DC, González-Alvarez R, de La Luz Martinez-Fierro M et al. Olfactomedin-like 2 A and B (OLFML2A and OLFML2B) expression profile in primates (human and baboon). *Biological research (2016) 49:44*. PMID: 27821182. DOI: [10.1186/s40659-016-0101-8](https://doi.org/10.1186/s40659-016-0101-8). PMCID: PMC5100274.
* **[pronker-2015-olfactomedin1-structure]** Pronker MF, Bos TG, Sharp TH et al. Olfactomedin-1 Has a V-shaped Disulfide-linked Tetrameric Structure. *The Journal of biological chemistry (2015) 290:15092-101*. PMID: 25903135. DOI: [10.1074/jbc.M115.653485](https://doi.org/10.1074/jbc.M115.653485). PMCID: PMC4463452.
* **[shi-2014-olfm2-smc]** Shi N, Guo X, Chen SY et al. Olfactomedin 2, a novel regulator for transforming growth factor-β-induced smooth muscle differentiation of human embryonic stem cell-derived mesenchymal cells. *Molecular biology of the cell (2014) 25:4106-14*. PMID: 25298399. DOI: [10.1091/mbc.E14-08-1255](https://doi.org/10.1091/mbc.E14-08-1255). PMCID: PMC4263453.
* **[sistani-2013-podocyte]** Sistani L, Rodriguez PQ, Hultenby K et al. Neuronal proteins are novel components of podocyte major processes and their expression in glomerular crescents supports their role in crescent formation. *Kidney international (2013) 83:63-71*. PMID: 22913984. DOI: [10.1038/ki.2012.321](https://doi.org/10.1038/ki.2012.321).
* **[sultana-2011-olfm2-eye]** Sultana A, Nakaya N, Senatorov VV et al. Olfactomedin 2: expression in the eye and interaction with other olfactomedin domain-containing proteins. *Investigative ophthalmology & visual science (2011) 52:2584-92*. PMID: 21228389. DOI: [10.1167/iovs.10-6356](https://doi.org/10.1167/iovs.10-6356). PMCID: PMC3088551.
* **[tomarev-2009-olfactomedin-review]** Tomarev SI, Nakaya N et al. Olfactomedin domain-containing proteins: possible mechanisms of action and functions in normal development and pathology. *Molecular neurobiology (2009) 40:122-38*. PMID: 19554483. DOI: [10.1007/s12035-009-8076-x](https://doi.org/10.1007/s12035-009-8076-x). PMCID: PMC2936706.
* **[wade-2009-horse-genome]** Wade CM, Giulotto E, Sigurdsson S et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science (New York, N.Y.) (2009) 326:865-7*. PMID: 19892987. DOI: [10.1126/science.1178158](https://doi.org/10.1126/science.1178158). PMCID: PMC3785132.
* **[wu-2019-amorphophalli-tnbc]** Wu C, Chen M, Zhang Q et al. Genomic and GeneChip expression profiling reveals the inhibitory effects of Amorphophalli Rhizoma in TNBC cells. *Journal of ethnopharmacology (2019) 235:206-218*. PMID: 30731183. DOI: [10.1016/j.jep.2019.02.004](https://doi.org/10.1016/j.jep.2019.02.004).
* **[zeng-2005-olfactomedin-phylogeny]** Zeng LC, Han ZG, Ma WJ et al. Elucidation of subfamily segregation and intramolecular coevolution of the olfactomedin-like proteins by comprehensive phylogenetic analysis and gene expression pattern assessment. *FEBS letters (2005) 579:5443-53*. PMID: 16212957. DOI: [10.1016/j.febslet.2005.08.064](https://doi.org/10.1016/j.febslet.2005.08.064).
* **[zhao-2021-tnbc-t5224]** Zhao Q, Zhang K, Li Y et al. OLFML2A is necessary for anti-triple negative breast cancer effect of selective activator protein-1 inhibitor T-5224. *Translational oncology (2021) 14:101100*. PMID: 33993098. DOI: [10.1016/j.tranon.2021.101100](https://doi.org/10.1016/j.tranon.2021.101100). PMCID: PMC8138778.
* **[uniprot-A0A9L0SKW1]** UniProt Consortium. UniProtKB/TrEMBL entry A0A9L0SKW1_HORSE, "Olfactomedin like 2A" (entry version 13, 10-JUN-2026). https://rest.uniprot.org/uniprotkb/A0A9L0SKW1.txt (local copy: citations/uniprot-A0A9L0SKW1-entry.txt).
* **[uniprot-Q68BL7-human-OLFML2A]** UniProt Consortium. UniProtKB/Swiss-Prot entry Q68BL7 (OLM2A_HUMAN), Olfactomedin-like protein 2A. https://rest.uniprot.org/uniprotkb/Q68BL7.txt (local copy: citations/uniprot-Q68BL7-human-OLFML2A-entry.txt).
* **[uniprot-Q8BHP7-mouse-Olfml2a]** UniProt Consortium. UniProtKB/Swiss-Prot entry Q8BHP7, mouse Olfactomedin-like protein 2A. https://rest.uniprot.org/uniprotkb/Q8BHP7.txt (local copy: citations/uniprot-Q8BHP7-mouse-Olfml2a-entry.txt).
* **[uniprot-A0A9L0R1T7-horse-isoform]** UniProt Consortium. UniProtKB/TrEMBL entry A0A9L0R1T7, horse Olfactomedin like 2A (Ensembl ENSECAT00000148204). https://rest.uniprot.org/uniprotkb/A0A9L0R1T7.txt (local copy: citations/uniprot-A0A9L0R1T7-horse-isoform-entry.txt).
* **[ensembl-ENSECAG00000023908]** Ensembl REST API: gene lookup, Compara orthologues and protein sequences for horse ENSECAG00000023908. https://rest.ensembl.org/lookup/id/ENSECAG00000023908 ; https://rest.ensembl.org/homology/id/equus_caballus/ENSECAG00000023908 (local copies: citations/ensembl-ENSECAG00000023908-orthologues.json, citations/ensembl-ENSECAG00000023908-proteins.fa).
* **[hpa-ENSG00000185585-OLFML2A]** Human Protein Atlas, OLFML2A (ENSG00000185585). https://www.proteinatlas.org/ENSG00000185585.json (local copy: citations/hpa-ENSG00000185585-OLFML2A.json).
* **[impc-olfml2a-query]** IMPC genotype-phenotype Solr query for marker_symbol:Olfml2a (0 records). https://www.ebi.ac.uk/mi/impc/solr/genotype-phenotype/select?q=marker_symbol:Olfml2a (local copy: citations/impc-olfml2a-query.json).


## Citations

1. anholt-2014-olfactomedin-review-abstract.md
2. anholt-2014-olfactomedin-review-fulltext.txt
3. anholt-2014-olfactomedin-review-summary.md
4. chen-2026-konjac-tnbc-emt-abstract.md
5. chen-2026-konjac-tnbc-emt-fulltext.txt
6. chen-2026-konjac-tnbc-emt-summary.md
7. ding-2025-tnbc-ezh2-abstract.md
8. ding-2025-tnbc-ezh2-fulltext.txt
9. ding-2025-tnbc-ezh2-summary.md
10. ding-2026-hnrnpc-esophageal-abstract.md
11. ding-2026-hnrnpc-esophageal-summary.md
12. ensembl-ENSECAG00000023908-orthologues.json
13. ensembl-ENSECAG00000023908-proteins.fa
14. ensembl-ENSECAG00000023908-summary.md
15. furutani-2005-photomedins-abstract.md
16. furutani-2005-photomedins-summary.md
17. gao-2022-tnbc-genechip-abstract.md
18. gao-2022-tnbc-genechip-fulltext.txt
19. gao-2022-tnbc-genechip-summary.md
20. garzarodriguez-2019-gar-abstract.md
21. garzarodriguez-2019-gar-summary.md
22. han-2015-gliomedin-propeller-abstract.md
23. han-2015-gliomedin-propeller-summary.md
24. hong-2022-intracranial-aneurysm-abstract.md
25. hong-2022-intracranial-aneurysm-fulltext.txt
26. hong-2022-intracranial-aneurysm-summary.md
27. hpa-ENSG00000185585-OLFML2A-summary.md
28. hpa-ENSG00000185585-OLFML2A.json
29. impc-olfml2a-query.json
30. li-2019-olfactomedin-evolution-abstract.md
31. li-2019-olfactomedin-evolution-summary.md
32. liu-2025-pig-teats-abstract.md
33. liu-2025-pig-teats-summary.md
34. lu-2023-aml-prognosis-abstract.md
35. lu-2023-aml-prognosis-fulltext.txt
36. lu-2023-aml-prognosis-summary.md
37. lu-2026-aml-all-abstract.md
38. lu-2026-aml-all-summary.md
39. ma-2021-glioma-wnt-abstract.md
40. ma-2021-glioma-wnt-fulltext.txt
41. ma-2021-glioma-wnt-summary.md
42. pedrosa-2021-holstein-abstract.md
43. pedrosa-2021-holstein-fulltext.txt
44. pedrosa-2021-holstein-summary.md
45. perezibave-2016-primates-abstract.md
46. perezibave-2016-primates-fulltext.txt
47. perezibave-2016-primates-summary.md
48. pronker-2015-olfactomedin1-structure-abstract.md
49. pronker-2015-olfactomedin1-structure-fulltext.txt
50. pronker-2015-olfactomedin1-structure-summary.md
51. shi-2014-olfm2-smc-abstract.md
52. shi-2014-olfm2-smc-fulltext.txt
53. shi-2014-olfm2-smc-summary.md
54. sistani-2013-podocyte-abstract.md
55. sistani-2013-podocyte-summary.md
56. sultana-2011-olfm2-eye-abstract.md
57. sultana-2011-olfm2-eye-summary.md
58. tomarev-2009-olfactomedin-review-abstract.md
59. tomarev-2009-olfactomedin-review-fulltext.txt
60. tomarev-2009-olfactomedin-review-summary.md
61. uniprot-A0A9L0R1T7-horse-isoform-entry.txt
62. uniprot-A0A9L0R1T7-horse-isoform-summary.md
63. uniprot-A0A9L0SKW1-entry.txt
64. uniprot-A0A9L0SKW1-summary.md
65. uniprot-Q68BL7-human-OLFML2A-entry.txt
66. uniprot-Q68BL7-human-OLFML2A-summary.md
67. uniprot-Q8BHP7-mouse-Olfml2a-entry.txt
68. uniprot-Q8BHP7-mouse-Olfml2a-summary.md
69. wade-2009-horse-genome-abstract.md
70. wade-2009-horse-genome-summary.md
71. wu-2019-amorphophalli-tnbc-abstract.md
72. wu-2019-amorphophalli-tnbc-summary.md
73. zeng-2005-olfactomedin-phylogeny-abstract.md
74. zeng-2005-olfactomedin-phylogeny-summary.md
75. zhao-2021-tnbc-t5224-abstract.md
76. zhao-2021-tnbc-t5224-fulltext.txt
77. zhao-2021-tnbc-t5224-summary.md