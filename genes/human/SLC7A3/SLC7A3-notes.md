# SLC7A3 (CAT-3) curation notes

UniProt: Q8WY07 (CTR3_HUMAN). HGNC:11061. Gene synonyms ATRC3, CAT3. 619 aa, 14 TM
helices, APC superfamily, Cationic amino acid transporter (CAT) family (TC 2.A.3.3).
Reviewed as batch 8 of the canonical-surfaceome backfill.

## Core biology

CAT-3 / hCAT-3 is a **sodium-independent facilitative uniporter** ("system y+") that
mediates uptake of **cationic (basic) L-amino acids** — L-arginine, L-lysine, L-ornithine —
by passive, electrogenic facilitated diffusion.

- [PMID:11591158 "hCAT-3 is glycosylated and localized to the plasma membrane. Transport
  studies in Xenopus laevis oocytes revealed that hCAT-3 is selective for cationic L-amino
  acids and exhibits a maximal transport activity similar to other CAT proteins."]
- UniProt CC FUNCTION: [file:human/SLC7A3/SLC7A3-uniprot.txt "Uniporter that mediates the
  uptake of cationic L-amino acids such as L-arginine, L-lysine and L-ornithine
  (PubMed:11591158). The transport is sodium ions- and pH-independent, moderately trans-
  stimulated and is mediated by passive diffusion"].
- UniProt CATALYTIC ACTIVITY (ECO:0000269|PubMed:11591158): L-arginine(in)=L-arginine(out)
  RHEA:32143, CHEBI:32682; L-lysine(in)=L-lysine(out) RHEA:70935, CHEBI:32551;
  L-ornithine(in)=L-ornithine(out) RHEA:71199, CHEBI:46911.

ChEBI substrates verified against UniProt record: L-arginine CHEBI:32682, L-lysine
CHEBI:32551, L-ornithine CHEBI:46911.

**Mechanism cautions (important for curation):**
- NOT an obligate antiporter, NOT a symporter — it is a facilitative uniporter (passive
  diffusion, trans-stimulated). Core MF = basic/cationic amino acid transmembrane
  transporter (uniporter).
- CAT-3 is a **single-chain** CAT; it is NOT heteromeric (unlike SLC7A5-11 LAT-type light
  chains, CAT family members do not need an SLC3A2/4F2hc heavy chain). Do NOT model
  in_complex 4F2hc/SLC3A2; do NOT add amino-acid-transporting complex terms.

## Expression / tissue context

Originally CAT-3 was described as neuron-specific in adult rat/mouse brain, but human
hCAT-3 has a much wider distribution:
- [PMID:11591158 "Human CAT-3 expression is not restricted to the brain, in fact, by far
  the highest expression was found in thymus. Also in other peripheral tissues, hCAT-3
  expression was equal to or higher than in most brain regions, suggesting that hCAT-3 is
  not a neuron-specific transporter."]
- UniProt TISSUE SPECIFICITY: highest in thymus, uterus, testis; lower in brain, mammary
  gland, prostate, salivary gland, fetal spleen; in brain highest in thalamus, hippocampus,
  amygdala [file:human/SLC7A3/SLC7A3-uniprot.txt].
- [PMID:16332251 "hCAT-3, an isoform expressed in thymus, brain, ovary, uterus and mammary
  gland"].

### The arginine-for-nNOS / blood-brain-barrier trap
A "special role of CAT-3 providing substrate for nNOS" was proposed on the basis of
neuron-specific expression in rat, but this does NOT hold in human:
- [PMID:16332251 "A special role of CAT-3 providing substrate for the nNOS (neuronal nitric
  oxide synthase) has been proposed based on the neuron-specific expression of CAT-3 in rat
  brain [9]. However, in humans, hCAT-3 exhibits a much wider expression pattern that does
  not correlate with the expression pattern of nNOS [10]."]

Supplying arginine substrate for NO synthesis is substrate supply, not participation in NO
biosynthesis — the gene fails the participation test for NO-biosynthesis BP terms (none are
in GOA, so nothing to down-grade, but flagged for synthesis). Likewise
"transport across blood-brain barrier" (GO:0150104): the BBB is formed by brain capillary
*endothelial* cells, whereas hCAT-3 in brain is *neuronal* and its highest expression is in
non-CNS tissue (thymus). The two NAS rows for GO:0150104 cite generic BBB review articles
(PMID:26590417, PMID:30280653), neither of which is SLC7A3-specific. This is an
over-annotation → MARK_AS_OVER_ANNOTATED (claim exceeds the evidence; CAT-1 is the main
BBB-endothelial system-y+ transporter).

## Regulation
- PKC (classical cPKC) activation reduces cell-surface hCAT-3 by internalization (not by
  changing catalytic activity): [PMID:16332251 "hCAT-3 activity is decreased by PKC via
  reduction of transporter molecules in the plasma membrane"]. This supports the plasma
  membrane localization (surface biotinylation + confocal).

## Localization
- Plasma membrane: IDA (PMID:11591158, PMID:16332251), IBA, SubCell IEA, Reactome TAS — all
  consistent. Multi-pass membrane protein (14 TM). ACCEPT plasma membrane; MODIFY generic
  "membrane" (GO:0016020) → GO:0005886 plasma membrane.

## Protein interactions
- HuRI binary Y2H (PMID:32296183): interactors SLC10A1 (Q14973) and TMEM237 (Q96Q45-2);
  also in UniProt INTERACTION section (NbExp=3). These are high-throughput binary
  interactions with no derivable specific molecular function. Bare GO:0005515 protein
  binding is uninformative → REMOVE per protein-binding policy (removal does not mean the
  interactions are false).

## Annotation action summary (29 GOA rows)
- Core MF: GO:0015174 basic amino acid transmembrane transporter activity (facilitative
  uniporter); specific children GO:0061459 (L-arg), GO:0015189 (L-lys), GO:0000064 (L-orn)
  all IDA from PMID:11591158 → ACCEPT. Directional BP imports GO:0097638/9/40 (IDA) ACCEPT.
- Generic MF/BP that merely restate the specific functions (GO:0015171 amino acid
  transmembrane transporter activity; GO:0022857 transmembrane transporter activity;
  GO:0055085 transmembrane transport) → TOO_GENERAL (specific is_a descendants accepted).
- GO:0006865 amino acid transport, GO:0015822 ornithine transport, GO:0089718 amino acid
  import across PM, GO:1903401 L-lysine transmembrane transport → ACCEPT (still informative;
  IBA/IEA/TAS/Reactome at reasonable levels).
- GO:0016020 membrane (IEA) → MODIFY to GO:0005886 plasma membrane.
- GO:0005515 protein binding x2 → REMOVE.
- GO:0150104 transport across blood-brain barrier x2 (NAS) → MARK_AS_OVER_ANNOTATED.

No proposed_new_terms needed (the transport functions and locations are well covered).
No source defects identified.
