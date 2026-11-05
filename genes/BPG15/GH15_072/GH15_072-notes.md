# GH15_072 (HolGH15, UniProt I6P9Q0) — curation notes

Staphylococcus phage GH15 ORF72, the phage's holin. Reviewed for the
[CACAO project](../../../projects/CACAO.md), batch 3, screen 3 (non-standard
GAF qualifiers).

**Deep research was unavailable for this gene.** No deep-research API key exists
in this container, so `just deep-research` was not run and no
`-deep-research-<provider>.md` file exists. The literature below was assembled
by hand from the cached publications, PubMed/Europe PMC queries and web search.

## Identity

- UniProt I6P9Q0, `SubName: Full=Holin {ECO:0000313|EMBL:AFF28544.1}`, 167 aa,
  `GN ORFNames=GH15_072`. No `GN Name=`, protein existence `PE 4: Predicted`.
- The sequencing paper is the GH15 genome announcement
  [PMID:22843868 "Complete Genome Sequence of Staphylococcus aureus Bacteriophage GH15."],
  EMBL JQ686190 / RefSeq YP_007002195.1.
- **Gene symbol.** The review stub was seeded `gene_symbol: I6P9Q0`, the bare
  accession. That is not the right symbol: GOA's own SYMBOL column for this row
  is `GH15_072` (its GENE NAME column carries the product name `Holin`), the
  UniProt ORF name is `GH15_072`, and the gene folder is `genes/BPG15/GH15_072/`.
  The corpus convention for phage ORFs with no assigned gene name is the ORF name
  (`JBD30_035`, `PHIKZ144`, `GH15_072`), not the accession. Set to `GH15_072`.
  The literature name for the protein is **HolGH15**
  [PMID:26873847 "The ORF72 gene (also designated HolGH15) derived from the genome of the Staphylococcus aureus phage GH15 was predicted to encode a membrane protein"];
  that is a protein name, not an HGNC-style gene symbol, so it belongs in the
  description rather than in `gene_symbol`.
- **Taxon naming quirk, not a defect.** NCBI taxid 760530 is named
  "Staphylococcus phage G15" (rank: isolate) and UniProt's `OS` line follows it,
  while the genome, the paper and the ORF prefix all say GH15. The EMBL
  cross-reference on this very entry (JQ686190) is the GH15 genome, so the entry
  is the GH15 protein under an NCBI name that drops the H. Recorded here only so
  that a future reader does not read it as a wrong-organism problem; no
  `gene_model_issues` or `source_defects` entry is warranted.

## What the primary paper shows

[PMID:26873847 Song et al. 2016, J Gen Virol] — **the cache is abstract-only**
(`full_text_available: false`); Europe PMC reports `isOpenAccess: N`, there is no
PMC record, and the publisher site returns HTTP 403. Everything below is from
the abstract.

Experiments reported:

1. Sequence/structure prediction: "An analysis indicated that the protein encoded
   by HolGH15 potentially consisted of two hydrophobic transmembrane helices" and
   "This protein exhibited the structural characteristics of class II holins and
   belonged to the phage_holin_1 superfamily" [PMID:26873847].
2. Heterologous expression: "Expression of HolGH15 in Escherichia coli BL21 cells
   resulted in growth retardation of the host cells, which was triggered
   prematurely by the addition of 2,4-dinitrophenol" [PMID:26873847].
3. Ultrastructure: "The expression of HolGH15 caused morphological alterations in
   engineered E. coli cells, including loss of the cell wall and cytoplasmic
   membrane integrity and release of intracellular components, which were
   visualized by transmission electron microscopy" [PMID:26873847].
4. Structure-function: "Mutation analysis indicated that the two transmembrane
   domains of HolGH15 were indispensable for the activity of the full-length
   protein" [PMID:26873847].
5. Exogenous antibacterial activity: "HolGH15 showed a broad antibacterial range"
   against S. aureus, L. monocytogenes, B. subtilis, P. aeruginosa, K. pneumoniae
   and E. coli, and "At the minimal inhibitory concentration, HolGH15 evoked the
   release of cellular contents and resulted in the shrinkage and death of
   Staphylococcus aureus and Listeria monocytogenes cells" [PMID:26873847].

**What the paper does not contain:** no phage infection, no lysis-timing
experiment on an infected S. aureus culture, and no assay of phage progeny
release or burst size. Every experiment is either heterologous expression in
E. coli or application of purified protein from outside. This matters for the
evidence code on the `viral release` row (below) and is the same evidential
situation our [LysK review](../../BPPGK/lysK/lysK-ai-review.yaml) faced for the
endolysin of phage K, where it deliberately chose `IC` over an experimental code
because "neither cached paper follows an infection".

The follow-up paper [PMID:32955931 Foodborne Pathog Dis 2021] is also
abstract-only and extends the exogenous activity: "In membrane permeabilization
assays, the cytoplasmic β-galactosidase of L. monocytogenes treated with HolGH15
was released via an increase in the permeability of the membrane" and "Electron
microscopy observations indicated that HolGH15 exhibited excellent bactericidal
potency by permeabilizing the cell membrane, damaging membrane integrity, and
inducing cellular content shrinkage or loss" [PMID:32955931].

