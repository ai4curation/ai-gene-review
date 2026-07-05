# SDD3 (YOL098C / Q12496) — curation notes

Journal for the AI GO-annotation review of the understudied ("dark") *S. cerevisiae*
gene **SDD3**. Provenance recorded inline as `[PMID:xxxx "verbatim text"]`.

## Identity

- SGD standard name **SDD3** = systematic name **YOL098C**; SGD:S000005458; UniProt **Q12496**
  (entry name YO098_YEAST). 1037 aa. Status at SGD: **Verified** (a real protein-coding gene,
  not a dubious ORF).
- The UniProt record still labels it "Uncharacterized protein YOL098C" with gene names
  `YOL098C` / ORF `HRF1037`; the SGD standard name SDD3 (from Wang & Chen 2015) has not yet
  propagated to the UniProt `GN` line — this is why `just fetch-gene yeast SDD3` failed on the
  symbol and the gene had to be fetched via the systematic name YOL098C. Files were then
  consolidated under `genes/yeast/SDD3/`.
- SGD name description: **"Suppressor of Degenerative Death"**.
- SGD one-line description: *"Putative metalloprotease; overproduction suppresses lethality due
  to expression of the dominant PET9 allele AAC2-A128P"* (SGD locus S000005458, sourced to Wang
  & Chen 2015, PMID:26192197).

## Domain architecture / inline bioinformatics (from SDD3-uniprot.txt)

- **Peptidase M16 family (pitrilysin/inverzincin clan ME)**. UniProt cross-refs:
  - Pfam `PF00675` Peptidase_M16 (N-terminal catalytic domain) + `PF05193` Peptidase_M16_C
    (C-terminal domain).
  - MEROPS `M16.A04`.
  - InterPro `IPR011249` (Metalloenzyme LuxS/M16), `IPR011765` (Pept_M16_N), `IPR007863`
    (Peptidase_M16_C).
  - Gene3D `3.30.830.10` ×3 (Metalloenzyme, LuxS/M16 peptidase-like fold).
  - PANTHER family `PTHR43016` "PRESEQUENCE PROTEASE"; subfamily `PTHR43016:SF16`
    "METALLOPROTEASE, PUTATIVE (AFU_ORTHOLOGUE AFUA_4G07610)-RELATED".
- **Catalytic-motif check (done inline on the sequence):** the M16 family inverted zincin
  signature **HxxEH** is present at residues **60-64 = H-T-L-E-H** (His60, Glu63, His64). In M16
  peptidases the two His residues coordinate the catalytic Zn²⁺ and the Glu is the general base; a
  candidate third metal ligand Glu lies ~70 residues downstream (E135, "…TEVYHID…"). So SDD3 **retains the
  canonical catalytic apparatus at the primary-sequence level** — it is NOT an obvious
  pseudo-protease (no gross loss of the HxxEH motif). This is sequence-level evidence of the
  *potential* for zinc metalloendopeptidase activity; it is NOT a demonstration of catalytic
  activity.
- The broad PTHR43016 family contains PreP/pitrilysin-type presequence proteases (mitochondrial
  MPP, PreP, cytosolic pitrilysin/insulysin relatives). However, SDD3 sits in the small,
  uncharacterized subfamily **SF16**, whose only reviewed members are all "putative" and
  uncharacterized (see orthology below). No SDD3-specific substrate, cleavage specificity, or
  catalytic assay exists.

## Orthology (from interpro/panther/PTHR43016/PTHR43016-entries.csv, subfamily SF16)

Reviewed SF16 members (a small, uniformly uncharacterized subfamily):
- *S. cerevisiae* YOL098C / SDD3 (Q12496, 1037 aa) — this gene.
- *S. pombe* SPAC3H1.02c (Q10068, 1036 aa) — near-identical length, clear ortholog; also
  "Uncharacterized". (SGD alias list for SDD3 explicitly includes `SPAC3H1.02c`.)
- *C. elegans* C05D11.1 (P48053, 995 aa) — "Uncharacterized".
- *A. fumigatus* AFUA_4G07610 — the PANTHER subfamily name is anchored to this ortholog.

Interpretation: SF16 is a **conserved-but-dark M16 subfamily** — orthologs from yeast to worm,
none functionally characterized. This is a textbook conserved-unknome situation.

## Known experimental / literature evidence

### PMID:26192197 — Wang X & Chen XJ (2015) Nature. "A cytosolic network suppressing mitochondria-mediated proteostatic stress and cell death." (full text cached)
- YOL098C was recovered in a **multicopy (overexpression) suppressor screen** for genes that,
  when over-expressed, inhibit AAC2^A128P-induced degenerative cell death. It is one of 40
  suppressors and one of eight uncharacterized ones named **SDD1-4**: *"The remaining eight
  include the uncharacterized YEL057C, YMR074C, YOL098C and the truncated YPR022C that are named
  SDD1-4 (Suppressor of Degenerative Death) respectively"* [PMID:26192197]. YOL098C is **SDD3**
  (third of the four).
- General mechanism of the network (not SDD3-specific): the suppressors relieve "mitochondrial
  Precursor Over-accumulation Stress" (mPOS) — cytosolic accumulation/aggregation of unimported
  mitochondrial precursors — largely by modulating cytosolic translation, mRNA turnover, and
  protein chaperoning/turnover: *"We also discover a large network of genes that suppress mPOS,
  by modulating ribosomal biogenesis, messenger RNA decapping, transcript-specific translation,
  protein chaperoning and turnover"* [PMID:26192197].
- Localization of the network: *"All of the suppressors are located in the cytosol, suggesting
  that they prevent cell death via pathways that operate in the cytosol"* [PMID:26192197].
