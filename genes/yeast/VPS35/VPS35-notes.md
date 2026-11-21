# VPS35 (YJL154C, P34110) curation notes

## Session 2026-11-21: provenance of the research

- Hosted deep-research providers (falcon, perplexity) are not configured in this
  environment, so no `VPS35-deep-research-<provider>.md` file was generated. Everything
  below is my own reading of the cached publications and the UniProt record.
- `just mod-description-deep-research yeast VPS35` succeeded and wrote
  `VPS35-deep-research-sgd.md` (SGD hand-written description, uncited). Its claims are
  checked in the review's `reference_review` for that file.
- PubMed searches (NCBI E-utilities esearch/esummary):
  - `Vps35 AND (Saccharomyces OR yeast) AND (Seaman[au] OR Nothwehr[au] OR Emr[au])`
  - `(Grd19 OR Snx3) AND retromer AND (yeast OR Saccharomyces)`
  - `retromer AND Saccharomyces cerevisiae AND (Vps35 OR Vps35p) AND (plasma membrane OR recycling)`
  - `retromer AND (Ypt7 OR Rab7) AND (yeast OR Saccharomyces) AND (Vps35 OR Vps26)`
  - `Vps35 AND yeast AND (D620N OR Parkinson)`
  - `Gopaldass N[au] AND (retromer OR CROP OR Atg18)`, `Ma M[au] AND Burd CG[au]`
  - `retromer AND yeast AND (sorting signal OR cargo recognition) AND Vps26`
  - three searches for the SGD claim on Ni2+/Cd2+ phenotypes (`VPS35 AND yeast AND
    (nickel OR cadmium ...)`, `VPS35 AND (P316S OR P299S)`, `Kubisch C[au] AND yeast`):
    no paper found.
- Newly cached with `just fetch-pmid`: PMID:1498362, 9105038, 10198044, 11038177,
  11598206, 17420293, 17696874, 17892535, 27262440, 28487947, 30188774, 31337624,
  31471931, 32074001, 36644906, 41699388, 41883240. Already-tracked papers used from the
  main cache: PMID:21062894, 24344282, 28100638, 30224749, 40234461, 42593964,
  20936498, 31332264.
- Full text of PMID:25533483 (Dhungel 2015; cached file is abstract only) was read from
  PMC efetch (PMC4289081) into the scratchpad only; quotes in the review use the cached
  abstract. Full texts of PMID:8649377 (grd screen) and PMID:10198044/11598206 were not
  retrievable (PMC 403 / no body).
- PAINT losses (`just paint-losses yeast VPS35`): "No IRD or IKR loss on this gene's
  lineage."

## Identity

- 944 aa hydrophilic peripheral membrane protein; Pfam Vps35 (PF03635), PANTHER
  PTHR11099:SF0, PIRSF Retromer_Vps35. Originally VPT7.
- "80% of Vps35p peripherally associates with a membranous particulate cell fraction"
  and the null mutant secretes proCPY but delivers PrA, PrB and ALP [PMID:1498362
  "proCPY was quantitatively missorted and secreted by delta vps35 cells"].

## Retromer cargo-selective complex (CSC)

- Seaman 1998 defined retromer: "Vps35p and Vps29p interact and form part of a
  multimeric membrane-associated complex that also contains Vps26p, Vps17p, and Vps5p"
  [PMID:9700157]. Two subcomplexes, Vps35-Vps29-Vps26 and Vps5-Vps17, "assemble together
  on an endosomal membrane" [PMID:9700157].
- Subunit wiring in yeast: R98 in the conserved PRLYL motif "is critical for Vps35p
  binding to Vps26p, while both R(98) and residues 733-944 are needed for efficient
  binding to Vps29p" [PMID:17892535]; a conserved Vps35 region is "essential for the
  interaction with Vps26p/VPS26 and for assembly of the retromer complex" [PMID:17696874].
  Vps26 "promotes the interactions between the cargo-selective component Vps35p and the
  structural components Vps5p/Vps17p" [PMID:11598206].
