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
