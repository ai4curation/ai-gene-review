# KRT9 (UniProt P35527) bioinformatics results

Target: human keratin, type I cytoskeletal 9 (KRT9), 623 residues. Purpose: characterise the
protein and place every reported disease variant on it, in support of the GO annotation review
and the epidermolytic palmoplantar keratoderma 1 (EPPK1, MONDO:0007758, MIM 144200) mechanism
entry. Every number below is copied from a file in `results/`, which the numbered scripts write
from the fetched inputs in `data/`; the source file is named after each finding.

## Checklist

- [x] No script contains hardcoded inputs or results; accession, gene and thresholds are
  command-line options, and all values come from `data/`.
- [x] Scripts tested on another input: `01_architecture.py` was run on KRT14 (P02533) as a
  control (`results/01_control_KRT14_*`).
- [ ] Scripts 02-05 were run for KRT9 only (not exercised on a second gene).
- [x] All analyses completed; no source was unreachable (one PANTHER ortholog accession,
  cat M3WGY3, no longer resolves in UniProt and was left out).
- [x] Direct script outputs are in `results/`; inputs and their provenance are in `data/`.
- [x] Provenance and method are stated below; limitations are listed at the end.

## Methods

### Data sources (all retrieved 2026-11-26; details in `data/manifest.json`)

| source | what | version |
|---|---|---|
| UniProtKB REST (`rest.uniprot.org`) | P35527 entry; all reviewed human keratins (54 with a "Keratin, type I/II" name); all reviewed human intermediate filament family proteins; ortholog sequences | release 2026_04 (04-November-2026); P35527 entry version 230, sequence version 3 |
| ClinVar via NCBI E-utilities (esearch + esummary, term `KRT9[gene]`) | 253 records | live database on the retrieval date |
| gnomAD GraphQL API (`gnomad.broadinstitute.org/api`) | gene constraint and all variants, dataset `gnomad_r4`, GRCh38, canonical/MANE transcript ENST00000246662 (NM_000226.4) | gnomAD v4 (dataset id `gnomad_r4`) |
| InterPro API | signature matches on P35527 (PROSITE PS00226 used for the helix termination motif) | live |
| PANTHER ortholog API (`matchortho`, least diverged orthologs) | 11 KRT9 orthologs, 10 resolved to UniProt sequences | PANTHER 19 |
| AlphaFold DB API | model AF-P35527-F1 | model version 6 (AlphaFold Monomer v2.0 pipeline) |
| RCSB PDB search + data API; PDBe `best_structures` | all PDB entries for reviewed human intermediate filament proteins (94 entries: 70 X-ray, 19 NMR, 4 EM, 1 without method) | live |

### Procedures

1. **Architecture** (`01_architecture.py`). Domain boundaries are the UniProt `Region` features.
   Composition per domain; "glycine loop" candidates are runs of at least three Gly/Ser residues
   (at least two Gly) between two non-Gly/Ser anchor residues. The heptad register is computed
   per UniProt coil segment by a Viterbi path over positions a-g: a residue at a or d scores its
   Kyte-Doolittle hydropathy / 4.5, continuing the heptad is free and any discontinuity costs 3.0.
   This is a hydrophobic-periodicity method, not a trained predictor; it was validated afterwards
   against crystal structures (finding S3). Boundary segments are defined a priori as the first
   20 residues of Coil 1A ("helix initiation segment") and the last 20 residues of Coil 2
   ("helix termination segment"); window sizes 10-30 are reported as a sensitivity analysis.
2. **Variants** (`02_variants.py`). UniProt natural variants, ClinVar records (protein change
   parsed from the record title) and gnomAD variants on the canonical transcript are merged by
   protein-level HGVS. The reference residue of every protein-level variant is compared with the
   canonical sequence. gnomAD allele counts use only call sets passing gnomAD filters.
   "Disease set" = UniProt variant with a disease note, or ClinVar Pathogenic / Likely pathogenic.
3. **Statistics** (`03_statistics.py`). Two-sided Fisher exact tests compare disease-set missense
   variants with gnomAD missense variants (PASS, allele count > 0, not in the case set) inside
   versus outside a region, at variant level and at distinct-position level; a one-sided binomial
   test compares the case fraction with the region's share of the protein length.
4. **Conservation** (`04_conservation.py`). FAMSA (pyfamsa 0.7.0, defaults) alignments of (i) the
   28 reviewed human type I keratins, (ii) all 54 reviewed human keratins, (iii) KRT9 with its
   PANTHER orthologs. "Identity" at a KRT9 position is the fraction of the other aligned
   sequences carrying the KRT9 residue. Disease variants of other keratins are their UniProt
   natural variants with a disease note, looked up by alignment column.
5. **Structure** (`05_structure.py`). pLDDT is read from the AlphaFold model. Templates are X-ray
   entries in which a chain of at least 30 residues aligns locally to KRT9 (BLOSUM62, at least
   25 aligned pairs, at least 25% identity) and has a parallel partner chain in the asymmetric
   unit. For each template residue mapped to a KRT9 position: side-chain heavy-atom contact with
   the partner chain (< 4.0 A), relative solvent accessibility in the dimer and in the isolated
   chain (Shrake-Rupley; Tien et al. 2013 maximum areas; "buried" < 0.25), interchain salt
   bridges (< 4.0 A), interchain hydrogen-bond candidates (<= 3.5 A) and intrachain salt bridges.
   Non-keratin homodimers (lamin, vimentin, GFAP) are used as remote templates only when their
   alignment to KRT9 has no gaps. AlphaFold-Multimer was not available and no model of the
   KRT9 heterodimer was built.

## Findings

Each statement stands on the named result file.

### Sequence architecture

- A1. The canonical UniProt P35527 sequence fetched for this analysis (623 residues, sequence
  version 3, UniProt release 2026_04) is identical to the sequence in the local
  `KRT9-uniprot.txt` record. (`02_numbering_check.json`)
- A2. The KRT9 head domain (residues 1-152) is 48.0% glycine and 21.7% serine (69.7% Gly+Ser,
  13.2% aromatic), and the tail domain (residues 462-623) is 56.8% glycine and 22.2% serine
  (79.0% Gly+Ser), whereas the three coil segments of the rod contain 0-3.6% glycine and 29.5-34.8%
  charged residues. (`01_KRT9_domains.tsv`)
- A3. The KRT9 head contains 16 glycine-loop candidates covering 78 residues, anchored most often
  by phenylalanine, and the tail contains 17 glycine-loop candidates covering 113 residues,
  anchored most often by tyrosine; the most frequent hexapeptides are GGFGGG (5 copies) in the head and YGGGSG
  (6 copies) in the tail. (`01_KRT9_architecture.json`)
- A4. A hydrophobic-periodicity heptad assignment of the KRT9 rod finds a continuous heptad
  register through Coil 1A (153-188) and Coil 1B (208-299), and two discontinuities in Coil 2
  (323-461): a one-residue skip after residue 342 and a stutter (equivalent to a four-residue
  insertion) after residue 405, 56 residues before the end of Coil 2. The same method places the
  stutter of KRT14 after residue 366, also 56 residues before the end of its Coil 2.
  (`01_KRT9_architecture.json`, `01_control_KRT14_architecture.json`)
- A5. In the computed register the start of KRT9 Coil 1A reads Met157 = a, Leu160 = d, Asn161 = e,
  Arg163 = g, Leu164 = a, Tyr167 = d, Leu168 = e, Val171 = a and Gln172 = b; at the end of Coil 2,
  Tyr454 = d and Leu458 = a; Cys406 is the first residue after the stutter and is assigned
  position e. (`01_KRT9_heptad_register.tsv`)
- A6. The helix initiation segment of KRT9 (first 20 residues of Coil 1A, 153-172) is
  EKSTMQELNSRLASYLDKVQ, against a human type I keratin consensus of EKETMQNLNDRLASYLEKVR.
  (`01_KRT9_architecture.json`, `04_conservation_summary.json`)
- A7. The PROSITE intermediate filament rod signature PS00226 matches KRT9 residues 451-459
  (IETYHNLLE), and the end of Coil 2 reads TYHNLLEGG (453-461): KRT9 has the helix termination
  motif in a variant form that does not match the strict pattern [ST]-Y-R-x-L-L-E-G-E (which
  matches KRT14 414-422, TYRRLLEGE), with His455 in place of the arginine and Gly461 in place of
  the final glutamate. (`01_KRT9_architecture.json`, `01_control_KRT14_architecture.json`)

### Residue numbering

- N1. Every protein-level variant agrees with the canonical P35527 sequence at its reference
  residue: 22 of 22 UniProt variant features, 211 of 211 ClinVar records with a protein change,
  and 1,496 of 1,496 gnomAD protein-level variants (synonymous included) on ENST00000246662; no
  mismatch was found.
  (`02_numbering_check.json`)
- N2. In the canonical P35527 sequence the only arginine in the first 20 residues of Coil 1A is
  Arg163; residue 162 is serine. The hotspot arginine is therefore R163 in current numbering.
  (`02_numbering_check.json`)
- N3. UniProt records a sequence conflict at residues 12-13 (canonical SR, a single T in the
  original cDNA sequences AAC60619 and CAA52924), which makes those earlier sequences one residue
  shorter upstream of the rod; canonical Arg163 is residue 162, Asn161 is residue 160 and Met157
  is residue 156 in that numbering, which accounts for older reports of "R162" and "N160".
  (`02_numbering_check.json`)

### Variant catalogue and distribution

- V1. UniProt lists 22 KRT9 natural variants (21 missense and one delins, Tyr167 to Trp-Leu), all
  annotated to EPPK1; ClinVar returns 253 KRT9 records, of which 153 are distinct missense
  changes, 4 nonsense, 3 frameshift and 10 in-frame indels in single-gene records, and 7 are
  multi-gene copy-number records; gnomAD v4 has 928 distinct missense changes on the canonical
  transcript, 810 of them passing filters with a non-zero allele count.
  (`02_variant_summary.json`, `03_statistics.json`)
