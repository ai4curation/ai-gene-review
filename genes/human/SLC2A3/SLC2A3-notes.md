# SLC2A3 (GLUT3) review notes

UniProt: P11169 (GTR3_HUMAN). HGNC: SLC2A3. Gene aliases: GLUT3. 496 aa.
Taxon: Homo sapiens (NCBITaxon:9606).

## Summary of function (synthesis)

GLUT3 is a **facilitative** (energy-independent, Na+-independent) glucose uniporter of the
major facilitator superfamily (MFS), sugar transporter (TC 2.A.1.1) / GLUT (SLC2) family,
glucose-transporter subfamily. It is the principal **high-affinity, neuronal** glucose
transporter but is expressed in many other tissues (sperm, platelets, placenta, embryonic
cells, leukocytes). It moves D-glucose down its concentration gradient across the plasma
membrane by alternating-access conformational cycling; the C-terminal domain provides the
primary substrate-binding site.

Substrate profile (from kinetics + structure):
- Primary: **D-glucose** (high affinity; Km for 2-deoxyglucose ~1.4–1.5 mM, vs ~11 mM for GLUT2)
  [PMID:8457197; PMID:9477959 "Km values for deoxyglucose transport of approximately 11 mM and approximately 1.5 mM, respectively"].
- Also transports (genuine secondary substrates): **galactose** (Km 8.5 mM), mannose, xylose,
  fucose, 2-deoxyglucose, and **dehydroascorbate (DHA)** (Km ~1.7 mM).
- **Does NOT transport fructose** — this is a defining distinction from GLUT2/GLUT5
  [PMID:9477959 "GLUT2 is capable of D-fructose transport, while GLUT3 is not"; also PMID:26176916].
  The QLS motif (residues 277–279, TM7) governs selectivity against fructose; the QLS→HVA mutant
  gains fructose transport [PMID:9477959; UniProt REGION 277-279 "Important for selectivity against fructose"].

Facilitated diffusion / uniport — there is NO coupling to Na+ or any ion and NO active transport.
Any symporter / active-transport / Na+-coupled term would be wrong-mode for this protein.

## Key evidence by source

- **PMID:8457197** (Colville et al. 1993, Biochem J): expressed human GLUT2 and GLUT3 in Xenopus
  oocytes. "GLUT2 mediates the transport of fructose and galactose, and GLUT3 mediates the
  transport of galactose." Competitive inhibition of GLUT3 deoxyglucose transport by D-glucose,
  D-galactose, maltose; cytochalasin B non-competitive. Basis of NOT-fructose and galactose IDA rows.
- **PMID:9477959** (Seatter et al. 1998, Biochemistry): QLS motif in TM7 controls substrate
  selection; GLUT3 high-affinity (Km ~1.5 mM deoxyglucose). Explicit: GLUT3 does NOT transport
  fructose. IMP plasma-membrane row.
- **PMID:26176916** (Deng et al. 2015, Nature): 1.5 Å crystal structure of human GLUT3 bound to
  D-glucose, outward-occluded; plus maltose-bound outward-open/occluded. "the C-terminal domain
  provides the primary substrate-binding site". Six D-glucose binding residues (159, 280-281, 286,
  315, 378, 386). Basis of D-glucose binding (IDA), transporter activity (IDA), membrane (IDA),
  D-glucose transmembrane transport (IDA).
- **PMID:9228080** (Rumsey et al. 1997, JBC): "Glucose transporter isoforms GLUT1 and GLUT3
  transport dehydroascorbic acid." Km DHA via GLUT3 1.7 mM; DHA reduced to ascorbate inside cells.
  GLUT2/GLUT5/SGLT1 do NOT transport DHA. Basis of DHA transporter activity (EXP).
