---
title: "IBA Annotation Quality Project"
maturity: COMPLETE
tags: [PIPELINE, FLAGSHIP]
---

# IBA Annotation Quality Project

## Overview

> Project log, per-pass verification narrative, and lessons learned: [IBA_REVIEW/HISTORY.md](IBA_REVIEW/HISTORY.md).

This project examines the quality of IBA (Inferred from Biological Aspect of Ancestor) annotations discovered through AI-assisted gene review. IBA annotations use phylogenetic trees to transfer function from characterized proteins to uncharacterized orthologs.

While IBA is a powerful curation tool, it can produce problematic annotations when:
1. **Functional divergence** - Orthologs have evolved different functions
2. **Pseudo-enzymes** - Catalytic function lost despite domain retention
3. **Context-specific function** - Function differs between organisms/tissues
4. **Over-generalization** - Broad terms transferred when specific functions differ

This project covers **both directions** of IBA quality: most of the page catalogs
where IBA is *wrong* (over-annotation, patterns 1–15), while
[IBA Incompleteness](#iba-incompleteness-core-function-that-iba-fails-to-propagate)
quantifies where IBA *under-calls* established biology — 511 curated human core
molecular functions that IBA alone would miss.

## IBA Quality Issues

### 1. Pseudo-Enzyme Propagation

**The Problem**: Enzymatic activity transferred to proteins that have lost catalytic function.

**Example - Epe1 (S. pombe)**:
- IBA annotation: `GO:0032452` (histone demethylase activity)
- Source: Related JmjC domain proteins with characterized demethylase activity
- Reality: Epe1 has degenerate active site (HVD vs HXD), no detectable activity
- **Impact**: Misleading annotation propagated via phylogenetic inference

### 2. Ubiquitin-Like Modifier Confusion

**The Problem**: Function from ubiquitin E1 transferred to ISG15-specific E1.

**Example - UBA7 (human)**:
- IBA annotations from ubiquitin pathway:
  - `GO:0008641` (ubiquitin-like modifier activating enzyme activity) - too general
  - Various ubiquitin-related terms
- Reality: UBA7 specifically activates ISG15, not ubiquitin, in mammals
- **Impact**: Generic terms obscure specific function

### 3. Substrate Specificity Transfer

**The Problem**: Specific substrate preference may differ between orthologs.

**Example - LPL1 (C. albicans)**:
- IBA annotation: `GO:0004622` (phosphatidylcholine lysophospholipase activity)
- Source: S. cerevisiae ortholog with characterized PC specificity
- Reality: Enzyme has broad specificity for ALL glycerophospholipids
- **Impact**: Over-specific annotation from ortholog doesn't capture full activity

### 4. Neo-Functionalization: Opposite Function in Subfamily

**The Problem**: When a subfamily undergoes neo-functionalization to catalyze the **opposite reaction**, IBA from the family root propagates the wrong function.

**Example - Cds1 (M. tuberculosis, V. cholerae) - PTHR10314 SF135**:
- IBA annotation: `GO:0019344` (cysteine biosynthetic process)
- Source: Root node (PTN000034104) of PTHR10314 family
- Reality: Cds1 catalyzes cysteine **CATABOLISM** (EC 4.4.1.1), the exact opposite!
- **Impact**: IBA propagates biosynthesis when the enzyme actually degrades cysteine to H2S + pyruvate

**Why this is severe**: The annotation isn't just wrong - it's **directionally opposite**. The enzyme produces H2S from cysteine degradation; the annotation says it synthesizes cysteine.

**Root Cause Analysis**:
| Evidence | SF135 (Cds1) | SF194/SF162 (Synthases) |
|----------|--------------|-------------------------|
| EC Number | **4.4.1.1** (lyase) | 2.5.1.47 (transferase) |
| Reaction | L-Cys → H2S + pyruvate | O-Ac-Ser + H2S → L-Cys |
| Branch length | **0.528** (longest) | 0.402-0.458 |
| Seq identity to synthases | **~24%** | 40-43% between each other |
| Active site motif | **ASSGST** | PTSGNTG |

The subfamily SF135 shares only 24% identity with synthases - less than synthases share with each other (43%). The longest branch length indicates maximum divergence and neo-functionalization.

### 5. Secondary Activity Promotion

**The Problem**: Non-core activities from well-characterized orthologs promoted to uncharacterized proteins.

**Example - LPL1 (C. albicans)**:
- IBA annotation: `GO:0047372` (monoacylglycerol lipase activity)
- This is likely substrate promiscuity, not core function
- **Action**: KEEP_AS_NON_CORE rather than ACCEPT

### 6. Organism/Tissue Context Transfer

**The Problem**: Annotations derived from organism-specific experimental systems carry that context to orthologs where it doesn't apply.

**Example - RIMBP2 (human)**:
- IBA annotation: `GO:0007274` (neuromuscular synaptic transmission)
- Source: Drosophila ortholog (FB:FBgn0262483) where NMJ is the primary synapse model
- Reality: Human RIMBP2 functions mainly at CNS synapses (hippocampal, auditory)
- **Impact**: Term implies NMJ function when actual function is at central synapses
- **Root cause**: IBA quality limited by organism-specific biases in source annotations

### 7. Pseudo-Enzyme Propagation Is a Recurring Human Pattern

**The Problem**: The Epe1 pseudo-demethylase case is not isolated. Catalytic-residue loss with fold retention recurs across human families, and IBA repeatedly transfers the ancestral enzymatic activity to the catalytically dead member. These are the **most defensible** REMOVE calls, because the catalytic deficiency is independently documented in UniProt.

**Examples (REMOVE — each verified against the UniProt record, not just the review)**:
- **DPYSL2 / CRMP1 / DPYSL3** — `GO:0016812` (metallo-hydrolase activity, cyclic amides): the CRMP/dihydropyrimidinase-like proteins are explicitly flagged by UniProt CAUTION — *"Lacks most of the conserved residues that are essential for binding the metal cofactor and hence for dihydropyrimidinase activity."* **Confirmed first-hand by MSA** ([msa/RESULTS.md](IBA_REVIEW/msa/RESULTS.md)): aligned against active dihydropyrimidinase (DPYS), all five CRMP/DPYSL paralogs have lost the carbamylated catalytic Lys (K159→L/M/Q) plus multiple Zn-coordinating His/Asp. They are non-catalytic cytoskeletal regulators.
- **AGO4** — `GO:0004521` (RNA endonuclease activity): UniProt FUNCTION states directly that AGO4 *"Lacks endonuclease activity and does not appear to cleave target mRNAs"* — only AGO2 is the catalytic slicer in humans. **MSA confirms** ([msa/RESULTS.md](IBA_REVIEW/msa/RESULTS.md)) AGO4 carries two substitutions in the catalytic tetrad (D669G, H807R) vs intact AGO2; usefully, the same alignment shows AGO3 *retains* the tetrad, so the "non-slicer" story is residue-specific, not a blanket family claim.
- **UBAC2** — `GO:0004252` (serine-type endopeptidase activity): UBAC2 has a rhomboid-**like** fold (a known inactive-rhomboid/pseudoprotease clan) but UniProt attributes no protease function — its curated roles are as an ERAD/ER-phagy adaptor. *(Caveat: the absence of catalytic residues is inferred from the inactive-rhomboid classification and the lack of any curated protease activity, not from an explicit UniProt CAUTION.)*
- **AKTIP** — `GO:0061631` (ubiquitin-conjugating enzyme activity): UniProt CAUTION states it *"Lacks the conserved Cys residue necessary for ubiquitin-[conjugating]"* activity. It is in the E2 PANTHER family (PTHR24067) and the IBA is inferred from many genuine UBE2 enzymes, but as a UEV-domain protein it is a catalytically dead pseudo-E2 (a component of the FTS/Hook/FHIP complex). A second annotation even records the NOT form.
- **DPYSL4** — `GO:0016812`: a fourth CRMP-family member (Dihydropyrimidinase-related protein 4) carrying the same metallo-hydrolase IBA on the same basis as DPYSL2/3/CRMP1 — the whole CRMP/dihydropyrimidinase-*related* clade is non-catalytic (see the MSA above); only true dihydropyrimidinase (DPYS) retains the activity.
- **CASP12 (human)** — `GO:0004197` (cysteine-type endopeptidase activity): UniProt RecName is literally *"Inactive caspase-12."* Most humans carry a truncated, catalytically dead variant; the caspase-family protease IBA is over-propagated.
- **Serpinh1/HSP47 (mouse)** — `GO:0004867` (serine-type endopeptidase inhibitor activity): the textbook **non-inhibitory serpin** — UniProt describes a collagen-specific ER molecular chaperone (*"Collagen-binding protein"*), not a protease inhibitor. The serpin-fold IBA propagates inhibitory activity HSP47 does not have.
- **Lesson**: a degenerate/absent active site, **independently documented** (UniProt CAUTION/FUNCTION, an "Inactive"/non-inhibitory RecName, or — best — the missing catalytic residue seen in an MSA), is the strongest single signal that an enzymatic IBA is wrong. Now represented by Epe1 (demethylase), the CRMP family DPYSL2/3/4/CRMP1 (amidohydrolase), AGO4 (slicer), UBAC2 (protease), AKTIP (E2 ligase), CASP12 (protease), and HSP47 (protease inhibitor).

### 8. Partial Sub-Activity Loss Within a Multidomain Family

**The Problem**: Distinct from full pseudo-enzymes — the protein **retains part of the ancestral activity but lost a specific sub-activity**, and IBA transfers the lost sub-activity.

**Examples (REMOVE — verified)**:
- **CAPG (human)** — `GO:0051014` (actin filament **severing**): CAPG caps but does **not** sever. The original characterization (cached PMID:1322908) states verbatim that CAPG *"reversibly blocks the barbed ends of actin filaments but does not sever preformed actin"*. The severing term over-extends from the gelsolin/villin family; CAPG retains capping only.
- **human/CRYAA** — `GO:0042026` (protein **refolding**): αA-crystallin is an ATP-independent **holdase** that prevents aggregation but cannot refold clients. This one is corroborated **inside GOA itself**: there is an explicit curated `NOT|involved_in` (ISS) annotation to GO:0042026, which the IBA directly contradicts. UniProt describes only aggregation-prevention chaperone activity, no refolding.
- **Worm small heat-shock proteins** — `GO:0042026` (protein refolding): a stronger version of the CRYAA case. hsp-16.2 is a holdase, not a foldase; and **hsp-12.3 / hsp-12.6 have *no* chaperone activity at all** — the title of PMID:9744800 is literally *"…Hsp12.2 and Hsp12.3 form tetramers and have no chaperone-like activity."* They are pseudo-sHSPs (tetramers/monomers rather than the large oligomers holdase function needs), so the family-level refolding IBA is fully refuted.
- **Lesson**: capping≠severing and holdase≠foldase are sub-activity distinctions that family-level IBA flattens. The CRYAA and hsp-12.3 cases are especially clean because a curator negated the term (CRYAA) or a paper demonstrated zero activity (hsp-12.3).

### 9. Regulatory-Sign Inversion Within a Family

**The Problem**: When a protein family contains members with **opposite regulatory signs** (activators vs inhibitors of the same process), a family-node IBA can transfer the wrong sign.

**Example - BCL2 (human and mouse)**:
- IBA annotation: `GO:0043065` (**positive** regulation of apoptotic process)
- Reality: BCL2 is the prototypical **anti-apoptotic** guardian; it inhibits MOMP and cytochrome c release (PMID:9027314, PMID:9219694).
- **Root cause (verified from GOA WITH/FROM)**: the IBA for GO:0043065 is inferred from a PANTHER node (PTN000135648) whose WITH/FROM list **mixes pro- and anti-apoptotic BCL2-family members** — pro-apoptotic BAX (Q07812) and BAK1 (Q16611) alongside anti-apoptotic members. The shared BH-domain fold unites activators and inhibitors of apoptosis under one family, so the "positive regulation" sign can leak onto BCL2.
- **Caveat (why this is "non-core" rather than flatly "wrong")**: BCL2 *does* have documented context-dependent pro-apoptotic behavior (e.g. caspase-cleaved BCL2), and GOA additionally carries a separate **NAS** annotation (PMID:14634621, ComplexPortal) to the very same GO:0043065. So the honest framing is that the *IBA family-node inference is unreliable for sign* (verified mechanism), not that positive regulation is impossible for BCL2. The companion review more confidently re-points related terms to their negative-regulation children (e.g. `GO:0001836` release of cytochrome c → `GO:0090201` *negative* regulation of release of cytochrome c).

### 10. Complex / Compartment / Pathway Membership Over-Transfer

**The Problem**: A family-level IBA asserts membership in a **specific complex, compartment, or pathway** that the target protein does not actually occupy, even though the catalytic fold or sequence homology is real. Compartment-split paralogs are the classic trap: they share a fold but route their product to different destinations.

**Examples (verified across multiple lines of evidence)**:
- **EIF4E2 (human)** — `GO:0016281` (eIF4F complex): 4EHP/EIF4E2 binds the cap but UniProt states it *"is unable to bind eIF4G"* and *"Does not interact with eIF4G"*; it is a translational repressor (4EHP-GYF2 complex), never an eIF4F subunit. A clear family-level over-transfer from EIF4E.
- **ALDH1L1 (rat)** — `GO:0005739` (mitochondrion): UniProt names it *Cytosolic 10-formyltetrahydrofolate dehydrogenase* with `SUBCELLULAR LOCATION: Cytoplasm, cytosol` and a cytosol IDA. Mitochondrial one-carbon oxidation is the job of the distinct paralog **ALDH1L2**.
- **HMGCS2 (rat)** — `GO:0010142` (farnesyl-PP biosynthesis, mevalonate pathway): a **paralog-pathway conflation**. The IBA comes from a PANTHER node (PTN000222418) that lumps the HMGCS paralogs. The cytosolic paralog **HMGCS1** feeds mevalonate→FPP→sterol/isoprenoid synthesis; mitochondrial HMGCS2's HMG-CoA is cleaved by HMG-CoA lyase to acetoacetate (ketogenesis). The shared HMG-CoA-synthase *reaction* is correctly classified under mevalonate biosynthesis (UniProt UniPathway tag), but assigning HMGCS2 to **FPP/isoprenoid** biosynthesis follows the wrong paralog's flux — an over-annotation. *(Nuance: the enzymatic step is real, so this is paralog over-annotation, not a fabricated activity.)*
- **PEX2 (human)** — `GO:0016593` (Cdc73/Paf1 complex): PEX2 is a peroxisomal RING E3 ligase for PEX5 retrotranslocation (UniProt) and has no role in RNA Pol II transcription elongation, so membership in the Cdc73/Paf1 complex is clearly wrong. *(Caveat: the cause is unconfirmed — the IBA WITH/FROM is a PANTHER node, not a PAF1 gene. A legacy synonym collision — PEX2's old name "PAF1"/Peroxisome Assembly Factor 1 vs the unrelated transcription factor PAF1 — is a plausible but unverified explanation.)*
- **Lesson**: complex membership, compartment, and downstream pathway are not conserved across paralogs even when the fold/reaction is; verify the protein actually occupies the annotated complex/compartment and that its product reaches the annotated pathway.

### 11. Substrate Over-Propagation From a Multi-Specificity Enzyme Family

**The Problem**: A PANTHER family lumps enzymes of **different substrate specificities**; a substrate-specific term is then propagated to a member that experimentally lacks that activity. Unlike LPL1 (a real but secondary/broader specificity), here the propagated activity is **absent** in the target.

**Example - AGK (human)** — `GO:0001729` (ceramide kinase), `GO:0046513`/`GO:0046512` (ceramide/sphingosine biosynthesis):
- AGK sits in PANTHER **PTHR12358**, which lumps "ACYLGLYCEROL KINASE" with "SPHINGOSINE KINASE." The ceramide-kinase IBA is propagated from a family node (Drosophila + mouse + node PTN008994514); the IEA/ISS variants both trace to one rodent ortholog (Q9ESW4).
- **Three independent lines refute the activity in human AGK**, outweighing the family inference:
  1. The direct human enzymology paper (the one UniProt itself cites): *"Significant phosphorylated products were only detected with monoacylglycerols and diacylglycerols as substrates, but not with any other lipid tested, including ceramide and sphingosine"* (PMID:15939762).
  2. A second study: *"No evidence for phosphorylation of ceramide by the recently described multiple lipid kinase was found"* (PMID:16269826).
  3. UniProt's own FUNCTION line states *"Does not phosphorylate sphingosine (PubMed:15939762)"*; its sole ceramide claim is a weak **"By similarity"** tag (propagated from Q9ESW4), not direct evidence.
- The dedicated ceramide kinase is the **separate** enzyme CERK. AGK's verified activity is MAG/DAG kinase (plus a kinase-independent TIM22 structural role).

**Example - SAMD8/SMSr (human)** — `GO:0033188` (sphingomyelin synthase activity):
- SAMD8 is in the sphingomyelin-synthase PANTHER family (PTHR21290), but UniProt's experimentally-supported FUNCTION says it makes **ceramide phosphoethanolamine (CPE)**, transferring a phospho**ethanolamine** head group from PE to ceramide — explicitly *not* the phospho**choline**-from-PC reaction that defines sphingomyelin synthases SMS1/SMS2: *"The larger PC prevents an efficient fit in the enzyme's catalytic pocket."* So the family-level sphingomyelin-synthase term is the wrong product/substrate; this is also accompanied by mislocalization IBAs (Golgi, plasma membrane) that belong to SMS1/SMS2, whereas SMSr is ER-retained.

**Example - CPT1C (human)** — `GO:0006631` (fatty acid metabolic process), `GO:0009437` (carnitine metabolic process):
- A **neofunctionalization** case: UniProt's RecName is literally *"Palmitoyl thioesterase CPT1C."* Although it sits in the carnitine O-acyltransferase family (PTHR22589) with CPT1A/B, experimental work shows CPT1C **lacks the canonical carnitine palmitoyltransferase activity** (it binds malonyl-CoA but does not catalyze carnitine-dependent acyl transfer). The IBA propagates the ancestral CPT1A/B fatty-acid/carnitine metabolism that CPT1C no longer performs.
- **Lesson**: a "By similarity"/propagated annotation is weak evidence; when direct experimental papers in the target species report the activity is **absent or different in product** (AGK no ceramide; SAMD8 makes CPE not SM; CPT1C is a thioesterase not a transferase), the substrate/activity-specific IBA is an over-propagation. A family node that mixes substrate specificities (acylglycerol+sphingosine kinases; SM+CPE synthases) leaks substrate terms across specificity boundaries.

### 12. Mis-Grouping Revealed by the WITH/FROM Column

**The Problem**: The IBA `WITH/FROM` field names the exact source proteins the function was transferred *from*. Reading it frequently reveals the error directly — the source is either the **wrong family entirely** or the **wrong paralog**. This is the single most useful diagnostic in this whole catalog.

**Tier A — wrong family / over-broad superfamily** (egregious; the source proteins are functionally unrelated):
- **NTN1 / NTN3 (human)** — `GO:0000981`/`GO:0006357`/`GO:0000978` (DNA-binding transcription-factor activity, Pol II transcription regulation, cis-regulatory DNA binding): Netrins are **secreted** axon-guidance cues (UniProt: extracellular; PANTHER PTHR10574 Netrin/Laminin) with no DNA-binding domain — yet they carry nuclear **POU-domain transcription-factor** IBAs. The WITH/FROM proves it: the source list is POU-domain TFs (POU2F1 P14859, POU1F1 P28069, POU4F1 Q12837, POU4F3 Q15319, …). A secreted protein cannot be a Pol II transcription factor; this is a phylogenetic grouping error.
- **NOTCH1 (human)** — `GO:0007411` (axon guidance): the WITH/FROM is **SLIT1/2/3** (O75093, O94813, O75094). NOTCH1 signals in neurogenesis but axon guidance is a SLIT function transferred across an over-broad node.
- **IL23R (human)** — `GO:0004925` (prolactin receptor activity), `GO:0017046` (peptide hormone binding): the WITH/FROM is **PRLR** (P16471). IL23R is a type-I cytokine receptor that binds the cytokine IL-23, not the hormone prolactin; the superfamily node is too broad.

**Tier B — wrong paralog** (subtle; the source is a close relative with a different function):
- **ABRAXAS1 (human)** — `GO:0090307`/`GO:0008608`/`GO:0008017` (mitotic spindle assembly, spindle–kinetochore attachment, microtubule binding): every one of these IBAs traces via WITH/FROM to **`UniProtKB:Q15018` = ABRAXAS2** (ABRO1, the BRISC-complex paralog). ABRAXAS1 is a nuclear BRCA1-A DNA-damage scaffold; the spindle/MT biology belongs to ABRAXAS2.
- **HINT2 (human)** — `GO:0005737` (cytoplasm): HINT2 has a mitochondrial targeting sequence and is mitochondrial; the cytoplasm term reflects the **HINT1** paralog.
- **CPT1C** (above) similarly inherits CPT1A/B metabolism it no longer performs.
- **opa1 (zebrafish) / eat-3 (worm)** — `GO:0016559` (peroxisome fission): both are UniProt *"Dynamin-like GTPase OPA1, mitochondrial"* inner-membrane **fusion** proteins. Peroxisome fission is done by the DRP1/DNM1L branch of the dynamin superfamily; the term is a within-superfamily mis-transfer (wrong organelle *and* wrong direction).
- **YAR1 (yeast)** — `GO:0045944` (positive regulation of transcription): YAR1 is an RPS3-binding 40S-ribosome-biogenesis factor (UniProt: interacts with RPS3), not a transcription activator; **ACL4 (yeast)** likewise gets mitochondrial-import terms by TOM70-family over-transfer despite being an Rpl4 chaperone.
- **Lesson**: **always read the WITH/FROM before flagging.** It tells you whether the IBA is a defensible family-level transfer or a traceable mis-grouping — and if a single paralog or out-of-family protein is the source, that is strong, near-mechanical evidence of error.

### 13. Generic / Mutually-Exclusive Compartment Over-Propagation

**The Problem**: Localization is one of the most frequently over-propagated IBA categories — but whether a flag is valid depends entirely on the **GO compartment hierarchy**, which makes this a two-sided pattern. Mutually-exclusive compartments are valid REMOVE grounds; broad *subsuming* terms are not.

**Tier A — valid REMOVE: a mutually-exclusive specific compartment on a protein that lives elsewhere.** `GO:0005634` nucleus is the one compartment the cytoplasm definition explicitly **excludes**, and plasma membrane / peroxisome / a specific organelle are likewise non-overlapping — so these are genuine errors:
- **Cytoplasmic PIWI/Argonaute & germ-granule proteins given `GO:0005634` nucleus** — PIWIL1 (human), and worm prg-1, wago-1, glh-1. All are cytoplasmic nuage/P-granule/chromatoid-body proteins (UniProt: cytoplasmic granule, no nucleus). The WITH/FROM nodes include **nuclear-acting Piwi orthologs** (e.g. *Drosophila* Piwi is nuclear; nuclear PIWIL4/MIWI2), so the nuclear compartment leaks onto the cytoplasmic members.
- **EIF2AK3/PERK → nucleus** (UniProt: ER membrane kinase) and **BIRC6 → nucleus** (UniProt: TGN/endosome/cytoskeleton/midbody — no nuclear pool).
- **Ribosome-associated chaperones SSB2 / SSZ1 (yeast) → `GO:0005886` plasma membrane** (UniProt: cytoplasmic, ribosome-associated) — PM propagated across the HSP70 family node.
- **BAIAP2L2 → `GO:0005654` nucleoplasm** (UniProt: plasma membrane / cell junction; I-BAR family) and **PIK3C3/VPS34 → `GO:0005777` peroxisome** (UniProt: autophagosome/endosome/midbody).
- **Inverse** — strictly **nuclear** proteins given `GO:0005737` cytoplasm: rqh1 (RecQ helicase) and HDA1 (HDAC) are nucleus-only, and nucleus is excluded from cytoplasm, so cytoplasm is wrong. And the genuinely **extracellular** SCGB1A1 given cytoplasm (secreted = outside the cell).

**Tier B — anti-pattern (do NOT flag; these reviewer REMOVEs were over-reaches).** `GO:0005737` cytoplasm **subsumes** mitochondrion, ER, Golgi, and lysosome (all `part_of` cytoplasm), so "cytoplasm" is defensible — if imprecise — for an organellar protein:
- "cytoplasm" REMOVE on **Aga / GLA** (lysosome), **DHCR24** (ER membrane, catalytic domain faces the cytosol), **ISCA1 / ATP5IF1 / gtpbp3** (mitochondrion) — all should be UNDECIDED/KEEP, not REMOVE.
- "membrane" (`GO:0016020`) REMOVE on **flvcr2a** is wrong — it is a multi-pass membrane transporter.
- **Self-correction**: HINT2's "cytoplasm" flag (added in the WITH/FROM pass) belongs here too — HINT2 is mitochondrial, but mitochondrion ⊂ cytoplasm, so cytoplasm is not strictly wrong; downgraded from the findings.

**Lesson**: before a localization REMOVE, place both compartments in the GO hierarchy. Mutually-exclusive (nucleus vs cytoplasm; PM vs internal; one organelle vs another) → valid. A broad subsuming term over a more specific true location (cytoplasm over any organelle; membrane over a membrane protein) → leave it.

### 14. Lineage-Inappropriate (Cross-Kingdom) Process Transfer

**The Problem**: Phylogenetic inference crosses kingdom/clade boundaries and lands a biological-process term on an organism where **the process does not exist** — or where the homolog was repurposed into a different system. The WITH/FROM typically names a vertebrate or *Drosophila* source. This is one of the largest and cleanest BP error classes.

**Examples (REMOVE — verified via UniProt + WITH/FROM):**
- **TOLL9 (mosquito, ANOGA)** — `GO:0006954` (inflammatory response): the IBA traces to **human TLR4 (O00206)** and other mammalian TLRs. Insects have Toll-pathway innate immunity but no vertebrate inflammation (no vasculature, immune-cell infiltration); the term is lineage-inappropriate.
- **ndhA / ndhD / ndhK (poplar, POPTR)** — `GO:0009060` (aerobic respiration): UniProt labels these *"NAD(P)H-quinone oxidoreductase, **chloroplastic**"* (`OG Plastid; Chloroplast`). They are photosynthetic plastid NDH subunits homologous to mitochondrial complex I — an **organelle-system swap**, not mitochondrial respiration.
- **che-3 (worm)** — `GO:0060294` (cilium movement involved in cell motility): che-3 is cytoplasmic **dynein-2** (retrograde IFT motor); *C. elegans* sensory cilia are **non-motile**. The motility term comes from axonemal-dynein orthologs in organisms with motile cilia.
- **D7 salivary proteins (mosquito, ANOGA: D7r2/D7r4/D7r5/D7L1)** — `GO:0007608` (sensory perception of smell): UniProt calls D7r4 a *"salivary protein… modulates blood feeding,"* female-saliva-specific. The OBP/PBP-GOBP fold was repurposed for binding biogenic amines/eicosanoids in saliva — these proteins are not expressed in antennae and have no olfactory role.
- **sta-2 (worm)** — `GO:0007259` (JAK-STAT signaling): transferred from fly/mammalian STATs, but *C. elegans* has **no JAK kinases**; STA-2 is activated via SNF-12/hemidesmosomes.
- **fshr-1 (worm)** — `GO:0009755` (hormone-mediated signaling): *C. elegans* lacks gonadotropins (FSH/LH/TSH); FSHR-1 functions in innate immunity/stress.
- **HEN1 (Arabidopsis)** — `GO:0034587` (piRNA processing): piRNAs are metazoan; plant HEN1 methylates miRNA/siRNA duplexes. Over-transfer from the metazoan HEN1/HENMT1 context.
- **Lesson**: check **taxon appropriateness** — does the process even occur in this lineage? GO taxon constraints catch some of these; the WITH/FROM naming a vertebrate/insect source is the tell. Watch especially for organelle-system swaps (plastid↔mitochondrion; cytoplasmic↔axonemal dynein).

### 15. Regulator / Effector and Direct / Downstream Conflation

**The Problem**: IBA (and curation generally) can blur the line between a **regulator or effector** of a process and the **core machinery**, or between a **downstream consequence** and the **direct function**.

**Examples (verified):**
- **lys-7 (worm)** — `GO:0007165` (signal transduction): LYS-7 is an antimicrobial **effector** whose expression is regulated *by* signaling; it is not itself a signaling component. (Same logical error as arnF's "response to iron" — see §arnF.)
- **SIR3 (yeast)** — `GO:0006270` (DNA replication initiation): SIR3 **represses** origin firing (negative regulation of MCM loading), the opposite of being part of the initiation machinery (ORC/CDC6/CDT1/MCM2-7).
- **UBP3 (yeast)** — `GO:0031647` (regulation of protein stability): a downstream *consequence* of its deubiquitinase activity (`GO:0004843`, the direct function), not a separate function.
- **sigF / sigG / sigK (*B. subtilis*)** — `GO:0003899` (DNA-directed RNA polymerase activity): these are **sigma initiation factors** (UniProt: *"initiation factors that promote…"* promoter recognition) — they confer promoter specificity to RNA polymerase but have **no catalytic polymerase activity**, which belongs to the core enzyme (RpoB/RpoC). A regulatory subunit assigned the **holoenzyme's** catalytic activity.
- **Lesson**: distinguish "does X" from "regulates/enables/results-in X." Effectors are not signal transducers; repressors are not part of the machinery they inhibit; a specificity subunit does not carry the catalytic activity of the complex it joins; downstream consequences are not direct molecular functions.

## Featured Examples

### Epe1 - Pseudo-Demethylase

**Species**: pombe
**Status**: COMPLETE

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0032452 histone demethylase activity | Pseudo-enzyme - no activity | REMOVE |
| GO:0006338 chromatin remodeling | Too broad | MODIFY |
| GO:0006357 regulation of transcription by RNA pol II | Valid | ACCEPT |
| GO:0003712 transcription coregulator activity | Valid | ACCEPT |

**Lesson**: IBA can propagate enzymatic activity to pseudo-enzymes that retain the domain fold but lack catalytic function.

### UBA7 - ISG15-Specific E1

**Species**: human
**Status**: COMPLETE

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0005737 cytoplasm | Correct | ACCEPT |
| GO:0019782 ISG15 activating enzyme activity | Correct, specific | ACCEPT |
| GO:0032020 ISG15-protein conjugation | Correct | ACCEPT |
| GO:0045087 innate immune response | Correct | ACCEPT |
| GO:0006974 DNA damage response | Correct | ACCEPT |

**Note**: UBA7 IBA annotations are largely correct because the ISGylation pathway is conserved.

### LPL1 - Phospholipase Specificity

**Species**: CANAL
**Status**: COMPLETE

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0006629 lipid metabolic process | Correct | ACCEPT |
| GO:0004622 PC lysophospholipase activity | Too narrow | MODIFY |
| GO:0005811 lipid droplet | Correct | ACCEPT |
| GO:0047372 monoacylglycerol lipase activity | Secondary activity | KEEP_AS_NON_CORE |

### RIMBP2 - Context-Specific Term Transfer

**Species**: human
**Status**: COMPLETE
**PANTHER Family**: [PTHR14234](../interpro/panther/PTHR14234/) (RIM BINDING PROTEIN-RELATED)

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0007274 neuromuscular synaptic transmission | Wrong synapse type context | MODIFY |

**Lesson**: IBA transferred a term specific to *Drosophila* NMJ context to a human gene that functions primarily at CNS synapses. The IBA source (FB:FBgn0262483) is the fly ortholog where neuromuscular junctions are a major experimental system. However, human RIMBP2 functions at hippocampal (mossy fiber, CA3-CA1), auditory ribbon, and other central synapses - not primarily at neuromuscular junctions. This illustrates how IBA can propagate organism-specific or tissue-specific contexts that don't apply to the target species.

**Root Cause Analysis**: This is a case where **IBAs are only as good as the manual annotations on orthologs**. The Drosophila RIMBP ortholog is well-characterized at the NMJ because that's the major accessible synapse type in flies. When this annotation gets transferred to human via phylogenetic inference, it carries the fly-specific context with it.

**Family-Level Context**: The [PANTHER family analysis](../interpro/panther/PTHR14234/PTHR14234-deep-research-falcon.md) reveals additional IBA quality concerns:
- The representative structure (PDB 4z8a) is from *Drosophila* RIM-BP bound to Cacophony (fly NMJ Ca2+ channel)
- The family contains **functionally divergent subfamilies**:
  - RIMBP1/2 (SF18, SF20): Neuronal synaptic scaffolds
  - RIMBP3 (SF21): **Non-synaptic** - testis-specific, spermiogenesis/manchette function
- The family research explicitly warns: "Avoid propagating 'regulation of neurotransmitter release' to RIMBP3 paralogs"
- This demonstrates that IBA issues can affect entire subfamilies, not just individual genes

### arnF (PTHR30561) - Functional Divergence Within SMR Superfamily

**Species**: ECOLI (Escherichia coli K12)
**Status**: COMPLETE
**Family**: PTHR30561 (Small Multidrug Resistance / Drug-Metabolite Transporter superfamily)

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0022857 transmembrane transporter activity | Too generic; conflates drug efflux with lipid flipping | MODIFY → GO:0140303 |
| GO:0005886 plasma membrane | Correct | ACCEPT |
| GO:0055085 transmembrane transport | Acceptable broad term | ACCEPT |

**Lesson**: The PANTHER family PTHR30561 groups **four functionally distinct protein families** that share the SMR/DMT fold:
- **ArnE/ArnF** — undecaprenyl phosphate-L-Ara4N **flippases** (intramembrane lipid translocation)
- **EmrE** (P23895) — multidrug **efflux pump** (exports lipophilic cations)
- **MdtI/MdtJ** (P69210/P69212) — **spermidine export**
- **Gdx/SugE** (P69937) — **guanidinium export**
- **Mmr** (P9WGF1) — *M. tuberculosis* multidrug resistance

The IBA inference of "transmembrane transporter activity" comes from propagating annotations from these bona fide solute exporters (EmrE, MdtI/J, Gdx, Mmr) to ArnF. But ArnF does something mechanistically different: it **flips a lipid-linked sugar between membrane leaflets**, not export a solute across the membrane. The correct MF term is GO:0140303 (intramembrane lipid transporter activity).

**Why this is instructive**: Unlike the cds1 case (opposite reaction) or Epe1 (lost activity), arnF retains *transport* function — the IBA isn't wrong in kind, just wrong in specificity. The SMR superfamily is a case where sequence homology correctly identifies the structural fold (small multidrug resistance-like) but the functional annotation doesn't track the divergence from drug efflux to lipid flipping. This is a **moderate severity** issue because the parent term "transmembrane transporter" is not false, but it's misleading about mechanism.

**EcoCyc vs. IBA comparison**: EcoCyc contributed 5 annotations for arnF, including two "response to iron(III) ion" annotations (IGI from PMID:12139617, IEP from PMID:15322361) that were marked as over-annotated — they conflate transcriptional regulation of the arn operon by BasS-BasR with direct gene function. The IMP annotations from EcoCyc (carbohydrate derivative transport/transporter activity, plasma membrane IDA) are well-supported. The IBA annotations from GO_Central are reasonable at the superfamily level but miss the flippase specialization.

**Root Cause Analysis**:
| Feature | ArnE/ArnF | EmrE | MdtI/J | Gdx |
|---------|-----------|------|--------|-----|
| Function | Lipid flippase | Drug efflux | Spermidine export | Guanidinium export |
| Substrate | Lipid-linked sugar | Lipophilic cations | Spermidine | Guanidinium |
| Mechanism | Intramembrane flip | Transmembrane export | Transmembrane export | Transmembrane export |
| PANTHER SF | SF9 | (family-level) | SF6 | (family-level) |

### Cds1 (PTHR10314) - Neo-Functionalization (Opposite Reaction)

**Species**: MYCTU (Mycobacterium tuberculosis), VIBCH (Vibrio cholerae)
**Status**: COMPLETE
**Family**: PTHR10314 (Cysteine Synthase/Cystathionine Beta-Synthase)

**IBA Annotations Flagged**:
| Term | Issue | Action |
|------|-------|--------|
| GO:0019344 cysteine biosynthetic process | **Opposite function** - enzyme is catabolic | REMOVE |

**Lesson**: This is the most severe type of IBA error - the annotation isn't merely imprecise, it's **directionally wrong**. Cds1 (subfamily SF135) catalyzes cysteine **degradation** (EC 4.4.1.1), producing H2S + pyruvate from L-cysteine. The IBA annotation GO:0019344 says it participates in cysteine **biosynthesis** - the exact opposite reaction!

**Root Cause Analysis**:
1. GO:0019344 is annotated at the PANTHER family root node (PTN000034104)
2. Root annotation propagates to ALL descendants, including subfamily SF135 (Cds1)
3. SF135 underwent **neo-functionalization**: same fold, opposite reaction
4. Evidence of neo-functionalization:
   - Longest branch length (0.528) from root = most divergent
   - Different EC class: 4.4.1.1 (lyase/catabolism) vs 2.5.1.47 (transferase/biosynthesis)
   - Only 24% sequence identity with synthases (synthases share 40-43% with each other)
   - Distinct active site motif: ASSGST (Cds1) vs PTSGNTG (synthases)

**Experimental Evidence**:
- PMID:34439535 (M. tuberculosis): Cds1 produces H2S, pyruvate from cysteine; KM=11.26 mM, kcat=78.71/s
- PMID:34283874 (V. cholerae): VC1061/cds1 is principal enzyme for cysteine-derived H2S production

**Recommendation for PANTHER Curators**:
- Remove GO:0019344 propagation to SF135
- Add SF135-specific annotations: GO:0019450 (L-cysteine catabolic process to pyruvate), GO:0080146 (L-cysteine desulfhydrase activity)

See detailed family analysis: `interpro/panther/PTHR10314/PTHR10314-notes.md`

## Genes with IBA Issues

| Gene | Species | IBA Issue Type | Severity | Status |
|------|---------|----------------|----------|--------|
| Epe1 | pombe | Pseudo-enzyme propagation | HIGH | COMPLETE |
| cds1 | MYCTU, VIBCH | **Neo-functionalization (opposite reaction)** | **CRITICAL** | COMPLETE |
| LPL1 | CANAL | Substrate specificity | MEDIUM | COMPLETE |
| UBA7 | human | Generic vs specific terms | LOW | COMPLETE |
| RIMBP2 | human | Context-specific term transfer | MEDIUM | COMPLETE |
| arnF | ECOLI | Functional divergence within SMR superfamily | MEDIUM | COMPLETE |
| DPYSL2/CRMP1/DPYSL3 | human | Pseudo-enzyme (UniProt CAUTION: metallo-hydrolase residues absent) | HIGH | COMPLETE |
| AGO4 | human | Pseudo-enzyme (UniProt: lacks endonuclease activity) | HIGH | COMPLETE |
| UBAC2 | human | Pseudo-enzyme (rhomboid-like, no curated protease activity) | MEDIUM | COMPLETE |
| CAPG | human | Partial sub-activity loss (caps but does not sever actin; PMID:1322908) | MEDIUM | COMPLETE |
| CRYAA | human | Partial sub-activity loss (holdase not foldase; curated NOT(refolding)) | MEDIUM | COMPLETE |
| BCL2 | human, mouse | Regulatory-sign inversion (anti-apoptotic; family-node mixes pro-/anti-) | MEDIUM | COMPLETE |
| EIF4E2 | human | Complex over-transfer (UniProt: does not bind eIF4G, no eIF4F) | MEDIUM | COMPLETE |
| ALDH1L1 | rat | Compartment conflation (UniProt cytosolic; mito is ALDH1L2) | MEDIUM | COMPLETE |
| HMGCS2 | rat | Paralog-pathway over-annotation (ketogenic; FPP synthesis is HMGCS1) | MEDIUM | COMPLETE |
| PEX2 | human | Complex over-transfer (peroxisomal E3, not Cdc73/Paf1 complex) | MEDIUM | COMPLETE |
| AGK | human | Substrate over-propagation (no ceramide/sphingosine kinase activity; 2 papers) | MEDIUM | COMPLETE |
| AKTIP | human | Pseudo-enzyme (UniProt CAUTION: lacks catalytic Cys for E2 activity) | HIGH | COMPLETE |
| DPYSL4 | human | Pseudo-enzyme (CRMP-family metallo-hydrolase, non-catalytic) | HIGH | COMPLETE |
| SAMD8 | human | Substrate neofunctionalization (CPE synthase, not sphingomyelin synthase) | MEDIUM | COMPLETE |
| CPT1C | human | Neofunctionalization (palmitoyl thioesterase; lost carnitine transferase) | MEDIUM | COMPLETE |
| NTN1/NTN3 | human | Wrong-family grouping (secreted Netrin → POU-domain TF activity) | HIGH | COMPLETE |
| NOTCH1 | human | Wrong-source transfer (axon guidance from SLIT1-3) | MEDIUM | COMPLETE |
| IL23R | human | Over-broad superfamily (prolactin-receptor activity from PRLR) | MEDIUM | COMPLETE |
| ABRAXAS1 | human | Wrong-paralog (spindle/MT terms trace to ABRAXAS2) | MEDIUM | COMPLETE |
| PIWIL1 / prg-1 / wago-1 | human, worm | Nucleus on cytoplasmic PIWI/Argonaute (mutually-exclusive compartment) | MEDIUM | COMPLETE |
| EIF2AK3, BIRC6 | human | Nucleus on ER-membrane / TGN-cytoskeletal protein | MEDIUM | COMPLETE |
| SSB2 / SSZ1 | yeast | Plasma membrane on cytoplasmic ribosome-associated chaperone | LOW | COMPLETE |
| BAIAP2L2, PIK3C3 | human | Nucleoplasm / peroxisome on membrane / autophagy protein | LOW | COMPLETE |
| SCGB1A1 | human | Cytoplasm on a secreted (extracellular) protein | LOW | COMPLETE |
| rqh1, HDA1 | SCHPO, yeast | Cytoplasm on strictly nuclear proteins | LOW | COMPLETE |
| TOLL9 | ANOGA | Cross-kingdom: inflammatory response from vertebrate TLR4 | MEDIUM | COMPLETE |
| ndhA/ndhD/ndhK | POPTR | Organelle swap: chloroplast NDH annotated as mito respiration | MEDIUM | COMPLETE |
| che-3 | worm | Cross-lineage: cilium motility on non-motile sensory cilia (IFT dynein) | MEDIUM | COMPLETE |
| D7r2/D7r4/D7r5/D7L1 | ANOGA | Cross-function: smell perception on repurposed salivary OBP-fold | MEDIUM | COMPLETE |
| sta-2, fshr-1 | worm | Cross-kingdom: JAK-STAT / hormone signaling absent in nematodes | MEDIUM | COMPLETE |
| opa1, eat-3 | DANRE, worm | Mis-grouping: peroxisome fission on mito-fusion OPA1 | MEDIUM | COMPLETE |
| hsp-12.3/hsp-12.6 | worm | Pseudo-sHSP: refolding, but "no chaperone-like activity" (PMID:9744800) | HIGH | COMPLETE |
| YAR1, ACL4 | yeast | Family over-transfer (Rps3 biogenesis factor; Rpl4 chaperone) | LOW | COMPLETE |
| SIR3, lys-7, UBP3 | yeast, worm | Regulator/effector & downstream conflation | LOW | COMPLETE |
| CASP12 | human | Pseudo-enzyme (UniProt "Inactive caspase-12") | MEDIUM | COMPLETE |
| Serpinh1/HSP47 | mouse | Pseudo-inhibitor (non-inhibitory serpin; collagen chaperone) | MEDIUM | COMPLETE |
| sigF/sigG/sigK | BACSU | Subunit assigned holoenzyme catalytic activity (sigma ≠ RNA pol) | LOW | COMPLETE |

## IBA Incompleteness: core function that IBA fails to propagate

All the patterns above concern IBA being *wrong* (over-annotation). The opposite
failure mode is just as real: IBA is frequently **incomplete** — it under-calls
well-established biology. Phylogenetic propagation is conservative by
construction (it only transfers what a curated ancestor already carries, at the
granularity the ancestor was annotated), so a great deal of experimentally
defined molecular function never reaches the leaf.

We quantified this with a generic **evidence-subtraction** tool
(`ai-gene-review subtraction-report`; see
[docs](https://ai4curation.io/ai-gene-review/subtraction_report/)). Running it in
"keep only IBA" mode over the 1015 reviewed human genes — i.e. asking *if IBA
were the sole evidence, what curated biology would we lose?* — and applying
ontology closure so that an IBA call to a **more general parent still counts** as
covering its ancestors:

- **62%** of annotation-grounded `core_functions` terms (4516 / 7278) would be
  lost if IBA were the only evidence.
- Restricting to **molecular function** and excluding low-information `binding`
  terms (GO:0005488, incl. `protein binding`): **511 curated core molecular
  functions across 423 genes** have **no IBA support at all**, **401** of them
  grounded by experimental/traceable evidence (IDA/IMP/IPI/EXP/TAS).

Because a term is only counted when it sits in a gene's `core_functions` — the
curator's distilled, highest-confidence judgement of what the protein *does* —
these are not annotation noise; they are the central activities a leaf-level
review would lose by trusting IBA alone. Two mechanisms recur:

### A. Activity absent from IBA entirely

The experimentally characterised activity is simply not propagated to the leaf —
no IBA annotation touches that branch — even though it is the protein's defining
biochemistry. These are clean, single-line losses (each verified: strong
non-IBA evidence, **zero** IBA at the term or any descendant):

| Gene | Core molecular function IBA misses | Evidence |
|------|-------------------------------------|----------|
| **USP21** | cysteine-type deubiquitinase activity (GO:0004843); deNEDDylase (GO:0019784) | IDA (PMID:10799498, PMID:32011234), IMP (PMID:26100909) |
| **P4HB** (PDI) | protein disulfide isomerase (GO:0003756); protein-disulfide reductase (GO:0015035) | EXP, IDA |
| **INPP5D** (SHIP1) | inositol-polyphosphate / PI(3,4,5)P3 5-phosphatase (GO:0004445, GO:0034485) | EXP, IDA |
| **FTH1** | ferroxidase activity (GO:0004322) | IMP |
| **PLD3** | single-stranded DNA 5′→3′ exonuclease (GO:0045145) | IDA |
| **NPM1** | histone chaperone activity (GO:0140713) | IDA |
| **PARK7** (DJ-1) | superoxide dismutase copper chaperone activity (GO:0016532) | IDA |
| **LRRK2** | GTPase activity (GO:0003924) | IDA |
| **SIRT2** | NAD-dependent demyristoylase (GO:0140773); tubulin deacetylase (GO:0042903) | IDA (PMID:25704306, PMID:32103017) |

### B. IBA stops at a general parent (true "too conservative")

Here IBA *does* annotate the gene with a broad term, but the experimentally
established **specific** activity — the exact substrate, regioselectivity, or
sub-activity — is never propagated. Closure confirms the IBA term is a strict
ancestor of the missed term, so this is genuine loss of resolution, not absence:

| Gene | IBA gives (general) | Experiment establishes (specific, IBA misses) |
|------|---------------------|------------------------------------------------|
| **HDAC6** | protein deacetylase (family) | tubulin deacetylase (GO:0042903); protein-lysine deacetylase (GO:0033558) — EXP/IDA/IMP |
| **SIRT2** | NAD-dependent deacetylase | histone **H4K16** deacetylase (GO:0046970) — IDA |
| **DPEP1** | (peptidase) | metallodipeptidase activity (GO:0070573) — IDA |
| **PARK7** (DJ-1) | (broader) | glyoxalase, glycolic-acid-forming (GO:1990422) — IDA |

**Caveat — IBA is not always the laggard.** Many of these genes are exceptionally
well studied; IBA legitimately covers their *canonical* function and only misses
secondary or recently characterised activities. **PTEN** is the clearest example:
its textbook PIP3 3-phosphatase activity (GO:0016314) *is* carried by IBA; what
IBA misses is the secondary protein-serine/threonine phosphatase (GO:0004722,
IDA PMID:9256433) and PI(3,4)P2 3-phosphatase (GO:0051800) activities. So
"incompleteness" should be read as *resolution and coverage gaps*, not as IBA
being useless — the same tool's forward direction shows IBA is the **sole**
support for 66 human core molecular functions (e.g. AKIRIN2 transcription
coregulator, GET1 protein-membrane adaptor, ATG14 PI3K regulator), so the two
analyses bound IBA's value from both sides.

**Reproduce:** `just subtraction-report-iba-conservative-core-mf` (writes
`reports/iba-too-conservative-core-mf.md`, the full ranked, evidence-enriched
table for all 423 genes); the raw keep-only TSVs come from
`just subtraction-report-iba-only-tsv`.

**Lesson for curators:** a leaf with only IBA annotations is very likely
*under*-annotated, not fully annotated. When IBA supplies only a broad
molecular-function term, treat it as a prompt to look for the specific
experimentally defined activity rather than as a finished call.

## Recommendations for IBA Curation

1. **Flag pseudo-enzyme candidates**: Proteins with enzyme domains but missing catalytic residues
2. **Flag neo-functionalized subfamilies**: Long branch lengths and different EC numbers indicate potential opposite function
3. **Validate substrate specificity**: Don't assume identical specificity across orthologs
4. **Distinguish core vs. secondary**: Mark promiscuous activities as non-core
5. **Prefer specific terms**: Replace generic IBA with specific terms when evidence exists
6. **Check for functional divergence**: Especially in rapidly evolving families
7. **Consider organism-specific biases**: Source annotations may reflect experimental systems (e.g., NMJ in flies) that don't apply to target species
8. **Validate annotations at family root**: Root-level annotations propagate everywhere - ensure they're truly universal to ALL subfamilies
9. **Synthesize multiple lines of evidence before flagging — never a single keyword**: a UniProt keyword (especially "By similarity"), a PANTHER node label, and a review assertion are each *individually* weak. Cross-check the term definition, direct experimental papers in the target species, the IBA WITH/FROM provenance, the MSA/active-site residues, and phylogenetic placement, and reason over the whole picture. The strongest REMOVE cases pair an explicit UniProt CAUTION/NOT with direct enzymology (DPYSL2, AGO4, CRYAA, AGK)
10. **Watch for opposite-sign family members**: When a family contains both activators and inhibitors (e.g., BCL2 family), a family-node IBA can transfer the wrong regulatory sign — inspect the WITH/FROM list for mixed members (but check whether independent non-IBA evidence also supports the term before calling it flatly wrong)
11. **Distinguish sub-activities**: capping vs severing, holdase vs foldase, slicing vs non-slicing — family-level IBA flattens these distinctions
12. **Don't inherit a paralog's compartment/complex**: family members share folds but not localization or complex membership — verify the protein actually occupies the annotated complex/compartment (EIF4E2, ALDH1L1, PEX2)
13. **Check the GO term's definition, not just its label, before calling an IBA directionally wrong**: e.g. "copper ion import" (GO:0015677) covers movement into a cell *or organelle*, so a Golgi-loading copper exporter can still satisfy it — a label that *looks* opposite may not be
14. **Read the WITH/FROM column first**: it names the exact source proteins. If they are the wrong family (NTN1←POU TFs; NOTCH1←SLITs) or a single wrong paralog (ABRAXAS1←ABRAXAS2; HINT2←HINT1), that is near-mechanical evidence of error. If they are a broad, coherent set of true orthologs, the transfer is probably defensible — slow down before flagging

## Quality Indicators

**Signs of problematic IBA**:
- Enzymatic activity for proteins with degenerate active sites
- **Long branch lengths from family root** (indicates divergence/neo-functionalization)
- **Different EC numbers between subfamilies** (may catalyze opposite reactions!)
- Generic terms when specific function is known
- Process annotations that don't match organism biology
- Multiple conflicting IBA annotations
- **Superfamily contains members with different transport mechanisms** (e.g., solute export vs lipid flipping in SMR family)
- **Enzymatic terms on proteins with a UniProt-documented degenerate/absent active site** (the strongest signal; e.g. DPYSL2, AGO4)
- **Family unites opposite-sign regulators** (activators + inhibitors of the same process; check WITH/FROM for mixed members — but confirm against non-IBA evidence)
- **Complex-membership or compartment terms on a protein whose paralog/relative occupies it instead** (cytosolic vs mitochondrial; eIF4F vs 4EHP repressor)

**NOT reliable grounds for flagging — verify with reasoning, not a single keyword**:
- A label that merely *looks* opposite — check the term **definition**. GO:0015677 "copper ion import" covers movement into a cell *or organelle*, so a Golgi-loading copper exporter (ATP7B) still satisfies it. (This is why ATP7B was **not** flagged.)
- A shared reaction that is *classified* under a pathway does not prove pathway membership in vivo — but it does mean the activity is real, so prefer "over-annotation/non-core" over "absent" (HMGCS2: the HMG-CoA-synthase step is genuine; only the FPP-pathway *flux* belongs to the other paralog).
- **Neither** a UniProt keyword **nor** a review assertion is sufficient on its own. Weigh all lines: a UniProt "By similarity" tag is weak and can be overturned by direct experimental papers (AGK: "ceramide By similarity" is refuted by two papers reporting no ceramide/sphingosine phosphorylation — so AGK *was* flagged); an explicit UniProt CAUTION or a curated NOT annotation is strong (DPYSL2, CRYAA).
- A broad **subsuming compartment** is not wrong just because a more specific location is known. `GO:0005737` cytoplasm includes mitochondrion, ER, Golgi, and lysosome (`part_of` cytoplasm), so "cytoplasm" is defensible for an organellar protein; only nucleus, plasma membrane, the extracellular space, or a *different* organelle are mutually exclusive enough to justify a localization REMOVE (see Pattern 13).

**Signs of reliable IBA**:
- Core metabolic enzymes with conserved mechanism
- Well-defined pathways with conserved components
- Structural proteins with conserved function
- Process/location terms that are organism-agnostic
- **Subfamilies with high sequence identity and same EC number**

---

## Project history & methodology

This page records the **synthesized findings**. The dated project log, the per-pass
verification narrative (what was added, what was retracted and why), and the
**lessons learned** are kept separately in [IBA_REVIEW/HISTORY.md](IBA_REVIEW/HISTORY.md).

A reproducible **multiple-sequence-alignment check** of the two central pseudo-enzyme
claims (Argonaute catalytic tetrad; CRMP/DPYSL metal-coordinating residues) lives in
[IBA_REVIEW/msa/](IBA_REVIEW/msa/RESULTS.md) — `uv run python catalytic_residue_msa.py`.
