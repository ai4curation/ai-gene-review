# HACD1: manual primary-source research and source checks

Prepared 2026-11-12 JST. This is manual research, not a provider-generated report.
Falcon failed with an authentication error; the configured Perplexity fallback
failed with insufficient quota. Neither produced a research report. Existing
publication caches were checked without modification. The review was seeded in the registered checkout and submitted as PR #6311;
the dated follow-up below records review corrections and source checks.

## Product identity and scope

The retained UniProt B0YJ81 record distinguishes canonical HACD1 (288 residues)
from CAP/B0YJ81-2 (140 residues: canonical residues 1–125 followed by an alternative
15-residue tail). CAP lacks the canonical catalytic region. This is distinct from
the disease-associated p.Tyr248Stop truncation. UniProt's CAP inactivity statement
is not an independently inspected negative enzymatic assay. Do not assign
phosphatase activity from the former PTPLA name. Source: retained
`genes/human/HACD1/HACD1-uniprot.txt`.

## Direct enzyme evidence

[PMID:18554506](https://febs.onlinelibrary.wiley.com/doi/full/10.1016/j.febslet.2008.06.007):
the original main Methods, Results and Discussion were inspected. Human HACD1
purified from HeLa cells dehydrates C16 3-hydroxypalmitoyl-CoA. Localization was
tested against an ER marker in HeLa cells. HACD1 rescued growth and restored
sphingolipid synthesis in doxycycline-suppressed PHS1 yeast. ELOVL associations
were studied by co-immunoprecipitation in HEK293T cells. The inspected biochemical assays used C16 substrate;
they did not measure a panel of other chain lengths. Complementation supports the VLCFA elongation context
but is not a measured C18–C26 substrate panel. Supplements were not inspected.
The local publication cache remains abstract-only; access to the original main
text is recorded separately here.

Rechecked original main text on 2026-11-11 UTC. Results section 3.1 / Figure 2C:
“Introducing the HACD1 gene into SAY32 cells completely restored sphingolipid synthesis”. Discussion:
“we used only 3-hydroxypalmitoyl-CoA as a substrate due to limited commercial availability.”
These excerpts support rescue and the stated assay limit. They do not replace
the unchanged abstract-only publication cache or claim supplementary inspection.

[PMID:23933735](https://pmc.ncbi.nlm.nih.gov/articles/PMC3842179/):
the original full text and cached full text support congenital myopathy associated
with homozygous p.Tyr248Stop. FLAG-tagged wild-type and mutant HACD1 were expressed
in HEK293T cells; the mutant lost activity in the C16 assay. The mutant also showed
glycosylation. The topology interpretation draws on yeast Phs1 rather than a direct
human structure. Normal circulating VLCFAs in one tested patient do not establish
normal muscle lipids or experimentally demonstrate compensation by another HACD.
These experiments do not test the CAP splice product.

## Reaction terminology

Official QuickGO definitions were checked on 2026-11-11 UTC. The following
compact facts make the evidence available within this PR:

| Term | Definition scope |
|---|---|
| GO:0018812 | Dehydration of a 3-hydroxy-fatty acyl-CoA to a (2E)-enoyl-CoA and water. |
| GO:0080023 | The (3R)-hydroxyacyl-CoA dehydration reaction, despite its hydratase label. |
| GO:0102158 | The very-long-chain (3R)-hydroxyacyl-CoA dehydratase class in the ER elongation cycle; the definition includes extension of C16-or-longer starting fatty acids by two carbons. |

The asserted `is_a` chain is GO:0102158 → GO:0080023 → GO:0018812.
[Official QuickGO definitions and child relations](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0080023,GO:0018812,GO:0102158)
were the source; the selected-response receipt pins SHA256
`d4659da499d24a79087d692c55437c99aabc82813f9c6336f6a59076e9c9efe7`.
No private relative link is needed. The three general MF rows are refined to
GO:0102158 for enzyme-class specificity, not reaction direction. A class/context
assignment is distinct from a measured panel of individual chain-length kinetics.

### Literal ontology provenance — checked 2026-11-14 UTC

[QuickGO GO/about](https://www.ebi.ac.uk/QuickGO/services/ontology/go/about) reports
`http://purl.obolibrary.org/obo/go/releases/2026-11-12/extensions/go-plus.owl`.
The [term response](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0080023,GO:0018812,GO:0102158)
gives GO:0080023 `definition.text` as "Catalysis of the reaction: a
(3R)-3-hydroxyacyl-CoA = a (2E)-enoyl-CoA + H2O." GO:0018812's `children` include
`{"id":"GO:0080023","relation":"is_a"}`; GO:0080023's `children` include
`{"id":"GO:0102158","relation":"is_a"}`. These parent-to-child fragments establish
the asserted child-to-parent chain GO:0102158 → GO:0080023 → GO:0018812.

## Interaction evidence

The original [HuRI HACD1 portal](https://interactome-atlas.org/search/HACD1)
was inspected by the read-only annotation consultant through a bounded HTTP read
and JSON parsing without executing page scripts. It maps HACD1 ORF6415 to
B0YJ81-1 and lists five validated HI-III interactions:

| Partner | Edge | Y2H version | Screens | DNA-binding fusion → activation fusion; ORFs |
| --- | ---: | ---: | ---: | --- |
| IL10RA / Q13651 | 24142 | 6 | 1 | HACD1 → IL10RA; 6415/9496 |
| CPLX4 / Q7Z7G2 | 53271 | 6 | 1 | HACD1 → CPLX4; 6415/52634 |
| RNF170 / Q96K19-5 | 30513 | 6 | 2 | HACD1 → RNF170; 6415/15061 |
| TMEM106C / Q9BVX2-1 | 37814 | 2 | 1 | HACD1 → TMEM106C; 6415/2758 |
| TECR / Q9NZ01-1 | 13315 | 1 | 1 | TECR → HACD1; 5155/6415 |

The internal dataset description still says unpublished; the official
[download page](https://interactome-atlas.org/download) associates HuRI with
Luck et al. 2020. Original clone sequences were not inspected. The
[original article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/) describes
repeated screening, pairwise retesting and sequence confirmation. Its aggregate
orthogonal-assay validation cannot be assigned to every individual pair.

[Target-and-PMID-filtered IntAct](https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/pubid:32296183%20AND%20id:B0YJ81?format=tab27)
provides curated corroboration: 16 records, including validated two-hybrid records
for all five pairs (respectively EBI-24695283, EBI-24668889, EBI-24655235,
EBI-24637830 and EBI-24473091). TMEM106C also has a HEK293T Gaussia
protein-complementation record, EBI-25291211. TECR array record EBI-24812736
contains a residue-182 interaction-disrupting mutation on TECR; do not describe
every TECR experiment as wild type. RNF170's isoform-confirmation comment is not
a negative binding result. Supplementary Tables 8/9/27 were not independently
retrieved, so these details are attributed to IntAct curation. No CAP interaction,
endogenous ER complex or adaptor role follows from these screens.

[PMID:38422897](https://pubmed.ncbi.nlm.nih.gov/38422897/):
the inspected abstract explicitly reports HACD1/2 interactions with TECR. The
isolated stable complex and modeled substrate/catalytic sites concern HACD2–TECR.
Full Methods and Results remained unavailable after bounded publisher and
Europe PMC attempts. The abstract plus curated HACD1 interaction records support
the plain association, but not HACD1-specific stoichiometry, assay host, tags,
catalytic enhancement, substrate channeling or CAP involvement. Do not transfer
HACD2's structural conclusions to HACD1. The two TECR contexts can be refined
to enzyme binding (GO:0019899), without an adaptor or channeling inference. The
other four HuRI partners retain non-core generic binding.
[Official enzyme-binding definition](https://www.ebi.ac.uk/QuickGO/term/GO:0019899)
specifies binding to a protein with catalytic activity.

### RNF170 partner isoform — checked 2026-11-14 UTC

The mapped RNF170 isoform Q96K19-5 is 116 residues long and lacks part of the canonical RING domain.
The official [RNF170 record](https://rest.uniprot.org/uniprotkb/Q96K19.json) places the
canonical RING domain at residues 87-130. Isoform 5 replaces residues 109-116 with
NLTPNSIW (VSP_023853) and omits residues 117-258 (VSP_023854); the official
[Q96K19-5 sequence](https://rest.uniprot.org/uniprotkb/Q96K19-5.fasta) has 116 residues.
These are database sequence/domain observations, not an inspected catalytic assay.
They do not show the isoform is inactive or invalidate the interaction. Original
HuRI clone sequences remain uninspected, so the mapped isoform is not independently
sequence-verified as the experimental construct. TECR has separate positive enzyme
and interaction evidence.

## CAP literature, assessed separately

[PMID:22067203](https://pmc.ncbi.nlm.nih.gov/articles/PMC3261120/):
prior direct full-text preparation is recorded in the retained primary-preparation
receipt; the repeat consultant retrieval failed. The study uses recombinant human
CAP140 from a fibroma-derived cDNA, expressed in bacteria. It tests gingival
fibroblast attachment on coated substrate and hydroxyapatite binding, and examines
isoform-specific expression. It does not directly establish crystal nucleation,
cell differentiation or a negative dehydratase assay. Larger antibody-reactive
species and post-translational modification explanations are not established
protein identities.

[PMID:25263524](https://pubmed.ncbi.nlm.nih.gov/25263524/):
the abstract and publisher preview describe recombinant human CAP140
self-assembly/hydroxyapatite nucleation and bone repair in a rat cranial defect.
Full Methods and Results were not obtained. This is not evidence for a canonical
HACD1 enzyme function or direct demonstration of endogenous cementum
mineralization. If fresh GOA contains CAP-specific annotations, assess them with
their isoform and evidence scope rather than importing these claims into the
canonical enzyme's core function.

## Additional clinical context and cache completion

The four contextual papers already cited in the notes are now included in the
reference list and fetched through the normal publication pipeline. The CAP
papers remain abstract-only in that cache; prior access to the original main
text of PMID:22067203 is described above. Existing publication files were not
refreshed or edited.

[PMID:32426512](https://pubmed.ncbi.nlm.nih.gov/32426512/) reports a human case
with a homozygous HACD1 LINE insertion and congenital myopathy. The original
[PMC text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7188472/) and the newly fetched
full-text cache support the clinical association and improvement over time.
It supplies no new patient dehydratase assay; proposed membrane mechanisms cite
earlier work.

[PMID:33354762](https://pubmed.ncbi.nlm.nih.gov/33354762/) describes three human
patients with novel homozygous variants and congenital myopathy. Two splice
effects are predicted; the third variant is nonsense. The inspected abstract
supports the disease association and variant spectrum, not experimentally
demonstrated splicing or enzyme loss. Publisher full text was unavailable.

## Phylogenetic evidence and limits

Retained PAINT/IBD records place five HACD1 IBA assertions at PTN000112207:
ER membrane, dehydratase activity, sphingolipid biosynthesis, fatty-acid elongation
and VLCFA biosynthesis. B0YJ81 is an experimentally supported descendant;
appearance among the evidence sources is not circular. The member index maps
B0YJ81 to PTHR11035:SF22. The underlying tree/MSA was not available in the retained
cache, and official remote tree/MSA requests returned 403. Do not assert an
independently verified ancestral placement, duplication history or alignment.
Judge functional evidence while respecting the curator's phylogenetic judgment.

## Provisional revision priorities

Preserve separate partner contexts when seeding, and preserve every inherited
supporting-text quote and original source field. Correct the reaction-direction
rationale. Distinguish demonstrated C16 biochemistry, yeast complementation and
curated VLCFA reaction scope. Reconsider the existing blanket description of
sphingolipid synthesis as merely indirect: the original study directly tests
rescue, and fatty-acid elongation supplies a structural part of sphingolipids.
Avoid substituting genericity for biological evidence when judging binding.
Do not add a process annotation without the required participation and comparator
checks. No final action table or new annotation is asserted by this preparation.


## UniProt / QuickGO discrepancy — checked 2026-11-11 23:53:55 UTC

UniProt entry version 133 contains six GO lines absent from the current canonical
QuickGO result: GO:0019899 enzyme binding, GO:0046848 hydroxyapatite binding,
GO:0071529 cementum mineralization, GO:0010811 positive regulation of cell-substrate
adhesion, GO:0065003 protein-containing complex assembly, and GO:0005783 ER.
Complete queries returned 22 canonical B0YJ81 rows and zero rows for each explicit
isoform B0YJ81-1 and B0YJ81-2. The canonical response SHA256 was
`fc4e2dd48133ce0da3a233b7d879eb015a868504978315f0f760f95e4852dd78`.
[Canonical query](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB%3AB0YJ81&includeFields=goName&limit=200),
[isoform 1](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB%3AB0YJ81-1&includeFields=goName&limit=200),
[isoform 2](https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB%3AB0YJ81-2&includeFields=goName&limit=200).

These results do not establish omitted isoform rows or a fetcher defect. No GOA
row or isoform field is manufactured. The six unqualified UniProt GO lines do
not prove that all six describe CAP: ER localization is explicitly assigned to
isoform 1 in the native location block, and enzyme binding is not uniquely
attributable to CAP. The earlier notes' blanket CAP attribution was incorrect and is corrected in place.

## Final follow-up decisions

Three general MF rows are MODIFY → GO:0102158; two TECR binding rows are MODIFY
→ GO:0019899. Sphingolipid biosynthesis is retained as a supported non-core use
of the elongation activity, with direct yeast rescue explicitly documented.
The informative long-chain acyl-CoA and fatty-acid biosynthetic processes remain
accepted and explicitly listed under the same existing dehydratase core-function
object. Both describe direct catalytic biosynthetic participation. The family assessment records the revised HACD1
specificity decision without alleging a PAINT placement error. HACD2's separate [PR #6316](https://github.com/ai4curation/ai-gene-review/pull/6316)
tracks its gene-specific correction. Its earlier rationale is not evidence that the
shared family reaction is unsound; HACD2 is not edited in this HACD1 PR. Final counts: 11 ACCEPT, 5 KEEP_AS_NON_CORE, 5 MODIFY; no NEW.