- **PMID:10862609** (Rumsey et al. 2000, JBC): title names GLUT4 but abstract/full text assay
  GLUT3: "Dehydroascorbic acid (DHA), the first stable oxidation product of vitamin C, was
  transported by GLUT1 and GLUT3 in Xenopus laevis oocytes". Legitimate GLUT3 DHA evidence —
  do NOT remove as paralog mis-attribution (full text covers GLUT3).
- **PMID:1695905** (Kayano et al. 1990, JBC): the GLUT5 isolation paper; mentions brain/GLUT3.
  Source of the NAS carbohydrate-metabolic-process and TAS glucose-transport rows (cloning-era
  author statements).
- **PMID:23975336** (Meireles et al. 2013, J Membr Biol): human BBB cell model (hCMEC/D3) expresses
  GLUT1, GLUT3, SGLT1 mRNA; 2-deoxy-D-glucose uptake Na+- and energy-independent. IGI rows for
  D-glucose import and transport-across-BBB (WITH GLUT1 P11166, SGLT1 P13866). GLUT1 is the
  canonical BBB endothelial transporter; GLUT3's barrier-crossing role is secondary → non-core.
- **PMID:35810171** (Fu et al. 2022, Nat Commun): micropeptide NEMEP/SMIM43 (Q4W5P6) "interacts
  with the glucose transporters GLUT1/GLUT3 and promotes glucose uptake likely through these
  interactions"; role in mesendoderm differentiation. UniProt SUBUNIT: interaction with SMIM43.
- **PMID:32296183** (Luck et al. 2020, HuRI) & **PMID:36115835** (Gogl et al. 2022, PDZ
  fragmentomics): large-scale binary / PDZ interactome screens. GLUT3 C-terminus
  (...IEPAKETTTNV) is bound by many PDZ-domain scaffolds (DLG1-4, MAGI1/2, MPDZ, PATJ, PDZK1,
  TJP1, GRIP1/2, WHRN, LNX1/2, FRMPD2, etc.). These are bare protein-binding (GO:0005515) rows →
  REMOVE per protein-binding policy (uninformative; interactions not asserted false).
- **PMID:20458337** (Buschow et al. 2010): B-cell exosome proteome — GLUT3 detected (HDA
  extracellular exosome). Proteomic localization, peripheral.
- Reactome rows: neutrophil-degranulation granule-membrane localizations (secretory/specific/
  tertiary/ficolin-1-rich granule membrane), plasma membrane DHA/Glc transport reactions, and
  vitamin C (ascorbate) metabolism. GLUT3 is expressed in leukocytes and traffics in granule
  membranes; genuine but peripheral to the core neuronal glucose-uptake function.

## SLC2A14/GLUT14 note
SLC2A14 (GLUT14) is a near-identical duplicate of GLUT3 (not in this batch); not relevant to
the annotation decisions here but explains high sequence-similarity hits.

## Action plan rationale
- Core MF: GO:0055056 D-glucose transmembrane transporter activity (facilitative uniport).
- Core BP: GO:0098708 D-glucose import across plasma membrane; GO:1904659 D-glucose transmembrane transport.
- Core location: GO:0005886 plasma membrane.
- Non-core genuine secondary activities: galactose (GO:0005354/GO:0015757), DHA
  (GO:0033300/GO:0070837), vitamin C metabolism context (GO:0019852).
- Non-core locations: perikaryon (neuronal), exosome, neutrophil granule membranes.
- MODIFY GO:0016020 membrane → GO:0005886 plasma membrane.
- TOO_GENERAL: GO:0022857 transmembrane transporter activity, GO:0055085 transmembrane transport
  (entailed by the specific D-glucose transporter activity/transport asserted).
- MARK_AS_OVER_ANNOTATED: GO:0005975 carbohydrate metabolic process (a facilitative transporter
  does not chemically metabolize sugars; NAS cloning-paper statement).
- ACCEPT negated: GO:0005353 fructose transporter activity (NOT), GO:0015755 fructose transport (NOT).
- REMOVE: all GO:0005515 protein binding IPI rows (19) per protein-binding policy.
