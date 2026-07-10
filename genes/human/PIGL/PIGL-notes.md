# PIGL (Q9Y2B2) — review notes

Human PIGL, N-acetylglucosaminyl-phosphatidylinositol de-N-acetylase (PIG-L; EC 3.5.1.89).
HGNC:8966, GeneID 9487, chromosome 17. 252 aa. Reference proteome UP000005640.

## Core biology

PIGL catalyses the **second step of glycosylphosphatidylinositol (GPI) anchor biosynthesis**:
the **de-N-acetylation of N-acetylglucosaminyl-phosphatidylinositol (GlcNAc-PI) to
glucosaminyl-phosphatidylinositol (GlcN-PI)**, releasing acetate. This deacetylation is a
prerequisite for the downstream inositol acylation and mannosylation steps of GPI assembly.

- UniProt FUNCTION: "Catalyzes the second step of glycosylphosphatidylinositol (GPI)
  biosynthesis, which is the de-N-acetylation of N-acetylglucosaminyl-phosphatidylinositol."
  [file:human/PIGL/PIGL-uniprot.txt]
- Reaction (RHEA:11660, EC 3.5.1.89): 6-(N-acetyl-alpha-D-glucosaminyl)-PI + H2O =
  6-(alpha-D-glucosaminyl)-PI + acetate. [file:human/PIGL/PIGL-uniprot.txt]
- GOA MF term carried: **GO:0000225 N-acetylglucosaminylphosphatidylinositol deacetylase
  activity** (confirmed in PIGL-goa.tsv, all MF rows).

## Enzyme activity — experimental

[PMID:10085243 Watanabe et al. 1999 "The second step of GPI biosynthesis is
de-N-acetylation of N-acetylglucosaminylphosphatidylinositol (GlcNAc-PI)"] — recombinant
rat PIG-L purified from E. coli "has GlcNAc-PI de-N-acetylase activity in vitro"; yeast
homologue Gpi12p (YMR281W) complements PIG-L-deficient mammalian cells and its disruption is
lethal in S. cerevisiae; "the de-N-acetylation step is also indispensable in yeasts". This
is the original cloning/functional paper (rat gene by expression cloning complementing a CHO
mutant defective in this step). Human GOA cites it as NAS (function) and IMP (BP), likely
via the CHO-complementation / cross-species functional identity.

[PMID:14742432 Pottekat & Menon 2004] — "We show that human PIG-L is a type I membrane
protein with a large cytoplasmic domain"; GlcNAc-PI de-N-acetylase activity "is localized to
the endoplasmic reticulum (ER)"; PIG-L retained in the ER by a multi-component signal (a
retention signal in the cytoplasmic domain residues 60–88, plus a weak luminal/TM signal).
This is the human enzyme-activity + ER-localization paper (EXP for MF; EXP/IDA for ER
membrane).

## Localization

ER membrane (GO:0005789). UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane ...
Single-pass type I membrane protein." Features: TRANSMEM 2..22 (helical), TOPO_DOM 23..252
cytoplasmic (large cytoplasmic domain). Consistent with GlcNAc-PI de-N-acetylation on the
cytoplasmic face of the ER, matching the topology of early GPI assembly.

Reactome R-HSA-162857 (second-step reaction): "In the second step of GPI synthesis,
N-acetylglucosaminyl-PI is hydrolyzed to yield glucosaminyl-PI and acetate. The
phosphatidylinositol (PI) derivatives involved in this reaction are located in the
endoplasmic reticulum membrane, as is the PIG-L enzyme that catalyzes it." Reactome
R-HSA-162710 (whole GPI pathway): "GPI is synthesized in the endoplasmic reticulum."

## Disease

Biallelic loss-of-function / hypomorphic PIGL variants cause **CHIME syndrome (Zeman-Sheard
syndrome; Coloboma, congenital Heart disease, Ichthyosiform dermatosis, intellectual
disability / Mental retardation, Ear anomalies; MIM:280000)**, an inherited GPI-deficiency
disorder. Recurrent variant p.Leu167Pro. [UniProt DISEASE; PMID:22444671, PMID:29473937,
PMID:35258128, PMID:39641205 — not needed as review citations for the function/localization
annotations, but establish the biology.]

## Domain / family

Belongs to the PIGL family; Pfam PF02585 (PIG-L), LmbE-like fold (Gene3D 3.40.50.10320,
SUPFAM SSF102588; InterPro IPR003737 GlcNAc_PI_deacetylase-related, IPR024078 LmbE-like).
PANTHER PTHR12993:SF11. Consistent with the deacetylase MF.

## Annotation-review decisions (summary)

MF GO:0000225 (deacetylase): all 5 rows (IBA, IEA, TAS-Reactome, EXP, ISS, NAS) ACCEPT —
core catalytic function, experimentally established (PMID:14742432 EXP; PMID:10085243). One
EXP + others accepted as core; NAS/ISS/IEA/TAS accepted (correct term, redundant support).

BP GO:0006506 (GPI anchor biosynthetic process): rows (IEA, TAS-Reactome, IMP, NAS) ACCEPT —
core biological process; second step of GPI assembly.

CC: GO:0005789 ER membrane (IEA, EXP, IDA, TAS-Reactome) ACCEPT — experimentally localized
(PMID:14742432), single-pass type I ER membrane protein. GO:0005783 endoplasmic reticulum
(IBA, is_active_in) ACCEPT as non-core parent — the more specific ER membrane is the
informative CC; ER is the broader IBA "is_active_in" term, correct but less specific.

No REMOVE actions: every annotation is correct for this well-characterized enzyme.

core_functions: GO:0000225 (MF) directly_involved_in GO:0006506, located_in GO:0005789.
