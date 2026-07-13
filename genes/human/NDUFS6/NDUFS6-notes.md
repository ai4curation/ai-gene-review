# NDUFS6 (O75380) review notes

## Identity
- NADH:ubiquinone oxidoreductase subunit S6 / "13 kDa-A" / CI-13kD-A (UniProt O75380, 124 aa precursor; mature 29-124 after mitochondrial transit peptide 1-28).
- Accessory (supernumerary) subunit of mitochondrial respiratory Complex I (NADH:ubiquinone oxidoreductase).
- HGNC:7713; gene on chromosome 5.

## Verified biology
- **Accessory / non-catalytic**: UniProt FUNCTION: "Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis." [file:human/NDUFS6/NDUFS6-uniprot.txt]. Despite the "S" (iron-sulfur protein / IP fraction) name it does NOT carry an electron-transfer Fe-S cluster of the catalytic wire.
- **Module**: N-module (NADH-oxidising / flavoprotein region of the peripheral/matrix arm). Historically assigned to the iron-sulfur protein (IP) fraction [PMID:12611891; PMID:9647766].
- **Zinc-binding motif**: contains a CHCC zinc-finger (Pfam PF10276 zf-CHCC; InterPro IPR019401 Znf_CHCC). C-terminal ...IACDGG...TCGYCGLQFRQHHH sequence.
- **Subunit / location**: component of Complex I; peripheral membrane protein on the matrix side of the mitochondrial inner membrane. UniProt SUBCELLULAR LOCATION: "Mitochondrion inner membrane ... Peripheral membrane protein ... Matrix side." [file].
- **Complex composition**: mammalian Complex I = 45 subunits (14 core + 31 accessory) [PMID:27626371; PMID:12611891].

## Assembly / stability role
- PMID:27626371 (Stroud et al., Nature 2016): systematic knockout of every accessory subunit; 25 of 31 accessory subunits (incl. NDUFS6) strictly required for assembly of a functional Complex I; loss of each subunit destabilises other subunits in the same structural module. Establishes accessory subunits (NDUFS6 among them) as "integral for assembly and function of human mitochondrial complex I." This is the experimental basis for the FUNCTION statement (ECO:0000269|PubMed:27626371 in UniProt).
- NDUFS6 stabilises the N-module during Complex I assembly (see also Reactome Complex I biogenesis R-HSA-6799198).

## Disease
- Mitochondrial complex I deficiency, nuclear type 9 (MC1DN9), MIM:618232. Autosomal recessive.
- PMID:15372108 (Kirby et al., JCI 2004): NDUFS6 mutations a novel cause of lethal neonatal complex I deficiency; patient cells grossly underexpress NDUFS6 and show abnormal Complex I assembly.
- PMID:19259137 (Spiegel et al., 2009): C115Y variant → fatal neonatal lactic acidemia in Caucasus Jews (not in GOA; noted in UniProt VARIANT).

## GOA MF terms (subunit is non-catalytic)
GOA lists MF annotations GO:0008137 (NADH dehydrogenase (ubiquinone) activity) and GO:0009055 (electron transfer activity), both NAS from the 1998 cDNA papers (PMID:9878551, PMID:9647766). These describe the **complex-level** catalytic activity, not the individual subunit — NDUFS6 does not itself carry NADH-dehydrogenase or electron-transfer catalysis. Handled as MARK_AS_OVER_ANNOTATED (activity belongs to the holoenzyme / catalytic core subunits, not this accessory subunit).

## Core function modeling decision
- molecular_function: GO:0005198 structural molecule activity (subunit-specific, non-catalytic structural role).
- contributes_to_molecular_function: GO:0008137 NADH dehydrogenase (ubiquinone) activity (complex-level activity the subunit supports but does not independently enable).
- directly_involved_in: GO:0006120 (mitochondrial electron transport, NADH to ubiquinone), GO:0032981 (mitochondrial respiratory chain complex I assembly).
- located_in: GO:0005743 mitochondrial inner membrane.
- in_complex: GO:0045271 respiratory chain complex I.

## Annotation actions summary
- GO:0045271 respiratory chain complex I (part_of): ACCEPT (well supported by IBA, multiple IDA/IPI/NAS, structure papers). Preferred CC over obsolete GO:0005747.
- GO:0005743 mitochondrial inner membrane (located_in / is_active_in): ACCEPT (UniProt SUBCELLULAR LOCATION; IDA ComplexPortal; IBA).
- GO:0005739 mitochondrion (located_in): KEEP_AS_NON_CORE (broader parent of inner membrane; large-scale proteomics).
- GO:0006120 mitochondrial electron transport, NADH to ubiquinone (involved_in): ACCEPT (core process the complex performs; subunit contributes).
- GO:0032981 assembly: not in GOA -> add as NEW (this is the real specific BP for the accessory subunit) — actually covered via core_functions; add NEW annotation with IMP evidence from PMID:27626371.
- GO:0008137 NADH dehydrogenase (ubiquinone) activity (enables): MARK_AS_OVER_ANNOTATED (catalysis is complex-level; subunit non-catalytic). Retain as contributes_to in core_functions.
- GO:0009055 electron transfer activity (enables): MARK_AS_OVER_ANNOTATED (subunit carries no redox cofactor / Fe-S wire).
- GO:1902600 proton transmembrane transport (involved_in, IEA GO_REF:0000108 from GO:0008137): MARK_AS_OVER_ANNOTATED (auto-inferred complex-level; NDUFS6 not a proton-pumping membrane-arm subunit).
- GO:0009060 aerobic respiration (NAS ComplexPortal): KEEP_AS_NON_CORE (complex-level high-level process).
- GO:0042776 proton motive force-driven mitochondrial ATP synthesis (NAS ComplexPortal): MARK_AS_OVER_ANNOTATED (ATP synthesis is Complex V; Complex I contributes to the PMF but this term over-reaches for an accessory CI subunit).
