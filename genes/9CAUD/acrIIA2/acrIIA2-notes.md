# acrIIA2 / LP101_024 (A0A059T5F6, Listeria phage LP-101) — curation notes

## Identity, and an important caveat about which protein was assayed

Unreviewed TrEMBL entry, 123 aa, `RecName: Full=Anti-CRISPR protein AcrIIA2
{ECO:0008006|Google:ProtNLM}` — i.e. **the name is a machine prediction (ProtNLM), not a
curator assertion**. `PE 4: Predicted`, no PDB, no GO annotations in GOA at all. The only
non-electronic support for the AcrIIA2 assignment is NCBIfam `NF033945 AcrIIA2_fam` and
CDD `cd22261 AcrIIA2`, both HMM family hits. Seeded taxon was wrong
(`NCBITaxon:10663`); UniProt gives `OX NCBI_TaxID=1458856` for Listeria phage LP-101, and
the review has been corrected to that.

**The published AcrIIA2 work was done on a different, closely related sequence.** Rauch et
al. name their reference sequence explicitly
[PMID:28041849 "AcrIIA2- (AEO04363.1), AcrIIA3- (CBY03209.1) and AcrIIA4- (AEO04689.1) homologous protein sequences were acquired by BLASTp searches"].
NCBI `efetch` of AEO04363.1 returns `gp29 [Listeria monocytogenes J0161]`, 123 aa:

```
MTLTRAQKKYAEAMHEFINMVDDFEESTPDFAKEVLHDSDYVVITKNEKYAVALCSLSTDECEYDTNLYL
DEKLVDYSTVDVNGVTYYINIVETNDIDDLEIATDEDEMKSGNQEIILKSELK
```

Pairwise comparison against A0A059T5F6 (same length, no gaps): **114/123 identical =
92.7%**, differing only at positions 3, 5, 8, 11, 39, 44, 56, 81, 112. All nine are
conservative or surface substitutions; none is in a position the structural paper
identifies as a Cas9 contact. So this is a genuine orthologue of the characterised
protein, encoded by a free Listeria phage rather than by a *L. monocytogenes* prophage.

**Consequence for evidence codes.** The functional claims for this accession are
transferred by sequence similarity, not demonstrated on it. Every annotation proposed here
therefore carries **ISS**, with `AEO04363.1` named as the source. The alternative — writing
IDA because the family is well characterised — would assert an experiment that was not
done on this sequence, and would be exactly the kind of accession-level slippage that
`modules/anti_crispr_suppression.yaml` records as an open gap for the AcrIII-1 exemplar.

## Mechanism: the module's DNA-mimicry assignment holds

The module (annoton `acriia2_dna_mimic`) places AcrIIA2 in the
`cas9_dna_mimicry_variant` as "the convergence case", i.e. a second, sequence-unrelated
Listeria inhibitor that attacks the same Cas9 surface as AcrIIA4. **The assignment is
correct, and the structural paper states it in almost those words.**

Liu et al. solved the AcrIIA2–SpyCas9–sgRNA complex at 3.3 Å
[PMID:30606466 "We show that AcrIIA2 binds SpyCas9 at a position similar to the target DNA binding region."],
identified the occluded residues
[PMID:30606466 "AcrIIA2 interacts with the protospacer adjacent motif (PAM) recognition residues of Cas9, preventing target double-stranded DNA (dsDNA) detection."],
and drew the mimicry conclusion together with the explicit statement that the binding
motif differs from AcrIIA4's
[PMID:30606466 "phage-encoded AcrIIA2 appears to act as a DNA mimic that blocks subsequent dsDNA binding by virtue of its highly acidic residues, disabling bacterial Cas9 by competing with target dsDNA binding with a binding motif distinct from AcrIIA4"].
That last clause is the whole point of the module's convergence claim: same enzyme, same
surface, same mimicry strategy, **different** binding motif and no sequence relationship.
Cached record is abstract-only, so these are abstract quotes and are marked as such.

AcrIIA2's guide dependence is also on record
[PMID:28448066 "Our data show that AcrIIA2 and AcrIIA4 interact with SpyCas9 in a sgRNA-dependent manner."],
as is the in vivo inhibition of both Lmo Cas9 and SpyCas9
[PMID:28448066 "Recently, two anti-CRISPR proteins (AcrIIA2 and AcrIIA4 from Listeria monocytogenes prophages) were identified, both of which inhibit Streptococcus pyogenes Cas9 (SpyCas9) and L. monocytogenes Cas9 activity in bacteria and human cells."],
[PMID:28041849 "these data demonstrate the utility of the AcrIIA2 and AcrIIA4 proteins to inhibit the function of an orthologous Cas9 in heterologous hosts"].

One mechanistic subtlety from the genetics is worth keeping: AcrIIA2 was more effective in
the cleavage assay than in the dCas9 binding assay, which the authors read as partial
inhibition of binding plus inhibition of cleavage
[PMID:28041849 "The enhanced efficacy of acrIIA2 in the cleavage-based Cas9 assay relative to the dCas9 based assay suggests that it may inhibit both binding and cleavage to some degree"].
Pure PAM-site occlusion predicts equal effects on binding and cleavage, so this is a hint
that AcrIIA2 may be doing something at the catalytic step as well. It is a single
qualitative observation in a heterologous system and is recorded as a knowledge gap rather
than annotated.

Breadth across orthologues is attributed to a conserved target surface
[PMID:28041849 "Using the orthologous Spy Cas9, it is clear that AcrIIA2 and AcrIIA4 have broad specificity, given that Lmo Cas9 and Spy Cas9 only share 53% sequence identity."].

## GOA state and the curation gap

GOA holds **zero** annotations for A0A059T5F6. Combined with an unreviewed entry whose
protein name is a ProtNLM prediction, this is a concrete instance of the second knowledge
gap recorded in `modules/anti_crispr_suppression.yaml` ("Most characterised Acr proteins
have no reviewed UniProt entry, and several carry uninformative names"). Here the name is
not uninformative but is machine-generated, which is arguably worse: it reads like a
curator assertion and is not one. The family HMM hits (NF033945, cd22261) do support the
assignment, and the 92.7% identity to the assayed protein supports it independently.

## Ontology gap

Same gap as AcrIIA4 and AcrF2: no GO molecular-function term for mimicry-based competitive
inhibition. The proposed term `nucleic acid mimicry-based competitive inhibitor activity`
is restated here with AcrIIA2-specific supporting text, since the three reviews should be
able to cite one proposal independently.
