# YET2 (Q04210 / YMR040W) review notes

Journal for the AI GO-annotation review of *Saccharomyces cerevisiae* **YET2** (systematic
name YMR040W; standard name YET2 = "Yeast ER Transmembrane 2"). This is an **understudied
("dark") gene**: SGD records molecular_function and biological_process as ND ("No biological
Data available"). The primary deliverable is an honest `knowledge_gaps` section plus
carefully-reasoned `description`/`core_functions` grounded in domain architecture, orthology,
and the thin literature — never invented function.

## Identity / fetch provenance

- Bare symbol `YET2` did not create the gene folder on the first `just fetch-gene` attempts
  (shared machine under heavy parallel load; empty output). Resolved identity directly against
  UniProt REST: `gene:YET2 AND organism_id:559292` → **Q04210**, `YET2_YEAST`,
  "Endoplasmic reticulum transmembrane protein 2", 160 aa, systematic name YMR040W, SGD
  S000004643. Re-fetched successfully with `--uniprot-id Q04210`.
- Files written to `genes/yeast/YET2/`: `YET2-uniprot.txt`, `YET2-goa.tsv`,
  `YET2-ai-review.yaml` (10 GOA annotations seeded).

## Domain / topology analysis (from YET2-uniprot.txt, inline — no sub-agent)

- **Family**: BCAP29/BCAP31 (BAP29/BAP31) family. Pfam PF05529 (Bap31); InterPro IPR008417
  (BAP29/BAP31) + IPR040463 (BAP29/BAP31_N); PANTHER PTHR12701 ("BCR-ASSOCIATED PROTEIN, BAP"),
  subfamily PTHR12701:SF19 ("ENDOPLASMIC RETICULUM TRANSMEMBRANE PROTEIN 1-RELATED").
  [file:yeast/YET2/YET2-uniprot.txt "SIMILARITY: Belongs to the BCAP29/BCAP31 family"]
- **Topology** (small, 160 aa, ~19 kDa): three predicted TM helices — TM1 3–23, TM2 46–66,
  TM3 104–124 — with N-terminus lumenal (1–2), a cytoplasmic loop 24–45, a large lumenal loop
  67–103, and a C-terminal cytoplasmic tail 125–160. This is the canonical BAP31-type
  triple-membrane-spanning architecture. [file:yeast/YET2/YET2-uniprot.txt TRANSMEM 3..23 /
  46..66 / 104..124]
- **C-terminal cytoplasmic tail (125–160)** is charged/leucine-rich
  (`...KEKLRRKQKYLEELQKKKF`), consistent with the coiled-coil "cytosolic" region that in
  mammalian BAP31 mediates protein–protein interactions and apoptosis signaling.
- **C-terminal di-lysine ER-retrieval motif**: MOTIF 157–160 (di-lysine motif). The tail ends
  `...QKKKF`, a KKxx-type COPI-retrieval signal. [file:yeast/YET2/YET2-uniprot.txt "The
  di-lysine motif confers endoplasmic reticulum localization for type I membrane proteins"]
  → strong structural basis for steady-state ER-membrane residence.
- UniProt FUNCTION (from Ref. 3 = Toikkanen 2006): "May play a role in anterograde transport
  of membrane proteins from the endoplasmic reticulum to the Golgi." Note the hedge "May" —
  UniProt itself marks this as tentative. [file:yeast/YET2/YET2-uniprot.txt]

Interpretation: domain architecture robustly places YET2 as an **ER polytopic membrane protein
of the BAP31 family**. Architecture supports a *scaffold/adapter* mode of action (three TM
helices + cytosolic coiled-coil tail, like BAP31) but does **not** encode any catalytic
domain — consistent with MF = ND. Localization (ER membrane) is well supported; a *specific
molecular activity and physiological cargo* are the core unknowns.

## Literature landscape — separating YET2 from YET1/YET3 and BAP31/BAP29

The yeast BAP31 family has three paralogs. Attribution matters: most mechanistic work is on the
**Yet1p–Yet3p complex**, NOT Yet2p.

1. **Toikkanen, Fatal, Hilden, Makarow, Kuismanen (2006)**, "YET1, YET2 and YET3 of
   *Saccharomyces cerevisiae* encode BAP31 homologs with partially overlapping functions",
   *J. Biol. Sci. (Faisalabad)* 6:446-456. DOI 10.3923/jbs.2006.446.456. **This is the sole
   YET2-naming/function paper and it is NOT indexed in PubMed** (low-tier journal; no PMID —
   confirmed by search and by UniProt citing it as "Ref. 3" without a PMID). Abstract
   (verbatim, from scialert): the three ORFs are YKL065C (YET1), **YMR040W (YET2)**, YDL072C
   (YET3); "YET genes were not essential for viability"; "disruption of YET1 increased and
   YET3 decreased the cell growth"; in "yet1Δ yet3Δ and **yet2Δ yet3Δ** double disruptant
   cells the growth was restored to the level observed in the wild type cells"; "Yet proteins
   have partially specialized, but overlapping functions"; "yet3Δ cells showed a defect in
   invertase secretion." → YET2-specific content is minimal: only its systematic-name
   assignment and its participation in a `yet2Δ yet3Δ` epistasis (growth restoration).
   No YET2-specific molecular activity is reported.

2. **Wilson JD, Barlowe C (2010)**, "Yet1p and Yet3p, the yeast homologs of BAP29 and BAP31,
   interact with the endoplasmic reticulum translocation apparatus and are required for
   inositol prototrophy", *J Biol Chem* 285:18252-61. **PMID:20378542** (cached
   abstract-only; PMCID PMC2881749). This is the key mechanistic paper but it is about the
   **Yet1p–Yet3p (BAP29/BAP31) complex**: Yet1p forms a complex with Yet3p; the Yet complex
   is NOT efficiently packaged into COPII vesicles (so does not act as an ER export receptor);
   a fraction associates with the Sec translocation complex; associations increase under ER
   stress; yet1Δ and yet3Δ show inositol-starvation growth defects. YET2-specific findings
   (from the full text, seen via PMC/WebFetch but NOT in the cached abstract — so NOT
   quotable as verbatim supporting_text): **Yet2p is DTT/UPR-inducible** ("undetectable in the
   absence of DTT but clearly present after DTT exposure"), Yet2p shows **minimal association**
   with the Yet1p–Yet3p complex and the translocation machinery, and **yet2Δ cells do NOT show
   the inositol prototrophy defect** seen for yet1Δ/yet3Δ. → Yet2p is the outlier: not part of
   the characterized Yet1p–Yet3p complex, stress-inducible, function unknown.

3. **Wilson JD, Barlowe C (2011)** (follow-up), "Yet1p–Yet3p interacts with Scs2p–Opi1p to
   regulate ER localization of the Opi1p repressor", *Mol Biol Cell* (DOI 10.1091/mbc.e10-07-0559).
   Again about the Yet1p–Yet3p complex (phospholipid/inositol INO1 regulation via Opi1p), not
   Yet2p.

4. Mammalian ortholog context (for family reasoning only; do NOT attribute to YET2 as fact):
   - **Human BAP31 = BCAP31 / P51572** (BAP31_HUMAN) — this is the IBA source
     (`UniProtKB:P51572`, PANTHER PTN000294723) for all YET2 phylogenetic annotations. BAP31
     is a cargo/quality-control chaperone and ER-export/retention factor and an apoptosis
     regulator. [PMID:15024066 — human BAP31 regulates ERAD turnover of PTP-like B;
     PMID:31206022 — BAP31–Tom40 at ER–mitochondria interface.] These are ortholog papers,
     not YET2 evidence.

5. **PMID:26928762** (Yofe et al., "One library to make them all: streamlining the creation of
   yeast libraries via a SWAp-Tag strategy", *Nat Methods* 2016) — the HDA source in GOA for
   `endoplasmic reticulum` localization (ECO:0007005). High-throughput C-terminal tagging /
   localization library; supports ER localization of YET2 as an observation, not a functional
   characterization.

## KNOWN vs NOT-known for YET2 (adjudicated)

KNOWN (well supported):
- ER membrane protein, polytopic (3 TM), BAP31 family — domain + HDA localization + IBA + IEA
  all converge. C-terminal di-lysine motif gives a mechanistic basis for ER residence.
- Non-essential; a genetic interaction with YET3 (yet2Δ yet3Δ growth phenotype) exists
  (Toikkanen 2006).
- Stress/UPR-inducible expression (Wilson & Barlowe 2010, full text).

NOT known (genuine gaps):
- **Molecular function**: no catalytic domain; MF = ND in SGD. Whether YET2 acts as a
  cargo-receptor/scaffold (BAP31-like) is inferred from family, never demonstrated for Yet2p.
- **Physiological cargo/client** proteins of Yet2p: undetermined.
- **Mechanism / complex membership**: Yet2p is NOT a stable member of the Yet1p–Yet3p complex
  (Wilson & Barlowe 2010); its own partners are unknown.
- **Biological role & redundancy**: whether YET2 is functionally redundant with YET1/YET3, and
  what unique role (if any) its stress-inducibility serves, is unknown. BP = ND in SGD.
- **Phenotype**: single yet2Δ has no reported strong phenotype (0 hits in 10 CRISPR screens,
  BioGRID-ORCS); the only phenotypic signal is epistatic (yet2Δ yet3Δ).

## Deep research provenance

Falcon deep research was attempted three times (`just deep-research-falcon yeast YET2`,
with a `--fallback perplexity-lite` on the first attempt). All falcon runs hit the 600 s
provider timeout with no output; the perplexity-lite fallback failed with a 401 quota error
("insufficient_quota"). No `YET2-deep-research-*.md` file was produced. This review is
therefore grounded directly in the UniProt record (Q04210), the GOA TSV, and manually
verified cached/primary literature (PMID:20378542 abstract; PMID:26928762; the Toikkanen 2006
naming paper via its DOI/scialert abstract; human ortholog BAP31 = P51572 papers for family
context). No fabricated deep-research content was substituted.

UPDATE: A genuine falcon deep-research file *did* eventually land
(`YET2-deep-research-falcon.md`, 294 lines, 21 citations; the Edison call ran
14:07-14:35 = 1703 s, exceeding the recipe's 600 s timeout so the recipe reported
failure, but the underlying job completed and wrote the file after disk space was
freed). It is retained and cited. Its most valuable YET2-specific content comes from
**Zung et al. 2024** (bioRxiv 10.1101/2024.05.09.593285, "The molecular mechanism of
on-demand sterol biosynthesis at organelle contact sites"): Yet2 is the
**lowest-abundance** yeast BAP31 paralog and, unlike Yet1/Yet3, is **not
constitutively expressed** — the authors argue this means Yet2 is "likely not simply
redundant with the Yet1-Yet3 branch" and "may ... fulfill a different function." This
directly corroborates the paralog-distinction and functional-role knowledge gaps. The
report otherwise documents the well-studied Yet3 (ergosterol/ERGosome scaffold at ER
contact sites) and Yet1-Yet3 (Opi1/inositol regulation) functions — paralog context,
NOT YET2 evidence. (Falcon's table lists Yet3 = YOR152C, which is an error; UniProt and
Toikkanen give Yet3 = YDL072C — the review uses the correct systematic name.) Per
project memory, falcon `file:` quotes are not substring-validated, so the two quotes
used from this file were grep-verified against it before use.

Note on the Toikkanen 2006 reference: DOI 10.3923/jbs.2006.446.456 (J. Biol. Sci. Faisalabad)
is not PubMed-indexed and its full text is not downloadable (the reference validator 403s on
it), so it cannot serve as a formally validated reference nor supply verbatim supporting_text.
Its (thin) YET2-specific content — the YMR040W=YET2 naming and the yet2Δ yet3Δ genetic
interaction — is described in prose in the relevant `review.reason`/knowledge-gap fields, with
formal provenance anchored to the UniProt file (which cites Toikkanen as its Ref. 3 FUNCTION
source) and to PMID:20378542.

## GOA annotation triage (10 annotations)

CC:
- GO:0005789 ER membrane (IBA, is_active_in) → ACCEPT (family + direct localization). Core.
- GO:0005789 ER membrane (IEA, GO_REF:0000044 UniProt-SubCell) → ACCEPT (redundant, correct).
- GO:0005783 ER (IEA, InterPro) → ACCEPT (correct but less specific than membrane).
- GO:0005783 ER (HDA, PMID:26928762) → ACCEPT (experimental localization).
- GO:0016020 membrane (IEA, InterPro) → ACCEPT but non-core (generic parent of ER membrane).

BP (all IBA from mammalian BAP31, or IEA InterPro — family inferences, no YET2 direct evidence):
- GO:0030970 retrograde protein transport, ER to cytosol (IBA) → KEEP_AS_NON_CORE. ERAD
  dislocation role of BAP31; plausible for the family (Yet complex sits at the Sec translocon)
  but never shown for Yet2p. Non-core, family-level inference.
- GO:2000060 positive regulation of ubiquitin-dependent protein catabolic process (IBA) →
  KEEP_AS_NON_CORE. ERAD-regulation inference from BAP31; no YET2 direct evidence.
- GO:0006886 intracellular protein transport (IEA, InterPro) → KEEP_AS_NON_CORE. Generic;
  consistent with the family's ER-export/protein-transport theme (UniProt FUNCTION hedge).

MF/BP root:
- GO:0003674 molecular_function ND (SGD, GO_REF:0000015) → this is the honest "MF unknown"
  placeholder. Keep as the dark-gene signal; action ACCEPT (it correctly records ignorance).
- GO:0008150 biological_process ND (SGD) → likewise ACCEPT (records that BP is uncurated/unknown).

I will NOT REMOVE any experimental annotation on paralog grounds. The IBA BP terms are
family-level inferences from BAP31; I mark them KEEP_AS_NON_CORE rather than REMOVE because they
are biologically plausible for the family and the Yet complex genuinely localizes to the
translocon — but they are not YET2-demonstrated, so they are non-core.

## Core function stance

Only two things are defensible as YET2 core:
1. Localization: integral ER-membrane protein (GO:0005789), scaffolded by 3 TM helices + a
   di-lysine ER-retrieval motif. This is a `locations` fact, not an MF.
2. A *putative* BAP31-family scaffold/adapter mode of action in ER membrane-protein
   homeostasis/transport — but this is inference, not demonstrated, so `core_functions` must
   flag it as such (and the MF is genuinely unknown → knowledge_gaps).

I will keep `core_functions` minimal and honest: one entry anchoring the ER-membrane
localization and the family-inferred (but unproven) role in ER membrane-protein
transport/homeostasis, with explicit deferral of the specific MF to knowledge_gaps.