- V2. ClinVar classifies 21 KRT9 missense variants and one nonsense variant (p.Tyr558Ter) as
  pathogenic or likely pathogenic; 20 of the 21 missense variants lie in Coil 1A at residues
  157-171 and the other is p.Tyr454His near the end of Coil 2. (`02_variants_merged.tsv`,
  `03_domain_distribution.tsv`)
- V3. Combining UniProt disease variants with ClinVar pathogenic or likely pathogenic variants
  gives 28 disease missense variants at 11 positions: 24 variants at eight positions of Coil 1A
  (Met157, Leu160, Asn161, Arg163, Tyr167, Leu168, Val171, Gln172) and four variants at three
  positions of Coil 2 (Cys406, Tyr454, Leu458). None lies in the head, linker 1, Coil 1B, linker
  12 or the tail. (`03_domain_distribution.tsv`, `02_variants_merged.tsv`)
- V4. All 24 disease missense variants in Coil 1A fall within its first 20 residues (153-172),
  the helix initiation segment, which is 3.2% of the protein; only 11 of 805 gnomAD missense
  variants outside the disease set fall there (Fisher exact odds ratio 433, p = 5.6e-34; at the
  level of distinct positions 8 of 11 versus 6 of 469, odds ratio 206, p = 7.3e-12). The
  enrichment is significant for every window size from 10 to 30 residues.
  (`03_enrichment_tests.tsv`)
- V5. The last 20 residues of Coil 2 (442-461), the helix termination segment, hold 3 of the 28
  disease missense variants against 21 of 805 gnomAD missense variants (odds ratio 4.5,
  p = 0.043); with ClinVar pathogenic or likely pathogenic variants alone it is 1 of 21 against 22
  of 807 (p = 0.45), so enrichment at the helix termination end is weakly supported and depends
  on two UniProt-listed variants (p.Leu458Phe, p.Leu458Pro) that ClinVar does not classify as
  pathogenic. (`03_enrichment_tests.tsv`, `02_variants_merged.tsv`)
- V6. Together the two 20-residue rod-end segments (40 residues, 6.4% of the protein) contain 27
  of 28 disease missense variants and 32 of 805 gnomAD missense variants (odds ratio 652,
  p = 3.0e-33); the single disease-set variant outside them is p.Cys406Arg. (`03_enrichment_tests.tsv`)
- V7. Fifteen of the 28 disease missense variants are at predicted heptad a or d positions, compared
  with 93 of 805 gnomAD missense variants (odds ratio 8.8, p = 1.7e-7); the remainder are at e
  (7), g (5) and b (1) positions. Four disease variants substitute proline (p.Leu160Pro,
  p.Arg163Pro, p.Gln172Pro, p.Leu458Pro). (`03_enrichment_tests.tsv`, `03_statistics.json`)
- V8. gnomAD missense variation inside the helix initiation segment is sparse and rare: 14
  variants with a combined allele count of 31 (largest 7), three of which are disease-set
  variants seen at very low frequency (p.Asn161Ser, allele count 2; p.Arg163Gln, 5;
  p.Val171Met, 1). (`03_boundary_gnomad_missense.tsv`)
- V9. p.Cys406Arg, listed by UniProt as an EPPK1 variant, has 835 alleles in gnomAD (allele
  frequency 5.2e-4, 5 homozygotes) and conflicting classifications in ClinVar; it is the only
  disease-set missense variant outside the rod-end segments and is far more frequent than any
  other (the next is p.Leu458Phe with 6 alleles). The population data do not support
  p.Cys406Arg as a fully penetrant dominant EPPK allele. (`03_statistics.json`)

### Loss-of-function tolerance

- L1. gnomAD v4 constraint metrics show KRT9 is not depleted of loss-of-function variation:
  pLI = 5.5e-8, observed/expected pLoF = 0.66 (90% interval 0.50-0.88, i.e. LOEUF 0.88; 34
  observed, 51.4 expected), and missense observed/expected = 0.95 (missense Z = 0.57).
  (`03_statistics.json`)
- L2. gnomAD v4 contains 84 high-confidence predicted loss-of-function KRT9 variants passing
  filters (42 frameshift, 26 stop-gained, 16 essential splice) with a combined allele count of 247
  (cumulative allele frequency 2.3e-4) and one homozygote; they are spread over every domain.
  (`03_statistics.json`, `03_plof.tsv`)
- L3. ClinVar holds seven truncating KRT9 variants (four nonsense, three frameshift); six are
  uncertain or unclassified and one, p.Tyr558Ter in the tail, is classified pathogenic by a single
  submitter with no condition named. No frameshift or splice variant is classified pathogenic or
  likely pathogenic. (`03_statistics.json`)
- L4. The disease alleles of KRT9 are almost exclusively missense substitutions at the two ends
  of the rod, while heterozygous predicted loss-of-function alleles occur in the general
  population at a combined frequency of about 2.3e-4 and the gene shows no loss-of-function
  constraint. This pattern argues against haploinsufficiency as the EPPK1 mechanism and is the
  pattern expected of a dominant-negative (assembly-poisoning) mechanism; the population data
  alone cannot demonstrate that mechanism. (`03_statistics.json`, `03_domain_distribution.tsv`)
- L5. In-frame insertions and deletions in gnomAD (36 variants, combined allele count 1,160) are
  confined to the glycine-rich head (16), linker 1 (2) and tail (18; allele count 1,115); none
  occurs in a coil segment. (`03_statistics.json`, `03_domain_distribution.tsv`)

### Conservation and cross-keratin hotspots

- C1. Met157, Leu160, Asn161, Arg163, Tyr167, Leu168, Val171 and Tyr454 of KRT9 are identical in
  all 27 other reviewed human type I keratins; Leu458 is identical in 24 of 27 (isoleucine in the
  other three). Among ten KRT9 orthologs (chimpanzee, gorilla, macaque, mouse, rat, cow, dog,
  opossum, platypus) these positions are identical except Leu168 (methionine in two).
  (`04_variant_conservation.tsv`, `04_conservation_summary.json`)
- C2. Gln172 is a KRT9-specific residue: the aligned position is arginine in 25 and histidine in 2
  of the 27 other human type I keratins, and arginine in KRT1 and KRT5. Cys406 is cysteine in 9
  and serine in 10 of the 27 other type I keratins. (`04_variant_conservation.tsv`)
- C3. Mean identity of KRT9 to the other human type I keratins is 0.74 in the helix initiation
  segment and 0.61 in the helix termination segment, compared with 0.48 for the rest of the rod
  coils, 0.33 for the head and 0.29 for the tail. (`04_region_conservation.tsv`)
- C4. KRT9 Arg163 aligns with KRT14 Arg125 and KRT10 Arg156, and with KRT16 Arg127, KRT17 Arg94,
  KRT12 Arg135 and KRT13 Arg114, all of which carry UniProt disease variants (KRT14 R125C/G/H/S in
  epidermolysis bullosa simplex; KRT10 R156C/H/L/P/S in epidermolytic hyperkeratosis); the type II
  keratins KRT1 and KRT5 have glutamine and lysine at this column. (`04_variant_conservation.tsv`)
- C5. Ten of the eleven rod positions with KRT9 disease variants also carry disease variants in at
  least one other human keratin (the exception is Cys406). Among 91 alignment columns with a
  keratin disease variant (gene counts include KRT9 itself), the column of KRT9 Asn161 ranks first (12 keratin genes, 30 variants),
  Met157 third (9 genes), Leu458 fourth (9 genes), Leu168 fifth (9 genes), Leu160 sixth (8
  genes), Arg163 eighth (7 genes, 23 variants) and Tyr454 tenth (6 genes).
  (`04_hotspot_columns.tsv`, `04_variant_conservation.tsv`)

### Structure

- S1. There is no experimental structure of KRT9: the UniProt entry has no PDB cross-reference,
  an RCSB search by accession P35527 returns no entry, and PDBe `best_structures` returns none.
  (`05_structure_summary.json`)
- S2. In the AlphaFold model AF-P35527-F1 (version 6) the coil segments are predicted with high
  confidence (mean pLDDT 86.3 for Coil 1A, 94.1 for Coil 1B, 92.7 for Coil 2) and the head and tail
  with very low confidence (mean pLDDT 34.7 and 38.5; 97% and 96% of residues below 50), consistent
  with disordered glycine-rich end domains. (`05_alphafold_plddt_by_domain.tsv`)
- S3. Seven type I keratin chains in crystal structures of type I/type II heterodimers can be
  mapped to KRT9 without gaps: KRT10 coil 1B with KRT1 (PDB 6E2J and 6EC0; KRT9 residues 200-299,
  64% identity), KRT10 coil 2B with KRT1 (4ZRY and 6UUI; KRT9 355-460, 55-56% identity) and KRT14
  coil 2B with KRT5 (3TNU and 6JFV; KRT9 369-460, 59-61% identity). Residues that the sequence
  method assigns to heptad a or d contact the type II partner in 89.5% of 191 observations,
  e or g residues in 56.7% of 194, and b, c or f residues in 0% of 283, which validates the
  computed register over Coil 1B and the second half of Coil 2. (`05_templates.tsv`,
  `05_heptad_vs_contact.tsv`)
- S4. No crystal structure of a keratin heterodimer covers Coil 1A, where 24 of the 28 KRT9
  disease missense variants lie. The only dimeric templates for this segment are homodimers of
  lamin A coil 1A (PDB 6YF5, 6YSH, 8I33; 45% identity to KRT9 over 40 residues) and vimentin coil
  1A (PDB 3G1E; 53% identity over 30 residues). (`05_templates.tsv`, `05_structure_summary.json`)
- S5. In the lamin and vimentin coil 1A homodimers, the residues aligned with KRT9 Val171,
  Tyr167 and Leu160 (predicted a, d and d positions) have side chains in contact with the partner
  helix in 12 of 12, 12 of 12 and 10 of 12 chains (mean relative accessibility 0.07, 0.24 and
  0.22), and the residue aligned with Met157 (a leucine in the templates) in 8 of 12; these
  positions form the hydrophobic core of the coil 1A dimer. (`05_variant_structure_summary.tsv`)
