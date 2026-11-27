# CRT10 (Q08226, YOL063C) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: CRT10 is the PomBase one-to-one ortholog of SCHPO/crt10 (O42996) and its
experimentally characterised findings will be used as a transfer reference. No ProtNLM2
output was consulted.

### Data and provenance
- `just fetch-gene yeast CRT10` created uniprot, goa (6 rows) and stub.
- `just deep-research-falcon yeast CRT10 --fallback perplexity-lite` FAILED: Edison API
  authentication returned 403 Forbidden, and the perplexity-lite fallback also failed.
  No deep-research file exists; the review is built from the primary literature below.
- Cached and read: PMID:18704118 (full text), PMID:16600900 (full text),
  PMID:20139071 (full text), PMID:37968396 (full text), PMID:25534857 (abstract only).

### Evolutionary context
- UniProt gives no PANTHER family for Q08226, so there is no PAINT/IBA node and no IBA
  rows. Q08226 has two strong PF08728 (CRT10) domains; the domain is fungal-specific.
- The reciprocal phmmer analysis done for the fission-yeast review
  (genes/SCHPO/crt10/crt10-bioinformatics/RESULTS-rereview.md) found Q08226 and O42996
  to be reciprocal sole hits through the CRT10-specific region, but similarity is weak
  (~60 residues) and O42996 is half the length. Transfer from Crt10 to O42996 should be
  limited to the pathway-level role; Rtt101/Mms1 complex membership has not been
  demonstrated for the fission-yeast protein.

### What is experimentally established in S. cerevisiae
1. Complex membership. Crt10 co-purifies with Rtt101 and Mms1, not Cdc53 [PMID:18704118
   "Crt10, a regulator of RNR gene transcription ( Fu & Xiao, 2006 ), co-purified with
   both Rtt101 and Mms1, but not with Cdc53"]. Binding to Rtt101 is Mms1-bridged
   [PMID:18704118 "The interaction between Crt10 and Rtt101 was dependent on Mms1"] and
   constitutive [PMID:18704118 "Crt10 interacted with Rtt101 in the absence of MMS"].
   Two distinct Crt10 E3 assemblies, one with Paf1C [PMID:25534857 "We also identified
   two distinct Crt10-containing E3 complexes, one of which contained the Paf1 complex"].
2. Nonfunctional 25S rRNA decay [PMID:25534857 "Crt10 was required for 25S NRD, but not
   for DNA repair"].
3. RNR regulation (genetic, indirect): crt10 deletion gives HU resistance, partial mec1
   rescue, elevated RNR2/RNR3, acts in the Dun1-Crt1 pathway and is needed for normal CRT1
   transcript levels [PMID:16600900 "Epistatic analysis indicates that CRT10 belongs to
   the CRT1 pathway but not the SML1 pathway."]. CRT10 is DNA-damage inducible, DUN1
   dependent.

### Inferred, not established
- Substrate-adaptor (DCAF-like) molecular function: proposed by analogy only
  [PMID:18704118 "suggesting that they could function as substrate-specific adaptors"].
  No substrate known. MF ND kept; GO:1990756 not proposed.
- Subcellular location: none reported.

### Decisions
- MF ND: ACCEPT. Protein binding x2 (Rtt101): REMOVE per GO:0005515 policy; bridged
  interaction.
- CC ND: MODIFY to GO:0035361 Cul8-RING ubiquitin ligase complex. Comparator check via
  QuickGO: Mms22 (same receptor role), Mms1, Rtt101, Hrt1, Rtt107 all carry IDA part_of
  GO:0035361 (mostly from PMID:20139071, which does not assay Crt10); Crt10 lacks it only
  because PMID:18704118 was curated to protein binding.
- Nonfunctional rRNA decay IMP/IGI: ACCEPT (core). Crt10 is a subunit of the E3 that
  executes the ubiquitin-dependent step, so participation rather than mere necessity.
- No NEW transcription-regulation term: evidence is indirect genetics and GOA carries no
  process from PMID:16600900; recorded as a suggested question.
