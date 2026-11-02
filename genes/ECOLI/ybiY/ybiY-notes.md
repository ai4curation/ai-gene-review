# ybiY (P75794, b0824, PFLE_ECOLI) notes

Deep research was unavailable for this gene (falcon returns 403; asta gave nothing
useful in Phase 1 of the RADICAL_SAM project). Notes built from UniProt, cached primary
papers, PubMed and the shared genome-context analysis
(`genes/ECOLI/pflC/pflC-bioinformatics/RESULTS.md`).

## Identity and family

- 299 aa radical SAM protein in the PFL-activating-enzyme family (PANTHER PTHR30352:SF14,
  "pyruvate formate-lyase 3-activating enzyme-related"; PIRSF000371; NCBIfam TIGR02494
  PFLE_PFLC). Radical SAM CX3CX2C ligands (C25, C29, C32) and SAM-binding residues
  annotated by similarity to PflA [file:ECOLI/ybiY/ybiY-uniprot.txt
  "/evidence=\"ECO:0000250|UniProtKB:P0A9N4\""].
- UniProt names it "Putative pyruvate formate-lyase 3-activating enzyme" with EC 1.97.1.4;
  the function line is by similarity only [file:ECOLI/ybiY/ybiY-uniprot.txt "Activation of
  pyruvate formate-lyase 2 under anaerobic conditions"; ECO:0000250]. PE level 3.
- TIGR02494 text: the E. coli PFLC and PFLE (= YbiY) proteins "appear to lack
  characterization and may activate enzymes with distinctive functions"
  [file:ECOLI/pflC/pflC-bioinformatics/RESULTS.md].

## Partner GRE: YbiW (P75793), a C-O lyase, not a pyruvate formate-lyase

- ybiY lies immediately 3' of ybiW, same strand, 5 bp gap
  [file:ECOLI/ybiY/ybiY... see file:ECOLI/pflC/pflC-bioinformatics/RESULTS.md]. ybiW-ybiY
  is divergent from fsaA (fructose-6-phosphate aldolase 1), a downstream anhydroglycolysis
  enzyme.
- YbiW catalyses ring-opening C-O cleavage of 1,5-anhydroglucitol 6-phosphate (AG6P)
  [PMID:39283600 "YbiW and PflD catalyze ring-opening C-O cleavage of
  1,5-anhydroglucitol-6-phosphate (AG6P) and 1,5-anhydromannitol-6-phosphate (AM6P),
  respectively"]. YbiW was crystallised with AG6P (PDB 8ID7). This is the first step of
  anhydroglycolysis, supporting anaerobic growth of E. coli on 1,5-anhydroglucitol.
- YbiW in vitro radical loading was low (0.02 per monomer) [PMID:42361324 "the newly
  characterized C–O lyases YbiW and PflD (0.02 and 0.06 radicals per monomer,
  respectively)"]. The cache abstract does not name the activase used; JACS full text was
  inaccessible (publisher 403).
- YbiW and PflD share the Gly-loop heptamer RVAGYSA, distinct from PFL/TdcE (RVSGYAV)
  [file:ECOLI/pflC/pflC-bioinformatics/RESULTS.md]. Activase specificity tracks the Gly
  loop [PMID:42361324]. YbiY and PflC are each other's closest paralogs (37.3% identity).

## Assessment

Same as pflC. No activase activity shown for YbiY itself; GO:0043364 (general activase)
is well supported by family placement (IBA), intact motifs and the ybiW-ybiY coupling.
The PFL-specific GO:0043365 / EC 1.97.1.4 is an over-annotation because YbiW is not a
formate C-acetyltransferase, so MODIFY to GO:0043364. Generic radical SAM rows use the
"catalysis not established" branch (GO:0051539 KEEP_AS_NON_CORE, no SAM-binding NEW row;
GO:0003824, GO:0016491 MODIFY to GO:0043364). No BP (anhydroglycolysis) term proposed for
the activase. At time of writing, genes/ECOLI/pflA was still INITIALIZED, so terms were
not aligned with it.
