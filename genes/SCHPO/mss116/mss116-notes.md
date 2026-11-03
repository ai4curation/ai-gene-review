# mss116 (S. pombe, O13622, SPBC691.04) curation notes

## 2026-11-01 session

### Sources consulted

- `mss116-uniprot.txt` (Swiss-Prot O13622; PE 3, inferred from homology).
- `mss116-goa.tsv` (11 GOA rows).
- `publications/PMID_38604460.md`: Wang, Feng, Huang 2024 *Mitochondrion*, the only
  S. pombe functional study. **Abstract only** (`full_text_available: false`; Europe PMC
  reports it is not open access and has no PMC copy). The bgpt MCP lookup by DOI
  failed (free-tier limit reached). A WebSearch found only abstract-level mirrors
  (x-mol, JoVE author pages), with no figures or methods.
- `publications/PMID_28520979.md`: De Silva et al. 2017 NAR, S. cerevisiae Mss116 and
  mitoribosome biogenesis / COX1 translation (full text cached).
- `publications/PMID_15618406.md`: Huang et al. 2005 PNAS, S. cerevisiae Mss116 is
  required for splicing of all mitochondrial group I and II introns (abstract cached).
- `publications/PMID_29514071.md`: Zeng et al. 2018 Cell Metab, yeast mtLSU assembly
  pathway (full text) places Mss116 as an early mtLSU assembly factor.
- `publications/PMID_34634819.md`: Herbert et al. 2021 NAR, S. pombe Mrh5 paper, which
  notes that Mss116 is the only other mitochondrial DEAD-box Q-motif helicase in S. pombe.
- `publications/PMID_16823372.md`: Matsuyama et al. 2006 ORFeome localisation (HDA
  mitochondrion row).

### Sequence and family

- 535 aa, predicted mitochondrial transit peptide 1..27 (UniProt FT TRANSIT,
  ECO:0000255), DEAD-box helicase ATP-binding domain 70..248 and helicase C-terminal
  domain 262..429, Q motif 38..66, DEAD box 195..198, disordered C-terminus 495..535.
- UniProt: "Belongs to the DEAD box helicase family. DDX18/HAS1 subfamily."
- UniProt CC FUNCTION is entirely By similarity (ECO:0000250): "ATP-dependent RNA
  helicase required for mitochondrial splicing of group I and II introns. Also required
  for efficient mitochondrial translation (By similarity)." This was written before
  PMID:38604460.
- S. pombe has only two mitochondrial DEAD-box Q-motif helicases
  [PMID:34634819 "There is only one other mitochondrial protein in this family in S. pombe, Mss116."].

### S. pombe evidence (PMID:38604460, abstract only)

All quotes are from the abstract.

- Deletion in an intron-containing mtDNA background lowers cox1 and cob1 mRNA, impairs
  mitochondrial translation, and causes respiratory and stationary-phase defects
  [PMID:38604460 "Deletion of spmss116 in a mitochondrial intron-containing background significantly reduced the levels of mitochondrial DNA (mtDNA)-encoded cox1 and cob1 mRNAs and impaired mitochondrial translation"].
- The mRNA defect is intron-dependent, but the translation defect is not
  [PMID:38604460 "Deletion of mitochondrial introns restored the levels of cox1 and cob1 mRNAs to wide-type (WT) levels but could not restore mitochondrial translation and respiration"].
  This is consistent with an intron-processing role (the S. cerevisiae role), but the
  abstract does not say that unspliced precursors accumulate, so splicing per se is
  not directly shown in the abstract.
- Mitoribosome assembly is impaired in both mtDNA backgrounds
  [PMID:38604460 "deletion of spmss116 in both mitochondrial intron-containing and intronless backgrounds impaired mitoribosome assembly and destabilization of mitoribosomal proteins"].
- The authors explain the translation defect as a consequence of the assembly defect
  [PMID:38604460 "defective mitochondrial translation caused by deletion of spmss116 is most likely due to impaired mitoribosome assembly"].

Not verifiable without the full text:

- Which subunit (mtLSU vs mtSSU) is affected, and the assay used (sucrose gradients?
  which markers?).
- Whether spMss116 co-sediments with mitoribosomes or any subunit (physical association).
- Whether unspliced cox1/cob1 precursors accumulate (direct splicing evidence) and which
  introns (group I vs group II) are affected.
- Whether helicase/ATPase-dead point mutants were tested (catalytic requirement).
- Whether localisation (mitochondrion, matrix) was tested in this paper.
- Whether mRNA-specific translation (e.g. Cox1) differs from global translation, as in
  S. cerevisiae.

### S. cerevisiae ortholog (P15424, YDR194C / SGD:S000002602)