- S6. The residues aligned with KRT9 Asn161, Arg163 and Leu168 (predicted e, g and e positions)
  flank the core: their side chains touch the partner helix in 6, 4 and 9 of 12 template chains
  and remain largely solvent exposed (mean relative accessibility 0.38, 0.45 and 0.28). The
  arginine equivalent to Arg163 forms no interchain salt bridge in these homodimers, but forms an
  intrachain salt bridge with the glutamate four residues earlier (lamin A Arg41-Glu37) in 5 of 12
  chains; KRT9 has a glutamate at the equivalent position (Glu159).
  (`05_variant_structure_summary.tsv`, `05_variant_structure_map.tsv`, `02_numbering_check.json`)
- S7. The residue aligned with KRT9 Gln172 (predicted b position, an arginine in the templates)
  makes no contact with the partner helix in any of 12 template chains (mean relative
  accessibility 0.52); the only KRT9 disease variant at this surface position is the proline
  substitution p.Gln172Pro. (`05_variant_structure_summary.tsv`, `02_variants_merged.tsv`)
- S8. In keratin heterodimer crystal structures the tyrosine equivalent to KRT9 Tyr454 (KRT14
  Tyr415, KRT10 Tyr449; predicted d position) packs against the type II partner in 4 of 5 chains,
  contacting KRT5 Ile467, Arg471 and Leu474 or KRT1 Ile479 and Tyr482, with mean relative
  accessibility 0.27. The leucine equivalent to KRT9 Leu458 (predicted a position, three residues
  from the end of Coil 2) contacts the partner in 2 of 5 chains (KRT5 Leu474, KRT1 Leu485).
  (`05_variant_structure_summary.tsv`, `05_variant_structure_map.tsv`)
- S9. The residue equivalent to KRT9 Cys406 (cysteine or alanine in the templates; predicted e
  position immediately after the stutter) makes no contact with the type II partner chain in any
  of five keratin heterodimer chains and is solvent exposed (mean relative accessibility 0.48).
  Together with its population frequency (V9) and low conservation (C2), this sets p.Cys406Arg
  apart from the other EPPK1 variants. (`05_variant_structure_summary.tsv`)
- S10. By structural class, the KRT9 disease missense variants divide into (i) hydrophobic core
  a/d positions (Met157, Leu160, Tyr167, Val171, Tyr454, Leu458; 15 variants), where substitutions
  remove or distort knobs-into-holes packing with the partner chain; (ii) core-flanking e/g
  positions in the helix initiation segment (Asn161, Arg163, Leu168; 11 variants), which are
  invariant in type I keratins but only partly buried in homodimer templates, so their role is
  more likely in heterodimer-specific or higher-order contacts that the available structures do
  not show; (iii) one surface b position hit only by a proline (Gln172); and (iv) one exposed e
  position of doubtful pathogenicity (Cys406). (`03_statistics.json`,
  `05_variant_structure_summary.tsv`)

## Limitations

- **Ascertainment.** EPPK1 diagnostics historically sequenced the 1A-encoding region of KRT9
  first, so the clustering of reported variants in the helix initiation segment is partly a
  reporting bias; the enrichment p-values describe the catalogue, not an unbiased mutational
  scan. The contrast with gnomAD (few, rare missense variants in the segment) and the conservation
  data are independent of that bias.
- **Disease set.** UniProt disease notes and ClinVar classifications were taken as given. Eight
  UniProt EPPK1 variants are not classified pathogenic or likely pathogenic in ClinVar
  (p.Met157Arg, p.Asn161His, p.Arg163Pro and p.Tyr167delinsTrpLeu have records without a
  classification; p.Met157Thr, p.Cys406Arg and p.Leu458Phe are "conflicting"; p.Leu458Pro has no
  ClinVar record). Several ClinVar assertions are single-submitter or without criteria.
- **gnomAD** has no phenotype data; mild or late-onset keratoderma in carriers cannot be excluded,
  and the pLoF counts include variants whose transcript effect is unverified (LOFTEE
  high-confidence calls only were counted). Loss-of-function tolerance is evidence against
  haploinsufficiency but is not a functional demonstration of a dominant-negative effect.
- **Heptad register.** Assigned from hydrophobic periodicity alone. It is validated against
  crystal structures for KRT9 200-299 and 355-460 only; for Coil 1A the validation rests on
  non-keratin homodimers. The one-residue "skip" reported after residue 342 lies in the region
  classically called linker L2/coil 2A, where a simple heptad model is known to be inadequate, and
  should not be over-read. UniProt gives a single "Coil 2" for KRT9, so no 2A/L2/2B boundaries
  were used.
- **Templates.** There is no experimental KRT9 structure and no heterodimer structure of any
  keratin coil 1A. Coil 1A contacts were read from lamin A and vimentin homodimers (45-53%
  identity); a type I/type II heterodimer may differ, particularly at the e/g positions (Asn161,
  Arg163, Leu168), and the type II partner residues are unknown. Template residues differ from KRT9
  at some sites (Met157 is Leu, Leu168 is Ile, Gln172 is Arg in the templates). Contacts were
  measured within the asymmetric unit only; crystal-symmetry contacts, tetramer (A11, A22, A12) and
  filament-level interactions were not analysed, and several templates carry engineered capping or
  stabilising mutations.
- **No complex modelling.** AlphaFold-Multimer was not available, so no model of the KRT9
  heterodimer with a type II partner (for example KRT1) was built; the AlphaFold monomer model
  was used only for per-residue confidence.
- **Alignments.** The glycine-rich head and tail align poorly; conservation values there (and for
  Tyr558) are unreliable. PANTHER orthologs include unreviewed and partial sequences (9 of the 10
  cover the end of Coil 2).
- **Snapshot.** ClinVar, gnomAD and PDB contents change; all numbers describe the retrieval
  recorded in `data/manifest.json`.

## Key tables

Generated by `06_report_tables.py` from the result files (also in `results/06_tables.md`).

### T1 Domain architecture and composition (01_KRT9_domains.tsv)

| domain | start | end | length | pct_G | pct_S | pct_G_plus_S | pct_aromatic_FYW | pct_charged_DEKR | shannon_entropy_bits | top_residues |
|---|---|---|---|---|---|---|---|---|---|---|
| Head | 1 | 152 | 152 | 48 | 21.7 | 69.7 | 13.2 | 5.92 | 2.44 | G:73,S:33,F:13,R:8 |
| Coil 1A | 153 | 188 | 36 | 0 | 8.33 | 8.33 | 5.56 | 33.3 | 3.64 | E:5,L:5,N:4,K:3 |
| Linker 1 | 189 | 207 | 19 | 5.26 | 5.26 | 10.5 | 21.1 | 21.1 | 3.26 | Y:4,K:3,P:2,A:2 |
| Coil 1B | 208 | 299 | 92 | 3.26 | 2.17 | 5.43 | 3.26 | 34.8 | 3.77 | L:14,D:12,E:9,K:7 |
| Linker 12 | 300 | 322 | 23 | 13 | 4.35 | 17.4 | 0 | 21.7 | 3.52 | T:3,G:3,N:3,V:3 |
| Coil 2 | 323 | 461 | 139 | 3.6 | 7.91 | 11.5 | 3.6 | 29.5 | 3.78 | E:22,Q:19,L:16,I:11 |
| Tail | 462 | 623 | 162 | 56.8 | 22.2 | 79 | 6.79 | 8.03 | 2.08 | G:92,S:36,Y:9,E:5 |
| full length | 1 | 623 | 623 | 28.4 | 14 | 42.4 | 7.22 | 18.6 | 3.61 | G:177,S:87,E:42,L:41 |

### T2 Coiled-coil register per coil segment (01_KRT9_architecture.json)

| segment | start | end | length | n_core_positions | core_fraction_apolar_LIVMFAYWC | n_discontinuities |
|---|---|---|---|---|---|---|
| Coil 1A | 153 | 188 | 36 | 11 | 0.818 | 0 |
| Coil 1B | 208 | 299 | 92 | 27 | 0.704 | 0 |
| Coil 2 | 323 | 461 | 139 | 40 | 0.75 | 2 |

| segment | after_residue | before_residue | position_before | position_after | residues_to_insert_to_restore_heptad | class | residues_from_segment_end | context |
|---|---|---|---|---|---|---|---|---|
| Coil 2 | 342 | 343 | b | b | 1 | skip (1-residue insertion equivalent) | 119 | KNRKDIENQYETQI |
| Coil 2 | 405 | 406 | a | e | 4 | stutter (4-residue insertion / 3-residue deletion equivalent) | 56 | EDTKNRYCGQLQMI |

### T3 Disease-set variants (02_variants_merged.tsv, 04_conservation_per_residue.tsv)