## Holin biology: does a holin perform lysis, or act upstream of it?

This is the question the batch-3 screen turns on, so it is worked through here
rather than assumed.

Canonical (class I/II) holins are the executors of inner-membrane rupture, not
merely the trigger that lets the endolysin out:

- "the holin, accumulates harmlessly in the cytoplasmic membrane until triggering
  at an allele-specific time to form micron-scale holes"
  [PMID:24585055 Young 2014].
- Cryo-EM shows "massive interruptions in the cytoplasmic membrane" after
  triggering, and the lesions, "ranging in scale up to > 1μm, is dependent solely
  on the function of the S105 protein" [PMID:24585055] — the holin alone, with no
  endolysin, destroys membrane integrity.
- "At the culture level, triggering of a holin, in the absence of endolysin
  function, is detected as a sudden halt in culture growth and respiration, with
  a loss of cytoplasmic ions and small molecules to the medium and a collapse of
  the proton motive force (pmf)" [PMID:24585055]. This is exactly the phenotype
  Song et al. observed on heterologous expression.
- The DNP result identifies HolGH15 as a genuine canonical holin rather than a
  generic toxic membrane protein: "Premature triggering of the lambda holin can
  be imposed by any treatment that reduces the pmf by as little as 40%; this can
  be effected with energy poisons like the uncoupler dinitrophenol (DNP) or by
  sudden anaerobiosis" and "The most important holin-specific feature that should
  be used is DNP-inducible triggering" [PMID:24585055].

The opposite reading — holin as an upstream enabler — is real but is about the
*endolysin*, not about lysis: "the holin would form non-specific channels, or
holes, in the cytoplasmic membrane allowing the endolysin to escape and attack
the peptidoglycan" [PMID:24585055], and
"Holins are small membrane proteins that accumulate in the membrane until, at a
specific time that is \"programmed\" into the holin gene, the membrane suddenly
becomes permeabilized to the fully folded endolysin"
[PMID:11018145 Wang, Smith & Young 2000]. GO itself once took that view: the
obsoleted `GO:0015176 holin` definition reads "Primary function of holins appears
to be transport of murein hydrolases across the cytoplasmic membrane to the cell
wall of bacteria".

But `GO:0044659 viral release from host cell by cytolysis` is defined as "The
dissemination of mature viral particles from a host cell by the rupture of cell
membranes and the loss of cytoplasm." The holin performs the membrane-rupture
half of that definition itself. So even on the timer/export reading, the holin is
*within* the process, and the destruction of the wall by the endolysin follows
immediately: "Destruction of the murein and bursting of the cell are immediate
sequelae" [PMID:11018145].

The division of labour that the [LysK review](../../BPPGK/lysK/lysK-ai-review.yaml)
draws — holin collapses the membrane potential, endolysin hydrolyses the wall —
holds here, and both halves sit inside GO:0044659.

## Ontology gap: GO has no holin molecular function

