# BCKDHB (P21953) review notes

## Identity
- 2-oxoisovalerate dehydrogenase subunit beta, mitochondrial (ODBB_HUMAN); BCKDE1B / BCKDH E1-beta.
- EC 1.2.4.4. HGNC:987. NCBITaxon:9606.
- Precursor: transit peptide 1..50 (mitochondrial); mature chain 51..392.
- ComplexPortal CPX-2216 "Mitochondrial 2-oxoisovalerate dehydrogenase complex".

## Core biology (from UniProt P21953, verified quotes)
- FUNCTION: "Together with BCKDHA forms the heterotetrameric E1 subunit of the mitochondrial branched-chain
  alpha-ketoacid dehydrogenase (BCKD) complex. The BCKD complex catalyzes the multi-step oxidative
  decarboxylation of alpha-ketoacids derived from the branched-chain amino-acids valine, leucine and
  isoleucine producing CO2 and acyl-CoA..." "The E1 subunit catalyzes the first step with the
  decarboxylation of the alpha-ketoacid forming an enzyme-product intermediate. A reductive acylation
  mediated by the lipoylamide cofactor of E2 extracts the acyl group from the E1 active site..."
- SUBUNIT: "Heterotetramer of 2 alpha/BCKDHA and 2 beta chains/BCKDHB that forms the branched-chain
  alpha-keto acid decarboxylase (E1) component of the BCKD complex." Complex organized around E2
  (24-meric DBT core) + 6-12 E1 + ~6 E3 (DLD dimer).
- COFACTOR: thiamine diphosphate (ThDP/TPP). BINDING 152 = ThDP (shared with alpha). Multiple K+ structural
  binding sites (178,180,181,228,231,233).
- SUBCELLULAR LOCATION: Mitochondrion matrix.
- INTERACTION: P21953 - P12694 (BCKDHA), NbExp=15 (IntAct EBI-1029067/EBI-1029053). This is the direct
  E1 heterotetramer partner. All 5 IPI GO:0005515 rows have WITH/FROM UniProtKB:P12694 = BCKDHA.

## Catalysis (UniProt CATALYTIC ACTIVITY, RHEA)
- RHEA:13457 (EC 1.2.4.4): lipoyl-lysyl-[protein] + 3-methyl-2-oxobutanoate (= alpha-ketoisovalerate, KIV
  from valine) + H+ = S(8)-2-methylpropanoyldihydrolipoyl-lysyl-[protein] + CO2. Evidence PubMed:10745006, 9582350.
- RHEA:84639: with 4-methyl-2-oxopentanoate (KIC from leucine).
- RHEA:84643: with (S)-3-methyl-2-oxopentanoate (KMV from isoleucine).
- So E1 handles all three BCKAs (KIV, KIC, KMV) -> the three separate leucine/isoleucine/valine
  catabolic BP terms are all legitimate for BCKDHB.

## Key literature (all cached abstract-only unless noted)
- PMID:10745006 (Aevarsson 2000, Structure): crystal structure of human E1b, "the 170 kDa
  alpha(2)beta(2) heterotetrameric E1b component"; K+ ion sites; MSUD mutations explained. Full_text: false.
- PMID:9582350 (Wynn 1998, JBC): "The E1 decarboxylase component of the human branched-chain ketoacid
  dehydrogenase complex comprises two E1alpha (45.5 kDa) and two E1beta (37.5 kDa) subunits forming an
  alpha2 beta2 tetramer." Assembly of E1 in type IA MSUD. Full_text: false.
- PMID:3593587 (Ono 1987): Purification/characterization of human liver BCKADH complex; "The BCKADH
  effectively oxidized all of KIV, KIC, and KMV". Full_text: false.
- PMID:2022752 (Nobukuni 1991, JCI): Complete E1beta defect from 11-bp deletion in mito targeting leader
  peptide; "BCKDH activity in the proband ... approximately 6% of the normal control level"; "The absence
  of the E1 beta subunit results in instability of the E1 alpha subunit." IMP support for complex,
  process, mitochondrion. Full_text: abstract only.
