# AP1S2 (sigma1B) sequence analysis

Reproduce with:

```bash
cd genes/human/AP1S2/AP1S2-bioinformatics
uv run --no-project --with biopython python sigma_cargo_site.py
```

All sequences are fetched live from the UniProt REST API at run time; the script asserts that
the accession returned is the accession requested, that the sequence length matches the length
UniProt declares, and that each comparator still carries the residue the cited paper reported at
the position it reported. Nothing is hardcoded. The captured run is in `sigma_cargo_site.out`
and the per-site table in `sigma_cargo_site.tsv`.

## Question 1 — does sigma1B retain the dileucine-signal binding residues?

Mattera et al. 2011 (PMID:21097499) mapped the `(D/E)XXXL(L/I)` sorting-signal binding site onto
the sigma side of the AP-1 gamma/sigma1, AP-2 alpha/sigma2 and AP-3 delta/sigma3 hemicomplexes by
mutagenesis, and showed that the `gamma1-sigma1B` hemicomplex binds the Nef, tyrosinase and
LIMP-II signals with avidity comparable to `gamma1-sigma1A`. The paper reports the sigma-side
residue numbers for sigma1A, sigma2 and sigma3A but not for sigma1B. This analysis maps them.

Global pairwise alignment (Biopython `PairwiseAligner`, BLOSUM62, gap open -11, extend -1):

| anchor | anchor site | AP1S2 (P56377) position | verdict |
|---|---|---|---|
| AP1S1 / sigma1A (P61966) | R15 | **R14** | RETAINED |
| AP1S1 / sigma1A | V88 | **V87** | RETAINED |
| AP1S1 / sigma1A | L101 | **L100** | RETAINED |
| AP1S1 / sigma1A | I103 | **I102** | RETAINED |
| AP2S1 / sigma2 (P53680) | R15 | R14 | RETAINED |
| AP2S1 / sigma2 | V88 | V87 | RETAINED |
| AP2S1 / sigma2 | L101 | L100 | RETAINED |
| AP2S1 / sigma2 | L103 | I102 | SUBSTITUTED (Leu -> Ile; sigma1A also carries Ile here) |
| AP3S1 / sigma3A (Q92572) | R15 | R14 | RETAINED |
| AP3S1 / sigma3A | V94 | V87 | RETAINED |
| AP3S1 / sigma3A | L107 | L100 | RETAINED |
| AP3S1 / sigma3A | L109 | I102 | SUBSTITUTED (Leu -> Ile, as for sigma1A) |

**Conclusion.** All four sigma-side residues whose substitution abolishes or weakens
dileucine-signal binding in sigma1A are present in AP1S2, at R14, V87, L100 and I102 in AP1S2's
own numbering (UniProt sequence version 1). The single difference against sigma2 (L103 -> I102)
is the same Leu/Ile difference that distinguishes the AP-1 sigma1 subfamily from sigma2, and
sigma1A — which was shown experimentally to bind all three test signals — carries Ile there too.
There is therefore no residue-level basis for arguing that sigma1B has lost the cargo-signal
binding site; the sequence evidence agrees with the functional result in PMID:21097499.

Caveat: this establishes that the site is intact, not that the pocket has the same fine
specificity. PMID:21097499 itself shows fine specificity differs between hemicomplexes
(gamma2-sigma1B binds the tyrosinase signal but not the LIMP-II signal), and that difference is
not read off these four positions.

## Question 2 — pairwise identity within the family

Global alignment identity to AP1S2 (P56377, 157 aa), over aligned columns:

| protein | length | identity to AP1S2 |
|---|---|---|
| AP1S1 / sigma1A (P61966, human) | 158 | 87.3% |
| AP1S3 / sigma1C (Q96PC3, human) | 154 | 72.5% |
| AP2S1 / sigma2 (P53680, human) | 142 | 48.9% |
| AP3S1 / sigma3A (Q92572, human) | 193 | 38.2% |
| Ap1s2 / sigma1B (Q9DB50, mouse) | 160 | **100.0%** |

The 87.3% sigma1B/sigma1A identity reproduces the "87% amino acid identity" reported when
sigma1B was first described (PMID:9733768), which is an independent check that the right pair of
accessions is being compared.

## Question 3 — how far can mouse sigma1B phenotypes be transferred to human?

Human AP1S2 and mouse Ap1s2 align with **zero mismatched columns over all 157 human residues**;
the mouse protein differs only by a 3-residue insertion at mouse positions 143-145. The mouse
sigma1B knockout phenotypes (PMID:20203623, PMID:25128028, PMID:24928897, PMID:27411398) are
therefore about a protein that is identical in sequence to the human one at every position the
two share. This is the strongest possible sequence basis for an ISS/ISO transfer, and it is why
the mouse work is treated here as sequence-similarity evidence for human AP1S2 rather than being
set aside as "mouse only".

## Question 4 — the sigma1 C-terminal extension

Against sigma2 (AP2S1, 142 aa), AP1S2 has 16 positions with no aligned sigma2 residue, of which
12 are contiguous at the C terminus (AP1S2 142-154, with 133-135 a separate short insertion).
This is the "C-terminal extension" that PMID:20203623 notes distinguishes the sigma1 isoforms
from sigma2, and it is the region in which the three sigma1 isoforms differ most from one
another. It is not covered by the dileucine-binding site analysed above, so this analysis says
nothing about what that extension does.
