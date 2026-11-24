# UNC93B1 (Q9H1C4, human) — curation notes

Unc-93 homolog B1; ER-resident multi-pass (12-TM) membrane chaperone/trafficking factor for
nucleotide-sensing Toll-like receptors.

## Deep-research cross-check (2026-09-30)
Falcon deep research (`UNC93B1-deep-research-falcon.md`) arrived after the review was written and
was compared against every decision.
- **Agreement:** ER-resident 12-TM MFS-like chaperone; binds TLR3/7/8/9 (and TLR5) via the
  N-terminal six-helix bundle; escorts them ER -> Golgi -> endolysosomes; LoF (e.g. H412R, 3d)
  traps TLRs in the ER and causes HSE susceptibility. All location, TLR-binding and transport
  decisions, the KEEP_AS_NON_CORE treatment of TLR3/7/9 pathway rows, and the protein-binding
  MODIFY/REMOVE decisions are consistent with the report. No annotation action changed.
- **Additions (verified in primary papers):** UNC93B1 also negatively regulates TLR7/TLR8 after
  delivery, and gain-of-function variants cause monogenic SLE/chilblain lupus
  [PMID:38869500 "these observations suggest that UNC93B1 mutations cause monogenic SLE
or CBL due to differentially enhanced TLR7 and TLR8 signaling"];
  [PMID:38780621 "identified both negative and positive regulatory regions affecting TLR3, TLR7,
and TLR9 responses"].
  Description extended with one sentence; both papers added to references.
- **Additions (abstract-only, not used for annotation):** UNC93B1 binds STING and delivers it to
  lysosomes for degradation, attenuating cGAS-STING signalling [PMID:35577759 "UNC93B1 interacts with STING and suppresses STING-activated downstream signaling by delivering STING to the lysosomes for degradation"].
  Single-laboratory report; raised as a suggested question rather than a NEW annotation.
- **Nuance / mild tension:** the report (via Song 2022, Front Immunol, PMID:35874766, not cached)
  says Asn272 glycosylation of UNC93B1 is needed for MyD88 recruitment to TLR9, which qualifies the
  older statement that UNC93B1 is dispensable for signal initiation [PMID:18305481]. Not verified
  in a cached primary text; description wording left as is.
- Minor report inaccuracy: it calls the TLR3 structure "mouse" only; Ishida 2021 solved human and
  mouse TLR3-UNC93B1 plus human TLR7-UNC93B1.
- Changes: description (GoF lupus sentence), 3 new references + falcon file reference, one
  supported_by quote from the falcon file on a GO:0006886 row, one new suggested question.

## Core biology
- ER-resident polytopic membrane protein; its function is to deliver nucleotide-sensing TLRs
  (TLR7, TLR9; also TLR3, TLR8) from the ER to endolysosomes
  [PMID:18305481 "function of the polytopic membrane protein UNC93B1 is to deliver the nucleotide-sensing receptors TLR7 and TLR9 from the ER to endolysosomes"].
- Physically interacts with TLR3/7/8/9 in the ER via their transmembrane regions
  [PMID:18305481 "essential for\nsignalling of TLR3, TLR7 and TLR9 in both humans and mice, physically interacts\nwith these TLRs in the endoplasmic reticulum (ER)"; PMID:33432245 "Both TLRs interact with the UNC93B1\namino-terminal six-helix bundle through their transmembrane and luminal\njuxtamembrane regions"].
- Cryo-EM structures of human/mouse TLR3-UNC93B1 and human TLR7-UNC93B1 complexes; UNC93B1
  resembles MFS transporters and is indispensable for TLR ER-to-endosome trafficking
  [PMID:33432245 "indispensable for the\ntrafficking of TLRs from the endoplasmic reticulum to the endosome"].
- UNC93B1 also physically associates with human TLR8 and is critical for TLR8 signalling
  [PMID:22164301 "UNC93B1 physically associated with human TLR8,\nsimilar to TLRs 3, 7, and 9, and played a critical role in TLR8-mediated\nsignaling"].
- Crucially, UNC93B1 is DISPENSABLE for ligand recognition and signal initiation by the TLRs
  themselves — it acts upstream as a trafficking chaperone, not as a signal transducer
  [PMID:18305481 "UNC93B1 is dispensable for ligand recognition and signal initiation by TLRs"].
- The mouse 3d mutation (H412R, Unc93b1) abolishes TLR3/7/9 signalling and antigen cross-presentation
  [PMID:16415873 "no signaling\noccurs via the intracellular Toll-like receptors 3, 7 and 9"].
- Human UNC-93B (UNC93B1) deficiency causes isolated herpes simplex encephalitis via impaired
  type I/III IFN responses [PMID:16973841 "autosomal recessive deficiency in the intracellular protein\nUNC-93B, resulting in impaired cellular interferon-alpha/beta and -lambda\nantiviral responses"].
- UNC93B1-deficient human cells are unresponsive to TLR3, TLR7, TLR8 and TLR9 and patients show
  defective B-cell tolerance checkpoints [PMID:19006693 "UNC-93B-deficient cells are unresponsive to TLR3, TLR7,\nTLR8, and TLR9"].
- Also required for TLR5 (a cell-surface TLR) plasma membrane localization and signalling
  [PMID:24778236 "TLR5, a cell surface receptor for bacterial protein flagellin, also\nrequires UNC93B1 for plasma membrane localization and signaling"].

## Participation-test analysis for TLR signaling-pathway process terms (project focus)
UNC93B1 is a trafficking chaperone. Applying the CLAUDE.md participation test: the "work" of a TLR
signaling pathway (ligand binding, receptor dimerization, TIR/adaptor recruitment, kinase
activation) is performed by the TLR and downstream components, NOT by UNC93B1. UNC93B1 is
*required* for the pathway (knockout abolishes signalling), but this is necessity, not
participation — and the same paper that establishes necessity states UNC93B1 is dispensable for
signal initiation [PMID:18305481]. UNC93B1 acts upstream as the chaperone that positions the
receptor.

However, GO curators have consistently annotated both human (Q9H1C4) and mouse (Q8VCW4) UNC93B1
to GO:0034138/0034154/0034162 (TLR3/7/9 signaling pathway) with experimental (IMP) and
phylogenetic (IBA, PANTHER:PTN002928790) evidence, and the mouse rows use
`acts_upstream_of_or_within`. Per the "do not overrule curators from incomplete evidence" rule,
these experimental annotations are not removed. Instead they are marked KEEP_AS_NON_CORE: the core
molecular function is Toll-like receptor binding / protein carrier (trafficking) activity and the
core process is intracellular protein transport; the TLR signaling-pathway terms record the
downstream process UNC93B1 enables as an upstream chaperone, which is non-core.

Comparator: CNPY3 (Q9BT09), another TLR chaperone, carries signaling receptor binding (GO:0005102)
but is not annotated to the TLR signaling-pathway process terms in QuickGO — consistent with the
view that a chaperone's core representation is receptor binding + trafficking rather than pathway
participation. UNC93B1's pathway annotations are a curator convention grounded in strong knockout
data, retained here as non-core.

## GO:0005515 generic protein binding rows
- PMID:22164301 (TLR8, Q9NR97) and PMID:33961781 (TLR8, Q9NR97): partner is a TLR → MODIFY to
  GO:0035325 Toll-like receptor binding (informative, supported).
- PMID:32296183 (HuRI binary interactome, ~24 partners: BEST2, CCDC107, CD79A, CLDN7, CREB3L1,
  CSE1L... EBP, ERGIC3, FATE1, FFAR3, GPR101, GPR37L1, GPRC5D, HHLA2, KLRC1, LDLRAD1, LEUTX, LIME1,
  MFF, REEP1, SLC35C2, SSMEM1, SYNDIG1, TM4SF18, TMEM237): high-throughput Y2H binary interactome,
  mostly membrane proteins with no functional follow-up → REMOVE as uninformative generic binding
  (removal does not assert the interactions are false).
- PMID:30833792 (CSE1L P55060, KPNB1 Q14974): interferon-stimulated-gene AP-MS network; nuclear
  transport proteins, no established functional UNC93B1 role → REMOVE as uninformative.
- PMID:33845483 (SARS-CoV-2 ORF7b P0DTD8, Xeno): virus-host proteomics screen → REMOVE as
  uninformative.

## Locations
ER and ER membrane (core, IDA), Golgi membrane (transits), endosome and lysosome (relocalizes with
CpG stimulation), early phagosome / phagocytic vesicle (ortholog/subcell mapping, non-core). All
ACCEPT; consistent with the ER-to-endolysosome trafficking route.

## 2026-11-22 ORGANELLES lysosome batch 2

- Three GO:0005764 rows: IBA is_active_in (PTN002928790, seed MGI:1859307), IEA GO_REF:0000120 (Ensembl projection from mouse Q8VCW4 plus SubCell), ISS (Q8VCW4). Review and GOA agree; no sub-compartment rows.
- Donor trace: the human UniProt lysosome item is ECO:0000250 to mouse Q8VCW4; the mouse entry's lysosome item is untagged and its relocalization note is itself ECO:0000250 (looked up at rest.uniprot.org, 2026-11-22). The only experimental mouse lysosome row in QuickGO is a UniProt IDA from PMID:18305481 (Kim et al. 2008), abstract-only here with no PMC copy.
- PMID:31546247 (Majer et al. 2019, Nature; PMC6856438, DOI 10.1038/s41586-019-1611-7): full text read in PMC and fetched into the cache. Tagged Unc93b1 retrovirally expressed in mouse macrophages is quantified within Lamp1-positive endosomes (Extended Data Fig. 1a), co-purifies with TLR9 from bead phagosomes, and TLR9 is released from it only within endosomes [PMID:31546247 "The plot shows quantification of the percentage of total Unc93b1 within Lamp1+ endosomes."].
- Call: all three rows ACCEPT -> KEEP_AS_NON_CORE. Real functional pool (TLR9 release), not cargo; non-core because LAMP1 alone does not separate late endosome/endolysosome from lysosome and the core chaperone activity is at the ER. ACCEPT is the close alternative. is_active_in kept without a WRONG_QUALIFIER defect (release activity shown in Lamp1-positive endosomes). No GO:0005765 row: only one weak line.
- Endosome rows (GO:0005768 IBA, IEA, ISS) rest on the same mouse donor chain; out of scope, not changed.
- Description sentence on relocalization to "endosomes and lysosomes" (uncited UniProt note) reworded to the LAMP1-positive endolysosome pool.

### Review follow-up (2026-11-22)

- The IBA reason now contrasts the kept is_active_in qualifier with the queried RAB rows.

## 2026-11-23 ORGANELLES endosome batch 1

- Four endosome rows (IBA is_active_in, IDA PMID:21642595, IEA GO_REF:0000120, ISS Q8VCW4) kept
  ACCEPT. Human IDA: UniProt ECO:0000269 note (colocalizes with LAMP5 in large endosomal vesicles),
  paper abstract-only with no PMC copy, curator deference. ISS/IEA: the circular mouse UniProt
  chain found in lysosome batch 2 (mouse Endosome item untagged), plus ARBA00028568 and an
  Ensembl projection from the mouse IDA (PMID:18305481, abstract-only). IBA seeds: mouse Unc93b1
  and human UNC93B1 itself.
- Deciding evidence (mouse full text PMID:31546247, cached): Unc93b1 quantified in Lamp1+
  endosomes by SIM in Unc93b1-knockout RAW264.7 cells re-expressing tagged Unc93b1, and
  co-fractionating with TLR9 in CpG-ligand-enriched endosomal fractions, where TLR9 is released
  ["As predicted, the association of Unc93b1 and TLR9 was weaker in endosomes than in the ER"].
- ACCEPT because the release step (end of the carrier-chaperone activity) is shown in the
  endosome and the compartment is resolved as endosomal; the lysosome rows stay KEEP_AS_NON_CORE
  because LAMP1 does not resolve the lysosome. core_functions (protein carrier chaperone) now lists
  the endosome root beside the ER membrane. No stage row (LAMP1 and an unstaged CpG fraction).
- is_active_in IBA: activity shown in endosomes; qualifier kept, no WRONG_QUALIFIER.
