# MMAA (Q8IVH4) review notes

## Summary of verified biology

MMAA = "Methylmalonic aciduria type A protein" = the human **cblA** protein. It is a
**mitochondrial GTPase** of the **SIMIBI-class G3E GTPase family, ArgK/MeaB subfamily**
(UniProt SIMILARITY; InterPro IPR005129 GTPase_ArgK; Pfam PF03308 MeaB; CDD cd03114
MMAA-like). It is **NOT the methylmalonyl-CoA mutase (MMUT/MUT)** and does NOT itself
isomerize methylmalonyl-CoA. Instead it is a **G-protein chaperone / cofactor-maintenance
protein for MMUT**.

Deep research: `just deep-research` recipe is absent in this worktree (no
`-deep-research-*.md` produced or fabricated). Grounded instead in the UniProt record,
the 6 cached primary publications, GOA, and `~/repos/dismech/kb/disorders/Methylmalonic_Acidemia.yaml`.

## Core functional facts (with provenance)

- **GTPase / GTP binding.** Crystallized GDP-bound (PDB 2WWW, res 72-418); binds and
  hydrolyzes GTP; GTPase activity is stimulated ~by MMUT (GAP effect).
  [PMID:20876572 "We show that MMAA exhibits GTPase activity that is modulated by MUT and that the two proteins interact in vitro and in vivo"]
  [UniProt CATALYTIC ACTIVITY: "GTP + H2O = GDP + phosphate + H(+); Rhea:RHEA:19669"; ACTIVITY REGULATION "GTPase activity is stimulated by MMUT"]
  KM(GTP) 42 uM (PMID:28497574), kcat 0.201 min-1. GTP-binding loops at 150-158, 292, 328-330.

- **Gatekeeper / AdoCbl delivery to MMUT (GTP-dependent).** Gates the transfer of
  adenosylcobalamin (AdoCbl) from MMAB (ATR) onto MUT apoenzyme; complex formation is
  nucleotide-selective (GMPPNP over GDP) and requires MUT apoenzyme.
  [PMID:20876572 "our data point to a gatekeeping role for MMAA by favoring complex formation with MUT apoenzyme for AdoCbl assembly and releasing the AdoCbl-loaded holoenzyme from the complex, in a GTP-dependent manner"]
  [PMID:28497574 "MMAA regulates the incorporation of the cofactor adenosylcobalamin (AdoCbl), generated from the MMAB adenosyltransferase, into the destination enzyme methylmalonyl-CoA mutase (MUT)"; "all mutations interfered with gating the transfer of AdoCbl from MMAB to MUT"]

- **Protectase + reactivase (dual chaperone role toward MMUT).** Protects MUT from
  progressive inactivation (slows formation of oxidized OH2Cbl / cob(II)alamin) and
  reactivates inactive MUT by GTP-hydrolysis-driven exchange of the damaged cofactor.
  [PMID:21138732 "MMAA plays dual roles in MCM activity. When it was added at the beginning of the reaction, it prevents inactivation by guarding MCM. After 60 min of reaction, when MCM is inactive, the addition of MMAA increases the enzymatic activity through GTP hydrolysis, indicating reactivation of MCM by exchange of the damaged cofactor"]
  [PMID:28943303 "the complex formation of hMCM/hMMAA decreases the rate of oxidized cofactor formation, protecting the hMCM enzyme"; "hMMAA is able to remove the damaged cofactor through GTP hydrolysis"]

- **Allosteric regulation of oligomerization.** Human MCM-CblA(MMAA) forms interconverting
  nucleotide-sensitive oligomers (M2C1, M2C2, M3C3...); GTPase-driven resolution to the
  loading-ready M2C1 state is required to load MCM with AdoCbl. Switch III patient
  mutations corrupt this. [PMID:31056463 full text].

- **Homodimer.** [PMID:20876572 "MMAA ... α2 homodimer"; UniProt SUBUNIT "Homodimer";
  GO:0042802/GO:0042803 IDA].

- **Localization.** Mitochondrion (matrix; has cleaved mitochondrial transit peptide 1-65),
  colocalizes with MMUT; also detected cytoplasm/cytosol (IDA/HPA).
  [PMID:28943303 "in vivo localization of hMMAA and its colocalization with hMCM in human fibroblasts mitochondria were demonstrated"]
  [UniProt SUBCELLULAR LOCATION: Mitochondrion; Cytoplasm; TRANSIT 1..65 Mitochondrion]

- **Disease.** Deficiency = methylmalonic aciduria, cblA type (MACA; MIM 251100), autosomal
  recessive, often vitamin-B12(hydroxocobalamin)-responsive. cblA mutations reduce the
  mitochondrial AdoCbl pool. [UniProt DISEASE; disorders KB Methylmalonic_Acidemia.yaml;
  PMID:31056463 "AdoCbl ... reduced to 3.3±1.6 % of the total pool in fibroblasts from cblA patients"]

## Annotation-level notes

- MF GTPase activity (GO:0003924) IDA x3 (20876572, 28943303, 21138732), IMP (28497574),
  IBA, IEA — all ACCEPT; this is a core MF.
- MF GTP binding (GO:0005525) IDA x2, IEA — ACCEPT (component of the GTPase MF).
- MF molecular carrier activity (GO:0140104) TAS(Reactome R-HSA-3159259) + IDA(31056463,
  MGI). MMAA does not itself carry/bind cobalamin as its cargo — it is the G-protein that
  GATES AdoCbl transfer (AdoCbl is carried/handed off between MMAB and MUT). "Molecular
  carrier activity" is a defensible but imprecise/over-annotation of the gating role; the
  more precise MF is GTPase activity and the role is a regulatory/chaperone one. MODIFY /
  MARK_AS_OVER_ANNOTATED (not itself the cofactor carrier).
- BP cobalamin metabolic process (GO:0009235) IDA/TAS — ACCEPT (core BP: intracellular B12
  handling / AdoCbl delivery).
- protein binding (GO:0005515) IPI with MMUT (P22033) — bare "protein binding"; the real
  interactant is MMUT and captured better as the chaperone/complex-formation role.
  MARK_AS_OVER_ANNOTATED (do NOT REMOVE per policy).
- identical protein binding / protein homodimerization (GO:0042802/GO:0042803) IDA/IPI —
  ACCEPT (homodimer is real, structurally verified).
- CC mitochondrion (GO:0005739) IDA/IEA/HTP, mitochondrial matrix (GO:0005759) TAS x4 —
  ACCEPT. Mitochondrion IDA is core. Matrix (Reactome) is consistent.
- CC cytoplasm (GO:0005737) IBA/IEA/IDA and cytosol (GO:0005829) IDA(HPA) — MMAA is
  synthesized with a mito transit peptide and functions in the matrix; cytoplasm/cytosol
  signal likely reflects precursor / partial import / antibody localization. KEEP_AS_NON_CORE
  (real detection but not the core functional location).
- PMID:34800366 HTP mitochondrion — ACCEPT as corroborating (large-scale mito proteome).
