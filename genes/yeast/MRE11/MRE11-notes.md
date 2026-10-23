# MRE11 (S. cerevisiae, P32829, YMR224C) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative of
SCHPO/mre11 (Rad32, Q09683). No ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon yeast MRE11 --fallback perplexity-lite` failed:
falcon (Edison) returned "Failed to authenticate", and the perplexity-lite
fallback returned HTTP 401 (insufficient quota). No deep-research file exists.
The review is built from the cached publications (all 38 GOA PMIDs plus
PMID:14522986 and PMID:35501303, fetched for this review) and the UniProt record.

### Evolutionary grounding

- PANTHER: P32829 is in PTHR10139:SF1 with S. pombe Rad32 (Q09683), mouse,
  Xenopus, Arabidopsis, C. elegans and Chaetomium (G0RYR3) Mre11; human MRE11
  (P49959) is in SF4 (interpro/panther/PTHR10139/PTHR10139-entries.csv).
- The IBAs come from the family-root PAINT node PTN000015644, except the intra-S
  checkpoint IBA, which comes from PTN000015646. They are deep-node
  propagations. For most of them (HR, NHEJ, telomere maintenance, meiotic DSB
  formation, Mre11 complex, mitochondrial HR) S. cerevisiae MRE11 (SGD:S000004837)
  is itself one of the experimental donors.
- The checkpoint IBAs (G2: donors fly/mouse; intra-S: mouse/pombe) have no
  S. cerevisiae Mre11 donor. They are kept as non-core.

### What is experimentally established in S. cerevisiae (direct evidence)

Biochemistry, with purified S. cerevisiae protein:
- ssDNA endonuclease activity, abolished by D56N and H125N
  [PMID:9858579 "the purified Mre11 protein was found to have single-stranded endonuclease activity"].
- 3'->5' exonuclease activity that releases mononucleotides; hairpin and 3' tail
  cleavage [PMID:11454871].
- dsDNA endonuclease, Sae2-stimulated within MRX, which preferentially cleaves the
  5'-terminated strand next to protein-blocked ends [PMID:25231868]. MR without
  Xrs2 does this equally well [PMID:27746018]. Oligomerization of MR drives
  multiple 5'-strand incisions [PMID:35501303].
- G4 / G-rich ssDNA binding and Mn2+-dependent cleavage [PMID:16116037, PMID:17698079].
- Adenylate kinase activity belongs to Rad50 (signature-motif mutant) in MR
  complexes [PMID:17349953]. Mre11 only contributes as a complex partner.

Genetics in vivo:
- In vivo, the Mre11 nick plus 3'->5' exonuclease drives bidirectional resection
  of Spo11-linked ends [PMID:22002605].
- Meiotic DSB formation needs Mre11, through a nuclease-independent C-terminal
  region [PMID:7789757, PMID:9845372, PMID:7625279]. Meiotic DSB processing
  needs the nuclease (H125N accumulates unresected DSBs) [PMID:9858579].
- NHEJ and telomere length: mre11 null mutants are defective
  [PMID:9501103, PMID:12399380]. Nuclease-dead alleles are not
  [PMID:9858579]. These roles are therefore structural (MRX, Tel1 recruitment
  via Xrs2 [PMID:27746018]), not catalytic.
- Peripheral roles: sister-chromatid recombination [PMID:23254329],
  suppression or modulation of BIR [PMID:17321803], mtDNA DSB repair
  [PMID:22214610], BER gap filling (shown mainly with xrs2) [PMID:20040573],
  and promotion (not suppression) of TNR expansions [PMID:27173583].

### Annotations flagged for upstream review

- PMID:23080121 (Limbo et al. 2012) is a S. pombe Rad32 ATLD17/18 study,
  with biochemistry on human MRE11. The three UniProt IMP rows on P32829
  (GO:0000729, GO:0004520, GO:0042138) cite it. The terms are true for
  S. cerevisiae Mre11 on other evidence, so they are kept, but each carries a
  source_defect: the reference/evidence code does not support this yeast entry.
  The paper does not assay meiotic DSB formation at all.
- PMID:31537797 (R-loop processing, IDA by UniProt): yeast work used rad50Δ;
  "MRE11 and RNH1 are linked genes on yeast chrXIII so triple mutants with
  mre11Δ were not made". The MRE11-specific findings are in human cells.
  Marked UNDECIDED with a source_defect.
- PMID:23267104 (bacterial protein interaction paper) does not mention Mre11
  or Xrs2. The IntAct row citing it is probably mis-keyed. GO:0005515 rows are
  removed anyway under the protein-binding policy.
- GO:0035753 "maintenance of DNA trinucleotide repeats": PMID:27173583 shows
  MRX *promotes* expansions, which is the opposite of maintaining fidelity.
  Marked as over-annotated.

### Transfer caveats for SCHPO/mre11

- Safe at the SF1 level: the nuclease chemistry (ssDNA endo, dsDNA endo,
  3'->5' exo), DSB end processing and resection, removal of protein-blocked
  ends, Mre11 complex membership, and HR.
- Do not transfer the S. cerevisiae-specific role of the Mre11 C-terminus in
  *meiotic DSB formation* without species evidence. In budding yeast it is
  nuclease-independent and tied to meiotic DSB-protein interactions
  [PMID:9845372].
- The sporulation and meiotic-transcription phenotypes [PMID:17396017] are
  downstream phenotypes. They are not process participation.
