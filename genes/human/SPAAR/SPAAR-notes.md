# SPAAR (LINC00961-encoded microprotein) — review notes

## 2026-09-30 — initial review (claude-code)

### Identity
- UniProt A0A1B0GVQ0 (SPAR_HUMAN), 90 aa canonical (isoform 1); isoform 2 lacks residues
  1-15 (alternative initiation, VSP_058780). HGNC:27244; synonyms LINC00961, SPAR.
  Mouse ortholog UniProt A0A1B0GSZ0.
- Topology (UniProt, from PMID:28024296): lumenal N-terminus (1-18), single TM helix
  (19-39), cytoplasmic C-terminus (40-90). Pfam PF22004 / InterPro IPR054161 (SPAR);
  no other domains, no catalytic motif.
- UniProt FUNCTION is annotated to **isoform 2** (the short, human/mouse-conserved form).
  Lee et al. 2021: "Two isoforms of the SPAAR protein have been experimentally
  characterized: a short form present in human and mouse, and a long form present in
  human but not in mouse" [PMID:34946813]. The 5' elongated long form arose de novo in
  primates [PMID:34946813 "In primates, we infer two independent evolutionary events
  leading to the de novo origination of 5' elongated isoforms of SPAAR from a noncoding
  sequence"]. GOA rows are on the canonical accession without isoform qualifiers.

### Primary evidence: Matsumoto et al. 2017 Nature (PMID:28024296; cached abstract only)
- Localisation + v-ATPase interaction: [PMID:28024296 "is localized to the late
  endosome/lysosome and interacts with the lysosomal v-ATPase to negatively regulate
  mTORC1 activation"].
- Specificity for amino-acid input: [PMID:28024296 "This regulation of mTORC1 is specific
  to activation of mTORC1 by amino acid stimulation, rather than by growth factors"].
- Peptide-specific KO mouse (lncRNA preserved): [PMID:28024296 "use CRISPR/Cas9
  engineering to develop a SPAR-polypeptide-specific knockout mouse while maintaining
  expression of the host lncRNA"]; muscle regeneration: [PMID:28024296 "SPAR
  downregulation enables efficient activation of mTORC1 and promotes muscle
  regeneration"].
- UniProt summary of the full-text mechanism: SPAAR interacts with ATP6V0A1 and ATP6V0A2
  and "acts by promoting the formation of a tightly bound supercomplex composed of the
  lysosomal V-ATPase, Ragulator and Rag GTPases, preventing recruitment of mTORC1"
  (UniProt CC FUNCTION, ECO:0000269|PubMed:28024296). I could not read the full text; this
  mechanistic detail is taken from UniProt's curated record.
- Commentaries: Tajbakhsh 2017 [PMID:28388426 "LINC00961 generates SPAR polypeptide that
  acts via the lysosome to suppress amino-acid-mediated mTORC1 activity"]; Matsumoto et
  al. 2017 Cell Cycle feature (PMID:28319435, title "SPAR, a lncRNA encoded mTORC1
  inhibitor").

### Endothelial / angiogenesis work (Baker lab)
- Spencer et al. 2020 [PMID:31990292, full text cached]. LINC00961 locus is endothelial
  enriched; the locus produces two molecules with opposing effects: [PMID:31990292 "The
  gene produces two molecules with opposing effects on angiogenesis: SPAAR and
  LINC00961."]. SPAAR ORF overexpression in HUVECs increased network formation
  [PMID:31990292 "Overexpression of the LV-SPAAR construct significantly enhanced
  endothelial network formation"]. Evidence for the peptide's angiogenic role is
  overexpression only; knockdown/locus KO removes both RNA and peptide.
- Endogenous SPAAR peptide not detected in basal HUVECs [PMID:31990292 "we are only able
  to see the presence of SPAAR micropeptide in LV-SPAAR conditions"].
- HA-SPAAR pull-down in HUVECs did **not** recover v-ATPase subunits: [PMID:31990292
  "SPAAR has been previously shown to bind the v-ATPase complex in HEK293.23 However, these
  proteins were not found in the SPAAR pull-down in HUVECs, suggesting a different function
  for SPAAR in ECs."]. Top hit SYNE1 (nesprin-1). This is a single overexpression AP-MS
  with no follow-up; not enough for an MF/BP annotation.
- Spiroski et al. 2021 [PMID:33478078]: whole-locus KO mice — sex-specific growth delay,
  smaller LV volumes, larger infarct risk area. Locus KO cannot separate lncRNA vs peptide
  function; not usable for peptide-specific GO annotation.

### Evolution
- Lee, Wacholder, Carvunis 2021 [PMID:34946813]: orthologs in marsupials and monotremes
  ("SPAAR has existed at least since the emergence of mammals"), low primary sequence
  conservation but conserved structure.

### Other literature
- Many LINC00961 cancer papers (miRNA sponge models, e.g. PMID:30825207 HCC) treat the
  transcript as a lncRNA and do not address the peptide. Not used for GO.

### Curation reasoning
- **Complex membership vs binding.** SPAAR is an interactor/regulator of the lysosomal
  v-ATPase, not a subunit (v-ATPase subunit inventory is ATP6V1*/ATP6V0*/accessory
  ATP6AP1/2; SPAAR is not among them and the interaction was not seen in HUVECs). GOA's
  `colocalizes_with GO:0046611` correctly avoids asserting membership; ACCEPT it with that
  reading. Do not propose `part_of`.
- **MF.** No MF term captures "negative regulator of amino-acid-induced mTORC1 lysosomal
  recruitment by stabilising v-ATPase-Ragulator-Rag supercomplex". `ATPase binding`
  (GO:0051117) would only restate the interaction, and there is no evidence SPAAR alters
  v-ATPase catalytic/pump activity, so no ATPase regulator term. Leave MF unset in core
  function; flagged as a question.
- **BP.** Core: GO:1904262 negative regulation of TORC1 signaling (IMP). GO:0071230
  cellular response to amino acid stimulus is acceptable (SPAAR acts specifically on the
  amino-acid arm of mTORC1 activation). GO:0043416 regulation of skeletal muscle tissue
  regeneration is a downstream tissue phenotype of the peptide-specific KO in mouse; keep
  as non-core.
- No NEW annotations proposed: angiogenesis evidence is overexpression-only in one study,
  with locus-level confounding.
