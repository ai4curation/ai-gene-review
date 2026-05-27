# METK1 notes

- Fetched with `just fetch-gene POPTR METK1`.
- Curated as a cytosolic S-adenosylmethionine synthase. The core function is methionine adenosyltransferase activity in S-adenosylmethionine biosynthesis; ATP binding is retained as non-core co-substrate binding.

- Addressed PR #469 review on 2026-05-10: replaced the uninformative catalytic-activity section header with the full UniProt reaction string: `Reaction=L-methionine + ATP + H2O = S-adenosyl-L-methionine + phosphate`.

## SPKW-PLANTS retrospective review (2026-05-21)

Reviewed two retired SwissProt-keyword-mapping (SPKW, `GO_REF:0000043`) annotations present in the Sept 2025 GOA snapshot but removed from current GOA after the keyword2GO pipeline was retired for cellular organisms.

- **metal ion binding (GO:0046872)** — derived from UniProt `Metal-binding`, `Magnesium`, `Cobalt`, `Potassium` keywords. Biochemically correct: UniProt COFACTOR records state the enzyme "Binds 2 divalent ions per subunit ... Can utilize magnesium, manganese or cobalt (in vitro)" and "Binds 1 potassium ion per subunit" [file:POPTR/METK1/METK1-uniprot.txt]. BINDING features confirm Mg2+ at residue 9 and K+ at residue 43. The term is true but a low-information grouping term. Action: **MARK_AS_OVER_ANNOTATED**, with proposed replacements `GO:0000287` (magnesium ion binding) and `GO:0030955` (potassium ion binding). GOA removal pruned a coarse term, not biologically meaningful information.

- **one-carbon metabolic process (GO:0006730)** — derived from UniProt `One-carbon metabolism` keyword. Defensible: SAM is the universal activated methyl donor feeding methyl-transfer (one-carbon) metabolism. But it is a broad parent and coarse/redundant relative to the precise child `GO:0006556` (S-adenosylmethionine biosynthetic process), already annotated via IBA and IEA. METK1 synthesizes the methyl-donor cofactor but does not itself transfer one-carbon units. Action: **KEEP_AS_NON_CORE**. GOA removal is a minor loss at most since the specific child term remains.

Conclusion: METK1 exemplifies the "unique-but-legitimate, low-information" SPKW category. Both retired terms are correct but coarse; their removal pruned redundant/uninformative annotation rather than losing real biology. Core function (methionine adenosyltransferase activity, SAM biosynthesis) is unaffected and remains fully captured by current GOA.