- Splicing of all group I and II mitochondrial introns, RNA end processing, translation
  of a subset of mRNAs [PMID:15618406 "Mss116p, is required for the efficient splicing of all group I and II introns, some RNA end-processing reactions, and translation of a subset of mRNAs"].
- RNA chaperone function [PMID:15618406 "the splicing of both types of introns may require DEAD-box proteins that function as RNA chaperones"].
- Mitoribosome biogenesis [PMID:28520979 "Mss116 interacts with the mitoribosome assembly factor Mrh4, is required for efficient mitoribosome biogenesis, and consequently, maintenance of the overall mitochondrial protein synthesis rate"].
- Associates with 54S mtLSU [PMID:28520979 "Mss116 co-sedimented with fully assembled ribosomes in extracts prepared in the presence of 0.5 mM MgCl2 and with dissociated mtLSU"].
- Role in mtLSU assembly is non-essential, early [PMID:28520979 "although its role is not essential, Mss116 might participate in the biogenesis of the mtLSU, probably at an early step"].
- Joins mtLSU assembly early [PMID:29514071 "Mss116 and Mrm2 are incorporated early"].
- Direct, helicase-dependent role in COX1 translation via Pet309 in S. cerevisiae
  [PMID:28520979 "Mss116 is required for efficient COX1 mRNA translation initiation and elongation"].

### Decisions / reasoning

- MF: RNA helicase activity (IBA/IEA/ISO) ACCEPT as core; ATP binding and ATP hydrolysis
  activity KEEP_AS_NON_CORE (component chemistry of the helicase); nucleic acid binding
  MODIFY to RNA binding.
- CC: mitochondrion (HDA, IBA) ACCEPT per organelle policy; mitochondrial matrix
  (IEA, ISS) ACCEPT: transit peptide plus the ortholog's matrix RNA substrates
  (introns, rRNA) and a function (mitoribosome assembly, intron processing) that only
  happens in the matrix. Two lines, so the sub-compartment stands.
- BP: mitochondrial mRNA processing (ISS) ACCEPT, now with S. pombe support
  (intron-dependent loss of cox1/cob1 mRNA).
- NEW: mitochondrial ribosome assembly (GO:0061668, IMP, PMID:38604460). Participation
  test: in S. cerevisiae Mss116 is physically incorporated into early mtLSU assembly
  intermediates and co-sediments with the mtLSU, so the helicase is a plausible
  direct assembly factor (an RNA helicase remodelling rRNA, like E. coli SrmB), not
  merely a substrate. Comparator: the paralogous mitochondrial DEAD-box assembly
  factor Mrh4 is the standard example annotated to ribosome assembly. Kept at the
  generic GO:0061668 rather than GO:1902775 mtLSU assembly because the S. pombe
  abstract does not say which subunit.
- Not added: mitochondrial translation (GO:0032543). The S. pombe authors attribute the
  translation defect to the assembly defect; GO:0061668 is not part_of translation in
  GO, and adding translation would be annotating a downstream consequence. A direct
  mRNA-specific translation role (as with S. cerevisiae Pet309/COX1) is not shown for
  S. pombe in the abstract.
- Not added: group I / group II intron splicing terms; the abstract shows an
  intron-dependent mRNA level defect, not accumulation of unspliced precursors.

## 2026-11-01 session 2: full text of PMID:38604460

The user supplied the PDF. The full text is now in `publications/PMID_38604460.md`
(PDF extraction; supplementary figures S1-S3 and tables not available). All quotes
below are exact substrings of the cached file; the extraction joined hyphenated
line breaks, so some words appear joined, e.g. "intronretaining".

### Answers to the six open questions from session 1

1. **Which subunit and which assay.** Sucrose gradients (DDM, 10 mM MgCl2) probed with
   mtSSU Mrp5 and Rsm24 and mtLSU Mrpl16, and steady-state westerns adding Mrpl40.
   Assembled mitoribosomes are reduced, and proteins of **both** subunits are reduced
   [PMID:38604460 "Deletion of spmss116 impaired the formation of the mitoribosome (Fig. 6B)."]
   [PMID:38604460 "Deletion of spmss116 led to a statistically significant reduction in levels of two mtSSU proteins Mrp5 and Rsm24, and two mtLSU proteins Mrpl40 and"].
   The same holds with intronless mtDNA (Fig. S3). mt-rRNA levels are unchanged
   [PMID:38604460 "the levels of other mt-mRNAs and mt-rRNAs were unchanged or slightly increased in Δspmss116 cells"].
   Neither GO:1902775 (LSU) nor GO:0180026 (SSU) is specifically supported.
2. **Physical association.** None was detected; this is the opposite of budding yeast
   [PMID:38604460 "The results showed that spMss116-Myc did not cosediment with the mtSSU, mtLSU, or mitoribosome (Fig. 6A)."].
