# slc7a10a / slc7a10b protein, expression and synteny comparison

Script: `pair_analysis.py slc7a10` (the same script as `genes/DANRE/agxta/agxta-bioinformatics/pair_analysis.py`;
run from the repo root) → `output.txt` (run 2026-09-28). The gar tissue-coverage control is
`genes/DANRE/agxta/agxta-bioinformatics/bgee_gar_coverage.txt`.

Zebrafish sequences come from the cached UniProt records (slc7a10a G8JL19, 511 aa; slc7a10b E7FE11, 517 aa). Human
SLC7A10 (Q9NS82), SLC7A5 (LAT1) and SLC7A8 (LAT2) come from UniProt. Orthologues in other species are the Ensembl
Compara member proteins of the orthologues Compara assigns to each zebrafish copy. Global alignments: Biopython
PairwiseAligner, BLOSUM62, gap open -10 / extend -0.5; identity = identical columns / alignment length.

## Duplication

Ensembl Compara calls slc7a10a / slc7a10b within-species paralogues with the duplication at the
Osteoglossocephalai node and gives one spotted gar gene (ENSLOCG00000001884) as a one-to-many orthologue of both.
Herring, cavefish, pike, cod, medaka, stickleback, fugu and tilapia each have one one-to-one orthologue of each
zebrafish copy (salmon has two of each, from the salmonid duplication); the osteoglossomorph arowana has only an
slc7a10a orthologue in Compara.

## Protein

| Comparison | Identity |
|---|---|
| slc7a10a vs slc7a10b | 77.8% (523 columns) |
| slc7a10a vs human SLC7A10 | 69.0% |
| slc7a10b vs human SLC7A10 | 70.2% |
| slc7a10a / slc7a10b vs human SLC7A8 (LAT2) | 61.7% / 60.3% |
| slc7a10a / slc7a10b vs human SLC7A5 (LAT1) | 47.3% / 45.8% |
| slc7a10a / slc7a10b vs gar SLC7A10 (515 aa) | 78.6% / 80.2% |

Both copies are closer to SLC7A10 than to its nearest paralog SLC7A8, and both have 12 predicted transmembrane
helices (UniProt).

**Functional residues of human Asc-1** (tested by mutagenesis in the cryo-EM study, PMID:38589439) and the
cysteine that forms the disulfide bond to the heavy chain 4F2hc/SLC3A2 (human C154): N52, Y131, I138, C154, F243,
F250, Y253, E257, Y333 and R339 are all identical in slc7a10a, slc7a10b, gar, coelacanth and both medaka
orthologues. No copy has lost a known substrate-site, gating or heavy-chain-linking residue.

**Relative rate (gar outgroup).** Of 508 gar positions aligned in both copies, 42 changed only in slc7a10a and 25
only in slc7a10b (chi2 = 4.31, P<0.05). slc7a10a has evolved somewhat faster.

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).** Both copies are low. slc7a10b is detected from the dome
stage through segmentation (2-6 TPM) and stays at 2-9 TPM; slc7a10a is near zero until hatching and then rises to
19-29 TPM in larvae (protruding mouth to day 5).

**Bgee (only "expressed" calls are returned).** slc7a10a has 21 calls, highest in bone, brain, heart, mesonephros,
larva and head kidney, with further calls in muscle, testis, skin, swim bladder, granulocytes, intestine, gill, spleen,
eye and liver. slc7a10b has 8 calls: brain, testis, gastrula, blastula, head, larva, eye and bone. In the entities
called for both, slc7a10a scores higher except in blastula.

**Gar (pre-duplication state).** Gar SLC7A10 has 8 calls: brain, eye, bone, ovary, larva, embryo, testis and skin.
Bgee samples 14 gar tissues; gar SLC7A10 has no call in heart, intestine, liver, mesonephros, muscle or gill, all of
which are sampled. The gar pattern (brain, eye, bone, gonads, embryo) resembles slc7a10b; slc7a10a is called in
several tissues where gar has no call (heart, mesonephros, muscle, intestine, gill, liver). Mammalian SLC7A10 is
also expressed outside the brain (lung, small intestine, placenta, adipose tissue, kidney), so whether the broad
slc7a10a pattern is a teleost gain or an ancestral pattern that gar does not show cannot be decided from these data.

**ZFIN.** No curated wild-type expression for either copy.

## Synteny

Local synteny is weak. Within 1.5 Mb of each copy only one teleost-level paralogue pair lies near the other copy:
sall1a (near slc7a10a, chr7) and sall1b (near slc7a10b, chr25), found in both directions (`output.txt` section 10). The
two neighbourhoods have otherwise been rearranged, so synteny neither adds much support nor contradicts the tree-based
calls.

## Conclusion

Both copies keep every functional residue of Asc-1 that has been tested, so both are predicted to be
small-neutral-amino-acid exchangers that pair with 4F2hc. They differ in expression: slc7a10a is the broadly
expressed, larval-rising copy, and slc7a10b is low, detected earlier in the embryo, and called mainly in brain,
eye, bone and testis, closer to the gar pattern.
