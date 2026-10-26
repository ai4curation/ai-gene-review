# Aspartate, asparagine and alanine: literature and taxon audit

## 2026-10-26 — boundary and chemistry

The module models a connected aspartate/asparagine formation-and-turnover unit,
with alanine transamination as a parallel optional branch. AspAT plus
glutamine-dependent ASNS form the required core; asparagine hydrolysis is optional.
Alanine chemistry is retained because it was part of the original module, but it
does not gate asparagine synthesis. These are enzyme-capability routes, not claims
that all reactions carry flux simultaneously. Transport and precursor supply can
limit the route even when its catalysts are present.

Three kinds of chemistry must remain distinct:

- AspAT and AlaAT exchange amino nitrogen between glutamate and a keto acid.
- ASNS uses glutamine **amide** nitrogen and ATP, yielding glutamate, AMP and
  diphosphate. Human N-terminal-cysteine mutagenesis separates glutamine hydrolysis
  from ammonia-dependent synthesis in vitro [PMID:2573597]. Recombinant human
  enzyme can use free ammonia [PMID:2564390]; that does not establish a separate
  native pathway or a glutamate-donor reaction.
- Asparaginase hydrolyses asparagine to aspartate and ammonium without a glutamate
  cosubstrate. It is not the reverse of the ATP-consuming ASNS reaction.

AspAT-to-ASNS is precursor continuity through aspartate. Arabidopsis ASP2 alleles
alter both Asp and Asn pools [PMID:12068109]; yeast ASN1/ASN2 double disruption
abolishes asparagine prototrophy under the tested conditions [PMID:8951815].
These results and enzyme chemistry support the connection, without demonstrating
physical channeling. Asparaginase-to-AspAT explicitly uses the **reverse** AspAT
direction; extracellular Asp3 additionally requires transport. The yeast
assimilation scheme in [PMID:36040324] makes these distinctions explicit.

The root taxon envelope is Eukaryota, demonstrated here by budding and fission
yeasts, human and Arabidopsis. It is neither universal presence nor an exhaustive
inventory of eukaryotic amino-acid metabolism. E. coli ansA and ansB remain
individually reviewed biochemical comparators; they are no longer participant
exemplars of a eukaryotic leaf. In particular, bacterial ansB must not inherit a
fungal cell-wall-bounded periplasm annotation.

## Comparative literature and reference assessment

Searches covered comparative aminotransferase evolution, plant aspartate/ASNS
metabolism, asparaginase structural classes and later ASP3 evolutionary work.
Normally fetched source caches were read; provider attempts and failures for
individual genes are documented in their notes, separately from this manual work.

| Source | Assessment and mined implication |
| --- | --- |
| PMID:35697072, aminotransferase evolution review | Full text; relevant to family specialization and promiscuity. A family name or an in-vitro side reaction does not establish the dominant native substrate or direction. |
| PMID:33624365, revised asparaginase nomenclature | Abstract available; historical bacterial-type and plant-type class names do not delimit organismal distribution. Detailed mechanisms are supported separately. |
| PMID:34258001, structural asparaginase review | Full text; separates Class 1 enzymes from Class 2 N-terminal-nucleophile hydrolases and discusses potassium-dependent plant enzymes. It does not prove the same specificity in every member. |
| PMID:31998641, ASNS review | Full text; useful for coupled glutamine hydrolysis and ATP-dependent amidation. Its physiological glutamine requirement is qualified by direct recombinant-enzyme evidence for ammonia use in vitro. Cancer responses are outside this catalytic boundary. |
| PMID:24902885, plastid AspAT review | Abstract available; identifies conventional and bifunctional plastid AspAT implementations. Specific Arabidopsis assignments use primary studies. |
| PMID:22776361 versus PMID:36040324 | The older recent-horizontal-transfer interpretation is challenged by later sampling and synteny favoring ancestral ASP3 followed by loss. Strain restriction remains supported. |
| PMID:40940428, 2025 Arabidopsis substrate survey | Primary abstract available; 38 enzymes and 4,104 reactions plus metabolic modeling demonstrate why substrate promiscuity deserves attention. It is not used to invent an activity or native flux for a named exemplar. |

The 2010 review *Biological functions of asparagine synthetase in plants*
(DOI:10.1016/j.plantsci.2010.04.010) was located in the literature search. The
module's specific plant assignments instead use cached target studies, avoiding
unverified extrapolation of donor preference from a general review.

## Families and plant implementations

The original module already had family groundings in `family_terms`; these were
not missing IDs. Single-family descriptors now use `term`, and every leaf is
restricted by its molecular function. Official PANTHER labels were read from
`panther.obo`, and member placements from fetched classifications. Labels that
sound like another compartment were not rewritten to fit expectations.

- PTHR11879 covers the selected conventional AspATs; fungal, human and plant
  cytosolic proteins occupy different subfamilies. ASP2 adds a native plant
  cytosolic example [PMID:9535706, PMID:12068109]. Aat2 predominance is specific to
  the nitrogen-starvation experiments [PMID:33397945], not every growth condition.
