# fgf8b notes (DANRE, Q805B2)

## 2026-09-28 session log

- Deep research FAILED for this gene (Edison: 402 Payment Required; the OpenAI key is invalid).
  Not retried, per instructions. Literature research was done by hand with Europe PMC REST; the
  searches and newly cached PMIDs are listed in `../fgf8a/fgf8a-notes.md`.
- Searches for fgf8b (or its old names fgf17 / fgf17a) morphants, mutants or CRISPR alleles found
  no published loss-of-function study of fgf8b. Full-text query `BODY:"fgf8b morpholino" OR ...`
  returned 0 hits; `BODY:"fgf8b mutant"` hits are dominated by the unrelated human FGF8b SPLICE
  ISOFORM. So every functional claim for fgf8b is expression, gain of function, or inference.

## Identity and naming

- Originally described as zebrafish fgf17 (Reifers et al. 2000); UniProt synonyms fgf17, fgf17a
  [file:DANRE/fgf8b/fgf8b-uniprot.txt "Synonyms=fgf17"].
- Renamed as a TGD co-orthologue of FGF8
  [PMID:17708537 "the teleost genes called fgf8 and fgf17a are duplicates of the tetrapod gene Fgf8, and thus should be called fgf8a and fgf8b"].
- Even at first description it was closer to Fgf8 in sequence
  [PMID:11091072 "In spite of a slightly higher aminoacid similarity to Fgf8"].
- Synteny: fgf8b on Dre1 with FGF8-flanking orthologues
  [PMID:19562753 "4 Mb region on zebrafish chromosome Dre1 containing fgf8b (Fig 4B)"].
- The fgf8b block lost fbxw4, whose introns carry fgf8 enhancers
  [PMID:17387144 "This block has retained NP_056263.1 and POLL , two genes that in the human genome are downstream from FGF8 , but has undergone deletion of fbxw4"].
- Protein: 212 aa, signal peptide 1-27, one N-glycosylation site; 70.8% identity to fgf8a
  (compare_pair.py). UniProt protein existence is "Evidence at transcript level".

## Expression (UniProt / PMID:11091072 and PMID:19562753)

- Not expressed during gastrulation; first at 8 somites in ventral MHB and anterior somites;
  optic stalks; otic vesicle at 24 h; hyoid at 30 h; dorsal diencephalon at 36 h
  [file:DANRE/fgf8b/fgf8b-uniprot.txt "Not expressed during gastrulation."].
- Shared with fgf8a at mid-somitogenesis: MHB and somites
  [PMID:19562753 "with strong expression of both genes in both species in the midbrain-hindbrain border (MBH) and somites (Fig. 6A–H)"].
- fgf8a-only domains: dorsal diencephalon and tailbud at mid-segmentation; telencephalon,
  olfactory epithelium, pharyngeal arches and fin AER at long-pec; heart.
  [PMID:19562753 "In zebrafish, fgf8a is required for the expression of cardiac genes (Reifers et al., ‘00b), but fgf8b is not expressed in the heart; conversely, in stickleback, fgf8b but not fgf8a is expressed in the heart (Jovelin et al., ‘07)."]
- Ear, anterior sensory patch: zebrafish fgf8b weak, fgf8a strong; stickleback the reverse
  [PMID:19562753 "The anterior sensory patch shows strong expression of sfgf8b in stickleback and its paralog zfgf8a in zebrafish, while expressing zfgf8b only weakly (Fig. 8D, F, H)."].
- No fgf8b-unique expression domain in zebrafish is reported in the sources read.

## Function

- Protein activity: mRNA injection shows it can act like fgf8
  [PMID:11091072 "fgf17 can act similar to fgf8 during gastrulation, when fgf17 is not normally expressed"].
- Regulation: downstream of pax2a (dose-dependent) and of fgf8a (maintenance) at the MHB
  [PMID:11091072 "only maintenance of fgf17 expression is disturbed at the MHB of acerebellar/fgf8 mutants"].
- Redundancy with fgf8a: the only test (ace;noi double mutants lacking fgf8a function and fgf8b
  expression) showed no enhanced DA-neuron phenotype
  [PMID:12843251 "To reveal possible redundant functions of FGF8 and FGF17, we analyzed th and dat expression in ace noi double mutant embryos that lack expression of both FGF8 and FGF17 (data not shown)."].

## Decisions

- 20 GOA rows reviewed.
- MF (growth factor activity, FGFR1/FGFR2 binding, FGFR binding NAS), FGFR signalling, MAPK
  cascade and extracellular region: ACCEPT. The protein keeps the FGF8 fold and signal peptide and
  acts like fgf8 in an injection assay, so the IBA MF/pathway terms apply to both paralogues.
- Cytoplasm IBA: MARK_AS_OVER_ANNOTATED (secreted ligand), same as fgf8a and human FGF8.
- D/V pattern formation IBA: MARK_AS_OVER_ANNOTATED. The protein could act in D/V patterning
  (injection assay), but the D/V axis is set in the blastula/gastrula, when fgf8b is not expressed.
  This is an expression-level loss of an ancestral subfunction, not a protein-level one.
- ARBA negative regulation of endodermal cell fate specification: REMOVE (gastrula-stage process;
  fgf8b not expressed then; no fgf8b evidence).
- ARBA mesoderm development and A/P pattern specification: MARK_AS_OVER_ANNOTATED (no
  fgf8b-specific evidence; the fgf8a evidence is gastrula-stage).
- NAS MHB development and pattern specification process: KEEP_AS_NON_CORE (expression and
  genetic-hierarchy evidence only; no loss-of-function).
- No NEW terms: no loss-of-function data exist for fgf8b.
