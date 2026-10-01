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


## 2026-09-30 BCKDHA source and mechanism reassessment

All 38 source assertions remain, with their 11 missing supporting-entity lists restored from GOA. The three pre-existing authored cofactor-binding annotations are retained, giving 41 total rows: 28 ACCEPT, eight KEEP_AS_NON_CORE, two MODIFY and three inherited NEW. No additional annotation or process assertion is introduced. The five BCKDHB interaction records are biologically coherent but generic, so they are retained as non-core instead of being rejected or treated as independent molecular functions.

One core now represents BCKDHA's contribution to the alpha2-beta2 E1 enzyme. The alpha chain helps bind and position ThDP and its metal ions; the assembled enzyme decarboxylates branched-chain ketoacids and reductively acylates the DBT lipoyl group. DBT and DLD perform the subsequent transfer-to-CoA and redox steps. Participation in the overall complex reaction does not assign those separate chemical activities to BCKDHA. This committed oxidation follows the reversible transamination step.

The magnesium and potassium contacts are grounded in the immutable UniProt record and the official human 1DTW structural record. Multiple listed coordinating residues do not constitute multiple alpha-chain potassium sites. The later 1U5B record contains manganese, so it is not used as specific magnesium-ligand evidence. Coordinates were not independently reanalyzed. Mature alpha Ser292 corresponds to precursor Ser337; phosphorylation disrupts lipoyl-domain recognition and reductive acylation more strongly than initial decarboxylation.

The two machine-derived UniProt products remain unchanged. Alternative-product targeting, assembly and regulation are experimental questions, not established loss of activity. Cached human studies and their complete abstracts support the synthesis, with full-paper and pair-level screen limitations recorded per reference. The provider reports remain unchanged as research leads. The earlier gel-band subunit assignments and counting of individual potassium contacts as separate sites are superseded here.

All ten normal Reactome records were recovered through Source94 after the documented initial local retrieval failed. Their recovered content was read and reassessed before this integration. Database descriptions are interpreted at their actual subunit and reaction level, including the alpha-versus-beta wording conflict in the PPM1K event. The original source assertions remain intact; a database wording discrepancy does not manufacture an experimental correction. Earlier notes are retained as history.

### Final validation and independent science review

The independent final biology review passed after narrowing an inherited universal activity-loss claim to severe impairment and removing an unlisted beta-specific residual-activity example from the alpha review. All 38 source annotations and three inherited cofactor-binding proposals remain in order; 11 missing supporting-entity lists were restored exactly from GOA. Both source-derived alternative products remain unchanged.

`just validate human BCKDHA` passed with six advisories: five supported generic protein-binding IPI annotations remain `KEEP_AS_NON_CORE` under the supplied action definitions, and annotations do not directly cite the retained generated research report. Primary normal publication records, reviewed UniProt and the ten normal Reactome records support the synthesis. No complete primary-paper, figure, pair-specific proteomics supplement, or PAINT-tree reconstruction is claimed. The separate `pkg_resources` deprecation notice is an environment warning. `just render human BCKDHA` succeeded. These are focused checks, not a claim that the entire repository was validated.


## 2026-09-30 — First PR feedback follow-up

Reviewed the first substantive feedback on PR #3614 against the current normal sources. All 38 source annotations and the three inherited cofactor-binding proposals remain in order, including qualifiers, supporting entities and both alternative products. Actions and core terms are unchanged.

The five experimentally attributed BCKDHB associations remain non-core under the user-supplied action definitions: generic binding is less informative than the shared E1 assembly, but that alone does not make a supported association false. This is an explicit application of the user's definitions, not a legacy-action exemption. The five policy advisories remain expected.

Selected existing source excerpts were moved into the experimental annotation decisions they support. Core excerpts now identify the E1 complex and its coupled decarboxylation/reductive-acylation chemistry with enough context to be intelligible. New excerpts are deliberately bounded; a bare citation elsewhere does not claim a pair-level experiment or unavailable full text was re-read. The complete abstracts and existing curator attribution retain the reading limits documented per reference. Repeating the same passage in every row would not supply independent evidence.

The former combined UniProt finding is split into focused statements about matrix location, transit and mature-chain ranges, shared ThDP ligand, and specific magnesium/potassium contacts. Each excerpt supports its own statement. Complete contact lists remain in the three inherited proposals, with spacing corrected. Multiple coordinating residues still do not mean multiple alpha-chain potassium sites.

The ten Reactome TAS decisions now justify matrix localization directly from the reviewed human UniProt SUBCELLULAR LOCATION. The cached Reactome summaries have no explicit compartment field, so they provide reaction context rather than independent localization experiments. E1 performs decarboxylation and reductive acylation, DBT transfers the acyl group to CoA, DLD reoxidizes the lipoyl group, BCKDK phosphorylates E1 alpha, and PPM1K removes that phosphate. Those roles are not inferred from a location annotation. Reactome source findings now describe source content with short exact excerpts; subunit-wording and genotype-specific cautions remain in reference-review notes. The PPM1K event's E1-beta wording remains disputed, and severe residual-activity values remain variant-specific.

The official AmiGO term page explicitly places GO:0120552 part_of GO:0009083 (BFO:0000050), confirming the existing specific core process choice. The broader source assertions remain unchanged. [AmiGO GO:0120552](https://amigo.geneontology.org/amigo/term/GO:0120552). No new process annotation is proposed.


## Follow-up validation, 2026-09-30

The independently reviewed follow-up passes focused validation (six warnings), history validation, and rendering. Five warnings concern supported generic binding retained as non-core under the supplied action definitions; the other records that primary/database sources, rather than the unchanged generated report, support annotation decisions. All 38 source assertions, three inherited NEW assertions and two products are preserved. No new global validation pass is claimed.