- ASP5 (P46248) is PTHR11879:SF46, whose official name says **CYTOPLASMIC** despite
  this protein's plastid evidence. The module uses the broader supported plastid
  location; the older recombinant study considered amyloplast versus chloroplast
  assignment tentative [PMID:9535706]. Stronger evidence includes import of the
  Arabidopsis precursor into viable pea chloroplasts [PMID:7766905] and native
  Arabidopsis AAT3 assignment [PMID:12068109]; the assay organism and target
  organism are kept distinct. ASP5 retains AspAT activity but does not
  acquire prephenate activity merely by proximity to the next implementation.
- PAT (Q9SIE1; At2g22250) is PTHR46383:SF1. Primary comparisons distinguish its
  bifunctional activity from ASP5 [PMID:20883697, PMID:25070637]. The correction
  [PMID:28011691] revises mutant identities and mutant-specific claims; wild-type
  bifunctional chemistry remains supported. No bacterial-transfer evolutionary
  claim is inferred from these assays. The release-19 PANTHER classification
  instead places Q9SIE1 in PTHR43795:SF2; the current UniProt placement is retained
  explicitly, without a guessed reassignment or override. PAT's aromatic-amino-acid reaction is
  outside this module.
- PTHR11772 covers the selected glutamine-dependent ASNS proteins. Arabidopsis
  ASN2 broadens sampling without treating its nitrogen-allocation phenotype as a
  purified donor-specific kinetic comparison.
- Yeast Asp1/Asp3 are Class 1 PTHR11707 enzymes. The existing PANTHER/UniProt
  classification discrepancy is retained explicitly in the family review; it is
  not repaired by mechanically moving these proteins to an incongruous family.
- ASPGB1 (Q8GXG1), PTHR10188:SF13, supplies a structurally distinct plant Ntn
  asparaginase. The later peptide study [PMID:22127737] qualifies an Asn-only
  interpretation of the earlier characterization [PMID:16705405]. Potassium
  activation belongs to the assayed exemplar, not every Ntn enzyme.
- PTHR11751 supplies AlaAT. Arabidopsis ALAAT1 contributes to post-hypoxic alanine
  breakdown [PMID:17319845]. Budding-yeast respiratory versus fermentative use is
  conditional [PMID:19396236], and inactive Alt2 is not admitted by family
  membership [PMID:23049841].

There are 25 eukaryotic module exemplars plus two bacterial comparator reviews,
27 genes in the review panel. Four identical S288C ASP3 copies are preserved as
distinct genes, not counted as four independent biochemical experiments.

## Source-model and phylogenetic checks

The five associated live GO-CAM JSON products were retrieved successfully and
compared with their cached source assertions. The three YeastPathways models had
new distinct activity identifiers where older cache entries reused reaction IDs;
they were refreshed with the normal `fetch-gocam --force` command. AAT2 and ASP3-1
links now identify the correct activities. The asparagine-biosynthesis model has
four RO:0002413 links connecting AAT1/AAT2 to ASN1/ASN2; the older blanket assertion
that it contains no causal links is no longer applicable. Its AAT1 cytosolic
placement and the degradation model's ASP3 cytosolic placements remain qualified
against target-specific compartment evidence.

The PomBase models retain matrix maa1/alt1, cytosolic caa1/asn1 and their annotated
process contexts. The physiological direction of maa1 is qualified using
[PMID:39502420]. Absence of a budding-yeast-length targeting peptide does not
disprove the curated fission-yeast alt1 assignment. Upstream pyruvate-carboxylase
activities are outside this module boundary; this does not itself invalidate
their broader process annotations.

PTHR11707's periplasmic-localization assessment was revised to remove reliance on
settled recent ASP3 transfer. The Asp1/Asp3 compartment split remains independent
evidence for reviewing the ancestral assertion. Family/subfamily assignments and
all PAINT node IDs, asserted terms, taxa, snapshots, seeds and verdicts were
preserved; neither donor count nor the evolutionary scenario is used as a proxy
for node quality.

## Validation status

Module schema/quote checks and refreshed member-index validation pass. Three
remaining membership advisories report the existing PAT and yeast-asparaginase
classification disagreements; both source placements are retained. All 46 corpus module-logic tests passed;
13 targeted presence/activity cases pass after making the parallel alanine branch
optional. Empty, AspAT-only, ASNS-only, hydrolysis-only, alanine-only and
bacterial-comparator-only contexts fail; demonstrated yeast/human/plant
AspAT-plus-ASNS implementations satisfy the catalytic core. These cases do not
test transport, expression, compartmental coupling or in-vivo flux.

All 27 individual reviews now pass focused strict/term/source checks, with their
548 original annotation payloads preserved: 323 ACCEPT, 110 MODIFY, 65 non-core,
20 REMOVE, 25 UNDECIDED and five over-annotation assessments. No NEW or PENDING
rows remain. The original raw records are retained except normal documented
source-cache refreshes. Independent module QA passes: nine family labels, 25
member placements, 12 activity links across five models and all four source
AspAT-to-ASNS edges were checked. The family correction preserves the original
PAINT assertions and verdicts. Full repository validation is running and remains
the pre-PR gate; only an approved and verified merge completes this audit.

Final negative-annotation audit: all six NOT rows in the27-gene panel were read.
The four localization exclusions remain UNDECIDED because exact negative
compartment evidence was not established; ASP5's two experimentally tested
negative prephenate activities are ACCEPT. Three initially mismatched
localization rationales and their associated reference findings were corrected
before integration; the source payloads were unchanged.
