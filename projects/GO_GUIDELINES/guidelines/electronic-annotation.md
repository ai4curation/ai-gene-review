# Electronic annotation: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- An IEA is a claim about a mapping or rule, applied to a gene. Review it by asking whether the
  mapping holds for every protein it fires on, and fix it where it was made.
- A signature-to-GO mapping is appropriate only if every protein matching the signature has the
  function. A term true for a subset belongs on a narrower entry or in a conditional rule.
- Provenance must be one hop from a curated or sequence-feature source to GO. Chains such as
  ARBA to keyword to GO, or ARBA to Rhea to GO, are not acceptable.
- A correct but general IEA is kept, never removed for being general. REMOVE is for a mapping
  that is wrong for the gene, an over-propagation you can argue on biological grounds, or a
  premise that has fallen.
- Before proposing a mapping removal, check what else would still supply the term to the members
  that should keep it, and record a replacement rule when only a condition can separate right
  from wrong members.

## Scope

This document covers annotations made without curator review of the individual gene product,
which carry IEA (ECO:0000501, evidence used in automatic assertion) and a GO_REF naming the
method:

- **Signature mappings**: InterPro2GO (`GO_REF:0000002`), including member databases that reach
  GO only through it (Pfam, NCBIfam, CDD, PANTHER via InterPro), and Rfam2GO.
- **Controlled-vocabulary mappings**: UniProt keywords (KW2GO, `GO_REF:0000043`, retired for
  cellular organisms), UniProt subcellular locations (SubCell2GO, `GO_REF:0000044`), EC2GO
  (`GO_REF:0000003`), Rhea2GO (`GO_REF:0000116`) and UniPathway2GO (`GO_REF:0000041`).
- **Rule systems**: UniRule (including HAMAP) and ARBA (`GO_REF:0000117`).
- **Phylogenetic and orthology pipelines** that run without a curator: TreeGrafter
  (`GO_REF:0000118`) and Ensembl Compara (`GO_REF:0000107`).
- **GO's own logical inferences** across aspects (`GO_REF:0000108`), and UniProt's combined
  record of identical predictions from several pipelines (`GO_REF:0000120`).
- How to review and challenge an IEA row, and how to record a mapping fix, including this
  repository's curated rules in `rules/curated/`.

PAINT/IBA, ISO, ISS and ISA are in [phylogenetic-propagation.md](phylogenetic-propagation.md).
Machine-learning and language-model predictions outside these pipelines share several failure
modes and are touched on in IEA-15; evidence-code choice in general is in
[evidence-codes.md](evidence-codes.md).

## Principles

