# COX11 (human) review notes

UniProtKB:Q9Y6N1 — Cytochrome c oxidase assembly protein COX11, mitochondrial. HGNC:2261. 276 AA precursor.

Deep research note: falcon provider was out of credits (402) at time of review; no `-deep-research-falcon.md` was generated. Review grounded in the UniProt record, seeded GOA TSV, and cached `publications/PMID_*.md`.

## Core biology (verified)

COX11 is a **mitochondrial inner-membrane copper metallochaperone** required for
**Complex IV (cytochrome c oxidase, CcO/CIV) assembly**. It is anchored in the inner
membrane by a single transmembrane helix (TRANSMEM 98–120; residues 76–97 matrix,
121–276 intermembrane space per UniProt topology) with a soluble C-terminal Ig-like
headgroup in the intermembrane space. This headgroup carries the conserved copper-binding
**CFCF motif** (Cys217/Cys219 in human) plus a third membrane-proximal cysteine (Cys121);
UniProt records Cu(+) BINDING at residues 217 and 219.

Function: COX11 receives Cu(I) from the soluble IMS chaperone **COX17** and specifically
and directly **delivers/inserts copper into the CuB site of the catalytic subunit MT-CO1
(COX1)** during CcO assembly. Stable copper binding requires COX11 dimerization, which is
supported by COX19.

- [PMID:35750769 "In the current model, the soluble IMS Cu-chaperone COX17, which has a twin CX9C structural motif and a CHCH Cu(I) binding motif, transfers Cu(I) to the IMS-exposed Cu-binding domains of IM-anchored COX11 and two SCO proteins (SCO1 and SCO2)."]
- [PMID:35750769 "COX11 and SCO1/SCO2 specifically and directly transfer Cu to the CuB and CuA sites, respectively."]
- [PMID:35750769 "the C217 and C219 residues in the human CcO, forming the conserved copper-binding CFCF motif"]
- [PMID:35750769 "the data suggest that COX19 is necessary to support COX11 dimerization"]

Human COX11 knockout is not fully lethal to CcO assembly (unlike yeast): COX11-KO retains
~15% holo-CIV, hinting at a partial alternative CuB metalation route in metazoans, but Cu
supplementation cannot substitute for COX11.
- [PMID:35750769 "the COX11-KO line retained 50% of COX1 and 15% of COX2 steady-state levels and 15% of residual fully assembled CcO"]
- [PMID:35750769 "These data functionally link COX11—as well as COX19 and PET191—to COX2 biogenesis."]

## Localization
Mitochondrion inner membrane; single-pass; intermembrane side. UniProt SUBCELLULAR
LOCATION supported by PubMed:15229189, PubMed:9878253, PubMed:35750769.
- UniProt: "SUBCELLULAR LOCATION: Mitochondrion inner membrane ... Single-pass membrane protein ... Intermembrane side"

## Disease
Biallelic COX11 variants cause mitochondrial complex IV deficiency nuclear type 23
(MC4DN23; MIM:620275), infantile-onset encephalopathy. COX11 knockdown lowers
respiration-derived ATP, rescuable by CoQ10.
- [PMID:36030551 "COX11 also participates in COX assembly by mediating copper delivery into to the complex"]
- [PMID:36030551 "COX11 is required to maintain mitochondrial‐derived ATP levels"]
- [PMID:36030551 "biallelic pathogenic variants in COX11 associated with infantile-onset mitochondrial encephalopathies"]

## Interactions (mostly non-core / context)
- COX2 and COX19 — during CcO assembly / dimerization support (PMID:35750769).
- COA4 (Q9NYJ1) — IntAct, PMID:33961781 (BioPlex high-throughput; bare protein binding).
- RANBP2 (P49792) — PMID:34400285; RANBP2 binds COX11, relevant to ADANE. Bare protein binding IPI.
- CNNM4/ACDP4 (Q6P4Q7) — Y2H, PMID:15840172; also basis of the intracellular cation-homeostasis IDA.

## Annotation decisions summary
- Core MF: GO:0016531 copper chaperone activity (ISS) — ACCEPT as core.
- GO:0005507 copper ion binding (IEA/InterPro) — ACCEPT (consistent with Cu-binding CFCF motif; broader than 0016531 but correct).
- Core BP: GO:0033617 mitochondrial respiratory chain complex IV assembly (IDA + IMP) — ACCEPT.
- Core CC: GO:0005743 mitochondrial inner membrane (IBA/IEA/IDA/TAS) — ACCEPT.
- GO:0006754 ATP biosynthetic process (IMP, PMID:36030551) — indirect/downstream consequence of CIV deficiency; KEEP_AS_NON_CORE.
- GO:0030003 intracellular monoatomic cation homeostasis (IDA, PMID:15840172) — CNNM4 coupling context; KEEP_AS_NON_CORE.
- GO:0005739 mitochondrion (HTP + IDA) — ACCEPT (broader localization).
- GO:0032991 protein-containing complex (IDA) — uninformative parent; MARK_AS_OVER_ANNOTATED (COX11 homodimer / CIV assembly intermediate is the real complex).
- GO:0005515 protein binding IPIs (x3) — bare protein binding, uninformative MF; MARK_AS_OVER_ANNOTATED.
