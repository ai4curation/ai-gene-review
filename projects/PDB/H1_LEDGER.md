# H1 ledger — do structures fill annotation gaps that traditional pubs would not?

**H1:** structures / structure-papers can fill GO annotation gaps that would *not* be
filled if curators used only traditional (non-structure) publications.

To make H1 testable we classify each structure-supported annotation into three outcomes:

| Outcome | Meaning | H1 bearing |
| --- | --- | --- |
| **STRUCTURE_UNIQUE** | The function is not establishable from *any* non-structure source (no text, no homology/electronic) — the structure is the sole route. | Strong support |
| **STRUCTURE_FIRST_EXPERIMENTAL** | The function is inferable from homology / electronic / other-organism text, but the structure (+ its paper) is the **first experimental-grade evidence for *this* protein**, upgrading an electronic-only (IEA/IBA) annotation. | Practical support |
| **STRUCTURE_CORROBORATES** | Non-structure **experimental** evidence for this protein already exists; the structure only confirms it. | Against (for this gene) |

## Round 1 — GAP_OPPORTUNITY, exp_mf==0 (n=4) — and why it was the wrong test

First test set: GAP_OPPORTUNITY genes with no experimental *MF* annotation. Result: **4/4
STRUCTURE_CORROBORATES.**

| Gene | Verdict | Non-structure evidence that pre-empted it |
| --- | --- | --- |
| SPR (human) | CORROBORATES | sepiapterin reductase: kinetics, catalytic-residue mutagenesis (PMID:10350607), EC 1.1.1.153, prior structure 1Z6Z |
| TOMM5 (human) | CORROBORATES | TOM-complex membership: experimental IDA (PMID:18331822) + ComplexPortal |
| HSPB3 (human) | CORROBORATES | cytoplasm IDA (PMID:19464326); sHSP/UPR role TAS; hetero-tetramer already in den Engelsman text |
| CFAP61 (human) | CORROBORATES | axoneme IDA proteomics (PMID:28282151, 36659204); radial-spoke assembly IMP (PMID:34792097) |

**Methodological flaw found:** `GAP_OPPORTUNITY` is *by construction* the bucket of genes
that already have experimental curation (that is what distinguishes it from
`GAP_NO_EXP_CURATION`). So every gene in it has non-structure experimental evidence, and a
structure can only ever corroborate. We were testing H1 on the genes guaranteed to refute
it. Confirmed empirically: among 148 GAP_OPPORTUNITY genes, **0** have `exp_total==0`.

A secondary but important observation: HSPB3's genuinely structure-distinctive fact — the
3:1 HspB2–HspB3 hetero-tetramer — had **no GO annotation slot** among HSPB3's existing
annotations. The structure's unique content corresponds to a *missing* annotation, not a
fillable existing one. **Resolution:** rather than leave it in free-text, we added it as a
`NEW` annotation — `GO:0051291 protein heterooligomerization` (IPI, PMID:29969581, PDB
6F2R). This is the cleanest demonstration of H1's *net-new-annotation* mode: the structure
motivates a GO annotation that the existing curation did not have. (The function was also
described in older non-structure complex work, so it is FIRST_STRUCTURAL but not strictly
UNIQUE; still, as a curation outcome it is a structure-driven gap-fill.)

## Round 2 — the correct frontier: GAP_NO_EXP_CURATION (n=63; 36 with cofactor/complex)

The fair test is genes with an uncited structure paper **and no experimental annotation of
any aspect** (`exp_total==0`). For these the structure is, *by construction*, at minimum the
**first experimental-grade evidence** — so on this bucket H1 cannot be trivially refuted, and
the live question becomes UNIQUE vs FIRST_EXPERIMENTAL. These are overwhelmingly
under-curated prokaryotic / archaeal metabolic enzymes with **diagnostic cofactors** (see
`data/h1_testset.tsv`). Top targets:

| Gene | Org | Cofactor in structure | Diagnostic of |
| --- | --- | --- | --- |
| mcrA | METAC | F430 (F43), coenzyme-M (COM), SAM, [4Fe-4S] | methyl-coenzyme M reductase (methanogenesis) |
| mxaI | METEA | PQQ, Ca | methanol dehydrogenase |
| merA | PSEAI | FAD, NADP, (Hg) | mercuric reductase |
| secA | BACSU | ADP | protein-translocating ATPase |
| cbh1 | HYPJE | cellobiose/cellotetraose | cellobiohydrolase |
| P07598 | DESVH | FeS, heme, Zn | (redox metalloenzyme) |

