# dpm-1 (U4PF58): evidence and exact-input prediction review

The enzyme name and reaction paragraph overassign full-length DPM1 activity to a 51-residue C-terminal product lacking the entire annotated glycosyltransferase domain.

## Input identity and functional boundary

U4PF58 corresponds exactly to residues 189–239 of the 239-residue same-gene reference Q9TYJ7. The selected WormBase transcript is Y66H1A.2b; the longer reference is Y66H1A.2a. None of the reference glycosyltransferase-2-like domain at residues 8–176 is present. This establishes a domain boundary, not whether the shorter transcript is translated or functional.

## Biological evidence

- [PMID:10835346 — Human dolichol-phosphate-mannose synthase consists of three subunits, DPM1, DPM2 and DPM3.](https://pubmed.ncbi.nlm.nih.gov/10835346/): The primary mammalian complex study distinguishes catalytic DPM1 from regulatory subunits; it does not demonstrate activity of the short worm product.

> mammalian DPM synthase contains catalytic DPM1 and regulatory DPM2

## Exact non-GO claims

The complete emitted record is preserved in [dpm-1-protnlm-source.json](dpm-1-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Dolichol-phosphate mannosyltransferase

NPI (CS 0). The sequence is DPM1-derived, but naming the isolated 51-residue tail as an active dolichol-phosphate mannosyltransferase overstates its function. A DPM1-derived C-terminal product description would preserve identity without assigning the absent catalytic machinery.

### Function

> Transfers mannose from GDP-mannose to dolichol monophosphate to form dolichol phosphate mannose (Dol-P-Man) which is the mannosyl donor in pathways leading to N-glycosylation, glycosyl phosphatidylinositol membrane anchoring, and O-mannosylation of proteins

NPI (CS 0). The full GDP-mannose-to-dolichol-phosphate transfer reaction requires a glycosyltransferase domain absent from the input. No full-length donor annotation can rescue that missing architecture. The glycosylation pathways listed are valid consequences of the full-length enzyme reaction, but not demonstrated functions of this peptide. [Sequence and domain mapping](dpm-1-bioinformatics/RESULTS.md); [DPM complex study](https://pubmed.ncbi.nlm.nih.gov/10835346/).

### Location

> Membrane

UNC (CS 1). A C-terminal peptide might retain an interaction determinant, but membrane association of this exact product has not been demonstrated. Localization of the full DPM complex cannot establish it.

No GO or EC term was emitted in this record; the name, function and location assessments above constitute its prediction review.

## Family integration

DPM1 sequence identity is established by an exact same-gene match. Catalytic family function requires preservation of the glycosyltransferase fold; the isolated tail does not qualify. This is not evidence for an evolved full-fold pseudoenzyme or for an incorrect input sequence in the prediction pipeline.

## Evidence limits

No exact-product protein expression or functional experiment was found. The genuine Falcon synthesis discusses conventional DPM1 biology without addressing the 51-residue input and is therefore insufficient for its catalytic assessment. The cached 2000 primary paper is abstract-only and supports the subunit distinction, not worm isoform function.

Exact sequence mapping: [dpm-1-bioinformatics/RESULTS.md](dpm-1-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This pass used no ProtNLM output. Its evidence is the UniProt records, a new sequence analysis, the cached
primary papers and the falcon deep research.

**Identity: the benchmark is an isoform fragment.** U4PF58 is the WormBase Y66H1A.2b product, 51 aa long.
It is identical to residues 189-239 of the canonical dpm-1 product Q9TYJ7 (Y66H1A.2a, 239 aa). UniProt has
no reviewed (Swiss-Prot) dpm-1 entry, and Q9TYJ7 and U4PF58 are the only two dpm-1 entries.
U4PF58 has no part of the glycosyltransferase 2-like domain (canonical 8-176). This was reproduced
independently from live UniProt records by `dpm-1-bioinformatics/compare_sequences_rereview.py`, with
output in `RESULTS-rereview.md`. The existing `RESULTS.md` and `compare_sequences.py` were left unchanged.

**Evolutionary grounding.** U4PF58, Q9TYJ7, human DPM1 (O60762) and yeast Dpm1 (P14020) are all in
PTHR43398:SF1, according to UniProt PANTHER cross-references. Q9TYJ7 is 64.7% identical to human DPM1
over 238 aligned columns, so the worm gene belongs to the metazoan three-subunit DPM synthase lineage,
where the catalytic DPM1 relies on DPM3 for tethering and stability
[PMID:16280320 "DPM1 was rapidly degraded by the proteasome in the absence of DPM3."].
PAINT places GO:0004582 at PTN002459128. Its seeds include human O60762, mouse Dpm1, yeast and
Mycobacterium proteins. So the activity is grounded for the full-length worm product, though not for
this fragment. The U4PF58 segment maps to human DPM1 211-260. That stretch holds only 2 of the 13
GDP-mannose binding residues that UniProt annotates by similarity to the archaeal structure
(Q8U4M3), and it has no metal-binding residue.

**Annotation decisions.** GO:0004582 (IEA, InterPro2GO) is kept as REMOVE for this product. I added a
`source_defects` entry (PROBABLE, REPOINT U4PF58 -> Q9TYJ7) so that the row can go upstream as a
fragment-coverage problem. The annotation is right for the gene and wrong only for this product.
No NEW terms were proposed: the fragment has no demonstrated activity, location or partner, and
core_functions stays empty. The description was rewritten to state the isoform relationship and
what is retained.

**Family review.** The family review `interpro/panther/PTHR43398/PTHR43398-review.yaml` lists U4PF58 as
the representative of SF1, and its GO:0004582 assessment is UNRESOLVED with an explicit exclusion for
the exact product. There is no subfamily-placement disagreement. Q9TYJ7 would make a better SF1
representative than the fragment. That is a suggestion for the family file and has not been applied
here.

**Next relative.** The canonical product Q9TYJ7 has no review in the repo. Because `genes/worm/dpm-1` is
keyed to the fragment, its review would go in `genes/worm/dpm-1__Q9TYJ7`. Related modules are
`modules/dolichol_phosphate_sugar_donor_supply.yaml` (Dol-P-Man synthase branch),
`modules/n_glycan_llo_assembly_lumenal.yaml`, `modules/gpi_anchor_core_glycan_assembly.yaml` and
`modules/dolichyl_phosphate_biosynthesis.yaml`.
