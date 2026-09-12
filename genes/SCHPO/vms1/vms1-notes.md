# S. pombe vms1 (SPCC1827.04 / O74977) — review notes

Trigger: [geneontology/go-annotation#6520](https://github.com/geneontology/go-annotation/issues/6520)
— "PAINT issue: GO:0036503 ERAD pathway IBA with S000002456, PTN000411325". A PomBase
curator flagged the ERAD IBA on fission-yeast `vms1` as resting on old papers and fitting
poorly with the protein's mechanism (a tRNA-cleaving enzyme), and proposed that
`rescue of stalled cytosolic ribosome` would be the better propagation.

> No deep-research file could be generated for this gene: `just deep-research-perplexity
> SCHPO O74977` fails in this environment because no provider API key is configured
> (`No research providers available`). These notes are hand-assembled from PubMed,
> UniProt, PomBase and the cached publications instead. Per repo policy they are **not**
> named `-deep-research-<provider>.md`.

## 1. What is annotated today

From `vms1-goa.tsv` (12 rows). Aspect summary:

- **BP**: exactly one annotation — `GO:0036503 ERAD pathway`, IBA, GO_REF:0000033,
  `WITH/FROM = PANTHER:PTN000411325|SGD:S000002456`.
- **MF**: `GO:0003674 molecular_function`, **ND** (GO_REF:0000015) — PomBase explicitly
  records "no data" for molecular function.
- **CC**: cytoplasm (EXP PMID:16823372, plus IEA), cytosol (HDA PMID:16823372),
  mitochondrion (ISS from UniProtKB:Q04311, plus IEA), ER membrane (ISS from Q04311,
  ISO from SGD:S000002456, plus IEA), `GO:0032473 cytoplasmic side of mitochondrial outer
  membrane` (IC from `GO:0036266`), `GO:0036266 Cdc48p-Npl4p-Vms1p AAA ATPase complex`
  (ISO from SGD:S000002456).

PomBase's own gene page confirms the same picture: `characterisation_status: biological
role inferred`, one BP annotation (IBA), five CC annotations, and no MF annotation
(queried via `https://www.pombase.org/api/v1/dataset/latest/data/gene/SPCC1827.04`).
Every fission-yeast phenotype record is from a large-scale screen (PMID:37787768,
PMID:28410370, PMID:32101745, PMID:34250083, PMID:25452419, PMID:23697806,
PMID:20473289); none is a targeted study of vms1 function.

**So: there is no fission-yeast-specific functional data for this gene at all.** The
review is necessarily about whether the inherited/ortholog-transferred annotations are
the right ones.

## 2. The PAINT node itself

The cached PAINT export for the family is a single line
(`interpro/panther/PTHR16036/PTHR16036-paint.tsv`):

```
family    node          go_id       aspect evidence negated seeds            taxon        date
PTHR16036 PTN000411325  GO:0036503  P      IBD      false   SGD:S000002456   taxon:2759   20240206
```

Two things follow:

1. The IBD is placed at **taxon:2759 (Eukaryota)** — the root of PTHR16036 — so the ERAD
   claim is projected to every eukaryotic member of the family, including S. pombe vms1
   and human ANKZF1.
2. It is the family's **only** PAINT annotation. The activity that the family is actually
   named for and best characterised by — polypeptidyl-tRNA cleavage during
   ribosome-associated quality control (RQC) — is **not propagated at all**.

A short `WITH/FROM` list is not itself an objection to an IBA (see `projects/IBA_REVIEW.md`),
and the seed annotation is a real experimental one. The objection here is about **node
placement and term choice**: an accessory, budding-yeast-specific role has been placed at
the eukaryotic root while the conserved, mechanistically defined role is missing.

## 3. What the S. cerevisiae ERAD seed actually shows

SGD:S000002456 (VMS1) is annotated to ERAD on the basis of Tran, Tomsic & Brodsky 2011:

- [PMID:21148305 "A Cdc48p-associated factor modulates endoplasmic reticulum-associated
  degradation, cell stress, and ubiquitinated protein homeostasis", "Ydr049p, also known
  as Vms1p, which binds Cdc48p at both the ER membrane and in the cytosol under
  non-stressed conditions."]
- [PMID:21148305 "Loss of YDR049 modestly slows the degradation of the cystic fibrosis
  transmembrane conductance regulator but does not impede substrate ubiquitination"]
- [PMID:21148305 "Ydr049p acts at a postubiquitination step in the ERAD pathway."]
- [PMID:21148305 "Ydr049p acts in parallel with Cdc48p partners to modulate ERAD and
  other cellular activities."]

This is a genuine but **modest and modulatory** effect ("modestly slows"), reported in 2010
before the family's catalytic function was known, and framed by the authors themselves as
acting *in parallel with* the canonical Cdc48 ERAD cofactors (Ufd1–Npl4, Ubx/Shp1). It is
budding-yeast biochemistry on budding-yeast ERAD substrates (CFTR, CPY*).

## 4. What the family's conserved function is

The Vms1/ANKZF1 family (VLRF1 clade of eRF1 homologs) rescues stalled ribosomes:

- [PMID:29632312 "Vms1 is the founding member of a clade of eRF1 homologs that we
  designate the Vms1-like RF1 clade (VLRF1)."]
- [PMID:29632312 "Vms1 activity is dependent on a conserved catalytic glutamine."]
- [PMID:31011209 "ANKZF1 and Vms1p sever polypeptidyl-tRNAs on RQC complexes by precisely
  cleaving off the terminal 3'CCA nucleotides universal to all tRNAs"] — note this paper
  corrects the earlier "peptidyl-tRNA hydrolase" description: the enzyme is a **tRNA
  endonuclease**, cutting the tRNA, not the peptidyl-tRNA ester bond.
- [PMID:31011209 "ANKZF1 liberates peptidyl-tRNAs from stalled ribosomes such that the
  tRNA is checked in an obligate way for integrity before reentry into the translation
  cycle."]
- [PMID:31189955 "Vms1 catalyses cleavage and release of the peptidyl-tRNA before or after
  addition of CAT tails"] and [PMID:31189955 "In doing so, Vms1 counteracts CAT-tailing of
  nuclear-encoded mitochondrial proteins that otherwise drive aggregation and compromise
  mitochondrial and cellular homeostasis"].
- [PMID:29107329 "The cytosolic protein Vms1, together with the E3 ligase Ltn1, protects
  against the mitochondrial toxicity of these proteins and maintains cell viability under
  respiratory conditions."]

Human ANKZF1 carries the corresponding experimental annotations in GOA — `GO:0072344
rescue of stalled cytosolic ribosome` (IDA ×4), `GO:0006515 protein quality control for
misfolded or incompletely synthesized proteins` (IDA ×4), `GO:0004521 RNA endonuclease
activity` and `GO:0140101 catalytic activity, acting on a tRNA` (IDA) — and *also* carries
the same PTN000411325 ERAD IBA. This repo's existing human review
(`genes/human/ANKZF1/ANKZF1-ai-review.yaml`) already actions that IBA as **REMOVE**, on the
grounds that RQC and ERAD are distinct pathways. The present review reaches a consistent
conclusion for the fission-yeast ortholog.

## 5. The third role: mitochondria (MAD)

S. cerevisiae Vms1 also translocates to mitochondria under stress:

- [PMID:21070972 "Vms1 stably associates with both Cdc48 and its cofactor Npl4, which have
  well defined roles in the degradation of endoplasmic reticulum (ER) proteins by the
  proteasome."]
- [PMID:21070972 "Vms1 plays a conserved role in recruiting the ubiquitin/ proteasome
  system for stress-responsive mitochondrial protein degradation."]

This is the basis of `GO:0036266 Cdc48p-Npl4p-Vms1p AAA ATPase complex` and the IC
annotation to the cytoplasmic side of the mitochondrial outer membrane. It is an ISO
transfer to fission yeast with no S. pombe evidence, so it is retained but not treated as
core.

## 6. Does fission-yeast vms1 retain the catalytic residue?

Yes. Own analysis, `vms1-bioinformatics/RESULTS.md`: aligning full-length UniProt
sequences, human ANKZF1 Q246 (whose Q246L mutation abolishes polypeptidyl-tRNA cleavage)
projects onto *S. cerevisiae* Q295 and *S. pombe* Q249, reproducing both UniProt
`ACT_SITE` calls. The fission-yeast context `RKQGGSQ` is identical to the budding-yeast
one. So vms1 is not a degenerate pseudoenzyme, and an ISS-grade tRNA-nuclease MF is
defensible where the current `ND` says nothing at all.

## 7. Review decisions taken

- `GO:0036503 ERAD pathway` (IBA) → **MODIFY**, proposed replacement `GO:0072344 rescue of
  stalled cytosolic ribosome`. This is exactly what the upstream issue proposes. MODIFY
  rather than REMOVE because the fission-yeast gene would otherwise be left with **zero**
  BP annotations, and the family-level inheritance being asserted is real — only the term
  is wrong. (Human ANKZF1 differs: there the RQC terms already exist as IDA, so a plain
  REMOVE loses nothing.)
- `GO:0003674` ND → **MODIFY** toward `GO:0004549 tRNA-specific ribonuclease activity`,
  flagged as ISS-grade. `GO:0004549` is what this repo's ANKZF1 review already proposes for
  the human ortholog, so the two stay consistent.
- `GO:0006515 protein quality control for misfolded or incompletely synthesized proteins`
  added as **NEW** at ISS strength, covering the fate of the released nascent chain (the
  proposed `GO:0072344` covers freeing the ribosome). Human ANKZF1 carries this term with
  four IDA annotations. Flagged in the review as optional — curators may judge `GO:0072344`
  alone sufficient for a gene with no fission-yeast functional data.
- CC annotations: the S. pombe-observed cytoplasm/cytosol are ACCEPTed. The ER-membrane and
  mitochondrial CCs are ortholog transfers with no fission-yeast support and are kept as
  non-core.
- Nothing here is asserted as fission-yeast experimental fact; every functional claim is
  labelled as ortholog/sequence inference.

## 8. Open questions for curators

- Should the PTHR16036 IBD at PTN000411325 be re-placed rather than re-termed? The cleanest
  fix upstream is probably to add an RQC IBD (`GO:0072344`) at the eukaryotic root — where
  both human and budding-yeast experimental evidence sits — and to restrict or drop the
  ERAD IBD, since its only seed is a modulatory budding-yeast result.
- Is `GO:0004549 tRNA-specific ribonuclease activity` or a new, more precise term
  ("tRNA 3'-CCA endonuclease") the right MF for this family? GO currently has no term for
  the specific 3'-CCA-removing reaction.
