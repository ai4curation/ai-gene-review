# ABCC11 (MRP8) curation notes

UniProt: Q96J66 (MRP8_HUMAN). HGNC:14639. Chromosome 16q12.1, tandemly duplicated with ABCC12.
NCBI Gene 85320. 1382 aa, full-length ABCC/MRP topology (two TMD-NBD halves; 12 TM helices
predicted; two Walker-A ATP-binding sites at 544-551 and 1175-1182). No rodent ortholog
[file:human/ABCC11/ABCC11-uniprot.txt "This protein has no ortholog in rodents"].

## Core biology

ABCC11/MRP8 is an ATP-dependent plasma-membrane efflux pump for lipophilic organic anions.
It belongs to the ABC transporter superfamily, ABCC family, conjugate transporter
(TC 3.A.1.208) subfamily. EC 7.6.2.2 (xenobiotic-transporting ATPase) and EC 7.6.2.3
(glutathione-S-conjugate-transporting ATPase).

### Molecular function / substrates (experimental)

- Cyclic nucleotide efflux: ectopic MRP8 lowers basal cAMP/cGMP and enhances cyclic
  nucleotide extrusion; competent in in vitro cAMP and cGMP transport
  [PMID:12764137 "ectopic expression of MRP8 reduces basal intracellular levels of cAMP and cGMP and enhances cellular extrusion of cyclic nucleotides"]
  [PMID:12764137 "MRP8 is an amphipathic anion transporter that is able to efflux cAMP and cGMP"]
  [PMID:15537867 "MRP8 is competent in the in vitro transport of cAMP and cGMP"].
- Glutathione S-conjugates (LTC4, DNP-SG), steroid sulfates (DHEAS, estrone-3-sulfate),
  glucuronide E217betaG, monoanionic bile acids (glycocholate, taurocholate), methotrexate
  [PMID:15537867 "the glutathione S-conjugates leukotriene C4 and dinitrophenyl S-glutathione, steroid sulfates such as dehydroepiandrosterone 3-sulfate (DHEAS) and estrone 3-sulfate, glucuronides such as estradiol 17-beta-D-glucuronide"].
  Kinetics: DHEAS Km 13 uM; E217betaG Km 62.9 uM; methotrexate Km 957 uM (PMID:15537867).
- Apical efflux pump for steroid sulfates; axonal protein; ATP-dependent DHEAS transport
  Km 21 uM in inside-out plasma membrane vesicles
  [PMID:16359813 "an apical efflux pump for steroid sulfates"]
  [PMID:16359813 "Inside-out plasma membrane vesicles containing recombinant ABCC11 mediated ATP-dependent transport of dehydroepiandrosterone 3-sulfate with a Km value of 21 microM"].
- Xenobiotic/drug efflux and resistance: confers resistance to 5-FU, 5-FdUR, ddC, PMEA by
  transporting the active metabolite 5-FdUMP
  [PMID:12764137 "MRP8 is able to confer resistance to fluoropyrimidines by mediating the MgATP-dependent transport of 5'-fluoro-2'-deoxyuridine monophosphate"]
  [PMID:25896536 "an efflux transporter for anionic lipophilic compounds, conferring resistance to antiviral and anticancer agents like 5-fluorouracil (5-FU)"].
  T546M variant markedly reduces 5-FdUMP transport
  [PMID:25896536 "exhibiting markedly reduced transport function of 5-FdUMP, the active cytotoxic metabolite of 5-FU"].

### Localization

- Plasma/cell membrane (polytopic integral membrane protein); apical cell membrane in
  polarized MDCK cells; axonal membranes of CNS/PNS (PMID:16359813).
  [PMID:16359813 "ABCC11 was expressed in polarized Madin-Darby canine kidney cells where it was sorted to the apical membrane"].
- Intracellular granules / large vacuoles and luminal membrane in cerumen gland secretory
  cells (PMID:19383836); cytoplasmic vesicle membrane (PMID:25896536) — intracellular
  trafficking/storage pools, non-core.
- Extracellular exosome: HDA from a urinary-exosome proteomic survey (PMID:19056867);
  consistent with shedding of a membrane protein, not a functional site. Non-core.

### Physiology / phenotype

- Earwax type and axillary odor: SNP 538G>A (Gly180Arg) determines dry (recessive) vs wet
  earwax; the Arg180 variant lacks N-glycosylation, is recognized as misfolded in the ER
  and undergoes proteasomal degradation
  [PMID:19383836 "This SNP variant lacking N-linked glycosylation is recognized as a misfolded protein in the endoplasmic reticulum and readily undergoes ubiquitination and proteasomal degradation, which determines the dry type of earwax as a mendelian trait with a recessive phenotype"].
- Apocrine odorant-precursor secretion (glutamine and Cys-Gly-S conjugates of
  3-methyl-3-sulfanylhexanol) per UniProt FUNCTION (PMID:19710689, not in cache).

## Curation decisions summary (44 rows)

- Plasma membrane rows (EXP/EXP/IBA/IDA/IEA/TAS): ACCEPT (core location).
- Apical plasma membrane (IDA, IEA): ACCEPT (core, polarized apical pump).
- GO:0016020 membrane (IEA): MODIFY -> GO:0005886 plasma membrane (generic -> specific,
  per ABC-transporter consistency).
- Vacuolar membrane (EXP, IEA) and cytoplasmic vesicle membrane (EXP, IEA): KEEP_AS_NON_CORE
  (real intracellular pools, not site of physiological efflux).
- Extracellular exosome (HDA): KEEP_AS_NON_CORE (proteomic shedding detection).
- Specific transporter activities ACCEPT: ABC-type xenobiotic (EXP/EXP/IDA/IEA), GS-conjugate
  (IDA, IEA), bile acid (IDA), purine nucleotide (IBA/IDA/IDA), cyclic GMP (EXP/EXP),
  plus ATP binding (IEA) and ATP hydrolysis (IEA) as core mechanism.
- Specific processes ACCEPT: bile acid/salt transport (IBA, IDA), purine nucleotide transport
  (IDA, IDA), xenobiotic transport (IDA), leukotriene transport (IDA), guanine nucleotide
  transmembrane transport (IEA logical inference from cyclic-GMP activity).
- Root/parent terms TOO_GENERAL (entailed by specific accepted terms): transmembrane
  transporter activity (GO:0022857), ATPase-coupled transmembrane transporter activity
  (GO:0042626), transmembrane transport (GO:0055085 x5), ABC-type transporter activity
  (GO:0140359 x2).
- GO:0015216 purine nucleotide transporter kept ACCEPT (covers cAMP, which the more specific
  cyclic-GMP term does not entail), not TOO_GENERAL.

No REMOVE actions were warranted: all rows are either correct, correct-but-general
(TOO_GENERAL/MODIFY), or real non-core localizations. No bare GO:0005515 protein binding row
present. All cited publications are abstract-only (full_text_available: false); supporting
quotes are drawn only from the cached abstracts, the UniProt flat file, and the cited Reactome
entries. No UNDECIDED rows: every cited abstract was accessible and sufficient to judge the
claim (experimental transport/localization data are stated directly in the abstracts).

## Sources
- UniProtKB Q96J66 (MRP8_HUMAN) flat file.
- PMID:12764137, PMID:15537867, PMID:16359813, PMID:19383836, PMID:25896536, PMID:19056867
  (abstracts).
- Reactome R-HSA-1454916, R-HSA-382556.
