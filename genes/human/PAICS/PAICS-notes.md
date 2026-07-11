# PAICS (P22234, PUR6_HUMAN) review notes

Bifunctional enzyme of de novo purine synthesis (DNPS). Catalyzes two consecutive
steps of the pathway:

1. **AIR carboxylase (AIRC; EC 4.1.1.21; GO:0004638)** — carboxylates AIR
   (5-aminoimidazole ribonucleotide) to CAIR (4-carboxy-AIR / 5-amino-1-(5-phospho-
   D-ribosyl)imidazole-4-carboxylate) using CO2/bicarbonate. In vertebrates this is
   a class II PurE that uses CO2 directly (unlike the bacterial two-enzyme
   N5-CAIR route). RHEA:10792.
2. **SAICAR synthetase (SAICARS; EC 6.3.2.6; GO:0004639)** — ATP-dependent condensation
   of CAIR with L-aspartate to form SAICAR (which ADSL subsequently cleaves to AICAR).
   RHEA:22628.

## Domain architecture (UniProt P22234)
- SAICAR synthetase domain: residues 2-260 (N-terminal)
- Linker: 261-266
- AIR carboxylase domain: 267-425 (C-terminal)
- CO2-binding: residue 332; catalytic residues His-303, Ser-332, Gly-334 (MUTAGEN → loss of AIRC activity)
- Homooctamer [PMID:17224163]: octameric carboxylase core + four peripheral synthetase dimers;
  substrate-channeling tunnels connect AIRC and SAICARS active sites.

## Localization
- Cytosolic [IBA GO:0005829; Reactome TAS]. Component of the purinosome, a
  reversible cytoplasmic multi-enzyme DNPS assembly.

## Key experimental evidence
- PMID:17224163 (J Mol Biol 2007): crystal structure (PDB 2H31), FUNCTION, CATALYTIC
  ACTIVITY (both EC 4.1.1.21 and 6.3.2.6), SUBUNIT (homooctamer), mutagenesis of AIRC
  active-site residues. UniProt uses this as ECO:0000269 for both catalytic activities.
  (abstract-only in cache; UniProt curator read full text.)
- PMID:31600779 (Hum Mol Genet 2019): PAICS deficiency (PAICSD, MIM:619859), autosomal
  recessive, p.Lys53Arg reduces both activities; prevents purinosome formation; multiple
  congenital anomalies + fatal neonatal outcome. FUNCTION, CATALYTIC ACTIVITY, PATHWAY.
- PMID:27590927 (Mol Genet Metab 2016): CRISPR-Cas9 KO of DNPS enzymes in HeLa →
  substrate accumulation + reduced purinosome assembly. MGI made IDA/IMP annotations for
  both MFs and de novo IMP/AMP/XMP/GMP BP terms from this.
- PMID:2253271 (Curr Genet 1990): cloned human cDNA (ADE2) complementing yeast ade1+ade2;
  established both SAICARS (5' half) and AIRC (3' half) activities. TAS.

## Over-annotations identified
- **cadherin binding (GO:0045296, HDA, PMID:25468996)**: BioID proximity-biotinylation of
  the E-cadherin cytoplasmic tail; PAICS is one of 612 vicinal proteins, not a genuine
  cadherin-binding function. Over-annotation.
- **extracellular exosome (GO:0070062) x2 (PMID:23533145, PMID:20458337)** and **membrane
  (GO:0016020, PMID:19946888)**: HDA from shotgun proteomics of exosomes / NK-cell membrane
  fractions; PAICS is an abundant cytosolic enzyme routinely detected as a
  co-purifying/contaminant species. Over-annotations (not the enzyme's site of action).
- **protein binding (GO:0005515, IPI x7)** and **identical protein binding (GO:0042802,
  IPI x5)**: high-throughput Y2H/AP-MS interactome hits (Stelzl, Rual, Rolland, Huttlin,
  etc.). GO:0042802 identical-protein-binding is corroborated by the homooctamer
  (PMID:17224163) so is biologically real but non-core (self-association). Bare protein
  binding is uninformative — MARK_AS_OVER_ANNOTATED per policy (do not REMOVE IPIs).

## Core functions (for core_functions block)
- MF GO:0004638 (AIRC) + MF GO:0004639 (SAICARS)
- BP GO:0006189 'de novo' IMP biosynthetic process (directly_involved_in);
  GO:0006164 purine nucleotide biosynthetic process (broader)
- CC GO:0005829 cytosol
</content>
</invoke>
