# MEA1 (Q16626, HGNC:6986) review notes

## Why this gene was selected

MEA1 ("male-enhanced antigen 1") has been a name-only gene since 1989. Until 2026 its entire
GOA molecular-function record was `GO:0005515 protein binding`, and its only biological-process
annotations traced to a single expression-pattern paper from the pre-GO era. HGNC has now added
PMID:41559075, which gives the protein a concrete, mechanistically resolved job that has nothing
to do with its name.

## Reference verification

PMID:41559075 verified against PubMed: Wan C, Wu J, Ouyang Y, Puscher H, Tian Y, Li S, Yin Q,
Shen J. "Regulation of AP1 adaptor assembly by the bi-handed chaperone MEA1." Nat Commun 2026
Jan 20;17(1). doi:10.1038/s41467-026-68662-3. PMC12923701. Full text cached.

PMID:2813404 verified: Lau YF, Chan KM, Sparkes R. "Male-enhanced antigen gene is
phylogenetically conserved and expressed at late stages of spermatogenesis." Proc Natl Acad Sci
USA 1989 Nov;86(21):8462-6. Abstract only in cache (`full_text_available: false`).

## What the 2026 paper establishes

MEA1 is an AP-1 assembly chaperone, not a testis protein:
[PMID:41559075 "Here, we identified Male-Enhanced Antigen 1 (MEA1), a previously uncharacterized
protein, as a critical AP1 regulator."]
[PMID:41559075 "Mechanistically, MEA1 acts as a bi-handed chaperone, simultaneously engaging and
stabilizing the μ1 and β1 subunits of AP1."]

Direct binding and stabilization, reconstituted in E. coli (a background with no endogenous AP1
or MEA1, so this is not an indirect cellular effect):
[PMID:41559075 "These results demonstrate that MEA1 directly binds to μ1 and β1, and stabilizes
them in a soluble state."]

Two independent hands, mapped to separate domains:
[PMID:41559075 "Pull-down assays showed that MEA1-NTD bound and stabilized μ1 to a similar extent
as FL MEA1, whereas MEA1-CTD neither bound nor stabilized μ1"]
[PMID:41559075 "Conversely, MEA1-CTD, but not NTD, bound and stabilized β1"]

Loss of function:
[PMID:41559075 "Interestingly, immunoblotting revealed that all four AP1 subunits—γ, β1, μ1, and
σ1—were strongly reduced in MEA1 KO cells compared to WT controls"]
[PMID:41559075 "MEA1 loss resulted in depletion of AP1 subunits, impaired trafficking of
AP1-dependent cargoes, and defective termination of STING signaling."]

Cytosolic, and released before the adaptor reaches the membrane:
[PMID:41559075 "Confocal imaging revealed that both MEA1 and AAGAB displayed diffuse cytosolic
localization"]
[PMID:41559075 "cell fractionation showed that the transferrin receptor (TfR) and AP1 γ subunit
were exclusively in the membrane fraction, whereas MEA1 and AAGAB were confined to the soluble
cytosolic fraction along with glyceraldehyde 3-phosphate dehydrogenase (GAPDH), a cytosolic
marker"]
[PMID:41559075 "In agreement with this, structural modeling showed that MEA1 occupies the
γ-binding site on β1"]

Specificity:
[PMID:41559075 "suggesting that MEA1 plays a limited role in AP2 regulation."]
[PMID:41559075 "Expression levels of AP3, AP4, and AP5 remained unchanged"]
[PMID:41559075 "These results demonstrate that MEA1 is critical for maintaining the integrity of
the AP1 adaptor complex, and suggest that its function is primarily dedicated to AP1, without
broadly regulating adaptor protein complexes."]

## How MEA1 differs from AAGAB (cross-check against genes/human/AAGAB/AAGAB-ai-review.yaml)

The AAGAB review in this repository describes AAGAB as a cytosolic assembly chaperone for
AP-type adaptors that binds already-folded subunits, enforces an ordered assembly pathway,
protects intermediates from degradation, and is released before the tetramer is complete.
Everything in that general description applies equally to MEA1, and the two files should read
consistently on those points. The differences are specific and worth stating precisely:

| | AAGAB | MEA1 |
|---|---|---|
| Clients within AP-1 | γ and σ1 | μ1 and β1 |
| Adaptors served | AP-1, AP-2, AP-4; specifically not AP-3 | AP-1 primarily; limited role in AP-2; not AP-3/AP-4/AP-5 |
| Architecture | N-terminal type I pseudoGTPase domain (σ subunits) + C-terminal dimerization domain (γ/α); homodimer that monomerizes on client binding | Intrinsically disordered, ~20 kDa, no recognizable fold or sequence homology; NTD binds μ1, CTD binds β1 |
| Hand-off | For AP-2, passes the α:σ2 intermediate to CCDC32 | No hand-off partner; released by collision with the AAGAB-bound hemicomplex |
| Disease | PPKP1A (punctate palmoplantar keratoderma) | none reported |

Both are called "bi-handed" in the 2026 paper, meaning each grips two different subunits at once.
The mechanism the paper adds is that the two chaperones work on complementary halves and neither
hands off to the other:
[PMID:41559075 "The MEA1-stabilized μ1 and β1 collide with the γ and σ1 subunits stabilized by
Alpha- and Gamma-Adaptin Binding Protein (AAGAB), another bi-handed chaperone, leading to
formation of the tetrameric AP1 adaptor and release of both chaperones."]
[PMID:41559075 "MEA1 and AAGAB did not interact directly when tested using recombinant proteins"]
[PMID:41559075 "These findings support a dual-chaperone collision model, in which MEA1:μ1:β1 and
AAGAB:γ:σ1 collide without stably associating with each other, and both MEA1 and AAGAB are
released upon formation of the full AP1 tetramer"]

So AAGAB's mechanism as recorded in its review (sequential hand-off to a downstream chaperone,
for AP-2) and MEA1's (collision of two independently loaded hemicomplexes, for AP-1) are
genuinely different solutions, not two descriptions of one thing.

## The GO term problem, and why nothing new is proposed here

GO still has no molecular-function term for an assembly chaperone that binds free, folded
subunits of a complex it will not join. The AAGAB review already worked this through and filed
two `proposed_new_terms`:

1. **AP-type membrane coat adaptor complex subunit binding** - binding to a free, unassembled
   subunit of a heterotetrameric AP-type adaptor, as distinct from binding the assembled complex.
2. **protein complex assembly chaperone activity** - binding folded subunits to stabilise them
   and impose assembly order, without forming part of the finished complex.

Both cover MEA1 exactly (MEA1's clients are μ1/β1 rather than γ/σ1, which the first term's
wording already anticipates), so this review deliberately does **not** propose a third term. It
reuses the AAGAB proposals verbatim in substance, with MEA1 evidence attached, so the two files
argue for the same two terms rather than two overlapping sets.

In the meantime the nearest existing MF term is `GO:0035650 AP-1 adaptor complex binding`, and
it is used here as a flagged stand-in in exactly the way AAGAB's review uses `GO:0035612`. The
flag matters: GO defines GO:0035650 as binding to the assembled heterotetramer, and MEA1 is
released before the tetramer exists - structural modeling places MEA1 on the γ-binding site of
β1, so MEA1 and γ cannot both be bound. The stand-in names the right complex at the wrong
altitude.

## The spermatogenesis annotations

`GO:0007283 spermatogenesis` (IEA from InterPro IPR009685, and TAS from PMID:2813404) and
`GO:0008584 male gonad development` (TAS from PMID:2813404) all trace to the same 1989 paper,
whose own conclusion is explicitly a hypothesis from an expression pattern:
[PMID:2813404 "The genetic conservation and testis-specific expression of the MEA gene support
the hypothesis that it plays an important role in mammalian spermatogenesis and/or testis
development."]
The same abstract records that the transcript is present in most tissues:
[PMID:2813404 "Although the Mea gene was transcribed as a 1-kilobase mRNA in most tissues, it
was expressed at the highest level in adult testis."]
and the 2026 paper is explicit that the testis association is a naming artefact:
[PMID:41559075 "Although initially cloned from a testis cDNA library (hence its name)38, MEA1 is
ubiquitously expressed across tissue types and is detected in all examined human cell lines39,40,
indicating a general cellular role."]

Action taken: `MARK_AS_OVER_ANNOTATED` for all three. No functional experiment has ever tested
MEA1 in spermatogenesis in any species, so these are annotations from enriched expression plus a
gene name. `REMOVE` would be defensible for the InterPro IEA in particular (the mapping exists
only because the family was named after the phenotype hypothesis), but nothing positively
excludes a testis role for an adaptor-assembly chaperone in a tissue with heavy membrane
trafficking, so the weaker action is the honest one. Note also that all three rows must share an
action under project rules.

## The interactome annotations were right all along

Three of the four `GO:0005515 protein binding` rows name partners that are now interpretable:
- PMID:16189514 and PMID:33961781 -> UniProtKB:P63010 = AP2B1, the β2 subunit of AP-2.
- PMID:32296183 and PMID:33961781 -> UniProtKB:Q9BXS5 = AP1M1, the μ1 subunit of AP-1.

So the binary interactome had MEA1-μ1 and MEA1-β2 on record years before anyone knew what they
meant, and the 2026 paper independently recovers both:
[PMID:41559075 "Besides μ1 and β1, the interactome of MEA1 also included the β2 and μ2 subunits
of AP2 (BioGRID)37, a central regulator of clathrin-mediated endocytosis18,43–47."]
They are still marked over-annotated, because bare `protein binding` conveys none of this; the
content is moved into the molecular-function and core-function entries.

## Open questions

- Is AP-1 assembly ordered or concurrent? MEA1 and AAGAB do not interact, so what determines the
  stoichiometry and timing of the two hemicomplexes, and is there a quality-control step that
  disposes of unpaired MEA1:μ1:β1?
- Does the limited AP-2 effect reflect genuine redundancy with AAGAB and CCDC32, or a distinct,
  weaker MEA1 activity on β2/μ2?
- MEA1 is intrinsically disordered with no fold. Does it fold on binding μ1 and β1, and can a
  single MEA1 molecule hold both at once in vivo, as the trimeric AlphaFold model implies?
- No human disease is yet linked to MEA1, although AAGAB truncations cause PPKP1A and AP-1
  subunit defects cause MEDNIK and related syndromes. Is MEA1 essential, or is there a viable
  hypomorphic range?
