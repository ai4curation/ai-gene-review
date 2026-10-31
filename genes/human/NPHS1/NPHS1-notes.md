# NPHS1 (nephrin, human, O60500) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: NPHS1 is the closest experimentally characterised relative of DROME/sns
(Q0E9F2). This review treats NPHS1 in its own right; ProtNLM2 output was not
consulted.

### Deep research

- `just deep-research-falcon human NPHS1 --fallback perplexity-lite` failed: falcon
  returned `403 Forbidden` at the Edison auth endpoint, and the perplexity-lite
  fallback timed out (600 s). No deep-research file exists; the review is built
  from cached publications, UniProt and Reactome.

### Evolutionary placement

- UniProt: `PANTHER; PTHR11640:SF136; NEPHRIN`. Same subfamily holds fly Sns and
  Hbs and worm SYG-2; the Neph/Kirre partners (KIRREL1-3, fly Kirre/Rst, worm
  SYG-1) are in a different subfamily (SF31), so they are heterophilic partners,
  not orthologs.
- IBA rows (plasma membrane, cell-cell junction, cell adhesion molecule binding,
  cell-cell adhesion) derive from PAINT node PTN002267852; O60500 is itself a donor
  for plasma membrane. PAINT did NOT propagate myoblast fusion from that node even
  though fly Sns/Hbs carry it experimentally - treated as a deliberate decision.
  Human/mouse myoblast-fusion annotations here rest only on mouse Ensembl-Compara
  IEA transfer from the mouse KO study.

### Key human / mammalian experimental findings

- Positional cloning; IgSF transmembrane protein; mutated in Finnish congenital
  nephrotic syndrome [PMID:9660941 "is a 1241-residue putative transmembrane protein of the immunoglobulin"].
- Human nephrin localises to the slit diaphragm by immunogold EM
  [PMID:10393930 "at the slit between podocyte foot processes"]; NPHS1 patients
  lack SD [PMID:10393930 "characterized by massive proteinuria already in utero and lack of slit diaphragm"].
- Mouse Nphs1 KO: absent SD, foot process effacement, neonatal death
  [PMID:11136707 "effacement of podocyte foot processes and absence of the slit diaphragm,"].
- Homophilic adhesion of human nephrin ectodomain (SPR) and cell aggregation
  [PMID:14633607 "homophilic interactions that could promote cellular contacts through direct"].
- Heterophilic: human nephrin binds worm SYG-1 (Neph1 ortholog) and rescues syg-2
  mutants [PMID:21858180 "both SYG-2 and nephrin could also be shown to strongly bind to SYG-1 by co-immunoprecipitation"].
  Reactome curates NPHS1:KIRREL cis heterodimers.
- Phospho-tyrosine signalling: Src-family (Fyn) phosphorylates cytoplasmic YDxV
  motifs that recruit Nck SH2, driving actin assembly
  [PMID:16525419 "multiple YDxV sites that form preferred binding motifs for the Nck SH2 domain"];
  [PMID:16543952 "these observations establish a function for nephrin in"].
- Podocin binds the cytoplasmic tail and enhances nephrin signalling (PMID:11562357).
- Myoblast fusion (zebrafish morphants, mouse KO myoblasts in vitro):
  [PMID:19470472 "suggest that nephrin plays a role in secondary fusion of myoblasts into nascent"].
  Necessity-level evidence only; kept non-core.

### Decisions summary

- Core: SD component; homophilic/heterophilic cell adhesion molecule binding;
  slit diaphragm assembly; phospho-tyrosine scaffold (SH2 domain binding) linking
  SD to actin via Nck.
- Generic protein binding: NCK1 row -> SH2 domain binding; SYG-1 row -> cell
  adhesion molecule binding; IQGAP1 row removed as uninformative.
- GBM development (IEP, nephrin used as marker) marked over-annotated; skeletal
  muscle tissue development (organismal phenotype) over-annotated; myoblast
  fusion and synapse protein localisation (heterologous worm rescue) kept non-core.
