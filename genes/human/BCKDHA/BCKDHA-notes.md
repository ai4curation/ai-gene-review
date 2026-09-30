# BCKDHA (P12694) review notes

## Summary of verified biology

BCKDHA encodes the **E1 alpha (E1α)** subunit of the mitochondrial **branched-chain
alpha-ketoacid dehydrogenase (BCKDH / BCKD / BCKDC)** complex. Together with BCKDHB
(E1β) it forms the **α2β2 heterotetrameric E1 decarboxylase component** (the
"branched-chain alpha-keto acid decarboxylase"). The complete complex is organized
around the E2 (DBT) 24-meric transacylase core, to which multiple E1 (α2β2) and E3
(DLD dimer) copies bind.

- The BCKD complex catalyzes the **first, committed, rate-limiting and irreversible
  step** of branched-chain amino acid (BCAA: leucine, isoleucine, valine) catabolism:
  oxidative decarboxylation of the branched-chain 2-oxo (α-keto) acids (KIC, KMV/KMVA,
  KIV — from the BCAAs via BCAT2) to branched-chain acyl-CoA + CO2.
- **E1 (BCKDHA + BCKDHB) catalyzes the first two half-reactions**: (1) TPP-dependent
  decarboxylation of the α-ketoacid, and (2) reductive acylation transferring the acyl
  group to the lipoyl domain of E2. EC 1.2.4.4.
- **Cofactors:** thiamine diphosphate (TPP/ThDP) and Mg2+; also structural K+ ions.
  TPP and Mg2+ binding residues are on E1α (UniProt BINDING features: TPP at
  158,159,207,239,240,265,336; Mg2+ at 238,267,269).
- **Localization:** mitochondrial matrix (cleaved transit peptide 1–45; chain 46–445).
- **Regulation:** phosphorylated at Ser337 (mature numbering; Ser292-alpha in structural
  papers) by BCKDK (inactivating) and dephosphorylated by PPM1K (activating). Phospho of
  the E1α phosphorylation loop shuts off reductive acylation, inactivating BCKDC.
- **Disease:** biallelic loss-of-function BCKDHA variants cause **Maple Syrup Urine
  Disease type IA (MSUD1A, MIM:248600)** — autosomal recessive. Classic MSUD has <2–5%
  residual activity. Founder Y438N (a.k.a. Y393N mature numbering) mutation common in Old
  Order Mennonites (incidence ~1:150 vs ~1:225,000 global).

## Key evidence / provenance

- UniProt P12694 (ODBA_HUMAN): FUNCTION, CATALYTIC ACTIVITY (EC 1.2.4.4; RHEA:13457
  primary reaction), COFACTOR (TPP, Mg2+), SUBUNIT (α2β2; complex organized on E2 core;
  interacts with PPM1K), SUBCELLULAR LOCATION (mitochondrion matrix), DISEASE (MSUD1A),
  numerous MSUD variants each annotated "loss of 3-methyl-2-oxobutanoate dehydrogenase
  activity". [file:human/BCKDHA/BCKDHA-uniprot.txt]
- PMID:10745006 (Aevarsson 2000, Structure): crystal structure of human E1
  (α2β2 heterotetramer) in complex with BCKDHB, TPP, K+, Mg2+; molecular basis of MSUD.
  "the 170 kDa alpha(2)beta(2) heterotetrameric E1b component of the branched-chain
  alpha-ketoacid dehydrogenase multienzyme complex". Abstract-only cache.
- PMID:9582350 (Wynn 1998, JBC): E1 decarboxylase = two E1α + two E1β forming α2β2
  tetramer; MSUD type IA affects E1α causing loss of E1 and BCKAD catalytic activities;
  E1α missense mutations impair assembly. Abstract-only.
- PMID:7883996 (Chuang 1995, JCI): intermediate MSUD; G245R and F364C E1α mutations
  disrupt E1 heterotetrameric assembly and function of the BCKAD complex. Abstract-only.
- PMID:3593587 (Ono 1987): purification/characterization of human liver BCKADH complex;
  oxidizes KIV, KIC, KMV. Abstract-only. (ComplexPortal + FlyBase source for several anns.)
- PMID:12902323 / 15166214 / 15576032 (Chuang lab): structural/mechanistic studies of
  human E1b (decarboxylation, reductive acylation, ThDP binding, phosphorylation-loop
  regulation). GOA lists these as IPI protein binding with WITH/FROM = UniProtKB:P21953
  (BCKDHB) — i.e., the E1α–E1β interaction. Abstract-only.
- PMID:28514442 (BioPlex 2.0) / 33961781 (BioPlex 3.0): large-scale AP-MS interactome
  screens; source of IPI protein binding (WITH/FROM P21953). Guilt-by-association scale.
- PMID:11839747 (Chang 2002): NMR of the E2 lipoyl-bearing domain of the human BCKD
  complex. TAS source for carboxy-lyase activity + mitochondrion.
- PMID:20833797 (Zhao 2011) HDA / PMID:34800366 HTP: mitochondrial proteome/phosphoproteome
  localization evidence.
- dismech Maple_Syrup_Urine_Disease.yaml (MONDO:0009563): confirms BCKDH complex
  (BCKDHA/BCKDHB/DBT/DLD) deficiency, first irreversible step of BCAA catabolism in mito
  matrix, regulation by BCKDK/PPM1K, Type IA = E1-alpha (BCKDHA); Mennonite Y438N founder.

