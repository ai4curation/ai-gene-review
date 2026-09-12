# AP1S3 bioinformatics: which sigma subunit do the two AP-1 structure papers describe?

Reproduce with `uv run python sigma_site_check.py` from this directory. Sequences are
fetched live from the UniProt REST API at run time; nothing is hardcoded, and the script
exits non-zero if any asserted position fails to resolve.

## Question

Two structural papers describe an AP-1 "sigma" chain purely by residue number:

- PMID:36261523 (Liu et al., Nature 2022; PDB 7R4H, 2.34 A cryo-EM) reports that the AP-1
  sigma subunit contacts the phosphorylated STING C-terminal tail.
- PMID:40752490 (Wang et al., Structure 2025; PDB 9DDT, 1.68 A X-ray) reports the AAGAB
  pseudoGTPase domain bound to "AP1sigma3".

Human has three interchangeable AP-1 sigma-1 paralogues (AP1S1/sigma-1A, AP1S2/sigma-1B,
AP1S3/sigma-1C) plus the AP-2 sigma (AP2S1). Residue numbers alone are therefore not
self-identifying. The test below asks (1) whether the published positions resolve in
AP1S3 (Q96PC3) numbering, and (2) whether they would resolve equally well in a paralogue,
i.e. whether numbering can discriminate at all.

## Results

Sequence lengths fetched live and asserted before scoring: Q96PC3 154 aa, P61966 158 aa,
P56377 157 aa, P53680 142 aa.

**Test 1 — 22 of 23 published positions resolve to exactly the residue named, in AP1S3's
own numbering.**

| Source | Site | AP1S3 residue | Result |
|---|---|---|---|
| PMID:36261523 | K60, R61 | K, R | match (phospho-S366 contacts) |
| PMID:36261523 | L65, F67, H85, V88, V98 | L, F, H, V, V | match (EXXXLI hydrophobic pockets) |
| PMID:36261523 | I103 | I | match (dileucine recognition) |
| PMID:40752490 | R10, K13, L40, S41, R61, Y62, A63, V88, V98, L101, Q124, R154 | all as named | match |
| PMID:40752490 | L104 | **I104** | **mismatch** |
| PMID:24791904 | F4, R33 | F, R | match (PSORS15 variants) |

The single mismatch is real and is reported rather than smoothed over: PMID:40752490 states
that AAGAB A168 makes hydrophobic contacts with "AP1sigma3 L101 and L104", but position 104
is isoleucine in AP1S3 **and** in AP1S1 (AP1S2 has F104, AP2S1 has V104). No AP-1 sigma
paralogue carries leucine there, so this is most consistent with a single-letter slip for
I104; the contact described (a hydrophobic packing interaction) is unaffected, since Ile and
Leu are isosteric in that role. It is recorded here so that no downstream claim rests on a
leucine that does not exist.

**Test 2 — the numbering does not by itself discriminate AP1S3 from AP1S1.**

Of the 22 verified AP1S3 sites, AP1S1 (sigma-1A) carries the identical residue at the
identical integer position at 20/22. Only two sites discriminate: AP1S3 S41 (AP1S1 has A41)
and AP1S3 R154 (AP1S1 has E154 and runs to 158). AP1S2 agrees at only 1/22 same-position
sites because a one-residue offset shifts its numbering, yet at the *aligned* positions it
agrees at 20/22 — the site is conserved, the numbering is not. AP2S1 agrees at 15/22.

Consequently the sigma identity in each paper is established not by the numbering but by
three independent facts:

1. PMID:40752490 states its construct explicitly: "Full-length human AP1S3 (Uniprot
   Q96PC3-1)".
2. PMID:36261523's construct is "AP-1sigma 1-154", and 154 is AP1S3's full length (AP1S1 is
   158, AP1S2 157, AP2S1 142).
3. PDBe SIFTS maps 7R4H chain S and 9DDT chain B to Q96PC3 (AP1S3) residues 1-154.

Two of AP1S3's discriminating sites are cited by PMID:40752490 (S41 in the AAGAB interface;
R154 as the last residue of the C-terminal helix Q124-R154 that is unmodelled in 9DDT), which
independently confirms AP1S3 numbering for that structure.

**A caveat that this analysis establishes, and that matters for annotation.** The
cell-based mutagenesis in PMID:36261523 (Fig. 4g: sigma-KR K60A/R61A, sigma V88D, sigma I103S)
was performed on a **pCDNA3-HA-AP1S1** construct, per that paper's Plasmids section — not on
AP1S3. Because V88 and I103 are the same residues at the same positions in both paralogues
(this analysis), those cellular results bear on the shared sigma site, but they are
loss-of-function data on AP1S1, not on AP1S3. AP1S3's own evidence in that paper is the
structure (chain S of 7R4H).

**Test 3 — pairwise identity to AP1S3:** AP1S1 68.8%, AP1S2 72.1%, AP2S1 44.4% (BLOSUM62
global alignment, identities over the shorter sequence).

## Interpretation

The cargo-facing surface of AP1S3 is intact and structurally characterised at 1.68-2.34 A:
the hydrophobic pockets that receive the two bulky residues of a `[DE]XXXL[LI]` sorting
motif (L65, F67, H85, V88, V98, I103) and the basic pair (K60, R61) that reads a
phosphoserine immediately C-terminal to the motif. The same V88/V98 pocket is the site the
assembly chaperone AAGAB occupies before the complex is built, so cargo binding and
chaperone binding are mutually exclusive on this subunit.

Both PSORS15 variants sit outside that cargo surface: F4 in the hydrophobic core (folding)
and R33 at the sigma/mu1A interface (assembly), consistent with both being reported as
destabilising rather than cargo-selective.
