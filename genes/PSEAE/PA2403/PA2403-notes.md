# PA2403 (Q9I178) — review notes

No provider deep research is available (perplexity is not a configured provider; the asta
run for the sibling gene in this batch returned twenty citations with no connection to the
subject, so it was not attempted here). These notes stand in its place.

## What is actually known

Very little, and that is the finding.

The UniProt entry is **unreviewed** (TrEMBL, Q9I178_PSEAE, 403 aa) with protein existence
`PE 4: Predicted`. It has no curated FUNCTION, CATALYTIC ACTIVITY, SUBUNIT or DISRUPTION
PHENOTYPE block at all. Its name, "PepSY domain-containing protein", is derived from a Pfam
match (`ECO:0000259|Pfam:PF03413`) rather than from any experiment, and the gene has no
symbol — only the ordered locus name, itself submitter-derived
(`ECO:0000313|EMBL:AAG05791.1`).

What the sequence does say:

- Four predicted transmembrane helices (Phobius: 12-37, 145-168, 199-221, 343-363), so a
  polytopic membrane protein. `ECO:0000256|SAM:Phobius` is sequence-analysis evidence and
  counts as valid computational support.
- Pfam PF03413 (PepSY) plus PF03929 (PepSY_TM); InterPro IPR025711 and IPR005625
  (PepSY-associated TM helix).
- PANTHER **PTHR34219**, whose family name is "IRON-REGULATED INNER MEMBRANE
  PROTEIN-RELATED", subfamily SF8 "PEPSY DOMAIN-CONTAINING PROTEIN".

So the family name and the regulation agree that this is an iron-responsive inner-membrane
protein. Neither says what it does.

## The two annotations, and why both are left undecided

`GO:0002049 pyoverdine biosynthetic process`, **IMP**, PMID:12207696, PseudoCAP.
`GO:0019290 siderophore biosynthetic process`, **IBA**, GO_REF:0000033, from
PANTHER:PTN009150613 whose WITH/FROM is this gene itself.

The second rests entirely on the first. `GO:0002049` is a descendant of `GO:0019290`, so the
IBA is the parent claim propagated from the only seed the node has, which is this one PAO1
row. That is the sole-seed situation this project audits: whatever is wrong with the seed
reaches every descendant of the node.

The paper is a GeneChip study of the iron-starvation response
[PMID:12207696 "GeneChip expression analysis of the iron starvation response in Pseudomonas
aeruginosa: identification of novel pyoverdine biosynthesis genes."] and its criterion for
calling a gene pyoverdine-biosynthetic is stated in the abstract:

> Under low-iron conditions, expression of 26 genes or operons was reduced in a DeltapvdS
> mutant compared with wild type, including numerous novel pyoverdine biosynthetic genes.

That is **PvdS-dependent transcription**. The mutant whose phenotype was scored is
*ΔpvdS* — the pyoverdine sigma factor — and the readout is PA2403's own expression, not
pyoverdine production. Being transcribed under the control of the pyoverdine sigma factor is
evidence of being *regulated with* the pathway; it is not evidence of carrying out a step in
it. PvdS also controls genes outside pyoverdine synthesis, including exotoxin A and PrpL
protease, which the same abstract lists among iron-regulated functions.

**This is a query, not a correction.** The abstract does not name PA2403, the paper has no
PMC record (`convert_article_ids` returns no PMCID, consistent with
`full_text_available: false`), and I cannot read the full text — which is exactly where a
PA2403 deletion assayed for pyoverdine would be reported if it exists. PseudoCAP curators had
the full text and I do not, so the project rule applies: do not overrule an experimental
annotation whose supporting text you have not read. Both rows are therefore `UNDECIDED`, and
the evidence-code concern is filed as a `SUSPECTED` source defect with
`requested_change: CHECK` rather than as a removal.

If the full text does contain only expression data for this gene, the correct code is IEP
(inferred from expression pattern), not IMP, and the IBD at PTN009150613 should be
re-examined, because an expression-dependence seed cannot support propagating a biosynthetic
process across a family.

## What would settle it

**Read the 2003 paper's candidate list first — it is cheaper than any experiment and may settle
the evidence-code question outright.** PMID:12686626 identified fourteen candidate genes, mutated
them and scored pyoverdine
[PMID:12686626 "The candidate genes were mutated and the effects of the
mutations on pyoverdine production were determined. Eight new pvd genes were
identified."], so six were assayed and found not required, and the abstract does not enumerate
the fourteen. If PA2403 is among them it was tested and scored negative, which is much stronger
than never having been followed up; if it is not, the reading in this review stands. That list is
in a readable full text, unlike the 2002 paper, which has no PMC record.

Two further points this review establishes that belong here rather than only in the YAML. The
evidence-code concern is **reference-level, not a single row**: five PAO1 genes carry the identical
PseudoCAP row — `involved_in GO:0002049`, IMP, PMID:12207696 — all dated 20190311 (PA2403, PA2412,
pvdN, pvdO, pvdP), so the request is about what that reference was taken to supply for the set, and
PA2403 is named only because it is the gene under review. And the divergence from **PA2412** is not
a difference of rule: PA2412 reaches ACCEPT on independent deletion-mutant data
[PMID:17502378 "Our results demonstrate that PA2412 is necessary for the production
or secretion of pyoverdine at normal levels."] while recording the same reference as unverified for
IMP; PA2403 has no such independent data, so the same row resolves differently on the same
reasoning.

Only then the wet lab: a clean deletion of PA2403 with pyoverdine quantified by fluorescence or CAS
assay under iron limitation. If pyoverdine is unaffected, both rows go; if it is reduced, the next question is
whether the protein acts in synthesis, in export, or in the iron sensing that gates the
pathway — which its four transmembrane helices and PepSY domains make a live question rather
than a formality.
