# ORC5 (donkey, A0A9L0JAR4) notes

## Sequence and record

- Unreviewed TrEMBL entry, 440 aa, "Origin recognition complex subunit 5"; PANTHER
  PTHR12705:SF0; Orc1-like AAA ATPase domain (8..155), ORC5 lid (204..271), ORC5 C-terminal
  winged-helix region (302..421) [file:EQUAS/ORC5/ORC5-uniprot.txt "Belongs to the ORC5 family."].
- 6 GOA rows, all IEA (InterPro2GO, TreeGrafter, GO_REF:0000120 combined).
- Donkey vs human O43913 (435 aa): 92.87% identity, 100% coverage of human; donkey has a
  5-residue C-terminal extension (436-440); Walker A P-loop GHTASGKT conserved
  [file:EQUAS/ORC5/ORC5-bioinformatics/RESULTS.md "BINDING (): human [37, 38, 39, 40, 41, 42, 43, 44] GHTASGKT -> donkey [37, 38, 39, 40, 41, 42, 43, 44] GHTASGKT."].

## Ortholog biology

- Human ORC5: subunit of the six-subunit ORC that binds replication origins in an
  ATP-dependent manner and is required to assemble the pre-replication complex
  [file:EQUAS/ORC5/ORC5-bioinformatics/human_O43913-uniprot.txt "ORC is required to assemble the pre-replication complex necessary to initiate DNA replication."].
- Human ORC cryo-EM: ORC2-5 forms a stable core; ORC subunits 1-5 have positively charged
  regions near DNA; the ORC5-ORC3 interface acts as a hinge that may facilitate DNA binding
  [PMID:32808929 "revealing a hinge at the ORC5·ORC3 interface that may facilitate ORC binding to DNA"].
- Human GOA (QuickGO 2026-10-14): nuclear ORC (IDA, IPI), DNA replication initiation (IDA),
  DNA replication origin binding (TAS, IBA).

## Decisions

- Core: nuclear origin of replication recognition complex, DNA replication initiation, DNA
  replication origin binding (as a contributing subunit of ORC), nucleus.
- ORC (InterPro): ACCEPT; DNA replication (combined IEA): TOO_GENERAL.

## ProtNLM2 (donkey40 snapshot)

- GO:0006260 DNA replication -> LSP (DNA replication initiation in GOA).
- GO:0005634 nucleus -> CNN (exact term in GOA, correct).
- Non-GO: function text describing ORC component binding origins, ATP-dependent DNA binding,
  pre-RC assembly (not scored; closely mirrors the ARBA function text in the donkey record).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this section.

### Deep research

- `just deep-research-falcon EQUAS ORC5 --fallback perplexity-lite` failed: Edison API returned
  403 Forbidden at login, and the perplexity-lite fallback also exited non-zero. No deep-research file
  was produced; the review relies on the cached papers below and the human UniProt record.

### Identity of the benchmark accession (gene-model issue)

- New analysis `ORC5-bioinformatics/compare_gene_models_rereview.py` (run with `uv run --script`;
  output `RESULTS-rereview.md`, `results-rereview.json`) fetched all ten donkey ORC5 UniProt entries.
  All are products of one Ensembl gene, ENSEASG00005017348, in proteome UP000694387, so they are
  transcript models of the same gene, not paralogs.
- A0A9L0JAR4 (440 aa) is identical in architecture to human O43913 through residue 421
  (402/420 identical in residues 1-420). It then ends in an alternative 19-residue segment
  `GPPKTCLQTHKNRLTMSSH` in place of the conserved mammalian C-terminus `TVNFDIIKYLYDFL` (human
  422-435), which human, mouse and horse all share
  [file:EQUAS/ORC5/ORC5-bioinformatics/RESULTS-rereview.md "Benchmark accession A0A9L0JAR4: length 440, identity 94.84% to human over 426 paired residues; C-terminus RGPPKTCLQTHKNRLTMSSH; human-type C-terminus present: False."].
  This looks like an alternative last exon or intronic read-through. Pfam ORC5_C (302..421) is intact.
- The earlier RESULTS.md reported 100% human coverage and 92.87% identity because it aligned the
  divergent tail against the human tail. It is superseded (but not deleted) by RESULTS-rereview.md.
- The canonical-type donkey product is A0A9L0I6Y4 (435 aa, same gene, 100% human coverage, human-type
  C-terminus). A0A9L0KD90 (463) and A0A9L0KFQ4 (474) also carry the human-type C-terminus but have
  extensions.
- Walker A GHTASGKT (37-44) and the DNA-proximal beta-hairpin residue H398 are conserved
  [PMID:32808929 "The β-hairpin loop in ORC5 of HsORC also consists of a positively-charged residue H398 in close proximity to DNA"].

### Evolutionary grounding

- PTHR12705 has a single subfamily (SF0), which contains ORC5 from human, fission yeast, rice and
  Plasmodium (`interpro/panther/PTHR12705/PTHR12705-entries.csv`). The donkey gene is PTHR12705:SF0.
  There is no subfamily split to worry about, and no family review disagrees with this placement
  (only the InterPro metadata/entries files exist). The TreeGrafter rows come from node PTN001398615.
- The closest characterised relative is human ORC5 (O43913), a one-to-one ortholog in the same
  subfamily. Human ORC5 has no review in the repo. The horse partner (genes/HORSE/ORC5, A0A3Q2KSP7) is
  reviewed by another agent.

### Literature used

- PMID:17716973 (abstract): ORC5 ATP-binding site mutations impair human ORC assembly
  [PMID:17716973 "Mutations in the ATP-binding sites of Orc4 or Orc5"].
- PMID:31160578 (full text): chromatin-bound ORC3/5 are multi-mono-ubiquitylated by OBI1 as
  origins fire
  [PMID:31160578 "Altogether, these results showed that chromatin-bound ORC3/5 become multi-mono-ubiquitylated concomitantly with origin firing."].
- PMID:32808929 (full text): human ORC cryo-EM.

### Decisions (unchanged in action, reasons revised)

- ORC, nuclear ORC, DNA replication initiation, nucleus: ACCEPT. Transfer is justified by one-to-one
  orthology in the single PANTHER subfamily. The alternative C-terminus removes only the last 14
  canonical residues, but no product-specific evidence exists.
- DNA replication origin binding: ACCEPT, recorded as contributes_to in core_functions, because
  the activity belongs to the complex.
- DNA replication: TOO_GENERAL. It is entailed by DNA replication initiation.
- No NEW terms. ATP binding (Walker A, PMID:17716973) is raised as a suggested question instead.
- Modules: `modules/dmel_replication_origin_licensing_activation.yaml` (Drosophila ORC/licensing;
  Orc5 = Q24169) is the only related module. There is no mammalian ORC module.
