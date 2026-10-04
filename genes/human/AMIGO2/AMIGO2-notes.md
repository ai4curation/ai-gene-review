# AMIGO2 (Q86SJ2) review notes

## 2026-10-04: PAINT/affinage review

AMIGO2 is an AMIGO-family adhesion protein and a PDK1 membrane scaffold.
- **PDK1 binding, human endothelial cells (HUVEC):** [PMID:26553931 "Amino acid residues 465-474 in AMIGO2 directly bind to the PDK1 pleckstrin homology domain."]
- **Binding is direct**, shown with purified proteins: "His-PDK1PH proteins, but not His-PDK1kinase, could bind to GST-AMIGO2CD under cell-free conditions".

Decisions:
- **NEW GO:0019901 protein kinase binding (IDA, PMID:26553931).**
  - AMIGO2's own cytoplasmic residues make the contact.
  - I chose a binding term rather than an adaptor or Akt-pathway process term because the evidence is one study. The Akt role is recorded as a BP_DARK gap.
- **Plasma membrane, membrane and the adhesion rows (ISS/IBA from rat): ACCEPT.**
- **Kept as non-core:** nucleus (IEA, by similarity only), brain development (IBA), and negative regulation of programmed cell death (ISS from mouse Alivin 1, supported in HUVEC).
- **REMOVE:** two protein-binding rows (CACNA1A from an ataxia Y2H screen; TMED8 from HuRI).
