# NDUFAF2 (Q8N183) review notes

## Identity
- HGNC symbol **NDUFAF2**; synonym **NDUFA12L**; alias **B17.2L / B17.2-like**; alias **Mimitin / MMTN** (Myc-induced mitochondrial protein).
- UniProt name: "NADH dehydrogenase [ubiquinone] 1 alpha subcomplex assembly factor 2" [file:human/NDUFAF2/NDUFAF2-uniprot.txt "RecName: Full=NADH dehydrogenase [ubiquinone] 1 alpha subcomplex assembly factor 2"].
- 169 aa precursor with an N-terminal mitochondrial transit peptide [file:human/NDUFAF2/NDUFAF2-uniprot.txt "TRANSIT         1..?"], C-terminal disordered region (116-169).
- Belongs to the complex I NDUFA12 subunit family [file:human/NDUFAF2/NDUFAF2-uniprot.txt "Belongs to the complex I NDUFA12 subunit family."]. It is a **paralog of the structural subunit NDUFA12 (B17.2)** but acts as an assembly factor, NOT a stable structural subunit.

## Core function: Complex I assembly factor / molecular chaperone
- Identified as a paralog of the B17.2 (NDUFA12) structural subunit; a bona fide molecular chaperone essential for complex I assembly [PMID:16200211 "we identified a paralogue (B17.2L) of the B17.2 structural subunit"], [PMID:16200211 "These results demonstrate that B17.2L is a bona fide molecular chaperone that is essential for the assembly of complex I and for the normal function of the nervous system."].
- **Transient binding to a late assembly intermediate, absent from the mature holoenzyme.** An anti-B17.2L antibody did NOT associate with the holoenzyme but recognized an ~830-kDa subassembly and co-immunoprecipitated a subset of complex I structural subunits [PMID:16200211 "An anti-B17.2L antibody did not associate with the holoenzyme complex but specifically recognized an 830-kDa subassembly in several patients with complex I assembly defects and coimmunoprecipitated a subset of complex I structural subunits from normal human heart mitochondria."].
- Acts in **late** assembly: "the observation that B17.2L specifically associates with a large subassembly of 830 kDa indicates that it is required until the late stages of assembly, as the holoenzyme has an estimated molecular mass of 980 kDa" [PMID:16200211]. It co-IPs subunits of BOTH the matrix and membrane arms, likely stabilizing a large subassembly at the arm junction.
- Model: chaperone/facilitator that stabilizes subassemblies, increasing assembly efficiency; not absolutely required (residual complex I activity persists in the null patient) [PMID:16200211 "The complete absence of full-length B17.2L does not entirely prevent assembly of mature complex I ... showed the presence of residual enzyme activity in the patient cells and tissues."].
- Reactome models NDUFAF2 with peripheral-arm (flavoprotein/FP) subunits during assembly, then dissociating from the 980 kDa complex to leave mature Complex I [file:reactome/R-HSA-6799196.md "the MCIA complex and it is assumed all of the assembly factors (NDUFAF2-7, TIMMDC1) dissociate from the 980kDa complex to leave mature Complex I"]. NOTE: Reactome places NDUFAF2 with the FP subcomplex; the primary experimental paper (PMID:16200211) shows it is on an ~830 kDa subassembly containing both arms, not the mature enzyme.

## No catalytic activity
- NDUFAF2 has no NADH dehydrogenase / oxidoreductase activity; it is an assembly factor. UniProt describes it only as a chaperone [file:human/NDUFAF2/NDUFAF2-uniprot.txt "Acts as a molecular chaperone for mitochondrial complex I assembly"]. Complex I catalysis is a property of the holoenzyme, not this factor.

## Localization
- Mitochondrion [file:human/NDUFAF2/NDUFAF2-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:15774466}."]. Has a mitochondrial transit peptide. IDA in mitochondrion (PMID:16200211, HPA, MGI PMID:22587331) and HTP mitochondrial-proteome (PMID:34800366) all consistent.
- Reactome TAS annotations place it at the mitochondrial inner membrane (site of complex I assembly), consistent with its transient association with membrane-embedded assembly intermediates.

