# DLK1 notes

Deep research providers unavailable in this environment; research from UniProt P80370 and the 5 cached
publications.

## Topology / localization
- Single-pass type I membrane protein: signal 1-23, extracellular 24-303 (six EGF-like repeats),
  TM 304-327, cytoplasmic 328-383. UniProt: "SUBCELLULAR LOCATION: Membrane; Single-pass type I membrane
  protein. Cytoplasm (By similarity)".
- The ectodomain is shed and circulates as fetal antigen 1 [PMID:7925474 "the primary structure,
  glycosylation and tissue localization of fetal antigen 1 (FA1) isolated from second-trimester human
  amniotic fluid"], so both a plasma-membrane and a soluble extracellular pool exist.
- Conclusion: plasma membrane with EGF-repeat ectodomain exposed, plus a bona fide secreted form.

## Functions
- Non-canonical Notch ligand lacking the DSL domain; inhibits NOTCH1-dependent proliferation
  [PMID:25093684].
- Inhibits osteoblast differentiation/bone formation and increases osteoclastogenesis and resorption in
  osteoblast-specific overexpressing mice [PMID:21308776].
- Imprinted (paternally expressed) DLK1-DIO3 locus; oncofetal re-expression (neuroblastoma, SCLC,
  hepatoblastoma) underlies interest as a surface target.

## Curation decisions
- Two interactome rows (GRN, SPRED1; PMID:32814053) removed per the protein-binding policy.
- Calcium ion binding (InterPro EGF-domain mapping) marked over-annotated: structural inference, no
  DLK1-specific evidence.
- `membrane` rows (incl. IBA) modified to plasma membrane; generic cell differentiation rows modified to
  the supported osteoblast/ossification terms.
