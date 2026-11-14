# ddlB (Escherichia coli K-12, P07862) notes

## Provenance

- Provider deep research (`just deep-research`) was **not** run for this gene; no
  `ddlB-deep-research-*.md` file exists. These notes summarise manual reading of
  the cached publications and the UniProt record. All cited papers are
  abstract-only in the cache except PMID:18304323 (full text).
- `just paint-losses ECOLI ddlB`: no IRD or IKR loss on the lineage.

## Literature summary

- ddlB is the classical ddl gene
  [PMID:1993184 "One of the two genes, designated as ddlB, is identical with the ddl gene already sequenced"].
  Overexpressed DdlB was purified and characterised kinetically
  [PMID:1993184 "Both DdlA and DdlB enzymes were purified to greater than 90% homogeneity and characterized kinetically."].
- Independent purification of the cloned ddl (= ddlB) product and inhibition by a
  phosphinate transition-state analogue
  [PMID:1554356 "The expressed enzyme was purified to homogeneity"];
  [PMID:1554356 "was found to be a classical slow-binding inhibitor of the E. coli ligase"].
- Mutant ST-640: temperature-sensitive ddl mutant lyses unless osmotically
  stabilised or given high D-alanine, makes less D-Ala-D-Ala and
  UDP-MurNAc-pentapeptide and accumulates UDP-MurNAc-tripeptide
  [PMID:4567144 "d-Alanyl-d-alanine and uridine diphosphate-N-acetyl-muramyl (UDP-MurNAc)-pentapeptide are synthesized in decreased amounts, accompanied by accumulation of UDP-MurNAc-tripeptide at 42 C but not at 30 C."];
  [PMID:4567144 "Combined genetic and enzymatic results show that the low ligase activity is due to a mutation in the ddl gene"].
- Active site: Y216/S150/E15 triad orients an omega-loop and D-Ala1; Y216F and
  S150A gain D-Ala-D-Lac depsipeptide ligase activity (VanA-like)
  [PMID:8756703 "Y216, S150, and E15 form a hydrogen-bonding triad that orients an omega-loop to close over the active site and also to orient substrate D-Ala1."].
- Oligomeric state: UniProt SUBUNIT says monomer
  [file:ECOLI/ddlB/ddlB-uniprot.txt "Monomer."], with no evidence tag, while GOA has an
  IDA homodimerization row from PMID:1993184 whose abstract does not describe the
  measurement; the abstract-only cache cannot show what the curator saw. Crystal
  structures split: RCSB entries 1IOV, 1IOW and 2DLN have one DdlB chain, 4C5B and
  4C5C have two (4C5A three), per the RCSB entry records (data.rcsb.org, checked
  2026-11-12). Multi-chain asymmetric units do not by themselves establish a native
  dimer. The row is kept as non-core, deferring to the EcoCyc curator who read the
  full text, with the conflict left as a suggested question and experiment.
- Localisation: cytosolic proteome [PMID:18304323 "We performed approximately 200 individual LC-MS/MS runs of the E. coli MC4100 cytosol"].

## Curation decisions

- Core: D-alanine-D-alanine ligase activity; peptidoglycan biosynthetic process;
  cytosol.
- cytoplasm IEA: MODIFY to cytosol; metal ion binding IEA: MODIFY to magnesium
  ion binding; ATP binding IEA: KEEP_AS_NON_CORE.
- protein homodimerization IDA: KEEP_AS_NON_CORE, deferring to the EcoCyc curator
  (abstract-only source; conflicts with UniProt "Monomer"; structures split; see
  suggested question).
