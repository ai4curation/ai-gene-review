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
