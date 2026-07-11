# MPDU1 (Lec35 / SL15) review notes

UniProtKB:O75352, human, HGNC:7207. 247 aa, multi-pass ER-membrane protein
(7 predicted TM helices), two PQ-loop domains (Pfam PF04193 ×2; SMART CTNS/lysosomal
cystine-transporter-like repeats). Belongs to the MPDU1 family (TC 2.A.43.3).
Deep research (falcon) unavailable — provider out of credits (HTTP 402). Review grounded
in UniProt record, GOA, and cached publications.

## Function (verified biology)

MPDU1 = Mannose-P-dolichol utilization defect 1 protein; hamster ortholog = Lec35p.
It is **required for efficient UTILIZATION of the lipid-linked monosaccharide donors
mannose-P-dolichol (Dol-P-Man / MPD) and glucose-P-dolichol (Dol-P-Glc / GPD)** on the
lumenal side of the ER, but it is **NOT itself a synthase and has no known catalytic
activity**. It appears to control the orientation/presentation of these donors so their
mannosyl/glucosyl groups are available to the lumenal glycosyltransferases.

- PMID:11179430 (Anand et al., Mol Biol Cell 2001) — definitive functional paper:
  - "The Lec35 gene product (Lec35p) is required for utilization of the mannose donor
    mannose-P-dolichol (MPD) in synthesis of both lipid-linked oligosaccharides (LLOs)
    and glycosylphosphatidylinositols"
  - Lec35p also required for MPD-dependent C-mannosylation of Trp residues and for
    GPD-dependent glucosylation of LLO: "MPD-dependent C-mannosylation of tryptophanyl
    residues, and glucose-P-dolichol (GPD)-dependent glucosylation of LLO. Both were
    found to require Lec35p."
  - Non-catalytic: "it was determined that Lec35p is not directly required for the
    enzymatic transfer of mannose from the donor to the acceptor substrate."
  - Localization/mechanism: "predicts a novel endoplasmic reticulum membrane protein";
    "Lec35p controls an aspect of MPD orientation in the endoplasmic reticulum membrane
    that is crucial for its activity as a donor substrate."

- PMID:11733564 (Schenk et al., J Clin Invest 2001) — MPDU1-CDG (CDG-If):
  - Patients' fibroblasts "accumulated incomplete lipid-linked oligosaccharide precursors
    for N-linked protein glycosylation"; the Lec35/MPDU1 gene is "known to be involved in
    the use of dolichylphosphomannose and dolichylphosphoglucose"; expression of normal
    Lec35 cDNA "restored normal lipid-linked oligosaccharide biosynthesis." IGI/TAS basis.

## Disease

CDG-If (MIM:609180), MPDU1-CDG (Orphanet 79323). Under-glycosylation of serum
glycoproteins; multisystem — nervous system defects, psychomotor retardation, and the
literature reports skin (ichthyosis) and visual involvement. Causative variants G73E,
L74S, L119P (UniProt VARIANT features; PMID:11733556, PMID:11733564).

## GOA annotations (12 lines) — decisions

MF:
- GO:0005515 protein binding (IPI, PMID:32296183, with MANBAL Q9NQG1) — bare protein
  binding; interaction IS corroborated by UniProt INTERACTION (O75352;Q9NQG1 MANBAL
  NbExp=3), but term uninformative → MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding (IPI, PMID:16237761, with HCV F protein P0C045) — bare
  protein binding, viral Y2H hit; uninformative and not a core function →
  MARK_AS_OVER_ANNOTATED (not REMOVE per policy on experimental IPIs).

CC:
- GO:0005789 endoplasmic reticulum membrane (NAS, PMID:11179430) — core location. ACCEPT.
- GO:0005783 endoplasmic reticulum (IDA, HPA) — correct, broader than ER membrane. ACCEPT.
- GO:0016020 membrane (IEA, SubCell) — correct but generic parent of ER membrane →
  MARK_AS_OVER_ANNOTATED (superseded by ER membrane).
- GO:0016020 membrane (HDA, PMID:19946888, NK-cell membrane proteome) — generic; MS
  proteome hit → MARK_AS_OVER_ANNOTATED.
- GO:0005739 mitochondrion (IDA, HPA) — inconsistent with ER-membrane biology and family;
  no functional support for a mitochondrial role. Likely IF cross-reactivity/contaminant.
  MARK_AS_OVER_ANNOTATED (HPA IDA; not confidently REMOVE).

BP:
- GO:0006488 dolichol-linked oligosaccharide biosynthetic process (TAS, PMID:11733564) —
  core. ACCEPT.
- GO:0009312 oligosaccharide biosynthetic process (IDA, PMID:11179430) — correct but
  parent of GO:0006488 → MODIFY to GO:0006488.
- GO:0009312 oligosaccharide biosynthetic process (IGI, PMID:11733564) — MODIFY to
  GO:0006488 (more specific, same evidence base).
- GO:0009312 oligosaccharide biosynthetic process (IBA, GO_REF:0000033) — PAN-GO
  phylogenetic; correct but general. KEEP_AS_NON_CORE (IBA, defer to phylogenetic call;
  broader than experimentally-supported GO:0006488).
- GO:0006457 protein folding (NAS, PMID:11179430) — indirect/downstream (N-glycosylation
  supports folding); not MPDU1's molecular role → MARK_AS_OVER_ANNOTATED.

## Core functions
No informative/catalytic MF term exists in GOA (only bare protein binding) and MPDU1 is
non-catalytic — do NOT invent a transferase MF. Represent core function via BP
(GO:0006488 dolichol-linked oligosaccharide biosynthetic process) + location
(GO:0005789 ER membrane).