## Curation decisions (policy-guided)

- MF core: GO:0003863 branched-chain 2-oxo acid dehydrogenase activity (the E1α
  decarboxylase MF). GOA has this as IDA (contributes_to and enables), IEA (EC/RHEA).
- Bare `protein binding` (GO:0005515) IPIs: all WITH/FROM = BCKDHB. Per policy MARK these
  as over-annotated (uninformative MF), not REMOVE. The biologically meaningful content
  (α2β2 heterotetramer) is captured by GO:0160157 complex membership + core_functions.
- IEA GO:0016624 (oxidoreductase ...disulfide as acceptor) is an InterPro2GO mapping — E1
  does NOT use a disulfide acceptor (that is E3/DLD); the acceptor for E1 is the lipoyl-
  lysine of E2. Too general/imprecise for E1α → MODIFY toward GO:0003863.
- GO:0016831 carboxy-lyase activity (TAS): correct but generic parent of the specific
  decarboxylase activity → MARK_AS_OVER_ANNOTATED / could MODIFY to GO:0003863.
- No falcon deep-research file available at time of writing (recipe launched; polled).

---

## 2026-09-04 — PAINT no-IBA project finishing pass

Reviewed every `existing_annotations` entry against the cached publications, the UniProt
record and `BCKDHA-deep-research-falcon.md` (which had landed by the time of this pass).
Status moved `INITIALIZED` → `COMPLETE`; validation is clean (`✓ Valid`, zero warnings,
`--terms` included) and `update-status` now agrees.

**Corrections made**

- **Residue numbering was mislabelled as "mature".** The description and two annotation
  summaries said Ser337 / TPP 158–336 / Mg 238,267,269 were "in mature numbering". They
  are not: UniProt P12694 numbering is *precursor* numbering (TRANSIT 1..45, CHAIN
  46..445), so Ser337 of the precursor is Ser292 of the mature chain — which is exactly
  the "Ser292-alpha" the structural literature uses, and 45 residues away from what the
  file claimed. Fixed in `description`, in the GO:0030976 and GO:0000287 summaries, and
  in the corresponding `core_functions` description. Verified position-by-position
  against the SQ block: 158 Y, 159 R, 207 S, 239 G, 240 A, 265 R, 336 H (ThDP);
  238 E, 267 N, 269 Y (Mg2+); 206 S, 208 P, 211 T, 212 Q (structural K+); 337 S.
- **`- No falcon deep-research file available`** — stale; the file exists and is now
  cited. Also removed two stray XML-ish tags that had been left at the end of this file.

**Additions**

- New `action: NEW` annotation **GO:0030955 potassium ion binding** (IDA,
  PMID:10745006). UniProt records four structural K+ BINDING sites on E1-alpha and the
  structure paper states the ions were located and that one of them orders the
  cofactor-proximal loop [PMID:10745006 "The position of two important potassium (K(+))
  ions was determined."; "One of these ions assists a loop that is close to the cofactor
  to adopt the proper conformation."]. Added as non-core (structural, not catalytic), so
  it is deliberately *not* promoted into `core_functions`.
- `supported_by` added to the previously bare magnesium `core_functions` entry.
- `file:human/BCKDHA/BCKDHA-deep-research-falcon.md` and
  `file:human/BCKDHA/BCKDHA-uniprot.txt` added to `references` with findings; the deep
  research is marked `correctness: UNVERIFIED` because it is an LLM synthesis whose own
  citation keys were not checked — it is used only where UniProt or PMID:10745006
  independently corroborate it. It does cleanly document the subunit division of labour
  at the cofactor site [file "The E1α subunit provides residues critical for binding the
  diphosphate portion of thiamine pyrophosphate and associated divalent metal atoms,
  while E1β subunits contribute residues that bind the thiazolium ring portion"].

**Actions left unchanged after re-checking** — the five bare `protein binding` IPIs stay
`MARK_AS_OVER_ANNOTATED` (all WITH/FROM P21953; the real content is the α2β2 tetramer,
already carried by GO:0160157); GO:0016624 stays `MODIFY`→GO:0003863; GO:0016831
carboxy-lyase stays `MARK_AS_OVER_ANNOTATED`. Note the earlier note in this file arguing
that "E1 does NOT use a disulfide acceptor" is **wrong** — EC 1.2.4.4 sits in EC 1.2.4,
"with a disulfide as acceptor", the acceptor being the lipoamide disulfide of E2, and
GO:0003863 *is_a* GO:0016624. The MODIFY call is still right, but for the granularity
reason only, and the YAML `reason` was already phrased that way.

**Family context** — see `interpro/panther/PTHR43380/PTHR43380-review.yaml`. Two things
worth carrying back here: (1) BCKDHA is no longer IBA-free — GOA now has IBAs for
GO:0009083 (20260530) and GO:0160157 (20250904), matching the two PAINT rows; (2) PAINT
still asserts **no molecular function** on the branched-chain side of PTHR43380, so
GO:0003863 — the best-evidenced term this gene has — does not propagate. PANTHER also
lumps bacterial pyruvate dehydrogenase E1-alpha (pdhA) into the same subfamily SF1 as
BCKDHA, so any MF term must be placed at a PTN node rather than at SF1.