| variant | ref check | domain | heptad | offset from 1A start | offset to coil 2 end | UniProt disease | ClinVar classification | ClinVar review status | gnomAD AC | gnomAD AF | type I identity | ortholog identity | other keratin genes with disease variant at column | sources |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| p.Met157Arg | OK | Coil 1A | a | 4 | 304 | EPPK1 | not provided | no classification provided | 0 |  | 1 | 1 | 8 | ClinVar;UniProt |
| p.Met157Lys | OK | Coil 1A | a | 4 | 304 | EPPK1 | Pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 8 | ClinVar;UniProt |
| p.Met157Thr | OK | Coil 1A | a | 4 | 304 | EPPK1 | Conflicting classifications of pathogenicity | criteria provided, conflicting classifications | 0 |  | 1 | 1 | 8 | ClinVar;UniProt |
| p.Met157Val | OK | Coil 1A | a | 4 | 304 | EPPK1 | Pathogenic | criteria provided, multiple submitters, no conflicts | 0 |  | 1 | 1 | 8 | ClinVar;UniProt |
| p.Leu160Phe | OK | Coil 1A | d | 7 | 301 | EPPK1 | Pathogenic | no assertion criteria provided | 0 |  | 1 | 1 | 7 | ClinVar;UniProt |
| p.Leu160Pro | OK | Coil 1A | d | 7 | 301 | - | Likely pathogenic | criteria provided, multiple submitters, no conflicts | 0 |  | 1 | 1 | 7 | ClinVar |
| p.Leu160Val | OK | Coil 1A | d | 7 | 301 | EPPK1 | Likely pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 7 | ClinVar;UniProt |
| p.Asn161His | OK | Coil 1A | e | 8 | 300 | EPPK1 | not provided | no classification provided | 0 |  | 1 | 1 | 11 | ClinVar;UniProt |
| p.Asn161Ile | OK | Coil 1A | e | 8 | 300 | EPPK1 | Pathogenic | no assertion criteria provided | 0 |  | 1 | 1 | 11 | ClinVar;UniProt |
| p.Asn161Lys | OK | Coil 1A | e | 8 | 300 | EPPK1 | Pathogenic/Likely pathogenic | criteria provided, multiple submitters, no conflicts | 0 |  | 1 | 1 | 11 | ClinVar;UniProt |
| p.Asn161Ser | OK | Coil 1A | e | 8 | 300 | EPPK1 | Pathogenic | criteria provided, multiple submitters, no conflicts | 2 | 1.37e-06 | 1 | 1 | 11 | ClinVar;UniProt;gnomAD |
| p.Asn161Tyr | OK | Coil 1A | e | 8 | 300 | EPPK1 | Pathogenic | no assertion criteria provided | 0 |  | 1 | 1 | 11 | ClinVar;UniProt |
| p.Arg163Gln | OK | Coil 1A | g | 10 | 298 | EPPK1 | Pathogenic/Likely pathogenic | criteria provided, multiple submitters, no conflicts | 5 | 3.10e-06 | 1 | 1 | 6 | ClinVar;UniProt;gnomAD |
| p.Arg163Gly | OK | Coil 1A | g | 10 | 298 | - | Likely pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 6 | ClinVar |
| p.Arg163Leu | OK | Coil 1A | g | 10 | 298 | - | Pathogenic/Likely pathogenic | criteria provided, multiple submitters, no conflicts | 0 |  | 1 | 1 | 6 | ClinVar |
| p.Arg163Pro | OK | Coil 1A | g | 10 | 298 | EPPK1 | not provided | no classification provided | 0 |  | 1 | 1 | 6 | ClinVar;UniProt |
| p.Arg163Trp | OK | Coil 1A | g | 10 | 298 | EPPK1 | Pathogenic/Likely pathogenic | criteria provided, multiple submitters, no conflicts | 0 |  | 1 | 1 | 6 | ClinVar;UniProt |
| p.Tyr167Asn | OK | Coil 1A | d | 14 | 294 | - | Likely pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 4 | ClinVar |
| p.Tyr167Asp | OK | Coil 1A | d | 14 | 294 | - | Likely pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 4 | ClinVar |
| p.Tyr167Ser | OK | Coil 1A | d | 14 | 294 | - | Likely pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 4 | ClinVar |
| p.Tyr167delinsTrpLeu | OK | Coil 1A | d | 14 | 294 | EPPK1 | not provided | no classification provided | 0 |  | 1 | 1 | 4 | ClinVar;UniProt |
| p.Leu168Ser | OK | Coil 1A | e | 15 | 293 | EPPK1 | Pathogenic | no assertion criteria provided | 0 |  | 1 | 0.8 | 8 | ClinVar;UniProt |
| p.Val171Gly | OK | Coil 1A | a | 18 | 290 | - | Likely pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 4 | ClinVar |
| p.Val171Met | OK | Coil 1A | a | 18 | 290 | EPPK1 | Pathogenic | no assertion criteria provided | 1 | 6.84e-07 | 1 | 1 | 4 | ClinVar;UniProt;gnomAD |
| p.Gln172Pro | OK | Coil 1A | b | 19 | 289 | EPPK1 | Pathogenic | no assertion criteria provided | 0 |  | 0 | 0.7 | 2 | ClinVar;UniProt |
| p.Cys406Arg | OK | Coil 2 | e | 253 | 55 | EPPK1 | Conflicting classifications of pathogenicity | criteria provided, conflicting classifications | 835 | 5.17e-04 | 0.333 | 0.889 | 0 | ClinVar;UniProt;gnomAD |
| p.Tyr454His | OK | Coil 2 | d | 301 | 7 | EPPK1 | Pathogenic | criteria provided, single submitter | 0 |  | 1 | 1 | 5 | ClinVar;UniProt |
| p.Leu458Phe | OK | Coil 2 | a | 305 | 3 | EPPK1 | Conflicting classifications of pathogenicity | criteria provided, conflicting classifications | 6 | 4.10e-06 | 0.889 | 1 | 8 | ClinVar;UniProt;gnomAD |
| p.Leu458Pro | OK | Coil 2 | a | 305 | 3 | EPPK1 | (no ClinVar record) |  | 0 |  | 0.889 | 1 | 8 | UniProt;gnomAD |
| p.Tyr558Ter | OK | Tail |  | 405 | -97 | - | Pathogenic | criteria provided, single submitter | 0 |  |  | 0.7 | 0 | ClinVar |

### T4 Missense variants per domain (03_domain_distribution.tsv)

| domain | length | ClinVar P/LP | UniProt disease | disease set (union) | disease positions | gnomAD missense (not in disease set) | gnomAD missense positions | gnomAD missense AC | gnomAD synonymous | gnomAD in-frame indels | gnomAD in-frame indel AC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Head | 152 | 0 | 0 | 0 | 0 | 243 | 127 | 8614 | 91 | 16 | 35 |
| Coil 1A | 36 | 20 | 17 | 24 | 8 | 27 | 18 | 547 | 19 | 0 | 0 |
| Linker 1 | 19 | 0 | 0 | 0 | 0 | 26 | 14 | 362 | 9 | 2 | 10 |
| Coil 1B | 92 | 0 | 0 | 0 | 0 | 114 | 62 | 1425 | 34 | 0 | 0 |
| Linker 12 | 23 | 0 | 0 | 0 | 0 | 31 | 20 | 222 | 12 | 0 | 0 |
| Coil 2 | 139 | 1 | 4 | 4 | 3 | 171 | 107 | 7146 | 74 | 0 | 0 |
| Tail | 162 | 0 | 0 | 0 | 0 | 193 | 123 | 2090 | 85 | 18 | 1115 |
| full length | 623 | 21 | 21 | 28 | 11 | 805 | 471 | 20406 | 324 | 36 | 1160 |

### T5 Enrichment tests (03_enrichment_tests.tsv)

| case_set | level | region | region_length | case_in | case_out | control_in | control_out | fisher_odds_ratio | fisher_p_two_sided | binomial_p_vs_length_fraction_greater |
|---|---|---|---|---|---|---|---|---|---|---|
| disease | variants | helix initiation segment (first 20 of Coil 1A) | 20 | 24 | 4 | 11 | 794 | 433 | 5.64e-34 | 2.59e-32 |
| disease | positions | helix initiation segment (first 20 of Coil 1A) | 20 | 8 | 3 | 6 | 463 | 206 | 7.27e-12 | 1.71e-10 |
| disease | variants | helix termination segment (last 20 of Coil 2) | 20 | 3 | 25 | 21 | 784 | 4.48 | 0.0429 | 0.0597 |
| disease | positions | helix termination segment (last 20 of Coil 2) | 20 | 2 | 9 | 14 | 455 | 7.22 | 0.0481 | 0.0468 |
| disease | variants | both boundary segments (20+20 residues) | 40 | 27 | 1 | 32 | 773 | 652 | 3.02e-33 | 1.67e-31 |
| disease | positions | both boundary segments (20+20 residues) | 40 | 10 | 1 | 20 | 449 | 224 | 1.95e-12 | 1.23e-11 |
| disease | variants | Coil 1A (whole) | 36 | 24 | 4 | 27 | 778 | 173 | 2.87e-28 | 3.13e-26 |
| disease | positions | Coil 1A (whole) | 36 | 8 | 3 | 17 | 452 | 70.9 | 2.45e-09 | 1.75e-08 |
| disease | variants | rod coils (1A+1B+2) | 267 | 28 | 0 | 312 | 493 | inf | 6.40e-12 | 4.97e-11 |
| disease | positions | rod coils (1A+1B+2) | 267 | 11 | 0 | 185 | 284 | inf | 4.44e-05 | 8.96e-05 |
| disease | variants | heptad a/d positions of rod coils | 78 | 15 | 13 | 93 | 712 | 8.83 | 1.73e-07 | 2.16e-07 |
| disease | positions | heptad a/d positions of rod coils | 78 | 6 | 5 | 51 | 418 | 9.84 | 6.28e-04 | 0.00101 |
| clinvar_plp | variants | helix initiation segment (first 20 of Coil 1A) | 20 | 20 | 1 | 11 | 796 | 1447 | 2.35e-31 | 2.75e-29 |
| clinvar_plp | positions | helix initiation segment (first 20 of Coil 1A) | 20 | 8 | 1 | 6 | 465 | 620 | 4.05e-13 | 9.86e-12 |
| clinvar_plp | variants | helix termination segment (last 20 of Coil 2) | 20 | 1 | 20 | 22 | 785 | 1.78 | 0.451 | 0.496 |
| clinvar_plp | positions | helix termination segment (last 20 of Coil 2) | 20 | 1 | 8 | 15 | 456 | 3.8 | 0.265 | 0.255 |
| clinvar_plp | variants | both boundary segments (20+20 residues) | 40 | 21 | 0 | 33 | 774 | inf | 1.81e-27 | 9.10e-26 |
| clinvar_plp | positions | both boundary segments (20+20 residues) | 40 | 9 | 0 | 21 | 450 | inf | 4.14e-12 | 1.85e-11 |
| clinvar_plp | variants | Coil 1A (whole) | 36 | 20 | 1 | 27 | 780 | 578 | 2.65e-26 | 3.42e-24 |
| clinvar_plp | positions | Coil 1A (whole) | 36 | 8 | 1 | 17 | 454 | 214 | 1.43e-10 | 1.06e-09 |
| clinvar_plp | variants | rod coils (1A+1B+2) | 267 | 21 | 0 | 314 | 493 | inf | 3.80e-09 | 1.87e-08 |
| clinvar_plp | positions | rod coils (1A+1B+2) | 267 | 9 | 0 | 187 | 284 | inf | 2.82e-04 | 4.88e-04 |
| clinvar_plp | variants | heptad a/d positions of rod coils | 78 | 11 | 10 | 94 | 713 | 8.34 | 9.80e-06 | 1.24e-05 |
| clinvar_plp | positions | heptad a/d positions of rod coils | 78 | 5 | 4 | 52 | 419 | 10.1 | 0.00173 | 0.0025 |
| uniprot | variants | helix initiation segment (first 20 of Coil 1A) | 20 | 17 | 4 | 11 | 794 | 307 | 1.32e-24 | 2.16e-22 |
| uniprot | positions | helix initiation segment (first 20 of Coil 1A) | 20 | 7 | 3 | 6 | 463 | 180 | 1.81e-10 | 3.87e-09 |
| uniprot | variants | helix termination segment (last 20 of Coil 2) | 20 | 3 | 18 | 21 | 784 | 6.22 | 0.0203 | 0.0286 |
| uniprot | positions | helix termination segment (last 20 of Coil 2) | 20 | 2 | 8 | 14 | 455 | 8.12 | 0.0403 | 0.0391 |
| uniprot | variants | both boundary segments (20+20 residues) | 40 | 20 | 1 | 32 | 773 | 483 | 3.57e-25 | 2.79e-23 |
| uniprot | positions | both boundary segments (20+20 residues) | 40 | 9 | 1 | 20 | 449 | 202 | 2.84e-11 | 1.75e-10 |
| uniprot | variants | Coil 1A (whole) | 36 | 17 | 4 | 27 | 778 | 122 | 3.91e-20 | 4.27e-18 |
| uniprot | positions | Coil 1A (whole) | 36 | 7 | 3 | 17 | 452 | 62 | 3.43e-08 | 2.21e-07 |
| uniprot | variants | rod coils (1A+1B+2) | 267 | 21 | 0 | 312 | 493 | inf | 3.52e-09 | 1.87e-08 |
| uniprot | positions | rod coils (1A+1B+2) | 267 | 10 | 0 | 185 | 284 | inf | 1.09e-04 | 2.09e-04 |
| uniprot | variants | heptad a/d positions of rod coils | 78 | 10 | 11 | 93 | 712 | 6.96 | 6.47e-05 | 8.91e-05 |
| uniprot | positions | heptad a/d positions of rod coils | 78 | 5 | 5 | 51 | 418 | 8.2 | 0.00293 | 0.00449 |

