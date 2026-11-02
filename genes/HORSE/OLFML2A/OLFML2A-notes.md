# OLFML2A: paired human–horse review notes

## Biological evidence

Photomedin-1/OLFML2A is distinct from photomedin-2/OLFML2B and OLFM2. Mouse recombinant experiments establish secretion, disulfide-linked oligomerization, and binding to sulfated glycosaminoglycans. Human podocyte imaging supports a relevant glomerular protein pool. Matrix binding does not by itself demonstrate matrix assembly or a defined signaling receptor.

- [PMID:15836428: Identification and characterization of photomedins: novel olfactomedin-domain-containing proteins with chondroitin sulphate-E-binding activity.](https://pubmed.ncbi.nlm.nih.gov/15836428/) — abstract cached; full-text availability must be checked separately.
- [PMID:18757743: Transcriptome-based systematic identification of extracellular matrix proteins.](https://pubmed.ncbi.nlm.nih.gov/18757743/) — abstract cached; full-text availability must be checked separately.
- [PMID:22913984: Neuronal proteins are novel components of podocyte major processes and their expression in glomerular crescents supports their role in crescent formation.](https://pubmed.ncbi.nlm.nih.gov/22913984/) — abstract cached; full-text availability must be checked separately.

## Exact horse model

The selected horse model lacks the human1–27 signal-peptide region and an internal segment. Its olfactomedin domain is strongly conserved, but normal secretory entry and maturation are unresolved. Consequently extracellular localization, binding and organization are UNC for this exact model despite a reasonable extracellular family default.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/OLFML2A/OLFML2A-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

Check horse transcript starts and test secretory targeting. Trace the extracellular-matrix screen at gene/assay level before making a specific matrix-organization claim. Cancer-expression/knockdown associations in the Edison report are leads, not a demonstrated receptor mechanism.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined the single GOA row, the description, core functions, the PANTHER placement and the
horse gene models. ProtNLM2 output was not consulted.

Deep research: `just deep-research-falcon HORSE OLFML2A --fallback perplexity-lite` failed (falcon
"Failed to authenticate"; perplexity 401 insufficient quota). No horse deep-research file exists. The
literature used is the cached primary papers (PMID:15836428, PMID:22913984, PMID:18757743), all of
them abstract-only. The human Falcon report was used only to find sources.

### Identity of the benchmark accession (gene-model finding)

- A0A9L0SKW1 (599 aa, ENSECAT00000146926) is NOT the canonical product. The same Ensembl gene
  (ENSECAG00000023908) also gives A0A3Q2LAT7 (621 aa) and five RefSeq isoforms. RefSeq isoform X1,
  XP_023484611.2 (650 aa), begins `MAAAALPPRPRPLALLLLPLLLLRAGTVRADSKVFGD`. That hydrophobic leader is
  homologous to the human 1-27 signal peptide (max 11-residue KD hydropathy 3.13, against 2.93 for
  human), and the isoform pairs with human Q68BL7 over all but five positions
  [file:HORSE/OLFML2A/OLFML2A-bioinformatics/RESULTS-rereview.md "The horse locus encodes a leader-bearing product."].
- A0A9L0SKW1 is leaderless. Human 2-27 are unpaired, and the model begins MDSQ-VFGD, the same start
  as A0A3Q2LAT7 and RefSeq X2. It is also the only horse model that lacks the segment opposite human
  123-144. Compared with the canonical product it is 51 residues shorter, has no signal peptide, and
  is missing that 22-residue N-terminal segment. The olfactomedin domain is complete, including the
  cysteines (horse C342/C529) of the conserved disulfide that corresponds to human 395-582. A
  leaderless start also occurs in human isoform 2 (VSP_029566, missing 1-39).
- The UniProt CAUTION about missing residues for PRU00446 feature propagation does not reflect a loss
  of the disulfide cysteines, because both are present.
- No reviewed (Swiss-Prot) horse OLFML2A exists, and no UniProt entry corresponds to RefSeq X1. Under
  the campaign rule there is therefore no canonical UniProt product to review next.

### Evolutionary grounding

- PANTHER PTHR23192:SF29 (OLFACTOMEDIN-LIKE PROTEIN 2A). Mouse Q8BHP7, human Q68BL7, pig and Xenopus
  OLFML2A are in the same subfamily (interpro/panther/PTHR23192/PTHR23192-entries.csv). OLFML2B is in
  SF37, so photomedin-2 data are not transferred.
- PAINT (PTHR23192-paint.tsv): node PTN000573635, the family root (taxon 33213), carries GO:0005576
  extracellular region and GO:0007165 signal transduction. Two other nodes carry other terms:
  PTN002754680 has GO:0005794 Golgi apparatus and GO:0001649 osteoblast differentiation, and
  PTN002754674 has GO:0009986 cell surface. Neither human nor horse OLFML2A has any of these terms
  in GOA, so OLFML2A is not inferred to sit below those nodes. Human gets
  both root IBAs; horse A0A9L0SKW1 carries neither in GOA.
- Mouse experimental GO (QuickGO, Q8BHP7): extracellular matrix binding IDA (PMID:15836428);
  identical protein binding IPI (PMID:15836428); extracellular matrix IDA (PMID:15836428,
  PMID:18757743); ECM organization IDA, acts_upstream_of_or_within (PMID:18757743).

### Decisions

- GO:0005576 extracellular region (IEA, GO_REF:0000044): UNDECIDED changed to ACCEPT. The earlier
  review was waiting on a transcript-model check, and that check shows the locus encodes a secreted,
  leader-bearing product. The SF29 mouse ortholog is experimentally secreted, and PAINT places the term
  at the root of the lineage. The leaderless model would not be secreted on its own. The caveat is
  recorded here and in identity notes rather than used to reject a gene-level location.
- NEW GO:0050840 extracellular matrix binding (ISS from mouse IDA, PMID:15836428). This is the one
  molecular activity established in SF29. It is kept at the curator's term and not refined to
  heparin or chondroitin-sulfate binding, because the binding site is unmapped and only mouse was assayed.
- Not added: extracellular matrix (CC) and ECM organization. Mouse IDA exists, but the repo
  PTHR23192 family review marks ECM residence as UNRESOLVED. The ECM-organization IDA is
  acts_upstream_of_or_within, from a screen whose abstract does not name OLFML2A, and the binding data
  show neither matrix assembly nor participation. Signal transduction (the root IBA) is not added: it
  has no OLFML2A-specific support, and PAINT did not propagate it to this horse entry.
- Not added: identical protein binding (dimerization). It is non-core, and the shortened N-terminal
  region of this model makes transfer of dimer formation uncertain.

### Relative to review next

The closest experimentally characterized relative is mouse Olfml2a (photomedin-1, Q8BHP7), the SF29
ortholog that carries all the IDA/IPI annotations. The repo has no mouse review (genes/mouse has no
Olfml2a folder). Human OLFML2A (Q68BL7) has a complete review, but its annotations are all
transferred from mouse.

### Family placement

The PTHR23192 family review lists A0A9L0SKW1 under SF29, which agrees with the UniProt PANTHER
cross-reference. There is no disagreement. Its subfamily description already flags the horse
gene-model difference.

Modules: no file under modules/ mentions OLFML2A, Q68BL7, Q8BHP7 or PTHR23192.
