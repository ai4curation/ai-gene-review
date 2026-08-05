# DGAT2 (Diacylglycerol O-acyltransferase 2) — review notes

UniProt: Q96PD7 (DGAT2_HUMAN), 388 aa. HGNC:16940. Gene on chromosome 11.

## Identity and function

DGAT2 catalyzes the terminal, only committed step of triacylglycerol (TAG)
biosynthesis: transfer of a long-chain acyl group from acyl-CoA to the sn-3
position of 1,2-diacyl-sn-glycerol (DAG), yielding TAG + CoA (EC 2.3.1.20).

- EC and reaction from UniProt: `DE   EC=2.3.1.20 {ECO:0000269|PubMed:16214399, ECO:0000269|PubMed:27184406}`
  and `Reaction=an acyl-CoA + a 1,2-diacyl-sn-glycerol = a triacyl-sn-glycerol + CoA; ... EC=2.3.1.20`
  [file:human/DGAT2/DGAT2-uniprot.txt].
- FUNCTION (UniProt): "Essential acyltransferase that catalyzes the terminal and only committed step
  in triacylglycerol synthesis by using diacylglycerol and fatty acyl CoA as substrates. Required for
  synthesis and storage of intracellular triglycerides (PubMed:27184406)."
  [file:human/DGAT2/DGAT2-uniprot.txt]. "In liver, is primarily responsible for incorporating
  endogenously synthesized fatty acids into triglycerides (By similarity)."
- DGAT2 is a member of the DGAT2/MOGAT family and has NO homology to DGAT1 (a MBOAT-family enzyme).
  From the cloning paper: DGAT2 "is a member of a gene family that has no homology with DGAT1"
  [PMID:11481335 "DGAT2 is a member of a gene family that has no homology with DGAT1"].
- Original cloning: expression in insect cells "stimulated triglyceride synthesis 6-fold" and activity
  "was dependent on the presence of fatty acyl-CoA and diacylglycerol, indicating that this protein is
  a DGAT. Activity was not observed for acyl acceptors other than diacylglycerol" [PMID:11481335].
- MgCl2 sensitivity distinguishes DGAT2 from DGAT1: "DGAT2 activity was inhibited by a high
  concentration (100 mm) of MgCl(2) in an in vitro assay, a characteristic that distinguishes DGAT2
  from DGAT1" [PMID:11481335].

## Secondary/moonlighting activities

- Acyl-CoA retinol O-fatty-acyltransferase (ARAT), EC 2.3.1.76:
  `Reaction=all-trans-retinol + an acyl-CoA = an all-trans-retinyl ester + CoA; ... EC=2.3.1.76;
  Evidence={ECO:0000269|PubMed:16214399}` [file:human/DGAT2/DGAT2-uniprot.txt]. NB: PMID:16214399's
  abstract foregrounds DGAT1 as the *major* ARAT; the DGAT2 ARAT EXP annotation reflects the full
  paper's assay of DGAT-family/MGAT enzymes ("enzymes involved in the synthesis of triacylglycerol,
  namely acyl coenzyme A:diacylglycerol acyltransferase (DGAT) ... are capable of carrying out the
  ... (ARAT) reaction"). Do not remove an EXP annotation on abstract grounds.
- Also uses 1-monoalkylglycerol (1-MAkG) as acyl acceptor to make monoalkyl-monoacylglycerol (MAMAG):
  from PMID:28420705 full text, "DGAT1, DGAT2, MGAT2, MGAT3, AWAT2/MFAT, and DC3 carried out both
  acylation steps resulting in synthesis of the final product, MADAG." DGAT2 is a minor player here
  and is highly selective for 1-MOG over 1-MAkG (~35-fold) [PMID:28420705].
- Has MGAT (2-acylglycerol O-acyltransferase) activity in vitro (Rhea-mapped GO:0003846). This is a
  side activity of the DGAT2/MOGAT-family fold; the paralog MGAT3 (also DGAT2-family) has both DGAT and
  MGAT activity [PMID:27184406 "MGAT3 possesses both DGAT and MGAT activities, in vitro"].

## Localization

- ER membrane, multi-pass: `SUBCELLULAR LOCATION: Endoplasmic reticulum membrane ... Multi-pass
  membrane protein ... Lipid droplet ... Cytoplasm, perinuclear region (PubMed:27184406)`
  [file:human/DGAT2/DGAT2-uniprot.txt]. Two TM helices (70-88, 93-112); most of the protein
  (incl. active site region) is cytoplasmic-facing (TOPO_DOM 113-388 Cytoplasmic).
- DGAT2 protein "was detected on endoplasmic reticulum" [PMID:14521909].
- In PMID:27184406, "unlike DGAT2, [MGAT3] does not become concentrated around the lipid droplet
  surface" — i.e., DGAT2 concentrates around the lipid-droplet surface (ER–LD contacts).

## Interactions / regulation

- Multimeric: "Forms multimeric complexes consisting of several DGAT2 subunits (By similarity)"
  [file:human/DGAT2/DGAT2-uniprot.txt] — basis for the IEA protein homodimerization annotation.
- Interacts with SLC27A1 (FATP1), enhanced by ZFYVE1/DFCP1: `Interacts with SLC27A1 and this
  interaction is enhanced in the presence of ZFYVE1 (PubMed:30970241)` [file:human/DGAT2/DGAT2-uniprot.txt].
  PMID:30970241 is about DFCP1/ZFYVE1 modulating ER–lipid-droplet contacts; the DGAT2 IPI
  (GO:0005515) uses WITH UniProtKB:Q6PCB7 (SLC27A1).
- Inhibited by niacin: `ACTIVITY REGULATION: Inhibited by niacin` [file:human/DGAT2/DGAT2-uniprot.txt].
- Drug target: ChEMBL CHEMBL5853; DrugBank Ervogastat (DB21489). Pharos Tchem.

