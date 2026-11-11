# SKT5 / CHS4 (YBL061C, UniProt P34226) notes

- Non-catalytic activator of chitin synthase III (Chs3). "chs4-null mutants are resistant to Calcofluor white and exhibit a considerable reduction in cell wall chitin and in chitin synthase III (CSIII) activity" and the defect "is due to a reduced V(max) of the enzyme" [PMID:9234668].
- Proposed "an essential component of the CSIII complex, acting as a post-translational regulator of this activity" [PMID:9234668].
- Two-hybrid "revealed an interaction between Chs4p and Chs3p"; Bni4 links Chs4 to septin Cdc10; "A GFP-Chs4p fusion protein also localizes to a ring at the mother-bud neck on the mother-cell side" [PMID:9314530].
- Farnesylated at C-terminal CVIM; "abolition of Chs4p prenylation causes a approximately 60% decrease in CSIII activity"; "Prenylation of Chs4p, however, is not a factor that mediates plasma membrane association" [PMID:17142567].
- UniProt: "SUBCELLULAR LOCATION: Cell membrane"; "SIMILARITY: Belongs to the SKT5 family." [UniProt:P34226]
- Paralog SHC1 is the sporulation-specific counterpart; Chs4 is degraded in sporulation [PMID:11918806].

## Pathway/module
- Module fungal_chitin_chitosan_synthesis: Chs4/Shc1 = enzyme activator (GO:0008047) positively regulating Chs3. Consistent with literature.
- YeastCyc PWY3O-15 (chitin biosynthesis) assigns only CHS1/2/3 to the 2.4.1.16 reaction; SKT5 is mentioned in the comment only (correctly not a catalyst).
- Also an adaptor (Chs3-Chs4-Bni4-septin) for bud-neck targeting; GO has no annotation for this adaptor role (only via protein-binding-type terms).
