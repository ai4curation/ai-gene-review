# Assimilatory sulfate reduction comparative audit

## 2026-10-26 — scope, panel and source survey

The existing module contains 26 unique protein exemplars across Pseudomonas,
Escherichia coli, Mycobacterium and two yeasts. Eighteen had existing reviews;
eight bacterial exemplars needed normal seeding. The agreed final panel has
29 proteins: preserve the represented activities, correct the mycobacterial
strain accession, and add Arabidopsis APS1 (Q9LIK9, At3g22890), APR1 (P92979,
At4g04610), and SIR (Q9LZ66, At5g04590). These exact accessions matter: APS1
also names a starch-metabolism enzyme, and SIR aliases FERONIA. Searching ATPS1
can retrieve PARALLEL SPINDLE 1 rather than ATP sulfurylase.

Natural review partitions are: yeast MET3, MET14, MET16, TRX1, TRX2, MET10,
MET5 (7); SCHPO sua1, met14, met16, trx1, met10, sir1 (6); PSEPK cysD, cysNC,
cysH, cysI, fpr-I (5); ECOLI cysD, cysN, cysC, cysH, cysJ, cysI (6); PSEAE
cysH (1); MYCTU sir (1); and the three plant proteins. Parent/other reviewers
own individual annotations. This module pass does not edit gene reviews.
The review and project-management workflows were applied; the fungal reviewer
provided an independent annotation-reviewer consultation on redox donors and
complex contributions. Existing OpenScientist material is discovery context,
not primary biological evidence.

### Corrected identity and family scope

The old P9WJ02 exemplar is CDC1551/Oshkosh SIR_MYCTO, with by-similarity
functional statements. It was described as though directly characterized
H37Rv. The agreed correction replaces it with P9WJ03, H37Rv Rv2391 (sir,
also sirA/nirA), rather than manufacturing another required representative.
PMID:15917234 describes the structural/biochemical protein; PMID:17644602
uses purified M. tuberculosis SirA but performs native deletion/rescue in
M. smegmatis. The latter kinetics use reduced methyl viologen. They establish
substrate specificity, not direct native ferredoxin pairing. The proposed
external ferredoxin-binding site is distinguished from a measured handoff.

UniProt REST and the official PANTHER ontology verified the new plant
placements: APS1 PTHR11055:SF46, APR1 PTHR46482:SF9, SIR PTHR11493:SF47.
The normal member index was built and refreshed after introducing the new
accessions. The official SF47 name is “SULFITE REDUCTASE [NADPH] SUBUNIT BETA”
even for plant ferredoxin SIR; this is why donor architecture cannot be read
from a family label. Existing family reviews likewise require functional
filters for PTHR42700 sulfurylases and PTHR46509:SF1 sulfonucleotide reductases.
No new PAINT node or evolutionary placement was guessed.

### Substrate route is distinct from redox architecture

PMID:10613872 full text establishes that purified P. aeruginosa CysH reduces
APS, not PAPS, with supplied thioredoxin. The native cysH disruption and
E. coli complementation are distinguished from KT2440 ortholog transfer.
PMID:9653199 full methods/results establish GSH-dependent Arabidopsis APR1:
its reductase and fused C-terminal redox domains cooperate, and GSH production
is required for APR1 complementation of E. coli cysH. The fused domain is
functionally glutaredoxin-like despite sequence similarity to thioredoxin.
Its isolated-domain protein-disulfide activities are not assigned wholesale
to the intact APR protein. GO:0033741 was verified live in QuickGO and supplies
the appropriate glutathione-dependent activity for the new plant route.

The prior universal thioredoxin wording is removed. Having APS kinase does
not prove that a genome uses PAPS reduction: plant PAPS supports sulfation
while primary reduction proceeds through APS. The ONE_OR_MORE route selector
now requires demonstrated complete routes, not kinase presence alone. Plant
APS1 support includes PMID:24027241 native allele/disruption and sulfur-flux
experiments. PMID:7487067 provides family comparison and complementation;
its purified kinetic enzyme was APS3, not APS1. PMID:30825314 is a structural
review used for broader plant context rather than proof of each target assay.

