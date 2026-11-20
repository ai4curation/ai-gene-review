# YTM1 notes

## 2026-10-17

- Deep research did not complete: the Falcon wrapper fell back to the lightweight
  provider but the fresh provider environment had no `agentapi` credentials on
  `PATH`. I therefore used cached primary literature and manual PubMed follow-up.
- `PANTHER:PTN000458086` is the relevant fungal WDR12/YTM1 PAINT node. The
  2024 IBDs place `GO:0030687`, `GO:0070545`, and `GO:0042273` on the fungal
  Ytm1 ancestor; the short donor list and the SGD self-source are expected for
  a PAINT placement grounded by SGD YTM1 evidence.
- The core mechanism is the Nop7-Erb1-Ytm1 subcomplex on 66S/pre-60S
  preribosomes. Miles et al. show that "Ytm1 binds directly to Erb1 and is
  present in a heterotrimeric subcomplex together with Erb1 and Nop7, both
  within preribosomes and independently of preribosomes"
  [PMID:16287855].
- WD40 mutations impair the Erb1 interaction and large-subunit maturation:
  "Mutations in the WD40 motifs of Ytm1 disrupt binding to Erb1, destabilize
  the heterotrimer, and delay pre-rRNA processing and nuclear export of
  preribosomes" [PMID:16287855]. Tang et al. refine the interaction map:
  "assembly of Nop7, Erb1, and Ytm1 into preribosomes is interdependent"
  [PMID:18448671].
- Bassler et al. establish the direct Rea1 remodeling step: "Rea1 induces the
  release of the Ytm1-Erb1-Nop7 subcomplex from the nascent 60S subunit and
  consequently enables this early pre-60S intermediate to exit from the
  nucleolus" [PMID:20542003]. The newer Mitterer et al. structure/function
  paper integrates Spb4 and Rrp17 into the same late-nucleolar transition:
  "The AAA+-ATPase Rea1 participates in the nucleolar exit by releasing the
  Ytm1-Erb1 heterodimer from the evolving pre-60S particle"
  [PMID:36929751].
- I retained `GO:0110136 protein-RNA complex remodeling`: Ytm1 is not the
  ATPase or helicase, but its MIDO/UBL region is the conserved Rea1 handle that
  enables ATP-dependent release of the subcomplex.
- The old `GO:0051276 chromosome organization` IMP row comes from a dosage
  chromosome-stability screen rather than normal Ytm1 mechanism. I marked it
  over-annotated and did not propagate it to the core function.

## ND literature-search citations (2026-11-06)

- existing_annotations[2], GO:0003674 molecular_function (ND, GO_REF:0000015), ACCEPT: the ND may be stale. These notes cite yeast Ytm1 papers showing that Ytm1 binds directly to Erb1 in the Nop7-Erb1-Ytm1 subcomplex (PMID:16287855) and that Rea1 releases the Ytm1-Erb1-Nop7 subcomplex from the nascent 60S particle (PMID:20542003, PMID:36929751); the notes also describe the Ytm1 MIDO/UBL region as the conserved Rea1 handle. Those are direct molecular studies of this gene product in S. cerevisiae, so a curator should decide whether they support an informative MF, such as a structural or adaptor activity within the pre-60S particle, instead of ND. The review's 2026-10-31 re-check judged that an interaction alone identifies no activity. The review action was left unchanged.
