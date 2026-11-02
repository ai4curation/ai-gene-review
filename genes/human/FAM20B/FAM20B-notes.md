# FAM20B (human, O75063) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: FAM20B is the closest experimentally characterised relative of fly
CG3631 (Q95T10). This review treats human FAM20B in its own right; no
ProtNLM2 output was opened or used.

### Data and deep research

- `just fetch-gene human FAM20B` created the UniProt, GOA (25 rows) and stub files.
- `just deep-research-falcon human FAM20B --fallback perplexity-lite` FAILED:
  Edison/falcon returned `403 Forbidden` at `/auth/login` ("Failed to authenticate"),
  and the perplexity-lite fallback also failed. No deep-research file exists.
  The review is built from the cached primary literature listed below, which I read
  directly.
- Extra PMIDs cached for this review: 24425863, 29572475, 37828045, 40422215,
  23395820, 27405802, 30847897, 33759783 (also 18400750, not used). 21901110
  (zebrafish fam20b/xylt1, Eames 2011) failed to cache and is not cited.

### Evolutionary grounding

- PANTHER 19.0 (file:interpro/panther/PTHR12450/PTHR12450-entries.csv): human
  FAM20B O75063, mouse Fam20b Q8VCS3, zebrafish fam20b Q5RH51 and fly CG3631
  Q95T10 are all in PTHR12450:SF14 GLYCOSAMINOGLYCAN XYLOSYLKINASE. FAM20C is SF11,
  FAM20A SF12, and worm famk-1 / fly CG31145 SF22.
- Zhang et al. 2018 [PMID:29572475] solved a Fam20B-like structure (hydra hmFam20)
  with Gal-Xyl bound, showed sponge/hydra single Fam20 proteins are
  Fam20B-like xylosylkinases, and that human Fam20B is a monomer whose
  Gal-Xyl-contacting residues are required for activity ("mutations of the
  equivalent residues in the human Fam20B protein significantly diminish kinase
  activity"). They also state fly has one Fam20B and one Fam20C, uncharacterised,
  while Drosophila linkage-region xylose phosphorylation has been detected
  ("this activity can probably be ascribed to Fam20B").
- IBA rows: GO:0016773 from PTN000966557 (a deep node also covering FAM20C,
  Q8IXL6) and GO:0030166 from PTN002488224 (FAM20B branch, ZFIN donor).

### Experimentally established in human (cells / recombinant human protein)

- Xylose 2-O-kinase on the GAG-protein linkage region; Golgi type II membrane
  protein [PMID:19473117].
- FAM20B knockout cells: linkage region truncated to Sia-Gal-Xyl, no elongation;
  phosphorylation increases GalT-II (B3GALT6) activity [PMID:25331875].
- Recombinant human FAM20B in a reconstituted one-pot linker system with XT1,
  B4GALT7, B3GALT6 and B3GAT3; phosphorylation accelerates linker synthesis and
  HS/CS initiation but not polymerisation [PMID:37828045].
- Phosphate is transient: PXYLP1 (XYLP) removes it from the trisaccharide; the
  phosphorylated tetrasaccharide is not polymerised; EXTL2 caps it with GlcNAc
  and terminates chains [PMID:24425863, PMID:23395820].
- Both overexpression and loss reduce GAG output in U251/glioblastoma cells,
  depending on D289/D309 [PMID:40422215], whereas overexpression raised CS/HS in
  HeLa [PMID:19473117]. Its physiological role is as a biosynthetic enzyme whose
  phosphate must later be removed by PXYLP1. It is not a negative regulator.
- Human genetics: biallelic truncating variants cause a lethal neonatal short-limb
  dysplasia [PMID:30847897] (phenotype only; not annotated).

### Decisions

- Protein binding (11 IPI rows): REMOVE. Decorin is a substrate (kinase assay in
  PMID:25789606, Fig 4C); the rest are HuRI/BioPlex/cell-map screens.
- GO:0016773: ACCEPT (all three rows). GO has no term for this specific reaction
  (RHEA:19461), so I proposed a new term. GO:0019200 carbohydrate kinase activity
  is not an is_a descendant of GO:0016773, and I did not add it.
- GO:0030166 IBA: MODIFY → GO:0120532 glycosaminoglycan-protein linkage region
  biosynthetic process (part_of CS/HS/DS proteoglycan biosynthesis). FAM20B
  catalyses a covalent step on the linker intermediate, so it passes the
  participation test. Comparators on this term are XYLT1/2, B4GALT7 and B3GALT6.
- GO:1902729 (Reactome TAS): REMOVE. Loss of function abolishes linker
  elongation and reduces GAGs; the Reactome summary's "making the chain
  unavailable" describes a transient intermediate that is relieved by PXYLP1.
- Localisation: Golgi membrane / Golgi apparatus ACCEPT; cytoplasm IEA TOO_GENERAL.
- No developmental phenotypes annotated (mouse tooth number, cleft palate,
  chondrosarcoma, zebrafish skeleton): these are downstream of GAG loss.

### For transfer to CG3631 (SF14)

Transferable at SF14 level: the xylose 2-O-kinase activity (GO:0016773) and the
linkage-region/proteoglycan biosynthesis role. These rest on human, sponge and
hydra biochemistry. PMID:29572475 reports that the Gal-Xyl recognition residues
are conserved across Fam20B proteins; I have not checked these residues in CG3631
myself. Do not
transfer: the human-specific disease phenotype, the vertebrate PXYLP1/EXTL2
quality-control circuitry (not established in fly), or any FAM20C-type protein
kinase activity (SF11).
