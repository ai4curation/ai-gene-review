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
