# NDUFA12 (B17.2) review notes

## Identity (authoritative: UniProt)
- UniProt entry: **Q9UI09**, name **NDUAC_HUMAN**, gene **NDUFA12** (synonym DAP13), 145 aa, human (NCBITaxon:9606).
  [file:human/NDUFA12/NDUFA12-uniprot.txt "ID   NDUAC_HUMAN"; "GN   Name=NDUFA12; Synonyms=DAP13;"]
- RecName: "NADH dehydrogenase [ubiquinone] 1 alpha subcomplex subunit 12"; AltNames "13 kDa differentiation-associated protein" (hence DAP13), "Complex I-B17.2 / CI-B17.2", "NADH-ubiquinone oxidoreductase subunit B17.2".
  [file:human/NDUFA12/NDUFA12-uniprot.txt "AltName: Full=13 kDa differentiation-associated protein"; "AltName: Full=Complex I-B17.2"]

## Core biology
- **Accessory (supernumerary) subunit of Complex I** (NADH:ubiquinone oxidoreductase), the first enzyme of the mitochondrial respiratory chain (45 subunits in humans). It is a **genuine stable subunit of the mature holoenzyme**, located in the **peripheral (matrix) arm** near the N/Q-module junction. **Non-catalytic** ("believed not to be involved in catalysis").
  [file:human/NDUFA12/NDUFA12-uniprot.txt "Accessory subunit of the mitochondrial membrane respiratory"; "chain NADH dehydrogenase (Complex I), that is believed not to be"; "involved in catalysis."]
- Complex I transfers electrons from NADH to the respiratory chain; the immediate electron acceptor is ubiquinone.
  [file:human/NDUFA12/NDUFA12-uniprot.txt "Complex I functions in the transfer of electrons"; "from NADH to the respiratory chain. The immediate electron acceptor for"]
