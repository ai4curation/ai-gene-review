# ced-2 (C. elegans, UniProtKB:Q9NHC3) curation notes

Manual synthesis written during the GO annotation review. Automated deep-research
providers were unavailable for this session, so there is no `ced-2-deep-research-*.md`
file. All statements below come from cached publications in `publications/` and the
UniProt record (`ced-2-uniprot.txt`).

## Identity and domains

- CrkII orthologue: an N-terminal SH2 domain and two SH3 domains, with no catalytic domain
  (UniProt; Pfam SH2, SH3_1, SH3_2; PANTHER PTHR19969:SF5 "CRK-like protein").
- [PMID:10707082 "ced-2 and ced-10 encode proteins similar to the human adaptor protein CrkII and the human GTPase Rac"]

## Pathway placement

- One of two partially redundant engulfment pathways, ced-2/ced-5/ced-10(/ced-12)
  [PMID:10707082 "Engulfment of apoptotic cells in Caenorhabditis elegans is controlled by two partially redundant pathways"].
- Acts in the engulfing cell [PMID:10707082 "CED-2 and CED-10 function in engulfing rather than dying cells to control the phagocytosis of cell corpses"].
- Binds CED-5 and forms a ternary complex with CED-5 and CED-12
  [PMID:10707082 "CED-2 and CED-5 physically interact"];
  [PMID:11703940 "CED-12 physically interacts with CED-5 and forms a ternary complex with CED-2 in vitro"].
- Crystal structure: the PXXP-binding surface of CED-2 (F125G) is dispensable for rescue; CED-2
  binds the N-terminal region of CED-5 instead
  [PMID:21616056 "A CED-2 point mutation (F125G) disrupting its interaction with the PXXP motif of CED-5 did not affect its rescuing activity"]
  (abstract-only).
- Upstream inputs:
  - PSR-1: endogenous CED-2 co-precipitates with Flag-PSR-1 [PMID:25564762 "co-precipitated the endogenous CED-2 protein"]; psr-1 acts in the ced-2 pathway for apoptotic germ cells and necrotic cells [PMID:25564762 "psr-1 acts in the ced-2 phagocytosis pathway to promote clearance of necrotic cells"].
  - MOM-5/Frizzled with GSK-3 and APR-1/APC [PMID:20126385 "Apoptotic cell clearance and migration of the distal tip cell require the MOM-5/Fz receptor, GSK-3 kinase, and APC/APR-1, which activate the CED-2/5/12 branch of the engulfment machinery"]. APR-1 binds the CED-2 SH2 domain in a phospho-dependent yeast two-hybrid assay, but not detected in vivo [PMID:20126385 "Despite extensive proteomics efforts, we were unable to identify any interaction between CED-2 and APR-1 in vivo"].
  - SRC-1 (UniProt SUBUNIT, PMID:20226672; not cached, not used as evidence here).
- ABL-1 inhibits engulfment partly independently of CED-2 [PMID:19402756 "the effect of ABL-1 on engulfment is at least partially independent of CED-2"].

## Phenotypes

- Persistent unengulfed corpses; the cells still die
  [PMID:6857247 "Mutations in two nonessential genes specifically block the phagocytosis of cells programmed to die during development"]
  (the two genes are ced-1 and ced-2).
- Distal tip cell migration defects [PMID:10707082 "result in defects both in the engulfment of dying cells and in the migrations of the two distal tip cells of the developing gonad"];
  [PMID:19402756 "As with ced-2, ced-5, and ced-12 null mutants, the DTC defect of these ced-10 null mutants was suppressed"].
- Engulfment genes promote death of weakly signalled cells
  [PMID:11449278 "mutations in engulfment genes enhance the frequency of this cell survival"];
  [PMID:11449279 "genes that mediate corpse removal can also function to actively kill cells"].
  Both cached records are abstract-only; Reddien's abstract lists ced-2 among the engulfment
  genes but neither abstract names which mutants were tested for the killing defect.

## Curation decisions (summary)

- Bare protein binding (4 partners: CED-5 x3 rows, APR-1, PSR-1): MODIFY to signaling adaptor
  activity (CED-5, PSR-1) or phosphotyrosine residue binding (APR-1, SH2-dependent Y2H).
- GO:1902742 (CED-8 paper, PMID:24225442): ced-2(n1994) is used only in engulfment
  double-mutant assays. MODIFY to GO:1904747, citing Reddien/Hoeppner, with the caveat above.
- GO:1901076 and GO:1903356 (Cabello 2010): unlike CED-1/6/7, the CED-2/5/12 branch is the route
  through which MOM-5 acts for engulfment and DTC migration. CED-2 is core machinery, not a
  regulator, so MODIFY to GO:0043652 and GO:0097628 (distal tip cell migration). Note: no ced-2 allele
  appears in that paper's strain list; ced-2 is mostly referenced as a comparison phenotype.
- Programmed cell death / apoptotic process IMP (persistent-corpse phenotype): MARK_AS_OVER_ANNOTATED.
- Signal transduction IMP: MODIFY to Rac protein signal transduction (GO:0016601).
- IBA RTK binding and enzyme-linked receptor signaling: KEEP_AS_NON_CORE (inherited SH2 adaptor
  capacity; no worm RTK partner shown).
- ced-2 itself (WBGene00000416) appears in the cell migration IBA WITH/FROM; this is expected and not circular.
