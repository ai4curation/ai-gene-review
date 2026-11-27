# ACAD8 (Isobutyryl-CoA dehydrogenase, mitochondrial) — review notes

UniProt: Q9UKU7 (ACAD8_HUMAN). HGNC:87. Gene synonyms ARC42, IBD. EC 1.3.8.5.

## Core biology (from UniProt Q9UKU7 and cited primary literature)

ACAD8 is the mitochondrial **isobutyryl-CoA dehydrogenase (IBD/IBDH)**, an FAD-dependent
member of the acyl-CoA dehydrogenase (ACAD) family. It catalyzes the third step of
**valine catabolism**: the FAD-dependent alpha,beta-dehydrogenation of isobutyryl-CoA
(2-methylpropanoyl-CoA) to methacrylyl-CoA, with electrons
passed to the electron-transfer flavoprotein (ETF).

- Function/pathway: "Isobutyryl-CoA dehydrogenase which catalyzes the conversion of
  2-methylpropanoyl-CoA to (2E)-2-methylpropenoyl-CoA in the valine catabolic pathway"
  [file:human/ACAD8/ACAD8-uniprot.txt]. PATHWAY: "Amino-acid degradation; L-valine
  degradation." [file:human/ACAD8/ACAD8-uniprot.txt].
- Catalytic activity (Rhea RHEA:44180, EC=1.3.8.5): 2-methylpropanoyl-CoA + oxidized ETF
  + H+ = 2-methylpropenoyl-CoA + reduced ETF [file:human/ACAD8/ACAD8-uniprot.txt].
