# mapre3a / mapre3b protein, expression and synteny comparison

Script: `pair_analysis.py` (run from the repo root with
`uv run python genes/DANRE/mapre3a/mapre3a-bioinformatics/pair_analysis.py > genes/DANRE/mapre3a/mapre3a-bioinformatics/output.txt`).
Raw output: `output.txt` (run 2026-09-28). Zebrafish sequences come from the cached UniProt
records used for the reviews (mapre3a A0A8M2B5B2, 273 aa, RefSeq XP_005158903.1; mapre3b
A0A8M9Q0D6, 278 aa, RefSeq XP_021330664.2) plus the RefSeq NP isoforms (Q4V903, 259 aa;
Q6GMJ3, 262 aa). Human MAPRE1/2/3 come from UniProt; gar and medaka proteins are the Ensembl
canonical proteins of the orthologues that Ensembl Compara assigns. Alignments: Biopython global,
BLOSUM62, gap -10/-0.5; identity = identical columns / alignment length.

## Orthology (Ensembl Compara)

- mapre3a (ENSDARG00000020231, chr17) and mapre3b (ENSDARG00000102878, chr4) are
  within-species paralogues with the duplication node at Clupeocephala.
- Both have the same single spotted gar orthologue (ENSLOCG00000016310) and the same human
  orthologue (MAPRE3). Each has its own one-to-one medaka orthologue (ENSORLG00000028482 for
  mapre3a, ENSORLG00000017672 for mapre3b), so medaka kept both copies too.

## Protein

| Comparison | Identity |
|---|---|
| mapre3a vs mapre3b (reviewed accessions) | 83.0% (282 columns) |
| mapre3a vs mapre3b (NP isoforms) | 85.6% (264 columns) |
| mapre3a / mapre3b vs human MAPRE3 | 77.9% / 76.6% |
| mapre3a / mapre3b vs human MAPRE1 | 64.1% / 63.9% |
| mapre3a / mapre3b vs gar MAPRE3 orthologue | 72.1% / 71.3% |
| mapre3a / mapre3b vs its own medaka orthologue | 79.7% / 79.6% |

Both copies are MAPRE3 (EB3) orthologues; each is closer to human MAPRE3 than to MAPRE1.

Per region of human MAPRE3 (identical residues / region length):

| Region (UniProt features of Q9UPY8) | mapre3a | mapre3b | gar |
|---|---|---|---|
| Calponin-homology (CH) domain (14-116) | 89.3% | 91.3% | 94.2% |
| EB1 C-terminal (EBH) domain (194-264) | 81.7% | 80.3% | 87.3% |
| APC-binding region (217-260) | 86.4% | 81.8% | 93.2% |
| Disordered linker (157-181) | 52.0% | 52.0% | 60.0% |

C-terminal tails: human MAPRE3 ends in ...QDEY, mapre3a ...LDQDEY, mapre3b ...QDQEEY, gar
...DDQDEY. Both zebrafish copies keep the C-terminal EEY/DEY-type aromatic end of the EB tail.
The two copies differ mainly in the linker between the CH and EBH domains, where mapre3b
(and its XP isoforms) has a few extra residues; the CH domain differs at only a handful of
positions.
Both copies keep the microtubule-binding CH domain, the EBH dimerization/partner-binding domain and the C-terminal aromatic tail.

**Relative rate (gar outgroup).** Of 271 gar positions aligned in both copies, 14 changed only
in mapre3a and 17 only in mapre3b (chi2 = 0.29, not significant). Neither copy is evolving
detectably faster.

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).** mapre3b is maternally supplied
(4-5 TPM in zygote and 2-cell, peaking at 34 TPM at 1k-cell) and stays at 6-14 TPM through
gastrula, segmentation and pharyngula stages, rising to 29-41 TPM in 3-5-day larvae. mapre3a is
at 0 TPM until the 20-25-somite stage and then rises from 2 TPM (prim-5) to 16 TPM (day 5).
mapre3b is maternal and expressed at every stage; mapre3a is zygotic and switches on only at late segmentation.

**Bgee calls (only "expressed" calls are returned; absence is not proven absence).**
mapre3a has 13 calls, highest in retina (88.8), brain (87.0) and testis (79.2), with lower
scores elsewhere. mapre3b has 20 calls, all 60-96 except granulocyte, highest in brain (95.8),
muscle (94.2), retina (92.8) and heart (91.5), and includes intestine, liver, gill, spleen,
ovarian follicle and pre-gastrula embryo, none of which has a mapre3a call.
Both copies are called in brain and retina; mapre3b has the broader profile with high scores in muscle, heart, gill, intestine and liver.

**Gar (pre-duplication state).** Gar MAPRE3 has 14 calls: brain 94.6, eye 92.6, muscle 85.8,
skin 82.1, larva 81.9, mesonephros 79.3, bone 78.7, heart 77.1, liver 73.8, testis 73.1,
embryo 72.4, gill 68.2, intestine 64.6 and ovary 45.3. So the unduplicated gene is broadly
expressed with neural and eye maxima; the broad mapre3b profile resembles the gar profile more
closely than the narrower, neural/retina/testis-biased mapre3a profile does.

**ZFIN.** No curated wild-type expression for mapre3a; one high-throughput in situ record for
mapre3b with anatomy "unspecified" (ZDB-PUB-040907-1). No published in situ patterns.

## Synteny

mapre3a is on chr17 (36.87 Mb) and mapre3b on chr4 (0.78 Mb). For each copy the script took all
protein-coding genes within 1.5 Mb, asked Ensembl for their zebrafish paralogues with a
teleost-level duplication node (Teleostei, Osteoglossocephalai or Clupeocephala), and checked
where the partner lies.

- **Conserved neighbour:** dpysl5a lies next to mapre3a (chr17:36.90 Mb) and its teleost-level
  paralogue dpysl5b next to mapre3b (chr4:0.80 Mb). This is the only neighbour pair found within
  1.5 Mb in either direction (8 of 34 mapre3a neighbours and 15 of 78 mapre3b neighbours have a
  teleost-level paralogue).
- **Chromosome level:** besides dpysl5, two more teleost-level pairs link the mapre3b region to
  chr17 (tulp4b/tulp4a and crybg1b/crybg1a); none besides dpysl5 links the mapre3a region to chr4.
One conserved neighbour pair (dpysl5a/dpysl5b) flanks both copies, a minimal double-conserved-synteny signal.

## Interpretation

- Protein: both copies keep every feature examined, evolve at similar rates, and are equally
  close to human MAPRE3. No evidence of protein-level divergence.
- Expression: mapre3b is maternal and broad, like gar MAPRE3; mapre3a is zygotic, later and
  more restricted (retina, brain, testis highest). This fits either a partition in which
  mapre3a kept a neural subset, or a decline of mapre3a, and cannot distinguish them without
  cell-resolved data and functional tests. The Bgee calls are thresholded and come from
  different sample sets, so absence of a call is weak evidence.
