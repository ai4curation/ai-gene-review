# NIT1 (P40447 / YIL164C) - research notes

S. cerevisiae **NIT1** = ORF **YIL164C**, UniProt **P40447**, SGD **S000001426**.
199 aa, ~21.6 kDa. UniProt PE=5 ("Uncertain"). This is an UNDERSTUDIED gene: no
gene-specific experimental biochemistry, only sequence-based / high-throughput data.

## The single most important fact: NIT1 (YIL164C) is NOT the yeast dGSH-amidase

There are two Nit-domain / carbon-nitrogen-hydrolase paralogs in S. cerevisiae that
are easily confused:

- **NIT2 = YJL126W** — the *characterised* one. It is the true ortholog of **human
  NIT1** and has **demonstrated deaminated-glutathione amidase activity (IDA)**. In
  Peracchi et al. 2017 the yeast enzyme they cloned and named "scNit1" is this gene:
  Table 1 gives its gene symbol as *NIT2*, and they used a "*NIT2*-KO" strain. So the
  dGSH-repair function belongs to YJL126W, **not** to YIL164C.
- **NIT1 = YIL164C** — the gene under review here. A *distinct* paralog. No specific
  substrate or biological role has been demonstrated. It is the "other" S. cerevisiae
  Nit-domain protein.

Provenance:
- [PMID:28373563 "both the mammalian Nit1 and its yeast ortholog are amidases highly active toward deaminated glutathione (dGSH; i.e., a form of glutathione in which the free amino group has been replaced by a carbonyl group)"] — the characterised yeast enzyme.
- [PMID:28373563 "Nit1-KO mutants of both human and yeast cells accumulate dGSH and the same compound is excreted in large amounts in the urine of Nit1-KO mice"] — the KO phenotype is for that ortholog (YJL126W per the paper's Table 1 / Methods), not YIL164C.
- SGD curation: yeast NIT2/YJL126W "enables deaminated glutathione amidase activity" (IDA), "hydrolase involved in amide catabolism; localizes to both the cytoplasm and mitochondria" (SGD locus page, WebFetch 2026-07).
- SGD: NIT2 is "one of two proteins in S. cerevisiae with similarity to the Nit domain" — the other is YIL164C (our NIT1).

**Implication for this review:** the temptation is to transfer the well-characterised
human-NIT1 / yeast-NIT2 dGSH-amidase function onto YIL164C. That would be a
paralog-mis-attribution error. YIL164C's function is genuinely unknown.

**The falcon deep-research file fell into exactly this trap** (documented, not fixed):
`NIT1-deep-research-falcon.md` asserts that YIL164C "IS" the dGSH amidase scNit1 and
copies over Peracchi's kinetics, crystal structure and triad. That is incorrect. Two
independent checks show scNit1 is NOT YIL164C:
- Peracchi 2017 **Table 1** lists the yeast dGSH-amidase gene as **NIT2** and the
  ω-amidase gene as **NIT3** (WebFetch of PMC5402446, 2026-07); SGD independently
  curates **NIT2 (YJL126W)** with "deaminated glutathione amidase activity" (IDA).
  SGD curates **YIL164C** with ONLY "nitrilase activity (ISA)" — no dGSH amidase, no
  experimental MF annotation.
- The scNit1 catalytic-triad numbering in Peracchi/Liu is **Glu45-Lys127-Cys169**; the
  UniProt-predicted triad for YIL164C (P40447) is **Glu44-Lys135-Cys169**. The Lys
  differs (127 vs 135), consistent with scNit1 being a *different* ORF (NIT2/YJL126W),
  not YIL164C. (Cys169 coincidence aside.)
So the falcon report's central functional claim for YIL164C is a paralog conflation.
I retain the falcon file (genuine late artifact) but do NOT use it to support any
functional claim; it is cited only with a reference_review flagging the error.

Yeast nitrilase/Nit-family ORF map (SGD, authoritative):
- NIT1 = YIL164C = P40447 (this gene) — nitrilase-family, function unknown (ISA only).
- NIT2 = YJL126W — deaminated glutathione amidase (IDA); ortholog of human NIT1.
- NIT3 = YLR351C — Nit-domain hydrolase in amide catabolism.

## Nitrilase superfamily context — the generic "nitrilase activity" trap

The carbon-nitrogen hydrolase (nitrilase) superfamily is notoriously over-annotated.
Pace & Brenner's foundational classification (PMID:11380987):

- 13 branches; **only branch 1 has demonstrated nitrilase activity**, the rest are
  amidases / amide-condensation enzymes:
  [PMID:11380987 "Despite historical classification of all of these sequences as nitrilase-related, only one branch is known to have nitrilase activity, whereas eight branches have apparent amidase or amide-condensation activities"].
- Annotation quality is poor:
  [PMID:11380987 "Automated sequence searching easily identifies predicted polypeptides as members of the nitrilase superfamily, but many database annotations have been applied haphazardly"].
- Catalytic triad:
  [PMID:11380987 "Essentially all members of the nitrilase superfamily have a conserved, apparent catalytic triad of glutamate, lysine and cysteine (only three apparently truncated sequences lack the glutamate)"].

Branch 1 (true nitrilases) is the plant IAN→IAA auxin-biosynthesis branch
(Arabidopsis NIT1–4). YIL164C is NOT a plant nitrilase; the SGD-assigned "nitrilase
activity" (ISA, GO:0000257) uses **Arabidopsis NIT1 (UniProtKB:P32961)** as the
with/from — a genuine branch-1 nitrilase — but transferring plant nitrilase activity
to a divergent fungal paralog is exactly the "haphazard" transfer Pace & Brenner warn
against. Human NIT1 and yeast NIT2 (the characterised orthologs) are **amidases, not
nitrilases**, so even the closest characterised relatives do not have nitrilase
activity:
[PMID:28373563 "Despite being ∼35% sequence identical to ω-amidase (Nit2), the Nit1 protein does not hydrolyze efficiently α-ketoglutaramate (a known physiological substrate of Nit2), and its actual enzymatic function has so far remained a puzzle"].

## Truncation / split-ORF: YIL164C + YIL165C

UniProt CAUTION for P40447: "Could be the product of a pseudogene. NIT1/YIL164C seems
to be the N-terminal part of a putative nitrilase-like protein formed of NIT1/YIL164C
and YIL165C." (file:yeast/NIT1/NIT1-uniprot.txt)

My own bioinformatics analysis (file:yeast/NIT1/NIT1-bioinformatics/RESULTS.md) supports
and sharpens this:
- The nitrilase E-K-C catalytic triad residues **are all present and correctly
  positioned in YIL164C**: E44 (proton acceptor), K135 (proton donor), C169
  (nucleophile, in the diagnostic `GGAICWEN` motif); they align to the same columns as
  the triad of human NIT1, human NIT2 and Arabidopsis NIT1. So YIL164C is NOT a
  triad-loss pseudoenzyme.
- BUT YIL164C covers only the **N-terminal ~2/3** of the nitrilase fold (alignment
  cols 1–270); the adjacent ORF **YIL165C (P40446, 119 aa)** covers the C-terminal
  ~1/3 (cols 271–406) with essentially no overlap, and their 318-aa concatenation
  spans the full domain (matching human NIT1 327 aa, Arabidopsis 346 aa). So YIL164C
  as annotated is a **truncated fragment** lacking the C-terminal third of the fold
  (which contributes to folding/oligomerisation in this superfamily) — unlikely to be
  an active enzyme on its own.
- Both YIL164C and YIL165C sit in the **uncharacterised PANTHER subfamily
  PTHR46044:SF1 "CN hydrolase domain-containing protein"**, not in any
  substrate-defined branch (arylacetonitrilase SF14, cyanide hydratase SF4,
  nitrilase-1-related SF11).

SGD independently notes: "in closely related species and other S. cerevisiae strain
backgrounds YIL164C and adjacent ORF, YIL165C, likely constitute a single ORF encoding
a nitrilase gene" (SGD locus page, WebFetch 2026-07); and that YIL164C/YIL165C "have
significant homology to the nitrilase superfamily … but have low sequence homology to
the other two S. cerevisiae nitrilases NIT2 and NIT3" (SGD / Koyama & Walsh 2022
community reference S000316277).

