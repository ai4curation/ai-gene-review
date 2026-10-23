# mlaD (P64604, Escherichia coli K-12) - curation notes

## Deep research
- 2026-10-23: `just deep-research ECOLI mlaD --provider perplexity` was attempted once and failed
  ("Provider 'perplexity' not available. Available: falcon, openscientist"). No deep-research file
  was generated; this review is built directly from cached full-text publications and the UniProt record.

## Identity and topology
- 183-residue single-pass (signal-anchor type II) inner-membrane protein: TM 8-28, periplasmic MCE/MlaD
  domain (39-116), disordered C-terminal tail [file:ECOLI/mlaD/mlaD-uniprot.txt]. MlaD family
  (Pfam PF02470; NCBIfam TIGR04430 OM_asym_MlaD; InterPro IPR030970 ABC_MlaD).

## Hexameric MCE ring and lipid binding
- [PMID:27529189 "Within this complex, MlaD forms an SDS-resistant hexamer via its soluble domain, and we
  demonstrate that this domain binds PLs."]; "hexameric sMlaD is a PL-binding complex with at least four
  binding sites"; preference for PG over PE.
- [PMID:28388411 "MlaD, PqiB, and YebT each bound phospholipid species that co-migrated with
  phosphatidylglycerol (PG), cardiolipin (CL) and phosphatidylethanolamine (PE) standards."]
- Crystal/EM structure: hexameric ring with central hydrophobic pore; pore-lining (beta5-beta6 loop)
  mutants fail to complement deltamlaD [PMID:28388411].
- In the MlaFEDB cryo-EM structure, a phospholipid acyl chain inserts into a constriction in the MlaD pore
  formed by Leu106/Leu107; pathway continuous from MlaE pocket through MlaD [PMID:33236984].

## Complex and partners
- MlaFEDB stable complex; MlaD reduces ATP hydrolysis ~3-fold and modulates coupling [PMID:27529189].
- MlaD binds MlaC directly [PMID:28388411 "a direct interaction between MlaC and MlaD"].
- MlaC spontaneously transfers PLs to MlaFEDB "in an MlaD-dependent manner" [PMID:34873038]; MlaD
  important for productive coupling of ATP hydrolysis to retrograde PL transfer.
- MlaD requires its native TM helix to assemble with MlaFEB and function [PMID:33236984].

## Curation decisions (summary)
- GO:0005515 protein binding x2 (MlaC; MlaE): REMOVE per protein-binding policy (no better MF term for
  MlaC docking; complex membership captured by GO:0043190).
- GO:0005543 phospholipid binding IDA: ACCEPT (core).
- GO:0015914 phospholipid transport (IEA, NAS): MODIFY -> GO:0120010.
- GO:0016020 membrane NAS: MODIFY -> GO:0005886.
- GO:1990531 (P-type flippase complex): MODIFY -> GO:0043190.
- GO:0120014 enables (IBA, IDA): ACCEPT; core records contributes_to since activity requires whole complex
  (plus MlaC).
