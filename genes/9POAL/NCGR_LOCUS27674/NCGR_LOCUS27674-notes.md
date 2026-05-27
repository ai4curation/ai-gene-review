# NCGR_LOCUS27674 (A0A811PC48) Review Notes

## Gene Identity
- **UniProt**: A0A811PC48 (TrEMBL, unreviewed)
- **Organism**: *Miscanthus lutarioriparius* (NCBITaxon:422564), a C4 grass in order Poales
- **Annotated as**: UMP-CMP kinase (EC 2.7.4.14)
- **Length**: 714 amino acids / 78.8 kDa
- **Evidence level**: PE3 (Inferred from homology)
- **Source**: Whole genome shotgun sequence [EMBL:CAD6242091.1]

## Key Concern: Likely Chimeric Gene Model

This protein is almost certainly a **chimeric gene model artifact** resulting from incorrect fusion of two separate genes during genome annotation:

### Evidence for chimeric model:

1. **Abnormal size**: 714 AA is 2-3.5x larger than any known UMP-CMP kinase:
   - Arabidopsis UMP-CMP kinase: 202 AA [PMID:9736767]
   - Rice YL2 (chloroplastic UMK): 351 AA including transit peptide [PMID:29866037]
   - Human CMPK1: 196-228 AA
   - E. coli CMP kinase: 225 AA

2. **Two unrelated domains**:
   - N-terminal: Adenylate kinase domain (Pfam PF00406, ADK) - consistent with UMP-CMP kinase
   - C-terminal (positions 555-650): Chalcone isomerase domain (Pfam PF16035, Chalcone_2) - functionally unrelated

3. **Conflicting automated annotations** from different domains:
   - UMP/CMP/dCMP kinase activities (from ADK domain via HAMAP/UniRule)
   - Fatty acid binding (from CHI-fold domain via PANTHER/TreeGrafter)
   - Intramolecular lyase activity (from CHI-fold superfamily via InterPro)

4. **Genome annotation context**: The *M. lutarioriparius* genome has 68,328 predicted gene models [PMID:33931638], which is very high even for an allotetraploid grass. The EVidenceModeler pipeline used is known to sometimes produce chimeric models in polyploid genomes.

### The two likely constituent genes:

**Gene 1 (N-terminal ~350 AA)**: A plastid/chloroplast-targeted UMP-CMP kinase
- Consistent with rice YL2 ortholog [PMID:29866037] or Arabidopsis PUMPKIN [PMID:30523175]
- Plant plastid UMKs have transit peptides and are 300-350 AA total
- Functions in de novo pyrimidine nucleotide biosynthesis in chloroplasts

**Gene 2 (C-terminal ~150+ AA)**: A CHI-fold fatty acid-binding protein (FAP)
- The Chalcone_2 domain (PF16035) belongs to the CHI superfamily
- FAP subfamily members are non-catalytic - they bind fatty acids but lack isomerase activity [PMID:22388820]
- Plant FAPs typically localize to plastids for de novo fatty acid biosynthesis [PMID:22388820]

## Annotation Assessment

All 13 GO annotations are IEA (electronic). Given the chimeric nature:

### Annotations likely correct for the UMP-CMP kinase portion:
- GO:0033862 UMP kinase activity (UniRule)
- GO:0036430 dCMP kinase activity (UniRule)
- GO:0036431 CMP kinase activity (UniRule)
- GO:0005524 ATP binding (InterPro)
- GO:0019205 nucleobase-containing compound kinase activity (InterPro)
- GO:0016776 phosphotransferase activity, phosphate group as acceptor (InterPro)
- GO:0006221 pyrimidine nucleotide biosynthetic process (UniProt)
- GO:0006207 'de novo' pyrimidine nucleobase biosynthetic process (InterPro)

### Annotations likely from the CHI-fold/FAP portion (erroneous for whole protein):
- GO:0005504 fatty acid binding (TreeGrafter/PANTHER) - from FAP domain
- GO:0016872 intramolecular lyase activity (InterPro) - from CHI superfamily, but FAPs are non-catalytic

### Localization annotations:
- GO:0005737 cytoplasm - plausible for UMK
- GO:0005634 nucleus - plausible for UMK (some UMKs are nuclear)
- GO:0009570 chloroplast stroma - plausible if this is a plastid-targeted UMK, though rice YL2 localizes to thylakoid membranes, not stroma

## References
- PMID:9736767 - Arabidopsis UMP-CMP kinase characterization
- PMID:29866037 - Rice YL2 chloroplastic UMP kinase  
- PMID:30523175 - Arabidopsis PUMPKIN plastid UMP kinase
- PMID:22388820 - CHI-fold FAP proteins and fatty acid binding
- PMID:33931638 - Miscanthus lutarioriparius genome assembly
