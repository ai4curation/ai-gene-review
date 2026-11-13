# infC (IF3, P0A707) — Escherichia coli K-12 notes

## Identity

- UniProt P0A707 (IF3_ECOLI), 180 aa, b1718. Two domains (IF3_N PF05198, IF3_C PF00707)
  joined by a flexible linker; HAMAP MF_00080; NCBIfam TIGR00168
  [file:ECOLI/infC/infC-uniprot.txt "Belongs to the IF-3 family"].
- infC uses the non-canonical AUU start codon, which limits its own expression; the
  older "autogenous mRNA binding" model was replaced by a kinetic start-codon
  discrimination explanation [file:ECOLI/infC/infC-uniprot.txt "Uses the non-canonical initiation codon AUU, which limits its expression"].
- PANTHER PTHR10938, subfamily SF0 named "TRANSLATION INITIATION FACTOR IF-3,
  MITOCHONDRIAL"; the family also contains plant chloroplast IF3 (PAINT IBD
  PTN000859419 chloroplast, AT2G24060/AT4G30690). There is no universal
  archaeal/cytosolic-eukaryotic IF3 ortholog; eukaryotes retain IF3 in mitochondria
  (MTIF3) and plastids. eIF1 is a functional, not homologous, analog in start-codon
  selection.

## Function (literature)

- Shifts 70S <-> 50S + 30S equilibrium towards free subunits (anti-association)
  [file:ECOLI/infC/infC-uniprot.txt "IF-3 binds to the 30S ribosomal subunit and shifts the equilibrium between 70S ribosomes and their 50S and 30S subunits in favor of the free subunits"].
- Footprinting: protects G700, G703, G791 near the 50S-protected bases
  [PMID:7739034 "Initiation factor 3 (IF-3) protects residues G700, G703 and G791 from attack by kethoxal"].
- Directed probing: C domain at the platform interface, coincides with H69 of 23S rRNA
  (explains anti-association); N domain at the E site
  [PMID:11684020 "The C domain coincides with the location of helix 69 of 23S rRNA, explaining the ability of IF3 to block subunit association"].
- Y107/K110 mutations reduce 30S affinity and impair fMet-tRNA selection
  [PMID:1457399 "tyrosine 107 and lysine 110 are critical components of the ribosome binding domain of IF3"].
- Start-codon discrimination in vivo: IF3 mutants raise initiation at class II codons
  3-5-fold [PMID:8858589 "IF3 is generally able to discriminate between efficient and inefficient codons in vivo"].
- Uniform destabilization of tRNA binding to the 30S underpins initiator selection
  [PMID:16857585 "uniform destabilization of the binding of all tRNAs to the 30S subunit by IF3"].
- Recycling: RRF + EF-G transiently split 70S; IF3 binds the 30S and prevents
  re-association [PMID:16043510 "IF3 stabilizes the dissociation by binding to the transiently formed 30S subunits, preventing re-association back to 70S ribosomes"];
  IF3 facilitates RRF-mediated processing of stalled ribosomes in vivo
  [PMID:18565340 "IF3 facilitates the RRF-mediated processing of the stalled ribosomes"].
  IF3 stabilizes rather than catalyses the split, so ribosome disassembly is non-core.
- Cold shock: IF3 is the main trans-acting source of selective cold-shock mRNA
  translation [PMID:14730025 "The most important sources of cold-shock translational bias is IF3"].
  Non-core (conditional, regulatory consequence of its initiation role).

## GOA rows — reasoning summary

- GO:0003743 (IBA, IDA PMID:4922687, IEA), GO:0006413 (IBA, IEA), GO:0005829 cytosol
  (IDA, IBA): ACCEPT.
- GO:0005737 cytoplasm (EXP PMID:330233, IEA): MODIFY to cytosol (correct but general).
- GO:0043022 ribosome binding (IDA PMID:11684020, IEA ARBA): MODIFY to GO:0043024.
- GO:0032790 ribosome disassembly (IMP PMID:18565340, IEA ARBA): KEEP_AS_NON_CORE.
- GO:0009409 response to cold (IDA PMID:14730025): KEEP_AS_NON_CORE.
- GO:0016020 membrane (HDA PMID:16858726, BN-PAGE complexome, abstract only):
  MARK_AS_OVER_ANNOTATED — soluble factor, no TM; membrane-fraction detection most
  plausibly reflects ribosome co-fractionation.
- GO:0005515 protein binding x2 (IPI with S7/rpsG): REMOVE per policy.
- NEW GO:1990145 maintenance of translational fidelity (IMP, PMID:8858589). Comparator:
  yeast eIF1 (SUI1, P32911), the eukaryotic start-codon fidelity factor, carries
  GO:1990145 by IMP (QuickGO query, 2026-11-13). IF3 itself performs the
  discrimination (destabilizes non-initiator / non-canonical start-codon complexes).

`just paint-losses ECOLI infC`: no IRD/IKR loss on this lineage.
