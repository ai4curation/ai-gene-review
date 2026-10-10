# GLT1 (YDL171C, Q12680) notes

Evidence journal (no paid deep research run; built from UniProt and cached publications).

- Glutamate synthase [NADH] (NADH-GOGAT), EC 1.4.1.14; 2145 aa precursor (mature chain 54-2145); cofactors [3Fe-4S], FAD, FMN; homotrimer; plant-like single-polypeptide GOGAT [UniProt:Q12680].
- Biochemistry: NADH-dependent GOGAT "specific for NADH, glutamine, and alpha-ketoglutarate"; "2 mol of glutamate synthesized per mol of glutamine consumed" [PMID:4362465]. Purified to homogeneity, inhibited by homocysteine sulfonamide; "uses NADH exclusively" [PMID:7047525].
- Gene: "S. cerevisiae has a single NADH-GOGAT enzyme, consisting of three 199-kDa monomers"; null mutants "completely devoid of GOGAT activity" [PMID:7836314].
- Regulation/physiology: GLT1 repressed by glutamate, activated by Gln3/Gcn4; "in a wild-type strain grown on ammonium, GOGAT constitutes an ancillary pathway for glutamate biosynthesis" [PMID:9657994]. gdh1 glt1 gdh3 triple mutant is a glutamate auxotroph [PMID:9287019].
- Supramolecular: Glt1 forms cytoophidia (filaments), predominantly in non-quiescent cells [PMID:39836171].
- Mitochondrial proteome hits [PMID:14576278, PMID:16823961]; N-terminal 53-residue presequence in UniProt, but no direct study of a mitochondrial GOGAT pool.

## Curation decisions
- Core MF GO:0016040; BP GO:0097054 and GO:0019676 (GS/GOGAT cycle with GLN1); CC cytosol.
- protein binding (YLR257W) x2: REMOVE.
- Mitochondrion HDA x4: KEEP_AS_NON_CORE (unresolved; possible presequence).
- iron ion binding (IEA): KEEP_AS_NON_CORE - iron is bound as an Fe-S cluster, captured by GO:0051536.