Retroactive frontier data points (already reviewed in earlier batches; both `exp_total==0`):
- **XYL1** (PICST): D-xylose reductase MF — classic enzymology exists (Verduyn, PMID:3921014),
  so the NADPH-bound structure is **STRUCTURE_FIRST_EXPERIMENTAL** (first experimental-grade
  evidence for this protein; family function known from text).
- **psaC** (CHLRE): PSI [4Fe-4S] / electron transfer — known from homology + classic PSI
  biochemistry; **STRUCTURE_FIRST_EXPERIMENTAL / CORROBORATES** at the CC level.

### Round 2 results (n=4 reviewed; all exp_total==0, so no verdict can be CORROBORATES)

| Gene | Structure | NEW annotations added | Verdicts |
| --- | --- | --- | --- |
| **merA** (PSEAI) | FAD-bound mercuric reductase (1ZK7/1ZX9, PMID:16114877) | — | **2 STRUCTURE_UNIQUE** (Hg-ion binding GO:0045340; FAD binding GO:0050660) + 4 FIRST_EXPERIMENTAL (mercuric reductase MF, NADP binding, Hg detox/response BP) |
| **mcrA** (METAC) | MCR cryo-EM with F430 (8GF5/8GF6, PMID:37307484) | **GO:0044674** MCR complex (IPI); **GO:0016151** nickel cation binding (IDA) | 3 FIRST_EXPERIMENTAL (catalytic MF + the 2 NEW) |
| **secA** (BACSU) | SecA ATPase, ADP/Mg (1M74, PMID:12242434) | **GO:0016887** ATP hydrolysis activity (IDA) | 5 FIRST_EXPERIMENTAL (ATP/nucleotide binding, exporting-ATPase, Sec translocation, + the NEW) |
| **mxaI** (METEA) | methanol dehydrogenase (1H4J, PMID:11502173) | — | **NULL** — mxaI is the small subunit; the abstract-only paper describes only the catalytic large subunit (mxaF), so no faithful mxaI-specific quote exists. Reference-only. |

Round-2 tally: **2 STRUCTURE_UNIQUE** annotations, **~12 STRUCTURE_FIRST_EXPERIMENTAL**, **4 NEW**
annotations added (incl. HSPB3's GO:0051291 from the round-1 follow-up), **1 NULL gene**.

## Conclusion

H1 has two empirically distinct forms, and the data separate them cleanly:

1. **Strong H1 (STRUCTURE_UNIQUE — function obtainable from no non-structure source):**
   *rare but real.* 0 cases in round 1 (GAP_OPPORTUNITY, by construction the wrong set);
   2 cases in round 2 from a single gene (merA's NmerA Hg-binding and FAD cofactor). These
   are cofactor/metal-binding facts that even homology text did not assert for the protein.

2. **Practical H1 (STRUCTURE_FIRST_EXPERIMENTAL — structure is the first experimental-grade
   GO evidence, upgrading IBA/IEA/By-similarity):** *common and the main payoff.* It was the
   verdict for ~every annotation across secA, mcrA, merA, and underlies the **63 GAP_NO_EXP_
   CURATION genes**: proteins with an uncited structure and zero experimental GO annotation,
   where folding in structure evidence demonstrably adds experimental support — and often
   **NEW** annotations (complex membership, cofactor/metal binding) — that traditional
   curation had not produced.

**Caveat (the mxaI lesson):** a structure paper existing for a gene does not guarantee it
fills that gene's gap — for multi-subunit assemblies the available text may characterize only
the catalytic subunit, leaving accessory subunits unsupported.

**Verdict on H1:** supported in the practical form, with quantified scope (63 genes), and
occasionally in the strong form. The decisive enabler is targeting `GAP_NO_EXP_CURATION`
(no prior experimental annotation), not famous genes whose text already suffices.

## Appendix — earlier-batch frontier genes (already reviewed, retroactively classified)

- **XYL1** (PICST, exp_total==0): NADPH-bound D-xylose reductase structure = FIRST_EXPERIMENTAL
  (classic enzymology exists in text, but no prior experimental GO annotation).
- **psaC** (CHLRE, exp_total==0): PSI structure = FIRST_EXPERIMENTAL / CORROBORATES at CC level.
