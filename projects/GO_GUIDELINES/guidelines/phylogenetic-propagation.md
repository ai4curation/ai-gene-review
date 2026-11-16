# Phylogenetic and orthology-based propagation: GO annotation guidelines

Status: draft v0.1 (2026-11-15) · Part of [GO_GUIDELINES](../../GO_GUIDELINES.md)

**In brief:**

- An IBA is the mechanical consequence of a PAINT curator's IBD placed on an ancestral
  PANTHER node. To challenge an IBA, argue with the node placement or the seed, never with
  the number of donors.
- The target gene appearing in its own IBA `WITH/FROM` is expected and is not circular.
  Genuine circularity is a chain with no experimental grounding anywhere in it.
- Propagate what the lineage inherited: conserved molecular function first, cellular
  processes cautiously, organismal, tissue, "response to" and regulatory-sign context almost
  never.
- Record a loss explicitly (IKR when key residues are gone, IRD for divergence without a
  residue explanation) rather than silently declining to propagate, and never add back what a
  PAINT loss deliberately removed without saying so.
- ISO and ISS need an experimentally supported donor that still carries the term, the right
  orthology edge (all paralogs named for one-to-many), and a term that is safe to move.
- A leaf whose only annotations are IBA is under-annotated, not finished.

## Scope

This document covers annotations that reach a gene product by inheritance or transfer from
another gene product:

- **PAINT** curation on PANTHER trees: IBD (ECO:0000319, biological aspect of descendant
  evidence used in manual assertion) on ancestral nodes, and the IBA (ECO:0000318) rows that
  descendants receive, with `GO_REF:0000033`.
- **PAINT losses**: IKR (ECO:0000320, phylogenetic determination of loss of key residues) and
  IRD (ECO:0000321, rapid divergence from ancestral sequence).
- **Curator-reviewed similarity transfers**: ISS (ECO:0000250), ISA (ECO:0000247) and ISO
  (ECO:0000266), including the automated mammalian ISO pipelines (`GO_REF:0000119`,
  `GO_REF:0000096`, `GO_REF:0000121`).
- When and why propagation should stop: subfunctionalisation, neofunctionalisation,
  pseudo-enzymes, lineage-specific processes and taxon constraints.

TreeGrafter (`GO_REF:0000118`) and Ensembl Compara (`GO_REF:0000107`) are electronic and are
covered in [electronic-annotation.md](electronic-annotation.md); this document refers to them
only where they share a failure mode with IBA or ISO. ISM (sequence-model matches) is also in
the electronic document, since it is not a transfer from a gene. How NOT behaves in general is
in [qualifiers-and-negation.md](qualifiers-and-negation.md); how to record a verdict on an
existing row is in [reviewing-annotations.md](reviewing-annotations.md).

## Principles

