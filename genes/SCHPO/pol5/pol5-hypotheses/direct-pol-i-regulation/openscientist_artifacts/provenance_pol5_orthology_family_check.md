# Pol5 / MYBBP1A ortholog-family co-membership check (computed, Iteration 3)

**Goal:** Verify the ortholog chain that justifies transferring the *S. cerevisiae* Pol5
ribosome-biogenesis/pre-rRNA-processing evidence onto *S. pombe* Pol5 (O60094), and gauge
how far the human ortholog can be trusted for transfer.

**Method:** InterPro entry membership (family-defining signatures) for the three UniProt
accessions, plus a lightweight exact-5-mer Jaccard as an *orientation-only* divergence proxy
(NOT a percent-identity measure).

## Result

| Protein | UniProt | Length | Shared family entries |
|---|---|---|---|
| S. pombe Pol5 | O60094 | 959 | IPR007015, PF04931, PTHR13213 |
| S. cerevisiae Pol5 | P39985 | 1022 | IPR007015, PF04931, PTHR13213 |
| Human MYBBP1A | Q9BQG0 | 1328 | IPR007015, PF04931, PTHR13213 |

Exact 5-mer Jaccard (orientation proxy only): Sp–Sc 0.004, Sp–Hs 0.001, Sc–Hs 0.003.

## Interpretation
- All three are members of the **same defining family** (IPR007015 "DNA polymerase V/Myb-binding
  protein 1A"; PANTHER PTHR13213 MYBBP1A family) → the standard basis for orthology-based transfer,
  corroborated by primary literature (PMID:31413149: "Pol5 is homologous to ... MYBBP1A").
- Low exact-5-mer overlap reflects deep sequence divergence (expected across ~1 billion years),
  **not** absence of orthology — it just means k-mer identity is uninformative here; HMM/profile
  family membership is the correct signal.
- Practical curation consequence: the **fungal→fungal** transfer (Sc Pol5 → Sp Pol5) that underlies
  the ISO **GO:0006364 rRNA processing** annotation is well justified. The **human** ortholog is more
  diverged and functionally partly distinct (an rRNA-transcription **repressor**, and it **fails to
  complement** yeast pol5Δ, PMID:31413149), so the direct *S. cerevisiae* processing evidence — not
  human transfer — is the strongest support for the fungal Pol5 biogenesis role.
- None of the orthologs functions as a sequence-specific Pol I **activator**; this check does not
  rescue the seed hypothesis.

*Computed via InterPro + UniProt REST; conservative, orientation-level interpretation.*
