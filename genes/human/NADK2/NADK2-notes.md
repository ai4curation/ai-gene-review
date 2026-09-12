# NADK2 (NAD kinase 2, mitochondrial) — review notes

UniProt: Q4G0N4 (NADK2_HUMAN). HGNC:26404. Synonyms: C5orf33, MNADK, NADKD1.
442 aa precursor; residues 1–62 mitochondrial transit peptide, chain 63–442.
EC 2.7.1.23. Belongs to the NAD kinase family.

## Core biology

NADK2 is the **mitochondrial NAD(+) kinase** — the enzyme that generates the
mitochondrial NADP(+) pool. It phosphorylates NAD(+) using ATP (or, in vitro,
inorganic polyphosphate) to yield NADP(+):

> NAD(+) + ATP = ADP + NADP(+) + H(+)   (EC 2.7.1.23, RHEA:18629)
[file:human/NADK2/NADK2-uniprot.txt "Reaction=NAD(+) + ATP = ADP + NADP(+) + H(+); Xref=Rhea:RHEA:18629"]

- UniProt FUNCTION: "Mitochondrial NAD(+) kinase that phosphorylates NAD(+) to yield
  NADP(+). Can use both ATP or inorganic polyphosphate as the phosphoryl donor. Also
  has weak NADH kinase activity in vitro; however NADH kinase activity is much weaker
  than the NAD(+) kinase activity and may not be relevant in vivo."
  [file:human/NADK2/NADK2-uniprot.txt]
- Discovered as C5orf33, the "missing" source of human mitochondrial NADP(+):
  "NAD kinase is the sole NADP(+) biosynthetic enzyme... no mitochondrial NAD kinase
  has been identified in human, and the source of human mitochondrial NADP(+) remains
  elusive. Here we present evidence demonstrating that a human protein of unknown
  function, C5orf33, is a human mitochondrial NAD kinase"
  [PMID:23212377 "no mitochondrial NAD kinase has been identified in human, and the source of human mitochondrial NADP(+) remains elusive"]

## Experimental evidence (PMID:23212377, Ohashi/Kawai/Murata 2012, Nat Commun; full text available)

- **Catalytic activity (IDA, MF GO:0003951):** purified recombinant Δ62 protein forms
  NADP+ from NAD+ and ADP from ATP by TLC.
  [PMID:23212377 "we detected the formation of NADP+ from NAD+ and of ADP from ATP (Fig. 2c), showing that C5orf33 protein has NADK activity"]
  - Kinetics: Km(NAD+) 0.022 mM, Km(ATP) 1.7 mM; NADHK activity only ~10% of NADK
    activity; inhibited by NADH, NADPH and NADP+.
    [file:human/NADK2/NADK2-uniprot.txt "Inhibited by NADH, NADPH and NADP(+)."]
- **Subcellular location (IDA, CC mitochondrion GO:0005739):** FLAG-tagged full-length
  protein localizes to mitochondria in HEK293A cells; Δ62 (no transit peptide) does not.
  [PMID:23212377 "This observation demonstrated that the C5orf33 protein is localized in mitochondria, whereas Δ62C5orf33 protein is not, confirming that C5orf33 protein is a mitochondrial NADK"]
  - Also confirmed by cell fractionation: mitochondrial, not cytosolic.
    [PMID:23212377 "C5orf33 protein was localized in the mitochondrial fraction but not in the cytosolic fraction"]
- **Homodimer (IDA, MF GO:0042803 protein homodimerization activity):** UniProt SUBUNIT
  = Homodimer (ECO:0000305|PubMed:23212377). Reactome names the "NADK2 dimer".
  [file:human/NADK2/NADK2-uniprot.txt "SUBUNIT: Homodimer."]
  Note: this is a structural/oligomerization property, not the catalytic function.
