# SMIM18 notes

## 2026-10-03 - initial review (MICROPROTEINS Tier 2)

### Identity
- UniProt P0DKX4 (SIM18_HUMAN), 95 aa, PE1 (proteomics identification). HGNC:42973, chr 8p12.
- Single predicted helical TM segment, residues 35-55 [file:human/SMIM18/SMIM18-uniprot.txt "FT   TRANSMEM        35..55"].
  Location annotation is by sequence analysis only [file:human/SMIM18/SMIM18-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Single-pass membrane"].
- Gene lies inside an intron of GTF2E2, opposite strand [file:human/SMIM18/SMIM18-uniprot.txt "CC   -!- CAUTION: Encoded in intron of the gene GTF2E2 (opposite strand)."].
  Ensembl REST overlap (8:30638559-30647260) confirms SMIM18 on + strand within GTF2E2 (- strand); a RNU5A-3P snRNA pseudogene also sits in the region.
- Sequence features from my own inspection (not experimentally tested): N-x-T sequon at N6 (NETT) in the
  ~34-residue N-terminal segment; a CCCC cluster (residues 61-64) immediately after the TM helix;
  basic/charged C-terminal tail. The juxtamembrane cysteine cluster is also a feature of its relative SMIM22/CASIMO1.

### Family / conservation
- InterPro IPR031671 "SMIM5/18/22", Pfam PF15831 SMIM5_18_22, CDD cd20255 CASIMO1_SMIM22; PANTHER PTHR36982:SF1
  [file:human/SMIM18/SMIM18-uniprot.txt "DR   InterPro; IPR031671; SMIM5/18/22."].
- So SMIM18 is a relative of SMIM22 (CASIMO1), the only member with functional data (SQLE binding, breast cancer cell
  proliferation) [PMID:29765154 "CASIMO1 microprotein interacts with squalene epoxidase (SQLE)"]. Family membership
  alone does not transfer this function: the shared region is essentially the TM helix plus juxtamembrane motif.
- Ensembl Compara (REST homology/id/human/ENSG00000253457, type=orthologues): 152 species with orthologues,
  including teleost fish (danio_rerio) and elephant shark (callorhinchus_milii) -> conserved across jawed vertebrates.
  Ensembl lists no human paralogues.
- PAN-GO: 0 IBA annotations.

### Expression
- HPA: "Group enriched (brain, pituitary gland, retina)" [file:human/SMIM18/SMIM18-uniprot.txt "DR   HPA; ENSG00000253457; Group enriched (brain, pituitary gland, retina)."];
  Bgee top: cortical plate. Original cDNA came from fetal brain [file:human/SMIM18/SMIM18-uniprot.txt "RC   TISSUE=Fetal brain;"].

### Literature
- PubMed esearch "SMIM18" (tiab and all fields): 0 hits (2026-10-03). No aliases in NCBI Gene (GeneID 100507341).
- NCBI Gene-linked PMIDs: 15885500 (cDNA discovery screen, CAP-Trapper; does not discuss this gene individually),
  20125193 (cognitive-test GWAS; gene-level association only), 8889548 (cDNA library method). None functional.
- [PMID:15885500 "led us to the discovery of 342 putative new human genes"] - source of the mRNA sequence only.

### Conclusion
- No functional literature. Only GOA row is IEA membrane (UniProt SubCell mapping) - correct, ACCEPT.
- No MF/BP can be supported; core_functions left empty. No NEW terms.
- Not in gocams/index.tsv.
