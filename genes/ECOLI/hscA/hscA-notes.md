# hscA (P0A6Z1, E. coli K-12) notes

Provider deep research could not run: `just deep-research-falcon` failed with Edison API 403 (auth), 2026-10-23. These notes are from the cached publications and the UniProt record.

## Function
- Specialized Hsp70 (Hsc66). ATP hydrolysis is rate-limiting [PMID:10713091 "These results indicate that ATP hydrolysis is the rate-limiting step under steady-state conditions and is >10(3)-fold slower than the rate of ADP/ATP exchange."]
- IscU is its substrate, recognized through the LPPVK motif [PMID:12871959 "Hsc66 interacts with peptides corresponding to a discrete region of IscU including residues 99-103 (LPPVK)"]; [PMID:15485839 "IscU behaves as a substrate for HscA, and HscB enhances the binding of IscU to HscA."]
- Catalyzes ATP-dependent cluster transfer [PMID:18986169 "HscA-mediated acceleration of [2Fe2S] cluster transfer exhibited an absolute requirement for both HscB and ATP."]
- Binds BioB and improves its in vivo cluster assembly [PMID:19821612 "In this work, we show that in Escherichia coli, HscA significantly improves the efficiency of the in vivo assembly of the [2Fe-2S](2+) cluster on BioB under conditions of low to moderate iron."]
- Cold-induced [PMID:7665466 "Expression of hscA was not induced upon heat shock but was induced approximately 11-fold 3 h after a shift from 37 to 10 degrees C."]

## Curation decisions
- Core MF is GO:0140662, in GO:0016226. This matches the module. The GO:0044183 IBA is changed to GO:0140662. GO:0016887 is kept as a second core MF.
- Generic protein folding, protein refolding and membrane are marked as over-annotated.
- Suspected source defect: the PMID:11983079 IPI WITH/FROM UniProtKB:P0A9R9 resolves to FtsE. The paper reports HscA with Fdx/IscA, so P0A9R4 (Fdx) was probably intended. Recorded under source_defects with confidence SUSPECTED.
- Open question: GO:0140662 says "folding", but HscA's output is remodelling of the cluster-loaded scaffold.
