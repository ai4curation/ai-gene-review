# oprG (Q9HWW1, PA4067) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol, worklist rank 73)

No deep-research provider was available; these notes are my own reading of the UniProt record, the
PseudoCAP-cited paper (PMID:19486157, abstract only) and the two structural/functional papers listed in
UniProt (PMID:21124774 and PMID:26655471, both full text, cached with `just fetch-pmid`).

## Identity

- PAO1 PA4067, UniProtKB Q9HWW1 (unreviewed), 232 aa with a SignalP signal peptide (1-21).
- OmpW family (Pfam PF03922; InterPro IPR005618; TCDB 1.B.39.1.3; PANTHER PTHR36920:SF1). Eight-stranded
  beta-barrel (PDB 2X27 crystal; 2N6L/2N6P NMR).

## Literature

- Channel activity and regulation (seed paper): [PMID:19486157 "Planar bilayer studies indicated that
  purified OprG formed cationic-selective channels with a conductance of 500 pS in 1 M KCl"]; anaerobic,
  ANR-dependent expression [PMID:19486157 "OprG was highly transcribed in anaerobic environments rich in iron
  via the ANR regulator"]; no role in iron or antibiotic uptake [PMID:19486157 "contrary to previous
  reports, OprG did not appear to be involved in either iron or antibiotic uptake"]; cytotoxicity phenotype
  [PMID:19486157 "In the absence of OprG, P. aeruginosa was significantly less cytotoxic toward human
  bronchial epithelial cells."] (an indirect phenotype, not annotated).
- Structure: [PMID:21124774 "OprG forms an eight-stranded β-barrel with a hydrophobic channel that leads
  from the extracellular surface to a lateral opening in the barrel wall."]; the authors proposed transport
  of small hydrophobic molecules.
- Substrates: [PMID:26655471 "we reconstituted the purified protein into liposomes and found it to
  facilitate the transport of small amino acids such as glycine, alanine, valine, and serine, which was
  confirmed by Pseudomonas growth assays."]. The lateral-gate hypothesis was not supported [PMID:26655471
  "The interfacial prolines did not form a lateral gate in these structures"].

## Node PTN005107949

QuickGO (2026-10-28): 13 GO:0055085 IBA leaves. Most are OmpW proteins of Gram-negative bacteria (E. coli
P0A915, Salmonella Q8ZP50, Vibrio P17266, Shewanella Q8EGD1, Yersinia A0A3N4B4L4, Xanthomonas Q8P5Y7,
Q8P5Y8, Q8PD09, Bradyrhizobium Q89TR3, Q89UU8). Two leaves are eukaryotic genome entries (Medicago
truncatula A0A072TCN1, Nematostella vectensis A8DW24), which are probably bacterial contaminants or
transfers in those assemblies; an outer-membrane beta-barrel cannot do the same job in an animal or plant
cell, so those two IBAs are doubtful. For the bacterial OmpW family the generic, cautious term
"transmembrane transport" is appropriate: substrates differ between members and are poorly known.

## Annotation decisions

- GO:0055085 transmembrane transport (IDA PseudoCAP; IBA): MODIFY to the specific supported descendants,
  GO:0003333 amino acid transmembrane transport (liposome swelling + growth assays, PMID:26655471) and
  GO:0098655 monoatomic cation transmembrane transport (cation-selective channel, PMID:19486157). The node
  term itself is sound for the clade.
- GO:0016020 membrane (IBA, from E. coli OmpW): MODIFY to GO:0009279 cell outer membrane.
- GO:0019867 outer membrane (IEA): MODIFY to GO:0009279 cell outer membrane.
- GO:0044384 host outer membrane (IEA from IPR000758 Enterovir_OMP): REMOVE; OprG is in the bacterium's
  own outer membrane, and this InterPro2GO mapping is wrong for a bacterial protein.
- NEW GO:0015288 porin activity (IDA, PMID:19486157 and PMID:26655471): beta-barrel channel in the outer
  membrane passing small cations and small amino acids.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN005107949 | GO:0055085 transmembrane transport | 1 (sole) | 13 (10 taxa) | GO:0055085, IDA, PMID:19486157 (PseudoCAP) | SOUND | Purified OprG forms cation-selective channels in planar bilayers, direct evidence that it moves solutes across a membrane; later liposome-swelling and growth assays add small amino acids (PMID:26655471). The generic node term suits the OmpW family, whose substrates vary and are poorly known. Caveat: two leaves are eukaryotic genome entries (Medicago A0A072TCN1, Nematostella A8DW24), probably bacterial contaminants, for which the IBA is doubtful. |