**A mapping is a universal claim.** InterPro2GO attaches a term to every protein that matches an
entry ([PMID:22301074](https://europepmc.org/article/MED/22301074), the InterPro GO-mapping
protocol). A term true of most members is false of the rest, and a single wrong mapping repeats
across every matched gene. The repo's InterPro review found mapping errors that each reached
hundreds to thousands of proteins ([INTERPRO](../../INTERPRO.md)).

**Provenance has to reach the source in one step.** The GO IEA working group's rubric scores
pipelines on responsiveness, currency, conformance to GO rules, provenance, explainability,
documentation, accuracy and uniqueness, and it judged multi-hop chains to be the main reason
KW2GO errors were hard to trace and harder to fix
([Drive: IEA WG pipelines update GOC 2026](https://drive.google.com/open?id=1lkoSLtiaa_w-P_g2F74u_xii5DeeULCV_6_0kjI413Y)).

**IEAs fill real gaps.** For many proteins in poorly curated organisms an IEA is the only
annotation. TreeGrafter supplied the only annotation to a term on 623 reviewed rows, of which
reviewers kept 70% ([TREEGRAFTER](../../TREEGRAFTER.md)); the plant keyword review found that
retiring KW2GO also removed correct facts carried nowhere else ([SPKW](../../SPKW.md)). The aim is
a leaner, more informative set, not a smaller one for its own sake
([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).

**Fix the source, not the symptom.** A gene-level REMOVE leaves the mapping in place and the next
release restores it. Every correction should name the mapping, rule or node that produced the row.

## Rules

<a id="iea-1"></a>

### IEA-1. Identify the pipeline before judging the row

**Read the GO_REF, `assigned_by` and `WITH/FROM` of every IEA row before reviewing it. Judge the
claim the pipeline made: the signature, keyword, EC number, reaction, rule or ortholog in
`WITH/FROM` is the premise.**

Rationale: every IEA must cite a GO_REF and a `WITH/FROM` naming its basis
([wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)).
`assigned_by` credits the group that made the decision (InterPro for InterPro2GO, UniProt for
keyword and HAMAP mappings) ([wiki: Annotation Assigned by](https://wiki.geneontology.org/index.php/Annotation_Assigned_by);
[go-annotation#1386](https://github.com/geneontology/go-annotation/issues/1386)). `GO_REF:0000120`
means two or more pipelines produced the same term, with the contributors listed in `WITH/FROM`; in
the repo's corpus a `GO_REF:0000118` row is therefore a TreeGrafter call no other pipeline
reproduced, and corroborated TreeGrafter calls were accepted 77% of the time against 43% for
uncorroborated ones ([TREEGRAFTER](../../TREEGRAFTER.md)). Corroboration raises confidence; it does
not make two pipelines independent if they share a training source.

Worked example: an IEA row of `GO:0005524` ATP binding with `GO_REF:0000002` and
`InterPro:IPR000719` in `WITH/FROM` is a claim that every protein-kinase-domain protein binds ATP.
The same term with `InterPro:IPR017441` is a claim from the kinase ATP-binding-site entry, which
requires the motif. The first fails for pseudokinases; the second does not
([INTERPRO](../../INTERPRO.md)).

Provenance: [GOC] for the fields; [GOC+] for reading `GO_REF:0000120` as corroboration.

<a id="iea-2"></a>

### IEA-2. A signature mapping must hold for every member of the entry

**Map a GO term to an InterPro entry (or any signature) only if every protein the signature
matches has the function. When a term is true for a subset, place it on a narrower entry (a
subfamily, a site entry, an active-site entry) or in a rule that can require a site, exclude a
domain or restrict a taxon. Do not keep an enzyme mapping on a family because "most" members are
active.**

Rationale: the InterPro protocol already avoids mapping whole-protein function to a domain and
avoids large, uncharacterised families ([PMID:22301074](https://europepmc.org/article/MED/22301074);
[go-annotation#2921](https://github.com/geneontology/go-annotation/issues/2921)). A 2007 InterPro
reply stated the opposite policy for enzymes: catalytic mappings are not removed because a family
has a few inactive members, and those members must be annotated manually
([go-annotation#385](https://github.com/geneontology/go-annotation/issues/385)). That policy pushes
the cost onto every downstream user and leaves pseudo-enzymes with false IEAs that nobody has time
to negate. Since 2011 the same problem has been discussed for the protein kinase domain and
tribbles pseudokinases ([wiki: InterPro2GO session 2011](https://wiki.geneontology.org/index.php/InterPro2GO_Session_October_4th_2011)).
Site-level entries now make the narrower mapping possible.

Worked examples (proposals in [INTERPRO](../../INTERPRO.md), not yet adopted by InterPro):

- `IPR000719` (Protein kinase domain) maps `GO:0005524` ATP binding and `GO:0006468` protein
  phosphorylation. Pseudokinases match the domain. The kinase ATP-binding-site entry `IPR017441`
  and the active-site entries `IPR008271` and `IPR008266` already carry the terms for members with
  the motifs, so the domain-level mappings can go.
- `IPR001424` (Cu/Zn superoxide dismutase domain) maps `GO:0006801` superoxide metabolic process,
  which copper-chaperone members do not perform. UniRule UR000000113 selects canonical Cu/Zn SODs
  and excludes CCS, but assigns only an EC number; the request is to remove the domain mapping and
  add `GO:0019430` removal of superoxide radicals to the rule, plus separate cover for fungal
  Cu-only SODs.
- `IPR013380` (Type 3 secretion system ATPase SctN) maps `GO:0046961` proton-transporting ATPase
  activity, rotational mechanism and `GO:0006754` ATP biosynthetic process. SctN is a soluble
  protein-exporting ATPase with no Fo partner: the terms are wrong for every member, so this is a
  plain removal, with `GO:0008564` protein-exporting ATPase activity as a candidate addition.

Provenance: [NEW]. Departs from the enzyme-mapping policy in go-annotation#385.

<a id="iea-3"></a>

### IEA-3. Map a domain to what the domain does, not to what proteins containing it do

**A domain entry may carry only terms the domain itself performs or enables. Whole-protein
functions (transcription factor activity, a complex's catalytic activity, a process) belong on
family entries whose membership is functionally uniform. Do not map GO terms to InterPro
homologous-superfamily entries.**

Rationale: this is InterPro's revised protocol ([PMID:22301074](https://europepmc.org/article/MED/22301074))
and its stated convention for homologous superfamilies ([go-annotation#2710](https://github.com/geneontology/go-annotation/issues/2710)).
The repo still finds domain entries carrying whole-protein or neighbouring-domain functions
([INTERPRO](../../INTERPRO.md)).

Worked examples: `IPR042371` (Z-binding domain) maps dsRNA adenosine deaminase activity, so ZBP1,
which has Z-binding domains but no deaminase domain, inherits ADAR1's catalytic activity; the
deaminase belongs to `IPR002466`. `IPR006935` (Helicase/UvrB, N-terminal) maps `GO:0003677` DNA
binding, which RIG-I-like receptors such as IFIH1 inherit although they sense RNA; the proposed fix
is `GO:0003676` nucleic acid binding, as on the sibling helicase entries `IPR011545` and
`IPR006555`. The MADS-box domain supports DNA binding and dimerisation, not DNA-binding
transcription factor activity ([INTERPRO](../../INTERPRO.md)).

Provenance: [GOC].

<a id="iea-4"></a>

### IEA-4. Never map to root, do-not-annotate, binding-only or obsolete terms

**A mapping must not target a GO root (`GO:0003674`, `GO:0008150`, `GO:0005575`), any term in
`gocheck_do_not_annotate` or `gocheck_obsoletion_candidate`, `GO:0005515` protein binding, or an
obsolete term. A mapping file that cannot keep its targets current should be retired.**

Rationale: root-term annotations may only use ND, and InterPro runs a pre-release check against
root mappings ([go-annotation#1020](https://github.com/geneontology/go-annotation/issues/1020)).
Predictions to do-not-annotate and obsoletion-candidate terms are excluded in GO's guidance for
external predictors ([Drive: Best practices for predicting GO data](https://drive.google.com/open?id=1z-6rNJ4tg3M-Ant-2kqDXohPZUlkw9GEZ5qlNZDYj18);
a legacy draft of the published external-guidelines page). When "biological regulation" and the
generic regulation terms became not-for-direct-annotation, InterPro2GO and UniRule mappings had to
be fixed as well as manual rows ([go-annotation#1887](https://github.com/geneontology/go-annotation/issues/1887)).
The UniPathway mapping file contains many obsolete terms and has not been maintained since 2015,
which is part of why it is being retired
([Drive: IEA WG pipelines update GOC 2026](https://drive.google.com/open?id=1lkoSLtiaa_w-P_g2F74u_xii5DeeULCV_6_0kjI413Y)).

Worked example: ARBA00026572 put `GO:0006139` nucleobase-containing compound metabolic process on
over 36,000 proteins, including *S. pombe* rib2, whose substrate is a flavin, not a nucleobase. The
curator asked for the term to be flagged do-not-annotate ([go-annotation#5902](https://github.com/geneontology/go-annotation/issues/5902));
in the current ontology it is in `gocheck_do_not_annotate`, so no mapping or rule should target it.

Provenance: [GOC].

<a id="iea-5"></a>

### IEA-5. Accept only one-hop provenance

**An electronic annotation must derive directly from a curated assertion or a sequence feature.
Reject pipelines, and treat rows with suspicion, where GO is reached through an intermediate
prediction: ARBA or UniRule to a keyword to GO; ARBA to a Rhea reaction or EC number to GO; an IEA
used as the premise for another IEA.**

Rationale: the IEA working group found that most automatic keyword assignments in TrEMBL came from
UniRule and ARBA, that KW2GO could not tell manual keywords from predicted ones, and that the chain
lost the evidence and propagated mistakes. On that basis it retired KW2GO (except for viruses) and
scheduled SubCell2GO, Rhea2GO and EC2GO for replacement on Swiss-Prot and withdrawal from TrEMBL
([Drive: KW2GO announcement](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk);
[Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).
The GO-CAM editor now refuses IEA rows from keywords, subcellular locations and UniPathway as
supporting evidence ([go-annotation#6085](https://github.com/geneontology/go-annotation/issues/6085)).
The ARBA-for-curators notes make the feedback-loop risk explicit: rules mined from annotations that
were themselves predicted inherit their errors at 100% "confidence"
([Drive: ARBA notes for curators](https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz)).

Worked example: KW2GO annotated about 175 *Drosophila* genes that do not encode enzymes with
catalytic-activity terms, and ribosome methyltransferases as ribosomal proteins from a historic
EMBL import ([Drive: KW2GO announcement](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk)).
Neither error could be traced from the GO row back to its cause without reconstructing the chain.

Provenance: [GOC] (IEA working group decision, 2026).

<a id="iea-6"></a>

### IEA-6. Know the current status of each pipeline

**Treat rows from retired pipelines as historical, rows from pipelines under replacement as
provisional, and rows from kept pipelines as disputable through the pipeline's tracker.**

Rationale: as of the IEA working group's Fall 2026 report
([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I);
[Drive: IEA WG pipelines update Sept 2026](https://drive.google.com/open?id=1FQpXSPZdK78X3wX5UEQ9jkFk6Xex0NCi8NeDawOs7IE)):

| Pipeline | GO_REF | Decision |
|---|---|---|
| KW2GO | `GO_REF:0000043` | Retired; kept for viruses only (ViralZone asked to align keyword use with GO) |
| SubCell2GO | `GO_REF:0000044` | Replace with direct annotations for Swiss-Prot; stop for TrEMBL |
| Rhea2GO | `GO_REF:0000116` | Replace with direct annotations for Swiss-Prot; stop for TrEMBL |
| EC2GO | `GO_REF:0000003` | Replace with direct annotations for Swiss-Prot; stop for TrEMBL |
| UniPathway2GO | `GO_REF:0000041` | Retire; loss files for groups to review |
| InterPro2GO | `GO_REF:0000002` | Keep; dispute through GitHub |
| Rfam2GO | | Keep; check mapped terms are current |
| GO inter-ontology inferences | `GO_REF:0000108` | Keep |
| ARBA, UniRule | `GO_REF:0000117` (ARBA) | Keep and improve; dispute through GitHub |
| TreeGrafter | `GO_REF:0000118` | Keep; update expected |
| Ensembl Compara | `GO_REF:0000107` | Revise or remove; Ensembl stopped orthology calls in January 2026 |

The repo verified that GOA had removed `GO_REF:0000043` rows for cellular organisms by about April
2026 ([SPKW](../../SPKW.md)). The GO wiki's IEA page still lists keyword and subcellular-location
mappings as sanctioned, with a note that several are "under review and revision"
([wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)).
IEAs older than one year draw a warning and those older than three years are filtered
(GORULE:0000029, same page).

Worked example: a cached GOA file for a human gene may still carry `GO:0006915` apoptotic process
from KW2GO. Review it for the retrospective record, but do not cite the row as evidence elsewhere,
and do not expect it in the next release.

Provenance: [GOC].

<a id="iea-7"></a>

### IEA-7. Use only exact reaction mappings, and only for physiological reactions

**EC2GO and Rhea2GO may drive annotation only through `exactMatch` cross-references. A
`broadMatch` or `narrowMatch` xref documents a relation and must never generate annotations. An EC
number applied to a protein for a non-physiological or assay-only reaction should not produce a GO
term, even if the EC assignment is kept.**

Rationale: broad-match EC xrefs leaked into the mapping export and annotated 82 *S. pombe* kinases
to `GO:0044024` histone H2AS1 kinase activity from EC 2.7.11.1; the GO position is that broadMatch
xrefs must not feed pipelines ([go-annotation#5432](https://github.com/geneontology/go-annotation/issues/5432)).
GO annotation concerns physiologically relevant reactions, so a mapping for a non-physiological EC
use should be removed while the EC number stays ([go-annotation#1519](https://github.com/geneontology/go-annotation/issues/1519)).
For weak or promiscuous activities, apply the same tiers as for experimental rows
([CLAUDE.md](../../../CLAUDE.md), "Measured activity is not automatically function";
[ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md)).

Worked example: the repo's Rhea audit found that 88% of reactions carrying an EC number map to the
same GO term EC2GO already supplies, so most `GO_REF:0000116` rows are redundant, and that the real
gap is reactions with no GO target at all (36% of enzymatic reactions), not mis-propagation
([RHEA](../../RHEA.md)). A reviewer seeing a Rhea2GO row should expect an EC2GO twin and judge the
pair together.

Provenance: [GOC].

<a id="iea-8"></a>

### IEA-8. A keyword or location mapping must respect GO's distinctions, which vocabularies often do not

**When reviewing a keyword- or subcellular-location-derived row, check three things: participation
versus regulation (a regulator is not part of the process); location of activity versus transit or
sequestration (Golgi for a secreted protein is transit); a metal cofactor versus a binding
function.**

Rationale: UniProt keywords are thematic; GO process terms are mechanistic. The KW2GO review found
"regulation of" and "in process" conflated, and that 35-50% of keyword-unique MF rows were binding
terms, mostly metal ion binding describing cofactors in metalloproteins
([Drive: KW2GO announcement](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk)).
The repo's keyword review found 79-100% over-annotation for eukaryotic apoptosis, autophagy, rhythm
and meiosis keywords, mostly a regulator or bystander annotated as a participant, while bacterial
keyword rows were mostly sound ([SPKW](../../SPKW.md)). Earlier tracker cases make the same point:
about 50 *S. pombe* "DNA repair" keyword rows were upstream chromatin or checkpoint effects
([go-annotation#1134](https://github.com/geneontology/go-annotation/issues/1134)); keyword-derived
`GO:0005794` Golgi apparatus on a protein that only passes through the Golgi is not a location of
activity ([go-annotation#4573](https://github.com/geneontology/go-annotation/issues/4573)); and
iron-sulfur cluster binding is not a kind of iron ion binding, so `GO:0051536` should not imply
`GO:0005506` ([go-annotation#390](https://github.com/geneontology/go-annotation/issues/390)).

Worked example: caspase substrates such as AIMP1 and BCAP31 carried `GO:0006915` apoptotic process
from the apoptosis keyword; being cleaved during apoptosis is not participation. The repo removed
them ([SPKW](../../SPKW.md)). Where GO's own concept changes, a keyword mapping must follow: KW-1110
moved from the obsolete `GO:0039527` to `GO:0140476` symbiont-mediated suppression of host
cytoplasmic pattern recognition receptor signaling pathway via inhibition of TRAF activity
([KW_1110_TRAF_KW2GO](../../KW_1110_TRAF_KW2GO.md)).

Provenance: [GOC+]. These are GOC principles applied to vocabularies that predate them.

<a id="iea-9"></a>

### IEA-9. Judge a rule by its condition sets, as conjunctions, against the experimental record

**Review a UniRule or ARBA rule by reading every condition set it serves, each as the conjunction
of all its conditions including taxon. A rule is wrong only if it annotates a protein that lacks
the function, has an obsolete consequent, or has been withdrawn. Rule size, generality, redundancy
and low recall are not errors. Before calling a protein a false positive, check its experimental
annotations to the term and its descendants.**

Rationale: an audit of 78 ARBA rule reviews in November 2026 found about 45 verdicts unsupported by
their own evidence; the commonest errors were treating rule size as evidence (the "limit of 12
condition sets" is a default in an analysis tool), verdicts on conditions never recorded, judging
signatures one at a time, mislabelled InterPro ids, and "false positives" that were experimentally
annotated ([docs: rule review receipts](../../../docs/rule_review_receipts.md)). ARBA's "100%
confidence" means only that every Swiss-Prot entry matching the condition carried the annotation
in training: missing negative examples, excluded HAMAP/PROSITE-ProRule annotations and errors in
templates all pass through, and signatures carry no taxon constraint of their own, so they can
"leak" into lineages where the function does not exist
([Drive: ARBA notes for curators](https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz)).
UniRule and ARBA apply GO taxon constraints during validation and prefer precision over recall
([Drive: Rule-based systems in GOA, 2025](https://drive.google.com/open?id=1_XLWtDWUzR0A-u8TTE3OoZa46XpHgICo)).

Worked examples: ARBA00090718 assigns (S)-2-hydroxyglutarate dehydrogenase activity to SerA-family
proteins, which make the (R) enantiomer, so the *P. putida* serA row was removed and the rule review
proposes deprecation. ARBA00089174 assigns adaptive thermogenesis from PM20D1 FunFams across
Eukaryota; the fission-yeast cps1 row was removed and the rule review restricts it to mammals
([ARBA_REVIEW](../../ARBA_REVIEW.md); [go-annotation#6018](https://github.com/geneontology/go-annotation/issues/6018)).
Including IBA rows in ARBA training removed many high-level and do-not-annotate predictions as
well as over-annotations such as ARBA00084588, which added endocrine pancreas development to
proteins matching one FunFam in vertebrates
([Drive: Including IBA in ARBA training](https://drive.google.com/open?id=1eIC-6mENH1bQoHsjDuaXu52IlXm5PyCD)).

Provenance: [GOC+]. The receipts requirements are this repository's ([CLAUDE.md](../../../CLAUDE.md),
"Reviewing rules").

<a id="iea-10"></a>

### IEA-10. Automated orthology transfer must preserve relations and stop at context

**An automated ortholog projection must use one-to-one orthologs, experimental donor rows only, and
the donor's gene-product-to-term relation unchanged. It should not transfer tissue, developmental,
"response to", or organism-specific process terms. When reviewing a Compara row, treat it as a
transfer of the donor row and check the donor's relation first.**

Rationale: the Compara method uses one-to-one and apparent one-to-one orthologs and projects only
IDA, IEP, IGI, IMP and IPI rows ([wiki: Ensembl Compara annotation projection](https://wiki.geneontology.org/index.php/Ensembl_Compara_annotation_projection)).
In practice it copies annotations wholesale: the IEA working group called it boilerplating that
cannot tell conservation from divergence, inflated by many-to-many paralog mappings, and silent in
review because a dispute must target the original source
([Drive: Ensembl and ISO pipelines](https://drive.google.com/open?id=1q9m9RbQqdpXMPrLq-jzTC-ouLJjUda_XAA93U8zTkNw);
[Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).
A 2024 report showed a mouse `acts_upstream_of_or_within` row arriving in human as `involved_in`
([go-annotation#5411](https://github.com/geneontology/go-annotation/issues/5411)). Developmental and
response-to terms on human GART from Compara were an early example
([go-annotation#1344](https://github.com/geneontology/go-annotation/issues/1344)), and Ensembl Plants
once projected auxin-signalling terms onto yeast ([go-annotation#1807](https://github.com/geneontology/go-annotation/issues/1807)).
In the repo's statistics, 20% of reviewed Compara rows were downgraded against 9% of IBA
([HOMOLOGY_PROPAGATION](../../HOMOLOGY_PROPAGATION.md)).

Worked example: human GART carried brainstem, cerebellum and cerebral cortex development from a
mouse phenotype by Compara projection. GART is a purine biosynthetic enzyme; the developmental terms
are downstream phenotypes and should not have been projected
([go-annotation#1344](https://github.com/geneontology/go-annotation/issues/1344)).

Provenance: [GOC+].

<a id="iea-11"></a>

### IEA-11. An inferred annotation falls with its premise

**For a row made by GO's inter-ontology inference (`GO_REF:0000108`, with the premise term in
`WITH/FROM`), review the premise. If the premise annotation is removed, remove the inferred row
too, whatever its own plausibility.**

Rationale: GO derives annotations along transitive relations between aspects
([wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)).
A wrong MF therefore drags a BP behind it, and the BP survives the MF's removal unless someone
follows the link ([IBA_REVIEW](../../IBA_REVIEW.md), pattern 16).

Worked example: CcmC proteins inherit `GO:0004096` catalase activity from a phenotype-derived seed,
and `GO:0098869` cellular oxidant detoxification then arrives as IEA `GO_REF:0000108` with
`GO:0004096` in `WITH/FROM`. Both go together ([phylogenetic-propagation.md, PH-2](phylogenetic-propagation.md#ph-2)).
Mouse Akt1's ER location was likewise inferred only from a flattened process row and was removed
with it ([ISO](../../ISO.md)).

Provenance: [GOC+].

<a id="iea-12"></a>

### IEA-12. Review actions: keep true general rows, remove wrong ones, never cite an IEA as evidence

**A correct but general IEA is ACCEPT or KEEP_AS_NON_CORE (or MODIFY when the row's own evidence
supports a specific descendant), never REMOVE. REMOVE is for a demonstrably wrong mapping or rule
output, an over-propagation argued on biological grounds, a fallen premise, or a taxon violation.
Never quote an ARBA statement, an electronic `DR GO` line, a keyword or a protein name as support
for anything.**

Rationale: the GOA position since 2008 is that correct but uninformative electronic annotations are
retained, and redundancy filtering is a display problem ([go-annotation#615](https://github.com/geneontology/go-annotation/issues/615));
PomBase filters IEA, ISS and similar rows where non-HTP experimental support exists, and no group
filters experimental rows ([go-annotation#1879](https://github.com/geneontology/go-annotation/issues/1879)).
In this repository, rows sharing a term reinforce each other and must receive consistent actions;
REMOVE is never a deduplication tool ([CLAUDE.md](../../../CLAUDE.md);
[action consistency](../../../docs/action_consistency.md)). ARBA-derived UniProt text,
submitter-imported text and electronic GO lines are unvetted predictions, and citing ARBA text for
an ARBA row is circular ([CLAUDE.md](../../../CLAUDE.md), "Quote UniProt for evidence"). The bar for
MODIFY is the row's own evidence: an InterPro2GO row from a generic GPCR signature supports only a
generic receptor term.

Worked example: TreeGrafter `GO:0005829` cytosol and `GO:0005737` cytoplasm rows on soluble
bacterial enzymes were first downgraded and, on re-review, moved to KEEP_AS_NON_CORE as true but
redundant ([TREEGRAFTER](../../TREEGRAFTER.md)). The keyword mapping to `GO:1990904` ribonucleoprotein complex, which a
curator found too broad to be useful, was kept by GOA because it is correct and informative for
genome-wide analyses in poorly annotated species ([go-annotation#615](https://github.com/geneontology/go-annotation/issues/615));
on a protein with no RNP association the same row would be wrong and removed.

Provenance: [GOC] for retention; [GOC+] for the action mapping.

<a id="iea-13"></a>

### IEA-13. When a mapping is wrong, route the fix to the mapping and record it in a form the source can use

**Record every proposed mapping change against the entry and term, not only against the gene:
removals and narrowings in the InterPro SSSOM mapping set, rule verdicts in a rule review, PAINT
changes in a family review. Before proposing a removal, run a sole-source check (which reviewed
genes lose the term outright) and a rule-cover check (what else still supplies the term to members
that should keep it).**

Rationale: a removal drops the term from every matched protein, including those for which it is
right. The repo's protocol asks for the cost to be stated in the row: list reviewed annotations for
which the entry is the only InterPro source and read their review actions; search interpro2go for
other entries carrying the term, the UniRule API for rules (HAMAP, PIRSR, PIRNR, RuleBase can
require a site, exclude a domain or restrict a taxon), and the EC mapping, since many rules assign
an EC number rather than a GO term ([INTERPRO README](../../INTERPRO/README.md#before-proposing-a-removal)).
Then choose: wrong for every member, remove; right for a subset another source covers, remove and
cite the cover; right for a subset nothing covers, remove only with a request for the covering rule,
otherwise propose narrowing. Disputes go through the GitHub trackers, which the IEA working group
kept as the channel for InterPro2GO, ARBA, UniRule and inter-ontology links
([Drive: IEA WG pipelines update Sept 2026](https://drive.google.com/open?id=1FQpXSPZdK78X3wX5UEQ9jkFk6Xex0NCi8NeDawOs7IE)).

Worked example: removing `GO:0005524` ATP binding from `IPR000719` costs annotations on seven
reviewed genes whose only InterPro source for the term is that entry, and reviewers accepted or kept
all seven. The note on the removal therefore asks for family rules (for example the JNK rule
UR001528758) to cover members without the site motif, rather than presenting the removal as free
([INTERPRO](../../INTERPRO.md)). For `IPR012724` (Chaperone DnaJ), ATP binding belongs to the Hsp70
partner and HAMAP MF_01152 assigns no ATP-binding term, so the removal needs no cover.

Provenance: [NEW].

<a id="iea-14"></a>

### IEA-14. Use a curated conditional rule when only a condition can separate right from wrong members

**When a mapping is right for some members and wrong for others, and a taxon, module context or
sequence feature separates them, write a curated rule that couples the sequence condition with the
restricting condition and names the mapping it replaces. When the term is wrong for every member,
record a removal instead.**

Rationale: interpro2go has no conditions, so a taxon-dependent or context-dependent truth cannot be
expressed in it. GOA has long transformed or filtered taxon-violating IEAs (for example viral
proteins matched to `nucleus`) for the same reason ([wiki: Planned changes to the IEA GO_REFs cited by UniProtKB](https://wiki.geneontology.org/index.php/Planned_changes_to_the_IEA_GO_REFs_cited_by_UniProtKB.);
archived). This repository's `CuratedRule` records make the condition explicit and auditable
([rules/curated README](../../../rules/curated/README.md)). A rule fires when any condition set holds;
a set holds when all its conditions hold. Every set needs a non-negated sequence-feature condition;
taxon and module conditions only restrict. Module conditions are exclusion-only: they block an
annotation only where the module is shown to be unsatisfiable in a complete proteome, because a
missing component may be a detection gap. Choose the condition that actually separates right from
wrong: a taxon when a whole lineage lacks the prerequisite and the taxon is an exact proxy; a module
when a taxon only approximates the prerequisite; a sequence feature when paralogs share a genome.

Worked examples: CR-0001 assigns `GO:0007034` vacuolar transport on `IPR005024` AND Eukaryota,
replacing the unconditional interpro2go row, because only eukaryotes have a vacuole. CR-0003 assigns
`GO:0006511` ubiquitin-dependent protein catabolic process on `IPR000426` unless the ubiquitin relay
module is unsatisfiable in the organism, since some archaea may have a ubiquitin-like conjugation
system. CR-0005 restricts `GO:0044548` S100 protein binding on `IPR037893` to Chordata
([rules/curated README](../../../rules/curated/README.md)). Before choosing a module condition over a
taxon, count what each keeps and drops: CR-0003 keeps 149 archaeal annotations on unevaluated
proteomes although the relay was found in 3 of 504 complete ones.

Provenance: [NEW].

<a id="iea-15"></a>

### IEA-15. Do not launder a prediction into manual evidence

**A curator who reviews an electronic prediction and agrees with it makes a new annotation with the
evidence they actually used: ISS, ISA or ISO for a reviewed similarity (with the match in
`WITH/FROM` and `GO_REF:0000024` or the paper), ISM for a reviewed sequence-model match. Do not copy
an IEA into a manual record, do not use an IEA as the evidence for a GO-CAM activity, and do not let
a computational prediction override experimental evidence in the same gene.**

Rationale: if sequence-based evidence has been reviewed by a curator, the code is ISS or a child,
not IEA ([wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29);
[wiki: ISM](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29)). Converting
an IEA to ISS makes sense for InterPro2GO and Compara, where sequence similarity is the basis, and
not for vocabulary mappings, where there is none ([wiki: Annotation consistency: IEA, ISS, IC](https://wiki.geneontology.org/index.php/Annotation_consistency%3A_IEA%2C_ISS%2C_IC_Usage_Discussion);
archived). Strong experimental evidence that a protein is a transcription coregulator overrides
computational evidence that it is a DNA-binding transcription factor, and the conflicting InterPro
mapping should be disputed; a mapping InterPro has already removed cannot support an annotation
([go-annotation#3007](https://github.com/geneontology/go-annotation/issues/3007)). For AI-generated
predictions, the IEA working group's draft position is that GO does not accept them without review by
a trained curator, and that training on IEA rows risks a loop that amplifies errors
([Drive: Draft AI policy statement](https://drive.google.com/open?id=1leeuPb1WDgyORZHrxhapW9HKLTPrCi6xsMi-KaZNCIQ);
draft, partly superseded).

Worked example: RCOR1, RCOR2, RCOR3 and MIDEAS carried `GO:0000981` DNA-binding transcription factor
activity, RNA polymerase II-specific by ISM from `IPR001005` and `IPR009057`, whose DNA-binding
mappings InterPro had already removed; they are corepressors and the rows were removed
([go-annotation#3007](https://github.com/geneontology/go-annotation/issues/3007)).

Provenance: [GOC].

<a id="iea-16"></a>

### IEA-16. Hold new prediction pipelines to the rubric before they enter GO

**A new electronic pipeline, or a revision of an existing one, should show: one-hop provenance to a
documented source; conformance to GO rules (taxon constraints, do-not-annotate terms, correct
relations, no "regulation of" for participants); explainable individual inferences; a named
maintainer who responds to disputes; regular rebuilds; measured accuracy on held-out, not in-sample,
data; and unique value over existing sources.**

Rationale: these are the IEA working group's rubric criteria and its recommendation that future
pipelines demonstrate value, need and compliance ([Drive: IEA WG pipelines update GOC 2026](https://drive.google.com/open?id=1lkoSLtiaa_w-P_g2F74u_xii5DeeULCV_6_0kjI413Y);
[Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).
We add the in-sample caveat: rules mined from Swiss-Prot and evaluated on the same well-studied
proteins measure training-set agreement, not accuracy on the poorly curated proteomes where the
pipeline matters ([ARBA_REVIEW](../../ARBA_REVIEW.md)). Groups whose curation is mapped directly to GO
(Rhea, subcellular location) should check that their SOP aligns with GO, or annotate GO separately
([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).

Worked example: the repo's NCBIfam audit found a large apparent gain from a proposed
`TIGR03542` to `GO:0010285` L,L-diaminopimelate:2-oxoglutarate transaminase activity mapping, but both
reviewed "gaps" were plant ALD1 proteins with `GO:0062045` L-lysine:pyruvate alpha-transaminase
activity, a cross-kingdom paralog; likewise the reviewed gain for `TIGR00417` to `GO:0004766`
spermidine synthase activity was tobacco PMT1, a `GO:0030750` putrescine N-methyltransferase. Scoping
the mapping to the model's lineage removed both errors ([NCBIFam](../../NCBIFam.md)).

Provenance: [GOC+].

## Decision aid

| Row | Question | Action |
|---|---|---|
| InterPro2GO term false for this gene, gene is an atypical member (pseudo-enzyme, divergent paralog) | Does a narrower entry or rule cover the true members? | REMOVE on the gene; propose narrowing or removal with rule-cover note (IEA-2, IEA-13) |
| InterPro2GO term false for every member of the entry | | REMOVE; propose removal and the correct family-wide term (IEA-2) |
| InterPro2GO term true but general; gene has a specific term from other evidence | Does this row's evidence support the specific term? | KEEP_AS_NON_CORE or ACCEPT; MODIFY only if the row's own signature supports the descendant (IEA-12) |
| Domain entry carries a whole-protein or neighbouring-domain function | | REMOVE on genes lacking that function; propose moving the mapping (IEA-3) |
| Mapping target is root, do-not-annotate or obsolete | | REMOVE or MODIFY; report the mapping (IEA-4) |
| KW2GO, SubCell2GO or UniPathway row in a cached file | Is the biology right? | Review for the record; do not cite; expect it to disappear (IEA-6) |
| Keyword row: regulator annotated to process, transit compartment, cofactor as binding | | MODIFY to regulation term, REMOVE transit location, REMOVE cofactor binding unless binding is the function (IEA-8) |
| EC2GO or Rhea2GO row from a broadMatch or non-physiological reaction | | REMOVE; report the mapping (IEA-7) |
| ARBA or UniRule row looks wrong | Which condition set fired? Does the protein have experimental annotation to the term or a descendant? | If no: REMOVE and file a rule review with the accession as counterexample; if yes: the row is probably right (IEA-9) |
| Compara row with development, response-to or tissue term | Is the donor row experimental and direct? | REMOVE or MARK_AS_OVER_ANNOTATED (IEA-10) |
| `GO_REF:0000108` row whose premise you removed | | REMOVE (IEA-11) |
| Term true for members in some taxa or contexts only | Does a taxon, module or feature separate them? | Write a curated rule (IEA-14) |

## Common errors

**Removing a true general IEA as redundant.** Redundancy is a display concern. Fix: KEEP_AS_NON_CORE,
or MODIFY only with the row's own evidence (IEA-12).

**Treating a gene-level MODIFY as a mapping error.** A specific term on one gene does not make the
general mapping wrong. Fix: record whether the proposal needs removal, a narrower entry, or nothing
upstream ([INTERPRO](../../INTERPRO.md)).

**Proposing a mapping removal without counting the cost.** Fix: run the sole-source and rule-cover
checks and state them (IEA-13).

**Judging a rule from its size or from one signature.** Fix: read the condition sets as conjunctions
(IEA-9).

**Naming an InterPro, Pfam or FunFam id from memory.** The label is the checksum of the id; over 20
ARBA reviews gave an id another entry's name. Fix: copy the official name ([docs: rule review
receipts](../../../docs/rule_review_receipts.md)).

**Calling a protein a rule's false positive without checking its curated annotations.** Rules are
mined from curated annotations; a surprising family is more often a curated row the reviewer did not
know. Fix: check experimental annotations to the term and descendants first (IEA-9).

**Citing ARBA text or the record's `DR GO` lines as evidence.** Fix: quote the curated or
experimental statement behind the annotation, or mark the row UNDECIDED (IEA-12).

**Leaving the inferred BP after removing the MF.** Fix: follow `GO_REF:0000108` rows to their premise
(IEA-11).

**Reading a mapping's precision as recall, or vice versa.** A mapping can be correct wherever it
fires and still miss most of the family (82.6% of Pfam-A families get no GO term through InterPro).
Absence of an IEA is not evidence of absence ([PFAM](../../PFAM.md)).

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| InterPro curator in [go-annotation#385](https://github.com/geneontology/go-annotation/issues/385) (2007) | Enzyme mappings are not removed because a family has a few catalytically inactive members; inactive members are annotated manually. | A mapping must hold for every member; move catalytic terms to site or active-site entries, or to rules (IEA-2). | Manual negation of pseudo-enzymes does not happen at scale; site entries now make the narrower mapping possible. Reflects the later InterPro direction in [PMID:22301074](https://europepmc.org/article/MED/22301074) and [#2921](https://github.com/geneontology/go-annotation/issues/2921). |
| [wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29) (last reviewed 2020, note added 2026) | Lists EC, HAMAP, InterPro, Rhea, UniProt keywords and subcellular locations as the mappings in use. | KW2GO is retired except for viruses; SubCell2GO, Rhea2GO and EC2GO are being replaced; UniPathway2GO is retired (IEA-6). | The page is out of date relative to the IEA working group decisions; it should carry the status table. |
| [wiki: IEA](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29) | Mappings between vocabularies "manually assessed to be equivalent" are sound bases for IEA. | Only one-hop provenance is acceptable; a vocabulary term assigned by a rule is itself a prediction (IEA-5). | KW2GO could not distinguish manual from predicted keywords; the chain hid errors ([Drive: KW2GO announcement](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk)). |
| [wiki: Annotation consistency: IEA, ISS, IC](https://wiki.geneontology.org/index.php/Annotation_consistency%3A_IEA%2C_ISS%2C_IC_Usage_Discussion) (archived, 2007) | Keyword2GO, EC2GO, SubCell2GO and Compara are reliable enough to display without other information. | Several are now retired or under replacement; Compara needs a consortium decision (IEA-6, IEA-10). | Reviews since 2025 found high error rates and multi-hop provenance; the 2007 assessment predates them. |
| [go-annotation#615](https://github.com/geneontology/go-annotation/issues/615) (2008) | Correct but uninformative IEAs are kept; filtering is the browser's job. | Agree for review actions (IEA-12), but mappings must not target do-not-annotate terms (IEA-4). | The do-not-annotate subset now names terms GO considers unfit for any annotation; [#5902](https://github.com/geneontology/go-annotation/issues/5902) moved one such IEA target into it. |
| [wiki: Ensembl Compara annotation projection](https://wiki.geneontology.org/index.php/Ensembl_Compara_annotation_projection) | Projects experimental rows between one-to-one orthologs; no limit on term type. | Preserve relations; exclude context, development and response-to terms; treat as provisional pending a consortium decision (IEA-10). | Relation upgrades ([#5411](https://github.com/geneontology/go-annotation/issues/5411)) and context transfer ([#1344](https://github.com/geneontology/go-annotation/issues/1344)); Ensembl stopped orthology calls in 2026. |
| [wiki: ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29) and Compara page | Automated orthology transfer is IEA; manually reviewed is ISO. | We note that automated mammalian ISO pipelines contradict this and leave the code question open (see Open questions). | The IEA working group recorded the same inconsistency ([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)). |
| [go-annotation#4573](https://github.com/geneontology/go-annotation/issues/4573) | Open question whether keyword-based CC relations should default to `located_in` rather than `is_active_in`. | A keyword or subcellular-location row is a location claim; transit compartments are not locations of activity and should not be mapped (IEA-8). | Consistent with the ER transit rule in [CLAUDE.md](../../../CLAUDE.md) and [ORGANELLES](../../ORGANELLES.md). |
| UniProt ARBA documentation as summarised in [Drive: ARBA notes for curators](https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz) | Rules have 100% confidence. | Read 100% as in-sample consistency; judge each condition set against experimental annotations (IEA-9, IEA-16). | The same notes list training bias, excluded negatives, template errors and leaking signatures. |
| (no prior GOC guidance) | | Curated conditional rules that couple a sequence condition with a taxon, module or feature condition and name the mapping they replace (IEA-14). | interpro2go cannot express conditions; GOA's taxon transformations were ad hoc and never published as rules. |
| (no prior GOC guidance) | | Sole-source and rule-cover checks before any mapping removal (IEA-13). | Removals proposed without them would have cost correct annotations (IPR000719 ATP binding). |

## Open questions

1. **Mass transfer by orthology.** Should GO keep any automated orthology pipeline (Compara,
   mammalian ISO) for species with active curation, reserve it for "unadopted" species, or retire it?
   If kept, which evidence code? The IEA working group asked for a consortium-wide decision and a new
   working group ([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).
2. **Conditional mappings upstream.** Should interpro2go (or a successor) support taxon and
   negative-domain conditions, so that rules like CR-0001 and CR-0005 can live at the source?
3. **TrEMBL coverage after SubCell2GO, Rhea2GO and EC2GO stop.** The plan is to rely on ARBA gaining
   GO coverage; who measures whether it does, and against what out-of-sample standard?
4. **Collateral loss from retirement.** Blanket retirement of KW2GO removed correct annotations that
   no other source carried (DELLA signalling, patatin storage activity in the repo's plant review). Should
   retirement loss files be curated into manual or PAINT annotations before deletion as standard practice?
5. **Viral keywords.** KW2GO survives for viruses. Should ViralZone keywords map to GO at all, given
   the clade-dependent host-context errors the repo found for phage immune terms ([SPKW](../../SPKW.md))?
6. **Pfam and NCBIfam coverage.** Most Pfam-A families and most NCBIfam models reach no GO term. Should
   GO accept member-database mappings directly when InterPro has not integrated the signature?

## Sources

**GO wiki**

- [wiki: Inferred from Electronic Annotation (IEA)](https://wiki.geneontology.org/index.php/Inferred_from_Electronic_Annotation_%28IEA%29)
- [wiki: Inferred from Sequence Model (ISM)](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Model_%28ISM%29)
- [wiki: Inferred from Sequence Orthology (ISO)](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29)
- [wiki: Ensembl Compara annotation projection](https://wiki.geneontology.org/index.php/Ensembl_Compara_annotation_projection)
- [wiki: Annotation Assigned by](https://wiki.geneontology.org/index.php/Annotation_Assigned_by) (draft)
- [wiki: Annotation consistency: IEA, ISS, IC Usage Discussion](https://wiki.geneontology.org/index.php/Annotation_consistency%3A_IEA%2C_ISS%2C_IC_Usage_Discussion) (archived)
- [wiki: InterPro2GO Session October 4th 2011](https://wiki.geneontology.org/index.php/InterPro2GO_Session_October_4th_2011) (historical)
- [wiki: Planned changes to the IEA GO_REFs cited by UniProtKB](https://wiki.geneontology.org/index.php/Planned_changes_to_the_IEA_GO_REFs_cited_by_UniProtKB.) (archived)

**Drive**

- [Drive: IEA WG GOC meeting Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I) (current decisions)
- [Drive: IEA WG pipelines update Sept 2026](https://drive.google.com/open?id=1FQpXSPZdK78X3wX5UEQ9jkFk6Xex0NCi8NeDawOs7IE)
- [Drive: IEA WG pipelines update GOC 2026](https://drive.google.com/open?id=1lkoSLtiaa_w-P_g2F74u_xii5DeeULCV_6_0kjI413Y) (rubric)
- [Drive: Retiring the KW2GO pipeline](https://drive.google.com/open?id=1QoTlEdEPLu5qteDKynRQsf0SiClWEJzNK3rjQgp23xk)
- [Drive: Ensembl and ISO pipelines](https://drive.google.com/open?id=1q9m9RbQqdpXMPrLq-jzTC-ouLJjUda_XAA93U8zTkNw)
- [Drive: ARBA notes for curators](https://drive.google.com/open?id=1iJcxukKRpwzXV6z0WjW3tb7XI7cIPQJz)
- [Drive: Including IBA annotations in ARBA training](https://drive.google.com/open?id=1eIC-6mENH1bQoHsjDuaXu52IlXm5PyCD)
- [Drive: Rule-based systems in GOA (2025)](https://drive.google.com/open?id=1_XLWtDWUzR0A-u8TTE3OoZa46XpHgICo)
- [Drive: Best practices for predicting GO data](https://drive.google.com/open?id=1z-6rNJ4tg3M-Ant-2kqDXohPZUlkw9GEZ5qlNZDYj18) (legacy draft of the published external-guidelines page)
- [Drive: Draft AI policy statement](https://drive.google.com/open?id=1leeuPb1WDgyORZHrxhapW9HKLTPrCi6xsMi-KaZNCIQ) (draft)

**GitHub issues (geneontology/go-annotation)**

[#385](https://github.com/geneontology/go-annotation/issues/385),
[#390](https://github.com/geneontology/go-annotation/issues/390),
[#615](https://github.com/geneontology/go-annotation/issues/615),
[#1020](https://github.com/geneontology/go-annotation/issues/1020),
[#1134](https://github.com/geneontology/go-annotation/issues/1134),
[#1344](https://github.com/geneontology/go-annotation/issues/1344),
[#1386](https://github.com/geneontology/go-annotation/issues/1386),
[#1519](https://github.com/geneontology/go-annotation/issues/1519),
[#1807](https://github.com/geneontology/go-annotation/issues/1807),
[#1879](https://github.com/geneontology/go-annotation/issues/1879),
[#1887](https://github.com/geneontology/go-annotation/issues/1887),
[#2710](https://github.com/geneontology/go-annotation/issues/2710),
[#2921](https://github.com/geneontology/go-annotation/issues/2921),
[#3007](https://github.com/geneontology/go-annotation/issues/3007),
[#4573](https://github.com/geneontology/go-annotation/issues/4573),
[#5411](https://github.com/geneontology/go-annotation/issues/5411),
[#5432](https://github.com/geneontology/go-annotation/issues/5432),
[#5902](https://github.com/geneontology/go-annotation/issues/5902),
[#6018](https://github.com/geneontology/go-annotation/issues/6018),
[#6085](https://github.com/geneontology/go-annotation/issues/6085)

**Papers**

- [PMID:22301074](https://europepmc.org/article/MED/22301074) Manual GO annotation of predictive protein signatures: the InterPro approach to GO curation (2012)
- [PMID:38995546](https://europepmc.org/article/MED/38995546) Interpreting Gene Ontology annotations derived from sequence homology methods (2024)

**Repository pages**

- [CLAUDE.md](../../../CLAUDE.md) (curated rules; reviewing rules; quoting UniProt)
- [INTERPRO](../../INTERPRO.md) and [INTERPRO README](../../INTERPRO/README.md), [PFAM](../../PFAM.md), [NCBIFam](../../NCBIFam.md)
- [ARBA_REVIEW](../../ARBA_REVIEW.md), [docs: rule review receipts](../../../docs/rule_review_receipts.md), [rules/curated README](../../../rules/curated/README.md)
- [SPKW](../../SPKW.md), [KW_1110_TRAF_KW2GO](../../KW_1110_TRAF_KW2GO.md), [RHEA](../../RHEA.md)
- [TREEGRAFTER](../../TREEGRAFTER.md), [HOMOLOGY_PROPAGATION](../../HOMOLOGY_PROPAGATION.md), [ISO](../../ISO.md), [IBA_REVIEW](../../IBA_REVIEW.md)
- [ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md), [ORGANELLES](../../ORGANELLES.md), [action consistency](../../../docs/action_consistency.md)
