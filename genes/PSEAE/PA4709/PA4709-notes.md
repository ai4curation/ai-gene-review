# PA4709 (Q9HV89) review notes

## The gene is phuS, and the entry does not say so

The UniProt entry carries no gene name — only `OrderedLocusNames=PA4709` — and a submitter-supplied
`SubName: Full=Probable hemin degrading factor {ECO:0000313|EMBL:AAG08095.1}`. Two independent
lines put it in the *phu* operon as **phuS**:

- The neighbouring locus **PA4710 is `phuR`** (UniProt Q9HV88, "Heme/hemoglobin uptake outer
  membrane receptor PhuR"), and PMID:10658665 describes the operon as `phuR` followed by
  `phuSTUVW`, so PA4709 is the first gene of that second transcript.
- The sequence matches the characterised protein exactly where it matters. PhuS is described as
  "a cytoplasmic, 39 kDa heme-binding protein" with alternate heme ligands "at positions 209 and
  212" [PMID:18020455]. Q9HV89 is **354 residues** (≈39 kDa) and carries **His at both 209 and
  212** — the local sequence is `LKDTHHFHALLK` for 205-216, confirmed against the fetched record.

The domain content agrees: `Pfam PF05171 HemS` (twice), `InterPro IPR007845 HemS/ChuX_dom`,
`IPR053733 Heme_Transport_Util_sf`.

## "Hemin degrading factor" is the wrong name

The HemS/ChuX family was originally named on the assumption that it degraded heme. PhuS does not:
it **binds** heme in the cytoplasm and **delivers** it to the iron-regulated heme oxygenase HemO,
which performs the degradation.

- [PMID:18990702 "The present data suggest that PhuS has a dual function in trafficking heme to HO,
  and in directly or indirectly sensing and maintaining iron and heme homeostasis."]
- [PMID:22451925 "we have discovered that holo-PhuS, but not apo-PhuS, forms a 1:1 complex with
  HemO"] — and the transfer is directional, the paper's title calling it "Induced fit on heme
  binding ... drives interaction with heme oxygenase (HemO)".

So the entry's name attributes to PhuS the activity of its partner. Filed as a `WRONG_STATEMENT`
source defect against UniProt at `PROBABLE`, with the missing `GN Name=phuS` noted in the same
explanation. The name is `ECO:0000313`, an unchecked submitter import, so it is not usable as
support here in any case.

## The heme-binding IMP cites a paper that does not measure binding

`GO:0020037` heme binding is annotated **IMP** from PMID:10658665. That paper is about the right
organism and the right operon, but what it reports for *phuS* is a growth phenotype:
[PMID:10658665 "Mutant strains with deletions in phuR and phuSTUV showed greatly reduced growth
with either haem or haemoglobin as the only iron source"]. A heme-utilisation growth defect in a
`phuSTUV` multi-gene deletion supports a role in heme acquisition; it does not demonstrate that
this protein binds heme, and the deletion is not even *phuS*-specific.

The claim is nonetheless correct, and the direct evidence exists:

- **Resonance Raman plus site-directed mutagenesis** identified the ligands
  [PMID:18020455 "This combined approach has identified a site in monomeric PhuS having alternate
  His ligands at positions 209 and 212."], both of which are present in this sequence.
- **Holo- versus apo-protein behaviour** shows the binding is functional rather than incidental
  [PMID:22451925 "replacement of His-212 by Ala disrupts the interaction of holo-PhuS with HemO"].

So the row is accepted on the strength of those papers, which are added to the references, and the
reference problem is recorded as a `CHECK` query rather than acted on: the cached entry for
PMID:10658665 is abstract-only, so the full text could contain binding work the abstract does not
mention.

## The iron-transport row is a parent, not an error

`GO:0006826` iron ion transport looked at first like an over-annotation — PhuS is cytoplasmic, it
traffics a cofactor rather than pumping an ion, and the degradation is HemO's. Checking the
ontology instead of trusting that reading: **`GO:0015886` heme transport descends from
`GO:0006826`**, through `GO:1901678` iron coordination entity transport. GO already treats heme
transport as a kind of iron ion transport, so the row is true and merely general, and the fix is an
ordinary refinement rather than a removal.

The row's own evidence supports the deeper term: its supporting signatures are `IPR053733`
Heme_Transport_Util_sf and `IPR007845` HemS/ChuX_dom, which name heme transport and utilisation
specifically, not metal-ion transport in general.

## What is left unannotated

PhuS's second documented role — sensing and buffering heme flux, acting as what one paper calls a
"control valve" on extracellular heme uptake — is not proposed as an annotation here. The evidence
is a set of indirect phenotypes (premature pyocyanin production, transcriptional responses to iron
deprivation) and the authors themselves hedge it as "directly or indirectly". Recorded as a
knowledge gap and a suggested experiment instead.
