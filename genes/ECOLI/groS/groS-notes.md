# groS manual review notes

- Deep research and FEBA fitness summaries were unavailable for this review; the synthesis below is based on the cached UniProtKB record and the cached publications cited by the seeded GOA rows.
- GroES/GroS is the heptameric co-chaperonin lid of the GroEL-GroES machine. GroEL binds unfolded proteins and ATP, whereas GroES binds GroEL's apical domains to cap the cis chamber and enable productive folding. The GroES folding, chaperone-binding, GroEL-GroES complex, and cytosolic localization rows are accepted.
- Every GO:0005515 row in the stub names GroEL as the interacting partner. Structural, cryo-EM, atomic-force, NMR, and single-molecule studies all assay the GroEL-GroES machine, so these rows are modified to GO:0051087 protein-folding chaperone binding rather than retained as generic protein binding.
- The IEA ATP-binding row is removed: GroES regulates ATP-dependent chaperonin cycling by capping GroEL, but the ATP/ADP nucleotide sites are in GroEL rings. The broad PAINT metal-ion-binding row is also removed; it was placed at the root of the GroES family from a single mycobacterial descendant and is not supported for E. coli GroES.
- Identical-protein-binding rows are kept as non-core because the GroES heptameric ring is essential architecture but not the terminal activity that the annotation should surface as the protein's core function.
- GroES is retained as a host factor for bacteriophage morphogenesis; that activity is real but contextual, so the phage virion-assembly process is non-core relative to the GroEL/GroES chaperonin cycle.