- **Physiological role (NAD+ metabolic process; ROS defense):** siRNA knockdown reduced
  mitochondrial NADK activity to 47% and increased intracellular ROS.
  [PMID:23212377 "NADK activity of the mitochondrial fraction was decreased to 47% upon knockdown of C5orf33"]
  [PMID:23212377 "human mitochondrial NADK is involved in the regulation of the generation of mitochondrial ROS"]
- Widely/ubiquitously expressed; mRNA more abundant than cytosolic NADK in most tissues.
  [PMID:23212377 "levels of C5orf33 mRNA were higher than those of the human NADK gene in all tissues examined except for colon, spleen and skeletal muscle"]

## Localization corroboration

- HPA immunofluorescence (IDA, GO_REF:0000052): mitochondrion.
- High-throughput mitochondrial proteome (HTP, PMID:34800366, Morgenstern et al. 2021,
  Cell Metab): NADK2 in the high-confidence human mitochondrial proteome.
- UniProt SubCell mapping (IEA, SL-0173 → mitochondrion) and ARBA (mitochondrial matrix).
- Reactome TAS (R-HSA-8955030 NADK2 reaction; R-HSA-9838081/9838093 LONP1 substrate
  entries): mitochondrial matrix. The matrix is the correct submitochondrial compartment
  for this soluble matrix enzyme (transit peptide, no TM segments).

## Downstream role of the mitochondrial NADP(H) pool

NADK2 supplies the NADPH used by NADP-dependent mitochondrial oxidoreductases. Loss of
NADK2 causes **mitochondrial NADP(H) deficiency**, secondarily crippling 2,4-dienoyl-CoA
reductase (DECR1, PUFA β-oxidation) and the first step of lysine degradation (AASS/DHTKD1
axis), producing DECR deficiency with **hyperlysinemia**. NADPH also feeds proline
biosynthesis via ALDH18A1/P5CS and antioxidant/one-carbon pathways.

According to PubMed (Houten et al. 2014, Hum Mol Genet
[DOI](https://doi.org/10.1093/hmg/ddu218), PMID:24847004):
> "NADK2 encodes the mitochondrial NAD kinase, which is crucial for NADP biosynthesis
> evidenced by decreased mitochondrial NADP(H) levels in patient fibroblasts. DECR and
> also the first step in lysine degradation are performed by NADP-dependent
> oxidoreductases explaining their in vivo deficiency."

UniProt DISEASE:
> "2,4-dienoyl-CoA reductase deficiency (DECRD) [MIM:616034]: A rare, autosomal
> recessive, inborn error of polyunsaturated fatty acids and lysine metabolism,
> resulting in mitochondrial dysfunction. Affected individuals have a severe
> encephalopathy... increased C10:2 carnitine levels and hyperlysinemia."
[file:human/NADK2/NADK2-uniprot.txt]

## Annotation review decisions (summary)

Core MF: **GO:0003951 NAD+ kinase activity** (IDA, PMID:23212377) + **GO:0005524 ATP binding**
(phosphoryl-donor substrate; UniProt KW, not in GOA experimental set but real).
Core BP: **GO:0019674 NAD+ metabolic process** (IDA); the informative/precise BP is
**GO:0006741 NADP+ biosynthetic process** (UniProt DR InterPro; the actual anabolic role).
Core CC: **GO:0005759 mitochondrial matrix** (soluble matrix enzyme).

- All GO:0003951 calls (IDA, IBA, IEA) → the catalytic function is the core function; keep.
- Mitochondrion CC calls (IDA, IBA, IEA, HPA IDA, HTP) → correct; matrix is more precise.
- GO:0019674 NAD+ metabolic process → accept (IDA); note the anabolic/product side is
  NADP+ biosynthesis (GO:0006741), which is more informative and is proposed as a new term.
- GO:0042803 protein homodimerization activity (IDA) → real (homodimer) but it is an
  oligomerization property, not the catalytic MF; keep as non-core.
- LONP1 Reactome TAS matrix entries (R-HSA-9838081/9838093) → NADK2 is a LONP1 protease
  substrate; the CC (matrix) is correct, but these do not describe NADK2's own function;
  keep as non-core matrix localization.