- **Curation caveat:** this is an *overexpression / gain-of-function genetic* phenotype in a
  screen, not a demonstration of SDD3's normal cellular role or of any biochemical activity.
  SDD3 was named but NOT individually characterized (no deletion phenotype, no substrate, no
  mechanism assigned to SDD3 specifically in this paper). Its recovery is fully consistent with,
  but does not prove, a proteostasis/protein-turnover role.

### PMID:14562095 — Huh WK et al. (2003) Nature. "Global analysis of protein localization in budding yeast." (abstract-only cache)
- Source of the GOA `GO:0005737 cytoplasm` HDA annotation (GFP-fusion localization study,
  ~75% of the proteome). SDD3-GFP was scored cytoplasmic. Consistent with the "all suppressors
  are cytosolic" statement above. (Note GOA cites PMID:14562095 for the CC term; the UniProt DR
  line lists the cytoplasm GO term as `HDA:SGD`.)

### PMID:30358795 — Wang Y et al. (2018) Metallomics. "The cellular economy of the S. cerevisiae zinc proteome." (abstract-only cache)
- Source of the GOA `GO:0008270 zinc ion binding` **RCA** annotation. This is a **proteome-wide
  computational prediction**: *"The yeast zinc proteome of 582 known or potential zinc-binding
  proteins was identified using a bioinformatics analysis that combined global domain searches
  with local motif searches"* [PMID:30358795]. SDD3/YOL098C was among the predicted zinc
  proteins — consistent with the M16 HxxEH zincin motif, but this is a prediction, not a direct
  binding measurement for SDD3.

## KNOWN vs NOT-known summary

KNOWN (defensible):
- Real, verified protein-coding gene; ~1037-aa cytoplasmic protein (experimental GFP
  localization, PMID:14562095; corroborated by PMID:26192197).
- Belongs to the M16 peptidase family (pitrilysin clan) and retains the canonical HxxEH catalytic
  zincin motif (sequence-level; UniProt/Pfam/InterPro/MEROPS + inline motif check).
- Predicted zinc-binding protein (computational, PMID:30358795), consistent with the domain.
- Overexpression suppresses AAC2^A128P-induced degenerative cell death (genetic gain-of-function;
  member of the anti-mPOS cytosolic proteostasis network, PMID:26192197).

NOT known (the real gaps):
- No demonstrated **catalytic (metalloendopeptidase) activity** for SDD3 or any SF16 ortholog;
  no substrate, no cleavage specificity, no in-vitro assay. "Putative metalloprotease" only.
- No demonstrated **direct zinc binding** for the SDD3 protein (RCA prediction only).
- No **loss-of-function** phenotype defining a normal biological role (the only phenotype is
  overexpression suppression). Whether SDD3 normally participates in cytosolic proteostasis /
  mitochondrial-precursor clearance, or does something else entirely, is undetermined.
- No physical **interaction partner or substrate** identified.
- The entire conserved **SF16 subfamily** (yeast→worm) is functionally uncharacterized.

## Annotation-by-annotation plan

1. `GO:0046872 metal ion binding` (IEA, InterPro/IPR011249) — domain-consistent but generic;
   KEEP_AS_NON_CORE (the more specific zinc term already exists). Generic parent of zinc binding.
2. `GO:0008270 zinc ion binding` (RCA, PMID:30358795) — computational zinc-proteome prediction,
   consistent with M16 zincin motif; KEEP_AS_NON_CORE (defensible as domain/prediction support,
   but not experimentally demonstrated for SDD3).
3. `GO:0005737 cytoplasm` (HDA, PMID:14562095) — experimental GFP localization; ACCEPT (core;
   the one solid, experimentally supported annotation). Cytosol would be more precise.
4. `GO:0008150 biological_process` (ND, GO_REF:0000015) — root "no data" placeholder;
   KEEP_AS_NON_CORE (this is the honest current state — BP is genuinely undetermined; do not
   invent a BP). ND root annotations are retained as-is, not removed.

Core functions: keep conservative. The only experimentally supported fact is cytosolic
localization. Catalytic activity is domain-inferred (motif intact) but never demonstrated, so it
belongs in knowledge_gaps, and I will include at most a single, explicitly-hedged domain-inferred
metalloendopeptidase core function (or none). Primary deliverable = knowledge_gaps.

## Deep research status

`just deep-research-falcon yeast SDD3 --fallback perplexity-lite` was run twice. First attempt
failed (falcon template error because the UniProt file was not yet under `genes/yeast/SDD3/`;
perplexity-lite fallback returned HTTP 401 insufficient_quota). A second attempt (after moving the
UniProt file into place) **succeeded**: falcon produced `SDD3-deep-research-falcon.md` (~29 min,
24 citations) before the recipe's separate perplexity-lite fallback step erred on quota. The
falcon report independently corroborates this review: it confirms "SDD3" is ambiguous but that the
target is YOL098C, places YOL098C squarely in the M16 metalloendopeptidase family with the HXXEH
inverted zinc-binding motif and clamshell architecture, contextualizes it against characterized
yeast M16 members (MPP Mas1/Mas2, Cym1), and states that "No primary literature was identified
that directly characterizes the function, substrate specificity, localization, or biological role
of YOL098C" — matching the knowledge_gaps here. This review is grounded directly in the UniProt
record, the GOA TSV, the cached primary literature (PMID:26192197 full text; PMID:14562095 and
PMID:30358795 abstracts), SGD, PANTHER orthology, inline domain/motif analysis, and this falcon
report — no fabricated content.