## Physiology / disease

- Predominantly expressed in liver and white adipose tissue [PMID:11481335; PMID:14521909]. Major
  hepatic TAG-synthesizing enzyme; therapeutic target for hepatic steatosis / NAFLD.
- Pathway: `PATHWAY: Glycerolipid metabolism; triacylglycerol biosynthesis (PubMed:27184406)`.
- A heterozygous Y223H variant is associated with autosomal-dominant early-onset axonal Charcot-
  Marie-Tooth disease (uncertain significance) [PMID:26786738 via UniProt VARIANT 223].

## Curation reasoning for annotations

Core, strongly supported:
- MF: diacylglycerol O-acyltransferase activity (GO:0004144) — multiple EXP/IDA (PMID:11481335,
  PMID:16214399, PMID:27184406) + IBA. Core.
- BP: triglyceride biosynthetic process (GO:0019432) — IDA (PMID:27184406, PMID:11481335) + IBA/TAS. Core.
- CC: ER membrane (GO:0005789) — IDA (PMID:27184406) + IC/ISS/IBA/TAS. Core.
- CC: lipid droplet (GO:0005811) — IDA (PMID:27184406). Core.
- BP: long-chain fatty-acyl-CoA metabolic process (GO:0035336) — IDA (PMID:11481335). Core-adjacent
  (reflects acyl-CoA substrate use / channeling endogenous FAs into TAG).
- BP: diacylglycerol metabolic process (GO:0046339) — IDA (PMID:11481335) + IBA. DAG is the substrate;
  keep (metabolic parent of the reaction).

Secondary MF (keep, non-core or over-annotated):
- retinol O-fatty-acyltransferase activity (GO:0050252) — EXP (PMID:16214399) + IEA(EC). Real side
  activity (ARAT); non-core.
- 2-acylglycerol O-acyltransferase activity (GO:0003846) — IEA Rhea. In-vitro MGAT side activity;
  keep as non-core.
- retinol metabolic process (GO:0042572) — IEA inter-ontology from GO:0050252. Follows the ARAT side
  activity; non-core.
- monoacylglycerol biosynthetic process (GO:0006640) — IDA (PMID:28420705); this is the MAMAG/ether-
  lipid side activity, minor for DGAT2 (35-fold selective against it). Keep as non-core.

Grouping/generic MF:
- acyltransferase activity, transferring groups other than amino-acyl groups (GO:0016747) — IEA
  InterPro/ARBA parent of GO:0004144; redundant generic. Over-annotated.
- protein binding (GO:0005515) — IPI with SLC27A1 (PMID:30970241). Uninformative bare term;
  mark over-annotated (never remove IPI).
- protein homodimerization activity (GO:0042803) — IEA(Ensembl) from mouse; UniProt says "multimeric
  complexes of several DGAT2 subunits (By similarity)". Keep as non-core.

Localization (keep; core ones ACCEPT, others non-core):
- ER (GO:0005783) IDA, ER membrane IC/TAS/ISS, perinuclear ER membrane (GO:1990578) IDA, membrane
  (GO:0016020) IDA — all consistent with multi-pass ER membrane protein.
- perinuclear region of cytoplasm (GO:0048471) ISS/IEA — consistent with "Cytoplasm, perinuclear
  region" in UniProt; non-core.
- mitochondrion (GO:0005739) colocalizes_with, IEA/ISS from mouse Q9DCV3 — DGAT2 is reported at
  ER–mitochondria / mitochondria-associated membranes in rodents; colocalizes_with qualifier is weak.
  Keep as non-core (do not remove — ISS from experimental mouse ortholog).

Physiology BP terms transferred by ISS/IEA from rodent orthologs (Q9DCV3 mouse, Q5FVP8 rat) — these
describe organism-level roles of DGAT2, largely correct but peripheral to the molecular core:
- lipid storage (GO:0019915), fat pad development (GO:0060613), fatty acid homeostasis (GO:0055089),
  intracellular triglyceride homeostasis (GO:0035356), cellular response to oleic acid (GO:0071400):
  KEEP_AS_NON_CORE (well supported by KO/physiology of orthologs).
- cholesterol homeostasis (GO:0042632), regulation of cholesterol metabolic process (GO:0090181),
  low-density lipoprotein particle clearance (GO:0034383), regulation of plasma lipoprotein particle
  levels (GO:0097006), regulation of lipoprotein metabolic process (GO:0050746), positive regulation
  of gluconeogenesis (GO:0045722), negative regulation of fatty acid oxidation (GO:0046322),
  response to nutrient (GO:0007584): downstream/indirect physiological consequences of altered TAG
  synthesis, not direct DGAT2 functions. KEEP_AS_NON_CORE (over-annotation-leaning but rodent-
  supported); do not treat as core.
- positive regulation of triglyceride biosynthetic process (GO:0010867) IEA from rat — DGAT2 *performs*
  TAG biosynthesis rather than *regulating* it; regulatory framing is awkward. KEEP_AS_NON_CORE.
- diacylglycerol biosynthetic process (GO:0006651) ISS/IEA from mouse — DGAT2 consumes DAG to make
  TAG; it does not synthesize DAG. Its MGAT side activity does make DAG from MAG in vitro, so this is
  defensible as a minor activity. KEEP_AS_NON_CORE.

References PMID:14521909 (psoriatic skin / diabetic mice; ER localization), PMID:11481335 (cloning),
PMID:16214399 (ARAT), PMID:27184406 (DGAT/localization), PMID:28420705 (ether lipid/MAMAG),
PMID:30970241 (SLC27A1 interaction) all verified against cached abstracts/full text.
