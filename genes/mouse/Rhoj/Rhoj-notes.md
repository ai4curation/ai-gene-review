# Rhoj (mouse, Q9ER71) review notes

## 2026-10-20 de novo review

### Deep research

`just deep-research-falcon mouse Rhoj --fallback perplexity-lite` failed. Falcon/Edison
returned 403 on authentication, and the perplexity-lite fallback returned 401 (quota
exceeded). No deep-research file exists. The review was written from the cached
literature listed below, which I retrieved by PubMed search and cached with
`cache_publication`.

### Identity and evolutionary grounding

- Swiss-Prot RHOJ_MOUSE, 214 aa, 2 isoforms. Isoform 2 (VSP_005709, residues 4-13
  missing) is the cDNA cloned by Vignal et al. [PMID:10967094].
- PANTHER: PTHR24072 (Rho family). In PTHR24072-entries.csv, Q9ER71 and human RHOJ
  Q9H4E5 are both RhoJ. Human Q9H4E5 is in subfamily SF17 ("RHO-RELATED GTP-BINDING
  PROTEIN RHOJ"), so mouse Rhoj and human RHOJ are 1:1 orthologs in the same subfamily.
  Its paralog Rhoq (TC10) is in a separate RhoQ group.
- Phylogeny: "Cdc42 underwent gene duplication to produce two related proteins-RhoQ and
  RhoJ" [PMID:32302585]. Rhoj is therefore inside the Cdc42-lineage clade.
- PAINT nodes reaching Rhoj:
  - PTN000632671 (Rho-family root): GTPase activity, GTP binding, plasma membrane, actin
    filament organization and signal transduction. Mouse Rhoj (MGI:1931551) is a seed for
    signal transduction, and human Q9H4E5 is a seed for GTPase activity, GTP binding and
    plasma membrane.
  - PTN008604842 (Cdc42 lineage, Opisthokonta): endocytosis and establishment of cell
    polarity, with Cdc42-ortholog seeds.
  - PTN008604840: protein kinase binding (PAK binding of Cdc42).
- ISO/ISS rows come from human Q9H4E5, which is the same subfamily, so transfer is
  appropriate.

### What is experimental in mouse, and what is transferred

Experimental in mouse (mouse protein or mouse genetics):
- Mouse TCL cDNA: GTP-dependent binding to the CRIB domains of Pak1 and WASP, and
  morphogenic F-actin ruffles in REF-52 fibroblasts [PMID:10967094 "GTP-bound but not
  GDP-bound TCL protein directly interacts with Cdc42/Rac interacting binding domains,
  such as those found in PAK and WASP"]. In vitro kinetics were reported in the same
  paper. MGI coded GTPase activity as ISS, which may mean that the kinetic assay used
  the human construct. The abstract alone does not settle this.
- Rhoj KO / inducible KO / EC-specific KO mice: reduced forward EC migration in aortic
  rings, reduced tip-cell positioning, delayed retinal vascular development, and reduced
  OIR neovascular tufts [PMID:32347571 "These results indicate that RhoJ is required for
  VEGF‐dependent forward EC migration in sprouting vessels."]. Delayed retinal
  vascularization was also reported in [PMID:22535667].
- Rhoj-null mice show perivascular fibronectin deregulation [PMID:32302585].
- Rhoj blockade or deletion suppresses tumor angiogenesis [PMID:24434213].
- Rhoj knockdown impairs migration of mouse endothelial progenitors [PMID:33115267], and
  impairs adipogenesis and mitotic clonal expansion in 3T3-L1 cells [PMID:12578843,
  PMID:20190400]. The adipogenesis results are cell-line knockdown phenotypes and are
  not annotated.

Shown with human RHOJ/TCL in human cells (transferred to mouse by orthology):
- Plasma membrane localization and the N-terminal and 121-129 determinants
  [PMID:27660391].
- Early/sorting endosome localization, and a role in delivering internalized receptors
  to early endosomes, while uptake itself is unaffected [PMID:12960428].
- PlexinD1 and VEGFR2 interactions (human constructs in HUVEC and 293T cells)
  [PMID:32347571].
- GLUL-dependent palmitoylation [PMID:30158707].
- Focal adhesions and actomyosin contractility [PMID:21148427]. ERG regulation and lumen
  formation [PMID:21628409].

### Decisions (summary)

- MF: GTPase activity, GTP binding and G protein activity are ACCEPTED. G protein
  activity is used as the core MF because it describes the switch and effector-binding
  role.
- Protein binding: the two Pak1 rows are MODIFIED to protein kinase binding
  (GO:0019901). The WASP and Dock10 rows are REMOVED under the protein-binding policy.
  Removal does not dispute the interactions.
- CC: plasma membrane is ACCEPTED in all four rows. It is transferred, not measured, in
  mouse.
- BP: Rho protein signal transduction, actin cytoskeleton/filament organization,
  regulation of EC migration, positive regulation of cell migration involved in
  sprouting angiogenesis, and regulation of sprouting angiogenesis are ACCEPTED.
  Signal transduction is TOO_GENERAL. Endocytosis, establishment of cell polarity,
  regulation of cell shape and retina vasculature morphogenesis are KEEP_AS_NON_CORE.
- No NEW annotations are proposed. Early/sorting endosome and focal adhesion have only
  human-cell evidence, so they are raised as questions instead.
