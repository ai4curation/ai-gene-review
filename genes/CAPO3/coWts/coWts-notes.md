# coWts (Capsaspora owczarzaki Warts/LATS ortholog) - curation notes

**Automated deep research was unavailable** (no deep-research provider key in this
environment). These notes are built manually from the cached full-text papers in
`publications/` and from database lookups (UniProt, NCBI, InterPro, PANTHER, QuickGO)
made on 2026-10-01. No `-deep-research-*.md` file exists for this gene.

## Identity

- UniProt A0A0D2VGR4 (TrEMBL, unreviewed), 1205 aa; UniProt ORF name CAOG_000619;
  EMBL KJE89067.1; RefSeq XP_004365490.1.
- Phillips & Pan 2024 name the targeted gene "coWts" with locus CAOG_00619
  [PMID:38517944 "Oligos oJP203 and oJP204 were used to generate gene-targeting constructs for the coWts gene (CAOG_00619)."].
- Mapping check (NCBI efetch, 2026-10-01): RefSeq XP_004365490.1 has
  `/locus_tag="CAOG_00619"` and `/product="serine/threonine protein kinase lats"`;
  the EMBL protein KJE89067.1 has `/locus_tag="CAOG_000619"` and
  `/product="AGC/NDR/LATS protein kinase"`. UniProt A0A0D2VGR4 cross-references both,
  so CAOG_00619 (old 5-digit tag) = CAOG_000619 (new tag) = A0A0D2VGR4.

## Domain architecture (UniProt / InterPro)

- Long N-terminal region (~1-640) that is largely disordered/low complexity.
- CDD cd21774 "Mob-binding domain found in the large tumor suppressor (LATS)
  subfamily" at 646-706 (InterPro API) - the MOB-binding (NTR) region typical of
  NDR/LATS kinases.
- Protein kinase domain 711-1045 (PROSITE PS50011) with ATP-binding Lys 740 and
  catalytic proton acceptor Asp 834 (PROSITE rules); AGC-kinase C-terminal domain
  1046-1119; predicted hydrophobic-motif phosphothreonine at 1108.
- UniProt CAUTION: "Lacks conserved residue(s) required for the propagation of
  feature annotation" (PRU00618, AGC C-terminal rule) - this is about feature
  propagation, not loss of the catalytic residues, which are annotated as present.
- FunFam 3.30.200.20:FF:000391 "Large tumor suppressor kinase 1".
- Overall architecture (C-terminal kinase preceded by MOB-binding region) matches
  Warts/LATS, not the Rho-effector kinases (ROCK/MRCK/citron have N-terminal kinase
  domains followed by coiled-coil, CRIB/PH/CNH regions).

## PANTHER placement - a Track C observation

- PANTHER/TreeGrafter places A0A0D2VGR4 in **PTHR22988:SF71 "CITRON RHO-INTERACTING
  KINASE"**, family PTHR22988 "MYOTONIC DYSTROPHY S/T KINASE-RELATED" (InterPro
  IPR050839 "Rho-associated Serine/Threonine Kinase"), E=9.6e-122 over 693-1110.
- The human members of PTHR22988 in the PANTHER 19 tree (treeinfo API, human filter)
  are MRCK alpha/beta/gamma, ROCK1/2 and CIT - Rho effector kinases. Human LATS1
  (O95835) and LATS2 (Q9NRM7) are instead in PTHR24356 (SF138 and SF149).
- Drosophila Warts (Q9VA38) is also classified into PTHR22988 (SF76) by current
  InterPro/UniProt - so the Warts/LATS clade is split across the two PANTHER families.
- GOA's PAINT IBAs for LATS1/LATS2/wts come from **PTN002390470** (hippo signaling,
  G1/S transition, etc.), a LATS node. coWts did not receive any of those; instead its
  TreeGrafter node is **PTN001122925**, which (QuickGO with/from search, 2012
  annotations) propagates protein serine/threonine kinase activity, cytoplasm,
  cytoskeleton and actomyosin structure organization to many fungal and other
  non-model proteins, with no model-organism (human, fly, mouse, yeasts) members.
  The actomyosin/cytoskeleton terms are characteristic of the ROCK/MRCK/citron
  family, so on coWts they are a product of the family-boundary placement rather than
  of anything known about Warts/LATS.

## Experimental findings (Phillips & Pan 2024, eLife)

- Knockout: both alleles had the kinase domain replaced by selectable markers
  [PMID:38517944 "For each gene, homologous recombination was used to replace the kinase domain of both WT alleles with selectable markers"].
- coYki localization: WT mScarlet-coYki is mostly cytoplasmic; coWts-/- cells show
  nuclear >= cytoplasmic signal
  [PMID:38517944 "In contrast, the majority of coHpo-/- and coWts-/- cells showed nuclear levels of mScarlet-coYki greater than or equal to that seen in the cytoplasm (Figure 1C and D)."].
  coWts-/- has a stronger effect than coHpo-/-
  [PMID:38517944 "Interestingly, we found that coWts-/- cells were significantly more likely to show nuclear mScarlet-coYki localization than coHpo-/- cells (Figure 1D)"].
  Authors' conclusion: [PMID:38517944 "Together, these results show that the Capsaspora Hippo kinase cascade regulates coYki by cytoplasmic sequestration, indicating a premetazoan origin of this regulatory activity of the Hippo pathway."]
