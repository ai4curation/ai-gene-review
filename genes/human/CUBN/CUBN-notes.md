# CUBN (Cubilin) — review notes

UniProtKB:O60494, HGNC:2548, human. 3623 aa precursor; large peripheral apical-membrane
glycoprotein. No transmembrane domain; anchored to the apical membrane through the
transmembrane protein amnionless (AMN), forming the **cubam** endocytic receptor.

## Core biology (verified)

- **Domain architecture:** N-terminal region (coiled-coil), 8 EGF-like domains, then 27
  CUB domains (CUB accounts for ~88% of the mass). [PMID:9478979 "a cluster of eight
  epidermal growth factor type domains followed by a cluster of 27 CUB domains"]. Lacks a
  hydrophobic membrane-spanning segment; released from membranes by non-enzymatic means —
  a **peripheral membrane protein** [PMID:9478979 "the receptor could be released from
  renal cortex membranes by nonenzymatic and nonsolubilizing procedures"].

- **Cubam receptor:** cubilin + AMN. Three cubilin chains combine into an intertwined
  β-helix that docks onto AMN; AMN provides the transmembrane anchor and clathrin-coated-pit
  internalization signals [PMID:30523278; PMID:14576052 "cubilin and AMN are subunits of a
  novel cubilin/AMN (cubam) complex"]. UniProt: "Component of the cubam complex composed of
  one CUBN trimer and one AMN chain." AMN is required for cubilin surface expression and
  glycosylation maturation; without AMN cubilin is retained in the ER [PMID:29402915;
  PMID:14576052].

- **Molecular function = cargo/endocytic receptor.** Non-enzymatic. Binds IF (CBLIF)-cobalamin
  and many other ligands; internalized (with AMN/megalin) by receptor-mediated endocytosis.
  IF-B12 binding is by CUB5-8 in a Ca2+-dependent dual-point mechanism [PMID:20237569 "how
  two distant CUB domains embrace the Cbl molecule by binding the two IF domains in a
  Ca(2+)-dependent manner"]. UniProt DOMAIN: "The CUB domains 5 to 8 mediate binding to CBLIF
  and ALB. CUB domains 1 and 2 mediate interaction with LRP2."

- **Ileum:** binds intrinsic-factor–cobalamin (IF-B12) and mediates dietary B12 absorption.
- **Kidney proximal tubule:** reabsorbs filtered ligands (albumin, transferrin, vitamin-D-binding
  protein GC, apoA-I/HDL, hemoglobin, etc.) via cubam + megalin (LRP2). [PMID:30523278;
  PMID:11994745 review].

- **Disease:** loss of function → Imerslund-Gräsbeck syndrome 1 / megaloblastic anemia 1
  (IGS1, MIM 261100): selective intestinal B12 malabsorption + mild proteinuria
  [PMID:10080186; PMID:14576052]. Also chronic benign proteinuria (PROCHOB, MIM 618884) from
  C-terminal variants (UniProt).

## GO annotation assessment summary

- **MF core:** cargo receptor activity (GO:0038024) — strongly supported (EXP/IDA, Reactome,
  ComplexPortal). This is the exact MF term in GOA and is the appropriate non-enzymatic
  receptor MF. `signaling receptor activity` (GO:0038023, old ProtInc TAS) is a misnomer —
  cubilin is an endocytic/cargo receptor, not a signaling receptor → MARK_AS_OVER_ANNOTATED.
- **calcium ion binding** (GO:0005509, IEA InterPro): supported — EGF-Ca and CUB-Ca sites;
  ligand binding is Ca2+-dependent (structure PMID:20237569). ACCEPT (non-core; enabling).
- **protein homodimerization activity** (GO:0042803, IDA PMID:10552972): cited PMID is the
  canine-accessory-activity genetics paper (abstract has no homodimerization assay) — but
  this is an experimental IDA I cannot fully verify; per policy keep as UNDECIDED rather than
  REMOVE. (Cubilin actually trimerizes via the N-terminal β-helix per PMID:30523278/20237569;
  "homodimerization" is imprecise.)
- **protein binding** (GO:0005515, IPI x3): uninformative bare term → MARK_AS_OVER_ANNOTATED
  (partners AMN Q9BXJ7, CBLIF/IF P27352 are captured better by cubam complex + cargo receptor).
- **BP core:** cobalamin transport (GO:0015889) — ACCEPT (IDA ComplexPortal PMID:14576052; TAS).
  receptor-mediated endocytosis (GO:0006898, NAS) — ACCEPT (mechanism of uptake).
  cobalamin metabolic process (GO:0009235, IDA) — KEEP_AS_NON_CORE (transport is the direct
  role; "metabolic process" is broader/upstream).
  vitamin D metabolic process (GO:0042359, Reactome TAS) — KEEP_AS_NON_CORE (reabsorbs GC:25(OH)D).
  tissue homeostasis (GO:0001894, NAS) — MARK_AS_OVER_ANNOTATED (vague).
- **CC core:** apical plasma membrane (GO:0016324) — ACCEPT. plasma membrane / membrane —
  ACCEPT (broader). brush border membrane / microvillus membrane — ACCEPT (specific apical).
  endosome, endocytic vesicle, coated pit — ACCEPT (endocytic pathway). lysosomal membrane /
  lumen — KEEP_AS_NON_CORE (ligand delivered to lysosome; ISS/TAS). cytosol (Reactome TAS) —
  MARK_AS_OVER_ANNOTATED (peripheral extracellular-facing protein, not cytosolic).
  extracellular exosome (HDA/IDA urinary-exosome proteomics) — KEEP_AS_NON_CORE (shed into
  urine; not a functional site). signaling receptor complex (GO:0043235) — the complex is
  cubam; "signaling" is a misnomer but it is the cubam receptor complex → ACCEPT the complex
  membership (part_of receptor complex) but note "signaling" is imprecise.
  extrinsic component of external side of plasma membrane (GO:0031232, NAS) — ACCEPT (accurate:
  peripheral, extracellular-facing).

## References
Grounded in CUBN-uniprot.txt (O60494), CUBN-goa.tsv, and cached publications/PMID_*.md.
No falcon deep research (provider out of credits, HTTP 402).
