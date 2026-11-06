# EIF2AK2 (PKR) review notes

## Literature search (no deep-research provider available)

Sources checked: the UniProt entry P19525 (curated FUNCTION, SUBUNIT, SUBCELLULAR LOCATION
and ACTIVITY REGULATION text); every GOA-cited publication cached by
`just fetch-gene-pmids human EIF2AK2` (49 papers; most are abstract-only); and the cached
Reactome reactions for the PKR pathway (R-HSA-98336xx/9835xxx/9839xxx). Context only: the integrated stress response module (module proposed in ai4curation/ai-gene-review#5904),
which models PKR as one realizer of the eIF2alpha kinase step, and GO-CAM 66b5638000001589, which is about PERK and contains no PKR activity.

## Key findings

- Core activity: dsRNA-activated eIF2alpha kinase [PMID:1695551 "On activation by dsRNA in the presence of ATP, the kinase becomes autophosphorylated and can catalyze the phosphorylation of the alpha subunit of eIF2, which leads to an inhibition of the initiation of protein synthesis"].
- dsRNA binding through the N-terminal dsRBMs [PMID:1351683 "The double-stranded RNA (dsRNA)-binding domain of the human p68 kinase has been localized to the N-terminal half of the enzyme"].
- Antiviral role through translational control [PMID:19189853 "PKR is activated by HCV infection and plays a critical antiviral role through inhibition of viral protein translation"].
- IFN-beta amplification through eIF2alpha phosphorylation, not direct signalling [PMID:22948139 "an eIF-2α-dependent translation inhibition mechanism is sufficient to explain the PKR-mediated amplification of IPS-1-dependent IFN-β induction by foreign RNA"].
- Dual specificity: tyrosine autophosphorylation [PMID:16373505 "human PKR is a dual specificity kinase phosphorylated at Y101, Y162 and Y293 in vitro and in vivo"] and CDK1 Tyr4 [PMID:20395957 "PKR, Ser/Thr kinase, phosphorylates its new substrate Cdc2 at the Tyr 4 residue"].
- Secondary substrates and signalling (non-core): MKK6 and p38 [PMID:15229216], TRAF-NF-kappaB [PMID:15121867], PPP2R5A [PMID:10866685], NFAR/ILF3 [PMID:21123651], and the NLRP3 inflammasome [PMID:22801494], whose role has been questioned by later mouse studies (not cached here).
- Location: mainly cytoplasmic/cytosolic, with a minor active nuclear pool [PMID:21072047 "Biochemical analysis demonstrated that nuclear PKR is an active kinase that can respond to stress"].

## Curation decisions

- The 58 bare protein-binding IPI rows are REMOVEd under the protein-binding policy. Identical protein binding is MODIFYed to protein homodimerization activity.
- The general protein kinase activity and kinase activity rows are MODIFYed to protein serine/threonine kinase activity, or to eIF2alpha kinase activity where eIF2alpha was the substrate assayed.
- Cytoplasm rows are MODIFYed to cytosol. Nucleus and nucleoplasm rows are kept as non-core.
- Protein phosphatase regulator activity is REMOVEd, because PKR regulates PP2A by phosphorylating B56alpha, not as a regulatory subunit.
- Cellular response to amino acid starvation: the ARBA IEA row is marked as over-annotated, because amino-acid sensing is the GCN2 branch. The IMP row from PMID:25329545 is UNDECIDED, because the abstract does not describe a PKR experiment.
- NEW: integrated stress response signaling (GO:0140467). Comparator: EIF2AK1 carries it by IDA.
