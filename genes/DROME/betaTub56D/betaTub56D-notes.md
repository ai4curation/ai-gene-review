# betaTub56D (Q24560, TBB1_DROME) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New review; no earlier review existed. ProtNLM2 output was not opened or used.

### Why this review was made

betaTub56D is the nearest experimentally characterised relative of betaTub97EF (Q8MST5), so its
findings will be the reference for transfer to that gene. The notes below keep two kinds of claim apart.
Some are established by experiments on this gene in D. melanogaster. Others are inferred from the
tubulin family.

### Deep research

`just deep-research-falcon DROME betaTub56D --fallback perplexity-lite` failed. Falcon gave
`Exception: Failed to authenticate` from the Edison client. The perplexity-lite fallback gave HTTP 401
`insufficient_quota`. So there is no deep-research file. I searched PubMed directly with
(betaTub56D OR "beta1 tubulin" OR "beta 1 tubulin" OR "beta1-tubulin") AND drosophila, which returned
18 hits, and cached the relevant ones. All of them are abstract-only in the cache except PMID:32066907.

### Phylogenetic placement (PANTHER 19.0)

- The PANTHER 19.0 fruit-fly classification places Q24560 in PTHR11588:SF504, "TUBULIN BETA-1
  CHAIN-RELATED". Q8MST5 (betaTub97EF) is in SF490, "TUBULIN BETA CHAIN".
- In the tree, betaTub56D sits in PTN000904125 with betaTub60D and betaTub65B. That node is sister to
  the betaTub97EF clade (PTN008520933) under the arthropod node PTN008974067. Both clades fall inside
  the metazoan beta-tubulin node.
- Every IBA on this gene comes from the tubulin root node PTN000172598. That node also carries alpha,
  gamma and other tubulins. Only family-wide terms are inherited: MT organisation, mitotic cell cycle,
  structural constituent, GTP binding, cytoplasm and microtubule. No gamma-tubulin nucleation terms
  are inherited, which is correct.
- The PTHR11588 family review leaves the GTPase activity (GO:0003924) scope UNRESOLVED family-wide.

### Experimental findings on this gene product in D. melanogaster

1. **It is the ubiquitous, constitutively expressed beta-tubulin.** [PMID:3119300 "The beta 1 tubulin
   gene of Drosophila is constitutively expressed, whereas the beta 2 tubulin is expressed specifically
   in the testes."] It is maternally supplied: mRNA is present in nurse cells and evenly distributed in
   early embryos [PMID:3125412 "beta 1 tubulin mRNA to be maternally expressed in the nurse cells of the
   egg chambers and evenly distributed during early embryogenesis"].
2. **It is incorporated into mitotic spindles.** Isotype-specific antibodies were used.
   [PMID:1903298 "Maternally expressed beta 1 tubulin is incorporated into mitotic spindles."] Later
   expression is strong in the CNS, chordotonal organs and apodemes (same paper). In testis, beta1 is
   the only beta isotype in the early mitotic stages of spermatogenesis, and it is a major component of
   cyst cells [PMID:8246879 "In the early, mitotically active stages of spermatogenesis, only the beta 1
   tubulin isotype is expressed."].
3. **It is required for microtubules to exist in fat body cells.** [PMID:32066907] RNAi against
   tubulin subunits "significantly disrupted MTs", and the extended data name the reagent as
   "β-Tub56D RNAi". UniProt's curated disruption phenotype states that "RNAi-mediated knockdown
   eliminates microtubules" (ECO:0000269, PubMed:32066907). Knockdown of the beta subunit also reduces
   alpha-tubulin levels, as expected for an obligate heterodimer. The nuclear-positioning and
   basement-membrane secretion defects in that paper are downstream consequences of losing
   microtubules. They are not activities of tubulin, so they are not annotated.
4. **The gene is essential, and its paralog cannot fully substitute.** Zygotic null larvae die in the
   first instar, after embryogenesis is carried by maternal protein. A UAS-betaTub56D transgene fully
   rescues; UAS-betaTub97EF (4B or 4C) rescues only partially. [PMID:29084803; publisher text read
   through web-fetch, see betaTub56D-literature/PMID_29084803-betaTub56D-excerpts.md. The cache is
   abstract-only.] Lethality shows necessity, not participation in any particular organismal process.
5. **Folding and stability depend on prefoldin.** UniProt curates an interaction with mgr (prefoldin
   subunit 3 / VBP1 counterpart) and Vhl [PMID:22451918, ECO:0000269]. mgr mutants lose tubulin, and
   depleting beta-tubulin phenocopies the mgr spindle defects (abstract). This shows betaTub56D is a
   prefoldin/CCT client and is needed for spindle integrity. It does not give betaTub56D a chaperone
   activity, and the interaction is not turned into a binding MF.
6. **A maternal beta1-GFP protein trap is dominant-negative in embryos.** Nonetheless, the maternal
   beta1-based microtubule network is enough for myoblast fusion and myotube elongation in beta3
   mutants [PMID:22306378]. This is more support for incorporation into embryonic microtubules.
7. Expression in apodemes is induced by muscle insertion [PMID:8905296, PMID:8408299, PMID:8735928].
   The CNS and maternal expression depends on intron enhancers [PMID:8692694]. These papers are about
   transcriptional regulation and say nothing new about protein function.
8. The PDB holds X-ray and cryo-EM structures with Q24560 as the beta chain (6TIS/6TIU/6TIY/6TIZ,
   7QUC/7QUD/7QUP, 7YSQ/7YSR), including microtubule lattice reconstructions. I did not read the
   primary papers, so they are not cited as evidence.

### Inferred, not tested on this gene

- GTP binding at the exchangeable (E) site, Mg2+ cofactor, and GTP-binding residues. UniProt
  propagates these from human/pig beta-tubulin (ECO:0000250). The E-site GTP is hydrolysed in the
  lattice with a catalytic residue from the alpha subunit of the next dimer. No betaTub56D-specific
  nucleotide measurement exists.
- Heterodimerisation with alpha-tubulin (tubulin complex). This is supported indirectly by the
  co-depletion of the alpha subunit in the fat body RNAi, but no direct biochemistry was found.

### Decisions

- Accept the core structural terms: structural constituent of cytoskeleton, microtubule, and
  microtubule cytoskeleton organization. The gene-specific evidence for these is strong.
- GTP binding is accepted. GTPase activity is accepted with the same caveat as the betaTub97EF review
  (composite site, realised only in the lattice), for consistency across the two paralogs.
- Mitotic cell cycle (IBA) is kept as non-core. The spindle evidence is captured by a NEW annotation,
  located_in mitotic spindle (GO:0072686), based on PMID:1903298.
- cytoskeleton → MODIFY to microtubule. microtubule-based process → MODIFY to MT cytoskeleton
  organization. cytoplasm is kept as non-core.
- The three ARBA developmental terms are MARK_AS_OVER_ANNOTATED. Unlike betaTub97EF, this gene is
  essential, but essentiality and organismal phenotypes are necessity evidence. The process terms are
  not participation by tubulin.
- No ancestor- or descendant-redundant NEW terms were proposed.

### Transfer caveat for betaTub97EF

betaTub56D and betaTub97EF are in different PANTHER subfamilies (SF504 versus SF490). Only the shared
family-level properties should be transferred: lattice incorporation, structural constituent, GTP
binding and MT organisation. The following are betaTub56D-specific and should not be transferred:
maternal supply, ubiquitous expression, essentiality, mitotic-spindle predominance in early embryos
and early germ cells, and full self-rescue.
