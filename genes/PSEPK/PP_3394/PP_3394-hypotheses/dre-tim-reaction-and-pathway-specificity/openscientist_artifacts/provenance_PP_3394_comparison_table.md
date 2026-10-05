# PP_3394 (Q88HG4) reaction/pathway specificity — computed comparison

Provenance for Iteration 1. All values computed from public UniProt/KEGG/PROSITE
records via `requests` + a Needleman–Wunsch (BLOSUM62, gap −8) implementation.

## Sequences compared
| Label | Accession | Locus | Length | Role |
|-------|-----------|-------|--------|------|
| PP3394 | Q88HG4 | PP_3394 | 309 aa | target (uncharacterized HMGL-family) |
| mvaB | Q88H25 | PP_3540 | 299 aa | annotated HMG-CoA lyase (paralog) |
| PaLiuE | Q9I2A0 | PA2011 | 300 aa | **experimentally verified** HMG-CoA lyase (PMID 19459965) |
| hHMGCL | P35914 | — | 325 aa | human HMG-CoA lyase (reference) |
| EcLeuA | P09151 | — | 523 aa | E. coli 2-isopropylmalate synthase (IPMS, condensation) |

## Pairwise % identity (global NW, BLOSUM62)
|        | PP3394 | mvaB | PaLiuE | hHMGCL | EcLeuA |
|--------|--------|------|--------|--------|--------|
| PP3394 | 100.0  | 38.3 | 38.2   | 38.0   | 38.8   |
| mvaB   | 38.3   | 100.0| 78.6   | 58.5   | 37.1   |
| PaLiuE | 38.2   | 78.6 | 100.0  | 57.5   | 38.3   |
| hHMGCL | 38.0   | 58.5 | 57.5   | 100.0  | 34.2   |
| EcLeuA | 38.8   | 37.1 | 38.3   | 34.2   | 100.0  |

**Key:** mvaB↔PaLiuE = 78.6 % (ortholog). PP3394 is ~38 % and *equidistant* to the
HMG-CoA-lyase clade (LiuE/mvaB/human) and to IPMS (LeuA) → superfamily-level only.

## Catalytic residue mapping (human HMGCL numbering → target, via NW)
| Human catalytic residue | PP3394 | mvaB |
|-------------------------|--------|------|
| Arg41 (substrate)       | R (pos12) | R (pos15) |
| Asp42 (metal)           | D (pos13) | D (pos16) |
| His233 (metal)          | H (pos207)| H (pos207)|
| His235 (metal)          | H (pos209)| H (pos209)|
| Cys266 (catalytic acid) | C (pos240)| C (pos240)|
Catalytic core retained in both → both are likely catalytically competent DRE-TIM metallolyases.

## Diagnostic PROSITE active-site signatures (computed regex match)
| Pattern | Meaning | PP3394 | mvaB | PaLiuE | hHMGCL | EcLeuA |
|---------|---------|--------|------|--------|--------|--------|
| PS01062 `SVAGLGGCPY` | **HMG-CoA lyase** active site | ✗ no match | ✓ @233 | ✓ @233 | ✓ @259 | ✗ |
| PS00815 `LR[DE]G.Q..{4}[^L]..{5}K` | **IPMS/homocitrate synthase** site-1 | ✓ @11 | ✗ | ✗ | ✗ | ✓ @12 |
| PS00816 `[LIVMFW]..HxH[DN]DxGx[GAS]x[GASLI]` | IPMS/HCS site-2 | ✗ | ✗ | ✗ | ✗ | ✓ @199 |

**Interpretation:** PP_3394 fails the HMG-CoA-lyase-specific signature that all three bona
fide HMG-CoA lyases pass, and instead matches the IPMS/HCS family site-1 signature (like
IPMS). N-terminal motif: PP_3394 has condensation-type `GLRDGLQ` (LRDG) vs HMG-CoA-lyase
`(G)PRDGLQ` (PRDG). But PP_3394 lacks IPMS/HCS site-2 and the C-terminal regulatory domain
(only 309 aa, single TIM barrel) → cannot be assigned as canonical IPMS/HCS either.

## Genomic context (KEGG)
- Leucine/isovalerate operon PP_4063–PP_4068 = acyl-CoA ligase, ivd (PP_4064), mccB
  (PP_4065), liuC (PP_4066), mccA (PP_4067) — **no internal HMG-CoA lyase gene**.
- PP_3394 and PP_3540/mvaB are dispersed; KEGG maps **both** to K01640 (EC 4.1.3.4) and to
  leucine-degradation module M00036 → paralog over-annotation.

## Phylogenetic placement (Iteration 2) — Neighbor-Joining, 9-member DRE-TIM panel
p-distance = 1 − global-NW fractional identity. Panel adds subfamily references:
BsHMGL (B. subtilis HMG-CoA lyase O34873), EcIPMS (P09151), ScHCS (homocitrate synthase
P48570), MjCimA (citramalate synthase Q58787), DmpG (4-hydroxy-2-oxovalerate aldolase P51016).

NJ Newick:
```
((PP3394:0.307,(BsHMGL:0.267,(hHMGCL:0.220,(mvaB:0.113,PaLiuE:0.101):0.092):0.066):0.041):0.015,
 ((EcIPMS:0.274,DmpG:0.368):0.040,(ScHCS:0.348,MjCimA:0.280):0.031):0.015);
```
- Two clades: **(A) HMG-CoA-lyase clade** {PP3394, BsHMGL, hHMGCL, mvaB, PaLiuE};
  **(B) condensation/aldolase clade** {EcIPMS, DmpG, ScHCS, MjCimA}.
- **PP_3394 falls inside clade A (HMG-CoA-lyase fold) but as the deepest, longest branch**
  (0.307 vs mvaB 0.113); ~38% identity to all clade-A members. Placement is tentative
  (long branch / possible long-branch attraction).
- **Implication:** whole-sequence phylogeny does NOT group PP_3394 with the condensation
  synthases (IPMS/HCS/CimA), so the seed's "acyl-transfer/condensation" alternative is
  phylogenetically disfavored. PP_3394 is an HMG-CoA-lyase-fold enzyme, but a divergent one
  whose HMG-CoA-lyase-specific active-site motif (PS01062) is degraded → substrate
  specificity remains unresolved.

## Bottom line
- Physiological leucine/terpene HMG-CoA lyase (LiuE role) = **mvaB / PP_3540** (78.6 % to
  characterized LiuE; carries PS01062).
- **PP_3394 = divergent DRE-TIM metallolyase of unresolved substrate specificity**; its
  HMG-CoA-lyase / leucine-catabolism annotation is likely over-annotation. "Ketone body
  biosynthesis" is a mammalian concept and is not appropriate for P. putida.
