# PDHX (human, O00330) review notes

## Deep research status
`just deep-research-falcon human PDHX` FAILED in this worktree: the wrapper
`scripts/deep_research_wrapper.py` hits a runtime `TypeError: unsupported operand
type(s) for |: 'type' and 'NoneType'` at line ~158 (a `dict | None` default
annotation evaluated at runtime under an incompatible interpreter). No
`-deep-research-falcon.md` was produced. Per project policy I did NOT fabricate a
`-deep-research-*.md`. This review is grounded in the UniProt record
(PDHX-uniprot.txt), the seeded GOA, cached publications/PMID_*.md, and the
disorder KB `~/repos/dismech/kb/disorders/Pyruvate_Dehydrogenase_Deficiency.yaml`.

## Core biology
PDHX = "component X" / E3-binding protein (E3BP). A **structural, non-catalytic**
subunit of the mitochondrial pyruvate dehydrogenase complex (PDC). Built into the
E2 (DLAT) dodecahedral inner core; its established function is to **bind and anchor
the E3 dihydrolipoyl dehydrogenase (DLD)** to the E2 core, positioning E3 to
reoxidise the lipoyl arms. Segmented multidomain architecture like E2: N-terminal
lipoyl(-binding) domain (lipoylated at K97), a peripheral subunit-binding domain
(PSBD; the E3-binding domain, residues ~183-220), and a C-terminal E2-like inner
core (I') domain that packs into the E2 60-mer core.

### Key evidence
- [PMID:9242632 "Protein X, recently renamed dihydrolipoamide dehydrogenase-binding
  protein (E3BP), is required for anchoring dihydrolipoamide dehydrogenase (E3) to
  the dihydrolipoamide transacetylase (E2) core of the pyruvate dehydrogenase
  complexes of eukaryotes."]
- **NOT a functional acetyltransferase**: [PMID:9242632 "the putative catalytic
  site histidine residue present in the inner core domains of all dihydrolipoamide
  acyltransferases is replaced by a serine residue in human E3BP; thus, catalysis
  of coenzyme A acetylation by this protein is unlikely."] => GO:0004742
  (dihydrolipoyllysine-residue acetyltransferase activity) and GO:0016746
  (acyltransferase activity) are homology/family over-annotations. The catalytic
  His is absent -> MARK_AS_OVER_ANNOTATED (not REMOVE for the IDA; keep as
  over-annotated). The IEA family maps => REMOVE-worthy in principle, but per
  policy for IEA I mark over-annotated / modify to the structural role; I use
  MARK_AS_OVER_ANNOTATED for the catalytic MF terms because they are family-fold
  correct but not the true function.
- Structural core: [PMID:16263718 "The dihydrolipoamide dehydrogenase-binding
  protein (E3BP) and the dihydrolipoamide acetyltransferase (E2) component enzyme
  form the structural core of the human pyruvate dehydrogenase complex by providing
  the binding sites for two other component proteins, dihydrolipoamide dehydrogenase
  (E3) and pyruvate dehydrogenase (E1)"]
- Tethers E3: [PMID:19240034 "a noncatalytic component, E3-binding protein (E3BP),
  which specifically tethers E3 dimers to the PDC."] — this is the strongest single
  statement: E3BP is explicitly "noncatalytic".
- E3-binding domain / DLD interaction, mutagenesis hot spot: [PMID:16442803
  "utilizes the specific dihydrolipoamide dehydrogenase (E3) binding protein (E3BP)
  to tether the essential E3 component to the 60-meric core of the complex"].
- Core stoichiometry ~48 E2 + 12 E3BP (or 40/20 reconstituted model): PMID:14638692,
  PMID:19240034, PMID:20361979 (uncached), UniProt SUBUNIT.
- PDHX is a "structural subunit": [PMID:25525879 "a structural subunit (PDH-binding
  component X, PDHX)"].
- PDHX is lipoylated at K97 and is a SIRT4 lipoamidase substrate: [PMID:25525879
  "42% for PDHX"] (SIRT4 removes lipoyl from PDHX peptide); UniProt MOD_RES 97
  N6-lipoyllysine; PTM "Delipoylated at Lys-97 by SIRT4".

### Interactions (IPI GO:0005515 protein binding)
- Biologically meaningful: DLD/E3 (P09622) — the anchoring partner; SIRT4 (Q9Y6E7)
  — lipoamidase regulator. These are the real functional interactions but bare
  "protein binding" is uninformative; per curation policy avoid bare protein binding
  and prefer a specific MF. Mark the DLD-supported ones as over-annotated (the
  specific "E3 anchoring" role is captured better by core_functions / structural
  constituent term).
- High-throughput screen hits with no established biological role for PDHX:
  AGTRAP (Q6RW13; PMID:21516116, PMID:25416956, PMID:31515488), CIDEB (Q9UHD4;
  PMID:32296183). These are proteome-scale Y2H / AP-MS maps (PMID:28514442,
  PMID:32296183, PMID:33961781). MARK_AS_OVER_ANNOTATED per policy (not REMOVE for
  IPI experimental).

### Localization
Mitochondrial matrix (UniProt SUBCELLULAR LOCATION: Mitochondrion matrix; TRANSIT
1..53). GO:0005739 mitochondrion (IBA/NAS/IDA/HTP) and GO:0005759 mitochondrial
matrix (IEA/TAS) all correct. Matrix is more specific and accurate.

### Disease
Pyruvate dehydrogenase E3-binding protein deficiency (PDHXD, MIM:245349;
MONDO:0009503; ORPHA:255182): PDC deficiency with normal E1/E2/E3 activities,
congenital lactic acidosis, hypotonia, psychomotor retardation. Disease gene per
Orphanet [ORPHA:255182 "PDHX | pyruvate dehydrogenase complex component X |
hgnc:21350 | Disease-causing germline mutation(s) in"].

## Annotation decisions summary
- GO:0045254 pyruvate dehydrogenase complex (part_of) — ACCEPT (all copies). Core.
- GO:0005759 mitochondrial matrix (located_in) — ACCEPT (most specific CC).
- GO:0005739 mitochondrion — ACCEPT (correct, less specific than matrix); keep.
- GO:0006086 pyruvate decarboxylation to acetyl-CoA — ACCEPT as involved_in/BP
  (PDHX is a required structural subunit of the complex that performs this; IC/IDA
  reasonable). The IEA involved_in and the ComplexPortal IDA are fine.
- GO:0004742 acetyltransferase activity (IDA MGI + IEA ARBA) — MARK_AS_OVER_ANNOTATED:
  catalytic His->Ser, catalysis unlikely (PMID:9242632); E3BP is noncatalytic
  (PMID:19240034). The IDA is likely a legacy family/reconstitution annotation.
- GO:0016746 acyltransferase activity (IEA InterPro) — MARK_AS_OVER_ANNOTATED (same
  reason; broad family term, no catalysis).
- GO:0005515 protein binding (IPI x many) — MARK_AS_OVER_ANNOTATED (bare, uninformative;
  the meaningful DLD/SIRT4 interactions are better captured by structural role).

## Core function (MF/role)
Best MF/role term: PDHX acts as a structural constituent that anchors E3(DLD) to the
E2 core. Candidate GO terms:
- GO:0098918 structural constituent of synapse — NO (wrong).
- GO:0005198 structural molecule activity — generic MF, defensible for a scaffold
  subunit; check branch.
- "protein-macromolecule adaptor activity" GO:0030674 — anchoring/adaptor MF for
  tethering E3 to E2; strong candidate for the "anchor E3 to E2" function.
Will use GO:0030674 (protein-macromolecule adaptor activity) as the MF capturing the
E3-anchoring/scaffold role, plus in_complex GO:0045254, locations GO:0005759.
Verify labels via OLS before finalizing.
