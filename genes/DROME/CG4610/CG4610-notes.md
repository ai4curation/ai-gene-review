# CG4610 (Q9W245) review notes

## Identity
- CG4610 is the Drosophila ortholog of human MTO1 / yeast MTO1 / bacterial MnmG (GidA)
  [file:DROME/CG4610/CG4610-uniprot.txt "Belongs to the MnmG family"]; PANTHER
  PTHR11806:SF0 "PROTEIN MTO1 HOMOLOG, MITOCHONDRIAL".
- FAD cofactor predicted [file:DROME/CG4610/CG4610-uniprot.txt "Name=FAD"].
- UniProt entry is unreviewed (TrEMBL) with no subcellular-location comment; mitochondrial
  location rests on orthology (IBA/ISS).

## Literature
- No Drosophila experimental study of CG4610 is in GOA. Annotations are IBA, IEA and ISS
  (from human MTO1 Q9Y2Z2 and yeast MTO1).
- In the MnmEG / GTPBP3-MTO1 system, MnmG/MTO1 is the FAD-dependent subunit that, with the
  GTPase MnmE/GTPBP3, transfers a methylene from CH2-THF to C5 of U34 and links the amine
  (glycine in bacteria, taurine in mammalian mitochondria). This is background knowledge from
  the orthologs.

## Decisions
- Accept contributes_to tRNA 5-taurinomethyluridine synthase activity (IBA/ISS), GTPBP3-MTO1
  complex, mitochondrial tRNA wobble uridine modification, mitochondrion, FAD binding.
- Generic tRNA processing / wobble uridine modification / cytoplasm: kept as non-core.
- The taurine-specific MF term assumes the mammalian chemistry; the actual U34 C5 substituent
  in fly mt-tRNAs should be verified (suggested question).

## Deep research (falcon)
- Falcon found no CG4610-specific literature; it stresses that substrate (glycine vs taurine)
  and localization are untested in flies: [file:DROME/CG4610/CG4610-deep-research-falcon.md
  "A mitochondrial tRNA-modification role is plausible because the characterized yeast and human eukaryotic MnmG-family systems act in mitochondria"].
- Yeast MSS1-MTO1 makes glycine-derived cmnm5U34, whereas human mitochondrial GTPBP3-MTO1 uses
  taurine (Maes et al. 2025 cited therein).
