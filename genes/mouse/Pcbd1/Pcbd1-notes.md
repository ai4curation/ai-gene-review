# Pcbd1 (mouse, P61458) — curation notes

## Why this review exists

Triggered by **geneontology/go-annotation#6591**, which asks:

> Would it be possible to replace the current MF GO term with
> "4-alpha-hydroxytetrahydrobiopterin dehydratase activity for MGI:1919812
> (Pcbd2) and MGI:94873 (Pcbd1). In the paper, the 2 enzymes complements
> P. aeruginosa PhhB which is a Pterin-4-alpha-carbinolamine dehydratase.

The "current MF GO term" is `GO:0004505 phenylalanine 4-monooxygenase activity`,
annotated IDA to both mouse paralogs from PMID:15182178. The requested
replacement is `GO:0008124`.

No deep-research file could be generated for this gene: `just deep-research mouse
Pcbd1` fails in this environment because no provider API key is configured
(OPENAI/EDISON/ASTA/PERPLEXITY all unset). These notes and the cached
publications are the evidence base. Companion review: `genes/mouse/Pcbd2/`.

## The term confusion, stated precisely

Both GO terms are real and both name a step of the same cycle, which is exactly
why they get swapped. Verified via OLS:

- `GO:0004505 phenylalanine 4-monooxygenase activity` — "Catalysis of the
  reaction: L-phenylalanine + tetrahydrobiopterin + O2 = L-tyrosine +
  4-alpha-hydroxytetrahydrobiopterin." Synonyms include *phenylalanine
  hydroxylase activity*, *PAH activity*. This is **Pah**, not Pcbd1.
- `GO:0008124 4-alpha-hydroxytetrahydrobiopterin dehydratase activity` —
  "Catalysis of the reaction: (6R)-6-(L-erythro-1,2-dihydroxypropyl)-5,6,7,8-
  tetrahydro-4a-hydroxypterin = (6R)-6-(L-erythro-1,2-dihydroxypropyl)-7,8-
  dihydro-6H-pterin + H2O." Synonyms include **"pterin-4-alpha-carbinolamine
  dehydratase activity"** — verbatim the activity the issue names.

The two reactions are consecutive: PAH consumes BH4 and *produces*
4a-hydroxy-BH4; PCD/DCoH consumes 4a-hydroxy-BH4 and dehydrates it to
quinonoid-BH2, which QDPR then reduces back to BH4. Pcbd1 therefore sits one
step downstream of the activity it is annotated with.

The likely origin of the error is the protein's third name. Pcbd1 is also
"phenylalanine hydroxylase-**stimulating** protein" (PHS) — UniProt's
`AltName: Full=Phenylalanine hydroxylase-stimulating protein`. It stimulates PAH
by accelerating cofactor turnover; it does not hydroxylate phenylalanine. A
historical name describing a *stimulatory* effect on another enzyme was read as
naming that enzyme's own activity.

UniProt agrees with the issue, not with the GOA row. The mouse entry carries
`EC=4.2.1.96` (a lyase) and the keyword `Lyase`, and its sole CATALYTIC ACTIVITY
block (`file:mouse/Pcbd1/Pcbd1-uniprot.txt`) is the RHEA:11920 dehydration:

```
Reaction=(4aS,6R)-4a-hydroxy-L-erythro-5,6,7,8-tetrahydrobiopterin =
  (6R)-L-erythro-6,7-dihydrobiopterin + H2O; Xref=Rhea:RHEA:11920, ...
  EC=4.2.1.96;
```

A monooxygenase (EC 1.14.16.1) annotation is incompatible with that EC class.

## Blast radius of the one bad IDA

The `GO:0004505` IDA is not isolated; it has seeded three further annotations,
and fixing the IDA should fix all of them:

1. `GO:0006571 L-tyrosine biosynthetic process` (IEA, GO_REF:0000108) — created
   by inter-ontology logical inference whose stated source is literally
   `GO:0004505` in the WITH field. Pcbd1 does not make tyrosine; PAH does.