### Sulfite-reductase donors and complexes

PMID:23794620 was normally force-fetched but remained abstract-only. Its full
text was read online at https://pmc.ncbi.nlm.nih.gov/articles/PMC3754593/.
FinR/FprA perturbation and E. coli CysJI rescue support a Pseudomonas electron
supply system, with major experiments in DSM3601. They do not identify the
immediate carrier for KT2440 CysI. The full text discusses FprA preference for
flavodoxin and FprB preference for a ferredoxin. A generic Fpr-to-ferredoxin-to-
CysI chain would therefore overstate the evidence. The module now separates
an Fpr-linked, carrier-unresolved variant from the ferredoxin-linked variant.
For the Pseudomonas catalytic role it uses specific free text rather than an
unsupported donor-specific GO identifier. GO:0016002 was verified obsolete
in QuickGO; it is not used as a workaround.

PMID:20424176 full text provides native Arabidopsis SIR mutant,
complementation and sulfur-flux evidence. Its reduced-dye extract assays are
not presented as direct native donor-pairing experiments. The plant and
mycobacterial family classification is integrated with target evidence and
explicit assay limits; sulfite and nitrite reductases are not interchangeable
merely because they share a siroheme fold.

PMID:26088143 full results establish E. coli CysJ/CysI reconstitution, activity
and the reported alpha8beta4 assembly. PMID:40140349 (peer-reviewed 2025 paper,
not the preceding preprint) resolves engineered minimal-complex interfaces.
Its minimal dimers do not complement CysJ-deficient cells and are not treated
as a native dimeric stoichiometry. Domain binding and complete electron-transfer
competence are distinct. The fungal enzyme remains separate: PMID:6751400
supports the purified yeast alpha2beta2 model; PMID:7928966 identifies Met10's
FAD/NADPH-associated architecture. Positive flavodoxin-domain evidence on
Met5/sir1, rather than simply absence on Met10, supports the different FMN-domain
distribution. This inference is not described as an isolated-subunit FMN assay.

### Fungal reductant qualification

PMID:3060034 reports a purified thioredoxin-fed PAPS-reductase reaction;
PMID:2026619 reports methionine auxotrophy of the tested trx1 trx2 mutant.
However, PMID:10844700 (cached abstract) reports assimilation under low-ROS
conditions without both thioredoxins. Further glutaredoxin deletion increases
assimilation rather than demonstrating that a particular glutaredoxin supplies
Met16. The donor is unresolved in that evidence. The module therefore retains
the characterized thioredoxin edge without universal exclusivity. The older
thioredoxin-first kinetic model is not silently elevated to settled covalent
chemistry. Fungal reviewer is checking newer mechanistic/structural sources.

### Research provenance and current state

Normal module research was attempted with Falcon (authentication failure) and
Perplexity-lite (HTTP401 insufficient quota). Neither produced a report; no
provider-named content was written manually. Logs are in
`.cache/module-audit-logs/sulfate-module-falcon.log` and
`sulfate-module-perplexity-lite.log`. Normal source caching initially hit
HTTP429 for PMID:20424176; the parent source batch subsequently fetched its
full text successfully. Cached publications were never manually authored.

The first revised grounding check passed with advisories for pending gene
reviews, broad-family functional limits, the honest carrier-unresolved free-text
activity, and an initially missing APR1 member-index entry. Schema issues in
that first draft were corrected. Final reference, family, member-conformance,
schema, render and history checks follow integration of the individual reviews;
this entry records the evidence survey and implemented architecture, not final
whole-panel completion.

The fungal reviewer recovered PMID:11319255's genuine publisher full text via
the normal ReferenceFetcher URL pipeline, yielding
`publications/url_https___oup.silverchair-cdn.com_article-minimal_1018655.md`.
Results and **Figure 3F/G** explicitly identify yeast P47169 and its FMN-domain
fusion, alongside Met10's FAD/NADP modules. The old pombe accession O14167 is
not assumed to equal present Q1K9C2; current sir1 has independent PF00258
support. The module cites the PMID for bibliography and the actual URL source
for its literal full-text quotation. This avoids claiming that an abstract-only
PMID cache contains the inspected full-text passage.