- PMID:12902323 (Wynn 2003): His146-beta' essential catalytic residue in reductive acylation. His-alpha/beta
  active-site mechanism. (IPI to BCKDHA.)
- PMID:15166214 (Li 2004): ThDP binding / phosphorylation-loop cross-talk in E1b. (IPI to BCKDHA.)
- PMID:15576032 (Wynn 2004): Regulation of BCKDC by phosphorylation of Ser292-alpha; disorder of
  phosphorylation loop shuts off reductive acylation. (IPI to BCKDHA.)
- PMID:28514442 (Huttlin 2017 BioPlex/Nature) & PMID:33961781 (Huttlin 2021 Cell): large-scale
  interactome; IPI GO:0005515 with BCKDHA. Full text available.
- PMID:34800366 (Morgenstern 2021 Cell Metab): high-confidence human mito proteome (HTP), mitochondrion.

## Disease
- MSUD 1B (MIM:620698), autosomal recessive; E1-beta subunit deficiency (Type IB). BCAA (Leu/Ile/Val) and
  their BCKAs accumulate -> encephalopathy, neurodegeneration. (dismech Maple_Syrup_Urine_Disease.yaml.)

## Curation plan
- Core MF: GO:0003863 branched-chain 2-oxo acid dehydrogenase activity (contributes_to; heterotetrameric
  E1 catalytic activity — BCKDHB contributes to shared active site with BCKDHA). Label per GOA/UniProt.
- Core BP: GO:0009083 branched-chain amino acid catabolic process (directly_involved_in).
- Core CC: GO:0005759 mitochondrial matrix; in_complex GO:0160157 BCKDH complex.
- IEA/IBA process terms (Leu/Ile/Val catabolism, response to nutrient) accept as non-core/accept-broader.
- 5x protein binding IPI (all vs BCKDHA): MARK_AS_OVER_ANNOTATED per policy (bare protein binding,
  real but uninformative; the informative capture is the E1 heterotetramer complex + MF).
- protein-containing complex GO:0032991 IEA: MODIFY -> too general vs GO:0160157.
- Reactome/HPA/HTP location terms: accept.

## Deep research
- falcon deep research file polled; see final report for whether it landed within the 8-min window.

---

## 2026-09-04 — PAINT no-IBA project finishing pass

Reviewed every `existing_annotations` entry against the cached publications, UniProt
P21953 and `BCKDHB-deep-research-falcon.md`. Status moved `INITIALIZED` → `COMPLETE`;
validation clean (`✓ Valid`, zero warnings, `--terms` included).

**Structural change to `core_functions`.** The single core function used
`molecular_function: GO:0003863`. But every *manual* GOA annotation of that term on
BCKDHB carries `contributes_to` (IDA PMID:10745006, IDA PMID:9582350, IMP PMID:2022752),
because the E1 active sites lie at the α/β′ interfaces and the β chain has no active site
of its own. The schema is explicit about this case: put the complex-level activity in
`contributes_to_molecular_function` and a subunit-specific activity in
`molecular_function`. Restructured accordingly — `molecular_function: GO:0030976`
(thiamine pyrophosphate binding, the concrete thing the β subunit does on its own) and
`contributes_to_molecular_function: GO:0003863`. Also added GO:0120552 to
`directly_involved_in` alongside GO:0009083, since the more precise process term is
annotated on this gene with IDA and IMP evidence.

**Additions**

- `action: NEW` **GO:0030976 thiamine pyrophosphate binding** (IDA, PMID:10745006).
  UniProt BINDING 152 on P21953 is a ThDP contact flagged "ligand shared with alpha
  subunit" with `ECO:0000269|PubMed:10745006`; verified as Tyr152 against the SQ block.
