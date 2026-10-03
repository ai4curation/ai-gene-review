# grk7a notes (DANRE, Q49HM9)

## 2026-09-28 session log

- Deep research FAILED for this gene (Edison: 402 Payment Required; OpenAI key invalid).
  Not retried. Literature research done by hand via Europe PMC REST searches
  (`grk7a OR grk7b OR "GRK7-1" OR "GRK7-2"`, `GRK7 AND (evolution OR phylogen*)`,
  `grk7b`, `GRK7 AND zebrafish AND (circadian OR UV cone OR paralog)`), and by resolving
  the DOIs cited in `genes/DANRE/grk7b/grk7b-deep-research-falcon.md`.
- Newly cached PMIDs: 34462505, 33579376, 33385424, 29321241, 19720650, 33598728,
  40251282, 39925416, 18803695, 40869203, 22442725, 37190066, 39531499, 26246494, 34550876.
- GOA-cited PMIDs 16039565, 16787417, 21299656 are abstract-only in the cache;
  30372740 and 36273582 are full text.

## Naming (map every name before using it as evidence)

| Name in literature | ZFIN gene | Evidence |
|---|---|---|
| GRK7-1, zGRK7-1, Grk7a | grk7a | UniProt Q49HM9 synonym `grk7-1`; EMBL AB212995 (Wada 2006) on Q49HM9 |
| GRK7-2, zGRK7-2, Grk7b | grk7b | UniProt Q1XHL7 synonym `grk7-2`; EMBL AB212996 (Wada 2006) on Q1XHL7 |
| GRK7a (Rinner 2005) | grk7a | EMBL AY900004 (Rinner 2005) is on Q49HM9; the pineal paper uses AY900004 as its GRK7a probe [PMID:33579376 "GRK7a (bases 60 to 1060 of the coding sequence, accession number, AY900004), and GRK7b (bases 60 to 1059 of the coding sequence, accession number, AB212996)"] |
| GRK1A / Grk1a | grk1a (rod kinase) | not this pair |
| GRK1B / Grk1b | grk1b (cone kinase) | not this pair |

Caution: several antibodies ("anti-Grk7", anti-carp GRK7, anti-pGRK7) recognise both
Grk7 paralogs, so "Grk7" immunoreactivity is not paralog-resolved unless a knockout or
knockdown control is used.

## Key facts with provenance

### Molecular function
- Recombinant GRK7-1 (grk7a) phosphorylates light-activated rhodopsin with very high Vmax:
  [PMID:16787417 "The recombinant GRKs phosphorylated light-activated rhodopsin, and the Vmax value of the major cone subtype, GRK7-1, was 32-fold higher than that of the rod kinase, GRK1A."]
- GRK7-2 (grk7b) is much slower (secondary citation of Wada 2006 by the same group):
  [PMID:33579376 "A previous comparison of the initial rates of rhodopsin phosphorylation by recombinant GRKs in zebrafish revealed that rhodopsin phosphorylation activity of GRK7a (GRK7–1) is more than 30-fold faster than those of GRK1a, GRK1b, and GRK7b (GRK7–2 [29])."]
- UniProt: KM=4.4 uM for rhodopsin, Vmax 773 nmol/min/mg (grk7a-uniprot.txt, from PMID:16787417).
- Both copies keep the PKA site (grk7a KKRRRS33; grk7b KKRRCS33) and a C-terminal CAAX
  geranylgeranylation motif (grk7a ...CTLL, grk7b ...CTLL); sequence inspection of the two
  UniProt records.
- The pair is 73% identical:
  [PMID:18803695 "In comparison, the 2 zebrafish GRK7 proteins, zGRK7-1 and zGRK7-2 are only 73% identical at the amino acid level, suggesting their duplication and divergence occurred much earlier."]

### Regulation by cAMP/PKA (grk7a-specific data; grk7b untested)
- [PMID:36273582 "These data suggest that the delay in cone recovery brought about by increased levels of cAMP is mediated by Grk7a rather than Grk1b in zebrafish larvae."]
- [PMID:36273582 "We also used a cone-specific dominant negative PKA transgenic zebrafish to show that PKA is part of the endogenous kinase pathway responsible for Grk7a phosphorylation in response to elevated cAMP."]

### Expression / localization
- Cone outer segments (GRK7-1): [PMID:16787417 "In situ hybridization and immunohistochemical studies localized both GRK1B and GRK7-1 in the cone outer segments and GRK1A in the rod outer segments."]
- All cones vs UV cones only: [PMID:33598728 "grk1a is expressed exclusively in rods, grk1b and grk7a in all cones, and grk7b only in UV cones [152, 196] (unpublished data)."]
- Adult scRNA-seq partition: [PMID:34462505 "Additionally, we found multiple pairs of paralogous genes that were differentially enriched between UV cones (grk7b, cngb3.2, and guca1e) and other cone types (grk7a, cngb3.1, and guca1e.2)."]
- Larval Grk7 protein is essentially all Grk7a: anti-Grk7 recognises both paralogs
  [PMID:30372740 "We generated a rabbit polyclonal antibody that recognizes both paralogs of zebrafish Grk7 (Grk7a and Grk7b)."]
  but [PMID:30372740 "Analysis of grk7a−/− larvae at 5 dpf show undetectable levels of Grk7 compared to wildtype (Fig. 2A, 2B)."]
