# APRA (aprA / PA1249) — Pseudomonas aeruginosa alkaline metalloprotease (Serralysin)

UniProt: Q03023 (APRA_PSEAE); EC 3.4.24.40; MEROPS M10.056; peptidase M10B
(serralysin) family. 479 aa precursor (propeptide 1–9, mature chain 10–479).

## Summary

AprA is a secreted, zinc-dependent alkaline metalloendopeptidase of the
serralysin (RTX-type metalloprotease, peptidase M10B) family. It is a major
extracellular virulence factor of *P. aeruginosa*. Structurally it is a
two-domain protein: an N-terminal catalytic metallopeptidase domain (HEXXH zinc
motif) and a C-terminal β-roll domain formed by hemolysin-type (RTX)
calcium-binding repeats that bind multiple Ca²⁺ ions. It has no cleavable
N-terminal signal peptide and is exported by a dedicated type I secretion system
(the AprDEF ABC-transporter / RTX exporter encoded in the same operon), with a
C-terminal secretion signal. It is co-secreted with, and held in check by, the
periplasmic/secreted inhibitor AprI.

Catalytically it preferentially cleaves peptide bonds N-terminal to (in P1' of)
hydrophobic residues. Biologically it acts on a broad range of host substrates,
and its best-characterized roles are in innate-immune evasion and modulation of
host epithelial physiology.

## Structure / cofactors (from UniProt Q03023 + crystallography)

- Catalytic Zn²⁺: coordinated by His185, His189, His195; catalytic Glu186
  (active site His-Glu-X-X-His … His "zincin/metzincin" motif). [UniProt Q03023
  FT ACT_SITE 186; BINDING 185/189/195 Zn] [PMID:8253063 EMBO J 1993, crystal
  structure: "two-domain protein with a calcium binding parallel beta roll motif"]
- Binds 8 Ca²⁺ per subunit and 1 Zn²⁺ per subunit. [UniProt Q03023 COFACTOR]
- C-terminal β-roll formed by hemolysin-type (RTX) Ca-binding repeats (FT REPEAT
  341–354, 355–367, 368–385; PROSITE PS00330 HEMOLYSIN_CALCIUM). The Ca²⁺-loaded
  β-roll is also the structural element required for type I secretion/folding.
- Cognate inhibitor complex solved: AprA + AprI ("inhibition by a zinc-NH2
  coordinative bond"). [PMID:11445573]
- Subcellular location: Secreted. [UniProt Q03023]

## Catalytic activity / specificity

- EC 3.4.24.40; "Preferential cleavage of bonds with hydrophobic residues in P1'."
  [UniProt Q03023 CATALYTIC ACTIVITY; ECO:0000269|PubMed:4199986]
- Specificity established with synthetic peptides. [PMID:4199986 Morihara 1973]

## Biological roles / host substrates (virulence)

### 1. Innate-immune evasion via degradation of monomeric flagellin (TLR5/FLS2)
- AprA degrades free **monomeric flagellin** (the TLR5/FLS2 ligand) but not
  polymeric flagellin in the flagellum, so the bacterium evades pattern-recognition
  receptor detection while keeping motility.
  [PMID:21901099 Bardoel 2011, "AprA effectively degrades the TLR5 ligand
  monomeric flagellin, while polymeric flagellin (involved in bacterial motility)
  and TLR5 itself resist degradation"]
  ["by degrading the ligand for TLR5 and FLS2, P. aeruginosa escapes recognition
  by the innate immune systems of both mammals and plants"]
- `aprA` mutants give >100-fold enhanced TLR5 activation. [PMID:21901099]
- This is the strongest experimental basis for the GO term
  GO:0141141 "symbiont-mediated evasion of recognition by host pattern recognition
  receptor". (Note: the GOA EXP annotation for GO:0141141 currently cites the
  *complement* paper PMID:22131330; the flagellin paper PMID:21901099 is the more
  apt primary reference. Complement lectin-pathway initiators (MBL/ficolins) are
  also soluble PRRs, so the term is still defensible for the gene.)

### 2. Inhibition of complement (classical + lectin pathways) via C2 cleavage
- AprA degrades human C1s and C2; complement inhibition mechanism is **cleavage of
  C2**; blocks C3b deposition via the classical and lectin (not alternative)
  pathways; blocks neutrophil phagocytosis/killing and C5a formation.
  [PMID:22131330 Laarman 2012, "AprA specifically blocked C3b deposition via the
  classical and lectin pathways, whereas the alternative pathway was not affected";
  "the mechanism of action for complement inhibition is cleavage of C2"]
- Basis for GO:0045959 (neg. reg. complement, classical) and GO:0001869 (neg. reg.
  complement, lectin), both IDA.

### 3. Activation of the epithelial sodium channel (ENaC)
- Purified AP proteolytically activates ENaC by cleaving the **γ-subunit**,
  increasing basal Na⁺ current in human bronchial epithelia (CF and non-CF);
  proposed to reduce airway-surface-liquid volume / mucociliary clearance in CF.
  [PMID:22859302 Butterworth 2012, "This activation was mapped to the γ-subunit of
  ENaC"; "an increase in basal ENaC current and a loss of trypsin-inducible ENaC
  current, consistent with sustained activation of ENaC"]
- Basis for GO:0010765 (positive regulation of sodium ion transport, IDA) and a
  second experimental confirmation of peptidase activity (GO:0008233, IDA).

## GO annotation review orientation

Core function:
- **Molecular function:** zinc metalloendopeptidase activity (GO:0004222), with
  catalytic Zn²⁺ binding (GO:0008270) and structural Ca²⁺ binding (GO:0005509).
- **Cellular component:** secreted / extracellular region (GO:0005576;
  GO:0005615 extracellular space is the more precise term).
- **Biological process:** proteolysis (GO:0006508), executed on host substrates
  to drive virulence (immune evasion; host ion-transport modulation = non-core,
  pleiotropic downstream consequences).

Likely over-/under-annotations to flag:
- GO:0008233 (peptidase) and GO:0008237 (metallopeptidase) IEA are correct but are
  high-level parents of the more informative GO:0004222 metalloendopeptidase
  activity → general/redundant.
- GO:0031012 "extracellular matrix" (located_in, IEA from InterPro) is a likely
  over-annotation — AprA is freely secreted into the extracellular space, not a
  structural ECM component. Prefer GO:0005576 / GO:0005615.

## Additional findings (from falcon/Edison deep research, APRA-deep-research-falcon.md)

Broader experimentally/review-supported substrate range and roles (not all yet GO-annotated):
- Complement: primary substrate is **C2** (cleaved into C2a/C2b, ~200 nM, blocks
  C4b2a convertase); also degrades **C1q, C1s, C3, C5a**. "AprA was identified as
  the first bacterial protease demonstrated to cleave C2."
- Cytokines: degrades **IFN-γ** and **TNF-α**, dampening inflammatory signaling.
- Disrupts **neutrophil extracellular traps (NETs)**.
- **Corneal infection**: degrades **fibrin**, causes tissue necrosis, increases
  bacterial attachment to corneal epithelium.
- **Polymicrobial biofilm**: cleaves *S. aureus* surface protein **SasG** (removes
  A domain, exposes B domain → MRSA aggregation, biofilm, antibiotic tolerance)
  [keim2024, bioRxiv preprint — treat as provisional].
- **Virulence in vivo**: *aprA* deletion raised murine survival to 77% vs 33% for
  WT PAO1 (cutaneous infection), with no change in bacterial counts [pletzer2020].
- Secretion: **type I secretion system** encoded by the *aprDEF* operon (AprD ABC
  transporter, AprE membrane-fusion protein, AprF outer-membrane factor); secreted
  with propeptide intact; folding/activation is Ca²⁺-dependent (RTX β-roll).
- Regulation: Las/Rhl quorum sensing and the ppGpp stringent response.
- Conservation: *apr* gene present in ~99% of clinical *P. aeruginosa* isolates;
  proposed anti-virulence drug target.

Note: the falcon report mis-attributes the flagellin/TLR5 finding to Laarman 2012;
the correct primary source is Bardoel 2011 (PMID:21901099).

## References
- UniProt Q03023 (APRA_PSEAE)
- PMID:4199986 — substrate specificity (synthetic peptides), EC 3.4.24.40
- PMID:8253063 — crystal structure, two-domain + Ca β-roll
- PMID:11445573 — AprA–AprI inhibitor complex structure
- PMID:21901099 — flagellin/TLR5/FLS2 immune evasion (Bardoel 2011)
- PMID:22131330 — complement classical/lectin inhibition via C2 cleavage (Laarman 2012)
- PMID:22859302 — ENaC γ-subunit activation (Butterworth 2012)
