# LNPEP (donkey, A0A9L0JGC2) notes

## Sequence and record

- Unreviewed TrEMBL entry, 1026 aa, "Leucyl-cystinyl aminopeptidase" (EC 3.4.11.3, ARBA name);
  peptidase M1 family; PANTHER PTHR11533:SF42; single N-terminal transmembrane segment 110..131
  (type II), catalytic M1 domain 393..611 with HExxH-(18)-E zinc ligands H464, H468, E487 and
  proton acceptor E465 [file:EQUAS/LNPEP/LNPEP-uniprot.txt "Belongs to the peptidase M1 family."].
- 12 GOA rows, all IEA (TreeGrafter, InterPro2GO, ARBA, GO_REF:0000120 combined).
- Donkey vs human Q9UIQ6 (1025 aa): 91.02% identity, 100% coverage of human
  [file:EQUAS/LNPEP/LNPEP-bioinformatics/RESULTS.md "with 91.02% identity across 1025 paired residues"].
  All mapped catalytic features conserved: zinc ligands H464/H468/E487, proton acceptor E465,
  GAMEN substrate motif (428-432), Tyr transition-state stabilizer (donkey 550), and both
  N-terminal dileucine internalization motifs (LL 53-54, 76-77). The human cleavage site that
  generates the pregnancy-serum form (F154-A155) is L154-A155 in donkey.

## Ortholog biology

- Human LNPEP (IRAP/oxytocinase/P-LAP) is a zinc M1 aminopeptidase that degrades oxytocin,
  vasopressin and angiotensin III [PMID:1731608 "the enzyme hydrolyzed oxytocin, vasopressin, and angiotensin III"].
- It is the angiotensin AT4 receptor binding site [PMID:11707427 "we identify the AT(4) receptor, by protein purification and peptide sequencing, to be insulin-regulated aminopeptidase (IRAP)"].
- Cell membrane (type II) and GLUT4 intracellular vesicles that translocate in response to
  insulin [file:EQUAS/LNPEP/LNPEP-bioinformatics/human_Q9UIQ6-uniprot.txt "The protein resides in intracellular vesicles together with GLUT4"].
- Existing human review: genes/human/LNPEP/LNPEP-ai-review.yaml (core MF metalloaminopeptidase
  activity; peptide catabolic process; cytoplasmic vesicle membrane, plasma membrane).

## Decisions

- Core: metalloaminopeptidase activity, peptide catabolic process, plasma membrane.
- Cytoplasmic vesicle -> MODIFY to cytoplasmic vesicle membrane (type II membrane protein).
- Broad MF/CC (aminopeptidase, metallopeptidase, membrane, cytoplasm): TOO_GENERAL.
- Zinc ion binding, peptide binding (angiotensin IV), regulation of blood pressure: non-core.

## ProtNLM2 (donkey40 snapshot)

- GO:0016020 membrane -> LSP (plasma membrane in GOA).
- GO:0008237 metallopeptidase activity -> LSP (metalloaminopeptidase activity in GOA).
- No non-GO outputs for this accession in the snapshot.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this pass.

- Deep research: `just deep-research-falcon EQUAS LNPEP --fallback perplexity-lite` failed
  (falcon "Failed to authenticate"; perplexity-lite HTTP 401 insufficient_quota). No
  deep-research file was produced; this pass relies on cached publications, the human Q9UIQ6
  Swiss-Prot record and the existing sequence comparison.
- Identity: A0A9L0JGC2 is a full-length gene model (1026 aa vs 1025 aa human Q9UIQ6; 100% of
  human paired, no unpaired segments >=5 aa) [file:EQUAS/LNPEP/LNPEP-bioinformatics/RESULTS.md
  "Paired coverage is 100.0% of the human sequence and 99.9% of the donkey sequence."]. Not a
  fragment or isoform; all three Pfam domains (Peptidase_M1_N, Peptidase_M1, ERAP1_C), the
  type II TM segment (110-131, Phobius) and all catalytic residues are present.
- Evolutionary grounding: UniProt places the donkey protein in PANTHER PTHR11533:SF42
  (LEUCYL-CYSTINYL AMINOPEPTIDASE), the same subfamily as human Q9UIQ6, mouse Q8C129 and rat
  P97629 (interpro/panther/PTHR11533/PTHR11533-entries.csv). Transfer from human/rodent LNPEP is
  therefore within-subfamily. Donkey GOA rows come from TreeGrafter node PTN001355382; human IBA
  rows for the LNPEP-specific terms (plasma membrane, regulation of blood pressure, neuropeptide
  catabolic process) come from PTN002609779 (rat Lnpep RGD:621752 donor). The node ids differ
  (likely PANTHER release difference); I could not inspect PAINT tree files for either node.
- PANTHER family review: interpro/panther/PTHR11533/ holds only an entries table and metadata (no
  family review); it agrees with SF42 placement. No disagreement.
- Modules: no module in modules/ lists LNPEP or Q9UIQ6. Grep for aminopeptidase/oxytocin/GLUT4
  hit only leptin_melanocortin_signaling.yaml and kallikrein_kinin_cascade.yaml, neither of which
  contains LNPEP.

### Changes

- GO:0006508 proteolysis: ACCEPT -> MODIFY to GO:0043171 peptide catabolic process. The previous
  reason argued the term was too broad while accepting it; this now matches the human review.
- GO:0031410 cytoplasmic vesicle: MODIFY now lists both supported descendants, cytoplasmic
  vesicle membrane and GO:0032593 insulin-responsive compartment (is_a cytoplasmic vesicle via
  secretory vesicle, OLS ancestors checked) [PMID:11701721 "IRAP is expressed and translocates to PM
  in response to insulin"].
- GO:0043171 peptide catabolic process: ACCEPT kept; added neuropeptide evidence
  [PMID:11389728 "P-LAP was shown to degrade several bioactive neuropeptides such as Met-enkephalin
  and dynorphin A (1-8)"]. Neuropeptide catabolic process (GO:0010813, descendant of GO:0043171,
  human IBA) goes in core_functions only, not as a NEW row, because it is a descendant of a term the
  gene already carries.
- Replaced quotes of the donkey record's ARBA-only "Single-pass type II membrane protein" with the
  human Swiss-Prot statement backed by PubMed:11389728 (ECO:0000269).
- Other rows unchanged after re-examination: plasma membrane ACCEPT; metalloaminopeptidase
  ACCEPT (core); aminopeptidase, metallopeptidase, cytoplasm, membrane TOO_GENERAL; zinc ion
  binding, peptide binding (AT4/angiotensin IV), regulation of blood pressure KEEP_AS_NON_CORE.
- Not transferred: MHC class I antigen cross-presentation (endosomal IRAP in mouse dendritic
  cells; human review accepts it). Equine immune-cell data are absent and the GOA set does not carry
  it, so it was not proposed as NEW.
- Relative: human LNPEP Q9UIQ6 (same subfamily SF42), already completely reviewed at
  genes/human/LNPEP/LNPEP-ai-review.yaml (status COMPLETE).