3. **Unspliced precursors.** Yes. RT-PCR shows intron-retaining cox1 (group I introns
   cox1-I1b, cox1-I2b) and cob1 (group II intron cob1-I1) precursors increased
   [PMID:38604460 "RT-PCR with cox1 and cob1 intron primers revealed that the levels of intronretaining cox1 and cob1 pre-mRNAs were increased in Δspmss116 cells"].
   The authors do not claim a splicing role, because the maturases come from
   mitochondrial translation
   [PMID:38604460 "relies on their intron-encoded proteins, whose synthesis was dependent on mitochondrial translation."]
   [PMID:38604460 "It remains to be determined whether spMss116 participates in splicing of mitochondrial introns."].
4. **Catalytic-dead mutants.** Not tested. The only rescue is overexpressed wild-type
   spMss116-HA. Budding-yeast Mss116 does **not** rescue
   [PMID:38604460 "overexpression of spmss116 but not scmss116 was able to restore growth of Δspmss116 cells on respiratory medium"].
5. **Global or specific translation defect.** Global: all mtDNA-encoded products fall
   in [35S] labelling with anisomycin, in both mtDNA backgrounds
   [PMID:38604460 "we demonstrate that the DEAD-box helicase spMss116 is required for global mitochondrial translation in S. pombe."].
   The budding-yeast Pet309/COX1-specific role is assigned in fission yeast to Mrh5C
   [PMID:38604460 "Thus, it appears that in S. pombe, Mrh5C assumes the role of the scMss116-Pet309 complex in mediating cox1 mRNA translation in S. cerevisiae."].
6. **Localisation.** There are dedicated experiments: Myc-tagged protein in purified
   mitochondria, controlled with Mcp60 (matrix), Sla1 (nuclear) and Tom20 (outer
   membrane); protease protection; carbonate extraction
   [PMID:38604460 "spMss116 was protected from proteinase K digestion in the absence of Triton X-100 (Fig. 1B), demonstrating that spMss116 is localized inside the mitochondria."]
   [PMID:38604460 "Most of spMss116 was found in the soluble fraction after treatment with Na2CO3, with a small amount in the pellet fraction (Fig. 1C)."].
   No IMS marker or mitoplasts were used, so matrix versus IMS is not resolved. The
   authors suggest a peripheral membrane protein
   [PMID:38604460 "These results suggest that spMss116 might be mitochondrial peripheral membrane protein."].

### Other facts

- S. pombe has **four** mitochondrial DEAD-box proteins (Mrh5, Rpm2, Mss116, Irc3).
  This corrects the session-1 statement "one of only two". Herbert 2021's "only one
  other" refers to the narrower class those authors considered.
- S. pombe mtDNA encodes an mtSSU protein
  [PMID:38604460 "a small mitochondrial ribosomal (mitoribosome) subunit (mtSSU) protein"].
  A primary translation defect could therefore itself impair assembly. The study did
  not relocate this gene to the nucleus, as De Silva 2017 did with VAR1 in budding
  yeast.
- The authors' own conclusion is weaker than the title
  [PMID:38604460 "Our study also suggests that spMss116 may participate in mitoribosome assembly."].

### Revised decisions

- **NEW GO:0061668 mitochondrial ribosome assembly, withdrawn.** The data establish
  necessity only. There is no co-sedimentation, no catalytic-mutant test, and
  assembly and translation cannot be ordered causally because of the mtDNA-encoded
  mtSSU protein. The authors themselves say "may participate". Recorded as a
  suggested question instead. GOA (2026) has no GO rows from this paper; whether
  PomBase captured it as FYPO phenotypes only was not checked.
- **GO:0032543 mitochondrial translation, still not added.** It has the same
  necessity-only problem; this is now recorded in the core function description
  rather than as a term.
- **GO:0090615 mitochondrial mRNA processing (ISS): ACCEPT → UNDECIDED.** The
  precursor accumulation is real but can be explained indirectly through loss of the
  maturases. The authors leave it open, and functional divergence from budding yeast
  is documented. No group I or group II splicing terms are added.
- **Mitochondrion IDA.** I tried a NEW row, but validation forbids NEW for a term
  already in GOA (HDA, IBA). The IDA evidence is now folded into the HDA row's reason,
  and a gene-specific IDA row is noted as a curation suggestion.
- **Matrix rows (IEA, ISS): ACCEPT kept.** The lines are now the transit peptide plus
  the protease-protected, carbonate-soluble behaviour; the reasons state that
  matrix versus IMS was not resolved experimentally.
- **Core function** location changed from mitochondrial matrix to mitochondrion,
  because the activity's site is shown only at organelle level. The process terms
  were removed from the core function, and a BIOLOGY knowledge gap was added
  (unknown target and step).
