# MET7 (YOR241W, Q08645) review notes

Context: YeastPathways module aspartate_family_threonine_biosynthesis; YeastCyc assigns MET7 to the
folate polyglutamylation reaction (EC 6.3.2.17) in several pathways/superpathways.

## Evidence journal
- Identity/activity: FPGS is encoded by MET7 [PMID:10799479 "folylpolyglutamate synthetase, which catalyzes the extension of the glutamate chains of the folate coenzymes, is encoded by the MET7 gene"]; first glutamate added by FOL3 (dihydrofolate synthetase) [PMID:10799479].
- Compartments: FPGS activity in cytoplasm and mitochondria [PMID:10775416 "have folylpolyglutamate synthetase activity in both compartments"]. MET7 "appears to encode both the cytoplasmic and mitochondrial forms" [PMID:10775416].
- Conflict: Cherest et al. argue the mitochondrial phenotype is not due to missing mitochondrial FPGS [PMID:10799479 "the loss of mitochondrial functions in met7 mutant cells is not because of the absence of a mitochondrial folylpolyglutamate synthetase"]; DeSouza et al. attribute petite formation to dTMP deficiency [PMID:10775416].
- Methionine: met7 is a methionine auxotroph [PMID:10775416 "disrupted the met7 gene and determined that the strain is a methionine auxotroph"]; cytoplasmic FPGS alone rescues [PMID:10775416 "All the genes providing cytoplasmic folylpolyglutamate synthetase complemented the methionine auxotrophy"]. Mechanism: Met6 needs polyglutamyl 5-CH3-THF, so the MET7 link to methionine biosynthesis is co-substrate supply (kept non-core).
- ER (HDA, N-terminal SWAT-GFP) is likely a tag artefact [PMID:26928762 "Tagging proteins at either terminus can mask targeting sequences as well as regulatory sequences."].
- Inner membrane / matrix: UniProt by similarity only [UniProt:Q08645].

## Pathway observations
- P4-PWY-1 (threonine+methionine superpathway) gives MET7 "L-threonine metabolic process" by RCA: removed (pure superpathway inflation).
- PWY3O-20 maps to "folic acid metabolic process": modified to tetrahydrofolylpolyglutamate biosynthetic process.
- MET7 does not belong in a threonine module; it is a one-carbon/methionine-branch cofactor enzyme.