## Disease
- Autosomal recessive **Mitochondrial complex I deficiency, nuclear type 10 (MC1DN10, MIM 618233)**; presentations include progressive encephalopathy, leukoencephalopathy, and Leigh syndrome [file:human/NDUFAF2/NDUFAF2-uniprot.txt "Mitochondrial complex I deficiency, nuclear type 10 (MC1DN10)"], [PMID:16200211 "We found a null mutation in B17.2L in a patient with a progressive encephalopathy"].

## Mimitin / Myc target
- Same protein independently found as "mimitin" (myc-induced mitochondrial protein), a direct MYC transcriptional target [file:human/NDUFAF2/NDUFAF2-uniprot.txt "By MYC. Direct transcriptional target of MYC."]. Effects on cell proliferation / insulin secretion are downstream of its complex I chaperone role [PMID:22587331 "Mimitin, a novel mitochondrial protein, has been shown to act as a molecular chaperone for the mitochondrial complex I and to regulate ATP synthesis."].

## Moonlighting: primary cilium formation (2024)
- Loss of NDUFAF2 causes ciliary defects; NDUFAF2 binds the basal-body/centriole protein ARMC9 and is required for early ciliogenesis steps — CP110 removal from mother centrioles, ciliary-vesicle docking, and transition-zone establishment [PMID:38949024 "NDUFAF2 is involved in the initial steps of cilia formation, including the docking of membrane vesicles, removal of CP110, and establishment of the transition zone."], [PMID:38949024 "we found that a ciliary protein, armadillo repeat containing 9 (ARMC9), interacts with NDUFAF2"].
- This is a genuine but non-core, recently discovered pleiotropic role; keep the corresponding GO terms as non-core. The mechanism appears partly indirect (via mitochondrial NAD+/complex I metabolism supporting ciliogenesis): NAD+ supplementation rescues ciliary defects [PMID:38949024 "NAD+ supplementation rescues the mitochondrial and cilia defects"].

## Interactions (IntAct / interactome screens)
- Curated binary/AP-MS interactions include NDUFA7 (a complex I subunit — consistent with the assembly role), ARMC9, and various screen hits (CYB5B, LAT, LPAR3, SEC22B, SMIM1, SPG21, STX8, TMEM201, TMEM97) [file:human/NDUFAF2/NDUFAF2-uniprot.txt "Interacts with ARMC9."]. Many high-throughput hits (PMID:32296183 HuRI Y2H, PMID:33961781 BioPlex, PMID:34819669 MuSIC) are bare "protein binding" (GO:0005515) IPI annotations; kept as non-core.

## Curation decisions summary
- Core function: chaperone-like binding that drives mitochondrial respiratory chain complex I assembly.
  - MF core: GO:0044877 protein-containing complex binding (IDA, PMID:16200211 — co-IP of complex I subunits). Honest, specific MF; NOT NADH dehydrogenase/oxidoreductase.
  - BP core: GO:0032981 mitochondrial respiratory chain complex I assembly (IMP, PMID:16200211; also IBA).
- Localization core: mitochondrion (GO:0005739); mitochondrial inner membrane (GO:0005743) accepted from Reactome as the assembly site.
- REMOVE (IEA only, biologically wrong for an assembly factor): GO:0045271 respiratory chain complex I "part_of" (InterPro IEA) — NDUFAF2 is explicitly NOT part of the mature holoenzyme [PMID:16200211]. Also GO:0016020 membrane (InterPro IEA) is uninformative/over-general given specific inner-membrane annotation.
- KEEP_AS_NON_CORE: cilium assembly (IMP PMID:38949024) and the ARMC9 IPI — real but pleiotropic/moonlighting.
- Bare protein binding (GO:0005515) IPI from high-throughput screens: MARK_AS_OVER_ANNOTATED (uninformative MF; policy forbids REMOVE of IPI protein binding).
