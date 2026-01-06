# UBP3 GO Annotation Curation Analysis

## Gene Overview
**UBP3** (Ubiquitin carboxyl-terminal hydrolase 3) is a deubiquitinating enzyme (EC 3.4.19.12) critical for protein quality control, selective autophagy, and transcriptional regulation in yeast. UBP3 acts as a cysteine-type serine/threonine protease that cleaves ubiquitin from target proteins in a cofactor-dependent manner (primarily with BRE5).

## Key Functional Domains
- **Catalytic domain (C19 family)**: residues 460-911, containing the characteristic USP (ubiquitin-specific protease) domain
- **Active site residues**: Cys469 (nucleophile) and His861 (proton acceptor)
- **Bre5-binding domain**: N-terminal region critical for cofactor recognition and substrate specificity

## Curation Strategy

Based on analysis of UniProt annotations, published literature, and the IBA/IMP/IDA evidence hierarchy:

1. **Molecular Function (MF)**: Accept cysteine-type deubiquitinase catalytic terms; remove generic protein binding terms
2. **Biological Process (BP)**: Accept substrate-specific deubiquitination pathways (ribophagy, H2B/Sec23 deubiquitination, transcriptional regulation); be critical of overly general terms
3. **Cellular Component (CC)**: Accept compartment localization with strong evidence (nucleus, cytosol, mitochondrion, cytoplasm)
4. **Evidence codes**: IBA (phylogenetic) and IMP/IDA (experimental) carry highest weight; IEA acceptable for catalytic domain-based inferences

## Annotation Categories

### Core Functions (ACCEPT)
1. **GO:0004843** - cysteine-type deubiquitinase activity (MF)
   - Multiple strong evidence sources (IDA, IBA, IMP, IEA)
   - Direct catalytic activity demonstrated biochemically
   - Essential for substrate recognition and processing

2. **GO:0016579** - protein deubiquitination (BP)
   - Multiple evidence types (IDA, IMP, IBA)
   - Broad process encompassing multiple substrate-specific pathways
   - Well-supported by biochemical literature

3. **GO:0034517** - ribophagy (BP)
   - Strong experimental evidence (IMP, NAS)
   - Selective autophagy of ribosomes requires Ubp3 catalytic activity
   - Functionally important phenotype in starvation response

### Substrate-Specific Functions (ACCEPT/MODIFY)
- SEC23 deubiquitination → part of COPII/ER-Golgi transport regulation
- H2B K123 deubiquitination → expected but not explicitly in current annotations
- Ribosomal protein deubiquitination → part of ribophagy
- MAPK signaling regulation (Ste7) → context-dependent

### Localization Terms (ACCEPT with caution)
- **Nucleus** (GO:0005634): IBA evidence; some deubiquitination activity in nucleus
- **Cytosol** (GO:0005829): IBA and IDA evidence; major catalytic compartment
- **Cytoplasm** (GO:0005737): IDA evidence; broader than cytosol, appropriate
- **Mitochondrion** (GO:0005739): IDA evidence; Ubp3-Bre5 translocates to mitochondria during mitophagy

### Problematic Annotations (REMOVE or MODIFY)
1. **GO:0005515** - protein binding (all 8 instances)
   - Generic, uninformative term
   - Identified from interaction databases (IntAct) via IPI evidence
   - Should be replaced with specific binding terms or removed entirely
   - Catalytic activity is primary function, not passive binding

2. **GO:0003729** - mRNA binding (HDA and IDA)
   - Limited evidence (proteome-wide survey, not mechanistic)
   - HDA (high-throughput direct assay) less informative than functional data
   - May reflect co-localization with RNA rather than functional binding
   - Consider MARK_AS_OVER_ANNOTATED

3. **GO:0031647** - regulation of protein stability (IBA)
   - Consequence of deubiquitination, not direct function
   - Indirect effect through removal of degradation signals
   - Too broad; the specific substrate pathways are more informative

4. **GO:0006508** - proteolysis (IEA)
   - Overly general; applies to all proteases
   - Deubiquitination is more specific than general proteolysis
   - Not strongly supported by evidence

## Annotation Actions Summary

Total Annotations: 54

