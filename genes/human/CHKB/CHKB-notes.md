# CHKB (choline kinase beta) review notes

UniProt: Q9Y259 (CHKB_HUMAN). HGNC:1938. Chromosome 22. 395 aa.
Names: Choline/ethanolamine kinase; Choline kinase beta; Ethanolamine kinase beta;
Choline kinase-like protein. EC 2.7.1.32 (choline kinase) and EC 2.7.1.82 (ethanolamine kinase).

## Core biology (from local UniProt record: file:human/CHKB/CHKB-uniprot.txt)

- Enzyme of the CDP-choline (Kennedy) pathway; catalyzes the **first, committed step** of
  phosphatidylcholine biosynthesis (choline -> phosphocholine) and, in parallel, the first step of
  phosphatidylethanolamine biosynthesis (ethanolamine -> phosphoethanolamine).
  UniProt FUNCTION: "Has a key role in phospholipid metabolism, and catalyzes the first step of
  phosphatidylethanolamine and phosphatidylcholine biosynthesis."
  [ECO:0000269|PubMed:19915674, ECO:0000269|PubMed:21665002]
- Two catalytic activities documented in the UniProt record:
  - choline + ATP = phosphocholine + ADP + H(+)  (EC 2.7.1.32; RHEA:12837)
  - ethanolamine + ATP = phosphoethanolamine + ADP + H(+)  (EC 2.7.1.82; RHEA:13069)
- Kinetics (PubMed:19915674): KM 0.57 mM for choline; KM 2.9 mM for ethanolamine.
- SUBUNIT: "Homodimer, and heterodimer with CHKA." [ECO:0000269|Ref.12] (Ref.12 = SGC PDB submission;
  a structural/crystallographic characterization, not a PMID.) The choline kinase family enzymes act
  as obligate dimers.
- Subcellular location: cytosolic (no membrane/organelle-targeting features; Reactome places the
  reaction "In the cytosol"). N-terminal Met removed; N-acetyl-Ala at position 2.
- PATHWAY (UniProt): "Phospholipid metabolism; phosphatidylethanolamine biosynthesis;
  phosphatidylethanolamine from ethanolamine: step 1/3." Also UniPathway UPA00558 / UER00741.
- Disease: **Muscular dystrophy, congenital, megaconial type (MDCMC)** [MIM:602541], autosomal
  recessive. UniProt: "early-onset muscle wasting, intellectual disability, and dilated
  cardiomyopathy in half of affected individuals ... peculiar enlarged mitochondria that are
  prevalent toward the periphery of the fibers but are sparse in the center."
  [ECO:0000269|PubMed:21665002, 22782513, 24997086, 25187204, 26006750, 26067811]
- MISCELLANEOUS: bicistronic locus that also produces CPT1B from a non-overlapping reading frame.
- Family: choline/ethanolamine kinase family (Pfam PF01633; PANTHER PTHR22603). Structures solved
  (PDBs 2IG7, 3FEG, 3LQ3) with ADP/Mg and hemicholinium-3.

## Key primary evidence

- PubMed:19915674 (Gallego-Ortega et al. 2009, PLoS One; full_text_available: true) — direct
  biochemical characterization of human ChoKalpha1 vs ChoKbeta. IDA source in GOA for
  choline kinase activity, ethanolamine kinase activity, and PE biosynthesis.
  Verbatim: "Both ChoKalpha1 and ChoKbeta displayed choline and ethanolamine kinase activities
  under these experimental conditions" [PMID:19915674]. Note the paper's *in vivo* finding that
  overexpressed ChoKbeta behaves preferentially as an ethanolamine kinase whereas ChoKalpha1 is
  dual choline/ethanolamine: "Whereas ChoKbeta display an ethanolamine kinase role, ChoKalpha1
  present a dual choline/ethanolamine kinase role" [PMID:19915674]. Both intrinsic activities are
  nonetheless real and measured; the GOA IDA rows for CHKB are appropriate.
  Also establishes dimeric behaviour: "the beta/beta homodimer the less active" (family acts as
  dimers) [PMID:19915674].

