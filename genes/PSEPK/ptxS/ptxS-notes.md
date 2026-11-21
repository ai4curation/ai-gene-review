# ptxS (PtxS) — Pseudomonas putida KT2440 — Curation Notes

UniProt: Q88HH7 (PTXS_PSEPK). Locus PP_3380. 339 aa. LacI/GalR-family HTH-type
transcriptional regulator (repressor). PE 1: Evidence at protein level.

## FUNCTION

PtxS is a LacI/GalR-family transcriptional repressor that negatively controls the
2-ketogluconate (2-KG) peripheral pathway of glucose metabolism in P. putida.

- [UniProt "Negatively regulates glucose metabolism by binding directly to the promoter region of the kgu and gad operons (PubMed:20581202). It also negatively regulates its own synthesis (PubMed:20581202)."]
- [PMID:20581202 "The genes for the periplasmic and cytoplasmic set of reactions are clustered in the host chromosome and grouped within two independent operons that are under the control of the PtxS regulator, which also modulates its own synthesis."]
- [PMID:20581202 "Footprint analysis revealed that PtxS binds to an almost perfect palindrome that is present within the three promoters and whose consensus sequence is 5'-TGAAACCGGTTTCA-3'. This palindrome overlaps with the RNA polymerase binding site."]

DNA binding is experimentally demonstrated (footprinting, EMSA-type promoter
binding). The CollecTF-derived GOA annotations for DNA-binding transcription
repressor activity (GO:0001217), transcription cis-regulatory region binding
(GO:0000976) and protein-DNA complex (GO:0032993) are IPI experimental
annotations sourced from PMID:20581202. PtxS represses by binding a palindromic
operator overlapping the RNA polymerase binding site, consistent with classic
LacI/GalR-family steric repression.

## ACTIVITY REGULATION

2-ketogluconate (2-keto-D-gluconate) is the molecular effector; binding causes
de-repression (dissociation from the operator).

- [UniProt "2-ketogluconate acts as a molecular effector and causes dissociation of PtxS from its target promoter."]
- [PMID:20581202 "in vitro we found that only 2-ketogluconate binds to the regulator with an apparent K(D) (equilibrium dissociation constant) of 15 muM, as determined using isothermal titration calorimetry assays."]

## SUBUNIT

Homodimer in solution (IPI identical protein binding, PMID:20581202).

- [UniProt "Homodimer in solution. {ECO:0000269|PubMed:20581202}."]
- [PMID:20581202 "Purified PtxS is a dimer that binds to the target promoters with affinities in the range of 1 to 3 muM."]

## DOMAIN

- [UniProt "Contains an N-terminal helix-turn-helix DNA-binding domain and a C-terminal domain that binds the effector."]
- N-terminal HTH lacI-type domain (residues 12–67); H-T-H motif (14–33).
- C-terminal periplasmic-binding-protein-like (PBP1) effector-binding domain
  (LacI/GalR architecture).

## CURATION SYNTHESIS

Core molecular function: sequence-specific DNA-binding transcription repressor
activity (GO:0001217), enacted through binding of a cis-regulatory palindromic
operator (GO:0000976). Core biological process: negative regulation of
DNA-templated transcription (GO:0045892), specifically of carbohydrate
(2-ketogluconate/glucose) catabolic genes.

Annotation notes:
- GO:0042802 identical protein binding (IPI, homodimer) — accept, supported by
  documented homodimer; not the core informative function but specific and
  evidence-backed (avoid generic "protein binding").
- GO:0003700 DNA-binding transcription factor activity (IEA/TreeGrafter) — for a
  dedicated repressor, GO:0001217 (repressor activity) is the more precise child
  term; MODIFY toward GO:0001217.
- GO:0003677 DNA binding (IEA) — broad parent of the cis-regulatory region
  binding term; over-annotated/uninformative on its own.
- GO:0006355 regulation of DNA-templated transcription (IEA) — broad parent of
  the more specific negative regulation term; over-annotated.

## 2026-11-08 — carbon-utilization batch re-review

This entry supersedes the broad-term action recommendations above. All 11 seeded
GO annotation rows were re-reviewed. The original term/evidence/source fields
were preserved. Both GO:0000976 rows and the generic DNA-binding row are refined
to GO:0000987 (sequence-specific cis-regulatory DNA binding); the generic TF row
is refined to GO:0001217 and generic transcription regulation to GO:0045892.
True broad claims are not over-annotation. Homodimerization is retained as a
precise supporting, non-core interaction feature. Repression and operator binding
are combined into one core regulatory activity rather than duplicated as two
independent functions.

### Primary evidence and target assertions

