# Curation Notes: doc (Q06259) — Bacteriophage P1

## Identity & Genomic Context
- **Gene symbol**: `doc` ("death on curing")
- **UniProtKB**: `Q06259` (`DOC_BPP1`, 126 aa, 13.6 kDa)
- **Organism**: Punavirus P1 (`NCBITaxon:2886926`, *Escherichia phage P1*)
- **Locus**: Plasmid addiction operon `phd-doc` (co-transcribed downstream of `phd`, with translational coupling between the stop codon of `phd` and the start codon of `doc`) [PMID:8411153].

## Molecular Function & Mechanism
1. **Fic-family Protein Threonine Kinase (EF-Tu Kinase)**:
   - Although Doc contains a degenerate Fic (filamentation induced by cAMP) catalytic motif (`HxFx(D/E)GNGRxxR`, specifically `H66-I67-F68-N69-D70-A71-N72-G73-R74`), it does **not** catalyze AMPylation [PMID:24141193].
   - Instead, Doc binds nucleoside triphosphates (ATP or GTP) in an **inverted orientation** relative to canonical Fic AMPylases, positioning the gamma-phosphate for transfer [PMID:24141193].
   - Doc specifically phosphorylates host translation elongation factor EF-Tu (`P0CE47`) at a single conserved threonine residue in domain 3, **Thr-382** (`Thr382`), which abolishes ternary complex formation with aminoacyl-tRNA and stalls translation elongation [PMID:24141193, PMID:24448800, PMID:18398006].
   - Quantitative phosphoproteomics across the entire *E. coli* proteome confirmed that EF-Tu `Thr-382` is the **sole** physiological phosphorylation target of Doc; no serine residues are phosphorylated [PMID:24448800, PMID:24141193].
   - Doc can also catalyze the reverse reaction (dephosphorylation of phospho-EF-Tu by ADP/GDP to form ATP/GTP) [PMID:24141193].

2. **Transcriptional Corepressor of the `phd-doc` Operon**:
   - Doc does **not** bind DNA on its own (`PMID:9829946`: *"Consistent with these in vivo results, we found that Phd binds to the operator DNA whereas Doc, which does not bind to the DNA by itself, greatly enhances the affinity and cooperativity of binding in combination with Phd"*).
   - Monomeric Doc possesses two distinct asymmetric binding sites (`Site 1` and `Site 2`) for the C-terminal intrinsically disordered domain of Phd (`Q06253`), enabling a single Doc monomer to bridge two operator-bound Phd dimers (`Phd2-Doc-Phd2`) on `OR1` and `OR2` [PMID:18757857, PMID:20603017].
   - At low `[Doc]/[Phd]` ratios, this bridging strongly enhances operator binding and transcriptional repression; at high `[Doc]/[Phd]` ratios, saturation of both sites on Phd dimers disrupts the bridge and derepresses transcription (**conditional cooperativity**) [PMID:20603017].

3. **Post-Segregational Killing (Plasmid Addiction)**:
   - In plasmid-free daughter cells, degradation of the labile Phd antitoxin by host ClpXP protease releases stable Doc to phosphorylate EF-Tu, arresting translation and causing cell growth arrest / post-segregational killing [PMID:8411153, PMID:11222604, PMID:18398006].

## Review of Existing GOA Annotations
- `GO:0004674` (`protein serine/threonine kinase activity`, IDA `PMID:24448800` and IEA `GO_REF:0000003` via `EC:2.7.11.1`): **ACCEPT**. Standard GO term for non-receptor protein serine/threonine kinases (GO does not maintain a separate `protein threonine kinase activity` term distinct from `GO:0004674`).
- `GO:0106310` (`protein serine kinase activity`, IEA `GO_REF:0000116` via `RHEA:17989`): **REMOVE**. Automated Rhea mapping artifact from the broad EC number `2.7.11.1`; both `PMID:24141193` and `PMID:24448800` proved that Doc exclusively phosphorylates **Thr-382** of EF-Tu and does not phosphorylate any serine residue.
- `GO:0003677` (`DNA binding`, IEA `GO_REF:0000043` via `UniProtKB-KW:KW-0238`): **REMOVE**. Doc does not bind DNA by itself [PMID:9829946]; it functions as a DNA-non-binding transcriptional corepressor (`GO:0003714`) by bridging Phd dimers.
- `GO:0005524` (`ATP binding`, IEA `GO_REF:0000043` via `UniProtKB-KW:KW-0067`): **ACCEPT**. Doc binds ATP (and GTP) in an inverted orientation to donate the gamma-phosphate to EF-Tu [PMID:24141193].
- `GO:0000166` (`nucleotide binding`, IEA): **TOO_GENERAL** (entailed by `GO:0005524` `ATP binding`).
- `GO:0016301` (`kinase activity`, IEA) and `GO:0016740` (`transferase activity`, IEA): **TOO_GENERAL** (entailed by `GO:0004674` `protein serine/threonine kinase activity`).
- `GO:0005515` (`protein binding`, IPI with `Q06253` in `PMID:20603017` and IPI with `P0CE47` in `PMID:24141193`): **REMOVE** per protein-binding policy.
- `GO:0039604` (`symbiont-mediated suppression of host translation`, IDA `PMID:18398006` and IMP `PMID:11222604`): **ACCEPT**.
- `GO:0044696` (`killing by virus of host cell by post-segregational killing`, IMP `PMID:11222604`): **ACCEPT**.