- Pineal: GRK1b, GRK7a and GRK7b mRNAs all detected in adult pineal
  [PMID:33579376 "We confirmed the expression of these GRKs in the pineal organ of zebrafish via in situ hybridization (Fig. S1)."]
- Both transcripts oscillate with the same circadian phase:
  [PMID:34550876 "Although many ohnologs (paralogs generated in a whole-genome duplication event), such as grk7a and grk7b, share a similar circadian phase or oscillatory amplitude, others, such as rcv1a and rcv1b, show an almost anti-phasic relationship."]
- Recoverin 2b co-localises with Grk1b, Grk7a and Grk7b in double cones (abstract only, PMID:33385424) — note this is at odds with a strictly UV-cone-restricted grk7b.

### Loss of function (grk7a)
- Morpholino (Rinner 2005): [PMID:16039565 "Photoresponse recovery in Grk7a-deficient larvae was delayed in electroretinographic measurements, and temporal contrast sensitivity was reduced, particularly under bright-light conditions."]
- TALEN knockout, PTC allele (7-bp del/6-bp ins, exon 1): modest delay
  [PMID:30372740 "A logarithmic linear regression of the non-saturating portion of the response shows a recovery half-life of 1.7 seconds for wildtype larvae, versus 2.3 and 3.0 seconds for grk1b−/− and grk7a−/− larvae, respectively (Fig. 4B, inset)."]
  [PMID:30372740 "Since the difference between wildtype and each knockout fish is modest, it appears that either GRK is sufficient for adequate cone visual function."]
- Pineal parapinopsin: [PMID:33579376 "We found that GRK7a knockdown slowed recovery of the response of parapinopsin photoreceptor cells, whereas GRK1b knockdown or GRK7b knockdown did not have a remarkable effect"]
- But in a GRK7a-knockdown background grk7b does contribute (pineal):
  [PMID:39925416 "These observations suggest that GRK7b and also presumably GRK1b contribute to the response termination processes in addition to GRK7a in control fish."]
- Ectopic GRK7 in rods (PMID:21486791; abstract does not say which paralog was expressed):
  [PMID:21486791 "exogenous GRK7 in GRK7-tg animals led to lowered rod sensitivity, as occurs in cones, but surprisingly to slower response kinetics."]
  The review PMID:33598728 identifies it as grk7a: [PMID:33598728 "Ectopic expression of cone grk7a in rods resulted in cone-like rod responses [194]."]

### Evolution
- PANTHER v19: TGD_tree, duplication on Neopterygii|Teleostei, 1 shared gar co-ortholog,
  2 medaka co-orthologs (projects/DANRE_DUPLICATION/panther_tgd_pairs.tsv); grk7a is the
  least-diverged ortholog (LDO) of human GRK7.
- [PMID:34462505 "All differentially partitioned genes except for opn1sw1 and opn1sw2 arose during the teleost-specific whole-genome duplication (arr3a/arr3b, cnga3a/cnga3b, grk7a/grk7b, gngt2a/gngt2b, and rcvrn2/rcvrn3) or later"]
- [PMID:19720650 "Teleost fishes have duplicates of both GRK1 and GRK7 that seem to agree with 3R."]
- Tetrapod/jawed-vertebrate GRK7 is single copy after 2R:
  [PMID:29321241 "It is also clear that, following 2R WGD, jawed vertebrates retained two GRK1 isoforms but only a single GRK7, whereas agnathan vertebrates retained two GRK7 isoforms but only a single GRK1."]

## Annotation decisions (summary)

- MF rhodopsin kinase activity (IBA/IDA/IEA): ACCEPT, core.
- MF photoreceptor activity (IMP, Rinner 2005): REMOVE — a knockdown phenotype cannot
  establish a photon-absorbing activity; grk7a is the kinase that inactivates the
  photoreceptor protein, and its catalytic activity is already captured by GO:0050254 (IDA).
- BP photoresponse recovery (IMP x2): ACCEPT, core.
- BP phototransduction, visible light (IMP): ACCEPT (shut-off is part of the cascade).
- BP visual perception (IMP, PMID:21299656): KEEP_AS_NON_CORE.
- Broad kinase IEAs: MODIFY to GO:0050254 (consistent with grk7b review).
- NEW: CC cone photoreceptor outer segment (GO:0120199) from PMID:16787417 IHC.