### Module draft validation and provenance

The integrated architecture contains three top-level steps (five parts including
the nested PAPS route), nine alternatives, twelve annotons, five connections,
29 unique representatives and 26 curated references. There are 28 literal-quote
occurrences across evidence and reference findings, including repeated quotes.
Revised schema validation passes; grounding/source validation passes with 14
advisories at this stage: eight pending member-function reviews, three broad-
family scope notices, two views of the unresolved-carrier function without a GO
ID, and the InterPro namespace notice. PANTHER member checks now resolve all
new exemplar families. Live InterPro API verification additionally confirmed
IPR011779 “Sulphate adenylyltransferase, large subunit” and IPR011798 “Adenosine
5'-phosphosulphate reductase”; their labels were corrected to the official
spelling even though the configured ontology validator does not check that
namespace. No identifier was guessed or substituted.

Helper history:
`history/modules/aps_dependent_assimilatory_sulfate_reduction/2026-10-26T033829Z-codex-92fb55.yaml`.
The history records the module work and explicitly leaves final individual-review
integration outstanding. APR1 independent QA was completed separately and its
focused validation passes; the parent owns its session history/render.

## 2026-10-26 — independent comparative biological QA

Read every reaction, alternative and connection against the native and comparative
sources, the complete fungal reviews, and family reviews. The 29-member panel and
five connections are preserved. The substrate sequence is sound: sulfurylase
supplies APS; direct APS reduction or kinase followed by PAPS reduction supplies
sulfite; the terminal reductase supplies sulfide. The broad bacterial, fungal and
green-plant envelope is a union of supported implementations, not a universal
pathway-presence claim. No member or annotation was added to clear validation
advisories. Other agents retain ownership of their individual gene panels.

Corrected residual assertions and strengthened scope:

- A remaining thioredoxin function description called it an obligatory donor.
  It now distinguishes the purified assay from the conditional native bypass in
  PMID:10844700. The reducing-equivalent input edge remains valid without donor
  exclusivity or an invented replacement donor.
- CysD/CysN is the interacting catalytic/GTPase unit, not necessarily a whole
  heterodimeric holoenzyme. The yeast structural paper discusses higher-order
  bacterial assemblies; PMID:16387658 characterizes P. syringae. No fixed CysD/CysN
  stoichiometry is imposed on E. coli and KT2440. CysNC's kinase-like domain is
  explicitly separated from evidence for an operative PAPS-reduction route.
- PTHR46482:SF9 contains the bacterial APS-reductase representatives as well as
  plant APR1. The bacterial external-thioredoxin selector now has its supported
  functional restriction, while the plant selector requires glutathione-fed
  activity and the fused redox architecture. The shared fold/name alone cannot
  identify donor choice.
- PTHR11493:SF47 contains plant ferredoxin SIR and NADPH-complex hemoproteins.
  The CysI/Met5 selectors now explicitly require contribution to the NADPH complex
  with their named partner architecture. This is not direct NADPH binding or
  autonomous whole-reaction activity by the hemoprotein. The validator's resulting
  annotation-supported/core advisory does not negate the existing contributes-to
  cores and is not a reason to rewrite those correct gene reviews.
- The free thioredoxin-family descriptor is retained. Official classification and
  UniProt placements differ (PTHR10438:SF468 versus PTHR46115); the old rationale
  that a surprising family name is enough to reject an ID was removed. Other
  declared PANTHER family/member placements agree with the normal index. IPR011779
  matches both CysN/CysNC target records; IPR011798 supports the bacterial APS
  reductase fold, with donor specificity independently constrained.
- EXACTLY_ONE describes selection of a concrete reaction implementation, not
  whole-genome exclusivity. The Fpr-to-CysI connection is explicitly recorded as
  having an intervening-carrier knowledge gap; it does not assert physical contact.

