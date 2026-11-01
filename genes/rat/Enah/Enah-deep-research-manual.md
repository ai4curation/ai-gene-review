# Enah (rat) - manual literature research

No deep-research API was available for this session; this summary was written by the
reviewer from cached publications (publications/PMID_*.md) and PubMed searches. Rat-specific
experimental literature on Enah/Mena is sparse, so most functional knowledge is from mouse
Mena (MGI:108360, UniProtKB:Q03173), human ENAH (UniProtKB:Q8N8S7) and the Ena/VASP family.

## Entry identity

- UniProtKB A0A8I6GMP8 (TrEMBL, 807 aa, Ensembl ENSRNOP00000097849), gene Enah, RGD:1307666.
  This is the entry to which GOA keys all 37 rat Enah annotations. A second TrEMBL entry for
  the same gene, A0A0G2K6I4 (563 aa, also RGD:1307666, GeneID 360891), carries only a
  handful of IEA rows.
- Domain architecture: N-terminal WH1/EVH1 domain (residues 1-111, PROSITE PS50229), a
  long LERER-repeat/proline-rich central region, and a C-terminal EVH2 region with the
  VASP tetramerisation coiled coil (Pfam PF08776, residues 772-799 coiled coil).

## Molecular function

- EVH1 binds FPPPP-type proline-rich motifs; the central proline-rich region binds profilin,
  SH3 and WW domains [PMID:8861907 "A conserved domain targets Mena to localized proteins
  containing a specific proline-rich motif"]; [PMID:10069337 "Mena binds directly to
  Profilin, an actin-binding protein that modulates actin polymerization"].
- WW domain ligand: FE65 WW domain binds PPLP motifs in Mena [PMID:9407065 "we identified
  the sequences in Mena that interact with the FE65 WW domain and found that they contain the
  signature proline-proline-leucine-proline motif"]; structural basis [PMID:17686488].
- SH3 ligand: IRSp53 (BAIAP2) SH3 domain binds Mena [PMID:11696321 "we have identified
  Mena, an Ena/VASP family member, as interacting with the SH3 domain of IRSp53"].
- Ena/VASP proteins bind actin filament barbed ends, antagonise capping protein and act as
  processive filament elongators [PMID:12086607 "In vitro, Ena/VASP promoted actin filament
  elongation by interacting with barbed ends, shielding them from capping protein"];
  [PMID:14570581 "these proteins associate with barbed ends of actin filaments and
  antagonize filament capping by capping protein (CapZ)"]; mechanism characterised with
  VASP [PMID:21217643].
- EVH1 binding partners include Abi-1 [PMID:12672821], Fat1 [PMID:15148305], and the LIM3
  domain of Tes [PMID:21278383].

## Localization

- Focal adhesions, lamellipodial edges and filopodial tips [PMID:15371503 "Ena/VASP proteins
  localize to focal adhesions and areas requiring dynamic remodeling of the actin
  cytoskeleton, including lamellipodial protrusions and filopodial tips"]; growth cone
  filopodia tips in neurons [PMID:10069337 "In primary neurons, Mena is concentrated at the
  tips of growth cone filopodia"].
- Rat-relevant: in hippocampal neurons Mena relocates to actin patches and binds gephyrin
  [PMID:16376568, abstract only] (source of the SynGO IDA rows).
- Rat testis: Tes immunoprecipitates Arp7A and Mena from rat testis extracts; Mena is in the
  subacrosomal layer (acroplaxome) of round spermatids [PMID:21278383 "immunoblot analysis of
  Tes immunoprecipitations (IP) with the indicated antibodies reveals that Arp7A, Tes, and
  Mena are complexed to each other in rat testes extracts"].

## Biological processes

- Filopodia formation and actin network geometry: [PMID:15066263] (neurons, downstream of
  netrin-1), [PMID:11696321] (with IRSp53 downstream of Cdc42), [PMID:12086607] (lamellipodia).
- Axon guidance / commissure formation and neurulation in mouse genetics: [PMID:10069337
  "failed decussation of the corpus callosum"; Mena/Profilin I compound mutants show
  "defects in neurulation"]; Mena/VASP double mutants [PMID:15371503 "display defects in
  neurulation, craniofacial structures, and the formation of several fiber tracts"].
  These are phenotypes of loss of a cytoskeletal regulator, i.e. upstream/necessity evidence.
- Listeria actin-based motility [PMID:8861907].
