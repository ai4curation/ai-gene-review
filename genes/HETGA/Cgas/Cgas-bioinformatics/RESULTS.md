# Naked mole-rat cGAS (A0AAX6RS70): conservation of catalytic and chromatin-binding residues

## Why this analysis was run

Every GO annotation on naked mole-rat cGAS is a TreeGrafter propagation from the
PANTHER ancestral node `PTN000069395` (`GO_REF:0000118`); there is no experimental
GO annotation on this protein. Two of the propagated claims needed independent
checking before they could be accepted or rejected:

1. **2',3'-cyclic GMP-AMP synthase activity (GO:0061501)** — is the catalytic
   machinery intact in the naked mole-rat protein, or has it degenerated?
2. **negative regulation of DSB repair via homologous recombination (GO:2000042)** —
   the primary literature reports that the naked mole-rat protein has *lost* this
   suppressive activity through changes at four amino acids, but the abstract does
   not name the residues. Can the reported positions be located and checked?

## Method

`align_cgas.py` performs a global Needleman-Wunsch alignment (BLOSUM62,
gap open -11, extend -1, free end gaps) of naked mole-rat cGAS (UniProt
A0AAX6RS70, 554 aa) against human cGAS (Q8N884, 522 aa) and mouse cGAS
(Q8C6L5, 507 aa). It then parses every `ACT_SITE`, `BINDING`, and `SITE` feature
out of the reference UniProt flat files and transfers each position through the
alignment, reporting whether the naked mole-rat residue is identical or
substituted. No residue identity is hardcoded; all come from the records in
`data/`.

Reproduce with:

```bash
uv run python align_cgas.py
```

Full output is in `alignment_output.txt`.

## Result 1: the catalytic core is fully intact

Global identity to human cGAS is 58.2% over aligned columns (55.2% to mouse) —
ordinary orthologue-level divergence. Every catalytically important residue that
UniProt annotates on human cGAS is present and identical in the naked mole-rat
protein:

| function | human | mouse | naked mole-rat | conserved |
|---|---|---|---|---|
| catalytic Mg(2+) / ATP | E225 | E211 | **E257** | yes |
| catalytic Mg(2+) / 2',3'-cGAMP | D227 | D213 | **D259** | yes |
| catalytic Mg(2+) / GTP / 2',3'-cGAMP | D319 | D307 | **D351** | yes |
| 2',3'-cGAMP binding | K362 | K350 | **K394** | yes |
| 2',3'-cGAMP binding | R376 | — | **R408** | yes |
| Zn(2+) thumb | H390 | H378 | **H422** | yes |
| Zn(2+) thumb | C396 | C384 | **C428** | yes |
| Zn(2+) thumb | C397 | C385 | **C429** | yes |
| Zn(2+) thumb | C404 | C392 | **C436** | yes |
| ATP binding | S213 / K414 | S199 / K402 | **S245 / K446** | yes |
| nucleosome acidic-patch arginine anchor | R255 | R241 | **R287** | yes |

Against the human record, 12 of 15 annotated single-residue sites are identical
and 0 are gapped. The three substitutions are **not** catalytic: human T211
(GTP contact) → A243, and human K187/L195, which UniProt annotates as
"important for preferential detection of curved long DNA", → N220/Q228 in the
disordered/DNA-binding N-terminal arm, the least conserved part of the protein
in any mammalian comparison. Against the mouse record, 13 of 14 sites are
identical (only the same T→A).

**Interpretation.** The nucleotidyltransferase triad, the zinc thumb that
recognises B-form dsDNA, and the ATP/GTP/cGAMP contacts are all retained. There
is no pseudoenzyme signature. The catalytic-domain-level block identities are
also normal (62.5% over the C-terminal DNA-binding region 384-407; 69.0% over
341-382). Nothing in the sequence argues against the propagated
2',3'-cGAMP synthase activity, dsDNA binding, or nucleosome/chromatin binding.
The conserved arginine anchor (R287) is particularly relevant: this is the
residue that docks cGAS onto the nucleosome acidic patch, and its retention is
consistent with the reported chromatin retention of the naked mole-rat protein.

## Result 2: the four divergent residues are C-terminal and regulatory, not catalytic

Chen et al. 2025 (PMID:41066557) state in the abstract only that the loss of HR
suppression happens "through the alteration of four amino acids during
evolution", without naming them. Secondary coverage of the paper names the four
substitutions as S463D, E511K, Y527L, T530K but does not state the numbering
frame. This analysis resolves that frame from sequence alone.

Reading the positions in **naked mole-rat numbering** gives an exact match to
the reported wild-type residues, and the aligned human and mouse residues are
exactly the mutant residues reported:

| naked mole-rat | aligned human | aligned mouse |
|---|---|---|
| S463 | D431 | D416 |
| E511 | K479 | K464 |
| Y527 | L495 | L480 |
| T530 | K498 | R483 |

So "S463D, E511K, Y527L, T530K" is a **humanising** substitution series applied
to the naked mole-rat protein: each mutation replaces the naked mole-rat residue
with the residue found at the aligned position in human (and, for three of four,
mouse) cGAS. This is internally consistent with the abstract's account of four
amino acids altered during evolution, and it was confirmed here from primary
sequence data rather than taken on trust from the secondary summary.

All four positions fall inside the C-terminal Mab-21-like HhH/H2TH-like domain
that UniProt annotates at 437-541 on A0AAX6RS70. All four are downstream of the
zinc thumb (422-436) and far from the catalytic triad (257/259/351).

**Interpretation.** The divergence that reverses the HR phenotype sits in a
C-terminal regulatory surface, not in the active site. This supports treating
the naked mole-rat protein as an enzyme with conserved catalysis whose
*regulatory* behaviour on chromatin has changed — consistent with the reported
mechanism (weakened TRIM41-mediated ubiquitination and weakened p97 interaction,
hence longer chromatin retention) — rather than as a protein that has lost or
swapped its molecular function.

## Limits

- This is a sequence-level argument. It shows the machinery for cGAMP synthesis
  is present; it does not demonstrate that the naked mole-rat enzyme actually
  produces cGAMP, and no naked mole-rat biochemical assay of cGAMP synthesis was
  found in the cached literature.
- Likewise it says nothing about whether downstream STING signalling and type I
  interferon induction are intact in this species.
- The residue-position check in Result 2 validates the *numbering frame and
  residue identities* of a secondary summary. It does not independently confirm
  the functional claim attached to those mutations, which rests on
  PMID:41066557.
- UniProt binding-site features on the human and mouse records are themselves a
  mix of experimental and inferred annotations; they are used here as a
  reference frame, not as independent evidence.
