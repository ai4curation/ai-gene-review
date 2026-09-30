# surA (Chaperone SurA) — Pseudomonas putida KT2440 (PSEPK)

UniProt: Q88QT4 (SURA_PSEPK); OrderedLocusNames PP_0403; 427 AA; Precursor.
Evidence level: PE=3 (Inferred from homology). The UniProt record is annotated
entirely by the HAMAP rule MF_01183 (Chaperone_SurA); the GOA file contains only
IEA annotations (GO_REF:0000002 InterPro, GO_REF:0000120 UniRule, GO_REF:0000002
InterPro2GO). There are no organism-specific experimental publications for the
P. putida protein; functional understanding derives from the well-characterized
E. coli ortholog and from the HAMAP family rule.

## FUNCTION

SurA is the primary periplasmic chaperone for outer membrane protein (OMP)
biogenesis. It binds unfolded OMPs emerging from the Sec translocon and escorts
them across the periplasm to the BAM complex for assembly into the outer membrane.

- [UniProt "Chaperone involved in the correct folding and assembly of outer membrane proteins."]
- [UniProt "Recognizes specific patterns of aromatic residues and the orientation of their side chains, which are found more frequently in integral outer membrane proteins."]
- [UniProt "May act in both early periplasmic and late outer membrane-associated steps of protein maturation."]

SurA additionally possesses peptidyl-prolyl cis-trans isomerase (PPIase / rotamase)
activity (EC 5.2.1.8), a parvulin-type isomerase activity.

- [UniProt "AltName: Full=Peptidyl-prolyl cis-trans isomerase SurA"]
- [UniProt "EC=5.2.1.8"]
- [UniProt "Reaction=[protein]-peptidylproline (omega=180) = [protein]-"]

Domain architecture and the relationship between PPIase and chaperone activity:
the PPIase activity resides only in the second parvulin domain, and this catalytic
activity is dispensable for the chaperone function; the chaperone (holdase) and
porin-recognition activities reside in the N-terminal region and C-terminal tail.

- [UniProt "The PPIase activity resides only in the second parvulin domain."]
- [UniProt "The N-terminal region and the C-terminal tail are necessary and sufficient for the chaperone activity of SurA."]
- [UniProt "The PPIase activity is dispensable for SurA to function as a chaperone."]
- [UniProt "The N-terminal region and the C-terminal tail are also required for porin recognition."]

Feature/domain evidence: two PpiC (parvulin) domains (residues 164–265 and 275–374)
plus an N-terminal SurA_N domain; InterPro signatures include IPR023034 (PPIase_SurA),
IPR000297 (PPIase_PpiC), IPR015391 (SurA_N), and the protein is assigned PANTHER
family PTHR47637 (CHAPERONE SURA).

## SUBCELLULAR LOCATION

SurA is a periplasmic protein bearing a cleavable N-terminal signal peptide
(residues 1–13; chain 14–427). It can associate with the outer membrane.

- [UniProt "SUBCELLULAR LOCATION: Periplasm"]
- [UniProt "Note=Is capable of associating with the outer membrane."]
- [UniProt "SIGNAL          1..13"]

## Curation reasoning summary

- MF core: PPIase activity (GO:0003755) — real enzymatic activity per the family
  rule (EC 5.2.1.8), confirmed in the ortholog; retain as a (secondary) core MF.
- MF core: carrier-holdase activity — SurA binds unfolded OMPs and escorts them across
  the periplasm to BAM while preventing off-pathway misfolding. GO:0051082 is now
  obsolete. GO:0140309 (unfolded protein holdase activity) is carrier-specific and
  fits SurA because its client is delivered to a defined acceptor/location; this is
  unlike an in-situ holdase for which the term would be inappropriate.
- BP: protein folding (GO:0006457) and Gram-negative-bacterium-type cell outer
  membrane assembly (GO:0043165) are well supported and core.
- BP: protein stabilization (GO:0050821) is a broad, mechanistically-implied
  process; keep as non-core.
- CC: periplasmic space (GO:0042597) and outer membrane-bounded periplasmic space
  (GO:0030288). GO:0030288 is the more specific, correct location for a Gram-negative
  periplasmic chaperone; GO:0042597 is its broader parent — keep but mark as
  over-annotated relative to the specific child.
- MF: peptide binding (GO:0042277) is a generic supporting binding term; SurA does
  recognize OMP peptide motifs, but the more informative MF terms are the chaperone
  and PPIase terms. Mark as over-annotated.

## 2026-08-29 dedicated re-review

The current QuickGO export contains seven qualifier-aware signatures, each reviewed
exactly once: two `enables`, three `involved_in`, and two `located_in`. All are IEA;
there are no IBA annotations and therefore no PTN/PAINT node to audit. The PANTHER
family entry is classification evidence, not an IBA provenance claim.

The former author-supplied NEW GO:0051082 row was not a current physical GOA signature.
It reflected a legacy UniRule assignment that remains visible in the UniProt flat file,
but GO:0051082 is obsolete. It was replaced by a NEW GO:0140309 ISS annotation with
the experimentally characterized E. coli SurA (UniProtKB:P0ABZ6) recorded as the
supporting entity. This is an evidence-specific replacement: E. coli SurA is reported
as responsible for "the periplasmic transit of the bulk mass of OMPs to the YaeT
complex" [PMID:17908933], and SurA prevents FhuA misfolding by "stabilizing a dynamic,
unfolded state" during stepwise membrane insertion [PMID:26344570]. These cached
records are abstract-only, so the review uses only their explicit abstract claims and
does not convert them into direct P. putida evidence.

The seven current GOA decisions remain four ACCEPT, two MARK_AS_OVER_ANNOTATED, and
one KEEP_AS_NON_CORE. The extra author-supplied current-term proposal is one NEW.
Direct biochemical confirmation of Q88QT4 carrier-holdase and PPIase activities remains
desirable because its UniProt evidence level is PE=3 and no P. putida-specific
experimental publication was identified in the cache.

## PR #2731 dependency resolution

The two external dependencies that originally blocked the ISS proposal are now
resolved. Merged project policy explicitly classifies SurA as a carrier-holdase:
GO:0140309 requires escort "to an acceptor molecule or to a specific location," and
delivery within one compartment is sufficient when a defined acceptor such as
YaeT/BAM is demonstrated [`projects/UNFOLDED_PROTEIN_BINDING.md`]. The aligned
E. coli donor review now independently asserts NEW GO:0140309 for P0ABZ6
[`genes/ECOLI/surA/surA-ai-review.yaml`].

The P. putida annotation remains ISS rather than direct experimental evidence.
PMID:26344570 supplies the donor's IDA basis for stabilizing an unfolded FhuA state
during stepwise membrane insertion, while PMID:17908933 independently supplies the
YaeT/BAM acceptor endpoint. P0ABZ6 is recorded machine-readably in
`supporting_entities`; Q88QT4 itself has no direct organism-specific assay in the
cached literature. The seven physical GOA decisions are unchanged.
