# murE (P22188, b0085) notes

## Identity
- UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate ligase, EC 6.3.2.13; MurCDEF family, MurE subfamily (UniProt P22188; HAMAP MF_00208; NCBIfam TIGR01085; PANTHER PTHR23135:SF4).
- No deep-research file was generated; these notes are from the cached publications, UniProt and targeted web searches. FEBA fitness fetch failed (no local FEBA db / server unavailable).

## Function
- Adds meso-diaminopimelate (meso-A2pm) to UDP-MurNAc-L-Ala-D-Glu, the third cytoplasmic stem-peptide step [file:ECOLI/murE/murE-uniprot.txt "Catalyzes the addition of meso-diaminopimelic acid to the nucleotide precursor UDP-N-acetylmuramoyl-L-alanyl-D-glutamate (UMAG)"].
- Enzyme over-produced and characterised; reverse and exchange reactions [PMID:2269304 "Reverse and exchange reactions could be catalysed."].
- Crystal structure 2.0 A with product bound; carbamylated Lys in active site; structural determinant for amino-acid selection identified [PMID:11124264 "the structural determinant responsible for the selection of the amino acid to be added to the nucleotide precursor was identified"]. UniProt: MOD_RES N6-carboxylysine K225; DAP recognition motif 414-417.
- Specificity: accepts DAP analogues (lanthionine, cystathionine) with higher Km [PMID:8021219 "the MurE synthetase accepted meso-lanthionine or D-allo- or L-allo-cystathionine in vitro as good substrates, although with higher Km values"]; does not use L-lysine per UniProt ("but not L-lysine", ECO:0000269). Barreteau et al. 2008 review (PMID:18266853; web full text at academic.oup.com, not in cache) states "the Escherichia coli enzyme has a very weak l-Lys-adding activity". So E. coli MurE is a DAP-type MurE; the L-lysine-adding activity (GO:0047482) belongs to Gram-positive MurE orthologs and is correctly absent from GOA for this gene.
- Substrate recognition needs many contacts across UDP-MurNAc-dipeptide [PMID:3905407 "multiple sites located over the whole molecule are required for a proper recognition"].

## Genetics
- ts murE mutants: low DAP-adding activity, impaired murein synthesis at 42 C and accumulation of UDP-MurNAc-dipeptide [PMID:4553000 "Murein synthesis at 42 C was impaired, and uridine-5'-diphosphate-N-acetyl-muramyl-l-Ala- d-Glu (UDP-MurNAc-dipeptide) was accumulated."].

## Location
- Soluble cytoplasmic enzyme; detected in the cytosol proteome [PMID:18304323].

## Annotation issues
- InterPro2GO from IPR005761 gives regulation of cell shape and cell division: these are downstream consequences of peptidoglycan supply, not activities of MurE -> over-annotation.
- IPI protein binding to CarA/YdaY from high-throughput screens: uninformative.
- Module `peptidoglycan_precursor_biosynthesis` MurE DAP variant uses GO:0008765 with P22188 as representative: consistent with this review.
