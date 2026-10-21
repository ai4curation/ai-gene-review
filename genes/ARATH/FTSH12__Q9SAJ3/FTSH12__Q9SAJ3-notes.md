# FTSH12 (Q9SAJ3, At1g79560) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: reviewed Swiss-Prot canonical product Q9SAJ3 (1008 aa) of At1g79560, PANTHER
PTHR43655:SF19. Folder name `FTSH12__Q9SAJ3` because `genes/ARATH/FTSH12` is keyed to
the alternative gene model A0A1P8ARD2. No ProtNLM2 output was opened or used.

Deep research: `just deep-research-falcon ARATH FTSH12__Q9SAJ3 --fallback perplexity-lite`
failed (Edison 403 authentication failure; Perplexity 401 insufficient quota). No
deep-research file was produced. Literature was read directly from cached publications;
the existing falcon report for the same locus (genes/ARATH/FTSH12/FTSH12-deep-research-falcon.md)
was consulted only as a pointer to papers, and every claim was checked against the papers.

### Experimentally established in Arabidopsis
- Subunit of the ~2-MDa Ycf2/FtsHi complex (BN-PAGE, complex purification)
  [PMID:30309901 "The inner envelope-localized Ycf2, FtsHi1, FtsHi2, FtsHi4, FtsHi5, FtsH12, and pdNAD-MDH proteins therefore form a stable 2-MD complex (the Ycf2/FtsHi complex), which interacts with the translocating preproteins."];
  confirmed by native-promoter Myc-FtsH12 IP [PMID:33216923].
- ATP-dependent association with inner-envelope translocation intermediates
  (pFd, pSSU, pL11, pLHCP; not OEP7) [PMID:30309901].
- Inner envelope localization, C-terminal AAA+/protease domains facing stroma; absent
  from thylakoids [PMID:33216923 "the FtsH12 immunosignal strongly increased in envelope fractions, but was absent in samples of the thylakoid membrane"].
- H769Y zinc-site mutant complements embryo-lethal knockout: protease motif dispensable
  [PMID:30309901 "Furthermore, even the FtsH12 zinc binding site is dispensable for its essential function."].
- Knockout embryo lethal (heart stage); knockdown pale cotyledons, deformed chloroplasts,
  altered TIC composition; N-terminome shows normal processing of imported proteins [PMID:33216923].
- Cryo-EM: heterohexameric AAA+ motor module (PDB 8XKU/8XKV include FTSH12) [PMID:39197452, abstract only].

### Inferred only (sequence)
- Walker A GPPGTGKT (533-540), Walker B FVFVDE (587-592), HEAGH (769-773) + D849
  (FTSH12__Q9SAJ3-bioinformatics/RESULTS.md). ATPase and peptidase activity of FTSH12
  itself have never been measured. Kikuchi 2018 notes FTSH12 lacks the conserved
  hydrophobic pore-loop residues and cross-links weakly to preproteins.

### Evolutionary grounding
- Kikuchi 2018 phylogeny: FTSH12 and FtsHi derive from the plastid (cyanobacterial)
  FtsH; FTSH12 is land-plant specific (likely absent in Chlorophyta). The IBA m-AAA
  complex / mitochondrial protein processing rows come from PTN000554085 (mitochondrial
  m-AAA node, eukaryote taxon) and were removed as compartment mismatch. The
  metalloendopeptidase IBA (PTN008683692) was kept as non-core because the catalytic
  site is retained, but no activity is demonstrated.

### Decisions
- Core: contributes to GO:0016464 chloroplast protein-transporting ATPase activity;
  GO:0045037; part_of GO:0062091; located in GO:0009706.
- Removed: plasma membrane (ISM), thylakoid membrane (contradicted; UniProt source defect
  recorded), m-AAA complex and mitochondrial protein processing (IBA), bare protein binding x6.
- Mitochondrion HDA marked over-annotated (no FTSH12-specific evidence; likely co-fractionation).
- General plastid/chloroplast/envelope/cytoplasm rows MODIFY -> chloroplast inner membrane.
- For transfer to A0A1P8ARD2: only complex membership, inner-envelope location and import-motor
  role are experimentally established; peptidase and ATP hydrolysis are sequence inferences.
