# CALR3 (Calreticulin-3 / Calreticulin-2 / Calsperin / CRT2) review notes

UniProt: Q96L12 (CALR3_HUMAN), 384 aa, gene CALR3 (synonym CRT2), HGNC:20407, chromosome 19.

## Identity and family
- Member of the calreticulin family (calreticulin/calnexin), a paralog of calreticulin-1 (CALR / P27797).
  [file:human/CALR3/CALR3-uniprot.txt SIMILARITY, "Belongs to the calreticulin family"]
- Has the canonical calreticulin domain architecture: N-terminal globular (lectin) domain,
  proline-rich P-domain (arm-like), and C-terminal acidic domain, plus an N-terminal signal
  peptide (1-19) and a C-terminal ER-retention motif (KDEL-like, FT MOTIF 381..384 "Prevents
  secretion from ER"). [file:human/CALR3/CALR3-uniprot.txt DOMAIN / FT]
- Confusing nomenclature: the protein originally described as "calreticulin-2 / CRT2"
  (Persson 2002, PMID:12384296) is the same protein UniProt now names Calreticulin-3 (CALR3).
  The PMID:21590275 paper uses "CRT-2".

## Tissue specificity / expression
- Testis-specific / testis-enriched expression. [file:human/CALR3/CALR3-uniprot.txt TISSUE SPECIFICITY
  "Testis specific. {ECO:0000269|PubMed:12384296}"; HPA "Tissue enriched (testis)"]
- Originally identified as a novel testis calreticulin isoform.
  [PMID:12384296 "Identification of a novel calreticulin isoform (Crt2) in human and mouse"]

## Function
- During spermatogenesis, CALR3 (calsperin) acts as a (lectin-independent) molecular chaperone
  for specific client proteins such as ADAM3, and is required for sperm fertility.
  [file:human/CALR3/CALR3-uniprot.txt FUNCTION "During spermatogenesis, may act as a
  lectin-independent chaperone for specific client proteins such as ADAM3. Required for sperm
  fertility (By similarity)"]. This is established largely in mouse (Calr3 knockout males are
  infertile, fail to process/transport ADAM3); the human function is by similarity.
- Belongs to the chaperone keyword set; predicted unfolded protein binding (InterPro IEA
  GO:0051082) and protein folding chaperone (Ensembl ortholog transfer GO:0044183).
  [file:human/CALR3/CALR3-uniprot.txt KW "Chaperone"; DR GO lines]

## Calcium binding — KEY NEGATIVE RESULT
- Unlike calreticulin-1, CALR3/CRT-2 is NOT a Ca2+-binding protein. Stains-all staining
  (a method to detect Ca2+-binding proteins) failed to stain HA-CRT-2 immunoprecipitate
  while HA-CRT-1 stained blue. [PMID:21590275 abstract "Stains-all staining ... could not
  stain the immunoprecipitate of HA-CRT-2, although HA-CRT-1 immunoprecipitate was stained
  blue ... CRT-2 capacity for Ca(2+)-binding may be absent or much lower than that of CRT-1"]
- UniProt FUNCTION concurs: "CALR3 capacity for calcium-binding may be absent or much lower
  than that of CALR. {ECO:0000269|PubMed:21590275}".
- GOA therefore carries a NOT|enables GO:0005509 calcium ion binding (IDA, PMID:21590275).
  This negation is CORRECT and should be ACCEPTed.
- Note the C-domain still contains acidic-residue stretches and UniProt's DOMAIN comment
  (by similarity to CALR) mentions calcium binding sites, but the experimental data on CALR3
  itself show no/low calcium binding. The metal-binding KW / GO:0046872 likely reflects
  the zinc-binding sites in the N-domain (by similarity), not calcium.

## Subcellular localization
- ER lumen, confirmed experimentally: immunofluorescence shows reticular/nuclear-envelope
  pattern colocalizing with calnexin and PDI; immunoEM confirms ER lumen localization.
  [PMID:21590275 "labeling for HA-CRT-2 was seen as a reticular network with a nuclear
  envelope pattern that colocalized with calnexin and protein disulfide isomerase.
  Immunoelectron microscopy confirmed that HA-CRT-2 was localized in the lumen of the
  endoplasmic reticulum"]
- The "nuclear envelope" GO:0005635 IDA annotation reflects the nuclear-envelope component
  of the continuous ER membrane network (the outer nuclear membrane is contiguous with the ER);
  it is real but represents the ER network appearance rather than a distinct nuclear-envelope
  function. ER lumen is the primary, core location.
  [file:human/CALR3/CALR3-uniprot.txt SUBCELLULAR LOCATION "Endoplasmic reticulum lumen
  {ECO:0000255|PROSITE-ProRule:PRU10138, ECO:0000269|PubMed:21590275}"]

## Annotation assessment summary
- Core: ER-lumen molecular chaperone (calreticulin family) functioning in spermatogenesis
  (folding/maturation of sperm proteins such as ADAM3).
- ACCEPT: protein folding (GO:0006457), protein folding chaperone (GO:0044183),
  ER lumen (GO:0005788), and the NEGATED calcium ion binding (GO:0005509, NOT).
- ERAD pathway (GO:0036503, IBA): a generic calreticulin-family phylogenetic transfer; CALR3's
  documented role is client-specific chaperoning in spermatogenesis rather than ERAD per se.
  Keep as non-core (plausible by family membership but not specifically demonstrated for CALR3).
- endoplasmic reticulum (GO:0005783, IEA): correct but a less specific parent of ER lumen;
  keep as non-core.
- nuclear envelope (GO:0005635, IDA): reflects the ER-network/NE appearance; keep as non-core.

## References available
- PMID:21590275 (cached) — localization + lack of Ca2+ binding.
- PMID:12384296 — identification / testis specificity (not cached; cited from UniProt).
- file:human/CALR3/CALR3-uniprot.txt — UniProt entry.
