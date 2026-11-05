# Sk2 review notes

## Session 1 (create review)

- `just fetch-gene DROME Sk2` resolved Q9VZW0 (unreviewed TrEMBL, 661 aa), 12 GOA rows.
- Literature: PMID:14722126 (abstract only), PMID:21321100 (full text read), PMID:38944040
  (abstract only), plus PMID:37669862, PMID:42230987 and PMID:30476102 for physiology context.
  See `Sk2-deep-research-manual.md` for quotes.
- Key findings:
  - Sphingoid base kinase: complements yeast SK mutant, broad sphingoid-base substrate range
    [PMID:14722126 "capable of phosphorylating a range of endogenous and non-endogenous sphingoid base substrates"].
  - Uses sphingosine and DHS [PMID:21321100 "Sk1 and Sk2 use both sphingosine and DHS as substrates and generate S1P and DHS1P"].
  - Cytoplasmic plus lysosomal-membrane pool in S2 cells [PMID:21321100 "Sk2 shows cytoplasmic staining; additionally, we found that Sk2 can localize to lysosomal membranes"].
  - The Sk2 P-element allele is a hypomorph, not a null as first reported [PMID:21321100 "The Sk2 P-element mutant reported earlier is a hypomorph and not a null mutant"].
- Decisions:
  - GO:0046512 sphingosine biosynthetic process (IBA): a sphingosine kinase consumes sphingosine
    and does not make it. Modified to GO:0046519 sphingoid metabolic process. Its parent
    GO:0006670 sphingosine metabolic process would also be true, but the kinase also uses
    dihydrosphingosine, so the sphingoid term covers both substrates.
  - GO:0006665 sphingolipid metabolic process (IDA) is correct but general. Modified to
    GO:0046519.
  - kinase/transferase IEA rows modified to GO:0008481. endomembrane system (IEA) modified to
    GO:0005765 lysosomal membrane, which the gene already carries by IDA.
  - Bare protein binding (IPI, interactome) removed per protein-binding policy. Partner CG33523 has
    no known function.
  - No NEW process terms. The photoreceptor trafficking, ovulation, flight, NMJ homeostasis and
    obesity data are overexpression or mutant phenotypes, and do not show which step Sk2 itself
    performs in those processes.
- Curation gap (not a knowledge gap): GOA has no annotation reflecting the dihydrosphingosine
  substrate. GO:0008481 already covers "a sphingoid base", so no new MF term is needed.
