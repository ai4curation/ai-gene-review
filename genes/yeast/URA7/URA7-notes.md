# URA7 (YBL039C, UniProt P28274) notes

## Function
- CTP synthase (EC 6.3.4.2), major isoform; URA8 paralogue (78% identical) [PMID:8121398].
- "The URA7 gene ... encodes CTP synthetase (EC 6.3.4.2) which catalyses the conversion of uridine 5'-triphosphate to cytidine 5'-triphosphate, the last step of the pyrimidine biosynthetic pathway" [PMID:1753946].
- Purified from the cytosolic fraction; dimer -> tetramer with UTP+ATP; GTP activation, CTP inhibition [PMID:8075080].
- "simultaneous presence of null alleles both URA7 and URA8 is lethal"; "URA7 appears to be the major gene for CTP biosynthesis" [PMID:8121398].
- Filaments/cytoophidia: "Ura7p, Psa1p, and Glt1p were each present in distinct filaments" [PMID:20713603]; "Ura7 is the only cytoophidium present in all complexes" [PMID:39836171].
- Phospholipid link: E161K (CTP-insensitive) Ura7 alters PC/PE/PA/PS synthesis [PMID:9668079] - CTP supply, indirect.

## Issues
- Vacuole HDA from SWAT library [PMID:26928762]; paper notes "higher vacuolar background fluorescence" with mCherry -> marked over-annotated.
- 'pyrimidine nucleobase biosynthetic process' (IBA, IMP) and RCA 'de novo pyrimidine nucleobase biosynthetic process' mis-scoped for CTP synthase -> MODIFY to GO:0044210.

## Review decisions
- Accept CTPS MF, CTP biosynthesis, de novo CTP, cytosol/cytoplasm, cytoophidium.
- Non-core: identical protein binding (IBA), phospholipid biosynthetic process (IMP).
