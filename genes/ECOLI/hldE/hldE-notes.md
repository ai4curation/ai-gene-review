# hldE notes

## 2026-10-02 ADP-heptose module review

HldE/RfaE is the bifunctional E. coli ADP-heptose enzyme. Kneidinger et al. purified E. coli HldE and GmhB and reconstituted the pathway from sedoheptulose 7-phosphate through ADP-D-beta-D-heptose, assigning HldE's N-terminal activity to heptose 7-phosphate kinase and its C-terminal activity to heptose-1-phosphate adenylyltransferase [PMID:11751812].

The LPS-core process annotations are appropriate in E. coli. Valvano et al. found that an E. coli rfaE/hldE disruption causes a heptoseless LPS phenotype, and separable domain experiments supported a bifunctional model with Domain I required for the kinase-side function and Domain II for ADP transfer [PMID:10629197].

The homodimerization row is non-core but experimentally supported. McArthur et al. found that purified HldE1 eluted at a mass consistent with dimers and that tagged HldE constructs co-purify in vivo; ATP-binding-site mutants exerted a dominant-negative effect, supporting a functional HldE dimer [PMID:16030223].

Review decisions:

- Accept both exact MFs, `GO:0033785` and `GO:0033786`.
- Accept `GO:0097171` and `GO:0009244` for E. coli because the full HldE/GmhB/HldD route to the L,D-heptose LPS donor is present.
- Keep cytosol, ATP binding, and homodimerization as non-core.
- Mark broad catalytic and carbohydrate terms as over-annotated.
