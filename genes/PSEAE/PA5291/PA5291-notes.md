# PA5291 (BetT3, Q9HTR3) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HTR3 --alias PA5291`; accession matches the worklist. No gene
name in UniProt; folder and symbol use the locus tag. No deep-research provider was used.
PMID:18156257 (Chen & Beattie 2008) is abstract-only and no full text could be retrieved.
PMID:21478341 (Malek et al. 2011) is abstract-only in the cache; the full text was read on PMC
(PMC3133218) and quotes marked "full text" are copied verbatim from it.

### Which PAO1 gene is BetT3?

- Malek et al. (full text): "three BCCTs, designated BetT1, BetT2, and BetT3 (PA14_70980, PA14_12990, and PA14_69850, respectively)".
- `PA5291-bioinformatics/` (script `map_pa14_betT.py`, output `output.tsv`): PA14_69850 is 100%
  identical to PAO1 PA5291 (661 aa); PA14_12990 is 100% identical to PAO1 PA3933 (653 aa). So
  BetT3 = PA5291 and BetT2 = PA3933.
- Malek et al. (full text), on the 2008 paper (their ref. 6, = PMID:18156257): "We previously showed that BetT2 and BetT3 transport GB and choline, respectively, and confer osmoprotection when expressed in P. syringae in a hyperosmolar environment ( 6 )."

### Literature on BetT3 (PA5291)

- Chen & Beattie 2008 abstract: [PMID:18156257 "Functional P. putida and P. aeruginosa transporters were identified, and their possession of a long C-terminal tail suggested an osmoregulatory function for this tail"].
- Malek et al. 2011: [PMID:21478341 "BetT3 and CbcXWV, but not BetT1, were sufficient to support growth on choline."];
  [PMID:21478341 "BetT3 was the major choline transporter under hyperosmolar conditions"];
  full text: "Choline transport was decreased by 52% and 80% in the Δ betT1 and Δ betT3 mutants, respectively".
  betT3 is induced by choline and repressed by BetI.

### The PA3933/PA5291 swap in PseudoCAP

PseudoCAP put the Malek et al. BetT3 data (choline transport, choline binding, choline catabolism,
hyperosmotic response) on PA3933, and the Chen & Beattie glycine betaine rows (GB:H+ symporter, GB
transport) on PA5291. With BetT3 = PA5291 and BetT2 = PA3933 these are the wrong way round:

- PA3933 rows citing PMID:21478341 belong to PA5291 (CONFIRMED: full text read plus sequence identity).
  Recorded on `genes/PSEAE/PA3933/`.
- PA5291 rows GO:0015653 and GO:0031460 citing PMID:18156257 most likely describe BetT2 = PA3933
  (PROBABLE: rests on Malek's summary of the 2008 paper; 2008 full text not read). Recorded here, as
  UNDECIDED rows with a PSEUDOCAP defect.
- PA5291 GO:0005275 (PMID:18156257) is consistent with BetT3 choline transport, so it is kept (MODIFY to
  GO:0015220).

### Annotation decisions

- GO:0005275 IDA (seed): MODIFY to GO:0015220. GO:0022857 IBA, IEA: MODIFY to GO:0015220.
- GO:0015653 IDA, GO:0031460 IDA: UNDECIDED + PSEUDOCAP WRONG_GENE_PRODUCT defects (PROBABLE).
- GO:0071475 IDA: KEEP_AS_NON_CORE (osmoprotection by choline uptake; BetT3 is the main choline
  transporter at high osmolarity).
- GO:0015837, GO:0055085 IEA: MODIFY to GO:0015871 choline transport.
- GO:0005886 IBA, IEA: ACCEPT. GO:0016020 IEA: MODIFY to GO:0005886.
- Action counts: MODIFY 6, UNDECIDED 2, KEEP_AS_NON_CORE 1, ACCEPT 2. Source defects: PSEUDOCAP 2
  (PROBABLE).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001247333 | GO:0022857 transmembrane transporter activity | 5 | 34 (19 taxa) | GO:0005275, IDA, PMID:18156257 (PseudoCAP) | SOUND | BetT3 (= PA5291) restored choline transport in a choline-uptake-deficient P. syringae strain (abstract plus Malek full text). Term should be choline transmembrane transporter. | E. coli BetT P0ABC9 and CaiT P31553; BetT1 Q9HTI9 (SOUND); BetT2 Q9HX83 (seed WRONG) | Yes |
| PTN001247333 | (same) | 5 | 34 | GO:0015653 glycine betaine:proton symporter, IDA, PMID:18156257 (PseudoCAP) | WRONG | Most likely BetT2 (PA3933) data attached to PA5291; PROBABLE (2008 full text not read). Does not affect the node term. | as above | Yes |

Node-level: no GO_CENTRAL defect. GO:0022857 suits the BCCT family node, and the IBD rests on two
experimentally characterised E. coli transporters plus BetT1 and BetT3. The PA3933 seed is wrong, but
that only removes one of five seeds.