**Every transfer has three parts, and each can fail on its own.** A donor (the gene product
with experimental evidence), an intermediate (the orthology call, similarity judgement or
PANTHER node), and a target. A review asks three separate questions: is the donor annotation
sound and current, is the relation the right one, and is this term safe to move. The repo's
`propagation_review` vocabulary records where the defect lives
([HOMOLOGY_PROPAGATION](../../HOMOLOGY_PROPAGATION.md), [ISO](../../ISO.md#failure-taxonomy)).

**PAINT is a judgement, not a similarity score.** The curator inspects the tree, the
alignment and every experimental annotation in the family, then decides where a function
arose ([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines);
[PMID:21873635](https://europepmc.org/article/MED/21873635), Gaudet et al. 2011). A single
judgement at a deep node reaches thousands of proteins, so the cost of an error and the value
of a fix are both multiplied. Fix the node, not the leaves.

**Molecular function is more conserved than process, and process more than context.** The
ortholog conjecture is a reasonable prior for biochemistry, a weak one for cellular process,
and no guide at all for tissue, developmental stage or physiological response
([ORTHOLOG_CONJECTURE](../../ORTHOLOG_CONJECTURE.md)). In the repo's ISO review, the commonest
failure was context that does not carry over, not wrong biochemistry ([ISO](../../ISO.md)).

**Absence of a propagated term is not evidence of absence, and absence of an IBA is not
evidence of novelty.** PAINT is conservative by construction. In 1,015 reviewed human genes,
511 curated core molecular functions had no IBA support at all
([IBA_REVIEW](../../IBA_REVIEW.md#iba-incompleteness-core-function-that-iba-fails-to-propagate)).

## Rules

<a id="ph-1"></a>

### PH-1. Review an IBA by its node placement, not by its donor count

**An IBA asserts that the target descends from a node at which a curator judged the function
to have arisen. Challenge it by showing the target sits outside the clade that inherited the
function, or that the target lost or changed the function after the node.**

Rationale: the IBA row is a mechanical output; the judgement lives in the IBD. A node seeded
by one well-characterised MOD or human gene can be sound, because the curator made the call
with the whole tree and alignment in view. The 2019 PAINT tracker discussion between curators
who wanted a two-seed minimum and PAINT curators who did not ([go-annotation#2382](https://github.com/geneontology/go-annotation/issues/2382))
shows why donor count is a poor proxy: single-seed IBDs fail when the BP term is loosely tied
to the MF, not because they are single.

Worked example: *S. pombe* Epe1 receives `GO:0032452` histone demethylase activity by IBA from
JmjC-domain relatives. The argument against it is target-specific: Epe1's Fe(II)-binding triad
has Tyr in place of the third His ligand and no demethylase activity is detectable in vitro
([IBA_REVIEW](../../IBA_REVIEW.md), pattern 1). The node is right for KDM2A/KDM2B; the leaf
lost the activity. The correct fix is a loss below the node (PH-9), not removal of the IBD.

Counter-example: UBA7 receives `GO:0019782` ISG15 activating enzyme activity by IBA, while
the InterPro2GO row gives only `GO:0008641` ubiquitin-like modifier activating enzyme
activity. Here the IBA is the more precise and better-supported claim
([IBA_REVIEW](../../IBA_REVIEW.md), pattern 2).

Provenance: [GOC+]. Sharpens [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)
and the repo rule in [CLAUDE.md](../../../CLAUDE.md) ("What an IBA asserts").

<a id="ph-2"></a>

### PH-2. Seed an IBD only from experimental annotations that make the claim the term makes

**An IBD must rest on experimental annotations (IDA, IMP, IGI, IPI, IEP, EXP and their HTP
counterparts under PH-3) on descendant gene products. Before using a seed, check that its
evidence type can support the aspect: an IMP phenotype grounds "needed for" a process, not a
molecular function.**

Rationale: only experimental annotations may support ancestral inference
([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)).
That rule says nothing about whether the experiment supports the aspect, and the repo found
IBDs whose sole seed was a molecular-function row derived from a pleiotropic mutant phenotype
([IBA_REVIEW](../../IBA_REVIEW.md), pattern 16). The cheap diagnostic is to read the seed's
sibling rows from the same reference: a block of IMP rows spanning unrelated processes is a
phenotype list, and the MF row inside it cannot stand. The 2023 PAINT tracker discussion of
TMX3 (PTHR46426) reached the same place: do not propagate an MF from a single IMP when a human
IDA in the family points to a different activity ([go-annotation#4697](https://github.com/geneontology/go-annotation/issues/4697)).

Worked example: the IBD for `GO:0004096` catalase activity on PANTHER node PTN001247822
(PTHR30071, CcmC) has one seed, *P. aeruginosa* CcmC, whose catalase row is an IMP from a
paper that also yields IMP rows for pyoverdine biosynthesis and several motility processes.
That set is the phenotype of a strain with no mature c-type cytochromes. Every CcmC leaf
inherits catalase activity, and the inter-ontology rule then adds `GO:0098869` cellular
oxidant detoxification as IEA. Withdrawing the seed must withdraw both
([IBA_REVIEW](../../IBA_REVIEW.md), §ccmC). Record such a case as
`root_cause: SOURCE_BAD` with `failure_modes: [SOURCE_EVIDENCE_WEAK]`.

Provenance: [GOC+]. The aspect check is our addition to the GOC seed rule.

<a id="ph-3"></a>

### PH-3. Use high-throughput seeds and single seeds only with an independent second line

**An IBD may rest on one seed gene or on HTP evidence when at least one independent line
agrees: a domain or active site consistent with the MF, a coherent MF-BP-CC set for the clade,
or unannotated literature in another lineage. A BP propagated from a single seed needs a
direct, mechanistic link to an MF or CC already placed on the same node.**

Rationale: the PAINT guideline already allows single-paper and HTP seeds with supporting data,
and notes that identical annotations from one paper in several species are not independent
([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)).
The HTP working group allowed HTP-evidenced rows to seed ISS/ISA/ISO/IBA with case-by-case
review ([go-annotation#1775](https://github.com/geneontology/go-annotation/issues/1775)).
Disputes about single seeds cluster on loosely connected BP terms such as "receptor
localization to synapse" or neuronal identity ([go-annotation#2382](https://github.com/geneontology/go-annotation/issues/2382),
[go-annotation#2219](https://github.com/geneontology/go-annotation/issues/2219)), while
single-seed MF on a conserved ribosomal or ubiquitin-ligase subunit is uncontroversial. The
rule targets the failing case without forbidding the sound one.

Worked example: SAP18 (PTHR13082) carried a corepressor IBD that FlyBase and PomBase curators
first read as a single-entity transfer. The PAINT curator's reply cited repression data for
human and *Arabidopsis* SAP18 outside GO, which is exactly the independent second line this
rule asks for; the residual question was whether fungi had lost the activity
([go-annotation#3413](https://github.com/geneontology/go-annotation/issues/3413)). Literature
outside GO counts, but the IBD's evidence box should cite it so that reviewers can see it.

Provenance: [GOC+]. Resolves a standing disagreement between curators who want a two-seed rule
and PAINT curators who reject one; we side with neither and condition on the term.

<a id="ph-4"></a>

### PH-4. Place the IBD at the deepest node the evidence supports, and no deeper

**Start from the most recent common ancestor of the experimentally annotated sequences. Move
the node deeper only when orthology, active-site conservation, consistent annotations in other
aspects, and the absence of contradicting well-studied members support it. Move it shallower,
or annotate twice, when the function plausibly arose more than once. Never place a term above
the taxon in which its prerequisite exists.**

Rationale: this is the PAINT A/B/C decision: the MRCA is right, the function is older, or it
is younger and convergent ([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)).
We add an explicit prerequisite test, because the cleanest repo failures are terms placed where
the protein family arose rather than where the pathway arose. Taxon-constraint violations in
PAINT come from three sources: old IBDs above an `only_in_taxon` limit, propagation through a
`never_in_taxon` clade, and horizontal transfer nodes
([wiki: 13 March 2024 PAINT call](https://wiki.geneontology.org/index.php/13_March_2024_PAINT_Conference_Call)).
PAINT now blocks CC and BP propagation below horizontal-transfer nodes
([wiki: 11 Feb 2026 PAINT call](https://wiki.geneontology.org/index.php/11_Feb_2026_PAINT_Conference_Call)).

Worked example: the STAT family IBD for `GO:0007259` cell surface receptor signaling pathway
via JAK-STAT sits on PTN000927860, the Unikonts node, though its seeds support only Bilateria.
JAKs are animal-only, so worm STA-1 and STA-2 and *Dictyostelium* STATs inherit a pathway their
lineage lacks. The PIAS node PTN000845825 likewise passes `GO:0046426` negative regulation of
receptor signaling pathway via JAK-STAT to worm GEI-17. The class-level fix is a taxon
constraint on the pathway term, which GO accepted; the node-level fix is a move of the IBD
(`TOO_DEEP`) or IRDs on the nematode and amoebozoan branches ([PAINT](../../PAINT.md),
[IBA_REVIEW](../../IBA_REVIEW.md), pattern 14, [TAXON_PATHWAY_VARIANCE](../../TAXON_PATHWAY_VARIANCE.md)).

Provenance: [GOC] for the A/B/C logic and HGT blocking; [GOC+] for the prerequisite test.

<a id="ph-5"></a>

### PH-5. Do not propagate binding-only, redundant, indirect or contextual terms

**Never place an IBD on: `GO:0005515` protein binding or its uninformative children such as
`GO:0042802` identical protein binding and `GO:0042803` protein homodimerization activity; a
partial MF already entailed by a placed MF (ligand binding under receptor activity, DNA
binding under a DNA-binding transcription factor activity); a one-step BP that restates a
placed MF; a downstream process the protein does not directly carry out; a "response to"
term; a localization process that reads as a mutant phenotype; any term in
`gocheck_do_not_annotate`.**

Rationale: the first four are in the PAINT guideline
([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines);
[go-annotation#2097](https://github.com/geneontology/go-annotation/issues/2097) for protein
binding). "Response to" terms are usually not propagated, with narrow exceptions such as
starvation for autophagy proteins ([go-annotation#2171](https://github.com/geneontology/go-annotation/issues/2171),
[go-annotation#2250](https://github.com/geneontology/go-annotation/issues/2250)). Localization
processes such as `GO:0048254` snoRNA localization, when the protein assembles the particle
and mislocalisation is the mutant readout, are phenotypes
([go-annotation#5691](https://github.com/geneontology/go-annotation/issues/5691)). PAINT
re-curated 505 families to remove do-not-annotate IBDs and now filters those terms from the
curation matrix ([wiki: 10 July 2024 PAINT call](https://wiki.geneontology.org/index.php/10_July_2024_PAINT_Conference_Call)).

Worked example: *S. pombe* sdh7 received `GO:0006979` response to oxidative stress and
regulation of gluconeogenesis by IBA from PTN000320077. The family's direct role is
mitochondrial complex II assembly; the other terms were removed from the node
([go-annotation#2171](https://github.com/geneontology/go-annotation/issues/2171)).

Provenance: [GOC], with the localization clause [GOC+] (a 2025 tracker consensus, not yet in
the written guideline).

<a id="ph-6"></a>

### PH-6. Propagate substrate and cargo specificity only within a duplication-free clade

**A substrate-specific MF (enzyme or transporter) may descend only to members that share the
seed's specificity without an intervening duplication that could have changed it. Across
duplications, place the general parent term on the deep node and the specific term on the
subclade with direct evidence.**

Rationale: the PAINT guideline asks for caution with substrates
([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)).
We make it operational. A PAPS transporter term propagated over an ancient duplication into a
fungal UDP-GlcNAc transporter was fixed by restricting the term to the animal-only node
([go-annotation#2033](https://github.com/geneontology/go-annotation/issues/2033)). The repo's
substrate cases fail the same way: the family node lumps specificities, and the leak can be in
the cleaved substrate or the co-substrate ([IBA_REVIEW](../../IBA_REVIEW.md), pattern 11;
[ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md)).

Worked example: human NQO2 inherits `GO:0003955` NAD(P)H dehydrogenase (quinone) activity from
the NQO1/NQO2 node (PTHR10204), but NQO2 uses dihydronicotinamide riboside, not NAD(P)H. The
correct term, `GO:0001512` dihydronicotinamide riboside quinone reductase activity, is already
supported by IDA. Because `GO:0001512` is not a descendant of `GO:0003955`, the review action is
a lateral MODIFY, and the PAINT fix is to restrict `GO:0003955` to the NQO1 clade. Human AGK
carries `GO:0001729` ceramide kinase activity from a node lumping acylglycerol and sphingosine
kinases; two direct assays found no ceramide phosphorylation ([IBA_REVIEW](../../IBA_REVIEW.md)).

Provenance: [GOC+].

<a id="ph-7"></a>

### PH-7. Do not propagate a cellular component across a node whose members live in different compartments

**When paralogs with different localisations interleave below a node, place no CC on that
node. Annotate compartments only on nodes whose descendants share them, and leave mixed nodes
without a CC.**

Rationale: compartment is not conserved across paralogs even when the fold and reaction are.
For alanyl-tRNA synthetases, where cytosolic and mitochondrial members are mixed in the tree,
the 2024 consensus was that saying nothing is better than a wrong compartment
([go-annotation#5546](https://github.com/geneontology/go-annotation/issues/5546)). The repo
found the same leak for nucleus onto cytoplasmic PIWI proteins, plasma membrane onto
ribosome-associated Hsp70s, and mitochondrion onto cytosolic ALDH1L1
([IBA_REVIEW](../../IBA_REVIEW.md), patterns 10 and 13).

Worked example: rat ALDH1L1 receives `GO:0005739` mitochondrion by IBA. UniProt names it the
cytosolic 10-formyltetrahydrofolate dehydrogenase and it has a cytosol IDA; the mitochondrial
paralog is ALDH1L2. When reviewing a localisation IBA, place both compartments in the GO
hierarchy first: `GO:0005634` nucleus versus `GO:0005737` cytoplasm is mutually exclusive and
a valid REMOVE; `GO:0005737` cytoplasm over a mitochondrial protein is not, because
`GO:0005739` mitochondrion is `part_of` cytoplasm. Root organelle terms follow
[cellular-component.md](cellular-component.md) and [ORGANELLES](../../ORGANELLES.md).

Provenance: [GOC+].

<a id="ph-8"></a>

### PH-8. Ignore seed qualifiers except NOT; carry `contributes_to` only where the subunit's role is conserved

**When judging whether an experimental row supports an IBD, ignore its gene-product-to-term
relation except NOT. IBDs default to `involved_in` (BP), `is_active_in` (CC) and `enables`
(MF). Use `contributes_to` on an IBD, ISS or ISO only when the seed carries it and the target
is a subunit of the same complex in which the activity is distributed. The annotation should
still read correctly if a consumer strips the qualifier.**

Rationale: the qualifier policy for GAF 2.2 is a 2020 PAINT decision
([wiki: 5 May 2020 PAINT call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)).
It means an `acts_upstream_of_or_within` seed can yield an `involved_in` IBA, which upgrades the
claim; the seed check in PH-2 is therefore where indirect evidence must be caught. PAINT
propagates the qualifier the primary annotation had and cannot add or remove it; where seeds
disagree the PAINT curator chooses ([go-annotation#5254](https://github.com/geneontology/go-annotation/issues/5254)).
Curators agreed that a `contributes_to` may be carried into an ISS/ISA, and that this should be
documented ([go-annotation#3242](https://github.com/geneontology/go-annotation/issues/3242)).
Peripheral RNA polymerase subunits are the cautionary case: `GO:0003899` DNA-directed RNA
polymerase activity with `contributes_to` is defensible on core subunits and doubtful on
Rpb4/7, which the enzyme does not need for catalysis ([go-annotation#1319](https://github.com/geneontology/go-annotation/issues/1319)).

Worked example: SPO11 might borrow `contributes_to` endonuclease activity from archaeal Top6A
by ISA. The PomBase view, which we adopt, is to use `contributes_to` only for distributed active
sites (polymerases, proteasome) and to prefer a regulator term or a weaker MF when the subunit
is known not to be catalytic ([go-annotation#3242](https://github.com/geneontology/go-annotation/issues/3242)).

Provenance: [GOC] for defaults; [GOC+] for the strip test and the seed-relation caveat.

<a id="ph-9"></a>

### PH-9. Record a loss with IKR or IRD, and choose IKR when a key residue explains it

**When members below an annotated node have lost the function, record the loss. Use IKR when
the loss is explained by missing key residues and say which residues. Use IRD for divergence
with no residue explanation. Before placing either, check that the loss clade does not contain
a seed of the IBD it blocks.**

Rationale: losses are part of the GOC design ([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines);
[wiki: IKR](https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29)), but
the two codes behave very differently downstream. An IKR produces a NOT|IBA on every
descendant, which users can see. An IRD sits only on the internal node in PAINT's `IBD.gaf` and
produces nothing for the genes below it: GOA holds no IRD rows, and none of PAINT's NOT|IBA leaf
rows comes from an IRD alone ([IRD_EVIDENCE](../../IRD_EVIDENCE.md)). A curator who knows the
residue therefore loses information by using IRD, which is the point of the PAINT team's
preference for IKR when a catalytic residue is missing
([go-annotation#2109](https://github.com/geneontology/go-annotation/issues/2109)). The IKR page
requires a `WITH/FROM` naming the alignment, domain or rule when the reference is a GO_REF, and
warns that families have exceptions: WNK1 lacks the canonical catalytic Lys yet is active
because another Lys substitutes ([wiki: IKR](https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29)).
When a paper both shows the missing site and assays inactivity, make both NOT IKR and NOT IDA.

Worked example: rat HPT matches the peptidase S1 domain but has lost the catalytic triad, so it
carries NOT `GO:0004252` serine-type endopeptidase activity by IKR with `InterPro:IPR000126` in
`WITH/FROM` ([wiki: IKR](https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29)).
Counter-example: the fungal IRD that blocks `GO:0042026` protein refolding on PTHR19375
(PTN001065099) is right for SSB and SSZ1, which fold nascent chains, and wrong for SSA, because
yeast SSA1 is itself a seed of the blocked IBD and has two refolding IDA rows. The repo verdict
is `LOSS_TOO_BROAD`, with the request to move the IRD onto the SSB/SSZ1 branch
([IRD_EVIDENCE](../../IRD_EVIDENCE.md)). Of 19 contested IRDs adjudicated in the repo, 12
looked wrong and 2 too broad, and in six of the 19 the loss clade contained a seed of the IBD
it blocked; that sample is biased towards conflicts and is not an error rate.

Provenance: [GOC] for the codes; [GOC+] for "prefer IKR" and the seed-in-clade check; [NEW] for
the requirement to name the residues (PANTHER does not publish them, see
[PANTHER_IBA_REVIEW](../../PANTHER_IBA_REVIEW.md)).

<a id="ph-10"></a>

### PH-10. NOT propagates only to the term annotated; a positive general term still descends

**A NOT on a node blocks that term (and, by GO semantics, its descendants) for the clade, but
never blocks the term's parents. When positive and negative experimental rows coexist at the
same or a more general level, the positive row governs unless the curator places an explicit
loss.**

Rationale: these are the PAINT propagation cases set out in 2014
([wiki: 11 MAR 2014 PAINT call](https://wiki.geneontology.org/index.php/11_MAR_2014_PAINT_Conference_Call)).
If a general term is placed at the root and a specific child is stopped at a clade, the
clade still inherits the general term; a NOT on the child says nothing about the parent. The
reverse also holds: a curated experimental NOT on a gene
should block a contradicting positive IBA on that gene, which PAINT intends and has repaired
when tree changes broke it ([wiki: 1 March 2023 PAINT call](https://wiki.geneontology.org/index.php/1_March_2023_PAINT_Conference_Call)).

Worked example: human CRYAA has a curated NOT `involved_in` `GO:0042026` protein refolding, and
also an IBA to the same term. The IBA contradicts a curated negative on the target and should be
removed ([IBA_REVIEW](../../IBA_REVIEW.md), pattern 8). The broader `GO:0006457` protein folding,
of which refolding is a child, is not blocked by the NOT.

Provenance: [GOC].

<a id="ph-11"></a>

### PH-11. The target in its own `WITH/FROM` is not circular

**When a gene's own experimental annotation helped seed the IBD, the gene legitimately appears
in the `WITH/FROM` of the IBA it receives. Do not call it circular, do not mark the source
`CIRCULAR_OR_REDUNDANT`, and do not remove the IBA for that reason. Reserve "circular" for a
chain with no experimental grounding anywhere, or a source that adds nothing because the target
has stronger direct evidence for the same claim.**

Rationale: the IBA on a seed says something its experimental row does not: that the function is
inherited rather than lineage-specific. Treating self-reference as circularity confuses the
provenance of the IBD (which includes the seed) with the evidence for the leaf. The repo audit
found 27 rows wrongly marked circular for this reason ([CLAUDE.md](../../../CLAUDE.md);
[IBA_REVIEW](../../IBA_REVIEW.md#what-an-iba-actually-asserts-and-two-ways-to-misread-the-withfrom)).
The 2018 tracker position was the opposite: "No IBA should have the same sequence in column 2
(object) and in column 8 (with)" ([go-annotation#2042](https://github.com/geneontology/go-annotation/issues/2042)).
A later thread records that self-referential IBAs were in fact retained in the export
([go-annotation#2219](https://github.com/geneontology/go-annotation/issues/2219)). Display
redundancy is a filtering problem for browsers, not an evidential defect.

Worked example: a single FlyBase gene seeded septate-junction terms on PTN000456925 and then
received IBAs citing only itself. The defect there was not the self-reference but the node: the
other descendants were neuronal Ig proteins with no septate-junction biology, and the tree was
withdrawn for re-curation ([go-annotation#2219](https://github.com/geneontology/go-annotation/issues/2219)).
Argue with the node (PH-1), not with the `WITH/FROM`.

Provenance: [NEW]. Departs from go-annotation#2042.

<a id="ph-12"></a>

### PH-12. Read the `WITH/FROM` first, and count donors correctly

**Before judging an IBA, resolve every gene in its `WITH/FROM` and the PTN node. Wrong-family
donors or a single wrong-paralog donor are near-mechanical evidence of a placement error. A
broad, coherent set of true orthologs means the transfer is probably sound: slow down.**

Rationale: in the repo's catalogue this was the single most useful diagnostic
([IBA_REVIEW](../../IBA_REVIEW.md), pattern 12). Two counting traps recur: the
`PANTHER:PTN…` entry is the node, not a donor; and one gene can appear twice under different
identifiers (a MOD id and a UniProt accession). No sentence may claim more than the enumeration
shows: "the IBD seed" asserts a sole donor and must be checked.

Worked examples: human NTN1 and NTN3, secreted netrins, carried `GO:0000981` DNA-binding
transcription factor activity, RNA polymerase II-specific; the donors were POU-domain
transcription factors (wrong family). NOTCH1 carried `GO:0007411` axon guidance with SLIT1/2/3
as donors. ABRAXAS1 carried spindle terms whose only donor was its paralog ABRAXAS2 (wrong
paralog) ([IBA_REVIEW](../../IBA_REVIEW.md), pattern 12).

Provenance: [GOC+].

<a id="ph-13"></a>

### PH-13. Stop propagation at duplications that changed function, at pseudo-enzymes, and at lineage boundaries

**Do not let an ancestral term reach members that (a) sit in a post-duplication subclade with a
documented different function, (b) have lost catalytic residues while keeping the fold, (c)
belong to a lineage in which the process or its prerequisites do not exist, or (d) were
characterised only in an organism-specific context that the target does not share.**

Rationale: these are the recurrent failure classes in the repo's IBA catalogue: neo- and
subfunctionalisation (opposite reactions within one family), pseudo-enzymes, regulatory-sign
inversion in families with activators and inhibitors, lineage-inappropriate processes and
context transfer ([IBA_REVIEW](../../IBA_REVIEW.md), patterns 4, 7, 9, 14, 6). Signals that
call for a check: a long branch, a different EC number in the subclade, a UniProt CAUTION or an
"Inactive" name, a vertebrate or insect donor on a process absent from the target's lineage.
Small leaf-level duplications in *S. pombe*, *C. elegans*, insects and plants deserve the same
scrutiny ([wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines)).
Check the mechanism as well as the conclusion: in a residue pass over 17 alleged pseudo-enzymes,
four had an intact catalytic site and were inactive for another reason (truncation, a blocked
zymogen junction, lost substrate contacts) ([IBA_REVIEW](../../IBA_REVIEW.md), pattern 7).

Worked examples: Cds1 (PTHR10314 SF135) inherits `GO:0019344` L-cysteine biosynthetic process
from the family root, but catalyses cysteine breakdown (EC 4.4.1.1) on the family's longest
branch. Mosquito TOLL9 inherits `GO:0006954` inflammatory response from human TLR4; insects have
Toll-pathway immunity but no vertebrate inflammation. Poplar plastid NDH subunits inherit
`GO:0009060` aerobic respiration from mitochondrial complex I homologs. BCL2 inherits
`GO:0043065` positive regulation of apoptotic process from a node whose donors mix BAX and BAK1
with anti-apoptotic members; for BCL2 the core term is `GO:0043066` negative regulation of
apoptotic process. Human RIMBP2 inherits neuromuscular synaptic transmission from a fly donor
studied at the NMJ ([IBA_REVIEW](../../IBA_REVIEW.md)).

Provenance: [GOC+].

<a id="ph-14"></a>

### PH-14. Before REMOVE on an IBA, complete the checklist and route the fix to the node

**A REMOVE or MARK_AS_OVER_ANNOTATED on an IBA must record: the term definition, aspect,
qualifier and taxon constraints; the PTN node and the seeds from `WITH/FROM`; the target's and
seeds' PANTHER subfamilies; a separate verdict on the source and on the propagation; and the
target-specific evidence (experiments, curated NOT rows, active-site residues, domain
architecture, localisation, isoforms, lineage). Then file the node-level fix.**

Rationale: per-gene removals leave the node in place and the next release reissues the error.
The repo's family reviews record the PAINT action in machine-readable form (`paint_action`:
MOVE_IBD, REMOVE_IBD, ADD_IRD, ADD_IKR, REMOVE_LOSS, MOVE_LOSS, with `target_node_id`), and the
`propagation_review` block separates `root_cause` (for example `SOURCE_BAD`, `PROPAGATION_BAD`,
`TERM_SCOPING_PROBLEM`) from biological `failure_modes` ([CLAUDE.md](../../../CLAUDE.md);
[IBA_REVIEW](../../IBA_REVIEW.md#propagation-taxonomy-and-checklist)). Cross-subfamily
propagation is triage evidence, not a verdict: in *S. pombe*, 36 cross-subfamily flags turned
out to be mostly conserved functions ([PANTHER_IBA_REVIEW](../../PANTHER_IBA_REVIEW.md)). PAINT
prunes per annotation, so a loss of a general term does not block a specific term placed on an
ancestor; request each change separately.

Worked example: worm GEI-17 inherits `GO:0046426` from PTN000845825, which is sound for human
PIAS1 and fly Su(var)2-10. Because GEI-17 and the fly seed share subfamily SF94, no subfamily
scope separates them; the requested fix is an IRD on the nematode branch, not removal of the IBD
([IBA_REVIEW](../../IBA_REVIEW.md), pattern 14).

Provenance: [GOC+]. The PAINT tracker asks for tickets with the PTHR id, PTN node, sequences and
error type ([go-annotation#5546](https://github.com/geneontology/go-annotation/issues/5546) shows
the template).

<a id="ph-15"></a>

### PH-15. Treat an IBA-only leaf as under-annotated, and check for orthologs split across families

**When a gene's only annotations in an aspect are IBA, or IBA supplies only a general parent,
look for the specific experimentally defined activity before concluding. When a gene has no IBA
but its one-to-one ortholog does, check whether PANTHER placed the pair in different families.**

Rationale: PAINT carries what the ancestor carries, at the ancestor's granularity. In the repo's
evidence-subtraction analysis, 62% of annotation-grounded core-function terms in 1,015 human
genes would be lost if IBA were the only evidence. A third mechanism is classification: the
human gene is not a descendant of the annotated node at all ([IBA_REVIEW](../../IBA_REVIEW.md#iba-incompleteness-core-function-that-iba-fails-to-propagate)).
PAINT itself is re-checking IBDs made before its 2017 database load after users reported
missing key terms ([wiki: 14 Jan 2026 PAINT call](https://wiki.geneontology.org/index.php/14_Jan_2026_PAINT_Conference_Call)).

Worked example: human DNAH12 sits in PTHR46532 and has no IBA; mouse Dnah12 sits in PTHR10676
and receives eight, including `GO:0036159` inner dynein arm assembly. The human review proposed
the same term from patient and knockout data. The mouse leaf also inherits
`GO:0008569` minus-end-directed microtubule motor activity, but DNAH12 lacks the
microtubule-binding domain, so that term should not transfer. Report the split to PANTHER;
meanwhile review the human gene's candidate terms one by one, citing the PTN node, and do not
assume all of them carry over ([IBA_REVIEW](../../IBA_REVIEW.md), §C).

Provenance: [NEW].

<a id="ph-16"></a>

### PH-16. ISO needs a current experimental donor, the right orthology edge, and every co-ortholog named

**An ISO row must name in `WITH/FROM` an orthologous gene product whose own annotation to the
term is experimental and still present. For one-to-many orthology, name every paralog in the
target's co-ortholog group. Do not transfer NOT, annotation extensions, or binding-only terms.
Re-run ISO when orthology calls change.**

Rationale: the ISO page makes the experimental donor and the `WITH/FROM` mandatory, names all
paralogs for one-to-many cases, and asks for updates when orthology predictions change
([wiki: ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29)).
MGI's documented rat-to-mouse pipeline transfers only IDA, IPI, IGI, IMP and EXP, excludes
`GO:0005515` and `GO:0005488`, brings no NOTs and no extensions ([Drive: MGI ISO rat filters](https://drive.google.com/open?id=1lx65V8ikyofnkDdwojm6fhHZ801ET1Z9)).
What the guidance does not say is how often donors go stale: of 4,232 ISO rows in the repo, 383
rest on a donor that no longer carries the term ([HOMOLOGY_PROPAGATION](../../HOMOLOGY_PROPAGATION.md)).

Worked examples: mouse Ghr receives ISO from human GHR and rat Ghr, true orthologs, but several
transferred terms (growth factor binding, response to estradiol) are no longer on the human
donor; a stale donor is a reason to look, not automatically a wrong term. Mouse Calm3 receives
ISO from rat Calm1 and Calm2 as well as from human CALM3 (`UniProtKB:P0DP25`), because the
mouse-rat pipeline donates across the three loci; harmless for protein-level terms since the
three proteins are identical, wrong for locus-level biology such as Calm3's dendritic mRNA
localisation ([ISO](../../ISO.md)).

Provenance: [GOC] for donor and `WITH/FROM`; [GOC+] for the currency check.

<a id="ph-17"></a>

### PH-17. Move conserved activity by orthology; do not move context

**By ISO or ISS, transfer molecular function and the cellular processes it directly executes.
Treat tissue, developmental, organismal, physiological-response, disease and regulatory-sign
terms as unsafe to transfer unless the target has its own evidence. Treat a donor that is not
the target's namesake (a paralog or a member of an expanded family) as a flag.**

Rationale: most ISO rows that reviewers downgrade are true but contextual
(`CONTEXT_OR_TISSUE_MISMATCH` was the commonest failure mode in 304 structured ISO reviews), and
ISO rows whose donors all carry a different symbol from the target are rejected or reduced about
three times as often as those with a namesake donor ([ISO](../../ISO.md)). Transfer between fungi
from orthologs only, and expect transcription and signalling processes to diverge
([go-annotation#1380](https://github.com/geneontology/go-annotation/issues/1380));
transfer across kingdoms produced auxin-signalling and leaf-formation terms on yeast elongator
([go-annotation#1807](https://github.com/geneontology/go-annotation/issues/1807)). A signed
causal chain flattened by export to `acts_upstream_of_or_within` loses its sign before transfer,
so orthology copies an antagonist into the process it opposes ([ISO](../../ISO.md), Akt1/Pck1).

Worked example: mouse Ang2 receives ISO from human ANG (`UniProtKB:P03950`). Mouse evidence
supports ribonuclease activity, not angiogenesis or receptor signalling; Ang2 is a divergent
member of an expanded rodent family, not ANG's namesake. Most rows were removed as
`PROPAGATION_BAD` with `WRONG_ORTHOLOG_OR_PARALOG` and `FUNCTIONAL_DIVERGENCE` ([ISO](../../ISO.md)).

Provenance: [GOC+].

<a id="ph-18"></a>

### PH-18. ISS and ISA need an experimentally characterised match, a reviewed alignment, and no binding-only terms

**Make an ISS or ISA only from a match whose annotation is experimental or IC, after checking
the alignment length, identity and conservation of residues the function needs. Put the match
in `WITH/FROM`; cite a paper that did the analysis or `GO_REF:0000024` when the curator did. Use
ISO instead when orthology is established. Never make ISS-family annotations to `GO:0005515`
protein binding. Antibody cross-reactivity is not similarity evidence.**

Rationale: the experimental-match rule prevents transitive annotation errors, and GO sets no
numeric identity cutoff because none works across lineages ([wiki: ISA](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Alignment_%28ISA%29);
[wiki: ISS](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29)).
GORULE:0000005 blocks ISS-family protein binding ([wiki: ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29));
the reason is that `WITH/FROM` cannot carry both the donor and the binding partner
([go-annotation#1876](https://github.com/geneontology/go-annotation/issues/1876)). A 2004 annotation
camp ruled out antibody cross-reaction ([go-annotation#11](https://github.com/geneontology/go-annotation/issues/11)).
ISS to a complex identifier is acceptable once orthology of each subunit is checked
([go-annotation#1925](https://github.com/geneontology/go-annotation/issues/1925)). Any automated
step in bulk transfer makes the evidence IEA ([wiki: ISA](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Alignment_%28ISA%29)).

Worked example: *S. cerevisiae* AAC3, cloned and shown to be similar to the characterised ADP/ATP
translocators AAC1 and PET9, may receive the antiporter activity by ISA from the paper that did
the alignment, with AAC1 and PET9 in `WITH/FROM`. Nat5p, similar to characterised NATs but with
no characterised member in its own orthologous group, may receive the general NAT activity by
ISA but nothing by ISO ([wiki: ISA](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Alignment_%28ISA%29)).

Provenance: [GOC].

<a id="ph-19"></a>

### PH-19. Do not add back what a phylogenetic curator deliberately removed

**Before proposing a NEW annotation, an ISS or an ISO for a term, check whether the target sits
under a PAINT IRD, IKR or NOT for that term. If it does, either argue with the loss explicitly
(and file the PAINT ticket) or do not add the term.**

Rationale: IRD is the least visible curation decision in GO, because it produces no row a
reviewer can see ([IRD_EVIDENCE](../../IRD_EVIDENCE.md)). PAINT curators now place preventive NOTs
on families specifically to stop positive ISS annotations following positive IEAs
([wiki: 14 Jan 2026 PAINT call](https://wiki.geneontology.org/index.php/14_Jan_2026_PAINT_Conference_Call)).
The repo found 24 IBAs in cached GOA files for terms PAINT has since blocked, and NEW rows with
direct experimental support that now argue against a PAINT loss; those rows are not invalid, but
must say so ([IRD_EVIDENCE](../../IRD_EVIDENCE.md)). This is the phylogenetic case of the general
NEW bar in [CLAUDE.md](../../../CLAUDE.md) ("Do not add what curators deliberately declined to add").

Worked example: yeast SSA3 and SSA4 rest only on the refolding IBA, which the fungal IRD (PH-9)
now withdraws. A reviewer who re-adds `GO:0042026` to SSA3 must cite target evidence and dispute
the IRD; their nearest experimental rows support only `GO:0006457` protein folding.

Provenance: [NEW].

<a id="ph-20"></a>

### PH-20. Keep IBA, TreeGrafter and automated orthology distinct in review and in tickets

**IBA (`GO_REF:0000033`, assigned by GO_Central) is curated; TreeGrafter (`GO_REF:0000118`,
IEA) grafts a sequence onto a PANTHER node and copies its terms without a curator; Ensembl
Compara (`GO_REF:0000107`, IEA) copies experimental annotations between one-to-one orthologs.
When a propagated row is wrong, decide whether the node annotation is wrong (fix in PAINT) or the
sequence was grafted onto the wrong node (fix in PANTHER/TreeGrafter), and file accordingly.**

Rationale: TreeGrafter output is routinely mistaken for IBA. Reviewers accepted 43% of
uncorroborated TreeGrafter rows against 73% of IBA rows, and in about three of four downgraded
TreeGrafter rows the placement was sound and the inherited node term was the problem
([TREEGRAFTER](../../TREEGRAFTER.md)). PAINT distinguishes the two cases and routes TreeGrafter
tickets to the PANTHER team ([wiki: 11 Feb 2026 PAINT call](https://wiki.geneontology.org/index.php/11_Feb_2026_PAINT_Conference_Call)).
TreeGrafter can also lag PAINT, propagating annotations that PAINT had already removed
([wiki: 14 Aug 2024 PAINT call](https://wiki.geneontology.org/index.php/14_August_2024_PAINT_Conference_Call)).

Worked example: three *S. rosetta* cadherins each carry ten animal-junction terms from graft node
PTN000616280 (PTHR24027:SF422). The placement is plausible; the inherited terms describe
multicellular adherens junctions in a unicellular organism, so the fix is a lineage block on the
node, not a regrafting ([TREEGRAFTER](../../TREEGRAFTER.md)).

Provenance: [GOC+].

## Decision aid

| Situation | Action on the row | Upstream fix |
|---|---|---|
| IBA term true for target, target also has EXP and appears in `WITH/FROM` | ACCEPT (PH-11) | none |
| IBA donors are a coherent set of orthologs, target has no contrary evidence | ACCEPT or KEEP_AS_NON_CORE by core status (PH-1, PH-12) | none |
| Target lost catalytic residues; fold retained; independently documented | REMOVE (PH-13) | ADD_IKR below node, naming residues (PH-9) |
| Subclade has a different substrate or co-substrate; correct term exists | MODIFY to the subclade term, lateral if needed (PH-6) | MOVE_IBD for the specific term |
| Process absent from target lineage, or prerequisite absent | REMOVE (PH-4, PH-13) | MOVE_IBD (`TOO_DEEP`) or ADD_IRD; propose taxon constraint |
| Compartment mutually exclusive with target's known location | REMOVE (PH-7) | REMOVE_IBD on mixed node |
| Compartment broader than but containing target's location | keep; do not REMOVE (PH-7) | none |
| Sole seed is IMP for an MF, or seed's paper is a phenotype list | REMOVE or UNDECIDED (PH-2) | REMOVE_IBD; dispute the seed row |
| Family node mixes activators and inhibitors; sign leaks | MODIFY to the correct-sign term (PH-13) | MOVE_IBD to the correct-sign clade |
| ISO donor no longer carries term | Check target biology; stale donor alone is not REMOVE (PH-16) | refresh pipeline |
| ISO donor is a paralog / expanded-family member | Scrutinise; REMOVE if target evidence diverges (PH-17) | report orthology call |
| ISO of a tissue, response-to or developmental term, no target evidence | KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED (PH-17) | none |
| Target under a PAINT IRD/IKR for a term you want to add | Do not add, or add with explicit dispute (PH-19) | PAINT ticket |
| Leaf has only general IBA term | Look for specific EXP activity; MODIFY or NEW (PH-15) | request deeper IBD |
| Gene has no IBA, ortholog has many | Check PANTHER family split (PH-15) | PANTHER ticket |

## Common errors

**Removing an IBA because the target "has only one donor".** Donor count is not evidential
strength. Fix: argue the node or the leaf (PH-1).

**Marking self-reference as circular.** Fix: leave the source as `SUPPORTS_TRANSFER`; use
`CIRCULAR_OR_REDUNDANT` only for ungrounded chains (PH-11).

**Calling a broad localisation IBA wrong.** `GO:0005737` cytoplasm on an organellar protein is
imprecise, not false. Fix: check `part_of` before REMOVE (PH-7).

**Treating the PTN node as a donor, or one gene's two identifiers as two donors.** Fix: resolve
`WITH/FROM` before counting (PH-12).

**"Lacks the catalytic residues" asserted without an alignment.** About a quarter of such claims
in one repo pass were wrong about the mechanism. Fix: align against an active control and state
the residue (PH-9, PH-13).

**Fixing the leaf and leaving the node.** The next PAINT or GOA release restores the row. Fix:
file `paint_action` with `target_node_id` (PH-14).

**ISO rows rejected because "there is no mouse evidence".** Transfer without target data is what
ISO asserts; that sentence is a tautology. Fix: give the reason the term does not transfer
(divergence, context, stale donor) ([IBA_REVIEW](../../IBA_REVIEW.md), "What the count is for").

**Upgrading the relation by propagation.** An `acts_upstream_of_or_within` seed yields an
`involved_in` IBA (PH-8), and Ensembl Compara has done the same across species
([go-annotation#5411](https://github.com/geneontology/go-annotation/issues/5411)). Fix: check the
seed's relation, not only its evidence code.

**Re-adding a term PAINT withdrew.** Cached GOA files can predate an IRD. Fix: check the current
PAINT release before writing NEW (PH-19).

## Differences from prior guidance

| Prior source | What it said | What we recommend | Why |
|---|---|---|---|
| [go-annotation#2042](https://github.com/geneontology/go-annotation/issues/2042) (2018) | No IBA should have the same sequence as object and in `WITH/FROM`; self-referential IBAs should not exist. | Self-reference is expected and not circular; keep such IBAs (PH-11). | The IBA on a seed asserts inheritance, which the seed's own row does not. [go-annotation#2219](https://github.com/geneontology/go-annotation/issues/2219) records that self-referential IBAs were retained anyway; the sources conflict and current export practice matches our rule. |
| FlyBase position in [go-annotation#2382](https://github.com/geneontology/go-annotation/issues/2382), [#3413](https://github.com/geneontology/go-annotation/issues/3413) | IBDs should need more than one supporting gene. | Single seeds allowed with an independent second line; single-seed BP needs a direct MF/CC link (PH-3). | PAINT curators and PomBase rejected a blanket rule in the same threads; failures concentrate on loosely linked BP, so we condition on the term. |
| [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines) | Only experimental annotations may seed an IBD. | Also check that the seed's evidence type supports the aspect (IMP does not support MF) (PH-2). | Experimental-code seeds have carried phenotype-derived MFs to whole families (ccmC). |
| [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines) | Choose MRCA, older or younger node by curator judgement. | Add an explicit test: never above the taxon where the term's prerequisite exists (PH-4). | JAK-STAT terms placed where STATs arose rather than where JAKs arose reached worms and amoebae. |
| [wiki: IRD](https://wiki.geneontology.org/index.php/Inferred_from_Rapid_Divergence%28IRD%29) (2018) | IRD "implies a NOT annotation"; example is a gene-level NOT row citing a TAIR communication. | IRD lives on internal nodes and creates no gene rows; prefer IKR when a residue explains the loss; check the loss clade for seeds (PH-9). | Current PAINT data contain no gene-level IRD rows; the wiki example no longer matches the data ([IRD_EVIDENCE](../../IRD_EVIDENCE.md)). The IRD page's three empty sections should be filled. |
| [wiki: IKR](https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29) | `WITH/FROM` must indicate the lacking residues via an alignment, domain or rule id. | Also name the residues in the review or ticket (PH-9). | PANTHER does not publish which residues an IKR used, so a domain id alone is not checkable. |
| [wiki: 5 May 2020 PAINT call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call) | Seed qualifiers other than NOT are ignored; IBDs default to `involved_in`/`is_active_in`/`enables`. | Keep the default, but check `acts_upstream_of_or_within` seeds for indirect evidence before placing a BP (PH-8). | The default silently upgrades indirect seeds to direct claims. |
| [go-annotation#1319](https://github.com/geneontology/go-annotation/issues/1319), [#5254](https://github.com/geneontology/go-annotation/issues/5254), [#3242](https://github.com/geneontology/go-annotation/issues/3242) | `contributes_to` propagates as made; should be documented. | Carry it only for distributed active sites; the row must read correctly if the qualifier is stripped (PH-8). | Software strips qualifiers; peripheral subunits otherwise inherit catalytic activity. |
| [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines) | Do not propagate protein binding, redundant MF/BP, indirect downstream processes. | Add "response to" terms, phenotype-like localization processes and do-not-annotate terms (PH-5). | Tracker consensus in 2018-2025 ([#2171](https://github.com/geneontology/go-annotation/issues/2171), [#2250](https://github.com/geneontology/go-annotation/issues/2250), [#5691](https://github.com/geneontology/go-annotation/issues/5691)) and the 2024 do-not-annotate clean-up are not in the written guideline. |
| [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines) | Be cautious with substrates. | Substrate terms only within duplication-free clades; general parent across duplications (PH-6). | Turns a caution into a rule that can be checked on the tree. |
| [go-annotation#5546](https://github.com/geneontology/go-annotation/issues/5546) | (tracker consensus) Not propagating a CC is right for mixed families. | Formalised as PH-7, with the mutually-exclusive versus subsuming test for reviewers. | Not in any written guideline; reviewers over-removed subsuming terms. |
| [wiki: ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29) | If any step is automated, use IEA, even when orthology is curated. | We record that GO_REF:0000119/0000096/0000121 pipelines are automated yet emit ISO, and review them as transfers of their donor (PH-16). | The written rule and practice disagree; the IEA working group lists this inconsistency as unresolved ([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)). See Open questions. |
| [wiki: ISO](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29) | Update annotations when orthology predictions change. | Also check donor currency: the donor must still carry the term (PH-16). | 383 of 4,232 repo ISO rows rest on a donor that dropped the term. |
| [wiki: ISS](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29) | Transfer from HTP-evidenced rows with care. | Same, plus treat context terms as unsafe to move regardless of the donor's evidence (PH-17). | Context is the commonest ISO failure, independent of evidence type. |

## Open questions

1. **Evidence code for automated orthology pipelines.** The mammalian ISO pipelines are
   automated but emit ISO; Ensembl Compara emits IEA for the same kind of transfer. Should GO
   require IEA for both, create a distinct code, or accept ISO for pipelines with documented
   filters? The IEA working group asked for a consortium-wide decision on mass transfer via
   orthology ([Drive: IEA WG Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)).
2. **Self-referential IBAs.** Our rule keeps them. Should GO formally retire the 2018 statement
   in go-annotation#2042, and should browsers suppress the IBA where the same gene has EXP to the
   same term?
3. **IRD visibility.** Should PAINT export NOT|IBA for IRD clades, or a separate "propagation
   blocked" file, so that reviewers can see deliberate absences?
4. **Residue disclosure for IKR.** Can PAINT record the residues behind each IKR in a field
   rather than in the curator's head?
5. **A machine-readable "do not propagate by orthology" flag on terms** (proposed in
   [go-annotation#1344](https://github.com/geneontology/go-annotation/issues/1344) and
   [#1807](https://github.com/geneontology/go-annotation/issues/1807)). Taxon constraints cover
   lineage, but not tissue or physiological context.
6. **Mixed seeds for sign.** When a family node's seeds include both positive and negative
   regulators of a process, should PAINT require the parent "regulation of" term on the node?

## Sources

**GO wiki**

- [wiki: PAINT annotation guidelines](https://wiki.geneontology.org/index.php/PAINT_annotation_guidelines) (last reviewed 2021)
- [wiki: Inferred from Key Residues (IKR)](https://wiki.geneontology.org/index.php/Inferred_from_Key_Residues_%28IKR%29) (2018)
- [wiki: Inferred from Rapid Divergence (IRD)](https://wiki.geneontology.org/index.php/Inferred_from_Rapid_Divergence%28IRD%29) (2018; thin)
- [wiki: Inferred from Biological aspect of Ancestor (IBA)](https://wiki.geneontology.org/index.php/Inferred_from_Biological_aspect_of_Ancestor_%28IBA%29) (2018; thin)
- [wiki: Inferred from Sequence Orthology (ISO)](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Orthology_%28ISO%29) (2018)
- [wiki: Inferred from Sequence Alignment (ISA)](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_Alignment_%28ISA%29) (2018)
- [wiki: Inferred from Sequence or structural Similarity (ISS)](https://wiki.geneontology.org/index.php/Inferred_from_Sequence_or_structural_Similarity_%28ISS%29) (2024)
- [wiki: 11 MAR 2014 PAINT call](https://wiki.geneontology.org/index.php/11_MAR_2014_PAINT_Conference_Call) (historical)
- [wiki: 5 May 2020 PAINT call](https://wiki.geneontology.org/index.php/5_May_2020_PAINT_Conference_Call)
- [wiki: 1 March 2023 PAINT call](https://wiki.geneontology.org/index.php/1_March_2023_PAINT_Conference_Call)
- [wiki: 13 March 2024 PAINT call](https://wiki.geneontology.org/index.php/13_March_2024_PAINT_Conference_Call)
- [wiki: 10 July 2024 PAINT call](https://wiki.geneontology.org/index.php/10_July_2024_PAINT_Conference_Call)
- [wiki: 14 Aug 2024 PAINT call](https://wiki.geneontology.org/index.php/14_August_2024_PAINT_Conference_Call)
- [wiki: 14 Jan 2026 PAINT call](https://wiki.geneontology.org/index.php/14_Jan_2026_PAINT_Conference_Call)
- [wiki: 11 Feb 2026 PAINT call](https://wiki.geneontology.org/index.php/11_Feb_2026_PAINT_Conference_Call)

**Drive**

- [Drive: IEA WG GOC meeting Fall 2026](https://drive.google.com/open?id=1cEmQivoBNbojaN6IjcDmQd74-VjEuYY4MmSMC2l1M9I)
- [Drive: MGI ISO rat filters](https://drive.google.com/open?id=1lx65V8ikyofnkDdwojm6fhHZ801ET1Z9)

**GitHub issues (geneontology/go-annotation)**

[#11](https://github.com/geneontology/go-annotation/issues/11),
[#1319](https://github.com/geneontology/go-annotation/issues/1319),
[#1344](https://github.com/geneontology/go-annotation/issues/1344),
[#1380](https://github.com/geneontology/go-annotation/issues/1380),
[#1775](https://github.com/geneontology/go-annotation/issues/1775),
[#1807](https://github.com/geneontology/go-annotation/issues/1807),
[#1876](https://github.com/geneontology/go-annotation/issues/1876),
[#1925](https://github.com/geneontology/go-annotation/issues/1925),
[#2033](https://github.com/geneontology/go-annotation/issues/2033),
[#2042](https://github.com/geneontology/go-annotation/issues/2042),
[#2097](https://github.com/geneontology/go-annotation/issues/2097),
[#2109](https://github.com/geneontology/go-annotation/issues/2109),
[#2171](https://github.com/geneontology/go-annotation/issues/2171),
[#2219](https://github.com/geneontology/go-annotation/issues/2219),
[#2250](https://github.com/geneontology/go-annotation/issues/2250),
[#2382](https://github.com/geneontology/go-annotation/issues/2382),
[#3242](https://github.com/geneontology/go-annotation/issues/3242),
[#3413](https://github.com/geneontology/go-annotation/issues/3413),
[#4697](https://github.com/geneontology/go-annotation/issues/4697),
[#5254](https://github.com/geneontology/go-annotation/issues/5254),
[#5411](https://github.com/geneontology/go-annotation/issues/5411),
[#5546](https://github.com/geneontology/go-annotation/issues/5546),
[#5691](https://github.com/geneontology/go-annotation/issues/5691)

**Papers**

- [PMID:21873635](https://europepmc.org/article/MED/21873635) Gaudet et al. 2011, Phylogenetic-based propagation of functional annotations within the Gene Ontology consortium
- [PMID:38995546](https://europepmc.org/article/MED/38995546) Interpreting Gene Ontology annotations derived from sequence homology methods (2024)

**Repository pages**

- [CLAUDE.md](../../../CLAUDE.md) (IBA section; PANTHER section; NEW bar)
- [IBA_REVIEW](../../IBA_REVIEW.md), [PANTHER_IBA_REVIEW](../../PANTHER_IBA_REVIEW.md), [PAINT](../../PAINT.md)
- [IRD_EVIDENCE](../../IRD_EVIDENCE.md), [ISO](../../ISO.md), [HOMOLOGY_PROPAGATION](../../HOMOLOGY_PROPAGATION.md)
- [ORTHOLOG_CONJECTURE](../../ORTHOLOG_CONJECTURE.md), [TREEGRAFTER](../../TREEGRAFTER.md), [FAMILIES](../../FAMILIES.md), [FUNGAL_PAINT_FAMILIES](../../FUNGAL_PAINT_FAMILIES.md) (family-level reviews of fungal IBD nodes)
- [ENZYME_SPECIFICITY](../../ENZYME_SPECIFICITY.md), [TAXON_PATHWAY_VARIANCE](../../TAXON_PATHWAY_VARIANCE.md), [ORGANELLES](../../ORGANELLES.md)
