# NFP (Nod Factor Perception) — Medicago truncatula — research notes

UniProt: Q0GXS4 (NFP_MEDTR). Gene: MTR_5g019040. 595 aa precursor.
Also called Nod-factor receptor 5 (NFR5 orthologue of Lotus japonicus).

## Summary of gene function

NFP is a plasma-membrane LysM-domain receptor-like kinase (LysM-RLK) of the model
legume *Medicago truncatula*. It is the **Nod factor receptor** that perceives
rhizobial lipo-chitooligosaccharide (LCO) signals ("Nod factors") secreted by
*Sinorhizobium meliloti*, and triggers the earliest steps of the nitrogen-fixing
root nodule symbiosis. NFP is **essential and non-redundant** for Nod factor
perception: *nfp* mutants are completely Nod-negative.

Architecture: signal peptide (1-27), extracellular region (28-246) with three
LysM domains (LysM1 ~51-98, LysM2 ~113-160, plus a third predicted LysM), a single
transmembrane helix (247-267), and an intracellular protein-kinase-like domain
(284-573). The LysM ectodomain is heavily N-glycosylated (9 sites).

## Nod factor perception by the LysM ectodomain

The extracellular LysM domains bind chitooligosaccharide / Nod factor ligands.
[PMID:16723404 "The extracellular region of this protein contains three tandem
lysin motifs (LysMs), a short peptide domain that is implicated in peptidoglycan
or chitin binding"] and [PMID:16723404 "A convergent model can be proposed where
the sulfated, O-acetylated lipo-chitooligosaccharidic Nod factor of S. meliloti
binds in similar orientation to the three LysM domains of M. truncatula NFP.
N-glycosylation is not expected to interfere with Nod factor binding"].

LysM domain residues are functionally required for Nod factor recognition:
the L154P substitution (in LysM2) impairs nodulation [PMID:22087221 / UniProt
SITE 154 "Required for nodulation"].

NFP is the most upstream component of the Nod factor signalling pathway. The
*nfp* mutant fails every assayed Nod-factor response [PMID:12753588 "The nfp
mutant thus shows no rapid calcium flux, the earliest detectable Nod factor
response of wild-type plants, and no root hair deformation. The nfp mutant is
also deficient in Nod factor-induced calcium spiking and early nodulin gene
expression"] and [PMID:12753588 "These data indicate that the NFP locus controls
an early step of Nod factor signal transduction, upstream of previously
identified genes and specific to nodulation"].

## NFP is a pseudokinase (catalytically dead intracellular domain)

The intracellular "kinase" domain of NFP is a **pseudokinase** — it lacks
catalytic activity. [PMID:16844829 "Consistent with deviations from conserved
kinase domain sequences, NFP did not show autophosphorylation activity,
suggesting that NFP needs to associate with an active kinase or has unusual
functional characteristics different from classical kinases"] and
[PMID:16844829 "one subfamily, which includes NFP, was characterized by
deviations from conserved kinase sequences"].

NFP therefore depends on an active co-receptor kinase to transduce the signal.
The InterPro/PROSITE-derived "Tyr protein kinase family" classification (UniProt
SIMILARITY line, PROSITE PS00109 PROTEIN_KINASE_TYR) is a sequence-motif
artefact: NFP is annotated by UniProt itself as a **serine/threonine** RLK, and
plant RLKs are Ser/Thr kinases — there is no evidence for tyrosine kinase
activity. The web literature confirms NFP/NFR5 "has no detectable
autophosphorylation activity and is considered a pseudokinase" and that "the
inactive kinase domain of MtNFP can be weakly transphosphorylated by the active
kinase of MtLYK3."

Implication for GO: "protein tyrosine kinase activity" (GO:0004713) is doubly
wrong (pseudokinase + Ser/Thr family, not Tyr). "protein kinase activity"
(GO:0004672, current InterPro IEA) is also unsupported — the domain is
catalytically dead.

## The NFP/LYK3 receptor complex

NFP and the active LysM-RLK LYK3 form heteromeric receptor complexes at the cell
periphery. [PMID:25351493 "our Förster resonance energy transfer-fluorescence
lifetime imaging microscopy analysis indicates that NFP and LYK3 form heteromeric
complexes at the cell periphery in M. truncatula nodules"]. NFP and LYK3
co-localize "in a narrow zone of about two cell layers at the nodule apex"
[PMID:25351493]. LYK3 (UniProt Q6UD73) is the active-kinase co-receptor; NFP
contributes ligand-binding/scaffolding but not phosphotransfer.

NFP also interacts with the small GTPase ROP10: [PMID:25794934 "ROP10 interacted
with the kinase domain of the NF receptor NFP in a GTP-dependent manner"] and
[PMID:25794934 "interactions between ROP10 and NF receptors are required for
root hair deformation and continuous curling during rhizobial infection"].
ROP10 (UniProt B2MVQ1) is a type II Rho-of-plants small GTPase.

## Nodulation: organogenesis and infection

NFP acts in both the epidermis and the cortex during nodulation.
[PMID:22874912 "Epidermal NFP is sufficient to induce cortical cell divisions
leading to nodule primordia formation"]. NFP is required throughout the
infection process: [PMID:16844829 "NFP was shown both to be expressed in
association with infection thread development and to be involved in the
infection process"]. NFP is needed for intracellular infection / rhizobial
release: in *nfp* mutants "Infection threads enter the cells, but the release
of the bacteria is hampered" (UniProt DISRUPTION PHENOTYPE, ECO from
PMID:25351493).

Disruption phenotype: complete Nod- phenotype, no calcium flux/spiking, no early
nodulin expression, no root hair deformation/curling, no infection threads
[PMID:12753588; PMID:16844829].

## NFP in pathogen resistance (defense)

Beyond symbiosis, NFP contributes to *M. truncatula* immunity against
filamentous pathogens. [PMID:23432463 "nfp, but not lyk3, mutants were
significantly more susceptible than wildtype plants to A. euteiches, whereas
NFP overexpression increased resistance"] and [PMID:23432463 "nfp mutants also
showed an increased susceptibility to the fungus Colletotrichum trifolii. These
results demonstrate that NFP intervenes in M. truncatula immunity"]. This
supports specific curated terms — positive regulation of defense response to
oomycetes (GO:1902290) and regulation of defense response to fungus
(GO:1900150) — both IMP from PMID:23432463. A broad keyword-derived "defense
response" (GO:0006952) adds nothing beyond these.

## Subcellular localization

Plasma membrane (cell periphery); also vacuolar lumen in cells where receptors
are being broken down. [PMID:25351493] — NFP-GFP localizes at the cell
periphery, and "Vacuolar localization is observed in cells undergoing breakdown
of the receptors" (UniProt SUBCELLULAR LOCATION). Single-pass type I membrane
protein.

## Glycosylation

NFP is highly N-glycosylated [PMID:16723404 "Expression of NFP in a homologous
system (M. truncatula roots) revealed that the protein is highly N-glycosylated,
probably with both high-mannose and complex glycans"]. UniProt lists 9 N-glyc
sites. The IDA "glycoprotein biosynthetic process" (GO:0009101) GO annotation
captures NFP *being* a glycoprotein substrate — NFP is not an enzyme of the
glycosylation machinery, so this is a marginal/over-annotation as a process the
gene is "involved in."

## Core function synthesis

1. Molecular function: Nod factor (lipo-chitooligosaccharide) receptor —
   transmembrane signalling receptor whose LysM ectodomain binds the rhizobial
   LCO ligand. Carbohydrate (chitin-type/LCO) binding via LysM domains.
   NOT a catalytically active kinase (pseudokinase).
2. Biological process: nodulation / root nodule symbiosis — perception of Nod
   factors and initiation of nodule organogenesis and rhizobial infection.
3. Secondary process: contribution to immunity against oomycete/fungal
   pathogens.
4. Cellular component: plasma membrane (forms heteromeric complex with LYK3).

## GO term ID verification (OLS)

- GO:0009877 nodulation — verified, leaf term.
- GO:0038023 signaling receptor activity — verified.
- GO:0004888 transmembrane signaling receptor activity — verified.
- GO:0008061 chitin binding — verified.
- GO:0007166 cell surface receptor signaling pathway — verified.
- GO:0050832 defense response to fungus — verified.
- GO:1900150 regulation of defense response to fungus — verified.
- GO:1902290 positive regulation of defense response to oomycetes — verified.
- GO:0031267 small GTPase binding — verified.
- GO:0004713 protein tyrosine kinase activity / GO:0004672 protein kinase
  activity — verified IDs; both rejected on pseudokinase grounds.
