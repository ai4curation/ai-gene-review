# ALDH7A1 (horse, A0A9L0R3Y5) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: full review of the Ensembl canonical horse ALDH7A1 translation A0A9L0R3Y5
(ENSECAP00000057580, gene ENSECAG00000010547). This review is the reference for later transfer to the
other horse translation A0A9L0RRL6 (`genes/HORSE/ALDH7A1/`). No ProtNLM2 file or prediction-evidence
folder was opened. The review does not use ProtNLM2 output.

### Setup and provenance

- `just fetch-gene HORSE A0A9L0R3Y5 --alias ALDH7A1__A0A9L0R3Y5` produced 13 GOA rows, all IEA:
  - GO_REF:0000044: UniProt SubCell mapping, itself ARBA-derived in this unreviewed entry.
  - GO_REF:0000120: combined IEA from human P49419, mouse Q9DBF1, ARBA and EC.
  - GO_REF:0000107: Ensembl Compara from human or mouse.
  - GO_REF:0000002: InterPro2GO.

  There are no IBA rows, probably because this accession is not in the PANTHER 19.0 member index.
  The stub set `gene_symbol` to the accession; I corrected it to ALDH7A1.
- Deep research: `just deep-research-falcon HORSE ALDH7A1__A0A9L0R3Y5 --fallback perplexity-lite`
  FAILED. Falcon gave "Exception: Failed to authenticate". The perplexity-lite fallback gave HTTP 401
  insufficient_quota. No deep-research file exists for this folder. The literature base is the cached
  human publications, the curated human review (`genes/human/ALDH7A1/`), and the human falcon deep
  research there.
- PubMed esearch, 2026-10-20, for `(ALDH7A1 OR antiquitin) AND (horse OR equine OR Equus)` and for
  `aminoadipic semialdehyde dehydrogenase AND (horse OR equine)` returned 0 records. **No function of
  horse ALDH7A1 is experimentally established in horse.** Every function claim below is an inference
  from the vertebrate ALDH7A1 clade.

### Evolutionary grounding (see ALDH7A1__A0A9L0R3Y5-bioinformatics/RESULTS.md)

- PANTHER PTHR43521:SF1 (UniProt DR line). InterPro IPR044638 ALDH7A1-like. CDD cd07130 ALDH_F7_AASADH.
- PAINT node PTN000192435 carries IBD for:
  - GO:0004043 and GO:0019477, seeded by human, mouse and zebrafish.
  - GO:0008802, seeded by human.
  - mitochondrion, seeded by mouse and human.
  - cytosol, nucleus, Golgi membrane and plasma membrane, seeded by human.

  The zebrafish seed means the node is at least a bony-vertebrate node, so horse is inside the clade.
  PAINT did NOT propagate aldehyde metabolic process, medium-chain fatty aldehyde dehydrogenase, choline
  catabolism, negative regulation of ferroptosis or hearing. I treat these as deliberate omissions and
  do not add them as NEW for horse.
- Horse vs human P49419: 95.7% identity over all 539 human residues, with no internal gap. Horse vs
  mouse Q9DBF1: 86.8%. All 14 experimentally annotated catalytic, NAD-binding and AASA-binding residues
  are conserved, including Glu323 (proton acceptor, human E296), Cys357 (nucleophile, human C330), and
  Glu454 (human E427, the PDE hot spot).
- Horse A0A9L0R3Y5 has a 27-aa Arg-rich N-terminal extension (MGCPGRGAGLYFRGSSGRRRVVRPGLS) upstream
  of the residue aligned with human Met1. The human-equivalent transit peptide follows at 28..53.
  Translation start and mitochondrial import of the horse protein are unverified.
- Human P49419 sits in SF5 and horse in SF1. The shared PAINT node and the high identity indicate an
  HMM classification artifact. Subfamily-specific transfer is not an issue here because no SF5-only
  function exists.

### Biology carried over from human (cited in the review)

- AASA/P6C oxidation to alpha-aminoadipate in lysine degradation [PMID:20207735 "the intermediate lysine
  degradation product, alpha-aminoadipic semialdehyde"; PMID:16491085 "these mutations abolish the
  activity of antiquitin as a delta1-piperideine-6-carboxylate (P6C)-alpha-aminoadipic semialdehyde
  (alpha-AASA) dehydrogenase"].
- Broad NAD+-dependent aldehyde oxidation [PMID:20207735 "Purified recombinant ALDH7A1 efficiently
  metabolized a number of aldehyde substrates"].
- Active form is a tetramer [PMID:38604394 "Because the tetramer is the active form of ALDH7A1"].
- Membrane NADH generation [PMID:31492851; PMID:40233740]. These are human-cell findings. The membrane
  locations are in the PAINT node, but ferroptosis regulation is not, so I keep the locations and do not
  add the process.

### Decisions summary

- ACCEPT:
  - GO:0004043 and GO:0019477 (core).
  - GO:0004029.
  - mitochondrion, mitochondrial matrix, cytosol.
  - identical protein binding (homotetramer).
  - Golgi membrane and plasma membrane (PAINT-placed locations of the membrane NADH-generating pool).
- KEEP_AS_NON_CORE: nucleus; betaine-aldehyde dehydrogenase.
- MODIFY: oxidoreductase activity to GO:0004029. amino acid catabolic process to GO:0019477.
- No NEW annotations.
