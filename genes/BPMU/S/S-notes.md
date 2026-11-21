# Curation Notes for S (Q9T1V0) — Phage Mu Tail fiber protein S (Mup49 / gp49 / gpS)

## Biological Summary
- **Gene / Protein**: `S` (Ordered locus name `Mup49`; UniProt `Q9T1V0`, 504 aa; also designated `gp49` or `gpS`).
- **Structure and Function**:
  - Receptor-binding tail fiber subunit expressed when the 3-kb invertible G-segment of phage Mu is in the `G(+)` orientation (`file:BPMU/S/S-uniprot.txt`, "-!- MISCELLANEOUS: The orientation of the G segment is defined as G+ and G-. G+ orientation provides S-U fibers whereas G- provides S'-U' fibers. S-U and S'-U' dont have the same host range (e.g. respectively E.coli and C.freundii).").
  - Shares a constant N-terminal baseplate-attachment domain (encoded upstream of the right-hand `gixL` recombination site outside the invertible G-segment) with `S'` (`Mup52`), while its variable C-terminal beta-helical receptor-binding domain (encoded inside the G-segment) recognizes the lipopolysaccharide (LPS) outer core of *Escherichia coli* K-12 (`GO:0001530` lipopolysaccharide binding, [PMID:31504613]; `GO:0098671` adhesion receptor-mediated virion attachment to host cell).
  - Requires a tail fiber assembly chaperone (`U` / `gp50`, or non-natively `U'` / `gp51` in heterologous co-expression, [PMID:31504613]) to fold into soluble trimeric tail fibers that attach to the baseplate ([PMID:27555589]).

## Annotation Decisions
- **ACCEPT**:
  - `GO:0001530` (`lipopolysaccharide binding`): Experimentally supported receptor-binding activity toward host outer-membrane LPS ([PMID:31504613]).
  - `GO:0098024` (`virus tail, fiber`): Forms the virion tail fiber attached to the baseplate ([PMID:27555589], [PMID:31504613]).
  - `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`): Primary receptor-binding adhesin mediating attachment of G(+) Mu virions to *E. coli* K-12.
- **KEEP_AS_NON_CORE**:
  - `GO:0030430` (`host cell cytoplasm`): Compartment of late protein synthesis and U-assisted folding prior to virion incorporation.
  - `GO:0098678` (`viral tropism switching`): S is one of the two alternate tail fiber effectors produced by the Gin-mediated G-segment inversion switch, determining *E. coli* K-12 host tropism (`file:BPMU/S/S-uniprot.txt`), though the DNA inversion reaction itself is catalyzed by Gin (`P03015`).
- **TOO_GENERAL**:
  - `GO:0098015` (`virus tail`): Entailed by `GO:0098024` (`virus tail, fiber`).
  - `GO:0019062` (`virion attachment to host cell`) and `GO:0046718` (`symbiont entry into host cell`): Both are broader ancestor processes entailed by `GO:0098671` (`adhesion receptor-mediated virion attachment to host cell`).
- **NEW**:
  - `GO:0039660` (`structural constituent of virion`, `enables`): Directly supported by negative-stain EM of baseplate-tail fiber complexes in [PMID:27555589] and [PMID:31504613].
