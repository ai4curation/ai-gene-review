# mvd (Dictyostelium discoideum) review notes

## 2026-11-18 manual review

UniProt Q54YQ9 (MVD1_DICDI), dictyBase DDB_G0278607, 391 residues, PE 3 (inferred from homology),
PANTHER PTHR10977:SF3. No deep-research provider keys are configured here; this review uses the
UniProt record, cached papers and the searches below. The searches are shared with the mvk review
(see `genes/DICDI/mvk/mvk-notes.md`).

### Literature searches (Europe PMC and web, 2026-11-18)

- `Dictyostelium AND ("mevalonate kinase" OR "diphosphomevalonate decarboxylase" OR "mevalonate
  diphosphate decarboxylase" OR "mevalonate pyrophosphate decarboxylase")`: no paper characterises
  Dictyostelium mvd.
- `Dictyostelium AND ("DDB_G0278607" OR "DDB_G0272018")`: 0 hits.
- `Dictyostelium AND cycloartenol` and related sterol queries: Nes et al. 1990 (PMID:11607106) and
  Godzina et al. 2000 (PMID:10783001).
- The 2014 Sheffield PhD thesis (Alkuwayti; open PDF on White Rose eTheses) is the only source of
  Dictyostelium localization data for this enzyme.

### Evidence

- Localization (thesis, unrefereed): the enzyme has no PTS1 or PTS2, and both C- and N-terminal GFP
  fusions are cytosolic in amoebae [thesis "In D. discoideum, diphosphomevalonate decarboxylase
  (DdDMPD) has neither a PTS1 nor a PTS2."; "When this construct was expressed in D discoideum
  amoebae, the GFP fluorescence was observed in the cytosol"]. The C-terminal tripeptide of Q54YQ9 is
  -QLN, not a PTS1. In the same work phosphomevalonate kinase, which makes the mvd substrate, is
  imported into peroxisomes by its C-terminal PTS1, and FDP synthase is peroxisomal (also published,
  PMID:22849378).
- Human MVD, donor of the UniProt ISS rows and a PAINT seed, is cytosolic [PMID:14972328 "We found
  a cytosolic localization for both endogenous human mevalonate pyrophosphate decarboxylase"].
- Sterols: Dictyostelium cyclises oxidosqualene to cycloartenol and makes dictyosterol, not
  cholesterol [PMID:11607106 "the stereochemical outcome of squalene oxide cyclization leads to the
  production of cycloartenol rather than lanosterol"]; [thesis "In D.discoideum the biosynthesis of
  dictysterol, the major sterol that is produced by growing amoebae"]. The cycloartenol synthase cDNA
  is characterised (PMID:10783001).
- So UniProt's PATHWAY line "Steroid biosynthesis; cholesterol biosynthesis" (ECO:0000305), and
  the GO:0006695 row mapped from it, transfer the human end product to an organism that does not
  make cholesterol. The Reactome cross-references on the entry (R-DDI-9969896 "Lanosterol
  biosynthesis") are likewise orthology projections from the human pathway; Dictyostelium makes
  cycloartenol, not lanosterol. There is no GO row from Reactome, so this is only noted here.

### PANTHER / PAINT

- Leaf PTN000861770 > PTN000861769 (D. discoideum and D. purpureum) > PTN000861730 (Dictyostelium
  plus the opisthokont clade PTN000104603) > PTN000104602 (all eukaryotes) > PTN000104601. No IRD or
  IKR on the lineage (`just paint-losses DICDI mvd`).

### Decisions

- Accept the GO:0004163 (IBA, IEA, ISS), GO:0019287 (IBA, IEA), cytosol (IBA, IEA, ISS) and GO:0008299
  rows.
- Cytoplasm (IEA SubCell, ISS): TOO_GENERAL, since cytoplasm does not separate cytosol from the
  peroxisomes where the neighbouring PMK and FDPS reside.
- GO:0016831 carboxy-lyase activity: TOO_GENERAL (IPR005935 also covers phosphomevalonate
  decarboxylases).
- GO:0006695 cholesterol biosynthetic process: MODIFY to GO:0016126 sterol biosynthetic process. The
  enzyme feeds the sterol pathway, but the Dictyostelium end product is dictyosterol by way of
  cycloartenol. A UniProt source defect (PATHWAY line, CHECK, PROBABLE) is recorded on the row.
