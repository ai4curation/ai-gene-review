# A3GALT2 focused report incorporation, 2026-09-21

Read the complete focused OpenScientist report, both CSV artifacts (decision
table and evidence matrix), citation index, and extracted HTML/PDF renderings.
The supplied artifacts contain no executed alignment, raw sequence output or
GTEx data. The numerical expression and identity claims are not adopted as
independently reproduced results.

## Decisive source correction

The report dismisses the positive human experiment because PMID:23378701 has a
pig-organ title and abstract. Full Methods and Figure 6 were independently read
in the publication cache and [live PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3558945/).
They explicitly describe a reconstructed human ORF, expression in CHO cells,
GFP sorting and mock-transfected controls. Exact excerpt: “the human iGb3
synthase showed very weak activity even in the CHO cell transfection experiment”.

The Methods are more precise than the shorthand Results description of cloning:
exon-2-to-exon-5 and exon-5 cDNA fragments came from pediatric thymus, while exon
1 and the start of exon 2 were introduced by a long primer. Thus this is a
human-sequence reconstruction experiment, not demonstration of an intact native
transcript/protein in human tissue. Figure 6 detects iGb3 and iGb4; Table 1 and
the text report weak capacity and no further B4/B5/B6 extension. Product
occurrence in human dendritic-cell lipids is separate evidence and does not
causally identify A3GALT2 as the native enzyme.

PMID:18630988 was re-read through the chimera, mutational and reverse-mutational
results and Methods. Figures 3–4 genuinely show negative human-domain chimeras
and a rat Y252N substitution that abolishes the measured Galα1,3Gal staining.
Figure 5 already tests reverse P187L/N252Y substitutions, individually and
together, in the rat/human exon-5 chimera without restoring staining. The report
misses that result while recommending a reverse mutation as an unperformed
test. An intact human construct with equivalent mutations could still be a
distinct experiment; it is not evidence that the published chimera reversal
was never tested.

The two studies differ in construct and detection method. Neither weak positive
nor negative chimera alone settles the native human role. Keep broad catalytic
and biosynthetic capacities non-core, retain the original NOT as UNDECIDED, and
preserve its source negation. No positive NEW is added.

## Independent sequence and ancestry checks

Live UniProt entries, all sequence version 1:

| Accession | Organism | Length | Residue aligned to human 253 |
|---|---|---:|---|
| U3KPV4 | human | 340 | N253 |
| A0A4Z3 | rat | 339 | Y252 |
| Q3V1N9 | mouse | 370 | Y283 |

The report calls Q3V1N9 rat and mixes rat experimental and human sequence
numbering. Independent global alignment maps human D199/D201 to rat D198/D200
and mouse D229/D231. These identity checks support accurate mapping, not an
inference that the weak positive assay cannot exist. Sequences, entry dates,
checksums and alignment settings are recorded in `A3GALT2-sequence-check.json`.

The live PTHR10462 tree gives:
`PTN008945697 → PTN000049004 → PTN002573328 → PTN000825659 → PTN000049131 →
PTN000049132 → PTN001627154 → PTN002573333 → PTN004161251 → PTN002470899`.
The last node is human U3KPV4. The local PAINT IBDs for Golgi, vesicle and broad
glycosyltransferase at PTN000049004 and glycosphingolipid biosynthesis at
PTN000049131 are therefore ancestors. No negative row occurs on this path.
Source response provenance is saved in `A3GALT2-paint-lineage.json`.

## Separate LacNAc question

The ISS source is rat **A0A4Z3**, not GGTA1. Rat UniProt attributes RHEA:13013 to
PMID:10854427, which the report did not assess. Its verified abstract reports
glycolipid preference; that does not establish absence of all glycoprotein or
LacNAc transfer. Official fetch returned abstract only; publisher PDF and HTML
requests were blocked, and the text-mining API returned metadata rather than
full assay text. The exact LacNAc assay remains unverified. Keep both
GO:0047276 rows UNDECIDED: the human lactosylceramide result neither establishes
nor excludes this GlcNAc-containing acceptor reaction.

The 2007 comparative-genomics conclusion in PMID:17298992 is historical context
that predates the 2013 human reconstruction. Its abstract was checked, but it
cannot replace reconciliation of the contradictory direct experiments.

All 11 original source objects are preserved. Actions remain unchanged from
the preceding full-gene review; reasons, primary/reference assessments and
actual lineage evidence now incorporate the report critically. No duplicate
provider request was launched.