- Substrate specificity: purified recombinant enzyme kcat/Km 0.8, 0.23, 0.04 uM^-1 s^-1
  with isobutyryl-CoA, (S)-2-methylbutyryl-CoA, and n-propionyl-CoA respectively
  [PMID:12359132 "Purified recombinant enzyme had a k(cat)/K(m) of 0.8, 0.23, and 0.04
  (microM(-1)s(-1)) with isobutyryl-CoA, (S) 2-methylbutyryl-CoA, and n-propionyl-CoA,
  respectively, as substrates. Thus, this enzyme is an isobutyryl-CoA dehydrogenase."].
  Thus catalytic efficiency favors isobutyryl-CoA approximately 3.5-fold over
  (S)-2-methylbutyryl-CoA and 20-fold over propionyl-CoA. Valine catabolism is the established
  physiological pathway; the alternate-substrate assays do not establish additional physiological flux.
- Cofactor: FAD [file:human/ACAD8/ACAD8-uniprot.txt: "Name=FAD; Xref=ChEBI:CHEBI:57692;
  Evidence={ECO:0000269|PubMed:14752098}"]. Crystal structure 1RX0 (1.77 A) solved with
  FAD and substrate analog (PubMed:14752098).
- Subunit: "Homotetramer, formed by a dimer of dimers" [file:human/ACAD8/ACAD8-uniprot.txt].
- Location: "Mitochondrion" [file:human/ACAD8/ACAD8-uniprot.txt]; residues 1-22 are a
  cleaved mitochondrial transit peptide. Reactome and GOA place the mature enzyme in the
  mitochondrial matrix (GO:0005759), consistent with soluble matrix ACADs.

## Identity/discovery

- cDNA cloned as a "novel member of the acyl-CoA dehydrogenase gene family", maps to 11q25,
  415-aa precursor [PMID:10524212 "A gene encoding the precursor for a novel member of the
  human acyl-CoA dehydrogenase (ACD) gene family has been isolated which maps to human
  chromosome 11q25."]. At that time function was unknown; the paper only established family
  membership by sequence similarity ("shares considerable sequence similarity with other
  members of the ACD family").
- ACAD8 identified as an isobutyryl-CoA dehydrogenase and a mitochondrial valine-pathway
  enzyme, distinct from the isoleucine-pathway SBCAD [PMID:11013134 "showed that ACAD-8 is
  an isobutyryl-CoA dehydrogenase and that both wild-type proteins are imported into
  mitochondria and form tetramers"; "indicate that ACAD-8 is a mitochondrial enzyme that
  functions in valine catabolism"].

## Disease — Isobutyryl-CoA dehydrogenase deficiency (IBDD; MIM:611283)

- Autosomal recessive; plasma carnitine deficiency and elevated C4-acylcarnitine; often
  detected on newborn screening; frequently benign/asymptomatic [file:human/ACAD8/ACAD8-uniprot.txt
  DISEASE block]. First patient homozygous Arg302Gln, stable but enzymatically inactive
  [PMID:12359132 "This encodes an Arg302Gln substitution ... The mutant enzyme was stable
  but inactive when expressed in E. coli."]. Additional variants from newborn screening for
  elevated C4-carnitine [PMID:16857760]. This is a disease-association/phenotype, not part
  of the normal molecular function — track as non-core if annotated.

## Historical ARC42 association (not in the current annotation seed)

The fetched UniProt record links ACAD8/ARC42 identification in the ARC/DRIP preparation to
[PMID:10235267](https://pubmed.ncbi.nlm.nih.gov/10235267/) and reports possible complex membership.
The publisher abstract describes the multisubunit complex's transcriptional activity, but the full
article was not accessible in this audit. The current 23-row GOA seed contains no transcription
annotation. The earlier note claiming a current DNA-templated-transcription IEA was therefore
incorrect for this source snapshot. No NEW transcription annotation is proposed, and no categorical
claim is made that ACAD8 lacks a context-dependent role based only on an inaccessible full paper.

## Interactions / proteomics annotations

- GO:0005515 protein binding IPI with UniProtKB:Q8TAG5 (VSTM2A) from BioPlex AP-MS
  [PMID:33961781]. The current policy removes the generic binding assertion when no informative
  mechanistic molecular function is established. The fetched IntAct cross-reference records two
  experiments. REMOVE does not deny the physical association; the exact supplementary experiment
  is not reconstructed from the cached narrative.
- GO:0005739 mitochondrion HTP from the MitoCoP high-confidence mitochondrial proteome
  [PMID:34800366] — consistent with matrix localization. The specific matrix location remains core.

## GO term notes

- GO:0003853 "short-chain 2-methyl fatty acyl-CoA dehydrogenase activity" is the GO term
  for EC 1.3.8.5 (the isobutyryl-CoA dehydrogenase reaction: a short-chain 2-methyl acyl-CoA
  -> 2-methyl-2-enoyl-CoA). This is the correct, most specific MF for ACAD8 and has three
  EXP annotations (PMID:11013134, 12359132, 16857760). Use as core MF.
- GO:0003995 "acyl-CoA dehydrogenase activity" is the parent/general MF; TAS from the
  discovery paper (PMID:10524212, when only family membership was known) and an IEA. Correct
  but less specific than GO:0003853 -> MODIFY to GO:0003853.
- GO:0016937 "short-chain fatty acyl-CoA dehydrogenase activity" is **not restricted to
  straight-chain substrates** and directly parents GO:0003853. The particular RHEA:31287 source
  maps measured propionyl-CoA oxidation, retained as a minor non-core reaction. This source-specific
  judgment does not exclude the branched-chain core activity from the parent GO term.
- GO:0016627 "oxidoreductase activity, acting on the CH-CH group of donors" — correct broader
  MF, refined to GO:0003853; broadness alone is not a reason to call catalysis non-core.
- GO:0006629 "lipid metabolic process" (TAS PMID:10524212 + InterPro IEA): broad pathway
  assignment refined to directly catalyzed L-valine catabolism. Acyl-CoA chemistry is not categorically
  outside lipid metabolism; the source does not establish an additional fatty-acid beta-oxidation role.
- GO:0006574 "L-valine catabolic process" (IEA UniPathway) is the correct core BP.


## 2026-09-26 complete annotation re-review

The existing review matched GitHub main blob `e357e75aef6b7754df2a6134d1619d14d2639403`, and no
open ACAD8 pull request was found. Its status was INITIALIZED despite 23 already adjudicated rows.
All 23 original annotation field sets were preserved. The updated decisions are 11 ACCEPT,
10 MODIFY, 1 KEEP_AS_NON_CORE and 1 REMOVE, with nine source-entity propagation audits and no NEW
annotations. The status is COMPLETE for this documented manual audit.

The PAINT source is ancestral node PANTHER:PTN000097535; the target's own experimental evidence
among descendants is not circular. Rhea reactions 44180 (isobutyryl-CoA), 48256
(S-2-methylbutyryl-CoA) and 31287 (propionyl-CoA), EC1.3.8.5, UniPathway UPA00362, InterPro domains
and UniProt subcellular-location mappings were traced against the untouched GOA and UniProt
records. ARBA and precise InterPro mapping internals were not inspected and are explicitly UNRESOLVED rather than
represented as independently validated.

Live ontology pages verified the relevant substrate-class scopes:
[GO:0003853](https://amigo.geneontology.org/amigo/term/GO%3A0003853) and
[GO:0016937](https://amigo.geneontology.org/amigo/term/GO%3A0016937). The latter permits branched
substrates and is the former's direct parent. The retained propionyl side-reaction rationale is
therefore about its particular Rhea source, not a straight-chain restriction in GO.

Broad mitochondrial annotations now refine to the matrix rather than being labeled non-core just
because they are broad. All five matrix annotations are accepted as a core location. The four
proteostasis Reactome event narratives discuss matrix substrates without naming ACAD8 individually;
the exact substrate membership was not independently reconstructed. The location is supported
independently by its explicit catalytic reaction R-HSA-70859 and human import assays. Candidate
substrate status does not give ACAD8 the protease's function. No degradation or proteostasis process
was added. MitoCoP's cached main text does not expose the ACAD8 supplementary row; this absence
was not treated as evidence against the curator's experimental localization assignment.

The PMID:12359132 abstract's mitochondrial-targeting sentence specifically concerns Arg302Gln,
which retains targeting despite lost activity. The wild-type import evidence is explicit in
PMID:11013134. These source contexts are now distinguished. The latter paper directly assays
ACAD8 despite a title emphasizing the ACADSB defect. Four core experimental/sequence papers are
abstract-only in cache; no inaccessible full-text experiment was claimed as newly inspected.
The BioPlex cache is labeled full_text_available but contains selected narrative sections; the
specific partner comes from GOA/UniProt/IntAct, not the study-wide quoted abstract.

FAD binding is retained as an annotation and integrated into the dehydrogenase core function,
rather than presented as a second independent biological role. The structure paper's public
[publisher abstract](https://www.sciencedirect.com/science/article/pii/S0021925820883811) supports
the homotetramer, FAD/product geometry and substrate-pocket interpretation. Its full text was not
retrieved; specific structural residue claims are not added. The main biological summary avoids
unnecessary clinical prognosis and uses methacrylyl-CoA without importing a stereochemical prefix
from a generalized chemical-class label.

### Research and access provenance

The required default Falcon workflow and GOA publication caching were launched concurrently.
All six seeded PMID caches were already present and confirmed by the normal fetch workflow.
The first genuine Falcon/fallback command failed before contacting either provider because uvx
could not create a temporary directory under the read-only user tool-install path (OS error1).
A coordinator-authorized retry used process-local writable `UV_TOOL_DIR`, `UV_TOOL_BIN_DIR` and
`UV_CACHE_DIR` paths under `/tmp`; this corrected that local path issue. Both provider attempts
then failed while resolving `pypi.org` for `deep-research-client`, after uv's internal dependency
retries (provider process exit2, wrapper exit1). No provider report was produced, and none was
created manually. No global configuration or permissions were changed.

Normal attempts to cache additional PMID:14752098 (structure) and PMID:10235267 (ARC) also failed
with `urlopen error [Errno 8] nodename nor servname provided, or not known`; 0/2 new publication
caches were created. Public primary abstracts were available through web search, but direct
publisher/full-text routes were inaccessible or provided only abstracts. These papers remain
background/structural context through existing UniProt provenance and the notes; the reviewed
source annotations retain their six available primary caches and five cached Reactome sources.
No source file or cached publication was hand-edited. No Git or shared project changes were made.

Logs are `/tmp/ACAD8-falcon.log`, `/tmp/ACAD8-falcon-writable-runtime.log`,
`/tmp/ACAD8-publications.log` and `/tmp/ACAD8-additional-publications.log`. Validation, rendering,
independent review and the exact publication manifest are recorded with the new history session.

The coordinator independently read all 23 annotation decisions and the core synthesis, agreeing with the biological judgments. Final citation cleanup grounds the FAD row in the available cached UniProt cofactor/structure record; the unsuccessful structural-paper fetch does not become a claim of additional primary full-text coverage. The manual full-text-unavailable flag on BioPlex reflects the incomplete narrative extraction, without altering its cached metadata.


## 2026-09-26 PR #3151 evidence-scope follow-up

The external review identified over-refinement of five mitochondrial-location
source rows. They now ACCEPT mitochondrion at the original evidence resolution;
the separately supported mitochondrial-matrix core and five Reactome matrix rows
remain unchanged. Import assays, MitoCoP and the PAINT mitochondrial node are not
represented as direct matrix-localization experiments.

Rechecked the [live GO:0016937 hierarchy](https://amigo.geneontology.org/amigo/term/GO%3A0016937):
GO:0003853 is its direct child. The broad GO activity therefore encompasses ACAD8's
core isobutyryl reaction and is now ACCEPT, while RHEA:31287 retains its narrower
propanoyl-to-acryloyl side-reaction provenance. Replacing that source reaction with
2-methyl chemistry would be incorrect. Independent biological consultation agreed
that the action should grade the asserted GO term while the reason preserves the
specific source reaction. Older sibling-review wording that describes these GO
terms as siblings is not current ontology evidence.

The lipid-to-valine replacement is explicitly a cross-branch pathway correction.
Removed the full_text_unavailable flag from the BioPlex reference: its missing
pair-specific supplementary evidence is documented separately from its available
article narrative. The transcription question now asks for a biological mechanism.
Uninspected InterPro rule details remain UNRESOLVED: source identifiers and their
protein-domain labels are recovered, but a sibling review's acceptance is not an
independent reconstruction of each mapping rule. ARBA predicates remain opaque.

All 23 original source-field sets are unchanged. Final actions: 17 ACCEPT,
5 MODIFY and 1 REMOVE; no NEW annotations. No cached source or provider file was edited.
