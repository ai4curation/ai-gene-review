# TLR6 (human, Q9Y2C9) review notes

## Identity and architecture
- Type I transmembrane Toll-like receptor: signal peptide 1-31, LRR ectodomain (32-586), TM 587-607, cytoplasmic TIR domain (UniProt Q9Y2C9).
- Cloning paper: [PMID:10231569 "Human and murine TLR6 are type-I transmembrane receptors that contain both an extracellular leucine-rich repeat (LRR) domain and a cytoplasmic Toll/IL-1 receptor (IL-1R)-like region."]; closest paralogue TLR1 (69% identity); constitutively active TLR6 activates NF-kB and JNK [PMID:10231569 "Like other TLR family members, constitutively active TLR6 activates both NF-kappaB and c-Jun N-terminal kinase (JNK)."]

## Core function: TLR2 co-receptor for diacylated lipopeptides
- Knockout: [PMID:11431423 "Here we show that TLR6-deficient (TLR6(-/-)) cells are unresponsive to MALP-2 but retain their normal responses to lipopeptides of other bacterial origins."] and [PMID:11431423 "co-expression of TLR2 and TLR6 is absolutely required for MALP-2 responsiveness"].
- [PMID:12077222 "TLR6 associates with TLR2 and recognizes diacylated mycoplasmal lipopeptide along with TLR2."]
- Structure: [PMID:19931471 "We have determined the crystal structures of TLR2-TLR6-diacylated lipopeptide, TLR2-lipoteichoic acid, and TLR2-PE-DTPA complexes."]; specificity set by TLR6: [PMID:19931471 "First, the lipid channel of TLR6 is blocked by two phenylalanines."]; mutation of those residues made TLR2-TLR6 respond to triacylated lipopeptides too.
- So the recognition MF is a heterodimer-level activity: TLR2 binds the acyl chains, TLR6 supplies the interface and discriminates diacyl vs triacyl. contributes_to pattern recognition receptor activity (GO:0038187) is the right MF shape. There is no TLR-specific MF term.
- Heterodimers pre-exist at the cell surface, are recruited to rafts on ligand, and traffic to Golgi independently of signalling [PMID:16880211 "Our data show that TLR2 forms heterodimers with TLR1 and TLR6 and that these heterodimer pre-exist and are not induced by the ligand."; "Activation occurs at the cell surface, and the observed trafficking is independent of signaling."]
- S. aureus sensing by TLR2/6 in HEK293T [PMID:20406817 "we next used HEK293T transfected with TLR2/6 and/or NOD2 and measured NF-κB activation"].

## Secondary: CD36-TLR4-TLR6 sterile inflammation
- [PMID:20037584 "Importantly, we determine that the earliest event in this inflammatory cascade is not ligation of the TLRs but rather CD36-mediated recognition, which signals via Src kinases to induce a previously undescribed TLR heterodimer of TLR4-TLR6."]
- MyD88 and TRIF both used; Tlr6-/- macrophages/microglia lose chemokine, IL-1b, ROS, NO responses to oxLDL / Abeta.
- Consequence for GO: amyloid-beta binding (IC) is not supported -> REMOVE; recognition is CD36.
- Sheedy 2013: CD36-TLR4-TLR6 primes NLRP3 [PMID:23812099 "These data indicate that CD36-TLR4-TLR6, acting via NF-κB and ROS, primes the NLRP3 inflammasome in response to oxLDL."], but [PMID:23812099 "oxLDL-induced IL-1β secretion from LPS-primed Tlr6–/– macrophages was similar to wild-type macrophages"] -> "positive regulation of NLRP3 inflammasome complex assembly" is over-annotation (priming, not assembly).
- Liu 2012: TLR6 suppresses TLR2-mediated Abeta responses [PMID:22198949 "TLR2-mediated Aβ42-triggered inflammatory activation was enhanced by TLR1 and suppressed by TLR6"] - context specific, somewhat at odds with Stewart 2010 (TLR2 not required there).