- **Subcellular location:** mitochondrion inner membrane; peripheral membrane protein; matrix side.
  [file:human/NDUFA12/NDUFA12-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion inner membrane"; "Matrix side"]
- **SIMILARITY:** "Belongs to the complex I NDUFA12 subunit family."
  [file:human/NDUFA12/NDUFA12-uniprot.txt "Belongs to the complex I NDUFA12 subunit family."]

## NDUFA12 vs NDUFAF2 (do NOT conflate)
- **NDUFA12 is the mature-enzyme subunit**, NOT the assembly factor. Its paralog **NDUFAF2 (a.k.a. NDUFA12L)** is the assembly factor.
- In NDUFA12-knockout cells, Complex I assembly is not affected, "probably due to substitution by the NDUFAF2 paralog."
  [file:human/NDUFA12/NDUFA12-uniprot.txt "In NDUFA12-knockout cells, complex I assembly is not"; "affected, probably due to substitution by the NDUFAF2 paralog."]
- Consequence for BP annotation: unlike many accessory subunits, NDUFA12 is dispensable for *assembly* per se (its slot can be filled by NDUFAF2), so the strongest core BP is electron transport / OXPHOS rather than complex-I assembly. It is nonetheless required for a fully mature, correctly functioning complex, and its loss causes disease (below).

## Disease
- **Mitochondrial complex I deficiency, nuclear type 23 (MC1DN23)** [MIM:618244]; autosomal recessive; NDUFA12 mutations are a cause of Leigh syndrome. A truncating variant (60-Arg--Lys-145 del) is documented.
  [file:human/NDUFA12/NDUFA12-uniprot.txt "Mitochondrial complex I deficiency, nuclear type 23 (MC1DN23)"; PMID:21617257 (Ostergaard et al. 2011, J Med Genet) "Respiratory chain complex I deficiency due to NDUFA12 mutations as a new cause of Leigh syndrome"]

## Evidence sources for existing annotations
- **PMID:12611891** (Murray et al. 2003, JBC) — one-step immunopurification of human Complex I; MS identifies human homologues of 42 polypeptides including "a protein thought to be in differentiation linked processes" (= DAP13/NDUFA12). Basis for IDA part_of Complex I. Abstract-only in cache (full_text_available: false).
- **PMID:27626371** (Stroud et al. 2016, Nature) — CRISPR knockout of each accessory subunit + quantitative proteomics; "25 subunits are strictly required for assembly of a functional complex." Basis for FUNCTION (accessory, not catalytic) and IDA part_of Complex I. Abstract-only in cache.
- **PMID:28844695** (Guo et al. 2017, Cell) — cryo-EM of human megacomplex I2III2IV2; "reveals the precise assignment of individual subunits of human CI". Basis for ComplexPortal IDA inner membrane + IPI part_of Complex I. Abstract-only in cache.
- **PMID:30030361** (Signes & Fernandez-Vizarra 2018, Essays Biochem) — review of OXPHOS assembly; supernumerary subunits "play essential roles in assembly, regulation and stability." Basis for ComplexPortal NAS aerobic respiration + NAS proton-motive-force ATP synthesis (complex-level roles, NAS). Abstract-only in cache.
- **PMID:24746669** (Wang et al. 2014, Dev Cell) — cyclin B1/Cdk1 phosphorylates CI subunits to enhance CI activity for G2/M. Used for IMP part_of Complex I and IMP "mitochondrial ATP synthesis coupled electron transport." Abstract-only in cache; the abstract concerns CI subunits generically (does not name NDUFA12); curator (UniProt/CAFA) read full text — do not overrule, but these are complex-level BP claims better treated as context (KEEP_AS_NON_CORE / defer) rather than core NDUFA12-specific evidence.
- **PMID:32296183** (Luck et al. 2020, Nature — HuRI) — human binary interactome; source of the three IntAct IPI "protein binding" annotations (partners TMED8/Q6PL24, MYO15B/Q96JP2, SYT4/Q9H2B2). Full text available but NDUFA12/partners appear only in supplementary data, not main text (no verbatim main-text quote). These Y2H binary hits are not the biologically relevant Complex I contacts → over-annotation of the uninformative "protein binding" term.
- **PMID:34800366** (FlyBase HTP mitochondrion) and **GO_REF:0000052** (HPA IDA) — localization to mitochondrion; consistent but coarser than inner-membrane/Complex I.
- **PMID:10830904** (Triepels et al. 2000, Hum Genet) — original cDNA characterization of the 17.2-kDa (B17.2) subunit; the NAS "NADH dehydrogenase (ubiquinone) activity" (GO:0008137) enables annotation reflects the name of the enzyme, not an independent catalytic activity of this non-catalytic subunit.

## Annotation decisions (summary)
- **Complex I membership (GO:0045271) — multiple lines (IBA, IEA, IDA×2 exp, IMP, IPI):** the IDA/IMP/IPI experimental ones = ACCEPT (core structural fact). Redundant IEA/IBA = ACCEPT/KEEP_AS_NON_CORE (defer to experimental).
- **Localization:** inner membrane IDA (ComplexPortal, PMID:28844695) = ACCEPT (core, matrix-side peripheral). IEA inner membrane, mitochondrion (Ensembl/HPA/FlyBase), Reactome TAS inner membrane = ACCEPT/KEEP_AS_NON_CORE (consistent, coarser or redundant). `membrane` (GO:0016020, InterPro IEA) = MARK_AS_OVER_ANNOTATED (too general given the specific inner-membrane localization).
- **MF GO:0008137 "NADH dehydrogenase (ubiquinone) activity" enables (NAS, PMID:10830904):** MARK_AS_OVER_ANNOTATED — NDUFA12 is explicitly non-catalytic; it *contributes to* the complex-level activity but does not *enable* it. Correct representation in core_functions: molecular_function = GO:0005198 (structural molecule activity), contributes_to = GO:0008137.
- **MF GO:0005515 "protein binding" (IPI×3, PMID:32296183/HuRI):** MARK_AS_OVER_ANNOTATED per policy (never REMOVE a bare protein-binding IPI); uninformative term, binary-interactome partners not the Complex I contacts.
- **BP proton transmembrane transport (GO:1902600, IEA GO_REF:0000108 from GO:0008137):** MARK_AS_OVER_ANNOTATED — inferred from the MF that itself is an over-annotation for this non-catalytic subunit; NDUFA12 does not itself pump protons.
- **BP proton motive force-driven ATP synthesis (GO:0042776, NAS) & aerobic respiration (GO:0009060, NAS):** complex-level roles; KEEP_AS_NON_CORE (true of Complex I as a whole, not a distinct NDUFA12 molecular contribution).
- **BP mitochondrial ATP synthesis coupled electron transport (GO:0042775, IMP, PMID:24746669):** KEEP_AS_NON_CORE — experimental (do not REMOVE), but the paper is about generic CI-subunit phosphorylation in the cell cycle, not NDUFA12's core evolved function.

## Core function (synthesis)
- MF: **GO:0005198 structural molecule activity** (honest, non-catalytic).
- contributes_to: **GO:0008137 NADH dehydrogenase (ubiquinone) activity** (complex-level).
- BP: **GO:0006120 mitochondrial electron transport, NADH to ubiquinone** and **GO:0032981 mitochondrial respiratory chain complex I assembly** (structural role in a mature, functional complex).
- location: **GO:0005743 mitochondrial inner membrane** (matrix-side peripheral).
- in_complex: **GO:0045271 respiratory chain complex I**.
