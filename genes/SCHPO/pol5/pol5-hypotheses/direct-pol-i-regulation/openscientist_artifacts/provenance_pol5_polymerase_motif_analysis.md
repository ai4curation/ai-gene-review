# Pol5 family-B DNA polymerase catalytic-motif analysis (computed, Iteration 2)

**Goal:** Test at the sequence level whether *S. pombe* Pol5 (O60094) retains a functional
family-B DNA polymerase active site — a prerequisite for any "polymerase"/direct-transcription framing.

**Method:** Retrieved UniProt sequences for *S. pombe* Pol5 (O60094), *S. cerevisiae* Pol5
(P39985 / YEL055C), and a bona fide family-B polymerase control, *S. cerevisiae* Pol1/CDC17
(P13382). Scanned for canonical family-B catalytic motifs with regex.

## Result (catalytic motif scan)

| Motif (family-B) | S. pombe Pol5 (O60094) | S. cerevisiae Pol5 (P39985) | CONTROL Pol1/CDC17 (P13382) |
|---|---|---|---|
| RegionI palm `D..SLYPS` / `SLYPS` | **absent** | **absent** | FOUND @863/866 |
| RegionII `YGDTDS` | absent (has degenerate `AGDTDS`) | absent (has degenerate `AGDTDS`) | FOUND @993 |
| `DTDS` (metal-coordinating Asp pair) | present @581 (context `YAGDTDSIDVLED`) | present @622 (context `YAGDTDSISVIEE`) | present @995 (context `YGDTDSVMIDTG`) |
| RegionIII `K...NS.YG` | **absent** | **absent** | FOUND @943 |
| PROSITE PS00116 exact | no match | no match | (window differs; strict regex n/a) |

## Interpretation
- Both Pol5 orthologs retain only a **degenerate GDTDS** (the Pol-B "motif C"/palm aspartate region),
  which is the origin of the legacy InterPro **IPR007015 "DNA polymerase V/Myb-binding protein 1A"**,
  Pfam **PF04931 "DNA polymerase phi"**, and PROSITE **PS00116** annotations carried on O60094.
- Critically, Pol5 **lacks the RegionI palm motif (D-x-x-SLYPS) and RegionIII (KxxxNSxYG)** that the
  genuine catalytic polymerase Pol1 possesses. A complete family-B catalytic triad cannot be formed.
- InterPro also assigns O60094 an **Armadillo/ARM-repeat fold (IPR016024 / SSF48371)** and the
  **PANTHER MYB-binding protein 1A family (PTHR13213)** — a nucleic-acid/protein-interaction scaffold,
  consistent with a ribosome-assembly role, not DNA-templated synthesis.
- Conclusion: sequence evidence supports the UniProt CAUTION (Pol5 "unrelated to B class DNA
  polymerases", PMID:12695662) and undermines any "polymerase"/direct Pol I transcription framing.
  It explains WHY the legacy family-B annotation persists (partial motif retention) without supporting
  a catalytic/transcriptional function.

*Computed via UniProt REST + regex; conservative interpretation. Not a substitute for experimental
enzymology, but concordant with the published demonstration (PMID:12695662).*
