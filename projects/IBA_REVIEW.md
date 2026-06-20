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

### 7. Directional/Polarity Inversion in Transporters

**The Problem**: A transporter is annotated with the **opposite direction** of solute movement, because the family node groups members that move the substrate either way (or the source captures the wrong vectorial sense).

**Example - ATP7B (human)**:
- IBA annotation: `GO:0015677` (copper ion **import**)
- Reality: ATP7B is a copper **exporter** — it pumps Cu(I) out of the cytosol into the Golgi lumen and bile-canalicular vesicles. Cellular copper **import** is done by CTR1/SLC31A1, an unrelated protein.
- A second IBA error places ATP7B at the `GO:0005886` plasma membrane (it traffics to pericanalicular vesicles, not the canalicular/plasma membrane; PM trafficking is the paralog **ATP7A**'s behavior, PMID:16472602).
- **Impact**: Like cds1, this is a **directionally wrong** annotation — the gene moves copper in exactly the opposite sense the term states.

### 8. Regulatory-Sign Inversion Within a Family

**The Problem**: When a protein family contains members with **opposite regulatory signs** (activators vs inhibitors of the same process), a family-node IBA can transfer the wrong sign.

**Example - BCL2 (human and mouse)**:
- IBA annotation: `GO:0043065` (**positive** regulation of apoptotic process)
- Reality: BCL2 is the prototypical **anti-apoptotic** guardian; it inhibits MOMP and cytochrome c release. Positive regulation of apoptosis is the opposite of its function (PMID:9027314, PMID:9219694).
- **Root cause (verified from GOA WITH/FROM)**: the IBA for GO:0043065 is inferred from a PANTHER node (PTN000135648) whose WITH/FROM list **mixes pro- and anti-apoptotic BCL2-family members** — pro-apoptotic BAX (Q07812), BAK1 (Q16611), and others alongside anti-apoptotic members. The shared BH-domain fold unites activators and inhibitors of apoptosis under one family, so the "positive regulation" sign leaks onto BCL2.
- The same review also re-points several BCL2 BP terms toward their **negative-regulation** counterparts (e.g. `GO:0001836` release of cytochrome c → `GO:0090201` negative regulation of release of cytochrome c).
- **Impact**: This is the regulatory analogue of cds1's opposite-reaction error — same fold, opposite biological sign.

### 9. Pseudo-Enzyme Propagation Is a Recurring Human Pattern

**The Problem**: The Epe1 pseudo-demethylase case is not isolated. Catalytic-residue loss with fold retention recurs across many human families, and IBA repeatedly transfers the ancestral enzymatic activity to the catalytically dead member.

**Examples (all REMOVE, refuted on biological grounds — missing catalytic residues)**:
- **DPYSL2 / CRMP1 / DPYSL3** — `GO:0016812` (metallo-hydrolase activity, cyclic amides): the dihydropyrimidinase-like CRMP proteins lack the metal-coordinating residues (UniProt CAUTION). They are non-catalytic cytoskeletal regulators, not amidohydrolases.
- **UBAC2** — `GO:0004252` (serine-type endopeptidase activity): a rhomboid **pseudoprotease** with no catalytic Ser/His dyad.
- **AGO4** — `GO:0004521` (RNA endonuclease activity): a **non-slicing** Argonaute paralog lacking the intact DEDH catalytic tetrad of AGO2.
- **Lesson**: a degenerate active site is the strongest single signal that an enzymatic IBA is wrong. This pattern is now represented by Epe1 (demethylase), the CRMP family (amidohydrolase), UBAC2 (protease), and AGO4 (slicer).

### 10. Partial Sub-Activity Loss Within a Multidomain Family

**The Problem**: Distinct from full pseudo-enzymes — the protein **retains part of the ancestral activity but lost a specific sub-activity**, and IBA transfers the lost sub-activity.

**Examples**:
- **CAPG (human)** — `GO:0051014` (actin filament **severing**): CAPG has only 3 of gelsolin's 6 domains and **caps** but does **not sever** F-actin. The original characterization states it "does not sever preformed actin filaments" (PMID:1322908). The severing term over-extends from gelsolin.
- **human/CRYAA** — `GO:0042026` (protein **refolding**): αA-crystallin is an ATP-independent **holdase** that prevents aggregation but cannot **refold** clients (which needs a foldase/ATP). The sHSP family is functionally heterogeneous (PMID:19464326), so refolding does not transfer.
- **Lesson**: capping≠severing and holdase≠foldase are sub-activity distinctions that family-level IBA flattens.

### 11. Synonym / Gene-Name Collision

**The Problem**: IBA (or the upstream grouping) is seeded by a **name collision** — two unrelated genes share a legacy symbol — and the function of the wrong gene is transferred.

**Examples**:
- **PEX2 (human)** — `GO:0016593` (Cdc73/Paf1 complex): PEX2 carries the legacy synonym **PAF1** ("Peroxisome Assembly Factor 1"), which is **not** the *PAF1* (RNA Pol II-associated factor 1) that belongs to the Cdc73/Paf1 complex. PEX2 is a peroxisomal RING E3 ligase with no role in transcription elongation.
- **P3R3URF (human)** — `GO:0019221` (cytokine-mediated signaling): a putative uORF microprotein whose IBA conflates it with the canonical **PIK3R3** biology it sits upstream of.
- **Lesson**: a single instructive failure mode where the homology/grouping itself is an artifact of nomenclature, not biology.

### 12. Paralog Compartment / Pathway Conflation

**The Problem**: Cytosolic and mitochondrial (or otherwise compartment-split) paralogs share a fold; IBA transfers the **other paralog's compartment or pathway**.

**Examples**:
- **ALDH1L1 (rat)** — `GO:0005739` (mitochondrion): ALDH1L1 is the **cytosolic** 10-formyl-THF dehydrogenase; mitochondrial one-carbon oxidation is the job of the paralog **ALDH1L2**.
- **HMGCS2 (rat)** — `GO:0010142` (farnesyl-PP biosynthesis, mevalonate pathway): mitochondrial HMGCS2 feeds **ketogenesis**; the mevalonate/isoprenoid pathway is the cytosolic paralog **HMGCS1**.
- **AGK (human)** — `GO:0001729`/`GO:0046513`/`GO:0046512` (ceramide/sphingosine kinase & biosynthesis) and `GO:0005886` (plasma membrane): AGK is a **mitochondrial acylglycerol kinase** (and TIM22 subunit); the ceramide-kinase activity and PM localization belong to the unrelated CERK it was co-discovered with.
- **EIF4E2 (human)** — `GO:0016281` (eIF4F complex): 4EHP/EIF4E2 binds the cap but **cannot bind eIF4G** and never assembles into eIF4F — an erroneous family-level complex-membership transfer from EIF4E.
- **Lesson**: compartment and pathway are not conserved across paralogs even when the catalytic fold is; check which paralog actually does the annotated job.

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
| ATP7B | human | **Transporter direction inversion (export annotated as import)** | **HIGH** | COMPLETE |
| BCL2 | human, mouse | **Regulatory-sign inversion (anti- annotated as pro-apoptotic)** | **HIGH** | COMPLETE |
| DPYSL2/CRMP1/DPYSL3 | human | Pseudo-enzyme (metallo-hydrolase residues absent) | HIGH | COMPLETE |
| UBAC2 | human | Pseudo-enzyme (rhomboid pseudoprotease) | HIGH | COMPLETE |
| AGO4 | human | Pseudo-enzyme (non-slicing Argonaute) | MEDIUM | COMPLETE |
| CAPG | human | Partial sub-activity loss (caps but does not sever actin) | MEDIUM | COMPLETE |
| CRYAA | human | Partial sub-activity loss (holdase, not foldase) | MEDIUM | COMPLETE |
| PEX2 | human | Synonym/name collision (PAF1 ≠ Paf1 complex) | MEDIUM | COMPLETE |
| ALDH1L1 | rat | Paralog compartment conflation (cytosolic vs mito ALDH1L2) | MEDIUM | COMPLETE |
| HMGCS2 | rat | Paralog pathway conflation (ketogenesis vs mevalonate HMGCS1) | MEDIUM | COMPLETE |
| AGK | human | Paralog conflation (acylglycerol vs ceramide kinase) | MEDIUM | COMPLETE |
| EIF4E2 | human | Complex-membership over-transfer (cannot form eIF4F) | MEDIUM | COMPLETE |

## Recommendations for IBA Curation

1. **Flag pseudo-enzyme candidates**: Proteins with enzyme domains but missing catalytic residues
2. **Flag neo-functionalized subfamilies**: Long branch lengths and different EC numbers indicate potential opposite function
3. **Validate substrate specificity**: Don't assume identical specificity across orthologs
4. **Distinguish core vs. secondary**: Mark promiscuous activities as non-core
5. **Prefer specific terms**: Replace generic IBA with specific terms when evidence exists
6. **Check for functional divergence**: Especially in rapidly evolving families
7. **Consider organism-specific biases**: Source annotations may reflect experimental systems (e.g., NMJ in flies) that don't apply to target species
8. **Validate annotations at family root**: Root-level annotations propagate everywhere - ensure they're truly universal to ALL subfamilies
9. **Check transport/reaction direction**: For transporters and enzymes, confirm the **vectorial sense** (import vs export) and reaction direction match the term — families often unite both directions
10. **Watch for opposite-sign family members**: When a family contains both activators and inhibitors (e.g., BCL2 family), a family-node IBA can transfer the wrong regulatory sign — inspect the WITH/FROM list for mixed members
11. **Distinguish sub-activities**: capping vs severing, holdase vs foldase, slicing vs non-slicing — family-level IBA flattens these distinctions
12. **Beware synonym/name collisions**: A legacy shared symbol (e.g., PEX2's old name PAF1) can seed a homology grouping that is an artifact of nomenclature, not biology
13. **Don't inherit a paralog's compartment/pathway**: Cytosolic vs mitochondrial paralogs share folds but not localization or pathway — verify which paralog actually performs the annotated job

## Quality Indicators

**Signs of problematic IBA**:
- Enzymatic activity for proteins with degenerate active sites
- **Long branch lengths from family root** (indicates divergence/neo-functionalization)
- **Different EC numbers between subfamilies** (may catalyze opposite reactions!)
- Generic terms when specific function is known
- Process annotations that don't match organism biology
- Multiple conflicting IBA annotations
- **Superfamily contains members with different transport mechanisms** (e.g., solute export vs lipid flipping in SMR family)
- **Transport/reaction direction terms** (import vs export, biosynthesis vs catabolism) — verify the vectorial sense
- **Family unites opposite-sign regulators** (activators + inhibitors of the same process; check WITH/FROM for mixed members)
- **Compartment terms on a protein whose paralog occupies the other compartment** (cytosolic vs mitochondrial)
- **A legacy gene-name synonym shared with an unrelated gene** (name-collision groupings)

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
- [x] human/ATP7B - Transporter direction inversion (HIGH severity)
- [x] human/BCL2, mouse/Bcl2 - Regulatory-sign inversion (HIGH severity)
- [x] human/DPYSL2, CRMP1, DPYSL3 - Pseudo-enzyme, metallo-hydrolase residues absent (HIGH severity)
- [x] human/UBAC2 - Pseudo-enzyme, rhomboid pseudoprotease (HIGH severity)
- [x] human/AGO4 - Pseudo-enzyme, non-slicing Argonaute (MEDIUM severity)
- [x] human/CAPG - Partial sub-activity loss, caps but does not sever (MEDIUM severity)
- [x] human/CRYAA - Partial sub-activity loss, holdase not foldase (MEDIUM severity)
- [x] human/PEX2 - Synonym/name collision (MEDIUM severity)
- [x] rat/Aldh1l1 - Paralog compartment conflation (MEDIUM severity)
- [x] rat/Hmgcs2 - Paralog pathway conflation (MEDIUM severity)
- [x] human/AGK - Paralog conflation, acylglycerol vs ceramide kinase (MEDIUM severity)
- [x] human/EIF4E2 - Complex-membership over-transfer (MEDIUM severity)

## Patterns Identified
- [x] Pseudo-enzyme IBA propagation (now Epe1 + CRMP family + UBAC2 + AGO4 — recurring, not isolated)
- [x] **Neo-functionalization: opposite reaction in subfamily** (most severe type)
- [x] Substrate specificity over-transfer
- [x] Secondary activity promotion
- [x] Organism/tissue context transfer
- [x] Mechanism divergence within structural superfamily (same fold, different transport mechanism)
- [x] **Transporter direction inversion** (import vs export — ATP7B)
- [x] **Regulatory-sign inversion within a family** (anti- vs pro-, mixed WITH/FROM — BCL2)
- [x] **Partial sub-activity loss** (capping vs severing, holdase vs foldase)
- [x] **Synonym/gene-name collision** seeding the wrong homology grouping (PEX2)
- [x] **Paralog compartment/pathway conflation** (cytosolic vs mitochondrial)

Last updated: 2026-06-20

# NOTES

## 2026-06-20

**Second corpus pass — mined the full review set (2,732 gene reviews) for IBA annotations flagged by AI review.**

Distribution of `review.action` over IBA-evidence annotations across the corpus:
`ACCEPT 4651 · KEEP_AS_NON_CORE 943 · MODIFY 321 · MARK_AS_OVER_ANNOTATED 189 · REMOVE 190 · UNDECIDED 39 · NEW 33 · PENDING 11`.

So ~700 IBA annotations were flagged as more than acceptable, and **190 were judged outright wrong (REMOVE)**. The 6 originally featured genes were a small sample; this pass adds eleven new, repo-backed examples and **five new pattern categories**:

1. **Transporter direction inversion (ATP7B)** — `GO:0015677` copper *import* on a copper *exporter*. The transport analogue of the cds1 opposite-reaction error. Also a paralog-derived PM-localization error (ATP7A traffics to PM, ATP7B does not).
2. **Regulatory-sign inversion within a family (BCL2)** — `GO:0043065` *positive* regulation of apoptosis on the prototypical *anti*-apoptotic protein. Confirmed root cause from GOA: the IBA WITH/FROM for this term mixes pro-apoptotic (BAX Q07812, BAK1 Q16611) and anti-apoptotic BCL2-family members under one PANTHER node (PTN000135648), so the wrong sign leaks across the shared BH-domain fold. Same error appears in mouse Bcl2.
3. **Pseudo-enzyme propagation is recurrent, not a one-off** — beyond Epe1: the CRMP/DPYSL family (DPYSL2, CRMP1, DPYSL3) annotated with metallo-hydrolase activity despite absent metal-coordinating residues; UBAC2 (rhomboid pseudoprotease); AGO4 (non-slicing Argonaute). Degenerate active site = strongest single signal an enzymatic IBA is wrong.
4. **Partial sub-activity loss** — CAPG caps but does not sever actin (3 of gelsolin's 6 domains; PMID:1322908); CRYAA is a holdase, not a foldase (no refolding). Distinct from full pseudo-enzymes: part of the ancestral activity is retained.
5. **Synonym/name collision** — PEX2 (legacy synonym PAF1, "Peroxisome Assembly Factor 1") wrongly placed in the Cdc73/**Paf1** transcription complex. The grouping is an artifact of nomenclature, not homology.
6. **Paralog compartment/pathway conflation** — ALDH1L1 (cytosolic) annotated mitochondrion (that is ALDH1L2); HMGCS2 (mito ketogenesis) annotated mevalonate/FPP biosynthesis (that is cytosolic HMGCS1); AGK (mito acylglycerol kinase) annotated ceramide/sphingosine kinase + plasma membrane (that is CERK); EIF4E2/4EHP annotated as an eIF4F-complex member though it cannot bind eIF4G.

**Methodological note**: all examples above are drawn directly from existing per-gene reviews in `genes/*/*/*-ai-review.yaml` (the AI-curation decisions already in the repo), not re-derived here. Term IDs, actions, and the BCL2 WITH/FROM provenance were re-verified against the gene reviews and GOA tables before inclusion. There remain ~175 additional REMOVE-flagged IBA annotations not yet triaged into named patterns — these are candidates for a future pass (e.g., piRNA cross-aspect errors in PIWIL1, circadian photo-entrainment in human/CRY1 and human/CRY2, ankzf1 ERAD vs RQC).

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
