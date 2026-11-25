# aroE (P15770) – Escherichia coli K-12 shikimate dehydrogenase (NADP+)

## Provenance of these notes

Provider deep research (`just deep-research`) was unavailable for this review (no provider
key in the session), so no `-deep-research-*.md` file exists. These notes are compiled by
hand from the cached publications in `publications/`, the UniProt record
(`aroE-uniprot.txt`) and the PANTHER family review
(`interpro/panther/PTHR21089/PTHR21089-review.yaml`). Literature checked: PMID:3883995,
PMID:12637497, PMID:5326114, PMID:12363343, PMID:15690043, PMID:18304323, PMID:12837789
(H. influenzae AroE, comparative), PMID:25524738 (family review), PMID:15735308 (HI0607),
PMID:23142411 (RifI2). Most E. coli primary papers are cached abstract-only.

## Activity

- Purified E. coli enzyme is a monomeric NADP-linked dehydrogenase
  [PMID:3883995 "E. coli shikimate dehydrogenase is therefore a monomeric NADP-linked dehydrogenase."].
- Structure of AroE with bound cofactor at 1.5 A; E. coli has two paralogs, NADP-specific
  AroE and YdiB (dual quinate/shikimate, NAD or NADP)
  [PMID:12637497 "Escherichia coli expresses two shikimate dehydrogenase paralogs, the NADP-specific AroE and a putative enzyme YdiB."]
  [PMID:12637497 "Structures of AroE and YdiB with bound cofactors were determined at 1.5 and 2.5 A resolution, respectively."]
  [PMID:12637497 "Comparison of their dinucleotide-binding domains reveals the molecular basis for cofactor specificity."]
- UniProt curated function (ECO:0000269 to PMID:12637497 and PMID:3883995): reversible NADPH-linked
  reduction of 3-dehydroshikimate to shikimate; no activity with NAD. Km 56 uM NADP, 65 uM shikimate.
- Reaction is step 4 of the 7-step shikimate pathway (chorismate biosynthesis)
  [PMID:12637497 "Shikimate dehydrogenase catalyzes the fourth step of the shikimate pathway, the essential route for the biosynthesis of aromatic compounds in plants and microorganisms."].
- Family context: AroE is the archetype of a mechanistically conserved family with several
  functional classes [PMID:25524738 "SDH is the archetypal member of a large protein family, which contains at least four additional functional classes with diverse metabolic roles."].
  YdiB is the catabolic quinate/shikimate paralog; AroE is the biosynthetic enzyme
  [PMID:23142411 "The two most widespread members of the family, AroE and YdiB, function in amino acid biosynthesis and quinate catabolism, respectively."].
- Orthologous H. influenzae AroE structure: two domains, Rossmann-fold NADPH-binding domain
  [PMID:12837789 "The molecule contains two domains, a catalytic domain with a novel open twisted alpha/beta motif and an NADPH binding domain with a typical Rossmann fold."].

## In vivo role

- Classic mutant mapping identified structural genes of the common (chorismate) pathway, aroE among them
  [PMID:5326114 "Structural genes for five of the enzymes of the common pathway leading to chorismate and for the two enzymes converting chorismate to phenylpyruvate and p-hydroxyphenylpyruvate, respectively, were identified."].
- aroE- strains accumulate the substrate 3-dehydroshikimate, i.e. the pathway is blocked at this step in vivo
  [PMID:12363343 "3-dehydroshikimate (DHS, aroE(-))- and shikimate 3-phosphate (S3P, aroA(-))-producing E. coli strains"].
- YdiB cannot substitute physiologically: it is the catabolic quinate/shikimate enzyme, so AroE is
  the biosynthetic shikimate dehydrogenase of E. coli.

## Location

- Detected in the soluble cytosolic fraction in a quantitative cytosol proteome of E. coli MC4100
  [PMID:18304323 "The decision to only investigate the cytosol of E. coli, rather than a whole cell lysate, was a direct consequence of our intention to provide reliable concentration estimates of all identified proteins"].
  Soluble, no signal peptide or TM segment in the 272-residue sequence.

## Interactions

- High-throughput TAP-MS (Butland et al. 2005) reports co-purification with YedE (P31064), an
  inner-membrane protein of unknown function. No functional consequence for AroE is known; the
  bare protein-binding row is uninformative.

## Curation conclusions (summary)

- Core: shikimate 3-dehydrogenase (NADP+) activity (GO:0004764), in chorismate biosynthetic
  process (GO:0009423), cytosol.
- `nucleotide binding` (IDA, structure with NADP) is correct but general; refine to NADP binding.
- `aromatic amino acid biosynthetic process` is not an ancestor of chorismate biosynthesis in GO;
  AroE contributes to it only through chorismate, so keep it as non-core.
