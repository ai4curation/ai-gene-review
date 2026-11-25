# selO (P77649) review notes

E. coli K-12 SelO / YdiU, a conserved pseudokinase-fold protein nucleotidyltransferase.
UniProt name: "Protein nucleotidyltransferase SelO"; AltNames protein adenylyltransferase
(EC 2.7.7.108) and protein uridylyltransferase (EC 2.7.7.-). SELO family (HAMAP MF_00692).

## Literature search (2026-11-24)

No deep-research file; searched PubMed directly.

- `SelO AMPylation pseudokinase Escherichia coli` -> 0 (too many AND terms); broadened.
- `Sreelatha A[Author] AMPylation` -> PMID:30270044 (the defining Cell paper), plus later
  mammalian SelO papers (PMID:40849408, 39700395, 41264253, 35101215, 40631560) that are about
  the human/mitochondrial ortholog, not E. coli, so used only as background.
- `YdiU[Title]` -> PMID:32966796 (Cell Rep, UMPylation of chaperones), PMID:35532215 (FlhDC),
  PMID:42432731 (SodA, 2026). `SelO OR YdiU UMPylation` -> 242; PMID:35532216 (Fur) via UniProt.
- UniProt P77649 cites PMID:30270044, 32966796, 35532215, 35532216 for function/catalytic
  activity; 3 PDB structures (6III, 6K20, 6LNA). Most mechanistic work on the UMPylation targets
  (FlhDC, Fur) is in Salmonella, but both papers confirm the activity with E. coli YdiU/substrates.

## Key findings

- SelO is a pseudokinase (protein-kinase fold with ATP flipped) that transfers AMP from ATP to
  Ser/Thr/Tyr of substrates [PMID:30270044 "SelO transfers AMP from ATP to Ser, Thr, and Tyr
  residues on protein substrates (AMPylation)"]. E. coli SelO AMPylates itself, SucA (Thr405) and
  GrxA (Tyr13); it localizes to mitochondria in eukaryotes and is needed for the oxidative-stress
  response. The E. coli enzyme was directly assayed (IDA rows PMID:30270044).
- YdiU/SelO also catalyses Mn2+-dependent UMPylation (UTP donor) of Tyr/His residues
  [PMID:32966796 "YdiU as an enzyme that catalyzes the covalent attachment of
  uridine-5'-monophosphate to a protein tyrosine/histidine residue, an unusual modification
  defined as UMPylation"]; auto-AMPylation padlocks the chaperone-UMPylation activity. Mn2+ and UTP
  are essential; it prefers UTP over ATP with Mn2+. Substrates include GroEL, DnaK, HtpG, ClpB.
- UMPylation of FlhC Ser31 abolishes FlhDC DNA binding and shuts off flagellar synthesis
  (Salmonella; E. coli FlhDC used in vitro) [PMID:35532215].
- UMPylation of Fur His118 destroys Fur dimers and derepresses iron uptake; the in vitro work
  used E. coli Fur and E. coli YdiU [PMID:35532216 "we used the E. coli homologous proteins (Fur
  and YdiU) for in vitro validation ... YdiU could catalyze in vitro UMPylation of Fur"].

## RHEA backing (staged RHEA:64604 Ser-UMP, 83887 Tyr-UMP, 83891 His-UMP -> broadMatch GO:0070569)

- E. coli SelO's UMPylation activity is demonstrated: Yang 2020 (PMID:32966796) shows UTP-donor
  UMPylation on Tyr/His (E. coli YdiU protein, auto-UMPylation and chaperone targets); Fur His118
  (PMID:35532216) and FlhC Ser31 (PMID:35532215) cover His, Ser and Tyr acceptors. So the
  protein genuinely has protein-uridylyltransferase activity (UMPylase). GO has no UMPylase MF
  term except the PII-specific GO:0008773 (Tyr, glutamine-synthesis signalling), which is wrong
  here. GO:0070569 uridylyltransferase activity is the correct existing broad class.
- The current GOA has NO UMPylase/UMPylation row at all (only AMPylase GO:0070733 and protein
  adenylylation GO:0018117). So the UMPylation activity is a genuine curation gap -> proposed as
  NEW to GO:0018177 protein uridylylation (BP, the only existing UMPylation term) and a NEW MF
  row, plus a proposed_new_term "protein UMPylase activity" under GO:0070569. The staged RHEA
  rows are thereby BACKED (review adds NEW annotation to GO:0070569 / its proposed child).
- Note: SelO is a dual AMPylase/UMPylase. Both are evolved activities (AMPylation: oxidative
  stress/redox; UMPylation: stress signalling, Mn2+-dependent), so neither is over-annotation.

## Curation decisions

- GO:0070733 AMPylase activity (IBA, IDA PMID:30270044, IEA RHEA/EC 2.7.7.108): ACCEPT the IDA
  (E. coli assay), ACCEPT IBA, ACCEPT the RHEA/EC IEA. Core.
- GO:0018117 protein adenylylation IDA: ACCEPT (core BP).
- GO:0016779 nucleotidyltransferase activity IEA: the generic parent of both AMPylase and
  UMPylase; KEEP (true, and it is the only existing term that covers the UMPylase side too). Not
  TOO_GENERAL because UMPylase has no specific GO term yet — keep it rather than assert it is
  subsumed. Actually both AMPylase (GO:0070733) and the proposed UMPylase sit under it; marking
  TOO_GENERAL once AMPylase is accepted is defensible, but UMPylase is only a proposed term, so I
  keep it as non-core to retain machine-readable coverage of the UMPylase activity. -> KEEP_AS_NON_CORE.
- Mg2+ (GO:0000287) and Mn2+ (GO:0030145) binding IEA: KEEP_AS_NON_CORE. Mg2+ supports AMPylation,
  Mn2+ is essential for UMPylation; both are genuine catalytic metals (PMID:30270044, 32966796).
- ATP binding GO:0005524 IEA: KEEP_AS_NON_CORE (cosubstrate).
- NEW: protein UMPylation (GO:0018177) BP and a NEW MF row to GO:0070569 with proposed child
  "protein UMPylase activity" — the demonstrated UMPylase activity is absent from GOA.

## Revision (PR review)

- GO:0016779 nucleotidyltransferase activity was changed from KEEP_AS_NON_CORE to TOO_GENERAL. Both specific child activities are now asserted in the review: GO:0070733 (accepted) and GO:0070569 uridylyltransferase activity (NEW). The generic parent therefore adds nothing, which matches how the trhO review treats its generic oxidoreductase rows.