#### T5b Window-size sensitivity, disease set, variant level

| region | region_length | case_in | case_out | control_in | control_out | fisher_odds_ratio | fisher_p_two_sided | binomial_p_vs_length_fraction_greater |
|---|---|---|---|---|---|---|---|---|
| helix initiation segment (first 10 of Coil 1A) | 10 | 12 | 16 | 10 | 795 | 59.6 | 7.62e-14 | 7.01e-15 |
| helix termination segment (last 10 of Coil 2) | 10 | 3 | 25 | 9 | 796 | 10.6 | 0.00612 | 0.01 |
| helix initiation segment (first 15 of Coil 1A) | 15 | 20 | 8 | 11 | 794 | 180 | 2.81e-26 | 1.11e-26 |
| helix termination segment (last 15 of Coil 2) | 15 | 3 | 25 | 13 | 792 | 7.31 | 0.0142 | 0.0292 |
| helix initiation segment (first 20 of Coil 1A) | 20 | 24 | 4 | 11 | 794 | 433 | 5.64e-34 | 2.59e-32 |
| helix termination segment (last 20 of Coil 2) | 20 | 3 | 25 | 21 | 784 | 4.48 | 0.0429 | 0.0597 |
| helix initiation segment (first 25 of Coil 1A) | 25 | 24 | 4 | 17 | 788 | 278 | 1.99e-31 | 5.32e-30 |
| helix termination segment (last 25 of Coil 2) | 25 | 3 | 25 | 26 | 779 | 3.6 | 0.0692 | 0.101 |
| helix initiation segment (first 30 of Coil 1A) | 30 | 24 | 4 | 24 | 781 | 195 | 4.09e-29 | 4.09e-28 |
| helix termination segment (last 30 of Coil 2) | 30 | 3 | 25 | 30 | 775 | 3.1 | 0.0945 | 0.15 |

### T6 gnomAD constraint (03_statistics.json)

| metric | value |
|---|---|
| pLI | 5.47e-08 |
| oe_lof | 0.661 |
| oe_lof_lower | 0.503 |
| oe_lof_upper | 0.88 |
| obs_lof | 34 |
| exp_lof | 51.4 |
| lof_z | 2.06 |
| oe_mis | 0.953 |
| oe_mis_lower | 0.898 |
| oe_mis_upper | 1.01 |
| obs_mis | 753 |
| exp_mis | 790 |
| mis_z | 0.566 |
| oe_syn | 1.01 |
| obs_syn | 292 |
| exp_syn | 290 |
| syn_z | -0.0821 |

| set | n_variants | total_allele_count | cumulative_allele_frequency | homozygotes | max_af | max_af_variant | by_consequence |
|---|---|---|---|---|---|---|---|
| plof_HC_pass | 84 | 247 | 2.33e-04 | 1 | 2.05e-05 | 17-41568626-TG-T | frameshift_variant:42, splice_acceptor_variant:6, splice_donor_variant:10, stop_gained:26 |
| plof_HC_pass_without_loftee_flags | 79 | 237 | 2.20e-04 | 1 | 2.05e-05 | 17-41568626-TG-T | frameshift_variant:40, splice_acceptor_variant:6, splice_donor_variant:10, stop_gained:23 |

ClinVar truncating records:

| variant | domain | classification | review_status | conditions | gnomad_ac |
|---|---|---|---|---|---|
| p.Lys170Ter | Coil 1A | not provided | no classification provided | not provided | 0 |
| p.Asn303fs | Linker 12 | Uncertain significance | criteria provided, single submitter | not provided | 0 |
| p.Glu381Ter | Coil 2 | Uncertain significance | no assertion criteria provided | Prostate cancer | 0 |
| p.Gln428Ter | Coil 2 | Uncertain significance | criteria provided, single submitter | Epidermolytic palmoplantar keratoderma, 1 | 0 |
| p.His550fs | Tail | Uncertain significance | no assertion criteria provided | not provided | 0 |
| p.Tyr558Ter | Tail | Pathogenic | criteria provided, single submitter | not provided | 0 |
| p.Gly584fs | Tail | Uncertain significance | criteria provided, single submitter | not provided | 0 |

Disease-set variants present in gnomAD:

| variant | gnomad_ac | gnomad_af | gnomad_homozygotes | clinvar |
|---|---|---|---|---|
| p.Asn161Ser | 2 | 1.37e-06 | 0 | Pathogenic |
| p.Arg163Gln | 5 | 3.10e-06 | 0 | Pathogenic/Likely pathogenic |
| p.Val171Met | 1 | 6.84e-07 | 0 | Pathogenic |
| p.Cys406Arg | 835 | 5.17e-04 | 5 | Conflicting classifications of pathogenicity |
| p.Leu458Phe | 6 | 4.10e-06 | 0 | Conflicting classifications of pathogenicity |

Ten most frequent gnomAD missense variants:

| variant | domain | gnomad_ac | gnomad_af | clinvar | disease_set |
|---|---|---|---|---|---|
| p.Ser82Asn | Head | 5419 | 0.00336 | Likely benign | no |
| p.Arg374Trp | Coil 2 | 3780 | 0.00234 | Conflicting classifications of pathogenicity | no |
| p.Ser366Gly | Coil 2 | 1317 | 8.16e-04 | Conflicting classifications of pathogenicity | no |
| p.Cys406Arg | Coil 2 | 835 | 5.17e-04 | Conflicting classifications of pathogenicity | yes |
| p.Arg233Cys | Coil 1B | 634 | 3.93e-04 | Conflicting classifications of pathogenicity | no |
| p.Asp180Glu | Coil 1A | 455 | 2.82e-04 | Benign/Likely benign | no |
| p.Arg34His | Head | 342 | 2.12e-04 | Uncertain significance | no |
| p.Gly507Arg | Tail | 331 | 2.09e-04 | Uncertain significance | no |
| p.Gly507Val | Tail | 331 | 2.09e-04 | Uncertain significance | no |
| p.Arg446Trp | Coil 2 | 295 | 1.83e-04 | Uncertain significance | no |

### T7 Conservation by region (04_region_conservation.tsv)

| region | n_residues | mean_typeI_identity | mean_all_keratin_identity | mean_ortholog_identity | n_invariant_in_typeI | n_positions_with_other_keratin_disease_variant |
|---|---|---|---|---|---|---|
| helix initiation segment (first 20 of Coil 1A) | 20 | 0.744 | 0.589 | 0.86 | 10 | 18 |
| helix termination segment (last 20 of Coil 2) | 20 | 0.61 | 0.573 | 0.783 | 6 | 13 |
| other rod coil residues | 227 | 0.482 | 0.354 | 0.786 | 21 | 30 |
| disease-variant positions | 12 | 0.838 | 0.607 | 0.924 | 8 | 10 |
| Head | 152 | 0.33 | 0.302 | 0.75 | 9 | 15 |
| Coil 1A | 36 | 0.678 | 0.542 | 0.806 | 15 | 27 |
| Linker 1 | 19 | 0.324 | 0.21 | 0.647 | 0 | 1 |
| Coil 1B | 92 | 0.523 | 0.386 | 0.804 | 10 | 5 |
| Linker 12 | 23 | 0.411 | 0.292 | 0.813 | 1 | 8 |
| Coil 2 | 139 | 0.459 | 0.348 | 0.778 | 12 | 29 |
| Tail | 162 | 0.286 | 0.265 | 0.719 | 23 | 3 |

