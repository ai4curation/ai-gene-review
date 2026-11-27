# ManY (P69801) - Curation Notes

## Gene Overview

ManY is the EIIC component of the mannose-specific phosphotransferase system (Man-PTS) in E. coli K12. Gene synonyms include `pel` (phage exclusion locus) and `ptsP`.

## Key Literature Findings

### Core Function: PTS EIIC Channel Component
- ManY (formerly II-PMan) is a very hydrophobic integral membrane protein (28 kDa) that forms the transmembrane channel together with ManZ (II-MMan) [PMID:2951378 "II-PMan (28 kDa) is very hydrophobic...Both are integral membrane proteins and most likely form the transmembrane channel"]
- The ManXYZ complex is the mannose-specific PTS permease consisting of three subunits encoded by the ptsLPM (manXYZ) operon [PMID:2951378 "The permease consists of three different subunits, IIIMan, II-PMan, and II-MMan, which are encoded in a single transcriptional unit ptsLPM"]
- All three subunits are required for sugar transport and phosphorylation [PMID:2951378 "All three subunits are required for sugar transport and phosphorylation"]
- ManY contains the specific substrate-binding site within its PTS EIIC type-4 domain [UniProt]

### Structural Information
- Cryo-EM structure (3.52 A, PDB:6K1H) shows ManY-ManZ forms a homotrimer of heterodimers [PMID:31209249]
- Multiple transmembrane helices with complex topology including intramembrane helices [PMID:8774730, PMID:32710850]
- C-terminus is cytoplasmic, confirmed by GFP/PhoA fusions [PMID:15919996]

### Substrate Specificity
- Primary substrate: mannose [PMID:2951378]
- Secondary substrates: glucose, fructose, N-acetylglucosamine [PMID:5545083, PMID:4153999, PMID:6252281]
- Glucose is primarily transported by PtsG; Man-PTS is a secondary glucose uptake system
- Fructose is primarily transported by FruAB; Man-PTS is a secondary fructose uptake system
- GlcNAc has two PTS systems: PtsM (Man-PTS) and another encoded near nagA,B [PMID:6252281 "N-Acetylglucosamine enters E. coli by two distinct phosphotransferase systems...One of these is the PtsM system"]

### Non-Transport Functions
- Bacteriophage lambda receptor: ManY and ManZ alone are sufficient for lambda DNA penetration [PMID:2951378 "II-PMan and II-MMan alone are sufficient for penetration of lambda DNA"]. Originally identified as "pel" mutations [PMID:353494]
- Chemoreceptor: PTS enzymes serve as chemoreceptors for sugars [PMID:4604906]

## Annotation Review Summary

### Accepted Core Annotations
- GO:0005886 (plasma membrane) - 4 annotations (IBA, IEA, 2x IDA): all accepted, well-supported
- GO:0009401 (PEP-dependent sugar PTS) - 3 annotations (IBA, IEA, IDA): all accepted, core BP
- GO:0015761 (mannose transmembrane transport) - 2 annotations (NAS, IDA): accepted, core BP
- GO:0022870 (protein-N(PI)-phosphohistidine-mannose PTS transporter activity) - IDA: accepted, core MF
- GO:0016020 (membrane) - 2 annotations (IEA, HDA): accepted, broader but correct

### Non-Core Annotations (KEEP_AS_NON_CORE)
- GO:0015764 (N-acetylglucosamine transport) - secondary substrate
- GO:0098708 (D-glucose import across plasma membrane) - secondary substrate
- GO:1990539 (fructose import across plasma membrane) - 2 annotations, secondary substrate

### New Annotations Suggested
- GO:1902495 (transmembrane transporter complex) - present in UniProt GO cross-refs but missing from GOA TSV

## Open Questions
- Should phage lambda receptor and chemoreceptor functions have dedicated GO annotations?
- Are there additional sugar substrates transported by the Man-PTS?
- No deep research file was available for this gene; one could be generated for more comprehensive review.

## Notes on Evidence
- Several key publications (PMID:353494, PMID:4604906, PMID:31209249, PMID:8774730) did not have cached full text in the publications directory
- PMID:5545083 (Kundig & Roseman 1971) had no abstract available in the cached file
- The review relied heavily on PMID:2951378 (Erni et al. 1987), which is the definitive characterization paper


## 2026-11-07 complete annotation re-review

All existing annotations and genuine Falcon research were re-read. No source file was refreshed. Historical notes above are retained; this audit supersedes their broad-term decisions and unsupported source attributions. General membrane/cytoplasm and ManX enzyme genera now refine to supported specific terms. ManX allows intra- and intersubunit phosphotransfer [PMID:2681202, PMID:8262947]; ManYZ supplies direct substrate-binding/translocation work, with contributes_to core rather than autonomous phosphorylation [PMID:31209249, PMID:2951378]. No new rows were added; historical complex NEW rows remain intact.

Source/construct scope, exact short quotations, access failures and ontology snapshots: `analysis/module_audits/bacterial_mannose_pts/ecoli-consultation/evidence.md`. In particular,1985IIMan is not uniquely modern ManZ,1996single-anchor ManZ topology is superseded by2019structure, and lambda membrane-component sufficiency does not establish a ManX pore. The2019ManYZ assay is counterflow in liposomes, not the complete PEP/ManX reaction; sequence-exact K-12 proteins were expressed recombinantly in knockoutBL21. Early sugar experimental annotations are retained with independent substrate corroboration and explicit inaccessible-table limits. All PAINT checks reported no IRD/IKR on the recovered target lineages.
