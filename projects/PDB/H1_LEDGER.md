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
it. Confirmed empirically: among 145 GAP_OPPORTUNITY genes, **0** have `exp_total==0`.

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

## Refinement: informativeness, and the three evidence layers of a structure paper

A structure paper is not one evidence unit but three, and they fill very different
annotation classes:

| Layer | What it is | GO terms it yields | Informative? | H1 status in our data |
| --- | --- | --- | --- | --- |
| **1. Model / coordinates** | bound cofactor, metal, fold, geometry, oligomeric state | "X binding", "metal ion binding", "ATP hydrolysis activity", "protein-containing complex", "heterooligomerization" | **No** — low information content; the same class the project guidelines tell us to avoid (cf. "protein binding") | This is where the STRUCTURE_UNIQUE / NEW wins concentrated (merA Hg & FAD binding; mcrA Ni binding; secA ATP hydrolysis; HSPB3 heterooligomerization) — i.e. structures uniquely fill the *least useful* slots |
| **2. The paper's integrative functional hypothesis** | structure **+** assays + mutagenesis + biological context → a specific mechanism/role | informative, specific function/mechanism | **Yes** | merA: NmerA "acquisition and delivery of Hg2+ to the catalytic core" (a metallochaperone-type role); secA: ATPase "mediates extrusion … based on cycles of reversible binding to the SecYEG translocon"; mcrA: "a model for the assembly of the MCR complex and the role of McrD" |
| **3. Specific catalytic identity (EC/family)** | rides on **sequence**, not coordinates | the defining MF (mercuric reductase, methyl-CoM reductase) | Yes | Already given by EC/Pfam/homology; structure only *confirms* it → FIRST_EXPERIMENTAL, never UNIQUE |

**Consequences for H1.**
- The *structure-demonstrated facts* (Layer 1) are low-information; the *informative function*
  (Layer 3) is sequence-borne and merely confirmed. So "structure alone" looks weak.
- The real informative gap-filling lives in **Layer 2 — the paper's structurally-grounded
  hypothesis** — which is *stronger than the coordinates alone prove but consistent with them*.
  Our exact-substring extraction leaned on Layer 1 (cofactor facts), so it **systematically
  under-counted** the value that lives in Layer 2.

**Curation posture for Layer 2 (the integrity guardrail).** A Layer-2 claim is
structure-*enabled inference*, not structure-*demonstrated fact*. It should be: (a) annotated to
the more informative term; (b) attributed to the authors' model and quoted as their claim
(`supporting_text` = the hypothesis sentence); (c) given a confidence-aware stance (author-
statement-like, or a `proposed`/hedged annotation) rather than laundered as a hard IDA from the
model. The distinction "demonstrated by the structure" vs "proposed by the authors on the basis
of the structure" must be preserved.

**Open test (Layer 2 rate):** re-read each frontier structure paper for its single headline
functional hypothesis and classify it on three axes — informative? · beyond coordinates? ·
already in prior text/EC vs paper-unique? The Layer-2 informative-gap-fill rate is the honest
measure of H1's value, and it is almost certainly higher than the ~0 Layer-1 rate but lower
than the raw FIRST_EXPERIMENTAL count.

## Layer-2 pass: scoring the papers' headline functional hypotheses

For each frontier paper we read its single headline functional hypothesis (Layer 2) and
scored it: *informative?* · *beyond coordinates?* · *paper-unique for THIS protein?* ·
*expressible as a GO term?*

| Gene | Paper's headline hypothesis (Layer 2) | Informative | Beyond coords | Unique (this protein) | GO-expressible | Net |
| --- | --- | --- | --- | --- | --- | --- |
| **merA** | NmerA scavenges Hg²⁺ from proteins and **delivers it to the catalytic core**; cytoprotective under glutathione depletion (metallochaperone-type role) | Yes | Yes (Hg-transfer + cell-protection assays) | **Yes** — NmerA was "of uncertain function" | Partial (detox BP yes; delivery MF has no good term) | **Layer-2 gap-fill** |
| **secA** | ATP/ADP binding gates an interdomain conformational cycle that drives extrusion of preprotein N-termini through SecYEG | Yes | Yes (two structures + fluorescence anisotropy) | Partial — SecA-as-translocation-ATPase already known; gated-cycle model refined | Yes, at process level (already broadly annotated) | Marginal (mostly prior) |
| **mcrA** | McrD binds asymmetrically, improving active-site fidelity; model for MCR assembly | hypothesis is about **McrD**, not mcrA | — | targets a different subunit | — | **NULL for mcrA** |
| **mxaI** | MDH catalytic mechanism (Asp303 base / Ca / PQQ) | about the large subunit **mxaF**, not mxaI | — | targets a different subunit | — | **NULL for mxaI** |
| **psaC** | antenna arrangement and energy-transfer pathways of the PSI-LHCI supercomplex | about the **LHC antenna**, not psaC | — | targets different proteins | — | **NULL for psaC** |
| **XYL1** | NADPH binding drives an open/closed conformational change; substrate-pocket determinants of specificity | a *mechanism*, not a new function | borderline (apo/holo comparison) | function already known (enzymology) | mechanism is not a GO term | **NULL (no new informative MF)** |

**Layer-2 informative-gap-fill rate: ~1 of 6 clear (merA), 1 marginal (secA), 4 null.** Even
crediting the papers' broader, structurally-grounded hypotheses — not just the coordinates —
the rate stays low.

**Meta-finding (compounds the mxaI lesson):** for multi-subunit / supercomplex structures the
paper's headline hypothesis frequently concerns a **different subunit** than the gene of
interest (mcrA paper → McrD; mxaI paper → mxaF; psaC paper → LHC antenna). So Layer-2 value
often misses the target protein entirely.

**Two independent throttles on Layer 2**, both visible here:
1. *Subunit mismatch* — the informative hypothesis is about a partner subunit (3 of 6).
2. *GO expressivity* — even the one genuine win (merA) states an informative function ("delivers
   Hg²⁺ to the catalytic core") with **no precise GO MF term**; it can only be banked as a
   `proposed_new_term` (added to the merA review) plus the expressible detox BP.

**Net on H1, all layers considered:** structures-via-papers reliably supply *first experimental
evidence* for under-curated proteins (common), but **new informative function is rare** — it
needs the paper's Layer-2 hypothesis to (a) concern the target protein, (b) state a specific
function, and (c) have a GO term to land in. In our frontier sample that conjunction held cleanly
once (merA), partly via a proposed new term.

## Appendix — earlier-batch frontier genes (already reviewed, retroactively classified)

- **XYL1** (PICST, exp_total==0): NADPH-bound D-xylose reductase structure = FIRST_EXPERIMENTAL
  (classic enzymology exists in text, but no prior experimental GO annotation).
- **psaC** (CHLRE, exp_total==0): PSI structure = FIRST_EXPERIMENTAL / CORROBORATES at CC level.