2. `GO:0004505` on **human** PCBD1 (IEA, GO_REF:0000107) — an Ensembl Compara
   transfer with `UniProtKB:P61458|ensembl:ENSMUSP00000020298` in WITH, i.e.
   propagated *from this mouse row*. The existing human review
   (`genes/human/PCBD1/PCBD1-ai-review.yaml`) already flags it for removal and
   records GO_REF:0000107 as `MISCITED` for exactly this reason. Mouse is the
   root cause.
3. `GO:0006571` on human PCBD1, same inter-ontology inference from the
   transferred MF.

There is also an independent `GO:0004505` IEA from `ARBA:ARBA00029278`
(GO_REF:0000117) on both mouse paralogs. That one is not downstream of the MGI
IDA, so it needs a separate ARBA fix — worth noting because correcting the IDA
alone will not clear the term from the gene product.

## What PMID:15182178 actually supports

Cached abstract-only (`full_text_available: false`), so the PhhB complementation
assay the issue describes is in the full text that the MGI curator read and I
cannot see. The abstract nonetheless states the enzymology directly, for DCoH2
and by comparison for DCoH:

> Like DCoH, DCoH2 forms a tetramer, displays pterin-4alpha-carbinolamine
> dehydratase activity, and binds HNF1alpha in vivo and in vitro.

"Like DCoH … displays pterin-4alpha-carbinolamine dehydratase activity" is a
statement about both proteins, and `pterin-4alpha-carbinolamine dehydratase
activity` is an exact synonym of GO:0008124. The paper also supports the
HNF1A interaction and the tetramer, which are the other MGI annotations from it.

So `MODIFY GO:0004505 → GO:0008124` keeps the evidence code (IDA) and the
reference, and only corrects the term. This is the minimal, curator-requested
change — not a reinterpretation of the experiment.

## The second, unrelated function: DCoH

Pcbd1 is a genuine moonlighting protein. As DCoH it binds the HNF1A homeodomain
transcription factor and stabilises its dimer
[PMID:1763325 "A dimerization cofactor of HNF-1 alpha (DCoH) was identified that displayed a restricted tissue distribution and did not bind to DNA, but, rather, selectively stabilized HNF-1 alpha dimers"],
and the resulting tetramer is more transcriptionally active without any change in
DNA binding
[PMID:1763325 "did not change the DNA binding characteristics of HNF-1 alpha, but enhanced its transcriptional activity"].
Note the specificity control in the same paper: "DCoH did not confer
transcriptional activation to the GAL4 DNA binding domain" — it is an
HNF1-directed cofactor, not a generic activation domain.

Two curation consequences:

- The `GO:0005515 protein binding` IPI with `PR:P22361` (mouse Hnf1a) is
  uninformative under this repo's guidelines. The informative term is
  `GO:0140297 DNA-binding transcription factor binding` (OLS-verified: "Binding
  to a DNA-binding transcription factor…"), which is what the experiment shows.
- The `GO:0005515` IPI with `PR:Q9CZL5` (Pcbd2) is the one row I could not settle.
  The candidate replacement is `GO:0046982 protein heterodimerization activity`
  ("Binding to a nonidentical protein to form a heterodimer"), because Pcbd2 is a
  paralog and so `GO:0042802 identical protein binding` cannot apply. But the
  cached abstract only reports DCoH2 disproportionating and forming a 2:2 complex
  *with HNF1*; it says nothing about a mixed DCoH/DCoH2 species. A discrete
  heterodimer, a mixed tetramer, and subunit exchange between separately assembled
  tetramers all map to different terms, so this is `UNDECIDED` pending full text —
  not doubt about the interaction, which the MGI curator read and recorded.
- MGI records `GO:0003713` and `GO:0045893` from PMID:1763325 as **ISO** with
  `UniProtKB:P61459` (rat Pcbd1) as the source. But UniProt cites this very paper
  on the *mouse* entry for "NUCLEOTIDE SEQUENCE [MRNA], AND PARTIAL PROTEIN
  SEQUENCE. STRAIN=C57BL/6 X CBA; TISSUE=Liver" — Mendel et al. cloned mouse
  DCoH from mouse liver. The function may well be directly, not orthologously,
  demonstrated in mouse. I am not changing the evidence code: only the full text
  shows which species the functional assays used, and the curator read it. Raised
  as a question instead.

## Localization

Cytosol + nucleus, with the nuclear pool tied to HNF1 recruitment. Mouse has no
direct localization paper in the cached set; every CC row is ISO/ISS/IBA/IEA from
human or rat. They are mutually consistent and consistent with the two
functions (dehydratase in the cytosol where the aromatic amino acid hydroxylases
generate 4a-hydroxy-BH4; coactivator in the nucleus), so they are accepted
rather than second-guessed. The human ortholog has the direct evidence
[PMID:24204001 "Because Pcbd1 was present in the cytosol of renal cells, we hypothesized that the relative abundance of PCBD1 and HNF1B in the kidney may favor the cytosolic localization"].

Redundancy is heavy — nucleus ×6, cytoplasm ×4, cytosol ×3, nucleoplasm ×3,
GO:0008124 ×4 (+1 after the MODIFY) — across IEA/ISO/ISS/IBA from mouse-rat,
mouse-human, Compara and SubCell pipelines. None of it is wrong; it is pipeline
duplication, and I have accepted rather than pruned, flagging the parent/child
redundancy (cytoplasm vs cytosol, nucleus vs nucleoplasm) in the reasons.

## The IBA node

`PANTHER:PTN002650414` carries the IBAs. From the cached PAINT table
(`interpro/panther/PTHR12599/PTHR12599-paint.tsv`) the node sits at
**taxon:117571 (Euteleostomi)** with three non-negated IBDs: `GO:0005654` and
`GO:0005829` seeded by `UniProtKB:P61457` (human PCBD1), and `GO:0008124` seeded
by `RGD:3263` (rat Pcbd1). Mouse Pcbd1 is inside that clade, so the IBAs follow
properly. Single-MOD donor lists are not a defect.

Worth noting: mouse **Pcbd2** does *not* receive these IBAs despite also being a
Euteleostomi-descended PTHR12599 member, which implies the node is placed below
the Pcbd1/Pcbd2 duplication rather than at the vertebrate root of the whole
family. That is a PAINT placement question, not a Pcbd1 problem.

## Summary of actions

| Term | Evidence | Action |
|---|---|---|
| GO:0004505 phenylalanine 4-monooxygenase activity | IDA PMID:15182178 | **MODIFY → GO:0008124** (the issue's ask) |
| GO:0004505 | IEA ARBA:ARBA00029278 | **REMOVE** (independent ARBA fix needed) |
| GO:0006571 L-tyrosine biosynthetic process | IEA GO_REF:0000108 | **REMOVE** (inferred from the wrong MF) |
| GO:0005515 protein binding (w/ Hnf1a) | IPI PMID:15182178 | **MODIFY → GO:0140297** |
| GO:0005515 protein binding (w/ Pcbd2) | IPI PMID:15182178 | **UNDECIDED** (see below) |
| GO:0008124 ×4 | IBA / IEA / ISO / ISS | ACCEPT (core) |
| GO:0003713, GO:0045893 | ISO PMID:1763325 | ACCEPT (core, DCoH) |
| GO:0042802 identical protein binding ×3 | IEA / IPI / ISO | KEEP_AS_NON_CORE |
| nucleus / nucleoplasm / cytoplasm / cytosol | various | ACCEPT |
| GO:0006729 tetrahydrobiopterin biosynthetic process | IEA InterPro | ACCEPT (regeneration, not de novo) |