- PubMed:21665002 (Mitsuhashi et al. 2011, Am J Hum Genet; full_text_available: false — abstract
  only). EXP source in GOA for choline kinase activity. Identifies CHKB as the MDCMC gene.
  Abstract, verbatim: "we have identified homozygous or compound heterozygous mutations in the gene
  encoding choline kinase beta (CHKB). This is the first enzymatic step in a biosynthetic pathway
  for phosphatidylcholine"; "In muscle of three affected individuals with nonsense mutations,
  choline kinase activities were undetectable, and phosphatidylcholine levels were decreased."
  [PMID:21665002]. Loss-of-function directly demonstrates CHKB choline kinase activity and its role
  in PC biosynthesis in vivo (human muscle).

- Reactome R-HSA-1483004 ("Cho is phosphorylated to PCho by CHK dimer") and R-HSA-1483222 ("ETA is
  phosphorylated to PETA by CHK/ETNK") — both place the CHKB-containing dimer reactions in the
  cytosol, and explicitly note the CHKA:CHKB heterodimer and CHKB homodimer. TAS source in GOA for
  cytosol.

## Curation decisions

- Molecular function — **choline kinase activity (GO:0004103)**: IDA (PMID:19915674) and EXP
  (PMID:21665002) directly support it -> ACCEPT (core). IBA and IEA rows for the same term ->
  ACCEPT / KEEP as they agree with experiment (redundant but not wrong).
- Molecular function — **ethanolamine kinase activity (GO:0004305)**: IDA (PMID:19915674) supports
  it directly (measured in cell extracts and recombinant enzyme) -> ACCEPT (core). IBA/IEA rows agree.
  CHKB is a genuine dual-substrate choline/ethanolamine kinase (the "choline/ethanolamine kinase"
  RecName reflects this).
- BP — **phosphatidylethanolamine biosynthetic process (GO:0006646)**: IDA (PMID:19915674), plus
  IBA and IEA. CHKB catalyzes the first step of PE biosynthesis (ethanolamine kinase branch) ->
  ACCEPT (core-ish; this is the pathway UniProt assigns as step 1/3).
- BP — **CDP-choline pathway (GO:0006657)** (IBA): CHKB catalyzes the first step of the CDP-choline
  (Kennedy) pathway for PC synthesis -> ACCEPT (core process). This is arguably the most disease-
  relevant CHKB process (MDCMC arises from defective de novo PC biosynthesis).
- CC — **cytosol (GO:0005829)** (TAS, Reactome x2): CHKB is a soluble cytosolic enzyme -> ACCEPT.
- CC — **cytoplasm (GO:0005737)** (IBA): correct but less specific than cytosol -> KEEP_AS_NON_CORE
  (redundant with the more precise cytosol annotation).
- **ATP binding (GO:0005524)** is not a separate GOA row here (UniProt keyword only), but is a real
  core molecular capability (multiple ATP BINDING sites in the record); include in core_functions.
- No REMOVE actions: the IEA rows (GO_REF:0000120, ARBA/Rhea/EC-based) map correctly to the two
  catalytic activities and to PE biosynthesis, matching the experimental data, so they are not
  clearly-wrong IEA.

## Core function summary

CHKB is a cytosolic choline/ethanolamine kinase that phosphorylates choline (and ethanolamine) using
ATP, providing phosphocholine for the CDP-choline (Kennedy) pathway of phosphatidylcholine synthesis
and phosphoethanolamine for phosphatidylethanolamine synthesis. It functions as a homodimer or as a
heterodimer with CHKA. It is especially important for phosphatidylcholine homeostasis in muscle and
brain; loss of function causes megaconial congenital muscular dystrophy (MDCMC).
