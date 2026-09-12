# cms1 (SPBC23G7.07c, UniProt O94465) — curation notes

Fission yeast (*Schizosaccharomyces pombe*) gene, systematic name SPBC23G7.07c, standard name **cms1**.
Understudied ("dark") gene. This journal records what is KNOWN vs NOT-known, with inline provenance.

> Provenance note on deep research: the automated deep-research harness (`deep_research_wrapper.py`
> SCHPO cms1 falcon --fallback perplexity-lite`, and `just deep-research-falcon`) hung and timed out
> (>550s, exit 124/no output) on two attempts and produced no report file. Per project guidance, this
> review is therefore grounded directly in the UniProt record, the QuickGO GOA TSV, the PomBase gene
> record (JSON API), the InterPro/PANTHER family data (PTHR24030), and the cached primary literature on
> the S. cerevisiae ortholog (publications/PMID_36417864.md). No `-deep-research-*.md` file was
> fabricated.

## Identity and domain reasoning (from cms1-uniprot.txt, InterPro, PomBase)

- 277 aa protein, MW ~31.6 kDa. UniProt evidence level **PE 3 (Inferred from homology)** — i.e. no
  direct protein-level experimental evidence for the *S. pombe* protein itself.
- UniProt RecName is simply "Protein cms1"; the only functional statements are inferred:
  - FUNCTION: "May play a role in the regulation of DNA replication and cell cycle control." {ECO:0000250}
    (this is a legacy homology inference derived from the budding-yeast *CMS1* high-copy-suppressor-of-*MCM10*
    history, NOT from any 90S ribosome work; see below).
  - SUBCELLULAR LOCATION: Nucleus {ECO:0000250} (by similarity).
  - SIMILARITY: "Belongs to the CMS1 family." {ECO:0000305}.
- Domain/family signatures: Pfam **PF14617 (CMS1)**, InterPro **IPR032704 (Cms1)**, PANTHER **PTHR24030
  / PTHR24030:SF0 (PROTEIN CMSS1)**. No catalytic-domain signature (no kinase, no methyltransferase,
  no active nuclease). The Pfam CMS1 domain corresponds to a degenerate/inactive helicase-like fold
  (see Lau et al. 2022 below).
- Sequence features (UniProt FT): a disordered region 28-68, with a polar-residue compositional bias
  (33-49) and a **basic-residue compositional bias (53-68)** — the stretch `KREKRKKQRQKQKERKRAK`. A basic
  disordered patch of this kind is a plausible (but unproven) nucleic-acid-contacting element, consistent
  with an RNP/ribosome-biogenesis context, but is not by itself an annotatable molecular function.
- PANTHER family PTHR24030 (interpro/panther/PTHR24030) is conserved from fungi to vertebrates; reviewed
  members include *S. cerevisiae* CMS1 (Q07897), human **CMSS1** (Q9BQ75, "Cms1 ribosomal small subunit
  homolog"), mouse/rat/zebrafish/Xenopus Cmss1, and *Thermochaetoides thermophila* CMS1. So cms1 is a
  genuinely conserved single-copy family member — unlike lineage-restricted orphans.

## PomBase-specific facts (PomBase API, gene SPBC23G7.07c)

- PomBase product name: **"U3-containing 90S preribosome complex subunit Cms1"**.
- PomBase `characterisation_status`: **"biological role inferred"** — i.e. the pombe gene's role is
  inferred (from orthology), not directly demonstrated in *S. pombe*.
- GO annotations in PomBase mirror the GOA TSV: MF = ND (root, no data); BP = ribosomal small subunit
  biogenesis (GO:0042274); CC = 90S preribosome (GO:0030686) + nucleus (GO:0005634). All functional
  terms are ISO transfers from *S. cerevisiae* CMS1 (SGD:S000003993).
- Deletion phenotype: PomBase records a single-locus phenotype **FYPO:0002060 "viable vegetative cell
  population"** — cms1Δ is viable (non-essential), consistent with *S. cerevisiae* (below). Other
  phenotype terms are high-throughput deletion-collection screen hits (e.g. FYPO:0003743 "decreased
  cell population growth during glucose starvation"; FYPO:0001701 "sensitive to bortezomib";
  FYPO:0000763 "resistance to cadmium") — these are pleiotropic screen signals, not core-function-defining.

## Ortholog evidence — the source of the ISO annotations

The ISO annotations are transferred from the *S. cerevisiae* ortholog **CMS1** (SGD:S000003993, Q07897).
The most informative primary study of that ortholog:

**Lau B, Beine-Golovchuk O, Kornprobst M, Cheng J, Kressler D, Jády B, Kiss T, Beckmann R, Hurt E.
"Cms1 coordinates stepwise local 90S pre-ribosome assembly with timely snR83 release." Cell Rep. 2022;
41(8):111684. PMID:36417864** (full text cached in publications/PMID_36417864.md). This paper is entirely
about *S. cerevisiae* Cms1 (no *S. pombe* data — grep found 0 "pombe" mentions), so it grounds the ORTHOLOG.

Key verbatim-supported facts about *S. cerevisiae* Cms1:
- It is a bona fide **90S pre-ribosome (small subunit processome) assembly factor**:
  [PMID:36417864 "CMS1 encodes a poorly characterized but conserved protein (human homolog CMSS1; Figure S2A)
  that was initially found as a high-copy suppressor of MCM10 (Wang and Wu, 2001). However, based on other
  analyses, it was implicated in 90S ribosome biogenesis"].
- It is **conserved** with a human homolog CMSS1:
  [PMID:36417864 "Notably, both a human Cms1 (CMSS1; Figure S2A) and an snR83 homolog (called ACA4) exist"].
- It is **nonessential**:
  [PMID:36417864 "... vulnerable mutations in Noc4 module subunits or in the Bms1-Rcl1 heterodimer can be
  suppressed by disrupting CMS1 or NOP6, which both are nonessential factors implicated in the early 90S
  assembly pathway"].
- It localizes to the 18S rRNA 3' major domain of an early 90S carrying the H/ACA snoRNA snR83 and
  coordinates local assembly with timely snR83 release (abstract).
- Proposed molecular activity is speculative/inactive-helicase-based RNA binding, NOT demonstrated:
  [PMID:36417864 "Via its inactive helicase domain, Cms1 might exert a specific RNA-binding activity toward
  the H32-34 region of the 3′-major domain, thereby competing with Enp1-Rrp12 binding at a related site"].
  Note the hedging ("inactive helicase domain", "might exert") — no catalytic activity; MF remains open.

## KNOWN vs NOT-known for *S. pombe* cms1

KNOWN (well-supported, chiefly by orthology to a strongly characterized budding-yeast factor):
- Member of the conserved CMS1/CMSS1 family (Pfam PF14617; PANTHER PTHR24030), single-copy, fungi→human.
- By orthology, a nucleolar **90S pre-ribosome / small-subunit-processome assembly factor** involved in
  **ribosomal small subunit (18S rRNA) biogenesis**; localizes to the nucleus.
- Non-essential in *S. pombe* (cms1Δ viable, FYPO:0002060) — matching *S. cerevisiae*.

NOT-known (genuine gaps for the pombe protein):
- No direct experimental characterization of the *S. pombe* protein exists (PE 3; "biological role
  inferred"). All functional GO terms are ISO transfers.
- **Molecular function is dark.** No catalytic activity; the only proposed activity (RNA binding via a
  degenerate/inactive helicase fold) is a hypothesis even for the budding-yeast ortholog and has not been
  biochemically demonstrated in any species. The basic disordered patch (53-68) is a candidate
  nucleic-acid contact but unproven.
- The legacy UniProt FUNCTION line ("regulation of DNA replication and cell cycle control", by similarity)
  reflects the historical *MCM10* high-copy-suppressor origin of budding-yeast CMS1 and is superseded by
  the 90S-ribosome-biogenesis role; it is not independently supported as a *core* function.

## Curation decisions (summary; see cms1-ai-review.yaml)

- GO:0042274 ribosomal small subunit biogenesis (BP, ISO) — ACCEPT (core; ortholog strongly supports).
- GO:0030686 90S preribosome (CC, ISO, part_of) — ACCEPT (core; the defining complex).
- GO:0005634 nucleus (CC, ISO, is_active_in) — ACCEPT as location (specific compartment is nucleolar,
  but nucleus is defensible and consistent).
- GO:0005634 nucleus (CC, IEA, located_in, GO_REF:0000044 SubCell) — KEEP_AS_NON_CORE (redundant IEA
  duplicate of the ISO nuclear call; location, not core function).
- GO:0003674 molecular_function (ND) — ACCEPT (honestly reflects that MF is genuinely unknown; do not
  invent an MF).

Core-function synthesis: cms1 is best represented as an accessory subunit of the 90S preribosome acting in
small-subunit biogenesis in the nucleus, with NO assertable molecular function (MF-dark). This is recorded
as a knowledge gap.
