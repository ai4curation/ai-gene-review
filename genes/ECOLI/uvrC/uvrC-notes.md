# uvrC (Escherichia coli K-12, P0A8G0, b1913) notes

Reviewer: Claude (AI-assisted). Provider deep research was not available for this gene
(no provider API access in this campaign), so these notes are built from the cached
publications in `publications/` and the UniProt record. No `-deep-research-*.md` file exists.

## Function

- UvrC carries both catalytic sites of the UvrABC dual incision. 3' incision is made by the
  N-terminal GIY-YIG region: "substitution R42A abolishes 3' incision, whereas formation of
  the UvrBC-DNA complex and the 5' incision reaction are unaffected" [PMID:10671556].
- 5' incision is made by the C-terminal RNase H-like region: "Enzyme reconstituted with these
  mutant proteins carried out normal 3' incision but was completely defective in 5' incision
  activity" [PMID:1387639]; the mutants (H538F, D399A, D438A, D466A) "conferred extreme UV
  sensitivity" [PMID:1387639].
- Incision geometry: "(A)BC excinuclease of Escherichia coli removes damaged nucleotides from
  DNA by hydrolyzing the 8th phosphodiester bond 5' and the 15th phosphodiester bond 3' to the
  modified base" [PMID:1387639].
- UvrC acts in a complex with UvrB on damaged DNA: "The two incision reactions take place in a
  complex of damaged DNA with UvrB and UvrC" [PMID:10671556]; "After association with the UvrC
  protein, one of the UvrB monomers is released" [PMID:12145219].
- Review: "UvrC is a dual endonuclease recruited to the UvrB•DNA pre-incision complex to
  introduce incisions on either side of the lesion" [PMID:33477956]; the UVR element between
  the two nuclease domains "is required for the interaction with UvrB" and the C-terminal
  (HhH)2 module is the DNA-binding domain [PMID:33477956].

## Regulation

- uvrC is not part of the inducible SOS response in E. coli, unlike uvrA and uvrB:
  "We show that transcription from both promoters on the chromosome is not inducible by UV
  damage" [PMID:3295776]. This is why the UniRule-derived SOS response row is treated as an
  over-annotation in the review.
- The UvrC paralog Cho (ydjQ, P76213) is SOS-inducible and makes an alternative 3' incision
  [PMID:11818552]; it is the other PTHR30562 subfamily (SF10).

## Phenotype

- Keio-collection radiation screen used for the IMP response-to-radiation row [PMID:27718375];
  the abstract does not list uvrC among the 33 "uncommon" genes, consistent with uvrC being one
  of the common, previously known radiation-sensitivity genes. Full text not cached.

## Decisions

- Core MF recorded as GO:0009381 excinuclease ABC activity (is_a GO:0004520 DNA endonuclease
  activity, the module's term). Both incision active sites lie in UvrC, so `enables` is
  appropriate for the catalytic subunit.
- DNA repair and DNA damage response rows refined to nucleotide-excision repair.
