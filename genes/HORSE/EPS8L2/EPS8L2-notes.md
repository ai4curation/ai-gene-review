# EPS8L2 (horse, F7BFV0) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted. No earlier review existed; the folder was created with
`just fetch-gene HORSE F7BFV0 --alias EPS8L2` (stub id confirmed as F7BFV0).

### Deep research

`just deep-research-falcon HORSE EPS8L2 --fallback perplexity-lite` failed: Edison/falcon
returned `403 Forbidden` at authentication, and the perplexity-lite fallback also failed.
No deep-research file exists. The review uses the cached primary literature below, read directly.

### Identity and gene model

- UniProt F7BFV0 (unreviewed, 806 aa, Ensembl ENSECAP00000009454.4), PANTHER PTHR12287:SF20
  (EPS8L2 subfamily), the same subfamily as human Q9H6S3 and mouse Q99K30
  (interpro/panther/PTHR12287/PTHR12287-entries.csv).
- Global alignment (EPS8L2-bioinformatics/RESULTS.md): 87.8% identity to human EPS8L2,
  86.6% to mouse Eps8l2, but 51.0% to EPS8 and 44.6% to EPS8L1, so it is the one-to-one ortholog.
- **Gene-model issue:** the horse model has a 91-residue N-terminal extension. Met92
  (`MSQSGSVSY...`) aligns to Met1 of human EPS8L2 (`MSQSGAVSC...`), and 806 - 91 = 715 = human
  length. Residues 1-75 are MobiDB-lite disordered and Pro-rich. Most likely an upstream in-frame
  start or 5' UTR included in the Ensembl model. All domains (PTB, SH3 584-643, C-terminal
  actin-binding effector region) are intact. Not a fragment; complete canonical-length product
  plus an N-terminal extension.

### Literature (read from cache)

- [PMID:14565974 Offenhauser 2004, full text] Human EPS8L2: directly binds F-actin
  ["eps8, eps8L1, and L2, but not eps8L3 could directly associate to F-actin"]; immunocomplexes
  have Rac-GEF activity ["Eps8-, eps8L1-, and eps8L2-, but not eps8L3-containing immunocomplexes
  displayed RacGEF activity"]; enriched in PDGF-induced ruffles; rescues ruffling in eps8-/- MEFs
  ["Ectopic expression of eps8, eps8L1, or eps8L2, but not of eps8L3, restored ruffling formation,
  in response to growth factor stimulation, in eps8 null MEFs"].
- [PMID:23918390 Furness 2013, full text] Mouse Eps8L2 at stereocilia tips ["Immunofluorescence
  showed that Eps8L2 was expressed at the tips of cochlear hair cell stereocilia"]; KO causes
  progressive hearing loss with hair-bundle deterioration ["We conclude that Eps8L2 is required for
  the long-term maintenance of the staircase structure and mechanosensory function of auditory hair
  bundles."]. Localization independent of Eps8 and myosin XVa.
- [PMID:26282398 Dahmani 2015] Human homozygous EPS8L2 frameshift, childhood-onset progressive
  deafness (one family).

### Decisions

- Actin binding, ruffle membrane, positive regulation of ruffle assembly, stereocilium tip,
  GEF activity (contributes_to; GO:0030676 Rac GEF is merged into GO:0005085): ACCEPT.
- Rho protein signal transduction (IBA+IEA) -> MODIFY to Rac protein signal transduction
  (GO:0016601 is not a descendant of GO:0007266; evidence is for Rac).
- Regulation of Rho protein signal transduction (IBA+IEA) -> MODIFY to positive regulation of
  Rac protein signal transduction (GO:0035022).
- Plasma membrane -> ruffle membrane; cytoplasm -> cytosol; stereocilium / stereocilium bundle
  -> stereocilium tip; plasma membrane bounded cell projection -> stereocilium tip + ruffle membrane.
- Sensory perception of sound: KEEP_AS_NON_CORE (MGI IDA on mouse; organism-level).
- Protein-containing complex, cytosol: KEEP_AS_NON_CORE.
- No NEW terms. Considered stereocilium maintenance (GO:0120045); comparator check found it on
  CLRN2, ELMOD3, PJVK, TPRN but not on EPS8 or mouse Eps8l2 (MGI chose sensory perception of
  sound), so raised as a suggested question rather than asserted.

### Relative and family

- Closest characterised relative: human EPS8L2 Q9H6S3 (same subfamily SF20; source of the
  IDA/IGI annotations). No review exists in genes/human/ (nor for mouse Eps8l2 Q99K30).
- interpro/panther/PTHR12287/ holds only entries/metadata, no family review; no placement
  disagreement (UniProt and the PANTHER entries list agree on SF20 for EPS8L2 orthologs).
- No module in modules/ covers the EPS8/ABI1/SOS1 Rac-GEF complex or stereocilia tip complex.
- Donkey partner genes/EQUAS/EPS8L2 is reviewed by another agent.