### T8 Conservation and cross-keratin disease variants at disease-set positions (04_variant_conservation.tsv)

| position | residue | heptad | typeI_identity | typeI_residue_counts | ortholog_identity | ortholog_residue_counts | aligned_residues_other_keratins | n_other_keratin_genes_with_disease_variant_at_column | hotspot_rank_by_genes | other_keratin_disease_variants |
|---|---|---|---|---|---|---|---|---|---|---|
| 157 | M | a | 1 | M:27 | 1 | M:10 | KRT10:M,KRT14:M,KRT16:M,KRT17:M,KRT12:M,KRT1:I,KRT5:I | 8 | 3 | KRT14:M119I(EBS1C);KRT14:M119T(EBS1A);KRT14:M119V(EBS1B and EBS1C);KRT6A:I167N(PC3);KRT16:M121T(PC1);KRT10:M150R(EHK2A);KRT10:M150T(EHK2A);KRT13:M108T(WSN2);KRT2:I182N(IBS);KRT17:M88K(PC2);KRT17:M88T(PC2 and SM);KRT12:M129T(MECD1);KRT12:M129V(MECD1) |
| 160 | L | d | 1 | L:27 | 1 | L:10 | KRT10:L,KRT14:L,KRT16:L,KRT17:L,KRT12:L,KRT1:L,KRT5:L | 7 | 6 | KRT14:L122F(EBS1A and EBS1B);KRT6A:L170F(PC3);KRT16:L124H(PC1);KRT16:L124P(PC1);KRT16:L124R(PC1);KRT13:L111P(WSN2);KRT5:L175F(EBS2A);KRT17:L91P(PC2);KRT12:L132P(MECD1);KRT12:L132V(MECD1) |
| 161 | N | e | 1 | N:27 | 1 | N:10 | KRT10:N,KRT14:N,KRT16:N,KRT17:N,KRT12:N,KRT1:N,KRT5:N | 11 | 1 | KRT86:N114D(MNLIX1);KRT86:N114H(MNLIX1);KRT14:N123K(EBS1A);KRT14:N123S(EBS1A);KRT6A:N171D(PC3);KRT6A:N171K(PC3);KRT6A:N171S(PC3);KRT6A:N171Y(PC3);KRT6A:171(PC3);KRT1:N188K(EHK1);KRT1:N188S(EHK1);KRT1:N188T(EHK1);KRT16:N125D(PC1);KRT16:N125G(PC1);KRT16:N125S(FNEPPK1 and PC1);KRT10:N154H(EHK2A);KRT13:N112S(WSN2);KRT5:N176S(EBS2A);KRT2:N186D(IBS);KRT2:N186K(IBS);KRT2:N186Y(IBS);KRT17:N92D(PC2);KRT17:N92H(SM);KRT17:N92S(PC2);KRT74:N148K(ADWH) |
| 163 | R | g | 1 | R:27 | 1 | R:10 | KRT10:R,KRT14:R,KRT16:R,KRT17:R,KRT12:R,KRT1:Q,KRT5:K | 6 | 8 | KRT14:R125C(EBS1A);KRT14:R125G(EBS1A);KRT14:R125H(EBS1A);KRT14:R125S(EBS1A);KRT16:R127C(FNEPPK1 and PC1);KRT16:R127P(PC1);KRT10:R156C(EHK2A);KRT10:R156H(EHK2A);KRT10:R156L(EHK2A);KRT10:R156P(EHK2A);KRT10:R156S(EHK2A);KRT13:R114C(WSN2);KRT13:R114H(WSN2);KRT17:R94C(PC2 and SM);KRT17:R94H(SM and PC2);KRT17:R94P(PC2);KRT12:R135G(MECD1);KRT12:R135I(MECD1);KRT12:R135S(MECD1);KRT12:R135T(MECD1) |
| 167 | Y | d | 1 | Y:27 | 1 | Y:10 | KRT10:Y,KRT14:Y,KRT16:Y,KRT17:Y,KRT12:Y,KRT1:F,KRT5:F | 4 | 14 | KRT14:Y129D(EBS1A);KRT10:Y160D(EHK2A);KRT10:Y160N(EHK2A);KRT10:Y160S(EHK2A);KRT13:Y118D(WSN2);KRT17:Y98D(PC2) |
| 168 | L | e | 1 | L:27 | 0.8 | L:8,M:2 | KRT10:L,KRT14:L,KRT16:L,KRT17:L,KRT12:L,KRT1:I,KRT5:I | 8 | 5 | KRT14:L130P(EBS1A);KRT6A:I178N(PC3);KRT16:L132P(PC1);KRT10:L161S(EHK2A);KRT13:L119P(WSN2);KRT5:I183M(EBS2A);KRT5:I183T(EBS2D);KRT17:L99P(PC2);KRT12:L140Q(MECD1);KRT12:L140R(MECD1) |
| 171 | V | a | 1 | V:27 | 1 | V:10 | KRT10:V,KRT14:V,KRT16:V,KRT17:V,KRT12:V,KRT1:V,KRT5:V | 4 | 13 | KRT14:V133L(EBS1C and EBS1B);KRT14:V133M(EBS1C);KRT5:V186E(EBS2C);KRT5:V186L(EBS2B);KRT5:V186M(EBS2B);KRT17:V102M(PC2);KRT12:V143L(MECD1) |
| 172 | Q | b | 0 | R:25,H:2 | 0.7 | Q:7,R:2,L:1 | KRT10:R,KRT14:R,KRT16:R,KRT17:R,KRT12:R,KRT1:R,KRT5:R | 2 | 24 | KRT14:R134P(EBS1B);KRT5:R187P(EBS2C) |
| 406 | C | e | 0.333 | S:10,C:9,G:3,A:3,V:1,T:1 | 0.889 | C:8,S:1 | KRT10:C,KRT14:C,KRT16:C,KRT17:C,KRT12:C,KRT1:E,KRT5:E | 0 | 86 |  |
| 454 | Y | d | 1 | Y:27 | 1 | Y:9 | KRT10:Y,KRT14:Y,KRT16:Y,KRT17:Y,KRT12:Y,KRT1:Y,KRT5:Y | 5 | 10 | KRT14:Y415C(EBS1C);KRT14:Y415H(EBS1B);KRT6A:Y465H(PC3);KRT6A:Y465S(PC3);KRT1:Y482C(EHK1);KRT10:Y449C(EHK2A);KRT12:Y429C(MECD1);KRT12:Y429D(MECD1) |
| 458 | L | a | 0.889 | L:24,I:3 | 1 | L:9 | KRT10:L,KRT14:L,KRT16:L,KRT17:L,KRT12:L,KRT1:L,KRT5:L | 8 | 4 | KRT86:L410P(MNLIX1);KRT14:L419Q(EBS1A);KRT6A:L469P(PC3);KRT6A:L469R(PC3);KRT1:L486P(EHK1);KRT16:L421P(PC1);KRT2:L484P(IBS);KRT17:L388P(PC2);KRT17:L388R(PC2);KRT12:L433R(MECD1) |
| 558 | Y |  |  |  | 0.7 | Y:7,S:1,G:1,V:1 | KRT10:-,KRT14:-,KRT16:-,KRT17:-,KRT12:-,KRT1:-,KRT5:- | 0 |  |  |

#### T8b Alignment columns with disease variants in the most keratin genes (04_hotspot_columns.tsv)

| rank_by_genes | KRT9_position | KRT9_residue | KRT9_domain | n_keratin_genes_with_disease_variant | n_disease_variants | genes |
|---|---|---|---|---|---|---|
| 1 | 161 | N | Coil 1A | 12 | 30 | KRT1;KRT10;KRT13;KRT14;KRT16;KRT17;KRT2;KRT5;KRT6A;KRT74;KRT86;KRT9 |
| 2 | 463 | E | Tail | 10 | 12 | KRT14;KRT2;KRT3;KRT5;KRT6A;KRT6B;KRT6C;KRT81;KRT83;KRT86 |
| 3 | 157 | M | Coil 1A | 9 | 17 | KRT10;KRT12;KRT13;KRT14;KRT16;KRT17;KRT2;KRT6A;KRT9 |
| 4 | 458 | L | Coil 2 | 9 | 12 | KRT1;KRT12;KRT14;KRT16;KRT17;KRT2;KRT6A;KRT86;KRT9 |
| 5 | 168 | L | Coil 1A | 9 | 11 | KRT10;KRT12;KRT13;KRT14;KRT16;KRT17;KRT5;KRT6A;KRT9 |
| 6 | 160 | L | Coil 1A | 8 | 12 | KRT12;KRT13;KRT14;KRT16;KRT17;KRT5;KRT6A;KRT9 |
| 7 | 450 | E | Coil 2 | 8 | 10 | KRT1;KRT14;KRT2;KRT4;KRT5;KRT81;KRT83;KRT86 |
| 8 | 163 | R | Coil 1A | 7 | 23 | KRT10;KRT12;KRT13;KRT14;KRT16;KRT17;KRT9 |
| 9 | 451 | I | Coil 2 | 7 | 11 | KRT1;KRT10;KRT12;KRT14;KRT2;KRT5;KRT6A |
| 10 | 454 | Y | Coil 2 | 6 | 9 | KRT1;KRT10;KRT12;KRT14;KRT6A;KRT9 |
| 11 | 164 | L | Coil 1A | 6 | 9 | KRT13;KRT16;KRT17;KRT5;KRT6A;KRT71 |
| 12 | 166 | S | Coil 1A | 6 | 6 | KRT1;KRT14;KRT16;KRT17;KRT5;KRT6A |
| 13 | 171 | V | Coil 1A | 5 | 8 | KRT12;KRT14;KRT17;KRT5;KRT9 |
| 14 | 167 | Y | Coil 1A | 5 | 7 | KRT10;KRT13;KRT14;KRT17;KRT9 |
| 15 | 457 | L | Coil 2 | 4 | 5 | KRT1;KRT14;KRT6A;KRT86 |

