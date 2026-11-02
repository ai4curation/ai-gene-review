# glt-1: biological evidence

GLT-1 is a major facilitator superfamily glucose transporter that supplies low-affinity, high-capacity glucose uptake in Neurospora crassa. It is the system I component of the dual-affinity glucose uptake machinery and operates principally when glucose is abundant. Its plasma-membrane role follows from extracellular glucose uptake; the system I mechanism is described as facilitated diffusion. Glucose transport is directly demonstrated, whereas a dedicated glucose-sensing role is established for the separate HGT transporters.

- carbohydrate:proton symporter activity: GLT-1 directly transports D-glucose. The gene-level system I assignment and its published diffusion mechanism do not support transferring the proton-coupled mechanism of system II; use the demonstrated substrate-specific transporter term.
- carbohydrate transport: The radiolabeled uptake and complementation experiments establish D-glucose transport. The substrate-specific transmembrane process is more informative than this broad transport annotation.
- membrane: A multipass MFS transporter mediating uptake of extracellular glucose is functionally located at the plasma membrane. This is a physiological localization inference from uptake experiments, not a claimed native microscopy measurement.
- transmembrane transporter activity: The substrate is experimentally resolved as D-glucose, so the generic transporter activity can be made substrate-specific.
- carbohydrate transmembrane transport: The radiolabeled uptake and complementation experiments establish D-glucose transport. The substrate-specific transmembrane process is more informative than this broad transport annotation.
- transmembrane transport: The radiolabeled uptake and complementation experiments establish D-glucose transport. The substrate-specific transmembrane process is more informative than this broad transport annotation.
- proton transmembrane transport: GLT-1 is assigned to the low-affinity system I described as glucose diffusion, whereas proton cotransport describes system II. A proton-transport annotation overstates the established mechanism for this target.

Primary evidence excerpts

- [PMID:24581151] “We conclude that NCU01633 is a D-glucose transporter of N. crassa, which was therefore named as D-glucose transporter 1 (GLT-1).”
- [PMID:28115989] “system I is a glucose diffusion system, while system II is an active, H+-co-transport mechanism;”

Provenance: live API snapshot 2026-09-09T03:00:51.831347+00:00. Complete API prediction JSON and all emitted claim IDs, text, and original evidence are preserved in the source and provenance JSON files. Current sequence/annotation data are separate comparison snapshots. Annotation overlap records known biology, not demonstrated training membership. All seven gene-focused Falcon jobs completed; the provider reports were inspected and useful primary leads checked. Publication retrieval used Europe PMC metadata/XML when the canonical PubMed fetch returned HTTP 429.

## 2026-09-20 full-gene reassessment

All eight rows and both primary full texts were assessed. PMID:24581151 heterologous expression/uptake identifies NCU01633 as GLT-1. PMID:28115989 Figures 2-5 and Methods directly address expression, glucose kinetics, mutants, complementation and eGFP localization (in yeast and Neurospora). The Discussion explicitly says “system I is a glucose diffusion system, while system II is an active, H+-co-transport mechanism”; GLT-1 is mapped to system I from kinetics/expression. These are substantive positive reasons to question coupling, but not a direct GLT-1 proton-flux assay. The Falcon report's evidence table similarly treats facilitated diffusion as less certain than glucose uptake.

Actual PTHR48022 tree places Q1K4S3 leaf PTN002362095 below PTN000627328, which bears membrane, carbohydrate transport and carbohydrate-proton symport IBDs. No negation is present in the recovered lineage. Broad transport/location terms are ACCEPT; coupling and its logical proton-transport derivative are UNDECIDED pending the focused report. The global OpenScientist GLT-1 hit concerns mammalian glutamate transport in Huntington disease and is not relevant to this fungal protein. No NEW assertion is necessary.

## 2026-10-10 OpenScientist proton-coupling follow-up

The focused OpenScientist report reconciled the PANTHER symporter IBA with target-specific evidence. I changed GO:0005351 carbohydrate:proton symporter activity from `UNDECIDED` to `MARK_AS_OVER_ANNOTATED`: PTN000627328 ancestry is current, but GLT-1 has Val48 at the TM1 position corresponding to the obligatory acidic protonation-site residue in XylE/STP symporters, while Neurospora HGT-1 and HGT-2 retain acidic residues there. The exact energetics still need a GLT-1 proton-flux assay, but the mechanism-specific symporter term is too strong for the established low-affinity D-glucose transporter.

