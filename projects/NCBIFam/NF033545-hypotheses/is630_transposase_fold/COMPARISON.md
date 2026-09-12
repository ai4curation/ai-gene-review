# Blinded comparison — IS630 transposase NF033545 / P16943

Holdout (before run) vs `openscientist.md`. Grounds the seed's single biggest
net-new headline (18,874). Run completed on the 3rd attempt after a transient
ConnectError then a 7200s timeout; narrowing to a Foldseek-only question at
max_iterations=2 finished in 798.5s.

## Verdict: CONFIRMED (high confidence), matches holdout exactly

- **Fold:** RNase H-like / retroviral-integrase **DDE transposase-integrase fold**.
  Foldseek top hits (PDB100 + AFDB-SwissProt) are ALL characterized DDE
  transposases — Mos1 mariner (5hoo/4r79/3hot, E to 1e-11, prob 1.0), Sleeping
  Beauty (5cr4), Hsmar1/SETMAR (3f2k), Tc3, IstA, IS3 InsF. No competing fold.
- **Active site:** intact **DDE triad D181 / D261 / E297** in two-metal RNase-H
  geometry (D181–D261 5.9 Å; E297–D181 6.2 Å; pLDDT 92–96); **DD(34)E** spacing
  characteristic of the mariner/IS630 superfamily.
- **Verdict:** transposase activity (**GO:0004803**) structurally supported;
  "uncharacterized" is a curation artifact (no wet-lab on this specific protein),
  not biological ambiguity.

Matches the holdout (genuine DDE transposase, intact triad).

## Curation consequence

NF033545 → GO:0004803 mapping **CONFIRMED**; the 18,874 net-new gain is grounded
(the equivalog HMM's core is a genuine transposase), and the 2 reviewed
"uncharacterized" entries (P16943 among them) are sound gap-fills. One caveat from
the holdout stands: IS elements frequently carry **defective/truncated copies**, so
a production ncbifam2go propagation over the TrEMBL tail should ideally apply an
"intact-DDE-triad" filter rather than blanket-propagating to every signature hit.

## Literature note
Foldseek/structural evidence only (no cached PMIDs needed); the template PDB ids
(5hoo, 4r79, 5cr4, 3f2k, ...) are checkable and the call is sound.
