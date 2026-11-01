---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:27:08.404009'
end_time: '2026-10-26T01:47:25.128244'
duration_seconds: 1216.72
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: TNFRSF1A
  gene_symbol: TNFRSF1A
  uniprot_accession: A0A9L0JKX4
  protein_description: 'SubName: Full=TNF receptor superfamily member 1A {ECO:0000313|Ensembl:ENSEASP00005050612.1};'
  gene_info: Name=TNFRSF1A {ECO:0000313|Ensembl:ENSEASP00005050612.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Not specified in UniProt
  protein_domains: DEATH-like_dom_sf. (IPR011029); Death_dom. (IPR000488); TNFR/NGFR_Cys_rich_reg.
    (IPR001368); TNFRSF1A. (IPR052493); TNFRSF1A_death. (IPR033994)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3303
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 93
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0JKX4
- **Protein Description:** SubName: Full=TNF receptor superfamily member 1A {ECO:0000313|Ensembl:ENSEASP00005050612.1};
- **Gene Information:** Name=TNFRSF1A {ECO:0000313|Ensembl:ENSEASP00005050612.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DEATH-like_dom_sf. (IPR011029); Death_dom. (IPR000488); TNFR/NGFR_Cys_rich_reg. (IPR001368); TNFRSF1A. (IPR052493); TNFRSF1A_death. (IPR033994)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "TNFRSF1A" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'TNFRSF1A' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **TNFRSF1A** (gene ID: TNFRSF1A, UniProt: A0A9L0JKX4) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# TNFRSF1A (TNF receptor 1) in the donkey, *Equus asinus*: UniProt A0A9L0JKX4

## 1. Introduction and summary

UniProt A0A9L0JKX4 is an unreviewed, computationally predicted protein from the domestic donkey (*Equus asinus*). It is labelled "TNF receptor superfamily member 1A" (gene symbol TNFRSF1A). The entry is a 410-residue translation of the Ensembl transcript ENSEAST00005054546.1, which comes from the gene ENSEASG00005016176 on donkey chromosome 22. That gene model rests on the chromosome-level Dezhou donkey reference genome [uniprot-A0A9L0JKX4-entry][wang-2020-donkey-genome-abstract]. The symbol is not ambiguous. The protein has an N-terminal signal peptide, TNFR/NGFR cysteine-rich repeats, one transmembrane helix and a C-terminal death domain classified as the TNFR1-specific death domain (IPR033994; CDD cd08313). This is the architecture of TNF receptor 1, also called TNFR1, p55/p60 or CD120a [uniprot-A0A9L0JKX4-entry]. Across its whole length it aligns with human TNFR1 (P19438), sharing identical residues at about 74% of its positions, and it is 100% identical to the other donkey TNFRSF1A entry (A0A8C4MD74, 453 aa) over every residue it contains [notes_sequence_analysis].

The main finding of this report concerns the gene model. A0A9L0JKX4 is not the canonical donkey TNFR1. It is the product of a non-canonical Ensembl transcript that skips the 129-nucleotide exon 3. Because 129 is a multiple of three, the skip keeps the reading frame and removes exactly 43 residues, equivalent to human residues 64–106. Those residues span the second half of cysteine-rich domain 1 (CRD1) and the first half of CRD2 [notes_sequence_analysis][uniprot-P19438-entry]. The horse Ensembl annotation contains the same isoform (A0A5F5PQM0), and human has a manually annotated (HAVANA) equivalent, ENST00000540022 (UniProt F5H061, 412 residues). However, the cDNAs cited as evidence for the human locus support skipping of exon 2, not exon 3, so experimental support for exon-3 skipping is still unclear in every species [notes_sequence_analysis][uniprot-F5H061-entry][refseq-NM_001346091-entry]. AlphaFold models of the variant predict that the four cysteines left over by the deletion pair with one another, forming a hybrid CRD1/CRD2 module followed by intact CRD3 and CRD4, though with lower confidence than the canonical domains [notes_sequence_analysis][jumper-2021-alphafold-abstract]. Everything else is conserved: CRD3, CRD4, the transmembrane segment, the membrane-proximal cytoplasmic region and the death domain. Its function therefore has to be read in two layers. The first is what TNFR1 does in general, which is well established in human and mouse. The second is what this particular exon-3-deleted variant can and cannot do, which has not been tested experimentally in any species.

TNFR1 is a single-pass type I membrane receptor. It binds trimeric TNF and lymphotoxin-α (TNF-β) through its extracellular CRDs [loetscher-1990-cloning-abstract][schall-1990-cloning-abstract][banner-1993-crystal-abstract]. Its cytoplasmic death domain then recruits the adaptor TRADD [hsu-1995-tradd-abstract][tartaglia-1993-death-domain-abstract]. From that point TNFR1 assembles a membrane-bound, pro-survival signalling complex (complex I: TRADD, RIPK1, TRAF2, cIAPs and LUBAC) that activates NF-κB and MAPK pathways [micheau-2003-two-complexes-abstract][haas-2009-lubac-abstract]. When NF-κB-dependent protection fails, a secondary cytoplasmic complex containing FADD and caspase-8 forms instead and drives apoptosis [micheau-2003-two-complexes-abstract]. If caspase-8 is unavailable, RIPK3 and MLKL drive necroptosis [vandenabeele-2010-necroptosis-abstract][murphy-2013-mlkl-abstract]. The receptor sits at the plasma membrane and in a large trans-Golgi pool, and it is released as soluble TNFR1 through shedding and vesicle release [jones-1999-golgi-abstract][hawari-2004-exosome-abstract][peschon-1998-tace-abstract]. In horses, the only direct evidence is tissue-level: TNFR1 is expressed in the corpus luteum and the placenta, and in the placenta it is the predominant TNF receptor [galvao-2012-equine-cl-abstract][fedorka-2022-equine-placenta-abstract]. No study of the donkey protein itself was found.

## 2. Identity verification and gene model of A0A9L0JKX4

The UniProt record gives a 29-residue signal peptide, a mature chain of residues 30–410, a helical transmembrane segment at 172–194, two TNFR-Cys repeats (43–82 and 83–126) and a death domain at 311–396 [uniprot-A0A9L0JKX4-entry]. Its InterPro, Pfam, SMART and PANTHER signatures are TNFRSF1A-specific (IPR052493; PTHR46861:SF1), and its CDD hit is the TNFR1 death-domain model (cd08313) [uniprot-A0A9L0JKX4-entry]. These signatures settle the symbol: the protein is TNFR1 and not another TNFR superfamily member. UniProt also attaches a caution: the entry "lacks conserved residue(s) required for the propagation of feature annotation" (PROSITE-ProRule PRU00206), and only two cysteine-rich repeats are annotated, compared with four in the human reviewed entry [uniprot-A0A9L0JKX4-entry][uniprot-P19438-entry]. Both oddities are explained by the gene model.

The donkey TNFRSF1A gene has two protein-coding transcripts in Ensembl. The canonical transcript (ENSEAST00005025834) has 10 exons and encodes a 453-residue protein (A0A8C4MD74). The second transcript (ENSEAST00005054546), which encodes A0A9L0JKX4, is identical except that exon 3 is missing [notes_sequence_analysis]. Human TNFRSF1A has the same 10-exon architecture, with an exon 3 of exactly 129 nucleotides [notes_sequence_analysis]. Exon 3 therefore encodes the same segment in both species. In human it contains Thr79, the site of the TRAPS-associated variant p.(Thr79Met) (T50M in mature-protein numbering), which Rittore et al. located in exon 3 [rittore-2021-tnfr1-d2-fulltext]. The alignment confirms that the 43 missing residues correspond to human 64–106 [notes_sequence_analysis].

The gap removes the cysteines at human positions 72, 81, 84, 99, 102 and 105. That deletion breaks both of the second and third CRD1 disulfides (59–72 and 62–81) and all three CRD2 disulfides (84–99, 102–117 and 105–125) annotated in the human structure, and orphans Cys59, Cys62, Cys117 and Cys125 from their canonical partners [uniprot-P19438-entry][notes_sequence_analysis]. The TNFR1 ectodomain is an end-to-end array of four disulfide-rich CRDs [banner-1993-crystal-abstract][naismith-1995-dimer-abstract]. In humans, single missense mutations that disrupt these conserved disulfides cause autoinflammatory disease [mcdermott-1999-traps-abstract]. Such mutant receptors form abnormal disulfide-linked oligomers, fail to bind TNF and are retained in the endoplasmic reticulum [lobito-2006-traps-er-abstract]. Taken alone, that precedent would predict a misfolded donkey isoform.

The AlphaFold models suggest a less damaging outcome. AlphaFold builds a confident 3D model of the canonical donkey receptor (A0A8C4MD74) with all twelve human-like disulfides in geometric position. In the exon-3-skipped protein, it predicts a different solution: the orphaned CRD1 cysteines (Cys59 and Cys62) pair with the orphaned CRD2 cysteines (canonical Cys117 and Cys125). That produces nine disulfides with no unpaired extracellular cysteine, in an ectodomain made of a hybrid CRD1/CRD2 module followed by intact CRD3 and CRD4 [notes_sequence_analysis][jumper-2021-alphafold-abstract]. Exon 3 therefore appears to be bounded at positions where a TNFR-Cys module can be fused in frame. Confidence in the hybrid module (mean pLDDT about 69–80) is clearly below that of canonical CRD1 and CRD2 (92–96) [notes_sequence_analysis]. The prediction is a hypothesis for experiment, not evidence that the protein folds.

Whether the transcript is real is a separate question. The donkey isoform was produced by the automated Ensembl pipeline on the ASM1607732v2 assembly [martin-2023-ensembl-abstract][notes_sequence_analysis]. In human, the equivalent exon-3-skipped transcript (ENST00000540022, TNFRSF1A-212; UniProt F5H061) is a manually curated HAVANA model, and Ensembl cross-references it to RefSeq NM_001346091 [uniprot-F5H061-entry][notes_sequence_analysis]. The RefSeq record, however, is derived from the TNFR1-d2 clone (JN172914) of Rittore et al. and is supported by cDNA AK298729 [refseq-NM_001346091-entry]. Direct alignment shows that both of these cDNAs lack exon 2 and keep exon 3 [notes_sequence_analysis]. So the best-documented human splice variant at this locus skips exon 2. The evidence behind the exon-3-skip model could not be traced, and no donkey or horse RNA evidence for exon-3 skipping was found. The most cautious reading is that A0A9L0JKX4 is a plausible but unverified isoform.

## 3. Domain architecture and ligand recognition by the TNFR1 ectodomain

TNFR1 was first cloned from human HL60 cells and placenta. Loetscher et al. found a 455-residue precursor with leader, extracellular, transmembrane and intracellular domains, and an extracellular region similar to the NGF receptor [loetscher-1990-cloning-abstract]. Schall et al. independently cloned it from a serum TNF-binding protein. They showed that cells expressing the receptor bind TNF-α, that TNF-α and TNF-β (lymphotoxin-α) are equally good competitors, and that the soluble serum TNF-binding protein is probably cut from the membrane receptor [schall-1990-cloning-abstract]. The 2.85 Å crystal structure of the TNFR1 ectodomain bound to TNF-β showed three receptor chains bound symmetrically to one ligand trimer. Each receptor is an elongated array of four similar cysteine-rich folding domains and sits in the groove between two adjacent ligand subunits [banner-1993-crystal-abstract]. That geometry is the structural basis for activation by ligand-driven clustering of receptor cytoplasmic tails [banner-1993-crystal-abstract]. Unliganded TNFR1 ectodomains also form parallel and antiparallel dimers, which suggests that the receptor self-associates before ligand arrives [naismith-1995-dimer-abstract]. A structural review of the superfamily brings these observations together. The basic signalling unit is one trimeric ligand bound by three receptors, each at the interface between two ligand monomers. Resting receptors may be pre-arranged in a non-signalling network of antiparallel dimers, and efficient signalling requires higher-order clustering [vanamee-2018-tnfsf-structure-abstract].

Chan et al. located this ligand-independent association in a pre-ligand-binding assembly domain (PLAD) in the membrane-distal CRD1. The PLAD is physically separate from the major ligand contacts, yet it is necessary and sufficient for assembling TNFR complexes that bind TNF and signal [chan-2000-plad-abstract]. Later work describes the PLAD/CRD1 as needed both for receptor homotrimerization and for holding CRD2 in a conformation that allows ligand-induced activation [rittore-2021-tnfr1-d2-fulltext]. The deleted segment in A0A9L0JKX4 therefore runs straight through the PLAD and the start of CRD2. On structural grounds, the variant would be expected to have reduced or absent TNF binding and impaired pre-assembly. This inference has not been measured. TRAPS mutants show how sensitive this region is: misfolded CRD1/CRD2 mutants lose TNF binding and can no longer associate with wild-type TNFR1 through the PLAD [lobito-2006-traps-er-abstract].

The closest experimental analogue is the human TNFR1-d2 isoform. It comes from skipping exon 2, not exon 3. That skip causes a frameshift, and translation restarts at an internal methionine (M109), giving a receptor that lacks CRD1 and most of CRD2 [rittore-2014-exon2-abstract][rittore-2021-tnfr1-d2-fulltext]. TNFR1-d2 is expressed in a tissue-specific way, whereas full-length TNFR1 is expressed everywhere [rittore-2014-exon2-abstract]. It localizes close to TNFR1, can interact with TNFR1 and forms pre-assembled clusters at the cell surface, but it does not activate NF-κB [rittore-2021-tnfr1-d2-fulltext]. By analogy, the donkey exon-3-skipped protein might also be a non-signalling or modulatory receptor. Two differences limit the comparison: the donkey variant keeps the signal peptide and the N-terminal part of CRD1, and it gives up a different internal segment.

## 4. Intracellular signalling: from the death domain to survival, inflammation and death

The cytoplasmic side of A0A9L0JKX4 is intact and closely matches human TNFR1, including the C-terminal death domain [notes_sequence_analysis]. Deletion and alanine-scanning work by Tartaglia et al. defined the ~80-residue death domain, which resembles the cytoplasmic region of Fas. It is required for TNF-induced cytotoxicity, the antiviral response and induction of nitric oxide synthase. The membrane-proximal cytoplasmic region separately contributes to NOS induction [tartaglia-1993-death-domain-abstract]. NMR studies show that the TNFR1 death domain folds as a bundle of six antiparallel α-helices. Mutagenesis identified two opposite surfaces, centred on helix α2 and parts of α3 and α4. These surfaces mediate both death-domain self-association and TRADD binding, and binding activity tracks cytotoxic activity [telliez-2000-dd-nmr-abstract][sukits-2001-dd-structure-abstract]. The death domain's first binding partner is TRADD, a 34 kDa adaptor whose own C-terminal death domain binds the TNFR1 death domain. TRADD can trigger both apoptosis and NF-κB activation, and the two outputs are pharmacologically separable [hsu-1995-tradd-abstract]. TRADD then binds TRAF2 and FADD directly. Dominant-negative mutants show that NF-κB activation (through TRAF2) and apoptosis (through FADD) split at TRADD [hsu-1996-tradd-traf2-fadd-abstract]. Further dissection placed JNK and NF-κB activation downstream of RIP (RIPK1) and TRAF2, and apoptosis downstream of FADD, and showed that NF-κB activation protects cells from TNF-induced death [liu-1996-dissection-abstract]. Mouse genetics support this order. RIP-deficient cells cannot activate NF-κB and become hypersensitive to TNF-induced death [kelliher-1998-rip-abstract]. TRADD-deficient cells lose TNF-induced apoptosis, TRAF2 recruitment and RIP1 ubiquitination at TNFR1, and NF-κB and MAPK signalling is strongly reduced [ermolaeva-2008-tradd-abstract].

Micheau and Tschopp combined these results into the two-complex model. Complex I forms at the plasma membrane from TNFR1, TRADD, RIP1 and TRAF2 and quickly activates NF-κB. A second, cytoplasmic complex (complex II) then forms, in which TRADD and RIP1 associate with FADD and caspase-8. If NF-κB has induced FLIP(L), complex II is inhibited and the cell survives. If not, caspase-8 activation commits the cell to apoptosis [micheau-2003-two-complexes-abstract]. Complex I is held together by ubiquitination. cIAP E3 ligase activity, together with TRADD and TRAF2, recruits LUBAC (HOIL-1/HOIP). LUBAC adds linear ubiquitin chains to NEMO, stabilizes the TNF-receptor signalling complex, and is needed for efficient NF-κB and JNK activation and for protection against apoptosis [haas-2009-lubac-abstract]. K63- and M1-linked chains on RIPK1 recruit TAK1 (through TAB2/TAB3) and the IKK complex (through NEMO). TAK1 phosphorylates IKKβ to drive canonical NF-κB, and also activates the MAPK kinases upstream of JNK and p38. The deubiquitinase CYLD, itself induced by NF-κB, removes these chains from RIPK1, which lets RIPK1 leave the receptor and seed complex II [gough-2020-review-fulltext]. When caspase-8 is inhibited or absent, TNFR1 can instead drive RIPK1/RIPK3-dependent programmed necrosis (necroptosis) [vandenabeele-2010-necroptosis-abstract]. The executioner is the pseudokinase MLKL, which RIPK3 activates by phosphorylation [murphy-2013-mlkl-abstract]. Reviews describe this survival, apoptosis and necroptosis branching as the central logic of TNFR1 signalling, and contrast it with TNFR2, which has no death domain [brenner-2015-review-abstract][gough-2020-review-abstract].

TNFR1 also signals through lipids. Distinct cytoplasmic regions activate a membrane-associated neutral sphingomyelinase and an endosomal acid sphingomyelinase, each feeding separate downstream pathways [wiegmann-1994-smase-abstract]. The WD-repeat adaptor FAN binds a nine-residue motif just upstream of the death domain, the N-SMase activation domain, and couples TNFR1 to ceramide production by neutral sphingomyelinase [adamklages-1996-fan-abstract][uniprot-P19438-entry]. Because the cytoplasmic region of A0A9L0JKX4 is intact, the donkey variant should keep the ability to bind TRADD and the other adaptors whenever its death domains are clustered. The open question is whether the damaged ectodomain can bind ligand well enough to cluster them.

## 5. Subcellular localization, trafficking and soluble forms

TNFR1 is a single-pass type I membrane protein. UniProt places human TNFR1 at the plasma membrane and the Golgi membrane, with a secreted soluble form [uniprot-P19438-entry]. In unstimulated monocytic and endothelial cells most TNFR1 sits in the trans-Golgi network, with a smaller fraction on the cell surface. After exogenous TNF is added, TRADD binds TNFR1 within a minute, but only at the plasma membrane and not in the Golgi pool [jones-1999-golgi-abstract]. Full-length TNFR1 also localizes to the Golgi in other studies, whereas a soluble splice isoform that lacks the transmembrane and cytoplasmic regions is spread diffusely through the cell, which fits a Golgi-retention signal located in the cytoplasmic region [gregory-2012-ms-fulltext]. Human TNFR1-d2, which lacks the N-terminal CRDs, still co-localizes with full-length TNFR1 and the Golgi apparatus [rittore-2021-tnfr1-d2-fulltext]. This suggests that the transmembrane and cytoplasmic parts, which the donkey isoform keeps, are enough to target it to the same compartments, provided the ectodomain passes ER quality control. TRAPS mutants show what happens when it does not. Receptors with misfolded CRD1/CRD2 regions are retained intracellularly with ER markers and are neither shed nor released on exosomes [lobito-2006-traps-er-abstract]. Even from that intracellular location they amplify LPS-induced MAPK activation and cytokine secretion in myeloid cells, in a way that depends on autocrine TNF and wild-type TNFR1 [simon-2010-traps-concerted-abstract]. If the exon-3-skipped donkey protein were made and misfolded, this is the precedent for how it could affect signalling.

Where the receptor sits in the cell also helps decide what it signals. TNF-bound TNFR1 is internalized into endocytic "receptosomes". Endocytosis requires a TNFR1 internalization domain (TRID), and the TRADD/FADD/caspase-8 death-inducing complex assembles on these internalized vesicles. RIP1 and TRAF2, by contrast, are recruited at the plasma membrane. When receptosomes fuse with trans-Golgi vesicles, acid sphingomyelinase and cathepsin D are activated [schneiderbrachert-2004-receptosome-abstract]. Soluble TNFR1 is produced in two ways. The first is ectodomain shedding by the metalloprotease TACE/ADAM17: TACE-deficient cells fail to shed a TNF receptor, among other substrates [peschon-1998-tace-abstract]. The second is constitutive release of full-length 55 kDa TNFR1 on exosome-like vesicles, which turns out to be the main soluble TNFR1 species in human serum and lung lining fluid [hawari-2004-exosome-abstract]. Soluble receptor can neutralize TNF. In TRAPS, impaired shedding and lower soluble TNFR1 have been proposed to contribute to disease [mcdermott-1999-traps-abstract]. An alternatively spliced soluble isoform (Δ6-TNFR1) blocks TNF and links TNFRSF1A to multiple sclerosis risk [gregory-2012-ms-abstract].

## 6. Physiological roles and evidence from equids

Gene-knockout studies in mice show that TNFR1 carries most TNF signalling. TNFR1-deficient mice develop normal lymphoid compartments but lose TNF-induced NF-κB activation in T cells. They resist lethal endotoxin and superantigen shock, yet are very susceptible to *Listeria monocytogenes* [pfeffer-1993-knockout-abstract][rothe-1993-knockout-abstract]. In humans, heterozygous missense variants in the TNFR1 ectodomain, mostly ones that disrupt conserved disulfides in CRD1 and CRD2, cause TNF receptor-associated periodic syndrome (TRAPS), an autosomal dominant autoinflammatory disease [mcdermott-1999-traps-abstract][rittore-2021-tnfr1-d2-fulltext]. This matters for the donkey isoform, because its 43-residue deletion removes the same CRD1/CRD2 disulfide region where TRAPS mutations cluster.

Equid-specific data are limited to expression and physiology in the horse (*Equus caballus*). In the mare corpus luteum, TNF, TNFRI and TNFRII are found in steroidogenic and endothelial luteal cells. TNFRI protein rises in the regressing corpus luteum, and TNF changes progesterone and prostaglandin output in a stage-dependent way [galvao-2012-equine-cl-abstract]. In the equine placenta, RNA sequencing and immunohistochemistry identify TNFR-1 as the predominant TNF receptor during healthy pregnancy. In experimentally induced ascending placentitis, TNF rises in maternal serum and TNFR-1 signalling within the chorioallantois is associated with pro-apoptotic and necroptotic transcriptional outcomes [fedorka-2022-equine-placenta-abstract]. These studies agree with the human and mouse model of TNFR1 as the main death-domain TNF receptor in equids. None of them separates the canonical from the exon-3-skipped isoform, and none was done in donkeys.

## 7. Functional annotation synthesis

The evidence indicates that the donkey TNFRSF1A gene encodes a cytokine receptor for TNF and lymphotoxin-α, found at the cell surface and in the Golgi. Its main molecular function is TNF receptor activity: a ligand-binding ectodomain linked through a single transmembrane helix to a death domain that serves as a scaffold for adaptor proteins. The receptor sits upstream of the canonical NF-κB, MAPK (JNK and p38), extrinsic apoptotic (caspase-8) and necroptotic pathways [banner-1993-crystal-abstract][hsu-1995-tradd-abstract][micheau-2003-two-complexes-abstract][brenner-2015-review-abstract][gough-2020-review-fulltext]. The GO terms already attached to A0A9L0JKX4 are tumor necrosis factor receptor activity, tumor necrosis factor binding, membrane raft, signaling receptor complex and inflammatory response, all inferred electronically. They fit the canonical gene product [uniprot-A0A9L0JKX4-entry].

For the exon-3-skipped isoform itself, the evidence is uneven. Several assignments rest on intact, conserved sequence: the transmembrane helix, the cytoplasmic region with its N-SMase activation motif and death domain, and the resulting membrane and Golgi localization [notes_sequence_analysis][tartaglia-1993-death-domain-abstract][adamklages-1996-fan-abstract]. TNF binding is the least secure inference. It depends on a properly folded CRD1–CRD2 region, and that region is replaced in this isoform by a hybrid module that AlphaFold predicts only with moderate confidence [notes_sequence_analysis]. Experimental analogues point in two directions. A human isoform lacking CRD1 and most of CRD2 (TNFR1-d2) still clusters with full-length TNFR1 but does not activate NF-κB on its own [rittore-2021-tnfr1-d2-fulltext]. Human receptors with misfolded CRD1/CRD2 regions are retained in the ER, do not bind TNF, and modulate inflammation indirectly [lobito-2006-traps-er-abstract][simon-2010-traps-concerted-abstract]. Transcript support for exon-3 skipping is also uncertain, because the cDNA evidence cited for the human locus documents exon-2 skipping instead [notes_sequence_analysis][refseq-NM_001346091-entry]. A careful curator would therefore apply the orthology-based TNFR1 annotations at the gene level. For this predicted isoform, the curator would keep the cellular-component and death-domain-dependent signalling terms as inferences, and would not assert TNF-binding activity without experimental support.

## Open Questions

The first question is whether the exon-3-skipped transcript exists in donkey tissues and in what amount. RT-PCR spanning exons 2–4, or a re-analysis of public donkey and horse RNA-seq for reads joining exon 2 directly to exon 4, would show whether ENSEAST00005054546 is a real alternative isoform or an annotation artefact. The same check is warranted in horse (A0A5F5PQM0). In human, the evidence that supports the HAVANA model ENST00000540022 / F5H061 should be traced and set against the well-documented exon-2-skipped TNFR1-d2. The Ensembl cross-reference between ENST00000540022 and the TNFR1-d2-derived RefSeq NM_001346091 looks like a mismatch and should be reported to the annotation groups.

The second question is whether the protein folds and reaches the membrane. AlphaFold predicts that the exon-3-skipped ectodomain re-pairs its orphaned cysteines (Cys59–Cys117 and Cys62–Cys125 in canonical numbering) into a hybrid CRD1/CRD2 module, but with moderate confidence. Expression of a tagged donkey isoform in cultured cells, together with non-reducing SDS-PAGE, could test this. Glycosidase sensitivity and co-localization with ER and Golgi markers would show whether the protein clears ER quality control, or instead behaves like TRAPS cysteine mutants that form disulfide-linked aggregates in the ER. Mass-spectrometric disulfide mapping would test the predicted pairing directly.

The third question is how the variant behaves towards TNF and lymphotoxin-α, and towards the full-length receptor. Ligand-binding assays would address the first. Co-expression with full-length donkey TNFR1, reading out PLAD-mediated association, NF-κB activation and TNF-induced death, would show whether the isoform is inert, a decoy, or a dominant modulator. Those results would place it relative to human TNFR1-d2 and Δ6-TNFR1.

Beyond the isoform, the canonical donkey receptor (A0A8C4MD74) has not been characterized. Its affinity for equine TNF, its signalling outputs and its tissue distribution are unreported. Equid-specific coding variation in TNFRSF1A, and possible links to inflammatory conditions in donkeys such as laminitis or reproductive inflammation, are also unexplored. They could be examined with the donkey population-genomic resources [wang-2020-donkey-genome-abstract].

## References

* **adamklages-1996-fan-abstract** — Adam-Klages S, Adam D, Wiegmann K, Struve S, Kolanus W, Schneider-Mergener J et al. FAN, a novel WD-repeat protein, couples the p55 TNF-receptor to neutral sphingomyelinase. *Cell 1996;86:937-47*. PMID: 8808629; DOI: 10.1016/s0092-8674(00)80169-5 (https://doi.org/10.1016/s0092-8674(00)80169-5); https://pubmed.ncbi.nlm.nih.gov/8808629/
* **banner-1993-crystal-abstract** — Banner DW, D'Arcy A, Janes W, Gentz R, Schoenfeld HJ, Broger C et al. Crystal structure of the soluble human 55 kd TNF receptor-human TNF beta complex: implications for TNF receptor activation. *Cell 1993;73:431-45*. PMID: 8387891; DOI: 10.1016/0092-8674(93)90132-a (https://doi.org/10.1016/0092-8674(93)90132-a); https://pubmed.ncbi.nlm.nih.gov/8387891/
* **brenner-2015-review-abstract** — Brenner D, Blaser H, Mak TW. Regulation of tumour necrosis factor signalling: live or let die. *Nature reviews. Immunology 2015;15:362-74*. PMID: 26008591; DOI: 10.1038/nri3834 (https://doi.org/10.1038/nri3834); https://pubmed.ncbi.nlm.nih.gov/26008591/
* **chan-2000-plad-abstract** — Chan FK, Chun HJ, Zheng L, Siegel RM, Bui KL, Lenardo MJ. A domain in TNF receptors that mediates ligand-independent receptor assembly and signaling. *Science (New York, N.Y.) 2000;288:2351-4*. PMID: 10875917; DOI: 10.1126/science.288.5475.2351 (https://doi.org/10.1126/science.288.5475.2351); https://pubmed.ncbi.nlm.nih.gov/10875917/
* **ermolaeva-2008-tradd-abstract** — Ermolaeva MA, Michallet MC, Papadopoulou N, Utermöhlen O, Kranidioti K, Kollias G et al. Function of TRADD in tumor necrosis factor receptor 1 signaling and in TRIF-dependent inflammatory responses. *Nature immunology 2008;9:1037-46*. PMID: 18641654; DOI: 10.1038/ni.1638 (https://doi.org/10.1038/ni.1638); https://pubmed.ncbi.nlm.nih.gov/18641654/
* **fedorka-2022-equine-placenta-abstract** — Fedorka CE, El-Sheikh Ali H, Scoggin KE, Loux SC, Ball BA, Troedsson MHT. Tumor necrosis factor signaling during equine placental infection leads to pro-apoptotic and necroptotic outcomes. *Journal of reproductive immunology 2022;152:103655*. PMID: 35716439; DOI: 10.1016/j.jri.2022.103655 (https://doi.org/10.1016/j.jri.2022.103655); https://pubmed.ncbi.nlm.nih.gov/35716439/
* **galvao-2012-equine-cl-abstract** — Galvão A, Skarzynski DJ, Szóstek A, Silva E, Tramontano A, Mollo A et al. Cytokines tumor necrosis factor-α and interferon-γ participate in modulation of the equine corpus luteum as autocrine and paracrine factors. *Journal of reproductive immunology 2012;93:28-37*. PMID: 22186103; DOI: 10.1016/j.jri.2011.11.002 (https://doi.org/10.1016/j.jri.2011.11.002); https://pubmed.ncbi.nlm.nih.gov/22186103/
* **gough-2020-review-abstract** — Gough P, Myles IA. Tumor Necrosis Factor Receptors: Pleiotropic Signaling Complexes and Their Differential Effects. *Frontiers in immunology 2020;11:585880*. PMID: 33324405; PMCID: PMC7723893; DOI: 10.3389/fimmu.2020.585880 (https://doi.org/10.3389/fimmu.2020.585880); https://pubmed.ncbi.nlm.nih.gov/33324405/
* **gough-2020-review-fulltext** — Gough P, Myles IA. Tumor Necrosis Factor Receptors: Pleiotropic Signaling Complexes and Their Differential Effects. *Frontiers in immunology 2020;11:585880*. PMID: 33324405; PMCID: PMC7723893; DOI: 10.3389/fimmu.2020.585880 (https://doi.org/10.3389/fimmu.2020.585880); https://pubmed.ncbi.nlm.nih.gov/33324405/
* **gregory-2012-ms-abstract** — Gregory AP, Dendrou CA, Attfield KE, Haghikia A, Xifara DK, Butter F et al. TNF receptor 1 genetic risk mirrors outcome of anti-TNF therapy in multiple sclerosis. *Nature 2012;488:508-511*. PMID: 22801493; PMCID: PMC4268493; DOI: 10.1038/nature11307 (https://doi.org/10.1038/nature11307); https://pubmed.ncbi.nlm.nih.gov/22801493/
* **gregory-2012-ms-fulltext** — Gregory AP, Dendrou CA, Attfield KE, Haghikia A, Xifara DK, Butter F et al. TNF receptor 1 genetic risk mirrors outcome of anti-TNF therapy in multiple sclerosis. *Nature 2012;488:508-511*. PMID: 22801493; PMCID: PMC4268493; DOI: 10.1038/nature11307 (https://doi.org/10.1038/nature11307); https://pubmed.ncbi.nlm.nih.gov/22801493/
* **haas-2009-lubac-abstract** — Haas TL, Emmerich CH, Gerlach B, Schmukle AC, Cordier SM, Rieser E et al. Recruitment of the linear ubiquitin chain assembly complex stabilizes the TNF-R1 signaling complex and is required for TNF-mediated gene induction. *Molecular cell 2009;36:831-44*. PMID: 20005846; DOI: 10.1016/j.molcel.2009.10.013 (https://doi.org/10.1016/j.molcel.2009.10.013); https://pubmed.ncbi.nlm.nih.gov/20005846/
* **hawari-2004-exosome-abstract** — Hawari FI, Rouhani FN, Cui X, Yu ZX, Buckley C, Kaler M et al. Release of full-length 55-kDa TNF receptor 1 in exosome-like vesicles: a mechanism for generation of soluble cytokine receptors. *Proceedings of the National Academy of Sciences of the United States of America 2004;101:1297-302*. PMID: 14745008; PMCID: PMC337047; DOI: 10.1073/pnas.0307981100 (https://doi.org/10.1073/pnas.0307981100); https://pubmed.ncbi.nlm.nih.gov/14745008/
* **hsu-1995-tradd-abstract** — Hsu H, Xiong J, Goeddel DV. The TNF receptor 1-associated protein TRADD signals cell death and NF-kappa B activation. *Cell 1995;81:495-504*. PMID: 7758105; DOI: 10.1016/0092-8674(95)90070-5 (https://doi.org/10.1016/0092-8674(95)90070-5); https://pubmed.ncbi.nlm.nih.gov/7758105/
* **hsu-1996-tradd-traf2-fadd-abstract** — Hsu H, Shu HB, Pan MG, Goeddel DV. TRADD-TRAF2 and TRADD-FADD interactions define two distinct TNF receptor 1 signal transduction pathways. *Cell 1996;84:299-308*. PMID: 8565075; DOI: 10.1016/s0092-8674(00)80984-8 (https://doi.org/10.1016/s0092-8674(00)80984-8); https://pubmed.ncbi.nlm.nih.gov/8565075/
* **jones-1999-golgi-abstract** — Jones SJ, Ledgerwood EC, Prins JB, Galbraith J, Johnson DR, Pober JS et al. TNF recruits TRADD to the plasma membrane but not the trans-Golgi network, the principal subcellular location of TNF-R1. *Journal of immunology (Baltimore, Md. : 1950) 1999;162:1042-8*. PMID: 9916731; https://pubmed.ncbi.nlm.nih.gov/9916731/
* **jumper-2021-alphafold-abstract** — Jumper J, Evans R, Pritzel A, Green T, Figurnov M, Ronneberger O et al. Highly accurate protein structure prediction with AlphaFold. *Nature 2021;596:583-589*. PMID: 34265844; PMCID: PMC8371605; DOI: 10.1038/s41586-021-03819-2 (https://doi.org/10.1038/s41586-021-03819-2); https://pubmed.ncbi.nlm.nih.gov/34265844/
* **kelliher-1998-rip-abstract** — Kelliher MA, Grimm S, Ishida Y, Kuo F, Stanger BZ, Leder P. The death domain kinase RIP mediates the TNF-induced NF-kappaB signal. *Immunity 1998;8:297-303*. PMID: 9529147; DOI: 10.1016/s1074-7613(00)80535-x (https://doi.org/10.1016/s1074-7613(00)80535-x); https://pubmed.ncbi.nlm.nih.gov/9529147/
* **liu-1996-dissection-abstract** — Liu ZG, Hsu H, Goeddel DV, Karin M. Dissection of TNF receptor 1 effector functions: JNK activation is not linked to apoptosis while NF-kappaB activation prevents cell death. *Cell 1996;87:565-76*. PMID: 8898208; DOI: 10.1016/s0092-8674(00)81375-6 (https://doi.org/10.1016/s0092-8674(00)81375-6); https://pubmed.ncbi.nlm.nih.gov/8898208/
* **lobito-2006-traps-er-abstract** — Lobito AA, Kimberley FC, Muppidi JR, Komarow H, Jackson AJ, Hull KM et al. Abnormal disulfide-linked oligomerization results in ER retention and altered signaling by TNFR1 mutants in TNFR1-associated periodic fever syndrome (TRAPS). *Blood 2006;108:1320-7*. PMID: 16684962; PMCID: PMC1895878; DOI: 10.1182/blood-2005-11-006783 (https://doi.org/10.1182/blood-2005-11-006783); https://pubmed.ncbi.nlm.nih.gov/16684962/
* **loetscher-1990-cloning-abstract** — Loetscher H, Pan YC, Lahm HW, Gentz R, Brockhaus M, Tabuchi H et al. Molecular cloning and expression of the human 55 kd tumor necrosis factor receptor. *Cell 1990;61:351-9*. PMID: 2158862; DOI: 10.1016/0092-8674(90)90815-v (https://doi.org/10.1016/0092-8674(90)90815-v); https://pubmed.ncbi.nlm.nih.gov/2158862/
* **martin-2023-ensembl-abstract** — Martin FJ, Amode MR, Aneja A, Austine-Orimoloye O, Azov AG, Barnes I et al. Ensembl 2023. *Nucleic acids research 2023;51:D933-D941*. PMID: 36318249; PMCID: PMC9825606; DOI: 10.1093/nar/gkac958 (https://doi.org/10.1093/nar/gkac958); https://pubmed.ncbi.nlm.nih.gov/36318249/
* **mcdermott-1999-traps-abstract** — McDermott MF, Aksentijevich I, Galon J, McDermott EM, Ogunkolade BW, Centola M et al. Germline mutations in the extracellular domains of the 55 kDa TNF receptor, TNFR1, define a family of dominantly inherited autoinflammatory syndromes. *Cell 1999;97:133-44*. PMID: 10199409; DOI: 10.1016/s0092-8674(00)80721-7 (https://doi.org/10.1016/s0092-8674(00)80721-7); https://pubmed.ncbi.nlm.nih.gov/10199409/
* **micheau-2003-two-complexes-abstract** — Micheau O, Tschopp J. Induction of TNF receptor I-mediated apoptosis via two sequential signaling complexes. *Cell 2003;114:181-90*. PMID: 12887920; DOI: 10.1016/s0092-8674(03)00521-x (https://doi.org/10.1016/s0092-8674(03)00521-x); https://pubmed.ncbi.nlm.nih.gov/12887920/
* **murphy-2013-mlkl-abstract** — Murphy JM, Czabotar PE, Hildebrand JM, Lucet IS, Zhang JG, Alvarez-Diaz S et al. The pseudokinase MLKL mediates necroptosis via a molecular switch mechanism. *Immunity 2013;39:443-53*. PMID: 24012422; DOI: 10.1016/j.immuni.2013.06.018 (https://doi.org/10.1016/j.immuni.2013.06.018); https://pubmed.ncbi.nlm.nih.gov/24012422/
* **naismith-1995-dimer-abstract** — Naismith JH, Devine TQ, Brandhuber BJ, Sprang SR. Crystallographic evidence for dimerization of unliganded tumor necrosis factor receptor. *The Journal of biological chemistry 1995;270:13303-7*. PMID: 7768931; DOI: 10.1074/jbc.270.22.13303 (https://doi.org/10.1074/jbc.270.22.13303); https://pubmed.ncbi.nlm.nih.gov/7768931/
* **notes_sequence_analysis** — Research agent's own analyses (Biopython pairwise alignments of proteins and cDNAs; Ensembl REST lookups of ENSEASG00005016176, ENSG00000067182, ENST00000540022; AlphaFold DB v6 model analysis of AF-A0A9L0JKX4-F1 and AF-A0A8C4MD74-F1), file `notes_sequence_analysis.md`. Ensembl REST: https://rest.ensembl.org/lookup/id/ENSEASG00005016176 ; AlphaFold: https://alphafold.ebi.ac.uk/files/AF-A0A9L0JKX4-F1-model_v6.pdb
* **peschon-1998-tace-abstract** — Peschon JJ, Slack JL, Reddy P, Stocking KL, Sunnarborg SW, Lee DC et al. An essential role for ectodomain shedding in mammalian development. *Science (New York, N.Y.) 1998;282:1281-4*. PMID: 9812885; DOI: 10.1126/science.282.5392.1281 (https://doi.org/10.1126/science.282.5392.1281); https://pubmed.ncbi.nlm.nih.gov/9812885/
* **pfeffer-1993-knockout-abstract** — Pfeffer K, Matsuyama T, Kündig TM, Wakeham A, Kishihara K, Shahinian A et al. Mice deficient for the 55 kd tumor necrosis factor receptor are resistant to endotoxic shock, yet succumb to L. monocytogenes infection. *Cell 1993;73:457-67*. PMID: 8387893; DOI: 10.1016/0092-8674(93)90134-c (https://doi.org/10.1016/0092-8674(93)90134-c); https://pubmed.ncbi.nlm.nih.gov/8387893/
* **refseq-NM_001346091-entry** — NCBI RefSeq NM_001346091.2, Homo sapiens TNF receptor superfamily member 1A (TNFRSF1A), transcript variant 2, mRNA (REVIEWED; derived from JN172914.1 and BC010140.2). https://www.ncbi.nlm.nih.gov/nuccore/NM_001346091 (local copy `citations/refseq-NM_001346091-entry.gb`)
* **rittore-2014-exon2-abstract** — Rittore C, Sanchez E, Soler S, Barat-Houari M, Albers M, Obici L et al. Identification of a new exon 2-skipped TNFR1 transcript: regulation by three functional polymorphisms of the TNFR-associated periodic syndrome (TRAPS) gene. *Annals of the rheumatic diseases 2014;73:290-7*. PMID: 23505244; DOI: 10.1136/annrheumdis-2012-203023 (https://doi.org/10.1136/annrheumdis-2012-203023); https://pubmed.ncbi.nlm.nih.gov/23505244/
* **rittore-2021-tnfr1-d2-fulltext** — Rittore C, Méchin D, Sanchez E, Marinèche L, Ea V, Soler S et al. TNFR1-d2 carrying the p.(Thr79Met) pathogenic variant is a potential novel actor of TNFα/TNFR1 signalling regulation in the pathophysiology of TRAPS. *Scientific reports 2021;11:4172*. PMID: 33603056; PMCID: PMC7893027; DOI: 10.1038/s41598-021-83539-9 (https://doi.org/10.1038/s41598-021-83539-9); https://pubmed.ncbi.nlm.nih.gov/33603056/
* **rothe-1993-knockout-abstract** — Rothe J, Lesslauer W, Lötscher H, Lang Y, Koebel P, Köntgen F et al. Mice lacking the tumour necrosis factor receptor 1 are resistant to TNF-mediated toxicity but highly susceptible to infection by Listeria monocytogenes. *Nature 1993;364:798-802*. PMID: 8395024; DOI: 10.1038/364798a0 (https://doi.org/10.1038/364798a0); https://pubmed.ncbi.nlm.nih.gov/8395024/
* **schall-1990-cloning-abstract** — Schall TJ, Lewis M, Koller KJ, Lee A, Rice GC, Wong GH et al. Molecular cloning and expression of a receptor for human tumor necrosis factor. *Cell 1990;61:361-70*. PMID: 2158863; DOI: 10.1016/0092-8674(90)90816-w (https://doi.org/10.1016/0092-8674(90)90816-w); https://pubmed.ncbi.nlm.nih.gov/2158863/
* **schneiderbrachert-2004-receptosome-abstract** — Schneider-Brachert W, Tchikov V, Neumeyer J, Jakob M, Winoto-Morbach S, Held-Feindt J et al. Compartmentalization of TNF receptor 1 signaling: internalized TNF receptosomes as death signaling vesicles. *Immunity 2004;21:415-28*. PMID: 15357952; DOI: 10.1016/j.immuni.2004.08.017 (https://doi.org/10.1016/j.immuni.2004.08.017); https://pubmed.ncbi.nlm.nih.gov/15357952/
* **simon-2010-traps-concerted-abstract** — Simon A, Park H, Maddipati R, Lobito AA, Bulua AC, Jackson AJ et al. Concerted action of wild-type and mutant TNF receptors enhances inflammation in TNF receptor 1-associated periodic fever syndrome. *Proceedings of the National Academy of Sciences of the United States of America 2010;107:9801-6*. PMID: 20457915; PMCID: PMC2906866; DOI: 10.1073/pnas.0914118107 (https://doi.org/10.1073/pnas.0914118107); https://pubmed.ncbi.nlm.nih.gov/20457915/
* **sukits-2001-dd-structure-abstract** — Sukits SF, Lin LL, Hsu S, Malakian K, Powers R, Xu GY. Solution structure of the tumor necrosis factor receptor-1 death domain. *Journal of molecular biology 2001;310:895-906*. PMID: 11453696; DOI: 10.1006/jmbi.2001.4790 (https://doi.org/10.1006/jmbi.2001.4790); https://pubmed.ncbi.nlm.nih.gov/11453696/
* **tartaglia-1993-death-domain-abstract** — Tartaglia LA, Ayres TM, Wong GH, Goeddel DV. A novel domain within the 55 kd TNF receptor signals cell death. *Cell 1993;74:845-53*. PMID: 8397073; DOI: 10.1016/0092-8674(93)90464-2 (https://doi.org/10.1016/0092-8674(93)90464-2); https://pubmed.ncbi.nlm.nih.gov/8397073/
* **telliez-2000-dd-nmr-abstract** — Telliez JB, Xu GY, Woronicz JD, Hsu S, Wu JL, Lin L et al. Mutational analysis and NMR studies of the death domain of the tumor necrosis factor receptor-1. *Journal of molecular biology 2000;300:1323-33*. PMID: 10903872; DOI: 10.1006/jmbi.2000.3899 (https://doi.org/10.1006/jmbi.2000.3899); https://pubmed.ncbi.nlm.nih.gov/10903872/
* **uniprot-A0A9L0JKX4-entry** — UniProtKB/TrEMBL A0A9L0JKX4 (A0A9L0JKX4_EQUAS), TNF receptor superfamily member 1A, Equus asinus; entry version 15 (02-SEP-2026); from Ensembl ENSEASP00005050612.1. https://rest.uniprot.org/uniprotkb/A0A9L0JKX4.txt (local copy `citations/uniprot-A0A9L0JKX4-entry.txt`)
* **uniprot-F5H061-entry** — UniProtKB/TrEMBL F5H061 (F5H061_HUMAN), TNF receptor superfamily member 1A, 412 aa, from Ensembl ENSP00000438343 (ENST00000540022). https://rest.uniprot.org/uniprotkb/F5H061.txt (local copy `citations/uniprot-F5H061-entry.txt`)
* **uniprot-P19438-entry** — UniProtKB/Swiss-Prot P19438 (TNR1A_HUMAN), Tumor necrosis factor receptor superfamily member 1A, Homo sapiens. https://rest.uniprot.org/uniprotkb/P19438.txt (local copy `citations/uniprot-P19438-entry.txt`)
* **vanamee-2018-tnfsf-structure-abstract** — Vanamee ÉS, Faustman DL. Structural principles of tumor necrosis factor superfamily signaling. *Science signaling 2018;11:None*. PMID: 29295955; DOI: 10.1126/scisignal.aao4910 (https://doi.org/10.1126/scisignal.aao4910); https://pubmed.ncbi.nlm.nih.gov/29295955/
* **vandenabeele-2010-necroptosis-abstract** — Vandenabeele P, Galluzzi L, Vanden Berghe T, Kroemer G. Molecular mechanisms of necroptosis: an ordered cellular explosion. *Nature reviews. Molecular cell biology 2010;11:700-14*. PMID: 20823910; DOI: 10.1038/nrm2970 (https://doi.org/10.1038/nrm2970); https://pubmed.ncbi.nlm.nih.gov/20823910/
* **wang-2020-donkey-genome-abstract** — Wang C, Li H, Guo Y, Huang J, Sun Y, Min J et al. Donkey genomes provide new insights into domestication and selection for coat color. *Nature communications 2020;11:6014*. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7 (https://doi.org/10.1038/s41467-020-19813-7); https://pubmed.ncbi.nlm.nih.gov/33293529/
* **wiegmann-1994-smase-abstract** — Wiegmann K, Schütze S, Machleidt T, Witte D, Krönke M. Functional dichotomy of neutral and acidic sphingomyelinases in tumor necrosis factor signaling. *Cell 1994;78:1005-15*. PMID: 7923351; DOI: 10.1016/0092-8674(94)90275-5 (https://doi.org/10.1016/0092-8674(94)90275-5); https://pubmed.ncbi.nlm.nih.gov/7923351/


## Citations

1. adamklages-1996-fan-abstract.md
2. adamklages-1996-fan-summary.md
3. alphafold-A0A8C4MD74-model.pdb
4. alphafold-A0A9L0JKX4-model.pdb
5. banner-1993-crystal-abstract.md
6. banner-1993-crystal-summary.md
7. brenner-2015-review-abstract.md
8. brenner-2015-review-summary.md
9. chan-2000-plad-abstract.md
10. chan-2000-plad-summary.md
11. ermolaeva-2008-tradd-abstract.md
12. ermolaeva-2008-tradd-summary.md
13. fedorka-2022-equine-placenta-abstract.md
14. fedorka-2022-equine-placenta-summary.md
15. galvao-2012-equine-cl-abstract.md
16. galvao-2012-equine-cl-summary.md
17. gough-2020-review-abstract.md
18. gough-2020-review-fulltext.txt
19. gough-2020-review-summary.md
20. gregory-2012-ms-abstract.md
21. gregory-2012-ms-fulltext.txt
22. gregory-2012-ms-summary.md
23. haas-2009-lubac-abstract.md
24. haas-2009-lubac-summary.md
25. hawari-2004-exosome-abstract.md
26. hawari-2004-exosome-summary.md
27. hsu-1995-tradd-abstract.md
28. hsu-1995-tradd-summary.md
29. hsu-1996-tradd-traf2-fadd-abstract.md
30. hsu-1996-tradd-traf2-fadd-summary.md
31. jones-1999-golgi-abstract.md
32. jones-1999-golgi-summary.md
33. jumper-2021-alphafold-abstract.md
34. jumper-2021-alphafold-summary.md
35. kelliher-1998-rip-abstract.md
36. kelliher-1998-rip-summary.md
37. liu-1996-dissection-abstract.md
38. liu-1996-dissection-summary.md
39. lobito-2006-traps-er-abstract.md
40. lobito-2006-traps-er-summary.md
41. loetscher-1990-cloning-abstract.md
42. loetscher-1990-cloning-summary.md
43. martin-2023-ensembl-abstract.md
44. martin-2023-ensembl-summary.md
45. mcdermott-1999-traps-abstract.md
46. mcdermott-1999-traps-summary.md
47. micheau-2003-two-complexes-abstract.md
48. micheau-2003-two-complexes-summary.md
49. murphy-2013-mlkl-abstract.md
50. murphy-2013-mlkl-summary.md
51. naismith-1995-dimer-abstract.md
52. naismith-1995-dimer-summary.md
53. peschon-1998-tace-abstract.md
54. peschon-1998-tace-summary.md
55. pfeffer-1993-knockout-abstract.md
56. pfeffer-1993-knockout-summary.md
57. refseq-NM_001346091-entry.gb
58. refseq-NM_001346091-summary.md
59. rittore-2014-exon2-abstract.md
60. rittore-2014-exon2-summary.md
61. rittore-2021-tnfr1-d2-abstract.md
62. rittore-2021-tnfr1-d2-fulltext.txt
63. rittore-2021-tnfr1-d2-summary.md
64. rothe-1993-knockout-abstract.md
65. rothe-1993-knockout-summary.md
66. schall-1990-cloning-abstract.md
67. schall-1990-cloning-summary.md
68. schneiderbrachert-2004-receptosome-abstract.md
69. schneiderbrachert-2004-receptosome-summary.md
70. simon-2010-traps-concerted-abstract.md
71. simon-2010-traps-concerted-summary.md
72. sukits-2001-dd-structure-abstract.md
73. sukits-2001-dd-structure-summary.md
74. tartaglia-1993-death-domain-abstract.md
75. tartaglia-1993-death-domain-summary.md
76. telliez-2000-dd-nmr-abstract.md
77. telliez-2000-dd-nmr-summary.md
78. uniprot-A0A9L0JKX4-entry.fasta
79. uniprot-A0A9L0JKX4-entry.txt
80. uniprot-A0A9L0JKX4-summary.md
81. uniprot-F5H061-entry.txt
82. uniprot-F5H061-summary.md
83. uniprot-P19438-entry.txt
84. uniprot-P19438-summary.md
85. vanamee-2018-tnfsf-structure-abstract.md
86. vanamee-2018-tnfsf-structure-summary.md
87. vandenabeele-2010-necroptosis-abstract.md
88. vandenabeele-2010-necroptosis-summary.md
89. wang-2020-donkey-genome-abstract.md
90. wang-2020-donkey-genome-fulltext.txt
91. wang-2020-donkey-genome-summary.md
92. wiegmann-1994-smase-abstract.md
93. wiegmann-1994-smase-summary.md