The dependent GO:1902600 proton transmembrane transport IEA now moves to `REMOVE`, because it comes from the unsupported symport assumption rather than independent GLT-1 evidence. The D-glucose transporter core function remains unchanged.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: all nine existing_annotations rows, description and core function re-examined against PMID:24581151, PMID:28115989 (full text), PMID:16418173 (MstE abstract), the falcon deep-research file and the PANTHER/PAINT lineage. ProtNLM2 files were not opened.

Identity: Q1K4S3 is the sole UniProt entry for NCU01633 (532 aa, sequence version 1, TrEMBL, PE 3). It is the full-length product, not a fragment, isoform or alternative gene model: full MFS sugar-porter architecture (Pfam PF00083, TIGR00879, PROSITE PS00217) and the length matches HGT-1/HGT-2 (553/527 aa).

Evolutionary placement: PANTHER PTHR48022:SF92 "LOW AFFINITY GLUCOSE TRANSPORTER MSTE". PAINT lineage (glt-1-paint-lineage.json): leaf PTN002362095 -> SF92 nodes PTN001174959/PTN001174958/PTN002362094 (Pezizomycotina speciation) -> SF91 duplication -> SF2 nodes -> PTN000627328 (LUCA root, which carries the membrane, carbohydrate transport and carbohydrate:proton symporter IBDs). The A. nidulans low-affinity glucose transporter MstE (Q5B0S0, AN5860; PMID:16418173 [“fluorescence at the periphery of conidia and hyphae is consistent with MstE location in the plasma membrane”]) is in SF92 and is the closest characterised relative. MstE is a donor to the membrane and carbohydrate-transport IBDs but not to the symporter IBD; the symporter donors are SF6 Aspergillus transporters (Q5ASJ3, Q5AYG1), S. cerevisiae MAL11/AGT1 (S000003521) and S. pombe SPCC548.07c. MstE has its own IDA/IMP for GO:0055056 and IDA plasma membrane (AspGD), which supports transferring the glucose transporter activity and plasma membrane location within SF92.

Bioinformatics re-check (new files glt-1-bioinformatics/tm1_site_rereview.py, RESULTS-rereview.md): residue aligned to XylE Asp27 is Val48 in GLT-1, Ser67 in MstE, Asp52 in HGT-1, Asp35 in HGT-2, Asn29 in GLUT1 (control). This reproduces the earlier OpenScientist Val48 finding and extends it: the non-acidic residue is shared by the SF92 relative, which fits a subfamily-level loss of the protonation site.

Changes:
- Description rewritten (Km 18.42 mM, system I, SF92/MstE relation, energetics caveat).
- GO:0005351 IBA kept MARK_AS_OVER_ANNOTATED; reason extended with the MstE Ser67 result and donor analysis. GO:1902600 kept MARK_AS_OVER_ANNOTATED (dependent logical inference). Note that the 2026-10-10 section above says REMOVE for GO:1902600; the YAML had already been softened to MARK_AS_OVER_ANNOTATED and that stays.
- Broad but correct rows changed from ACCEPT to MODIFY, following the repo rule that correct-but-general terms get a specific replacement: GO:0008643 (IBA), GO:0034219, GO:0055085 -> GO:1904659 D-glucose transmembrane transport; GO:0016020 (IBA and IEA) -> GO:0005886 plasma membrane; GO:0022857 -> GO:0055056 D-glucose transmembrane transporter activity.
- GO:0055056 NEW (IDA, PMID:24581151) retained.
- Added references PMID:16418173 and file:NEUCR/glt-1/glt-1-bioinformatics/RESULTS-rereview.md; extra support for the core function from PMID:28115989.
- Not added: glucose sensing or carbon catabolite repression signalling. Transceptor evidence in PMID:28115989 is for HGT-1/HGT-2, not GLT-1, and the Avicel/cellulase phenotypes are downstream.

Family review: interpro/panther/PTHR48022/PTHR48022-review.yaml places glt-1 in SF92, which agrees with UniProt and the PAINT lineage. No disagreement. No module under modules/ references glt-1, NCU01633 or PTHR48022.

Next relative: A. nidulans mstE (Q5B0S0), SF92, no review in the repo (genes/EMENI has no mstE folder).
