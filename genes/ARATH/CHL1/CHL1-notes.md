# CHL1 (At5g40090) - Disease Resistance Protein / CHS1-Like 1

## Identity

- **UniProt**: Q9LUJ8
- **Gene**: CHL1 (CHILLING SENSITIVE 1-LIKE 1, CHS1-LIKE 1)
- **Locus**: At5g40090
- **Organism**: Arabidopsis thaliana
- **Protein**: Disease resistance protein CHL1 (459 aa, 51.6 kDa)
- **Domain architecture**: TIR -- NB-ARC (truncated NLR, lacks LRR domain)

**CRITICAL NOTE**: The gene symbol "CHL1" in Arabidopsis is ambiguous. The more
commonly studied CHL1 is At1g12110 (Q05085/NPF6.3/NRT1.1), a nitrate transporter
also known as CHLORINA 1. The CHL1 under review here (Q9LUJ8, At5g40090) is a
disease resistance protein named CHS1-LIKE 1. The existing GOA and UniProt files
in this directory were fetched for the wrong protein (Q05085). The BioReason
prediction file correctly targets Q9LUJ8.

## Domain Architecture

- **TIR domain** (residues 16-170): Toll/interleukin-1 receptor homology domain.
  In plant NLRs, TIR domains have NADase enzymatic activity -- they cleave NAD+
  to produce signaling molecules (pRib-AMP, di-ADPR, etc.) that activate the
  EDS1-PAD4-ADR1 signaling node [PMID:34497423, "The EDS1-PAD4-ADR1 node
  mediates Arabidopsis pattern-triggered immunity"].

- **NB-ARC domain** (residues 191-401): Nucleotide-binding adaptor shared by
  APAF-1, R proteins, and CED-4. This is an AAA+ ATPase that acts as a molecular
  switch: ATP-bound = active, ADP-bound = inactive.

- **No LRR domain**: CHL1 is a "truncated NLR" or TIR-NBS (TN) protein. It lacks
  the C-terminal leucine-rich repeat domain found in canonical TNL immune receptors.
  This places it in a special class of atypical NLR proteins whose functions are
  still being elucidated.

## Functional Summary

CHL1 is a truncated TIR-NBS immune receptor that limits chloroplast damage and
cell death at low temperatures. Its paralog CHS1 (At1g17610) was identified through
a chilling-sensitive mutant screen. CHL1 overexpression alleviates chilling damage
and enhances plant growth at both moderate and cold temperatures
[PMID:23617639, "Over-expression of CHS1 or CHL1 alleviates chilling damage and
enhances plant growth at moderate (24C) and chilling (13C) temperatures"].

## Key Literature

### PMID:23617639 - Zbierzak et al. 2013, Plant Journal
"A TIR-NBS protein encoded by Arabidopsis Chilling Sensitive 1 (CHS1) limits
chloroplast damage and cell death at low temperature"

Key findings:
- CHS1 (At1g17610) encodes a TIR-NBS protein; CHL1 (At5g40090) is its paralog
- The chs1-1 mutation causes chilling sensitivity with activated defense responses
  and salicylic acid production at 13C
- Overexpression of CHS1 or CHL1 alleviates chilling damage
- Chilling sensitivity depends on EDS1 and PAD4 regulators
- Photosynthetic complex changes and thylakoid membrane damage precede cell death
- The mutant showed excessive necrotic response to bacterial infection

### PMID:23651299 - Wang et al. 2013, Plant Journal
"A missense mutation in CHS1, a TIR-NB protein, induces chilling sensitivity in
Arabidopsis"

Key findings:
- Independent identification of CHS1 as a TIR-NB protein
- CHS1 protein stability is positively regulated by low temperature
- The chs1 mutant displays both chilling-sensitive and defense-associated phenotypes
- Defense phenotypes include extensive cell death, H2O2 and SA accumulation, PR gene
  expression

### PMID:27699788 - Zhang et al. 2017, New Phytologist
"Temperature-dependent autoimmunity mediated by chs1 requires its neighboring TNL
gene SOC3"

Key findings:
- CHS1 interacts with the NB and LRR domains of neighboring TNL gene SOC3
- Mutant chs1 gains additional interaction with the TIR domain of SOC3
- Loss of SOC3 completely suppresses the chilling-sensitive phenotype of chs1-2
- This establishes a paired immune receptor mechanism: TN protein (CHS1) working
  with neighboring TNL (SOC3) to control temperature-dependent immunity

## Molecular Mechanism

CHL1/CHS1-type TIR-NBS proteins function as adaptors or regulators within the
plant immune system. They pair with full-length TNL receptors (like SOC3 pairs with
CHS1) to form functional immune receptor complexes. This is analogous to other
documented truncated NLR functions:

- TN10 pairs with clustered TNL receptors [PMC8069298]
- TN13 associates with CC-NBS-LRR receptor RPS5 [PMID:33982335]
- TIR-NBS2 is required for activated defense in exo70B1 mutant [PMID:25617755]

The TIR domain in these proteins has NADase activity that generates small molecule
signals (pRib-AMP/ADP, di-ADPR) which bind to and activate EDS1-PAD4 heterodimers,
recruiting helper NLRs like ADR1 to execute immune responses.

## GO Annotation Status

The actual GOA annotations for Q9LUJ8 (from QuickGO) are:
- GO:0043531 ADP binding (IEA, InterPro:IPR002182)
- GO:0061809 NAD+ nucleosidase activity, cyclic ADP-ribose generating (IEA, EC:3.2.2.6)
- GO:0006952 defense response (IEA, InterPro:IPR044974)
- GO:0007165 signal transduction (IEA, InterPro:IPR000157)
- GO:0005737 cytoplasm (IEA, UniProt-SubCell)
- GO:0009507 chloroplast (ISM, TAIR)

## BioReason Prediction Assessment

The BioReason SFT prediction for Q9LUJ8 is domain-architecture-driven and generally
sound in recognizing the TIR-NB-ARC architecture. However:

1. **Mitochondrial localization (GO:0005739)**: BioReason claims mitochondrial
   localization. This is INCORRECT. UniProt annotates CHL1 to the cytoplasm, and
   TAIR predicts chloroplast. There is no evidence for mitochondrial localization.
   The reasoning that "Apaf-like assemblies often interface with mitochondrial
   signaling hubs" conflates animal apoptosome biology with plant NLR biology.

2. **Defense response to fungus (GO:0050832) and bacterium (GO:0042742)**: These
   are plausible but SPECULATIVE for CHL1 specifically. The documented function is
   in cold stress response. The chs1 mutant showed altered bacterial response
   (excessive necrosis), but CHL1 itself has not been shown to directly mediate
   pathogen defense.

3. **Positive regulation of cell death (GO:0010942)**: Partially supported. The
   chs1 mutant (gain-of-function) activates cell death, but the wild-type CHS1/CHL1
   actually LIMITS cell death. So this is backwards.

4. **Protein binding (GO:0005515)**: Too generic. The actual molecular function is
   NAD+ nucleosidase activity (GO:0061809) based on TIR domain enzymatic function.
   BioReason missed this key enzymatic activity entirely.

5. **No GO term predictions listed**: The BioReason file has empty GO term prediction
   sections, suggesting the model did not generate specific GO predictions beyond the
   narrative.