### T9 AlphaFold pLDDT by domain (05_alphafold_plddt_by_domain.tsv)

| domain | start | end | mean_plddt | min_plddt | max_plddt | fraction_plddt_ge_90 | fraction_plddt_ge_70 | fraction_plddt_lt_50 |
|---|---|---|---|---|---|---|---|---|
| Head | 1 | 152 | 34.7 | 26.9 | 64.2 | 0 | 0 | 0.974 |
| Coil 1A | 153 | 188 | 86.3 | 65.9 | 95.8 | 0.444 | 0.972 | 0 |
| Linker 1 | 189 | 207 | 68.5 | 52.6 | 91.1 | 0.0526 | 0.474 | 0 |
| Coil 1B | 208 | 299 | 94.1 | 74.1 | 97.4 | 0.913 | 1 | 0 |
| Linker 12 | 300 | 322 | 52.6 | 32.8 | 82.9 | 0 | 0.13 | 0.522 |
| Coil 2 | 323 | 461 | 92.7 | 62.4 | 97.8 | 0.863 | 0.986 | 0 |
| Tail | 462 | 623 | 38.5 | 29.8 | 59.3 | 0 | 0 | 0.963 |
| full length | 1 | 623 | 62 | 26.9 | 97.8 | 0.355 | 0.443 | 0.507 |

### T10 Templates (05_templates.tsv)

Keratin type I / type II heterodimers:

| template | resolution_A | chain_gene | partner_chain | partner_keratin_gene | partner_description | template_first_resnum | template_last_resnum | target_start | target_end | n_aligned_pairs | identity_to_target | target_domains_covered | n_disease_positions_covered | pubmed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6E2J:B | 2.39 | KRT10 | A | KRT1 | Keratin, type II cytoskeletal 1 | 195 | 294 | 200 | 299 | 100 | 0.64 | Coil 1B:92,Linker 1:8 | 0 | 31036554 |
| 6EC0:B | 2.98 | KRT10 | A | KRT1 | Keratin 1 | 195 | 294 | 200 | 299 | 100 | 0.64 | Coil 1B:92,Linker 1:8 | 0 | 31036554 |
| 4ZRY:A | 3.3 | KRT10 | B | KRT1 | Keratin, type II cytoskeletal 1 | 350 | 455 | 355 | 460 | 106 | 0.557 | Coil 2:106 | 3 | 27595935 |
| 6UUI:X | 2.07 | KRT10 | C | KRT1 | Keratin, type II cytoskeletal 1 | 350 | 455 | 355 | 460 | 106 | 0.547 | Coil 2:106 | 3 | 32226330 |
| 6JFV:A | 2.6 | KRT14 | B | KRT5 | Keratin, type II cytoskeletal 5 | 330 | 419 | 369 | 458 | 90 | 0.589 | Coil 2:90 | 3 | 31995743 |
| 6JFV:C | 2.6 | KRT14 | D | KRT5 | Keratin, type II cytoskeletal 5 | 330 | 421 | 369 | 460 | 92 | 0.598 | Coil 2:92 | 3 | 31995743 |
| 3TNU:A | 3 | KRT14 | B | KRT5 | Keratin, type II cytoskeletal 5 | 332 | 421 | 371 | 460 | 90 | 0.611 | Coil 2:90 | 3 | 22705788 |

Non-keratin IF homodimers aligned without gaps and covering disease-set positions:

| template | resolution_A | chain_gene | partner_chain | partner_keratin_gene | partner_description | template_first_resnum | template_last_resnum | target_start | target_end | n_aligned_pairs | identity_to_target | target_domains_covered | n_disease_positions_covered | pubmed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6YF5:A | 1.83 | LMNA | B |  | Prelamin-A/C,Microtubule-associated protein RP/EB family member 1 | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 | 32645958 |
| 6YF5:B | 1.83 | LMNA | A |  | Prelamin-A/C,Microtubule-associated protein RP/EB family member 1 | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 | 32645958 |
| 6YF5:C | 1.83 | LMNA | D |  | Prelamin-A/C,Microtubule-associated protein RP/EB family member 1 | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 | 32645958 |
| 6YF5:D | 1.83 | LMNA | C |  | Prelamin-A/C,Microtubule-associated protein RP/EB family member 1 | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 | 32645958 |
| 6YSH:A | 2.83 | LMNA | B |  | Prelamin-A/C,Microtubule-associated protein RP/EB family member 1 | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 | 32645958 |
| 6YSH:B | 2.83 | LMNA | A |  | Prelamin-A/C,Microtubule-associated protein RP/EB family member 1 | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 | 32645958 |
| 8I33:A | 1.62 | LMNA | C |  | Prelamin-A/C | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 |  |
| 8I33:B | 1.62 | LMNA | D |  | Prelamin-A/C | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 |  |
| 8I33:C | 1.62 | LMNA | A |  | Prelamin-A/C | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 |  |
| 8I33:D | 1.62 | LMNA | B |  | Prelamin-A/C | 26 | 65 | 148 | 187 | 40 | 0.45 | Coil 1A:35,Head:5 | 8 |  |
| 3G1E:A | 1.83 | VIM | B |  | Vimentin | 102 | 131 | 152 | 181 | 30 | 0.533 | Coil 1A:29,Head:1 | 8 | 19422834 |
| 3G1E:B | 1.83 | VIM | A |  | Vimentin | 102 | 131 | 152 | 181 | 30 | 0.533 | Coil 1A:29,Head:1 | 8 | 19422834 |
| 1GK4:A | 2.3 | VIM | B |  | VIMENTIN | 329 | 406 | 383 | 460 | 78 | 0.295 | Coil 2:78 | 3 | 11889032 |
| 1GK4:B | 2.3 | VIM | A |  | VIMENTIN | 329 | 406 | 383 | 460 | 78 | 0.295 | Coil 2:78 | 3 | 11889032 |
| 1GK4:C | 2.3 | VIM | D |  | VIMENTIN | 339 | 406 | 393 | 460 | 68 | 0.324 | Coil 2:68 | 3 | 11889032 |
| 1GK4:D | 2.3 | VIM | C |  | VIMENTIN | 339 | 406 | 393 | 460 | 68 | 0.324 | Coil 2:68 | 3 | 11889032 |
| 1GK4:E | 2.3 | VIM | F |  | VIMENTIN | 339 | 406 | 393 | 460 | 68 | 0.324 | Coil 2:68 | 3 | 11889032 |
| 1GK4:F | 2.3 | VIM | E |  | VIMENTIN | 339 | 406 | 393 | 460 | 68 | 0.324 | Coil 2:68 | 3 | 11889032 |
| 1GK6:A | 1.9 | VIM | B |  | VIMENTIN | 355 | 406 | 409 | 460 | 52 | 0.288 | Coil 2:52 | 2 | 11889032 |
| 1GK6:B | 1.9 | VIM | A |  | VIMENTIN | 355 | 406 | 409 | 460 | 52 | 0.288 | Coil 2:52 | 2 | 11889032 |

### T11 Predicted heptad position vs observed partner contact (05_heptad_vs_contact.tsv)

| template_set | target_heptad | n_residue_observations | fraction_sidechain_contacting_partner | mean_rsa_in_dimer | mean_rsa_lost_on_dimerisation |
|---|---|---|---|---|---|
| keratin heterodimer | a | 101 | 0.871 | 0.177 | 0.328 |
| keratin heterodimer | b | 94 | 0 | 0.435 | 4.96e-04 |
| keratin heterodimer | c | 94 | 0 | 0.463 | 6.79e-04 |
| keratin heterodimer | d | 90 | 0.922 | 0.131 | 0.349 |
| keratin heterodimer | e | 95 | 0.537 | 0.402 | 0.0829 |
| keratin heterodimer | f | 95 | 0 | 0.485 | 0 |
| keratin heterodimer | g | 99 | 0.596 | 0.363 | 0.0783 |
| keratin heterodimer | a+d | 191 | 0.895 | 0.155 | 0.338 |
| keratin heterodimer | e+g | 194 | 0.567 | 0.382 | 0.0806 |
| keratin heterodimer | b+c+f | 283 | 0 | 0.461 | 3.90e-04 |
| non-keratin IF | a | 321 | 0.869 | 0.174 | 0.304 |
| non-keratin IF | b | 315 | 0.00952 | 0.45 | 0.00132 |
| non-keratin IF | c | 313 | 0.00958 | 0.461 | 0.00203 |
| non-keratin IF | d | 307 | 0.883 | 0.171 | 0.329 |
| non-keratin IF | e | 313 | 0.594 | 0.393 | 0.0876 |
| non-keratin IF | f | 311 | 0 | 0.487 | 0 |
| non-keratin IF | g | 311 | 0.547 | 0.372 | 0.0854 |
| non-keratin IF | a+d | 628 | 0.876 | 0.172 | 0.316 |
| non-keratin IF | e+g | 624 | 0.571 | 0.383 | 0.0865 |
| non-keratin IF | b+c+f | 939 | 0.00639 | 0.466 | 0.00112 |

### T12 Structural context of disease-set positions (05_variant_structure_summary.tsv)

