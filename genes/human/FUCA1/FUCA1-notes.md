# FUCA1 notes

Deep research (`just deep-research-falcon human FUCA1`) timed out after 600 s ("All providers failed"),
so the literature work was done manually with PubMed and the cached `publications/` files.

## Function
- Lysosomal tissue alpha-L-fucosidase (GH29, EC 3.2.1.51). Knockout evidence: [PMID:27491075 "Homozygous knockout mice completely lack α-L-fucosidase activity in all tested organs leading to highly elevated amounts of the core-fucosylated glycoasparagine Fuc(α1,6)-GlcNAc(β1-N)-Asn"].
- Order of steps with AGA: [PMID:27491075 "It is known that α1,6-(core)-fucosylation sterically inhibits the lysosomal aspartyl-glucosaminidase (AGA; EC 3.5.1.26)"] -> FUCA1 acts before AGA on glycoasparagines.
- Substrate classes: [PMID:39796208 "This enzyme is responsible for breaking down fucose-containing glycoproteins, glycolipids, and oligosaccharides within the lysosome"].
- Patient cells: [PMID:4074382 "Studies on fibroblasts from patients with less than 5% of normal alpha-L-fucosidase activity (fucosidosis) showed 8 of 11 patients synthesized no detectable alpha-fucosidase protein"]; partial secretion [PMID:1873910 "only 25%-30% of control enzyme was secreted with the remainder retained intracellularly"].

## Annotation notes
- IDA PMID:19666478 is a FUCA2-focused paper, but the full text states "we prepared and characterized human FUCA1 and FUCA2", so the IDA rows are accepted.
- HuRI protein-binding rows (CIB1, MED10, UBQLN2) removed as uninformative.
- Added NEW glycoprotein catabolic process (GO:0006516), which is also the term the dismech Fucosidosis entry marks as DECREASED.
- Module: `modules/lysosomal_glycoprotein_degradation.yaml` (created in the same session).
