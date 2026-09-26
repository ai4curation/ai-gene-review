# pvdD Gene Review Notes

## Identity and Context

- `pvdD` is `PP_4219` in *Pseudomonas putida* KT2440 and was previously annotated as `ppsD`. [PMID:31451546 Arginine Biosynthesis Modulates Pyoverdine Production and Release in *Pseudomonas putida* as Part of the Mechanism of Adaptation to Oxidative Stress, "pvdD (PP_4219; previously annotated as ppsD), which does not produce pyoverdine"]
- UniProt `Q88F79` is a 3470 aa multimodular non-ribosomal peptide synthetase with repeated AMP-binding, condensation, phosphopantetheine carrier, and terminal thioesterase domains, consistent with a soluble cytosolic NRPS assembly-line enzyme. [file:PSEPK/pvdD/pvdD-uniprot.txt, "Non-ribosomal peptide synthetase"; "DR   InterPro; IPR010071; AA_adenyl_dom."; "DR   InterPro; IPR001242; Condensation_dom."; "DR   InterPro; IPR006162; Ppantetheine_attach_site."; "DR   InterPro; IPR001031; Thioesterase."]

## Main Functional Conclusions

- `pvdD/PP_4219` is a pyoverdine structural gene in KT2440. [PMID:31451546 Arginine Biosynthesis Modulates Pyoverdine Production and Release in *Pseudomonas putida* as Part of the Mechanism of Adaptation to Oxidative Stress, "the genes analyzed were pvdD and pvdA, encoding a pyoverdine nonribosomal peptide synthetase and a protein involved in pyoverdine side chain synthesis, respectively"]
- Loss of `pvdD` abolishes pyoverdine production, making it an appropriate negative control for pyoverdine-deficient phenotypes. [PMID:31451546 Arginine Biosynthesis Modulates Pyoverdine Production and Release in *Pseudomonas putida* as Part of the Mechanism of Adaptation to Oxidative Stress, "pvdD (PP_4219; previously annotated as ppsD), which does not produce pyoverdine"]
- KT2440 uses pyoverdine as its characterized siderophore, not enterobactin. [PMID:19459056 Siderophore-mediated iron acquisition in the entomopathogenic bacterium *Pseudomonas entomophila* L48 and its close relative *Pseudomonas putida* KT2440, "Structural analysis of the pyoverdine produced by the closely related P. putida KT2440 showed that this strain produces an already characterised pyoverdine, but different from P. entomophila, and no evidence was found for the production of a second siderophore."]
- The KT2440 pyoverdine structures recovered experimentally are the known pyoverdines G4R and G4R A. [PMID:28631237 Structural characterization of pyoverdines produced by *Pseudomonas putida* KT2440 and *Pseudomonas taiwanensis* VLB120, "In Pseudomonas sp. putida KT2240 samples, the known pyoverdines G4R and G4R A were readily confirmed."]
- pvdD/PP_4219 is a pyoverdine nonribosomal peptide synthetase required for pyoverdine production in P. putida KT2440.

## GO Curation Implications

- Enterobactin-specific terms in the seeded GOA are incorrect for `pvdD`; they should be replaced with pyoverdine- or siderophore-specific process terms. [PMID:19459056 Siderophore-mediated iron acquisition in the entomopathogenic bacterium *Pseudomonas entomophila* L48 and its close relative *Pseudomonas putida* KT2440, "this strain produces an already characterised pyoverdine"; PMID:31451546 Arginine Biosynthesis Modulates Pyoverdine Production and Release in *Pseudomonas putida* as Part of the Mechanism of Adaptation to Oxidative Stress, "pyoverdine nonribosomal peptide synthetase"]
- Generic `catalytic activity` is too weak; the protein is better described as a non-ribosomal peptide synthetase with amino acid ligation chemistry and phosphopantetheine-dependent carrier modules. [file:PSEPK/pvdD/pvdD-uniprot.txt, "Non-ribosomal peptide synthetase"; PMID:12700264 Substrate specificity of the nonribosomal peptide synthetase PvdD from *Pseudomonas aeruginosa*, "showing that PvdD has peptide synthetase activity."]
- `phosphopantetheine binding` is directionally right but under-specific for this enzyme class; `phosphopantetheine-dependent carrier activity` better captures the carrier-module function of the PCP domains. [file:PSEPK/pvdD/pvdD-uniprot.txt, "DR   InterPro; IPR020806; PKS_PP-bd."; "DR   InterPro; IPR006162; Ppantetheine_attach_site."]
- `cytosol` is the better localization term over generic `cytoplasm` for this large soluble bacterial NRPS. [file:PSEPK/pvdD/pvdD-uniprot.txt, "KW   Reference proteome"; "Non-ribosomal peptide synthetase"]
- phosphopantetheine binding is directionally right but under-specific for this enzyme class; phosphopantetheine-dependent carrier activity better captures the carrier-module function of the PCP domains.

## Missing Ontology Coverage

- GO has `pyoverdine biosynthetic process` but lacks a pyoverdine-specific synthetase complex term; this absence likely drives over-transfer to `enterobactin synthetase complex`.


## Full-gene re-review, 2026-09-20

Reviewed all ten source rows and both core functions. Restored catalytic activity, cytoplasm, phosphopantetheine binding, core amino-acid activation and secondary-metabolite biosynthesis. Kept the specific enterobactin/DHB-serine/complex corrections, but removed unverified transfer of P. aeruginosa threonine-module assignments to the three-module KT2440 target. Read the complete Falcon report and incorporated its target-versus-comparator limitations. GO:0072330 remains UNDECIDED pending chemical-structure review: a pyoverdine name alone does not exclude a monocarboxylic acid. Source rows unchanged and no NEW added.

PMID:25895945 specifically establishes three KT2440 structures (Asp-Orn-OHAsp-Dab-Gly-Ser-cOHOrn), two with cyclization and succinate/succinamide side-chain differences. PMID:28631237 also examines KT2440, but its three *new* structures are from P. taiwanensis VLB120; those must not be imported as target chemistry. Root independently found the cyclic hydroxyAsp-Dab pair in the full text of PMID:31451546 and could not access a molecular figure to count free carboxyls. This supports UNDECIDED pending a focused chemistry/ontology report, rather than asserting either mono- or polycarboxylate class.