| position | residue | domain | heptad | alphafold_plddt | keratin_template_residues | keratin_n_obs | keratin_n_contact_partner | keratin_mean_rsa_dimer | keratin_n_buried | nonkeratin_template_residues | nonkeratin_n_obs | nonkeratin_n_contact_partner | nonkeratin_mean_rsa_dimer | nonkeratin_n_buried | nonkeratin_n_interchain_salt_bridge | nonkeratin_n_interchain_hbond | nonkeratin_n_intrachain_salt_bridge | structural_class |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 157 | M | Coil 1A | a | 73.3 |  | 0 | 0 |  | 0 | L | 12 | 8 | 0.331 | 4 | 0 | 0 | 0 | interface (side chain contacts partner in majority of templates) |
| 160 | L | Coil 1A | d | 79.7 |  | 0 | 0 |  | 0 | L | 12 | 10 | 0.215 | 8 | 0 | 0 | 0 | interface (side chain contacts partner in majority of templates) |
| 161 | N | Coil 1A | e | 82.8 |  | 0 | 0 |  | 0 | N | 12 | 6 | 0.381 | 0 | 0 | 0 | 0 | interface in a minority of templates |
| 163 | R | Coil 1A | g | 85.6 |  | 0 | 0 |  | 0 | R | 12 | 4 | 0.453 | 0 | 0 | 0 | 5 | interface in a minority of templates |
| 167 | Y | Coil 1A | d | 88.9 |  | 0 | 0 |  | 0 | L;Y | 12 | 12 | 0.235 | 6 | 0 | 0 | 0 | interface (side chain contacts partner in majority of templates) |
| 168 | L | Coil 1A | e | 89.4 |  | 0 | 0 |  | 0 | I | 12 | 9 | 0.283 | 6 | 0 | 0 | 0 | interface (side chain contacts partner in majority of templates) |
| 171 | V | Coil 1A | a | 93.8 |  | 0 | 0 |  | 0 | V | 12 | 12 | 0.0717 | 12 | 0 | 0 | 0 | interface (side chain contacts partner in majority of templates) |
| 172 | Q | Coil 1A | b | 91.6 |  | 0 | 0 |  | 0 | R | 12 | 0 | 0.523 | 0 | 0 | 0 | 7 | no partner contact in any template |
| 406 | C | Coil 2 | e | 96.2 | A;C | 5 | 0 | 0.476 | 0 | A | 6 | 0 | 0.424 | 0 | 0 | 0 | 0 | no partner contact in any template |
| 454 | Y | Coil 2 | d | 86.8 | Y | 5 | 4 | 0.274 | 3 | Y | 8 | 8 | 0.157 | 8 | 0 | 2 | 0 | interface (side chain contacts partner in majority of templates) |
| 458 | L | Coil 2 | a | 78.1 | L | 5 | 2 | 0.549 | 0 | L | 8 | 8 | 0.391 | 0 | 0 | 0 | 0 | interface (side chain contacts partner in majority of templates) |
| 558 | Y | Tail |  | 33.5 |  | 0 | 0 |  | 0 |  | 0 | 0 |  | 0 | 0 | 0 | 0 | no template coverage |

#### T12b Contact partners per position (05_variant_structure_map.tsv; entry, chain:residue)

| position | template_set | n_obs | partner_residues_within_4A | intrachain_salt_bridge_partners | interchain_hbond_candidates |
|---|---|---|---|---|---|
| 157 | non-keratin | 12 | 6YF5 A:L38, 6YF5 B:L38, 6YF5 C:L35, 6YF5 C:L38, 6YF5 D:L35, 8I33 A:D34, 8I33 A:L35, 8I33 B:L35, 8I33 B:L38, 8I33 C:L35, 8I33 C:L38, 8I33 D:L35, 8I33 D:L38 |  |  |
| 160 | non-keratin | 12 | 3G1E A:L110, 3G1E B:F114, 3G1E B:L110, 6YF5 A:L35, 6YF5 A:L38, 6YF5 A:L42, 6YF5 A:N39, 6YF5 B:L35, 6YF5 B:L38, 6YF5 B:L42, 6YF5 B:N39, 6YF5 C:L38, 6YF5 C:N39, 6YF5 D:L35, 6YF5 D:L38, 6YF5 D:N39, 8I33 A:L35, 8I33 A:L38, 8I33 B:L35, 8I33 B:L38, 8I33 B:L42, 8I33 B:N39, 8I33 C:L35, 8I33 C:L38, 8I33 C:L42, 8I33 C:N39, 8I33 D:L35, 8I33 D:L38 |  |  |
| 161 | non-keratin | 12 | 6YF5 A:L38, 6YF5 B:L38, 6YF5 C:L38, 6YF5 D:L38, 8I33 A:L38, 8I33 D:L38 |  |  |
| 163 | non-keratin | 12 | 3G1E B:F114, 6YF5 A:L42, 6YF5 C:L42, 8I33 C:I46, 8I33 C:L42 | 6YF5 B:E37, 6YF5 D:E37, 6YSH A:E37, 6YSH B:E37, 8I33 C:E37 |  |
| 167 | non-keratin | 12 | 3G1E A:F114, 3G1E A:L117, 3G1E B:F114, 3G1E B:L117, 6YF5 A:I46, 6YF5 A:L42, 6YF5 A:V49, 6YF5 B:I46, 6YF5 B:L42, 6YF5 B:V49, 6YF5 C:I46, 6YF5 D:I46, 6YF5 D:L42, 6YSH A:I46, 6YSH B:I46, 8I33 A:I46, 8I33 B:I46, 8I33 B:L42, 8I33 B:V49, 8I33 B:Y45, 8I33 C:I46, 8I33 C:V49, 8I33 D:L42 |  |  |
| 168 | non-keratin | 12 | 6YF5 A:Y45, 6YF5 B:Y45, 6YF5 C:Y45, 6YF5 D:Y45, 6YSH A:Y45, 6YSH B:Y45, 8I33 A:R41, 8I33 A:Y45, 8I33 C:Y45, 8I33 D:Y45 |  |  |
| 171 | non-keratin | 12 | 3G1E A:K120, 3G1E A:V121, 3G1E B:K120, 3G1E B:L117, 3G1E B:V121, 6YF5 A:R48, 6YF5 A:V49, 6YF5 A:Y45, 6YF5 B:R48, 6YF5 B:V49, 6YF5 B:Y45, 6YF5 C:R48, 6YF5 C:V49, 6YF5 C:Y45, 6YF5 D:L52, 6YF5 D:R48, 6YF5 D:V49, 6YF5 D:Y45, 6YSH A:R48, 6YSH A:V49, 6YSH B:R48, 6YSH B:V49, 8I33 A:L52, 8I33 A:V49, 8I33 A:Y45, 8I33 B:V49, 8I33 C:V49, 8I33 C:Y45, 8I33 D:L52, 8I33 D:R48, 8I33 D:V49, 8I33 D:Y45 |  |  |
| 172 | non-keratin | 12 |  | 3G1E A:D119, 3G1E B:E125, 6YF5 B:D47, 6YSH B:E53, 8I33 A:D47, 8I33 B:D47, 8I33 D:D47 |  |
| 406 | keratin | 5 |  |  |  |
| 406 | non-keratin | 6 |  |  |  |
| 454 | keratin | 5 | 3TNU B:I467, 3TNU B:L474, 3TNU B:R471, 3TNU B:Y470, 4ZRY B:I479, 4ZRY B:Y482, 6JFV B:I467, 6JFV B:L474, 6JFV B:R471, 6JFV D:I467, 6JFV D:R471 |  |  |
| 454 | non-keratin | 8 | 1GK4 A:R401, 1GK4 B:R401, 1GK4 C:I397, 1GK4 C:R401, 1GK4 C:Y400, 1GK4 D:I397, 1GK4 D:L404, 1GK4 D:R401, 1GK4 D:Y400, 1GK4 E:I397, 1GK4 E:L404, 1GK4 E:R401, 1GK4 E:Y400, 1GK4 F:L404, 1GK4 F:R401, 1GK4 F:Y400, 1GK6 A:E405, 1GK6 A:L404, 1GK6 A:R401, 1GK6 A:Y400, 1GK6 B:L404, 1GK6 B:R401, 1GK6 B:Y400 |  | 1GK4 OH-F:R401.NE, 1GK6 OH-A:E405.OE2, 1GK6 OH-A:R401.NE |
| 458 | keratin | 5 | 3TNU B:L474, 4ZRY B:L485 |  |  |
| 458 | non-keratin | 8 | 1GK4 A:L404, 1GK4 B:L403, 1GK4 B:L404, 1GK4 B:Y400, 1GK4 C:Y400, 1GK4 D:L403, 1GK4 E:L404, 1GK4 E:Y400, 1GK4 F:L404, 1GK4 F:Y400, 1GK6 A:L404, 1GK6 A:Y400, 1GK6 B:L404, 1GK6 B:Y400 |  |  |

### T0 Data sources (data/manifest.json)

| key | retrieved_utc | release | url |
|---|---|---|---|
| alphafold_P35527 | 2026-11-26T19:08:51Z |  | https://alphafold.ebi.ac.uk/api/prediction/P35527 |
| clinvar_KRT9 | 2026-11-26T19:08:50Z |  | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=KRT9%5Bgene%5D&retmax=10000&retmode |
| experimental_structure_check | 2026-11-26T19:09:33Z |  | search.rcsb.org + www.ebi.ac.uk/pdbe/api/mappings/best_structures |
| gnomad_KRT9 | 2026-11-26T19:08:51Z | gnomad_r4 | https://gnomad.broadinstitute.org/api |
| human_if_family | 2026-11-26T19:09:33Z | 2026_04 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A9606%29+AND+%28reviewed%3Atrue%29+AND+%28fami |
| human_keratins | 2026-11-26T19:08:18Z | 2026_04 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A9606%29+AND+%28reviewed%3Atrue%29+AND+%28fami |
| interpro_P35527 | 2026-11-26T19:08:51Z |  | https://www.ebi.ac.uk/interpro/api/entry/all/protein/uniprot/P35527?page_size=100 |
| panther_orthologs | 2026-11-26T19:08:28Z | 19 | https://pantherdb.org/services/oai/pantherdb/ortholog/matchortho?geneInputList=P35527&organism=9606&orthologTy |
| rcsb_if_entries | 2026-11-26T19:09:34Z |  | https://search.rcsb.org/rcsbsearch/v2/query + https://data.rcsb.org/graphql |
| uniprot_P35527 | 2026-11-26T19:08:17Z | 2026_04 | https://rest.uniprot.org/uniprotkb/P35527.json |