- Vps5 binds Vps29 and Vps35 through its disordered N-terminus [PMID:40234461 "Vps5
  binds both Vps29 and Vps35 subunits through its unstructured N-terminal domain"]
  (C. thermophilum proteins; the Vps5 PL motif is needed for Vps10 recycling in
  S. cerevisiae).
- Fungal retromer architecture on membranes: "Vps35 forms the 'legs' of these arches,
  and Vps29 resides at the apex" [PMID:30224749, C. thermophilum]. Purified full-length
  yeast CSC has the same overall shape as human CSC [PMID:28100638].
- Vps35-Vps35 dimerisation: "higher-order self-assembly of retromer via the conserved
  Vps35 interface is necessary to drive membrane constriction by the SNX-BARs/retromer
  coat" [PMID:36644906]; yeast vps35 PISA and AAA3KE alleles give an intermediate Vps10
  missorting phenotype [PMID:36644906].
- Cytosolic pool: only ~5% of Vps35 is cytosolic, where it forms a large complex with
  Vps29 [PMID:9700157].

## Cargo recognition

- Vps35 "directly associates with the cytosolic domains of cargo proteins"; cross-linking
  with A-ALP depends on its retrieval signal, and cargo-tail mutations suppress
  cargo-specific vps35 alleles but not the null [PMID:11038177]. The authors
  conclude that Vps35p acts as a receptor for the retrieval signal domains of cargo
  proteins [PMID:11038177].
- Allele specificity: "distinct structural features within Vps35p are required for
  associating with the cytosolic domains of each cargo protein" (A-ALP vs Vps10)
  [PMID:10198044].
- Bipartite recycling signal (Vps10, Ear1): "we propose that cargo recognition by the
  yeast retromer is mediated through Vps26 and Vps35" [PMID:31337624]. Vps35-FLAG
  co-IPs Vps10-GFP also in vps26Δ cells [PMID:31337624].
- Snx3 (Grd19) is a cargo-specific adaptor: Ftr1-Fet3 recycling requires "the sorting
  nexin Grd19/Snx3p, the pentameric retromer complex, and the Ypt6p Golgi Rab GTPase
  module", and "After export from the endosome, Fet3p-Ftr1p transits through the Golgi
  apparatus for resecretion" [PMID:17420293].
- Cargo triggers remodelling: membrane remodelling by Snx3 or SNX-BAR at low
  concentration is reactivated by CSC and cargo [PMID:30188774]. Snx3 and SNX-BARs can
  form hybrid retromer coats [PMID:41699388].
- Other cargoes: Vps68 recycling depends on retromer and Mvp1 [PMID:41883240]; Kex2 and
  Ste13/DPAP A retrieval [PMID:9700157, PMID:22593205].

## Process: endosome-to-Golgi retrieval (core)

- "the VPS29, VPS30, and VPS35 gene products are required for the normal recycling of
  Vps10p from the prevacuolar endosome back to the Golgi" [PMID:9105038].
- "Vps35p is required for the prevacuolar compartment-to-TGN transport of both A-ALP and
  Vps10p" [PMID:10198044].
- Retrieval from the vacuole membrane too: "recycling of the transmembrane receptor Vps10
  from vacuoles requires the retromer, the dynamin-like Vps1, and the Rab7 GTPase Ypt7"
  [PMID:25512334].
- Fission of the retromer/Mvp1-coated tubules needs Vps1 [PMID:24567361]; this agrees
  with the VPS1 review. Chi et al. found no evidence that Mvp1 associates with the
  retromer trimer [PMID:24567361], whereas a weak Mvp1-Vps26 co-IP was reported in 2026
  [PMID:41883240].

## Endosome-to-plasma membrane transport: not a yeast retromer step

- In yeast, "the best-characterized plasma membrane recycling pathways involve transit of
  cargo through the Golgi for resecretion" [PMID:17420293]; the retromer-dependent route
  for Ftr1 passes through the Golgi [PMID:17420293].
- Snc1: retromer is a minor third route; the data "support the existence of three
  distinct and parallel recycling pathways mediated by Drs2/Rcy1/COPI, Snx4-Atg20, and
  retromer that retrieve an exocytic v-SNARE from the endocytic pathway to the Golgi"
  [PMID:32074001], and retromer "plays no role in FM4-64
  recycling" [PMID:32074001].
- TGN residents "do not appear to visit the plasma membrane" [PMID:11038177].
- So GO:0032456 (endosome to plasma membrane transport; GO:0099638 was merged into it)
  overstates Vps35's role in yeast: its step in PM recycling is endosome-to-Golgi.
  PMID:9700157 (the ComplexPortal NAS reference) contains no statement about plasma
  membrane transport (full text searched).

## Ypt7 (Rab7) recognition

- GST-Ypt7 and GST-Ypt7(Q68L) beads "efficiently capture the retromer CSC subunits
  (Vps26, Vps29, and Vps35)" but not Vps5/Vps17 [PMID:22593205]; Vps35 repeat 6
  (aa 218-252) is required for Ypt7 binding and vacuole targeting, and Vps35-GFP reaches
  the vacuole membrane in vps26Δ cells [PMID:22593205].
- "Recognition of Ypt7 by retromer is required for its function in retrograde sorting"
  [PMID:22593205]; Vps35Δ6 missorts Vps10, Ste13 and Ftr1 [PMID:22593205].
- "Ypt7-GTP specifically binds to the retromer cargo-recognition subcomplex"
  [PMID:21062894, abstract]. SNX-BAR displaces Ypt7 from cargo-bound CSC during tubule
  formation [PMID:28100638].
- This supports a NEW GO:0031267 small GTPase binding row (IPI, PMID:22593205).

## CROP complex and vacuole fission

- Atg18 co-purifies with Vps26, Vps29 and Vps35; CSC mutants (incl. vps35Δ) "maintained
  their large central vacuoles" after salt shock [PMID:35466426]; "Integration into CROP
  potentiates the membrane fission activity of the PROPPIN Atg18 on synthetic liposomes"
  [PMID:35466426].
- SGD annotated only GO:0170071 CROP complex from this paper (QuickGO by reference: four
  rows, VPS35, VPS29, PEP8, ATG18). Comparator: ATG18 carries GO:0090148 membrane
  fission (IDA, PMID:29030482) but no S. cerevisiae protein carries GO:0140572 vacuole
  fission (QuickGO exact, taxon 559292: 0 hits; the same term id returns 271 IEA hits in
  other fungi, so the query works). I did not propose a NEW vacuole fission row.

## Other phenotypes

- Golgi retention: grd screen mutants mislocalise A-ALP to the vacuole [PMID:8649377,
  abstract only]; loss of Vps35 "rapidly leads to mislocalization of A-ALP, a model TGN
  membrane protein, to the vacuole" [PMID:10198044]. Kept as non-core (outcome of
  retrieval).
