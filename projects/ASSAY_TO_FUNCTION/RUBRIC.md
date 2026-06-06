# Readout → annotation rubric (ASSAY_TO_FUNCTION)

A curator-facing rubric for deciding what GO annotation a **convergent
phenotypic readout** licenses. Grounded in the publications-corpus mining (see
[`../ASSAY_TO_FUNCTION.md`](../ASSAY_TO_FUNCTION.md)); machine-readable form in
[`rubric.yaml`](rubric.yaml).

## The core rule

A readout that reports the **state of a process P** (ROS level, caspase
activity, UPR activation, ΔΨm, Ca²⁺, pH, viability…) measures a *downstream
consequence*, not the gene product's molecular activity. So a positive readout
after perturbing gene G licenses **at most**:

- aspect **BP** (or **CC** for organelle-health probes) — **never MF**;
- framing **"response to P" / "regulation of P"** — not a direct effector role;
- default **non-core**.

Promote to **core** only when *independent* evidence (genetics, biochemistry,
structure) places G in the **recognized machinery / sensor set** for P — not
merely as a perturbation that moves the needle.

This is what curators are already doing in the corpus: the same readout yields
`ACCEPT` for the machinery and `KEEP_AS_NON_CORE` / `MARK_AS_OVER_ANNOTATED`
for genes acting indirectly.

## Decision procedure

```
Is the evidence a state/phenotype readout (not a molecular assay of G)?
│
├─ No  → ordinary evidence rules apply (MF/direct annotation may be fine).
│
└─ Yes → 1. Reject any MF term sourced from this readout.
              (Exception: a transcriptional reporter for a bona fide
               DNA-binding TF — MF TF-activity is legitimate.)
         2. Use a "response to P" / "regulation of P" BP term at the
            altitude the readout DIRECTLY reports — not a more distal or
            tissue-specific child.
         3. Is G in the recognized core machinery / sensor set for P?
              ├─ Yes → core annotation OK (ACCEPT).
              └─ No  → KEEP_AS_NON_CORE (or MARK_AS_OVER_ANNOTATED if the
                       gene's real function clearly lies elsewhere).
```

## Quick reference

| Readout class | Licenses | Never | Default | Core only if G is… |
|---|---|---|---|---|
| Apoptosis / caspase | BP | MF | non-core | BCL2 family, caspase, IAP, APAF1, BH3-only |
| Viability / proliferation | BP | MF | non-core | core cell-cycle/division machinery |
| Oxidative stress / ROS | BP | MF | non-core | antioxidant enzyme / redox sensor (SOD, catalase, PRDX, KEAP1-NRF2) |
| Autophagy flux | BP, CC | MF | context | ATG/ULK/BECN1/ATG8 machinery |
| Mito membrane potential | CC, BP | MF | non-core | respiratory chain / import / bioenergetic component |
| UPR / ER stress | BP | MF | non-core | UPR transducer (IRE1/PERK/ATF6/XBP1) or BiP |
| Calcium flux | BP | MF* | non-core | Ca²⁺ channel/pump/sensor (EF-hand) |
| Iron probe | BP | MF | non-core | Fe transporter / Fe-S biogenesis / storage |
| pH probe | BP | MF | non-core | proton pump/transporter |
| Transcriptional reporter | BP, **MF** | — | context | sequence-specific TF / coregulator |

\* Ca²⁺-binding MF (EF-hand) can be justified by independent structural/binding
evidence, not by the imaging readout itself.

## Worked contrasts from the corpus

Each pair shows the **same readout** licensing a core annotation for the
machinery vs. an over-annotation for a gene acting indirectly:

- **Apoptosis:** `BCL2` → *negative regulation of apoptotic process* (ACCEPT)
  vs `Akt1` → *negative regulation of intrinsic apoptotic signaling* (NON_CORE).
- **Proliferation:** `CDK1` → *G2/M transition of mitotic cell cycle* (ACCEPT)
  vs `ACTB` → *positive regulation of cell population proliferation* (OVER_ANNOTATED).
- **ROS:** `TP53` → *positive regulation of ROS metabolic process* (ACCEPT)
  vs `PEX10`/`PEX13` (peroxins) → *cellular response to ROS* (OVER_ANNOTATED).
- **UPR:** `ATF4` → *PERK-mediated UPR* (ACCEPT) vs `HSPA1A` → *ER UPR*
  (NON_CORE); and `IRE1` → *unfolded protein binding* **(MF, OVER_ANNOTATED)** —
  a textbook reporter-driven MF over-call.
- **Autophagy:** `AMBRA1` → *autophagosome assembly* (ACCEPT) vs `ABI2` →
  *mitophagy* (OVER_ANNOTATED).
- **Transcription (the MF exception):** `ATF2`/`ASCL1` → *DNA-binding
  transcription factor activity* (ACCEPT — genuine TFs) vs `AIP` →
  *transcription coactivator activity* (OVER_ANNOTATED).

## Caveat: dedicated signaling ligands (signature vs incidental)

The "phenotypic hub readout ⇒ non-core" rule, and the flagger's
`indirect_ligand` discriminator, **over-fire on dedicated cytokines and growth
factors**. For a gene whose entire biological purpose is to regulate a process
(VEGFA→endothelial proliferation; IL21→B-cell/Tfh responses), the regulated
process is *core* even though it is mechanistically downstream of receptor
signaling. "Cytokine activity" alone is nearly contentless, so the regulated
processes are the informative, identity-defining annotations.

The discriminating axis is therefore **signature vs incidental**, not
ligand-vs-not:

- **Signature** — the process the gene is known/named for, and that loss-of-
  function abolishes → keep core (VEGFA endothelial proliferation; IL21 germinal
  center / Tfh / B-cell responses).
- **Incidental / generic / tissue-specific-secondary / context-dependent** →
  demote (HMGB1→CXCR4 calcium; VEGFA→generic anti-apoptosis; IL21→T-cell
  proliferation is borderline and was deferred to expert review, issue #1418).

Mechanistic directness still matters for the *ligand vs receptor* distinction
(knockout *necessity* ≠ the ligand *directly* performing the process), but it
must not be applied so bluntly that a dedicated cytokine's signature outputs are
stripped to non-core.

## How this was derived

Across 722 thematically-aligned (annotation, source-paper-readout) pairs, the
GO aspect of hub-readout annotations is overwhelmingly BP/CC with ~zero MF
(transcriptional reporters excepted, and there the MF is legitimate). The
distinguishing action is **non-core demotion**, not removal — see the action
and aspect tables in [`../ASSAY_TO_FUNCTION.md`](../ASSAY_TO_FUNCTION.md). The
"core only if in the machinery" discriminator is read directly off the
ACCEPT-vs-downgrade contrasts above.