## Curation decisions of note
- GO:0001875 LPS immune receptor activity (IDA, contributes_to, PMID:16880211): MODIFY to GO:0038187 PRR activity. Cited abstract concerns diacylated lipoprotein/LTA; TLR6 KO cells lose only MALP-2 responses. Full text not cached, so kept as MODIFY rather than REMOVE.
- GO:0031663 LPS-mediated signaling (IEA GO_REF:0000108, derived from GO:0001875): REMOVE.
- GO:0007250 activation of NIK activity (NAS): REMOVE; cloning paper only shows NF-kB/JNK reporter activation.
- GO:0046209 NO metabolic process (IEA): REMOVE; regulation already captured.
- GO:2001238 positive regulation of extrinsic apoptotic signaling: over-annotation (neurons die from microglial products).
- protein binding: MODIFY to TLR2 binding / Toll-like receptor binding where supported; TLR1 rows (TM peptides, BioPlex) REMOVE.
- Pathway terms: GO:0038124 (TLR6:TLR2) is_a GO:0002224 but is NOT a child of GO:0034150 (TLR6 signaling pathway), which itself sits under cell-surface TLR signaling. TLR6 has no annotation to GO:0034150. No NEW annotations added — GO:0038124 already covers it. Raised as a suggested question (ontology structure).
- Qiu 2013 PLoS One (PMID:23626692) carries a 2024 expression of concern.

## Deep research
- The review was completed without a deep-research file, from the UniProt record and the cached publications listed above (full text for PMID:20037584, 20067962, 20406817, 23155421, 23626692, 23812099, 33576548; abstracts only for the rest). `TLR6-deep-research-falcon.md` arrived afterwards; see the cross-check section below.

## Deep-research cross-check (2026-09-30)

Compared the completed review against `TLR6-deep-research-falcon.md`.
**No annotation action, term, description or core function was changed.**

Agreement:
- TLR6's best-established functional form is the TLR2:TLR6 heterodimer, and it is a
  receptor rather than an enzyme. Matches the core functions and the `Toll-like receptor 2
  binding` / TLR2:TLR6 complex rows.
- Diacyl specificity is set sterically by TLR6 Phe343 and Phe365 blocking the channel that
  in TLR1 takes the third acyl chain, and swapping them for the TLR1 residues broadens the
  response to triacylated ligands. Independent restatement of PMID:19931471, which the
  review already quotes.
- Plasma membrane as the functional location, with CD36, CD14 and LBP as accessory
  receptors. Supports the accepted membrane and raft rows and the CD36 core function.
- Ligands: Pam2CSK4, FSL-1, MALP-2, diacylated Gram-positive and Mycoplasma lipoproteins.
  Matches the accepted diacyl lipopeptide binding and detection rows.
- TIRAP/MAL then MyD88, myddosome, TRAF6-TAK1, canonical NF-kappaB plus JNK/p38/ERK.
  Supports the accepted NF-kappaB and MyD88-dependent pathway rows and keeping the JNK row
  non-core.

Additions not acted on:
- The report says that in the TLR2:TLR6 complex the two ester-linked chains insert into the
  TLR2 pocket while the glycerol moiety and peptide head group contact both receptors. This
  speaks directly to the existing suggested question on whether TLR6 itself touches the
  ligand, but the claim is carried only by secondary reviews here, so the `lipopeptide
  binding` rows were left as they were and the question stands.
- Trained immunity, blood-brain-barrier expression, sex differences, H. pylori-driven TLR6
  desensitisation, periodontal bone resorption and pulmonary arterial hypertension. All
  downstream, indirect or context-specific; none passes the participation test for a NEW
  process term.
- Polymorphism associations (A359T>C, Ser249Pro, rs3775073). Not annotation-relevant.

Conflicts: the report states that TLR6 signals "exclusively" through MyD88, whereas the
review keeps two `TRIF-dependent toll-like receptor signaling pathway` rows (IEA/ISS) as
non-core on the strength of the CD36-TLR4-TLR6 sterile-inflammation work
(PMID:20037584). The report's claim is from secondary reviews and concerns the canonical
TLR2:TLR6 route, which is not in dispute, so the non-core rows were left in place. The
report also does not discuss the CD36-TLR4-TLR6 heterodimer at all, so it neither supports
nor contradicts the removal of the amyloid-beta binding IC row.
