# Step-by-step pathway reconstruction from the *G. kaustophilus* HTA426 genome

Each row names a step of the characterised Bacillales route, the statement that assigns it,
and the call for this genome with its basis. Computed in this job; see `plot_1.png` and
`best_hits_summary.csv` for the underlying scores.

| Step | Enzyme and assigning statement | HTA426 candidate | Locus tag | Basis for the call |
|---|---|---|---|---|
| 1. GGPP/HepPP + sn-G1P -> HepGP | PcrB. PMID 21761520: "produces heptaprenylglyceryl phosphate in bacillales" | Q5L3C1 | **GK0274** | Characterised; PDB 4NAE/4NAF; control search recovers it at 255.3 bits, E=3.3e-69 |
| 1a. supply of sn-glycerol-1-phosphate | AraM/EgsA. PMID 18558723: "AraM, which constitutes the first identified G1PDH from bacteria" | **none** | - | No IPR023003/PF13685 protein; AraM query best hit 27.3 bits (E=2.5); KEGG K00096 absent from gka |
| 2. HepGP -> HepG (dephosphorylation) | unassigned. PMID 27226549: "we ... suppose that dephosphorylation is catalyzed by the phosphatase PhoB or by any other phosphatase in an unspecific manner" | candidates only | GK3079 (PpaX, HAD, co-operonic with GK3078); GK2701, GK0573, GK0221, GK0190 (alkaline phosphatases); GK1433 (PAP2); GK2526 (PGP phosphatase) | No gene is assigned in any organism, so this is a candidate list, led by GK3079 on synteny grounds |
| 3. HepG + acetyl-CoA -> Ac-HepG | YvoF. PMID 27226549: "the yvoF gene product was identified to be the acetyltransferase" | Q5KVC3 | **GK3078** | 282.8 bits, E=1.3e-77; reciprocally distinct from the MAT ortholog GK1921 |
| 4. Ac-HepG translocation to the outer leaflet | proposed, no gene assigned. PMID 40626731: "We propose Ac-HepG is shuttled to the outer membrane leaflet" | candidate only | GK3080 (Q5KVC1, polytopic membrane protein, positional ortholog of yvoD, in the GK3078 operon) | Operon position only; no functional evidence in any organism |
| 5. Ac-HepG + lipoprotein -> N-acetyl-lipoprotein | LhaT (YpjA). PMID 40626731: "lipoprotein heptaprenylglyceryl N-acetyl transferase (LhaT) (formerly YpjA)" | Q5KXW2 | **GK2189** | 281.9 bits, E=2.6e-77; single copy; next-best hit 27.7 bits |
| 5a. lipoprotein substrate generation | Lgt, LspA (standard machinery) | Q5KVC0, Q5L0V0 | **GK3081**, **GK1145** | Pfam PF01790 and PF01252 annotated; lgt is 100 bp downstream of the GK3078 operon |
| Alt. HepGP -> DGGGP (second prenylation) | archaeal DGGGP synthase; excluded in Bacillales by PMID 27226549 | **none** | - | Best hit 28.6 bits (E=0.68); only UbiA members are ctaB (GK1081) and menA (GK2877) |
| Alt. DGGGP -> CDP-archaeol | CarS | **none** | - | Best hit 30.9 bits (E=0.084) |
| Alt. prenyl chain saturation | archaeal geranylgeranyl reductase | **none** | - | Best hit GK2836 at 53.4 bits, FAD-oxidoreductase superfamily level, versus a 250-285 bit ortholog scale; no PF01494 in the proteome |

## Conclusion supported by the genome

The genome supports the lipoprotein N-acetylation fate and excludes the archaeal diether fate.
It cannot by itself assign the dephosphorylation step, and it cannot explain where sn-glycerol-1-phosphate
comes from in this organism.