- `action: NEW` **GO:0030955 potassium ion binding** (IDA, PMID:10745006). Six structural
  K+ BINDING sites on P21953 (178 G, 180 L, 181 T, 228 C, 231 D, 233 N — all verified
  against the sequence), and the structure paper places the second of the two located K+
  ions in this subunit [PMID:10745006 "The second is located in the beta subunit near the
  interface with the small C-terminal domain of the alpha subunit."]. Kept non-core:
  structural, not catalytic.
- `suggested_questions` and `suggested_experiments` sections, which were absent.
- The deep-research file now carries a `findings` entry and a `reference_review`
  (`relevance: MEDIUM`, `correctness: UNVERIFIED` — LLM synthesis, used only where
  UniProt or PMID:10745006 corroborate). It is also now cited as `supported_by` on the
  `response to nutrient` IBA, where it genuinely does support the claim
  [file "BCKDK is upregulated under nutrient-excess conditions and suppressed during
  nutrient scarcity or catabolic stress"].

**GO:0007584 response to nutrient (IBA)** — kept `KEEP_AS_NON_CORE`, but the reasoning is
now grounded in the PAINT data rather than assertion: the IBD sits at
`PANTHER:PTN000178891` in PTHR42980, is seeded by a *single* rat descendant (RGD:2197) and
dates from **2017**, while the same node's GO:0009083 was refreshed in 2026 from five
seeds across plants, insects and mammals. In the family review this node/term pair is
assessed `TOO_DEEP`: the node is ancestral to bacterial and plant members for which a
whole-organism dietary response is untestable. For human BCKDHB itself the term is
harmless and defensible, so it stays rather than being removed — pruning belongs at the
family level.

**Not changed after re-checking** — the five bare `protein binding` IPIs stay
`MARK_AS_OVER_ANNOTATED` (all WITH/FROM P12694); GO:0032991 stays `MODIFY`→GO:0160157;
the three granular Leu/Ile/Val catabolic-process IEAs stay `ACCEPT` (RHEA:13457/84639/84643
cover all three branched-chain 2-oxo acids). Nothing was downgraded on the strength of an
abstract-only cache — PMID:10745006, PMID:9582350 and PMID:3593587 are all abstract-only
here and their curator annotations were deferred to.

**Family context** — `interpro/panther/PTHR42980/PTHR42980-review.yaml`. BCKDHB is *not*
IBA-free in the fetched GOA: it receives all three of the family's PAINT assertions
(GO:0009083 20260530, GO:0160157 20250214-node, GO:0007584 2017). Note that P21953 appears
in its own WITH/FROM for two of them — that is the expected marker of a node seeded on the
target's own experimental annotation, not circularity. The real gap is that PTHR42980 has
**no molecular-function IBD at all**, so GO:0003863 — the term with three independent
experimental annotations on this gene — does not propagate to any ortholog.


## 2026-09-30 BCKDHB source and mechanism reassessment

All 41 source assertions remain, with 15 missing supporting-entity lists restored by the normal GOA projection. Two pre-existing authored cofactor-binding annotations remain separately identifiable, giving 43 rows: 34 ACCEPT, six KEEP_AS_NON_CORE, one MODIFY and two inherited NEW. No additional process or annotation is proposed. The five supported alpha-chain interaction records are retained as non-core under the supplied ActionEnum; lack of a more specific assay-grounded replacement is not evidence that an interaction is wrong.

One core describes BCKDHB's participation in the shared alpha2-beta2 E1 active sites. The beta chain contributes ThDP contacts and catalytic chemistry; His146-beta is the numbering used in PMID:12902323, not a newly asserted precursor coordinate. E1 decarboxylates branched-chain ketoacids and reductively acylates the DBT lipoyl group. DBT and DLD perform the subsequent CoA-transfer and reoxidation steps. Alpha-chain phosphorylation regulates assembled E1 and is not a separate beta-chain kinase or phosphatase function. The overall complex oxidation follows reversible transamination.

Six UniProt potassium-binding features describe coordinating residues, not six separate potassium sites. ThDP binding is supported within the assembled alpha/beta active site rather than as an independently demonstrated activity of isolated beta protein. No magnesium-binding annotation is introduced. A short IBA donor list is not a weak phylogenetic argument, and inclusion of the target among experimentally grounded descendants is legitimate. No PAINT-node reconstruction is claimed here.

Both UniProt products are preserved. P21953-2 replaces canonical residues 212–218 and lacks residues 219–392; matching isoform numbers do not establish equivalence to RefSeq transcripts. Its import, assembly and retained enzymatic activity remain questions. The familial leader-region frameshift in PMID:2022752 is not treated as a clean mitochondrial-import experiment, and the reported residual complex activity is approximately 6%, not universally zero. That normal cache is abstract-only despite its repeated Full Text heading.

The complete cached primary abstracts and relevant UniProt features were read, along with official human 1DTW metadata; no new coordinate, density, figure, supplement or full-paper analysis is claimed. Specific interactome and mitochondrial-proteomics supplementary rows were not inspected. The generated Falcon report remains unchanged as a source of leads, not as primary verification. Its incorrect NAD+ regeneration wording and unsupported extramitochondrial generalizations are superseded by the bounded account here. Historical notes are retained.

All ten normal Reactome records were imported through Source94 after the preserved original local retrieval failed. Their normal bodies were reassessed before this proposal was generated. Their reaction descriptions are interpreted at their actual subunit and complex level; database labels for other enzymes do not establish autonomous BCKDHB chemistry. The precise reading scope and any event wording discrepancy are recorded per reference. This integration adds no verbatim quotation.

Reactome R-HSA-5693153 has disputed beta-subunit wording: the phosphorylation-loop evidence identifies E1 alpha. The ten recovered short caches do not expose explicit compartment fields; retained matrix annotations also rely on the independently read human UniProt/E1 evidence.


### Validation of the integrated review

The focused `just validate human BCKDHB` command passed with six advisories: five supported generic protein-binding records retained as non-core under the supplied ActionEnum, and one noting that annotations cite primary/database evidence rather than the unchanged generated Falcon report. These advisories do not indicate an unsupported interaction or require a new molecular-function claim. Rendering passed, and the generated HTML is checked against the reviewed YAML. No global validation pass is claimed.


## 2026-09-30: evidence anchors and mitochondrial compartment

The two inherited NEW cofactor/ion-binding assertions and the single core function now include short verbatim anchors. The immutable UniProt precursor152 feature identifies the beta-chain thiamine-diphosphate contact shared with alpha; the PMID10745006 abstract locates the second structural potassium ion in beta; and the PMID9582350 abstract supports the assembled wild-type alpha2beta2 enzyme. This restores machine-checkable evidence while preserving the distinction between deposited structural interpretation and an independent inspection of atomic coordinates [PMID:10745006; PMID:9582350]. The local UniProt record is also quoted for its explicit matrix location.

The ten Reactome-sourced annotations concern mitochondrial matrix localization. Their reasons now lead with that compartment and its independent UniProt corroboration, rather than reaction summaries. The fetched summaries do not expose a compartment field. Five are ordinary pathway events; R-HSA-9865115, R-HSA-9865121, R-HSA-9907572, R-HSA-9912480 and R-HSA-9912527 are disease-variant events. Earlier references to normal caches meant the standard machine-fetch procedure, not that each event represented normal physiology. The existing PPM1K/E1-beta description dispute remains explicit and does not invalidate matrix localization.

The biological summary restores the supported EC1.2.4.4 designation and the 24-subunit cubic DBT core. All41 source assertions, both inherited NEW entries, both alternative products and all decisions remain unchanged. Supported generic interactions retain the supplied ActionEnum's non-core treatment; no evidence-free replacement activity is introduced to suppress a policy advisory. Final focused validation and independent review are recorded separately.


## Follow-up validation, 2026-09-30

The independently reviewed follow-up passes focused validation (six warnings), history validation, and rendering. Five warnings concern supported generic binding retained as non-core under the supplied action definitions; the other records that direct primary/database sources, rather than the unchanged generated report, support annotation decisions. All 41 source assertions, two inherited NEW assertions and two products are preserved. No new global validation pass is claimed.

## Generic binding policy cleanup, 2026-10-05 UTC

The five bare BCKDHA GO:0005515 interaction rows are now REMOVE under the codified generic-binding policy. This removes an uninformative generic term rather than the E1 alpha/beta partnership itself: each row preserves its original reference, IPI qualifier and P12694 supporting entity, and the BCKDHA partnership remains captured by the E1 heterotetramer rows and the contributes_to GO:0003863 rows.

No replacement molecular function is introduced for the physical association alone. Existing-annotation totals after this cleanup are 34 ACCEPT, 1 KEEP_AS_NON_CORE, 1 MODIFY, 5 REMOVE and 2 NEW across 43 rows; the only remaining KEEP_AS_NON_CORE row is the structural potassium-binding proposal.


## 2026-10-09: source-specific binding review under the project instruction

This entry supersedes the October 5 binding-policy removal and the earlier authority attributed to the ActionEnum alone. The user's explicit [ClinGen project instruction on published main](https://github.com/ai4curation/ai-gene-review/blob/f7dc8b60bf8be80744f75955c3c1a3c16bd73888/projects/CLINGEN_MENDELIAN.md#curation-instructions) states:

> retain a supported, biologically correct `GO:0005515` (protein binding) annotation as `KEEP_AS_NON_CORE` when no evidence-backed, more specific replacement has been established.

All five BCKDHA interaction assertions are restored to KEEP_AS_NON_CORE after checking their individual sources. The three structural citations were checked against their complete cached abstracts, publication-specific IntAct records and primary RCSB citation/entity metadata:

| Original source | Example deposited structure | Verified human protein entities |
| --- | --- | --- |
| PMID:12902323 | [1OLS](https://www.rcsb.org/structure/1OLS), IntAct EBI-1036952 | P21953 / P12694 |
| PMID:15166214 | [1V1R](https://www.rcsb.org/structure/1V1R), IntAct EBI-1039093 | P21953 / P12694 |
| PMID:15576032 | [1X7W](https://www.rcsb.org/structure/1X7W), IntAct EBI-1041254 | P21953 / P12694 |

These are checks of deposited source/partner identity and crystallographic-association provenance. They do not claim a new reading of complete articles, atomic coordinates, density, interfaces or assay controls. The alpha-chain phosphorylation mechanism remains distinct from the beta-chain contribution to the shared active site. The inspected evidence does not justify replacing all of these associations with a newly inferred heterodimerization or enzyme-regulation activity.

The [official BioPlex release page](https://bioplex.hms.harvard.edu/interactions.php) assigns the directed networks to the 2017 and 2021 publications. The [BioPlex 2.0 HEK293T file](https://bioplex.hms.harvard.edu/data/BioPlex_2.0_293T_DirectedEdges.tsv) (PMID:28514442) and [BioPlex 3.0 HEK293T file](https://bioplex.hms.harvard.edu/data/BioPlex_3.0_293T_DirectedEdges.tsv) (PMID:33961781) each contain BCKDHB, GeneID 594, as bait and BCKDHA, GeneID 593, as prey. This resolves the exact pair and cell assignment left uninspected in the earlier notes. AP-MS establishes complex association without identifying a binary interface. Representation in both releases is not counted as independent experimental replication. No matching edge was found in the inspected BioPlex 3.0 HCT116 directed network; a missing reported edge does not establish absence of the biological interaction.

The source linkage was checked separately for each assertion; none is restored solely because another paper establishes the alpha/beta complex. No new scientific quotation or annotation is added. All 41 original source assertions, the two inherited NEW cofactor-binding entries, both alternative products, existing supporting references and quotations, and the shared-active-site core remain intact. Current totals are 34 ACCEPT, six KEEP_AS_NON_CORE, one MODIFY and two inherited NEW across 43 entries.

Correction to the October 5 journal: the pre-existing non-core contextual annotation is GO:0007584 response to nutrient. GO:0030955 potassium ion binding remains one of the two inherited NEW entries. Historical notes and source caches are preserved.