- PD-gene genetic interaction (Dhungel 2015, full text via PMC): TIF4631 upregulation
  is toxic in vps35Δ, raises a UPRE-lacZ reporter threefold, and is suppressed by VPS10
  overexpression; the authors explain it through Vps10 recycling and protein misfolding.
  No evidence that Vps35 regulates UPR signalling, so GO:1900102 is over-annotated.
- Copper: vps35Δ is copper-sensitive; D686N (yeast equivalent of D620N) does not rescue
  [PMID:27262440, abstract]. High-level D686N expression causes α-synuclein-dependent
  toxicity [PMID:28487947].
- Lipid droplets: Vps35 is recruited to the vacuole-LD interface during stationary phase
  and retromer promotes LD internalization [PMID:42593964]. Not annotated here.

## GO-CAMs (`gocams/index.tsv`)

- No production GO-CAM contains S. cerevisiae VPS35 (SGD:S000003690, P34110).
- S. pombe model gomodel:693b3c0900002174 "retrograde transport endosome to Golgi
  (GO:0042147) (partial)" (production, PomBase, 2025-12/2026-01) has the CSC as a complex
  node (GO:0030906; has_part vps35 SPCC777.13, vps29 SPAC15E1.06, vps26 SPAC4G9.13c)
  enabling GO:0140312 cargo adaptor activity, occurs_in GO:0005768 endosome, part_of
  GO:0042147; evidence ECO:0000305 / GO_REF:0000111 with GO:0030906.
  Causal chain: snx3 (GO:0043495 protein-membrane adaptor) -RO:0012009-> CSC
  -RO:0012009-> retromer tubulation complex (GO:0030905; vps5 SPCPJ732.01, vps17
  SPAPJ696.01c; GO:0180020 membrane bending, part_of GO:0097750) -RO:0002304-> grp1
  (vesicle membrane tethering) -> GARP -> SNARE complex.
- S. pombe mvp1 (SPAC3A11.06) has GO:0140312 / GO:0042147 / GO:0010008 in the MVB model
  gomodel:6918f23700004102.
- This matches the review's core function (contributes_to cargo adaptor activity, in
  GO:0030906, part_of GO:0042147). The pombe model uses endosome; this review uses
  endosome membrane for the peripheral-membrane location.

## Decisions summary (see review YAML)

- ACCEPT: retromer complex and CSC (IBA, IEA, IMP, IPI), retrograde transport endosome to
  Golgi (IBA, IEA, IPI, NAS), cargo adaptor activity contributes_to (IBA, IMP, IPI),
  late endosome (IBA), protein transport (IEA).
- MODIFY: endosome (IPI) and endomembrane system (NAS) -> GO:0010008 endosome membrane.
- TOO_GENERAL: membrane (IEA, SubCell).
- KEEP_AS_NON_CORE: cytosol, fungal-type vacuole membrane, CROP complex, protein
  retention in Golgi apparatus.
- MARK_AS_OVER_ANNOTATED: endosome to plasma membrane transport (NAS, ComplexPortal),
  obsolete endosome to plasma membrane protein transport (IBA), negative regulation of ER
  UPR (IGI).
- REMOVE: nine bare protein binding IPI rows (Vps5, Vps17, Vps29 partners), per policy.
- NEW: small GTPase binding (IPI, PMID:22593205).
