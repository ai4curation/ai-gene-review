# DPM3 (Q9P2X0) review notes

Human DPM3 = dolichol-phosphate mannosyltransferase subunit 3 (anchoring subunit).
92 aa; two predicted TM helices (aa 8-28, 37-57). Belongs to the DPM3 family.
Deep research: falcon is OUT OF CREDITS (HTTP 402); no `-deep-research-falcon.md` was
generated. Review grounded in UniProt (Q9P2X0), the seeded GOA, and cached publications.

## Core biology

DPM3 is the **membrane-anchoring / stabilizer subunit** of the heterotrimeric
dolichol-phosphate mannose (Dol-P-Man / DPM) synthase complex (DPM1/DPM2/DPM3). It is
**non-catalytic** — its function is structural/anchoring, not enzymatic.

- The catalytic subunit DPM1 lacks a transmembrane domain; DPM3 tethers DPM1 to the ER
  membrane. [file:human/DPM3/DPM3-uniprot.txt "Stabilizer subunit of the dolichol-phosphate
  mannose (DPM)"; "synthase complex; tethers catalytic subunit DPM1 to the endoplasmic";
  "reticulum. {ECO:0000269|PubMed:10835346}."]
- Within the complex, DPM3 associates with DPM1 via its C-terminal domain and with DPM2 via
  its N-terminal portion. [PMID:10835346 "The third subunit, DPM3, comprises 92 amino acids
  associated with DPM1"; "via its C-terminal domain and with DPM2 via its N-terminal portion."]
  [file:human/DPM3/DPM3-uniprot.txt "complex composed of DPM1, DPM2 and DPM3; within the
  complex, associates"; "with DPM1 via its C-terminal domain and with DPM2 via its N-terminal"]
- Stability chain: DPM2 stabilizes DPM3; DPM3 stabilizes/directly stabilizes DPM1.
  Overexpression of DPM3 in Lec15 (DPM2-null) cells restored DPM biosynthesis with an increase
  in DPM1, i.e. DPM3 directly stabilizes DPM1. [PMID:10835346 "overexpression of DPM3 in";
  "restored the biosynthesis of DPM with an"; "indicating that DPM3 directly stabilized DPM1."]
- The DPM synthase makes dolichol-phosphate-mannose (Dol-P-Man / DOLPman), the mannosyl donor
  used for GPI-anchor biosynthesis, N-glycan precursor assembly, and protein O- and
  C-mannosylation. [PMID:10835346 "Dolichol-phosphate-mannose (DPM) synthase generates mannosyl
  donors for"; "N-glycan and protein O- and C-mannosylation."]
- UniProt pathway: Protein modification; protein glycosylation.
  [file:human/DPM3/DPM3-uniprot.txt "Protein modification; protein glycosylation."]

## Localization

ER membrane, multi-pass membrane protein. [file:human/DPM3/DPM3-uniprot.txt "Endoplasmic
reticulum membrane; Multi-pass"] IDA localization to ER / ER membrane from PMID:10835346.
Reactome (TAS) also places the reaction and complex in the ER membrane. The HDA "membrane"
(GO:0016020) call comes from a large-scale NK-cell membrane-proteome MS study
(PMID:19946888), a generic membrane term subsumed by the ER-membrane annotations.

## Disease

DPM3-CDG (congenital disorder of glycosylation type Io) — an
alpha-dystroglycanopathy-type muscular dystrophy. UniProt records two OMIM disease entries:
- MDDGC15 (limb-girdle, MIM:612937): muscle weakness, increased serum CK, dystrophic muscle
  biopsy, reduced O-mannosylation of alpha-dystroglycan. [file:human/DPM3/DPM3-uniprot.txt
  "MDDGC15 patients have muscle"; "weakness, increased serum creatine kinase, dystrophic
  changes on muscle"; "reduced O-mannosylation of alpha-dystroglycan."]
- MDDGB15 (congenital with impaired intellectual development, MIM:618992).
The L85S variant reduces DPM1 binding and DPM synthase activity (Lefeber et al. 2009,
PMID:19576565, characterized in UniProt VARIANT feature). DPM1-CDG patients also show reduced
DPM1-DPM3 binding as the pathogenic mechanism. [PMID:23856421 "reduced binding to DPM3, an
essential,"; "non-catalytic subunit of the DPM complex"]

## GOA annotation assessment (summary)

- Core MF: GO:0043495 protein-membrane adaptor activity (ISS) — best captures the
  anchoring/tethering role; ACCEPT as core.
- GO:0008047 enzyme activator activity (IDA, PMID:10835346) — DPM3 raises DPM synthase output
  by stabilizing DPM1; defensible but the effect is via stabilization/anchoring rather than
  classic allosteric activation. KEEP as non-core (the adaptor term is more informative).
- GO:0005515 protein binding (IPI x4) — DPM1/DPM2 interactions. Uninformative bare term;
  MARK_AS_OVER_ANNOTATED (the specific adaptor MF + complex CC capture the biology).
- CC: GO:0005789 ER membrane (multiple: IBA/IEA/NAS/TAS/IDA) — ACCEPT; GO:0005783 ER (IDA)
  ACCEPT (parent, non-core); GO:0016020 membrane (HDA) MARK_AS_OVER_ANNOTATED (generic);
  GO:0033185 DPM synthase complex (IBA/IPI/IDA) — ACCEPT as core complex.
- BP: GO:0180047 dolichol phosphate mannose biosynthetic process (IDA) core; GO:0006488
  dolichol-linked oligosaccharide biosynthetic process (IBA) ACCEPT; GO:0043048 dolichyl
  monophosphate biosynthetic process (IDA) — this term is about making dolichyl monophosphate
  (Dol-P), NOT Dol-P-Man; DPM makes Dol-P-Man from Dol-P, so this looks like a mislabeled/too
  literal mapping — MODIFY to GO:0180047. GO:0009101 glycoprotein biosynthetic process (IEA)
  KEEP_AS_NON_CORE (downstream). GO:0035269 protein O-linked glycosylation via mannose (ISS)
  KEEP_AS_NON_CORE (downstream consumer of Dol-P-Man; not DPM3's direct activity).