## SGD-curated status and phenotypes (all high-throughput / sequence-based)

- ORF status: **Verified ORF** (not dubious), but molecular function is only "putative
  nitrilase" by sequence alignment (ISA); biological process and cellular localization
  are curated as **unknown** (ND). No GFP localization datum.
- Deletion (high-throughput screens): increased chronological lifespan and competitive
  fitness; decreased anaerobic growth and starvation resistance; abnormal vacuolar
  morphology. These are pleiotropic screen hits, not a defined pathway role.
  (SGD locus page, WebFetch 2026-07.)

## The ISA reference (PMID:10959838)

PMID:10959838 (Pace et al. 2000, worm NitFhit crystal structure) is the
`original_reference_id` for the SGD ISA "nitrilase activity" annotation, but the
with/from field is Arabidopsis NIT1 (P32961). The paper is a **structure** paper about
C. elegans NitFhit and states the fold has "a presumptive Cys-Glu-Lys catalytic triad"
— it does not demonstrate any substrate for the enzyme, let alone for yeast YIL164C.
Abstract only (full_text_available: false).

## KNOWN vs NOT-KNOWN (explicit)

KNOWN:
- YIL164C is a verified ORF encoding a carbon-nitrogen-hydrolase-superfamily
  (nitrilase-family) domain (Pfam PF00795; PANTHER PTHR46044:SF1).
- It retains an intact, correctly positioned Glu-Lys-Cys catalytic triad (E44/K135/C169).
- It corresponds to the N-terminal ~2/3 of a full nitrilase fold; the C-terminal third
  is the adjacent ORF YIL165C; together they equal one full-length domain.
- It is a distinct paralog from yeast NIT2 (YJL126W), which is the characterised dGSH
  amidase / ortholog of human NIT1.
- High-throughput deletion phenotypes exist (lifespan, fitness, vacuolar morphology).

NOT KNOWN:
- Its physiological substrate — no substrate has been demonstrated for YIL164C.
- Its catalytic activity in vivo — whether the truncated fragment folds/oligomerises
  into an active enzyme at all.
- Its biological process and cellular localization (curated as unknown).
- Whether YIL164C and YIL165C are translated as a single protein in S288C, or whether
  YIL164C is a disrupted pseudogene remnant.

## References used
- PMID:11380987 — Pace & Brenner 2001, nitrilase superfamily classification (full text cached).
- PMID:28373563 — Peracchi et al. 2017, Nit1 = dGSH amidase (abstract cached); the yeast enzyme is NIT2/YJL126W.
- PMID:10959838 — Pace et al. 2000, worm NitFhit structure (abstract cached); ISA source.
- file:yeast/NIT1/NIT1-uniprot.txt — UniProt P40447 (family, PROSITE triad, pseudogene CAUTION).
- file:yeast/NIT1/NIT1-bioinformatics/RESULTS.md — triad-integrity, truncation, orthology analysis.
- SGD locus YIL164C / NIT2(YJL126W); Koyama & Walsh 2022 SGD community reference S000316277 (no PMID; not used for verbatim quotes).
