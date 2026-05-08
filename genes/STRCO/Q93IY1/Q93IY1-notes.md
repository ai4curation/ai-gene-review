# Q93IY1 / SCO5104 - Notes

## Identity

- UniProt: Q93IY1 (unreviewed TrEMBL entry)
- Gene: SCO5104 (ordered locus name)
- **NOT OsaC** - OsaC is SCO5747. SCO5104 is an OsaC-like paralogue.
- Organism: *Streptomyces coelicolor* A3(2) (strain ATCC BAA-471 / M145)
- NCBI TaxID: 100226
- 880 amino acids, predicted PE level 4

## Key Publication

[PMID:19154327 "Osmoregulation in Streptomyces coelicolor: modulation of SigB activity by OsaC"]
- This paper characterizes OsaC (SCO5747) and lists SCO5104 as one of four *S. coelicolor* genes with related domain composition
- **SCO5104 mutants showed NO observable phenotype under hyperosmotic conditions** (from full text, results not shown)
- The characterized OsaC (SCO5747) is required to return *osaB* and *sigB* expression back to constitutive levels after osmotic stress
- OsaC domain architecture: N-terminal kinase domain (anti-sigma factor-like) → PAS domains → GAF domain → C-terminal phosphatase domain
- OsaC N-terminal domain functions as a **SigB anti-sigma factor** (sigma factor antagonist)
- Co-purification experiments confirm association of OsaC with SigB (demonstrated for SCO5747, not SCO5104)

## CORRECTION NOTE (from deep research)

Initial review incorrectly identified SCO5104 as OsaC. Deep research (Falcon) clarified that OsaC = SCO5747, and SCO5104 is a paralogue with no observed osmotic stress phenotype. The osmotic stress response annotation was removed and other annotations were made more conservative.

## Domain Architecture (from UniProt/InterPro)

- **PAS domain** (aa 48-103, PROSITE:PS50112) - sensory domain; in the homolog Rv1364c, the PAS domain binds fatty acids (palmitoleic acid preferred over palmitic acid) [PMID:21220116]
- **PAS_4 domain** (Pfam:PF08448) - additional PAS-type sensory domain
- **GAF_2 domain** (Pfam:PF13185) - additional sensory domain
- **HATPase_c_2 domain** (Pfam:PF13581) - histidine kinase-like ATPase domain; in OsaC this functions as an anti-sigma factor domain
- **SpoIIE domain** (Pfam:PF07228) - PP2C-type serine/threonine phosphatase domain

## PANTHER Family

- PTHR43156: Bacterial Sigma Factor Regulator
- Subfamily: PTHR43156:SF2 (Stage II sporulation protein E)
- Family members include:
  - *B. subtilis* SpoIIE (P37475) - Stage II sporulation protein E, septum-associated phosphatase
  - *B. subtilis* RsbP (O07014) - phosphoserine phosphatase that activates SigB
  - *B. subtilis* RsbU (P40399) - phosphoserine phosphatase in SigB pathway
  - *M. tuberculosis* Rv1364c (P9WLZ7) - multidomain regulatory protein for SigF regulation
  - *Synechocystis* IcfG (P37979)

## Homolog Rv1364c (M. tuberculosis) - IBA reference protein

Based on PubMed articles about the IBA reference protein P9WLZ7 (Rv1364c):

[PMID:19700407 "Interdomain communication in the Mycobacterium tuberculosis environmental phosphatase Rv1364c"]
- Rv1364c is a single-chain "environmental phosphatase" with fused phosphatase, kinase (anti-sigma), and anti-anti-sigma domains
- The anti-sigma factor kinase domain activates the phosphatase domain
- The kinase-phosphatase fusion protein autophosphorylates in E. coli
- Phosphorylation is antagonized by the phosphatase activity
- Demonstrates PP2C-type phosphatase activity (IDA evidence for GO:0016791)

[PMID:19016841 "Loss of kinase activity in Mycobacterium tuberculosis multidomain protein Rv1364c"]
- Rv1364c RsbU domain has conserved PP2C-type serine/threonine phosphatase activity
- The RsbW (kinase/anti-sigma) domain has LOST kinase activity due to substitutions in ATP-binding regions
- Still retains functional anti-sigma factor interactions with SigF
- This is a key difference from B. subtilis orthologs

[PMID:21220116 "Structural characterization of the multidomain regulatory protein Rv1364c from Mycobacterium tuberculosis"]
- Crystal structures of PAS domain and phosphatase/kinase dual domain
- PAS domain binds palmitic acid but has 100x greater affinity for palmitoleic acid
- Full-length protein can exist as monomer and dimer
- Fatty acid binding may trigger monomer-dimer switch affecting phosphatase activity and sigma factor regulation

[PMID:16263329 "Interactions of anti-sigma factor antagonists of Mycobacterium tuberculosis in the yeast two-hybrid system"]
- Confirms Rv1364c interactions with anti-sigma factor RsbW and sigma factor SigF

## Functional Summary

OsaC (SCO5104/Q93IY1) is a multidomain regulatory protein that modulates SigB activity in response to osmotic stress in *S. coelicolor*. Its key functions are:

1. **Sigma factor antagonist (anti-sigma factor) activity** - The N-terminal kinase-like domain functions as a SigB anti-sigma factor, sequestering SigB to prevent transcription of stress response genes
2. **PP2C-type protein serine/threonine phosphatase activity** - The C-terminal SpoIIE domain is a PP2C-type phosphatase that likely dephosphorylates anti-anti-sigma factor proteins
3. **Signal sensing** - PAS and GAF domains likely sense environmental/metabolic signals (possibly fatty acids or energy levels) to regulate the switch between active and inactive states
4. **Osmoregulation** - Required to return SigB-dependent gene expression to basal levels after osmotic stress

## eggNOG assignments

- COG2172: Anti-sigma regulatory factor (Ser/Thr protein kinase)
- COG2203: FOG: GAF domain
- COG2208: Predicted PP2C-type phosphatase
