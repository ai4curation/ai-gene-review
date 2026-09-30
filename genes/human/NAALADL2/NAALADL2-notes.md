# NAALADL2 (human) — review notes

UniProt: Q58DX5 (NADL2_HUMAN), HGNC:23219. "Inactive N-acetylated-alpha-linked acidic
dipeptidase-like protein 2". M28 peptidase family, M28B subfamily; PANTHER PTHR10404:SF32.
MEROPS classifies it as a non-peptidase homolog (M28.975).

## 2026-09-04 — finishing pass (PAINT no-IBA project)

Deep quality pass over the draft review; validated to zero warnings and promoted to
COMPLETE. The draft's three annotation calls (ACCEPT membrane IEA; MARK_AS_OVER_ANNOTATED
for HuRI protein binding and for the HPA nucleoplasm IDA) were all retained — each held up
under scrutiny — but were strengthened as below.

### Changes made

- **Named the interaction partners in the IPI review.** The five GOA `protein binding`
  rows correspond to IntAct/HuRI partners GPR25 (O00155), GRM2 (Q14416), LAPTM4B
  (Q86VI4), SLC30A3 (Q99726) and ITM2B (Q9Y287) [file:NAALADL2-uniprot.txt "Q58DX5;
  O00155: GPR25; NbExp=3"]. All five are integral membrane proteins detected by yeast
  two-hybrid — a system with known limitations for transmembrane baits — and none has a
  functional connection to NAALADL2. This materially supports the over-annotation call.
- **Anchored the pseudoenzyme claim to UniProt's CAUTION.** Added the explicit CAUTION
  quote [file:NAALADL2-uniprot.txt "conserved zinc-binding and active sites and therefore
  has probably lost"] to the reference findings and core_functions support, alongside the
  weaker FUNCTION line ("May be catalytically inactive").
- **Added the foundational gene paper** PMID:15168106 (Tonkin et al. 2004, Hum Genet;
  fetched full text) as a reference: 1.37 Mb gene at 3q26.3 severed by a CdLS-associated
  translocation, no CdLS point mutations found ["Mutation screening of NAALADL2 in a panel
  of CdLS patient DNA samples failed to identify patient-specific mutations"]; homology to
  NAALADase/GCPII and transferrin receptors is low (25–27% identity); expression strongest
  in kidney and placenta ["strongest expression in kidney and placenta; embryonic
  expression was largely confined to duodenal and stomach endoderm, mesonephros,
  metanephros and pancreas"]. Description expanded accordingly.

### Independent residue check of the pseudoenzyme claim (recorded in the family review)

Pairwise alignment (BLOSUM62, global and local agree) of Q58DX5 against GCPII/FOLH1
(Q04609, the family's best-characterized enzyme) shows the M28 catalytic core is
degenerate in NAALADL2. Most decisively, GCPII's catalytic-glutamate motif
`FASW-DAEE` (E424 = proton-shuttle/nucleophile-activating Glu, ACT_SITE in UniProt;
E425 = zinc ligand) aligns to NAALADL2 `FCSW-GGTA` — the Glu pair is T499/A500, i.e.
lost. Active human paralog NAALAD2 (Q9Y3Q0) retains E414/E415 at the homologous
positions (positive control); non-peptidase TFRC (P02786) has G456/D457 (negative
control). Zinc-ligand positions D453 and H553 are also substituted (H528, and no
confidently alignable residue, respectively); H377 is retained (H452) and D387 is
conservatively substituted (E462). This corroborates UniProt's CAUTION and is captured
as a machine-checked `residue_sites` entry (`gcpii_catalytic_glu_pair`) in
`interpro/panther/PTHR10404/PTHR10404-review.yaml`.

### Why NAALADL2 receives no IBA (family-level finding)

From the PANTHER 19 tree (live treeinfo service) human NAALADL2 descends from
PTN000044792, the Eukaryota-root node where PAINT (snapshot 2025-09-02) asserts an IBD
for GO:0004180 carboxypeptidase activity — so mechanically it *would* receive that IBA.
It has none (PAN-GO: "0 GO annotations based on evolutionary models" per the UniProt
entry), and the cached paint.tsv contains an explicit IRD/NOT only for the transferrin
receptor clade (PTN008499203). The most parsimonious reading is that the NAALADL2 clade
(PTN002572070, Euteleostomi, 19/19 leaves NAALADL2) is silently tree-pruned in PAINT —
correct biology, but an explicit IRD (as for the TfR clade) would be more robust and
auditable. Recommended in the family review. GOA is thus currently *clean* of the
pseudoenzyme over-annotation risk for this gene; the review guards against its
introduction.

### Open questions (unchanged)

- True topology/localization: predicted type II membrane protein vs HPA nucleoplasm
  staining — unresolved; treat HPA signal as provisional.
- Any non-catalytic (substrate-binding, adhesion, scaffold) role of the pseudo-peptidase
  ectodomain, by analogy to transferrin receptors, which repurposed the same fold for
  ligand binding.
