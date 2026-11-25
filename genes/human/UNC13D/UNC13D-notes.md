# UNC13D (Munc13-4, UniProtKB:Q70J99) — curation notes

## Provenance of this file

No `-deep-research-*.md` file exists for UNC13D. Only `openscientist` and `claude_code` are registered as
providers in this environment; earlier attempts in this campaign showed `falcon` and `perplexity` are not
available, and the one openscientist run attempted in an earlier batch was stopped by the session's
background limit without producing output. No provider file was written, and this file is deliberately
**not** named as one. These are my own notes from the cached publications, the UniProt record, the local
GO edit file, QuickGO and the PANTHER classification files, with provenance for each assertion.

## What the protein is

A cytosolic, peripheral membrane priming factor for the exocytosis of secretory lysosomes in
haematopoietic cells: two Munc13 homology domains flanked by two C2 domains, with no transmembrane
segment and Ca2+ bound at the C2 sites (UniProt `FT BINDING`). It works as the effector of small GTPases,
and three are documented.

- **Rab27a**, on the granule. The partnership was established with the cloning of the relationship
  [PMID:15548590 "We show that Munc13-4 is a direct partner of rab27a."], and the disease alleles on both
  sides break it [PMID:15548590 "the FHL3 mutant Munc13-4Delta608-611 failed to bind rab27a"]. The binding
  site on the GTPase is mapped, by patients rather than by mutagenesis [PMID:25312756 "All 6 patients
  carried mutations at amino acids R141, Y159, or S163 of Rab27a that disrupt the interaction of Rab27a
  with Munc13-4, without impairing the interaction between melanophilin and Rab27a."]. That selectivity
  is why those patients have normal pigment and failed cytotoxicity.
- **Rab15**, in endothelium [PMID:22899725 "a specific effector of Rab27, Munc13-4, appears to be also an
  effector of Rab15 and is required for WPB exocytosis"].
- **RhoG**, at the plasma membrane [PMID:33513601 "We discovered that RhoG engages in a protein-protein
  interaction with Munc13-4, an exocytosis protein essential for CG fusion with the PM."], where the
  recruitment runs the other way than one might expect: the interaction increases RhoG's own affinity for
  membrane lipids and thereby targets UNC13D to them (UniProt `CC:SUBUNIT`).

## Two jobs, shown to be separable

This is the fact that shapes the review. One paper separates them cleanly: independently of Rab27a,
Munc13-4 assembles the exocytic-vesicle pool [PMID:17237785 "Independently of Rab27a, hMunc13-4 mediated
the assembly of Rab11(+) recycling and Rab27(+) late endosomal vesicles, constituting a pool of vesicles
destined for regulated exocytosis."], and with active Rab27a it primes the granule
[PMID:17237785 "It also primed cytotoxic granule fusion, possibly through interaction with active
Rab27a."]. UniProt summarises the pair as granule maturation plus granule docking and priming at the
immunologic synapse.

That is why the record's three endosomal location rows (late endosome, recycling endosome, exocytic
vesicle) are accepted as core rather than treated as incidental: they are the compartments the protein
builds, not places it passes through.

## Comparator checks run for this review

Both by term id against QuickGO, with the hit count checked non-zero first, following the rule added to
`CLAUDE.md` after the GZMB false negative.

| Question | Result |
|---|---|
| Is `GO:0043316` cytotoxic T cell degranulation a real gap? | **Yes.** 12 human rows, so the query returns positives. The carriers are this gene's own fusion partners — STX11 ×5, STXBP2 ×2, SNAP23, VAMP8 — plus CEACAM1, FCGR2B and NCKAP1L. The convention therefore admits the fusion machinery; the cargo does not carry it (perforin and the granzymes: zero). UNC13D is the one member of that module missing from the term. Proposed as `NEW`. |
| Should `GO:0061792` secretory granule maturation be proposed, since both UniProt and the paper title say Munc13-4 is required for granule maturation? | **No.** The term plus its descendant `GO:1990502` carry six human rows between them, all on neuroendocrine dense-core-vesicle biogenesis genes (HID1, BAIAP3, PTPRN, SNX19). What Munc13-4 does is deliver a separate endosomal vesicle that fuses with an already-formed granule, which is a different kind of claim. Raised as a `suggested_questions` entry instead. |
| Should `GO:0043320` natural killer cell degranulation be proposed as well? | **Not here.** It is as true biologically, and PMID:17237785 names NK cells, but no gene in the current annotation set carries both siblings and the NK assay is not among the evidence read for this review. Left for a curator with it in hand; the companion STXBP2 review does propose it, from a row whose own evidence is an NK experiment. |

## Ontology facts checked rather than assumed

- `GO:0017137` Rab GTPase binding and `GO:0017048` Rho GTPase binding are **both alt_ids of `GO:0031267`
  small GTPase binding** in the current edit file, surviving only as NARROW synonyms. So the
  generic-sounding term really is the most specific one available for this protein's three GTPase
  partnerships, and the five bare `GO:0005515` rows whose partners are Rab27a or RhoG are refined onto it
  rather than onto a child that no longer exists.
- `GO:0101004` cytolytic granule membrane is `bounding_layer_of GO:0044194` cytolytic granule, which is
  itself `is_a GO:0005764` lysosome. So proposing the membrane term covers the granule by part_of and
  there is no need to propose both — the project's rule against proposing a term and its ancestor
  together applies.
- `GO:0043306` positive regulation of mast cell degranulation is a descendant of `GO:0043304` through
  positively_regulates being a sub-property of regulates, so the mast cell MODIFY is a refinement and not
  a lateral move.

## The two Reactome rows

`Reactome:R-HSA-6798751` is "Exocytosis of azurophil granule lumen proteins", and it gives this gene
`GO:0035578` azurophil granule lumen and `GO:0005576` extracellular region. Both are topologically wrong
for this protein: no signal peptide, no transmembrane segment, no Secreted keyword, C2 domains that bind
membrane lipids from the cytosol, and two partners (Rab27a, RhoG) that are themselves cytosolic. A protein
in the granule lumen would be separated from its own partners by a bilayer.

Recorded as a `WRONG_TERM` source defect against Reactome at `PROBABLE` with `requested_change: CHECK`
rather than asserted, because the cached Reactome entry holds only the event summary and no participant
list, so what Reactome actually models for this protein cannot be read from here. Contrast the same
granule on STXBP2, where the GOA row is `GO:0042582` azurophil granule — the organelle, which is right
for a cytosolic-face protein.

## Three mouse-ortholog projections that go one step too far

`GO:0001944` vasculature development, `GO:0060155` platelet dense granule organization and `GO:1900026`
positive regulation of substrate adhesion-dependent cell spreading all arrive from mouse Unc13d by
Ensembl Compara, and all three share one shape: a secretion factor acquiring the downstream processes that
its cargo affects. Munc13-4 primes a granule; what the released cargo then does to vessels, or to how a
platelet spreads, is done by the cargo and by the cells that respond to it. Marked over-annotated rather
than removed, since the loss-of-function consequences are presumably real. For the dense granule row,
`GO:0002576` platelet degranulation would be the fitting term, but it is not proposed as a replacement
because MODIFY needs this row's own evidence and an ortholog projection whose mouse experiment cannot be
read is not that.
