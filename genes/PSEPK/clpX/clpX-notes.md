# clpX (Q88KI9) — Pseudomonas putida KT2440 — review notes

Gene: clpX / PP_2301
Protein: ATP-dependent Clp protease ATP-binding subunit ClpX
UniProt: Q88KI9 (CLPX_PSEPK), 442 aa, Reviewed/Swiss-Prot, evidence PE 3 (inferred from homology)
HAMAP rule: MF_00175 (ClpX)

## FUNCTION

ClpX is the AAA+ ATPase (unfoldase) component of the ClpXP protease. It is the
ATP-dependent specificity/recognition factor that selects substrate proteins,
unfolds them, and translocates them into the ClpP peptidase chamber for
degradation. In the absence of ClpP it can act as a standalone chaperone.

- [UniProt "ATP-dependent specificity component of the Clp protease. It directs the protease to specific substrates. Can perform chaperone functions in the absence of ClpP."]

The protein contains an N-terminal C4-type zinc-binding domain (ZB domain),
involved in substrate/adaptor recognition, and a central AAA+ ATPase module with
a P-loop / Walker A nucleotide-binding site that binds and hydrolyzes ATP to
power unfolding and translocation.

- ZB domain: [UniProt "DOMAIN          19..72 /note=\"ClpX-type ZB\""]
- ATP-binding (Walker A) site: [UniProt "BINDING         137..144 /ligand=\"ATP\""]

## SUBUNIT

ClpX assembles into a homohexameric ring. In the presence of ATP this ring docks
onto one or two heptameric ClpP rings (14 ClpP subunits) to form the ClpXP
protease, a barrel-like structure with an internal proteolytic chamber that
resembles the architecture of the eukaryotic proteasome.

- [UniProt "Component of the ClpX-ClpP complex. Forms a hexameric ring that, in the presence of ATP, binds to fourteen ClpP subunits assembled into a disk-like structure with a central cavity, resembling the structure of eukaryotic proteasomes."]

## COFACTOR

- Zinc: N-terminal C4-type zinc finger coordinated by four cysteines.
  - [UniProt "BINDING         31 /ligand=\"Zn(2+)\""]
  - [UniProt "BINDING         34 /ligand=\"Zn(2+)\""]
  - [UniProt "BINDING         53 /ligand=\"Zn(2+)\""]
  - [UniProt "BINDING         56 /ligand=\"Zn(2+)\""]
- ATP: bound and hydrolyzed at the AAA+ Walker A P-loop (residues 137-144).
  - [UniProt "BINDING         137..144 /ligand=\"ATP\""]

## SIMILARITY / CLASSIFICATION

- [UniProt "Belongs to the ClpX chaperone family."]
- Keywords: [UniProt "ATP-binding; Chaperone; Metal-binding; Nucleotide-binding; Reference proteome; Zinc."]
- Domains/families: AAA+ ATPase core (Pfam PF07724 AAA_2), ClpB_D2-small
  (PF10431), zf-C4_ClpX zinc finger (PF06689); NCBIfam TIGR00382 clpX.

## REVIEW REASONING (annotation-by-annotation)

All 8 GOA annotations are IEA (electronic). The only cited primary reference
(PMID:12534463) is the KT2440 genome sequencing paper and contains no
ClpX-specific functional data; functional inferences here rest on the UniProt
HAMAP-derived record and conserved ClpX/ClpXP biology.

- GO:0005524 ATP binding (F, IEA) — real, but broad relative to the specific
  GO:0016887 ATP hydrolysis activity that is also annotated. Mark as
  over-annotated. The Walker A motif is present (FT BINDING 137..144).
- GO:0006457 protein folding (F? actually BP, IEA) — imprecise. ClpX is an
  unfoldase that feeds substrates to ClpP for degradation; the dominant cellular
  role is protein catabolism/quality control, not folding. MODIFY to
  GO:0030163 protein catabolic process.
- GO:0008270 zinc ion binding (F, IEA) — ACCEPT; supported by the C4 ZB domain
  with four cysteine Zn ligands.
- GO:0009376 HslUV protease complex (C, IEA TreeGrafter) — REMOVE. ClpX forms
  the ClpXP (endopeptidase Clp) complex, not the HslUV complex (which uses HslU,
  a distinct AAA+ ATPase). This is a TreeGrafter mis-graft across the AAA+ family.
  Correct complex is GO:0009368 endopeptidase Clp complex.
- GO:0016887 ATP hydrolysis activity (F, IEA) — ACCEPT; core enzymatic activity
  that powers unfolding/translocation.
- GO:0046983 protein dimerization activity (F, IEA) — over-annotation. ClpX forms
  a homohexamer, not a dimer; "dimerization" is an imprecise InterPro-derived
  call. MARK_AS_OVER_ANNOTATED.
- GO:0051301 cell division (P, IEA TreeGrafter) — KEEP_AS_NON_CORE. ClpXP
  influences division indirectly by degrading regulators (e.g. cell-division
  inhibitors / FtsZ-related factors) in other bacteria; pleiotropic downstream
  effect, not the core proteolytic function.
- GO:0140662 ATP-dependent protein folding chaperone (F, IEA) — ACCEPT as the
  best available MF for the ATP-dependent unfoldase/chaperone activity (UniProt
  notes chaperone function in the absence of ClpP).

## OPEN ISSUES

- There is no current, non-obsolete GO MF term that cleanly captures "ATP-dependent
  protein unfoldase / translocase" activity; GO:0051082 (unfolded protein binding)
  is obsolete and GO:0140662 is the nearest active MF.
- No P. putida-specific experimental characterization of ClpXP substrates was
  found; all evidence is homology-based.
