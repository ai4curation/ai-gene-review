---
title: "IBA Annotation Quality Project"
maturity: COMPLETE
tags: [PIPELINE, FLAGSHIP]
---

# IBA Annotation Quality Project

## Overview

This project examines the quality of IBA (Inferred from Biological Aspect of Ancestor) annotations discovered through AI-assisted gene review. IBA annotations use phylogenetic trees to transfer function from characterized proteins to uncharacterized orthologs.

While IBA is a powerful curation tool, it can produce problematic annotations when:
1. **Functional divergence** - Orthologs have evolved different functions
2. **Pseudo-enzymes** - Catalytic function lost despite domain retention
3. **Context-specific function** - Function differs between organisms/tissues
4. **Over-generalization** - Broad terms transferred when specific functions differ

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
- **DPYSL2 / CRMP1 / DPYSL3** — `GO:0016812` (metallo-hydrolase activity, cyclic amides): the CRMP/dihydropyrimidinase-like proteins are explicitly flagged by UniProt CAUTION — *"Lacks most of the conserved residues that are essential for binding the metal cofactor and hence for dihydropyrimidinase activity."* They are non-catalytic cytoskeletal regulators.
- **AGO4** — `GO:0004521` (RNA endonuclease activity): UniProt FUNCTION states directly that AGO4 *"Lacks endonuclease activity and does not appear to cleave target mRNAs"* — only AGO2 is the catalytic slicer in humans.
- **UBAC2** — `GO:0004252` (serine-type endopeptidase activity): UBAC2 has a rhomboid-**like** fold (a known inactive-rhomboid/pseudoprotease clan) but UniProt attributes no protease function — its curated roles are as an ERAD/ER-phagy adaptor. *(Caveat: the absence of catalytic residues is inferred from the inactive-rhomboid classification and the lack of any curated protease activity, not from an explicit UniProt CAUTION.)*
- **Lesson**: a degenerate/absent active site, **independently documented**, is the strongest single signal that an enzymatic IBA is wrong. This pattern is now represented by Epe1 (demethylase), the CRMP family (amidohydrolase), AGO4 (slicer), and UBAC2 (protease).

### 8. Partial Sub-Activity Loss Within a Multidomain Family

**The Problem**: Distinct from full pseudo-enzymes — the protein **retains part of the ancestral activity but lost a specific sub-activity**, and IBA transfers the lost sub-activity.

**Examples (REMOVE — verified)**:
- **CAPG (human)** — `GO:0051014` (actin filament **severing**): CAPG caps but does **not** sever. The original characterization (cached PMID:1322908) states verbatim that CAPG *"reversibly blocks the barbed ends of actin filaments but does not sever preformed actin"*. The severing term over-extends from the gelsolin/villin family; CAPG retains capping only.
- **human/CRYAA** — `GO:0042026` (protein **refolding**): αA-crystallin is an ATP-independent **holdase** that prevents aggregation but cannot refold clients. This one is corroborated **inside GOA itself**: there is an explicit curated `NOT|involved_in` (ISS) annotation to GO:0042026, which the IBA directly contradicts. UniProt describes only aggregation-prevention chaperone activity, no refolding.
- **Lesson**: capping≠severing and holdase≠foldase are sub-activity distinctions that family-level IBA flattens. The CRYAA case is especially clean because a curator already negated the term.

### 9. Regulatory-Sign Inversion Within a Family

**The Problem**: When a protein family contains members with **opposite regulatory signs** (activators vs inhibitors of the same process), a family-node IBA can transfer the wrong sign.

**Example - BCL2 (human and mouse)**:
- IBA annotation: `GO:0043065` (**positive** regulation of apoptotic process)
- Reality: BCL2 is the prototypical **anti-apoptotic** guardian; it inhibits MOMP and cytochrome c release (PMID:9027314, PMID:9219694).
- **Root cause (verified from GOA WITH/FROM)**: the IBA for GO:0043065 is inferred from a PANTHER node (PTN000135648) whose WITH/FROM list **mixes pro- and anti-apoptotic BCL2-family members** — pro-apoptotic BAX (Q07812) and BAK1 (Q16611) alongside anti-apoptotic members. The shared BH-domain fold unites activators and inhibitors of apoptosis under one family, so the "positive regulation" sign can leak onto BCL2.
- **Caveat (why this is "non-core" rather than flatly "wrong")**: BCL2 *does* have documented context-dependent pro-apoptotic behavior (e.g. caspase-cleaved BCL2), and GOA additionally carries a separate **NAS** annotation (PMID:14634621, ComplexPortal) to the very same GO:0043065. So the honest framing is that the *IBA family-node inference is unreliable for sign* (verified mechanism), not that positive regulation is impossible for BCL2. The companion review more confidently re-points related terms to their negative-regulation children (e.g. `GO:0001836` release of cytochrome c → `GO:0090201` *negative* regulation of release of cytochrome c).

