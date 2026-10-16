# sctN1 / InvC (P0A1B9, STM2894) — curation notes

Salmonella enterica serovar Typhimurium LT2, SPI-1 injectisome (T3SS-1) ATPase.
Standardized name SctN1; historical names InvC, SpaI/SpaL.

## Identity
- UniProt P0A1B9, 431 aa, `RecName: Full=SPI-1 type 3 secretion system ATPase`, EC 7.4.2.8
  (protein-translocating / protein-exporting ATPase EC), not the ATP synthase EC 7.1.2.2.
  Keywords include Translocase, Protein transport, Virulence, Cytoplasm.
- PANTHER PTHR15184:SF9 "SPI-1 TYPE 3 SECRETION SYSTEM ATPASE" (the subfamily is named for this
  protein). Domains: IPR005714 (ATPase_T3SS_FliI/YscN), IPR000194 and IPR004100
  (F1/V1/A1 alpha/beta nucleotide-binding and N-terminal domains), IPR040627 (T3SS_ATPase_C).
- Distinct from SsaN (SPI-2 ATPase, sctN2) and from the flagellar FliI.

## Enzymology and catalytic residues
- Purified InvC hydrolyses ATP; a P-loop mutation (K165E) abolishes activity and cannot
  complement an invC mutant
  [PMID:8045880 "purified preparations of InvC showed significant ATPase activity";
  "Site-directed mutagenesis of a residue essential for the catalytical function of this family
  of proteins resulted in a protein devoid of ATPase activity and unable to complement an invC
  mutant of S. typhimurium"].
- Active-site mutants G164C, R189G, R191H, R223H are catalytically dead
  [PMID:15060043 "Proteins with mutations in residues predicted to be located within the predicted
  active site (G164C, R189G, R191H, and R223H) were devoid of any detectable ATPase activity"].
- Crystal structures of InvCΔ79 apo / ATPγS / ADP show ATP-dependent remodelling of two
  pore-facing loops [PMID:31393998 "Both loops face the central pore of the predicted InvC cylinder
  and are essential for the function of the T3SS ATPase"].
- No evidence anywhere for ATP synthesis by InvC; no Fo-type membrane sector partner exists in
  the injectisome. The family ATPase activity of the flagellar paralog FliI is insensitive to
  F-, V- and P-type ATPase inhibitors [PMID:8943245 "The activity was not affected by inhibitors
  of the F-, V- or P-type ATPases"].

## Substrate handling (the actual biological work)
- InvC recognizes secretion substrates and, in an ATP-dependent manner, releases the chaperone
  and unfolds the effector [PMID:16208377 "InvC induces chaperone release from and unfolding of
  the cognate secreted protein in an ATP-dependent manner"; "has a critical function in substrate
  recognition"]. SicP–SptP was the model chaperone/effector pair.
- The hexamer's pore-lining two-helix finger and loop are required, exactly as in ATP-driven
  protein translocases/unfoldases [PMID:26170413 "a two-helix-finger motif and a conserved loop
  located at the entrance of and within the predicted pore formed by the hexameric ATPase are
  essential for InvC function"].
- Direct binding to the effector SopD [PMID:20185511 "we have identified an association between
  SopD and the SPI-1 T3S system ATPase, InvC"].

## Localization / complex
- InvC is a soluble protein that is peripherally membrane-associated through protein–protein
  contacts with the injectisome [PMID:15060043 "InvC was localized almost exclusively in the
  membrane fraction"; "characteristic of a peripherally associated membrane protein"]. It has no
  transmembrane segment.
- Oligomerizes; gel filtration gives monomer and ~290 kDa species [PMID:15060043 "These two peaks
  are consistent with the existence of a hexameric"]. Isolated InvCΔ79 is monomeric/dimeric
  [PMID:31393998 "the Salmonella T3SS ATPase InvC can form monomers and dimers in solution"],
  i.e. the N-terminal domain and the platform drive assembly.
- In situ cryo-ET places InvC in the cytoplasmic sorting platform of the SPI-1 injectisome
  [PMID:28283062 "InvC was located within the hexameric nave of the wheel with its
  carboxy-terminus facing the toroidal-shape structure formed by the cytoplasmic domain of InvA";
  "InvC affected the overall stability of the sorting platform"]. Chain:
  PrgH/basal body – OrgA – SpaO pods – OrgB (SctL) spokes – InvC (SctN) – InvI (SctO) stalk – InvA
  export gate. OrgB interaction shown genetically/biochemically [PMID:15060043 "We have shown here
  that a similar interaction occurs between InvC and the MixN homologue OrgB"].

## Phenotype
- invC mutants attach but cannot invade epithelial cells [PMID:8045880 "A mutation in invC
  rendered S. typhimurium defective in their ability to enter cultured epithelial cells"].
- Knockdown of invC mRNA reduces secretion and invasion [PMID:14762212 "expression in Salmonella
  results in invC mRNA and InvC protein depletion, decreased type III secretion and interference
  with host cell invasion"].

## The ATP-synthase annotation problem
InvC carries two IBA rows from PANTHER node PTN008558586 (GO:0046933 rotational ATP synthase
activity, contributes_to; GO:0045259 proton-transporting ATP synthase complex, part_of), plus
downstream/side IEA rows GO:0015986 (GO_REF:0000108 logical inference from GO:0046933),
GO:0046034 and GO:1902600 (InterPro2GO from IPR004100).

Node placement (from `projects/TREEGRAFTER/rotary_atpase/node_placement.tsv` and
`interpro/panther/PTHR15184/PTHR15184-paint.tsv`): PTN008558586 is a **DUPLICATION** node whose
two children are PTN000390097 (bacterial export ATPases: SF9 SPI-1 T3SS ATPase — this protein —,
SF62 SPI-2 ATPase, SF81 flagellar FliI) and PTN008558588 (the genuine F1-beta clade, SF51/74/75/76/
80/82/83/85). The IBD for GO:0046933/GO:0045259 was placed **at the duplication node**, seeded
entirely by F1-beta members (E. coli AtpD P0ABB4, human ATP5F1B P06576, yeast ATP2, S. pombe atp2,
plus plant/rat alpha/beta subunits). It therefore leaks across the paralogy boundary into the
export-ATPase clade. The correct placement of the F1 function is the F1-beta child PTN008558588.
This is an argument about node placement, not about donor counts.

Biologically: the injectisome has no Fo sector, no c-ring, no proton half-channels, and InvC is a
soluble peripheral protein with no transmembrane segment. Where proton motive force is used by a
type III system, the protons move through the membrane export gate (FlhA/InvA-type components),
not through the ATPase [PMID:21934659 "the export gate complex by itself is a proton-protein
antiporter"; PMID:18216859 "the flagellar secretion apparatus functions as a proton-driven protein
exporter"]. So GO:0046933, GO:0045259, GO:0015986 and GO:1902600 are all REMOVE for this protein;
GO:0046034 is "true but misleading" (ATP hydrolysis for export is not ATP metabolism in the GO
sense) and is marked over-annotated, consistent with the sibling FliI reviews.

## Notes on term choices
- `GO:0008564 protein-exporting ATPase activity` (IEA from EC 7.4.2.8) is the right, informative MF
  and is retained as the core function; ATP hydrolysis GO:0016887 and ATP binding GO:0005524 are
  accepted as the underlying chemistry.
- `GO:0043335 protein unfolding` was considered for the chaperone-release/unfolding activity
  (PMID:16208377) but no T3SS/flagellar export ATPase in GOA carries it (comparator check on
  SsaN/InvC/FliI entries returns none; the term's annotation set is dominated by ClpA/HslU/trigger
  factor chaperones). Raised as a suggested question instead of asserted as NEW.
- `GO:0005515 protein binding` (IPI with SopD) is uninformative on its own but is a genuine
  experimental record of effector docking; kept as non-core.