The full primary PMID:15917234 article was independently read from the author
upload at
https://www.researchgate.net/publication/7824990_Siroheme-_and_Fe4-S4-dependent_NirA_from_Mycobacterium_tuberculosis_Is_a_Sulfite_Reductase_with_a_Covalent_Cys-Tyr_Bond_in_the_Active_Site .
Methods and Figure 6 use artificial methyl viologen, reduced with dithionite;
the external ferredoxin-binding region is a structural proposal. The normal URL
fetch returned HTTP403, so no full-text cache was fabricated. The module retains
the supported SirA ferredoxin-linked enzyme-class inference, explicitly distinct
from native partner identification. The native deletion/rescue in PMID:17644602
is M. smegmatis, whereas the purified target is M. tuberculosis H37Rv.

Plant donor evidence was strengthened independently of the Arabidopsis dye assay:
normal fetches cached PMID:26920048 (primary maize SiR-Fd complex structures,
interface mutagenesis, Fd-dependent activity and binding) and PMID:11132635
(review of maize enzyme/Fd-mutant work), both abstract-only. Their abstracts
explicitly describe the relevant results. These support the comparative plant
mechanism; neither is mislabeled as an Arabidopsis pairing assay. The Arabidopsis
native-flux/complementation evidence remains PMID:20424176. The inactive cloned
protein in PMID:8695637 is not used as activity confirmation.

The E. coli sulfite-reductase alpha8beta4 count remains attributed to the
PMID:26088143 reconstitution, with the current UniProt alpha8beta8 statement
acknowledged as a source conflict. PMID:40140349 engineered minimal dimers do
not settle a replacement native stoichiometry. The fungal alpha2beta2 model is
likewise attributed to the purified yeast system, not imposed on every fungus.
Positive beta flavodoxin-domain support remains computational placement rather
than a direct isolated-subunit FMN-binding assay.

No further biological blocker was identified. Source-specific donor limits,
mixed-family restrictions and unresolved carrier identity are preserved rather
than converted into artificial certainty.

## 2026-10-26 PR #5560 evidence follow-up

Canonical citation identity, exact quoted subunit-domain evidence, NOT-localization
reasoning and explicit residual knowledge gaps were repaired in the member reviews.
The PMID:23794620 full text was recovered normally. PMID:11319255 remains abstract
only after normal refresh/warming; its inspected publisher Results/Figure 3 are
quoted in a reproducible source-analysis artifact with the durable DOI.

Independent review of item 8 retains the E. coli CysD/CysN hydrogen-sulfide
biosynthetic core and CysI cysteine-biosynthetic participation. Live GO:0070814 and
GO:0019344 definitions cover reactions **and pathways** resulting in the product.
CysD adenylates sulfate and CysN couples GTP hydrolysis to APS synthesis
[PMID:2828368; PMID:8003495]; CysI reduces sulfite to the sulfide used by cysteine
synthase. These gene products perform chemical work within the pathway. They are
neither passive substrates nor genes whose only evidence is necessity. This does
not assign sulfite-reductase activity to CysDN or cysteine-synthase activity to CysI.
The project participation rule explicitly permits catalysing a step, and the schema
does not restrict directly_involved_in to the terminal product-forming reaction.

Live UniProt cross-references reconfirmed the initially surprising PANTHER
placements: E. coli CysC/P0A6J1 is PTHR11055:SF63, whereas yeast MET14/Q02196 and
S. pombe met14/Q9P7G9 are PTHR11055:SF1. They are not transposed; official names
are retained and the biochemical selector restricts the family role.

Review suggestion 15 was already represented: the second TRX1 core function
explicitly carries GO:0000103 with thioredoxin-to-PAPS-reductase evidence. No
redundant core assertion was added.


## 2026-10-26 approved-review citation residuals

Replaced the silverchair CDN URL reference/source identifier with canonical PMID:11319255 plus the already committed reproducible MET5 source-analysis artifact for full-text quotations. The bibliographic title remains the exact PMID title. The primary Results quotation is now accompanied by the Figure 3F/G legend identifying yeast P47169 (Met5) and Met10; the old pombe accession is still not equated to current sir1. This repairs citation identity and target traceability without changing any activity, family/member, compartment, reaction or connection. The artifact SHA256 was verified against the existing normally fetched publisher cache; no publication cache was edited. Gene-level FMN evidence received the same identifying legend without action or payload changes.