### 10. Complex / Compartment Membership Over-Transfer

**The Problem**: A family-level IBA asserts membership in a **specific complex or compartment** that the target protein does not actually belong to, even though the catalytic fold or sequence homology is real.

**Examples (REMOVE — verified)**:
- **EIF4E2 (human)** — `GO:0016281` (eIF4F complex): 4EHP/EIF4E2 binds the cap but UniProt states it *"is unable to bind eIF4G"* and *"Does not interact with eIF4G"*; it is a translational repressor (4EHP-GYF2 complex), never an eIF4F subunit. A clear family-level over-transfer from EIF4E.
- **ALDH1L1 (rat)** — `GO:0005739` (mitochondrion): UniProt names it *Cytosolic 10-formyltetrahydrofolate dehydrogenase* with `SUBCELLULAR LOCATION: Cytoplasm, cytosol` and a cytosol IDA. Mitochondrial one-carbon oxidation is the job of the distinct paralog **ALDH1L2**.
- **PEX2 (human)** — `GO:0016593` (Cdc73/Paf1 complex): PEX2 is a peroxisomal RING E3 ligase for PEX5 retrotranslocation (UniProt) and has no role in RNA Pol II transcription elongation, so membership in the Cdc73/Paf1 complex is clearly wrong. *(Caveat: the cause is unconfirmed — the IBA WITH/FROM is a PANTHER node, not a PAF1 gene. A legacy synonym collision — PEX2's old name "PAF1"/Peroxisome Assembly Factor 1 vs the unrelated transcription factor PAF1 — is a plausible but unverified explanation.)*
- **Lesson**: complex membership and compartment are not conserved across paralogs/family members even when the fold is; verify the protein actually occupies the annotated complex/compartment.

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
| PEX2 | human | Complex over-transfer (peroxisomal E3, not Cdc73/Paf1 complex) | MEDIUM | COMPLETE |

## Recommendations for IBA Curation

1. **Flag pseudo-enzyme candidates**: Proteins with enzyme domains but missing catalytic residues
2. **Flag neo-functionalized subfamilies**: Long branch lengths and different EC numbers indicate potential opposite function
3. **Validate substrate specificity**: Don't assume identical specificity across orthologs
4. **Distinguish core vs. secondary**: Mark promiscuous activities as non-core
5. **Prefer specific terms**: Replace generic IBA with specific terms when evidence exists
6. **Check for functional divergence**: Especially in rapidly evolving families
7. **Consider organism-specific biases**: Source annotations may reflect experimental systems (e.g., NMJ in flies) that don't apply to target species
8. **Validate annotations at family root**: Root-level annotations propagate everywhere - ensure they're truly universal to ALL subfamilies
9. **Verify catalytic-residue loss against UniProt before calling a pseudo-enzyme**: the strongest REMOVE cases (DPYSL2, AGO4) cite an explicit UniProt CAUTION/FUNCTION statement, not just a review assertion
10. **Watch for opposite-sign family members**: When a family contains both activators and inhibitors (e.g., BCL2 family), a family-node IBA can transfer the wrong regulatory sign — inspect the WITH/FROM list for mixed members (but check whether independent non-IBA evidence also supports the term before calling it flatly wrong)
11. **Distinguish sub-activities**: capping vs severing, holdase vs foldase, slicing vs non-slicing — family-level IBA flattens these distinctions
12. **Don't inherit a paralog's compartment/complex**: family members share folds but not localization or complex membership — verify the protein actually occupies the annotated complex/compartment (EIF4E2, ALDH1L1, PEX2)
13. **Check the GO term's definition, not just its label, before calling an IBA directionally wrong**: e.g. "copper ion import" (GO:0015677) covers movement into a cell *or organelle*, so a Golgi-loading copper exporter can still satisfy it — a label that *looks* opposite may not be

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

**NOT reliable signs of a bad IBA (verify before flagging)**:
- A label that merely *looks* opposite — check the term definition (GO:0015677 "copper ion import" includes import into an *organelle*)
- A "no activity reported" claim in a review when UniProt still curates the activity (e.g. AGK sphingosine/ceramide kinase) — defer to the curated record

**Signs of reliable IBA**:
- Core metabolic enzymes with conserved mechanism
- Well-defined pathways with conserved components
- Structural proteins with conserved function
- Process/location terms that are organism-agnostic
- **Subfamilies with high sequence identity and same EC number**

---

# STATUS

## Analyzed Genes
- [x] pombe/Epe1 - Pseudo-enzyme propagation (HIGH severity)
- [x] MYCTU/cds1 - Neo-functionalization opposite reaction (CRITICAL severity)
- [x] VIBCH/cds1 - Neo-functionalization opposite reaction (CRITICAL severity)
- [x] CANAL/LPL1 - Substrate specificity (MEDIUM severity)
- [x] human/UBA7 - Generic vs specific terms (LOW severity)
- [x] human/RIMBP2 - Organism/tissue context transfer (MEDIUM severity)
- [x] ECOLI/arnF - Mechanism divergence in SMR superfamily (MEDIUM severity)
- [x] human/DPYSL2, CRMP1, DPYSL3 - Pseudo-enzyme; UniProt CAUTION confirms missing metal residues (HIGH severity)
- [x] human/AGO4 - Pseudo-enzyme; UniProt "lacks endonuclease activity" (HIGH severity)
- [x] human/UBAC2 - Pseudo-enzyme; rhomboid-like, no curated protease activity (MEDIUM severity)
- [x] human/CAPG - Partial sub-activity loss; PMID:1322908 "does not sever" (MEDIUM severity)
- [x] human/CRYAA - Partial sub-activity loss; curated NOT(refolding) ISS in GOA (MEDIUM severity)
- [x] human/BCL2, mouse/Bcl2 - Regulatory-sign inversion; family-node mixes pro-/anti- (MEDIUM severity, with caveat)
- [x] human/EIF4E2 - Complex over-transfer; UniProt "does not bind eIF4G" (MEDIUM severity)
- [x] rat/Aldh1l1 - Compartment conflation; UniProt cytosolic, mito is ALDH1L2 (MEDIUM severity)
- [x] human/PEX2 - Complex over-transfer; peroxisomal E3, not Paf1 complex (MEDIUM severity)

## Retracted on second-pass verification (do NOT re-add without new evidence)
- [ ] ~~human/ATP7B (copper import inversion)~~ — GO:0015677 covers import into an *organelle*; ATP7B loads Cu into the Golgi, so the term is defensible
- [ ] ~~human/AGK (acylglycerol vs ceramide kinase)~~ — UniProt curates sphingosine (experimental) + ceramide (by similarity) phosphorylation; the "no activity" basis is contradicted
- [ ] ~~rat/Hmgcs2 (mevalonate pathway conflation)~~ — UniProt assigns HMGCS2 to `(R)-mevalonate biosynthesis`; the pathway link is not clearly wrong

## Patterns Identified
- [x] Pseudo-enzyme IBA propagation (now Epe1 + CRMP family + AGO4 + UBAC2 — recurring, not isolated)
- [x] **Neo-functionalization: opposite reaction in subfamily** (most severe type)
- [x] Substrate specificity over-transfer
- [x] Secondary activity promotion
- [x] Organism/tissue context transfer
- [x] Mechanism divergence within structural superfamily (same fold, different transport mechanism)
- [x] **Partial sub-activity loss** (capping vs severing, holdase vs foldase)
- [x] **Regulatory-sign inversion within a family** (anti- vs pro-, mixed WITH/FROM — BCL2; flag with caution)
- [x] **Complex/compartment membership over-transfer** (EIF4E2, ALDH1L1, PEX2)

Last updated: 2026-06-20

# NOTES

## 2026-06-20

**Second corpus pass — mined the full review set (2,732 gene reviews) for IBA annotations flagged by AI review, then independently verified each candidate before adding it.**

Distribution of `review.action` over IBA-evidence annotations across the corpus:
`ACCEPT 4651 · KEEP_AS_NON_CORE 943 · MODIFY 321 · MARK_AS_OVER_ANNOTATED 189 · REMOVE 190 · UNDECIDED 39 · NEW 33 · PENDING 11`.

So ~700 IBA annotations were flagged as more than acceptable, and 190 were judged outright wrong (REMOVE) in the per-gene reviews. I shortlisted ~12 candidates and **independently checked each against the UniProt record, the GO term definition, the GOA WITH/FROM provenance, and cached publications** — not just the review YAML. The verification mattered: **three candidates were retracted** because the primary evidence contradicted the review's reasoning.

**Verification step (key, because flagging an IBA wrong is a strong claim).** Result:

*Added (verified):*
1. **Pseudo-enzyme, UniProt-documented** — DPYSL2/CRMP1/DPYSL3 (`GO:0016812`; UniProt CAUTION: *"Lacks most of the conserved residues … essential for binding the metal cofactor"*) and AGO4 (`GO:0004521`; UniProt FUNCTION: *"Lacks endonuclease activity and does not appear to cleave target mRNAs"*). UBAC2 (`GO:0004252`) added more cautiously — rhomboid-like fold + no curated protease activity, but no explicit CAUTION.
2. **Partial sub-activity loss** — CAPG (`GO:0051014`; cached PMID:1322908 verbatim *"does not sever preformed actin"*) and CRYAA (`GO:0042026`; corroborated by an explicit curated `NOT|involved_in` ISS annotation already in GOA).
3. **Regulatory-sign inversion** — BCL2 (`GO:0043065`); verified that the IBA WITH/FROM node (PTN000135648) mixes pro-apoptotic BAX (Q07812)/BAK1 (Q16611) with anti-apoptotic members. **Kept with a caveat**: GOA also has a non-IBA NAS annotation to the same term and BCL2 has context-dependent pro-apoptotic roles, so the defensible claim is "the IBA family-node sign is unreliable," not "positive regulation is impossible."
4. **Complex/compartment over-transfer** — EIF4E2 (`GO:0016281`; UniProt *"does not interact with eIF4G"*), ALDH1L1 (`GO:0005739`; UniProt cytosolic, mito paralog is ALDH1L2), PEX2 (`GO:0016593`; peroxisomal E3, biologically not a Paf1-complex member — though the "name collision" *cause* is unverified).

*Retracted on verification (do not re-add without new evidence):*
- **ATP7B / `GO:0015677` (copper import)** — I had called this a "direction inversion." But the GO definition is *"movement of copper ions into a cell **or organelle**,"* and ATP7B pumps Cu(I) from the cytosol **into the Golgi lumen**. So the term is defensible for a Golgi-loading exporter; the "opposite direction" framing was wrong. **Lesson: read the term definition, not the label.**
- **AGK / ceramide & sphingosine kinase (`GO:0001729`, `GO:0046513`, `GO:0046512`)** — the review claimed "no significant ceramide/sphingosine phosphorylation," but the UniProt record (gene name "Multiple substrate lipid kinase") curates **sphingosine** phosphorylation (experimental, PubMed:15939762) and **ceramide** (by similarity). The REMOVE basis is contradicted by the curated record. **Lesson: defer to UniProt when it still curates the activity.**
- **HMGCS2 / `GO:0010142` (mevalonate pathway)** — UniProt explicitly assigns HMGCS2 to `PATHWAY: (R)-mevalonate biosynthesis; step 2/3`. The mevalonate link is the enzyme's actual reaction step; the cytosol-vs-mito flux argument makes it at most over-annotation/non-core, not flatly wrong.

**Methodological note**: examples originate from existing per-gene reviews in `genes/*/*/*-ai-review.yaml`, but inclusion here required first-party verification (UniProt `*-uniprot.txt`, QuickGO term definitions, GOA `*-goa.tsv` WITH/FROM, cached `publications/`). ~175 additional REMOVE-flagged IBA annotations remain un-triaged — future-pass candidates, each to be verified the same way (e.g., PIWIL1 piRNA cross-aspect, human/CRY1 and human/CRY2 photo-entrainment, ankzf1 ERAD vs RQC).

## 2026-03-04

**Added ECOLI/arnF - Mechanism Divergence Within SMR Superfamily**

arnF illustrates a new pattern: **mechanism divergence within a structural superfamily**. The PANTHER family PTHR30561 groups the entire SMR/DMT superfamily — EmrE (drug efflux), MdtI/J (spermidine export), Gdx (guanidinium export), Mmr (multidrug resistance), and ArnE/ArnF (lipid flipping). All share the same 4-TM-helix fold, but ArnE/ArnF evolved a fundamentally different transport mechanism: intramembrane lipid translocation rather than transmembrane solute export.

The IBA WITH/FROM field reveals the problem directly:
- GO:0022857 (transmembrane transporter activity): inferred from EmrE (P23895), MdtI (P69210), MdtJ (P69212), Gdx (P69937), Mmr (P9WGF1), ArnE (Q47377), and ArnF itself
- All the non-ArnE/ArnF proteins are genuine solute exporters; the annotation is correct for them but misleading for arnF

**Comparison with other IBA issue types**:
- Epe1: function **lost** (pseudo-enzyme) — HIGH severity
- cds1: function **inverted** (opposite reaction) — CRITICAL severity
- arnF: function **diverged in mechanism** (flip vs export) — MEDIUM severity

arnF sits in a middle ground: the IBA isn't wrong (it IS a transporter), but it mischaracterizes the mechanism. The correct term GO:0140303 (intramembrane lipid transporter activity) captures the flippase specificity.

**EcoCyc annotation quality**: EcoCyc contributed 5 of 18 annotations. The two "response to iron(III) ion" annotations (IGI + IEP) are classic over-annotations — they annotate based on transcriptional regulation rather than direct function. Iron activates BasS-BasR → induces arn operon → ArnF is expressed. But ArnF doesn't sense, bind, or respond to iron. EcoCyc's IMP annotations (carbohydrate derivative transport/transporter activity) and IDA (plasma membrane) are well-supported and accurate.

## 2026-01-26

**Added PTHR10314/cds1 - Neo-Functionalization (Opposite Reaction) Pattern**

This is arguably the most informative example for the IBA quality review project. The cds1 case (subfamily SF135 of PTHR10314) demonstrates the **most severe type of IBA error**: annotation of the exact **opposite biological function**.

Key findings from family analysis:
- GO:0019344 (cysteine biosynthetic process) is annotated at family root and propagates to all descendants
- Subfamily SF135 (Cds1/desulfhydrases) underwent neo-functionalization: same fold, opposite reaction
- Cds1 catalyzes cysteine **CATABOLISM** (EC 4.4.1.1): L-Cys → H2S + pyruvate + NH3
- IBA says cysteine **BIOSYNTHESIS** - directionally wrong!

Evidence of neo-functionalization in SF135:
1. Longest branch length (0.528) from root = most sequence divergence
2. Different EC class: 4.4.1.1 vs 2.5.1.47
3. Only 24% identity with synthases (synthases share 43% with each other)
4. Different active site motif: ASSGST vs PTSGNTG

Detailed analysis in: `interpro/panther/PTHR10314/PTHR10314-notes.md`

This pattern represents a new category beyond the previously identified issues:
- Pseudo-enzyme (Epe1): function lost, but domain retained
- Neo-functionalization (cds1): function **inverted**, same fold

Both reviewed genes (MYCTU/cds1, VIBCH/cds1) have comprehensive reviews with experimental evidence from PMID:34439535 and PMID:34283874.

---

**Added RIMBP2 - Organism Context Transfer Pattern**

RIMBP2 illustrates a subtle but important IBA quality issue: **context-specific term transfer**. The IBA annotation `GO:0007274` (neuromuscular synaptic transmission) was transferred from the Drosophila ortholog (FB:FBgn0262483), where NMJ is a primary experimental system for studying synaptic function.

However, human RIMBP2 functions primarily at:
- Hippocampal mossy fiber synapses
- CA3-CA1 synapses
- Auditory ribbon synapses

Not at neuromuscular junctions. The annotation isn't "wrong" in the sense that RIMBP2 is involved in synaptic transmission, but it's misleading because it implies NMJ function.

**Key Insight**: IBAs are only as good as the manual annotations on orthologs. When source organisms have biased annotation (e.g., flies are heavily annotated at NMJ because that's the accessible synapse type), this bias propagates through phylogenetic inference.

**Family-Level Analysis (PTHR14234)**: The PANTHER family analysis provides additional context:
- Representative structure is *Drosophila* RIM-BP (PDB 4z8a) - fly-centric
- Family includes RIMBP3 (SF21) which is **non-synaptic** (testis/spermiogenesis)
- Family research warns: "Avoid propagating 'regulation of neurotransmitter release' to RIMBP3 paralogs"
- This shows IBA issues can affect entire subfamilies when root annotations don't apply universally

See: `interpro/panther/PTHR14234/PTHR14234-deep-research-falcon.md`

**Recommendation**: For synaptic genes, consider whether the specific synapse type in the term (NMJ, CNS, etc.) actually applies to the target species, or whether a more general synaptic transmission term would be more accurate.

## 2026-01-22

**Project Creation**

Documented IBA quality issues discovered through AI review.

**Key Finding**: The most severe IBA quality issue is **pseudo-enzyme propagation** - transferring enzymatic activity to proteins that have lost catalytic function while retaining the domain fold.

**Epe1 Case Study**:
- JmjC domain → IBA from active demethylases
- Epe1 has HVD motif (not HXD), missing Fe(II) coordination
- Mass spec assays: NO demethylation detected
- H297A catalytic mutant: retains anti-silencing function
- **Conclusion**: All enzymatic IBA annotations should be REMOVE

**Recommendation**: Develop automated pipeline to flag IBA annotations for proteins with degenerate active site motifs.
