# URA5 (YML106W, UniProt P13298) notes

## Function
- Major OPRTase (EC 2.4.2.10), PyrE subfamily type I PRTase, homodimer by similarity [UniProt:P13298].
- Jund & Lacroute isolated OPRTase ("OMP pyrophosphorylase") mutants; enzyme level constant: "The specific activity of OMP pyrophosphorylase remains constant under all of the physiological conditions used to repress, to derepress, or to induce pyrimidine biosynthesis" [PMID:4550660].
- Recombinant enzyme purified and characterised [PMID:9882434].
- URA10 "contributes only 20% of the total activity found in wild type cells" [PMID:2182197]; so URA5 ~80%.
- Not induced by Ppr1: "The other genes of UMP biosynthesis, except for ura5, are regulated by induction" [PMID:2679804].

## Review decisions
- Accept OPRTase MF rows and de novo UMP/pyrimidine process rows; cytoplasm/cytosol accepted; nucleus HDA non-core.
- MODIFY GO:0046132 'pyrimidine ribonucleoside biosynthetic process' (IBA, IEA, IMP, IDA): OMP is a nucleotide, not a nucleoside -> GO:0044205.
- MODIFY GO:0016757 glycosyltransferase -> GO:0004588; PRPP-PWY-1 'nucleotide biosynthetic process' -> GO:0044205.