Read the cached abstract and the publisher full text of
[PMID:20581202, Daddaoua et al. 2010](https://journals.asm.org/doi/full/10.1128/JB.00520-10).
The Materials and Methods explicitly name KT2440 DNA, wild-type KT2440 and an
isogenic ptxS mutant. Recombinant KT2440 PtxS was produced in E. coli BL21(DE3);
this is an expression host, not the source species for the regulatory claims.
The local publication cache remains abstract-only and was not manually changed.
PMC direct navigation encountered a browser challenge; the publisher full text
was accessible. Europe PMC full-text XML returned HTTP 500.

Evidence inspected: promoter-lacZ construction and beta-galactosidase methods;
results on reporter derepression in the ptxS mutant; DNA-complex experiments and
operator mapping; oligomerization assays; and the calorimetry section. Together
these establish direct repression at Pkgu, Pgad and PptxS. The new
[regulatory evidence sidecar](ptxS-regulatory-evidence.yaml) records exactly these
three promoter relationships, with condition, strain, assays and source. It does
not expand an operon into separate experimentally bound targets or import genomic
coordinates. RegPrecise and CollecTF labels, UniProt, and iModulon assignments
are not counted as independent experiments supporting the same paper.

2-Ketogluconate is directly bound in the calorimetry assay and reduces operator
occupancy. Glucose and gluconate induction are not direct ligand-binding claims.
The pathway-level statement is transcriptional control of the 2-ketogluconate
branch between gluconate and 6-phosphogluconate. No NEW annotation to glucose
catabolism, gluconate catabolism or the Entner-Doudoroff pathway is added: PtxS
regulates the expression of the proteins performing those reactions. The verified
GO:0045892 and core-function/target descriptions retain the supported mechanism
and pathway context. A broad carbohydrate-metabolism regulation term would add
little specificity here.

A bounded update search also found the 2012 PtxS-DNA crystallization study
(PMID:23143237) and the 2024 KT2440 GnuR study (PMC11590683). The former is an
additional structural lead, and the latter concerns another regulator; neither
was used to manufacture a new PtxS target. P. aeruginosa PtxR/exotoxin mechanisms
and P. plecoglossicida studies were kept distinct. The unsupported old claim that
the PANTHER SF145 name identifies PtxS's nearest characterized relative was
removed; family/subfamily labels do not establish its effector or regulon.

### Workflow, ontology and source availability

- `just fetch-gene-pmids PSEPK ptxS`: existing PMID:20581202 cache found; no source overwrite.
- `just deep-research-falcon PSEPK ptxS --fallback perplexity-lite`: Falcon authentication failed (403); fallback failed for insufficient quota (401). This manual primary-source review is recorded here, not in a provider-named file.
- `just mod-description-deep-research PSEPK ptxS`: skipped because PSEPK has no configured MOD provider.
- `just fetch-fitness PSEPK ptxS`: no reachable FEBA source/local database; no fitness artifact produced and no fitness claims used.
- `just paint-losses PSEPK ptxS`: first attempt encountered a shared temporary-download race; retry completed but Q88HH7 was not a leaf in the cached PTHR30146 tree. A lineage-loss assessment therefore was not available; the review has no IBA rows.
- QuickGO term endpoint checked GO:0000987, GO:0001217 and GO:0045892: all current, with the expected labels and MF/BP aspects. GO:0000987 is the sequence-specific refinement of GO:0000976. No RNA polymerase II-specific term was used.

The review remains complete for the existing annotation set and the three
characterized promoter relationships, not for all possible targets. Genome-wide
completeness and integration with other carbon regulators remain open questions.


## 2026-11-11 — PR review follow-up

Added GO:0097367 carbohydrate derivative binding (NEW, IDA, PMID:20581202) for the already documented 2-ketogluconate ITC measurement. The apparent KD is 15 micromolar and effector binding derepresses operator-bound PtxS. This is a functional regulatory interaction, not incidental glucose/gluconate induction. The cached abstract provides the verbatim quote; no provider output was modified.

Added PMID:18245293, whose KT2440/PSC303 experiments define the PtxS regulon, and GO:0010906 regulation of glucose metabolic process (NEW, IMP). Read the primary Methods, PtxS regulon results and Table 3 (https://pmc.ncbi.nlm.nih.gov/articles/PMC2293218/). PtxS itself executes regulation through operator binding and repression of genes for the gluconate/2-ketogluconate branch; it does not execute their metabolic reactions. The transcription-regulation term and glucose-regulation term are not is_a/part_of ancestors of each other (QuickGO checked 2026-11-11). Broad pathway regulation is used rather than assigning a net glucose-flux sign from one branch's transcriptional response.

Comparator check (2026-11-11): QuickGO queries for GO:0010906 on same-role regulators HexR/Q88P32, GnuR/Q88HE5 and Cra/P0A9I3 returned zero hits. This supplies no evidence for an overlooked annotation; in particular the proposed HexR row in this PR is not treated as an independent database precedent. The current electronic terms emphasize transcriptional regulation. The new proposal rests on the target-specific experimental regulatory step and the GO definition, not symmetry or pathway completeness. The proposal is for regulation, preserving the distinction that explains why regulators should not receive pathway-execution terms. The metabolic route includes gluconate and 2-ketogluconate as intermediates of glucose utilization, as experimentally established in the cited KT2440 study.