- **Not measured**: coWts kinase activity, coYki phosphorylation (no phospho-specific
  blots or Phos-tag), direct coWts-coYki interaction, coHpo -> coWts phosphorylation,
  or coWts subcellular localization. Mechanism is inferred from the 4SA mutant: coYki
  with the four predicted Wts/LATS sites mutated is nuclear
  [PMID:35659869 "In contrast, the majority of cells transfected with mScarlet-coYki 4SA showed uniform mScarlet signal throughout the cell or enriched mScarlet signal in the nucleus (Figure 5C and F)."].
- Proliferation: not increased; slower in shaking culture
  [PMID:38517944 "this result suggests that coWts is not a negative regulator of cell proliferation as in Drosophila and mammals, but instead is required for normal cell viability under some growth conditions"].
- Cell shape: subpopulation of elongated, contractile cells, rescued by coWts transgene
  [PMID:38517944 "The presence of elongated cells was rescued by transgenic expression of coHpo or coWts in the respective mutant (Figure 3A and B), demonstrating that the elongated cell phenotype was specifically due to the absence of these kinases."].
- Actomyosin analysis (Lifeact F-actin fibre, blebbistatin, LatB) was done in the
  coHpo mutant and WT, not in coWts
  [PMID:38517944 "As contractile cells in the coHpo mutant background tended to show a more elongated morphology than the coWts mutant, we focused on the coHpo mutant for further analysis."].
  Myosin's role remains unclear
  [PMID:38517944 "Thus the specific role of myosin activity in the phenotypes observed in Hippo pathway mutants in Capsaspora remains unclear."].
- Aggregates: coWts-/- aggregates are less circular, more densely packed, and coWts-/-
  cells have shorter filopodia within aggregates
  [PMID:38517944 "However, coWts -/- aggregates, while similar in size to WT, showed reduced circularity."]
  [PMID:38517944 "Whereas the number of cells per unit area in coYki -/- aggregates was not significantly different from WT, the number of cells per area in coHpo -/- and coWts -/- was significantly increased relative to WT (Figure 5E)."].
- Phenotypes are phenocopied by hyperactive coYki 4SA and require coYki's TEAD-binding
  residue, i.e. they run through coYki transcription
  [PMID:38517944 "These results suggest that the phenotypes observed in coHpo and coWts mutants are due to coYki activation resulting from a loss of upstream kinase signaling."]
  [PMID:38517944 "This result indicates that these phenotypes are mediated by the transcriptional activity of coYki."].
  Epistasis could not be tested
  [PMID:38517944 "Since techniques are currently unavailable to create double mutants in Capsaspora, we could not test this possibility through classic genetic epistasis."].
- RNA-seq: 609 genes differentially expressed in coWts-/-; shared set with coHpo/coYki
  [PMID:38517944 "This result indicates that coYki, coHpo, and coWts regulate a shared set of genes, a subset of which may affect the cytoskeletal properties of cells through actin regulation."].

## Earlier work

- Sebé-Pedrós et al. 2012 tested Capsaspora Yki, Sd and Hpo in Drosophila; coWts was
  aligned but not functionally tested (no "Co-Wts" experiment in the full text)
  [PMID:22832104 "To test the functional relevance of our evolutionary analysis, we assayed the activities of Capsaspora owczarzaki (Co) Hippo pathway components in Drosophila (see Supplemental Information for sequence alignment of Yki, Sd, Hpo, Wts and Mats homologues among Capsaspora, Drosophila and humans)."].
  Co-Hpo phosphorylated Drosophila Wts in S2R+ cells, i.e. Co-Hpo can act on a Wts
  substrate, but this used Dm-Wts.
- Review (Phillips 2024 TIBS) summarises the coWts knockout
  [PMID:38729842 "Consistent with this result, targeted deletion of either Capsaspora Hippo (coHpo) or Capsaspora Warts (coWts) does not increase cell proliferation, but greatly increases the rate of occurrence of an actomyosin-mediated contractile behavior displayed by cells [66] (Figure 3A)."].

## Annotation judgements (summary)

- Kinase MF terms: accept on domain grounds (intact Lys/Asp), activity not measured.
- GO:1900181 negative regulation of protein localization to nucleus: accept the IEA;
  the knockout gives IMP-grade support (coYki is the protein whose nuclear
  localization increases). A separate NEW IMP row was tried but the validator rejects
  NEW for a term already in GOA, so the evidence is recorded in the IEA row's review.
- GO:0035329 hippo signaling: NEW IMP. Warts is a core kinase of the cascade (it does
  a step of the pathway rather than being regulated by it); comparator: Drosophila wts
  and human LATS1/2 carry it (IDA/IGI/IBA). Readout (coYki cytoplasmic retention) was
  shown genetically; phosphorylation steps were not.
- Cytoskeleton / actomyosin structure organization / cytoskeleton organization: these
  are not supported for coWts itself; phenotypes run through coYki-dependent
  transcription, and the source node is a ROCK/citron-family PANTHER placement.
- No NEW term for cell shape, aggregate cell density, or proliferation: these are
  downstream, transcription-mediated effects (participation test fails), and no GO term
  exists for "cell packing density within aggregates".