Both holin terms are obsolete: `GO:0015176` (MF) and `GO:0015832` (BP), each with
comment "This term was made obsolete because it represents a class of gene
products" and only `consider GO:0019835 cytolysis` offered. `GO:0140911
pore-forming activity` is defined as insertion "into the membrane of another
cell", which fits HolGH15 applied exogenously but not a holin acting on the
membrane of the cell that made it; it is also unclear whether HolGH15 forms
discrete pores or the micron-scale lesions of canonical holins. No MF is
therefore asserted in this review, and the gap is recorded as a
`suggested_questions` entry rather than as a `proposed_new_terms` entry, since
naming an activity that avoids the gene-product-class problem that got
`GO:0015176` obsoleted is a decision for GO editors.

## Why no NEW row for the broad-spectrum antibacterial activity

`GO:0051673 disruption of plasma membrane integrity in another organism` is a
good description of what PMID:26873847 and PMID:32955931 actually measure
(permeabilisation of L. monocytogenes, P. aeruginosa, K. pneumoniae and other
species by externally applied protein). It was considered and rejected: none of
those species is a host of phage GH15, exogenous application of purified protein
is not a natural process, and GO annotates biological roles rather than
biotechnological applications. The in vivo role is on the host and is already
covered by GO:0044659 and GO:0020002. Recorded instead in `core_functions`
commentary and `suggested_questions`.

## CACAO rows

Both GOA rows are `assigned_by: CACAO`, both IDA, both citing PMID:26873847.

| Term | Aspect | Qualifier | Date | Verdict |
|---|---|---|---|---|
| GO:0020002 host cell plasma membrane | CC | located_in | 2025-03-31 | ACCEPT |
| GO:0044659 viral release from host cell by cytolysis | BP | acts_upstream_of_or_within_positive_effect | 2025-03-03 | ACCEPT term, WRONG_QUALIFIER defect |

### GO:0020002, located_in, IDA

Biologically right. Two Phobius transmembrane helices (25-44, 56-73) in the
UniProt record, Pfam PF04531 `Phage_holin_1`, NCBIfam TIGR01598 `holin_phiLC3`,
InterPro IPR006485 `Phage-like_holin`; the paper's own mutagenesis shows both
TMDs are "indispensable for the activity of the full-length protein"
[PMID:26873847]; and DNP-triggerable growth arrest is the signature of a protein
sitting in an energised cytoplasmic membrane [PMID:24585055]. The corpus
precedent is [sieA](../../BPP22/sieA/sieA-ai-review.yaml), where GO:0020002 is
ACCEPTed for a phage protein in the bacterial inner membrane.

Two caveats that do *not* change the action:

- The abstract's membrane statements are predictions ("was predicted to encode a
  membrane protein", "potentially consisted of two hydrophobic transmembrane
  helices"); whatever direct localisation experiment supports the IDA is in the
  full text, which is not accessible. Per the curator-deference rule the student
  read it; this is not grounds to downgrade.
- The cells in which HolGH15 was expressed are E. coli BL21, a heterologous
  expression host, not phage GH15's host S. aureus. This brushes against the
  batch-1 shape *heterologous-system localization read as a host location*
  (Sindbis 6K in frog oocytes, phi29 p3 in a mammalian "host cell nucleus"), but
  does not instantiate it: the heterologous cell is itself a bacterium whose
  cytoplasmic membrane is the same structure as the real host's, GO:0020002 names
  no species, and the same paper shows the protein acting on S. aureus. A
  near-miss, not a defect.

### GO:0044659, acts_upstream_of_or_within_positive_effect, IDA

The term is right (see the holin-biology section). The qualifier is wrong, and
the comparator evidence is unusually clean. Of the 50 experimental (IDA/IMP/IGI)
annotations to GO:0044659 in GOA, 44 use `involved_in`, including:

- `P03705` lambda S, the archetypal canonical holin — `involved_in`, IDA,
  UniProt;
- `D6QY02 lysGH15` — the endolysin of **this same phage GH15**, from the same
  Jilin University group, a CACAO IDA row with `involved_in`;
- `P13559 XV` (PRD1 endolysin, already reviewed in CACAO batch 1) —
  `involved_in`, IDA, CACAO.

All six experimental rows on this term with a non-standard positive-effect
qualifier are CACAO rows (I6P9Q0, M1R9I8, P03682, P11187, Q9T1W9, Q9T1X2). Two of
those genes carry a **paired UniProt row with the same term, same PMID and same
evidence code qualified `involved_in`** (Q9T1W9 Mup25, Q9T1X2 lys, both from
PMID:35471081) — a professional curator working from identical input chose
`involved_in` where CACAO chose the positive-effect variant. Filed as a
`WRONG_QUALIFIER` source defect against CACAO, exactly as in
[acrIIA5](../../9CAUD/acrIIA5/acrIIA5-ai-review.yaml).

A second, independent defect on the same row, which the screen did not predict:
the evidence code. GO:0044659 asserts the dissemination of progeny virions, and
no experiment in PMID:26873847 follows an infection or measures release of
progeny. The protein's lytic activity is directly assayed, so IDA is defensible
for the cytolysis half; the life-cycle half is an inference from holin class.
This is the situation in which the LysK review chose `IC`. Filed as a
`WRONG_EVIDENCE_CODE` defect with `confidence: SUSPECTED`, because the
inaccessible full text could in principle contain an infection experiment the
abstract does not mention.

## GONUTS

GONUTS has been **retired**, not merely taken offline. `gowiki.tamu.edu` now
returns HTTP 410 Gone with a page titled "GONUTS has been retired" ("The GO wiki
that was at gowiki.tamu.edu is no longer online."); EcoliWiki and OMP are still
served. This is a change from the "temporarily offline while we perform upgrades"
banner recorded in the project page through batches 1-2, and it means the GONUTS
curator notes and figure references are permanently unavailable as a check on
abstract-only CACAO rows.

The Internet Archive does hold a snapshot of
`gowiki.tamu.edu/wiki/index.php/PMID:26873847` dated 2024-11-06 (confirmed via
the Wayback availability API), but `web.archive.org` is blocked by this
container's egress policy, so it could not be read. Both CACAO rows on this gene
are dated March 2025, after that snapshot, so it would probably not have shown
them in any case.

## Suggested work

- Lysis-timing and burst-size experiments on S. aureus infected with GH15 and
  with a holin-defective derivative: the one experiment that would turn the
  GO:0044659 row into a genuinely direct annotation.
- Whether HolGH15 forms micron-scale lesions (canonical holin) or small channels
  (pinholin), which determines whether a pore-forming MF would ever fit.
- Whether HolGH15 and LysGH15 act as a functional pair in vivo, as the
  holin-endolysin model predicts.
