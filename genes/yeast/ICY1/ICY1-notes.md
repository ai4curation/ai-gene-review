# ICY1 (YMR195W) — curator notes

UniProt: Q04329 (ICY1_YEAST). Systematic name YMR195W. SGD: S000004808.
Standard name ICY1 = "Interacting with CYtoskeleton" (SGD nomenclature; the name
predates and is not backed by a demonstrated molecular function). 127 aa, 14.3 kDa.
This is an UNDERSTUDIED ("dark") gene: molecular function and biological process
are officially undetermined (GO ND).

## Provenance of primary facts

- **Function (indirect / genetic):** [PMID:14504216 "we screened for high-copy
  suppressors of the inability of tim18Delta mutants to live without mitochondrial
  DNA (mtDNA). We identified several genes encoding cytosolic proteins, including
  CCT6, SSB1, ICY1, TIP41, and PBP1, which, when overproduced, rescue the mtDNA
  dependence of tim18Delta cells."] and [PMID:14504216 "disruption of the genes
  identified by the different suppressors produces cells that are unable to grow
  without mtDNA."]. Interpretation: ICY1 overexpression is a high-copy suppressor
  of the petite-negative phenotype of mitochondrial-import mutants, and icy1Δ cells
  cannot survive loss of mtDNA (become petite-negative). This paper describes ICY1
  as a **cytosolic** protein. It does NOT assign a molecular function.
- **Subcellular location (GFP screen, HDA):** [PMID:14562095] Huh et al. global GFP
  localization — ICY1 is called to the **vacuole membrane** (SGD GO:0000329
  fungal-type vacuole membrane; UniProt "Vacuole membrane; Peripheral membrane
  protein"). Note the abstract is method-level; the ICY1 call is from the dataset.
  There is thus a localization discrepancy in the literature: cytosolic (14504216)
  vs. vacuole membrane (14562095). Both are recorded; neither pins a mechanism.
- **Disruption phenotype:** UniProt records "Invasive growth defect with elongated
  cell morphology" citing [PMID:12673624] (Suzuki et al., transposon screen in a
  Sigma1278b pseudohyphal strain). The abstract is a general screen description and
  does not name ICY1; the ICY1-specific phenotype is in the full-text tables (curator
  read full text — do not overrule).
- **Induction:** [PMID:15843968] ICY1 is induced by amino acid starvation
  (adhesion-inducing conditions). Abstract: ["adhesion can be induced by starvation
  for amino acids, and depends on the transcriptional activator of the general amino
  acid control system, Gcn4p"] and ["Twenty-two novel genes were identified as
  inducible by amino acid starvation"]. ICY1 is among the induced set (full-text
  table). UniProt: "Induced by amino acids starvation."
- **Abundance:** [PMID:14562106] ~4050 molecules/cell in log-phase SD medium
  (UniProt MISCELLANEOUS). Consistent with a real, moderately expressed protein.
- **SGD description (verbatim):** "Protein of unknown function; required for
  viability in rich media of cells lacking mitochondrial DNA; mutants have an
  invasive growth defect with elongated morphology; induced by amino acid
  starvation." (yeastgenome.org locus S000004808).

## Orthology / paralogy

- SGD lists ICY1's **paralog** (from the whole-genome duplication) as **ATG41 /
  ICY2 (YPL250C)**, which functions in autophagosome formation. However, Icy1 has
  only **low sequence similarity** to Atg41/Icy2, and — unlike icy2Δ — icy1Δ does
  NOT show an autophagy defect. So the autophagy role of the paralog cannot be
  transferred to ICY1. (yeastgenome.org; Atg41 autophagy paper PMID via search.)
- No InterPro / Pfam / PANTHER / SUPFAM / PROSITE / SMART family is assigned in the
  UniProt record (checked: none). No transmembrane segment, no signal peptide, no
  coiled-coil, no recognizable catalytic motif. OrthoDB cluster 4033322at2759,
  HOGENOM CLU_149528_0_0_1 — small, fungal-restricted grouping.

## Inline domain / sequence reasoning (done inline, no sub-agent)

Sequence (127 aa):
MSSNYATPLDDEVFPLSFANYQFTEHVSLGEHYSLNTSEDAKYNNLNGPFVVPRDTGKFDLNTSSASDETVFSLDNPQENNYKHQAMNNVQDCRMAVAAKTTQSCDKLTDLYANAAQQNYRLWLSSF

- Composition: Asn-rich (N 11.0%), Ser 10.2%, Thr 7.1%; net acidic (D+E 16 vs K+R 8);
  only 2 Cys, 1 Trp. This bias (Asn/Ser/Thr-rich, acidic, low aromatic/Cys) is
  typical of an intrinsically disordered / low-complexity small protein rather than
  a globular enzyme.
- No PROSITE-style catalytic signature is apparent by eye; the "MAVAAK" / "CDKLTD"
  stretches are not diagnostic motifs. UniProt annotates the whole chain as a single
  feature (PRO_0000203325) with no domains.
- The "Membrane / Vacuole; Peripheral membrane protein" keywords derive purely from
  the GFP localization; there is no hydrophobic membrane anchor in the sequence, so
  any membrane association is peripheral (consistent with the SubCell IEA).

## KNOWN vs NOT-known summary

KNOWN (evidence-supported):
- Small (127 aa) fungal protein, moderately abundant (~4050 molecules/cell).
- Genetic role linked to survival of mtDNA-less (rho0) cells: high-copy suppressor
  of petite-negativity in import mutants; icy1Δ is petite-negative [PMID:14504216].
- Localizes to vacuole membrane in a genome-wide GFP screen [PMID:14562095];
  described as cytosolic in [PMID:14504216] — location not fully settled.
- icy1Δ: invasive-growth defect with elongated morphology [PMID:12673624]; SGD also
  lists abnormal vacuolar morphology, petite-negative, decreased growth.
- Transcriptionally induced by amino-acid starvation (Gcn4-linked context)
  [PMID:15843968].

NOT known (knowledge gaps — the real deliverable):
- Molecular function: NO biochemical activity, ligand, or catalytic role known
  (GO MF = ND). No enzymatic motif; likely non-enzymatic. The "cytoskeleton
  interaction" implied by the ICY1 name is not substantiated by any cited
  molecular-interaction evidence I could verify.
- Biological process: the mtDNA-survival and invasive-growth phenotypes are
  genetic/indirect; the direct pathway ICY1 acts in is undefined (GO BP = ND).
- Whether the vacuole-membrane localization is functionally meaningful or the
  cytosolic pool is the active one is unresolved.
- Direct binding partners / whether it truly "interacts with the cytoskeleton" —
  unverified in the sources available here.

## Curation plan

- 4 GOA annotations. Localization terms (GO:0005774 IEA SubCell; GO:0000329 HDA)
  are supported by the GFP screen → keep. The vacuole-membrane call is the only
  positive experimental localization; keep as non-core (localization, not function).
- ND root terms (GO:0003674, GO:0008150) are placeholders indicating "no data";
  keep as-is (standard ND handling), do not invent MF/BP.
- core_functions: minimal/empty — no defensible molecular function to assert.
- knowledge_gaps: REQUIRED, primary deliverable (unknown MF, BP, mechanism of the
  petite-negative/invasive-growth phenotypes, reality of cytoskeleton interaction).
