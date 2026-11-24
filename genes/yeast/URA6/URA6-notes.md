# URA6 (YKL024C, UniProt P15700) notes

## Function
- UMP kinase (EC 2.7.4.14), adenylate kinase family, UMP-CMP kinase subfamily, monomer [UniProt:P15700].
- "The enzyme can use UMP and dUMP as phosphate acceptors with high activity"; "ATP and dATP are the best phosphate donors" [PMID:8391780].
- Localisation: "primarily in the cytoplasm (approximately 80%) and also in the nucleus (approximately 20%), but not in the mitochondria" [PMID:8391780].
- AMP kinase side activity: "yeast UK exerts significant AK activity which is responsible for the complementation" (multicopy suppression of aky2) [PMID:1333436]; CMP phosphorylation reported [PMID:1333436] but disputed by others [UniProt:P15700 CAUTION].
- SOC8 = URA6; P-loop K->E abolishes UMP kinase activity [PMID:1655742].

## YeastCyc / GO-CAM
- RXN-12002 (UMP kinase) in PWY-7176, PYRIMID-RNTSYN-PWY, PWY0-162, PRPP-PWY-1; RXN-11832 (CMP kinase) in YEAST-RNT-SALV. GO-CAMs give URA6 the obsolete GO:0004127 ((d)CMP kinase) instead of GO:0033862 (module notes this).
- RCA 'de novo pyrimidine nucleobase biosynthetic process' rows (PWY-7176, PYRIMID-RNTSYN-PWY, YEAST-DE-NOVO-PYRMID-DNT) mis-scoped for a nucleotide kinase.

## Review decisions
- Accept UMP kinase MF rows, UDP biosynthesis, cytoplasm/cytosol/nucleus.
- MODIFY GO:0006207 rows -> GO:0006225 (or GO:0009263 for the deoxy pathway); MODIFY generic kinase MF parents -> GO:0033862.
- Non-core: AMP kinase (IDA/IGI), CDP biosynthesis (IBA), pyrimidine ribonucleotide salvage (RCA), ATP binding.