| Category | Count | Action |
|----------|-------|--------|
| Cysteine-type deubiquitinase activity | 4 | ACCEPT |
| Protein deubiquitination | 6 | ACCEPT |
| Ribophagy | 3 | ACCEPT |
| Localization (nucleus, cytosol, cytoplasm, mitochondrion) | 7 | ACCEPT |
| Ubp3-Bre5 complex | 1 | ACCEPT |
| Protein binding | 8 | REMOVE |
| mRNA binding | 2 | MARK_AS_OVER_ANNOTATED |
| Protein stability regulation | 1 | REMOVE |
| Stress granule assembly | 1 | ACCEPT |
| ER-Golgi transport regulation | 2 | ACCEPT |
| Golgi protein retention | 5 | ACCEPT |
| Mitophagy regulation | 1 | KEEP_AS_NON_CORE |
| Osmotic stress response | 2 | ACCEPT |
| Peptidase/hydrolase terms | 4 | MODIFY |

## Key Literature Evidence

1. **Catalytic Activity (Baker et al. 1992, PMID:1429680)**
   - First demonstration of Ubp3 deubiquitinating activity
   - Activity on ubiquitin fusions in vivo
   - Substrate specificity unclear in early work

2. **Sec23/COPII Specificity (Cohen et al. 2003, PMID:12778054)**
   - Bre5 cofactor required for substrate specificity
   - Sec23 mono-ubiquitination prevents degradation
   - Connection to ER-Golgi transport pathway

3. **Ribophagy (Kraft et al. 2008, PMID:18391941)**
   - Novel selective autophagy pathway
   - Ubp3 catalytic activity essential
   - Ribosomal protein ubiquitination is direct target

4. **Stress Granule Assembly (Nostramo et al. 2016, PMID:26503781)**
   - Ubp3 catalytic activity required for assembly
   - Stress granule formation correlates with cell survival
   - Bre5 interaction essential

5. **Mitophagy Regulation (Müller et al. 2015, PMID:25704822)**
   - Ubp3-Bre5 complex negatively regulates mitophagy
   - But promotes other autophagy pathways (ribophagy)
   - Selective pathway regulation

## Proposed New Annotations

Based on literature not currently captured:

1. **GO:0016045** - detection of mechanical stimulus (if histone modification involved in mechanotransduction)
2. **GO:0031398** - positive regulation of protein ubiquitination (indirect effect of Ubp3 activity on pathway balance)
3. **GO:0006325** - chromatin organization (if H2B K123 deubiquitination is annotated)

Note: These would require specific substrate evidence documentation.

## Recommendations

### Priority 1: Immediate Changes
- REMOVE: All GO:0005515 (protein binding) annotations (8 total)
- MODIFY: GO:0031647 to more specific substrate pathways or REMOVE
- MODIFY: GO:0006508 (proteolysis) - too general for a specific deubiquitinase

### Priority 2: Review Evidence Quality
- Evaluate HDA evidence for mRNA binding (GO:0003729)
- Confirm IPI evidence specificity for cofactor interactions

### Priority 3: Core Annotations (ACCEPT)
- GO:0004843 (deubiquitinase activity) - multiple evidence types
- GO:0016579 (protein deubiquitination) - well-supported
- GO:0034517 (ribophagy) - functionally important
- GO:0060628 (ER-Golgi transport) - SEC23 substrate specificity
- GO:0047484 (osmotic stress response) - Hog1 MAPK interaction

## Evidence Quality Assessment

**Highest Quality Evidence:**
- IDA from primary research (Baker 1992, Cohen 2003, Kraft 2008)
- IMP from targeted genetic studies (ribophagy, stress granules)
- IBA from ortholog-based inference (appropriate for conserved function)

**Lower Quality Evidence:**
- IEA from keyword mapping (too general)
- HDA from proteome-wide surveys (co-localization not functional evidence)
- IPI from binary interaction networks (does not indicate substrate specificity)

## Core Function Summary

UBP3 is fundamentally a **cysteine-type deubiquitinase** that:
1. Cleaves ubiquitin from specific protein substrates in a cofactor-dependent manner
2. Regulates protein stability of key COPII/secretory pathway components (SEC23)
3. Catalyzes selective autophagy of ribosomes during starvation (ribophagy)
4. Maintains stress granule formation during nutrient stress
5. Modulates MAPK signaling through Ste7 deubiquitination
6. Negatively regulates mitophagy while promoting other autophagy pathways

Secondary functions involve compartmentalization (nucleus, cytosol, mitochondrion involvement), but the primary molecular function is ubiquitin C-terminal hydrolysis.
