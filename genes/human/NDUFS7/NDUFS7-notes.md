# NDUFS7 (PSST) review notes

UniProtKB:O75251, HGNC:7714, human NADH:ubiquinone oxidoreductase core subunit S7 (PSST subunit,
Complex I-20kD). 213 aa precursor; mitochondrial transit peptide 1-38, mature chain 39-213.

## Core biology (verified)

- **Core catalytic subunit of mitochondrial respiratory Complex I** (NADH:ubiquinone oxidoreductase,
  EC 7.1.1.2). One of the 14 conserved "core" subunits (7 mtDNA-encoded ND subunits + 7 nuclear-encoded)
  that carry out catalysis; the ~30 other subunits are supernumerary/accessory. NDUFS7 is nuclear-encoded.
  [file:human/NDUFS7/NDUFS7-uniprot.txt "Core subunit of the mitochondrial membrane respiratory chain"]
- **Part of the iron-sulfur (IP) fragment**, in the Q-module near the ubiquinone-reduction site.
  UniProt: "This is a component of the iron-sulfur (IP) fragment of the enzyme".
- **Coordinates a [4Fe-4S] cluster** (UniProt COFACTOR: "Binds 1 [4Fe-4S] cluster"; BINDING residues
  88, 89, 153, 183). This is the terminal electron-acceptor cluster N2 that donates electrons to
  ubiquinone. PMID:27226634 (full text): "transfer of two electrons, one at a time, from the terminal
  electron acceptor iron-sulfur cluster N2 to ubiquinone is coupled to the ejection of four protons".
  Hence NDUFS7 carries a genuine redox MF (Fe-S binding / NADH:ubiquinone oxidoreductase), unlike
  purely accessory subunits.
- **Catalytic activity** (UniProt, ECO:0000269|PubMed:17275378): ubiquinone + NADH + 5 H(+)(in) =
  ubiquinol + NAD(+) + 4 H(+)(out); RHEA:29091; EC 7.1.1.2. NDUFS7 is "Essential for the catalytic
  activity of complex I" (PMID:17275378).
- **Localization**: mitochondrial inner membrane, peripheral membrane protein, matrix side
  (UniProt SUBCELLULAR LOCATION, ECO:0000305|PubMed:12611891). GOA anatomical term = GO:0005743.
- **Assembly**: Hydroxylated at Arg-111 (Arg-73 of mature protein in PMID:27226634) by NDUFAF5 early
  in Complex I assembly, before the peripheral/membrane arm juncture forms (PMID:27226634; UniProt PTM).

## Disease

- Mitochondrial complex I deficiency, nuclear type 3 (MC1DN3, MIM:618224); autosomal recessive;
  Leigh syndrome. Variant V122M (PMID:10360771, PMID:10330338), R145H (PMID:17275378, decreased enzyme
  activity). Complex I deficiency is the most frequent cause of mitochondrial disease.

## Annotation review reasoning

- **MF core**: The genuine, GOA-supported redox MFs are GO:0008137 NADH dehydrogenase (ubiquinone)
  activity and the Fe-S cluster binding terms (GO:0051536 / GO:0051539). Chose GO:0051539
  "4 iron, 4 sulfur cluster binding" as the primary Fe-S core MF because UniProt specifies a [4Fe-4S]
  cluster (matches the InterPro IPR006138 IEA and the 4 BINDING residues). GO:0008137 as the enzyme-
  activity MF (contributes_to at subunit level, but GOA carries `enables` IBA/IMP, so kept). GO:0048038
  quinone binding is consistent with the ubiquinone-reduction site being at the NDUFS7/ND1 interface.
- **NADH dehydrogenase activity GO:0003954** (contributes_to, IMP PMID:14749350) — the diaphorase/
  EC 1.6.99.3 activity; kept as accepted (contributes_to), but GO:0008137 (ubiquinone activity) is the
  more precise physiological MF.
- **GO:0016655** oxidoreductase acting on NAD(P)H, quinone acceptor (NAS PMID:8938450) — parent of
  GO:0008137; over-annotated (too general) given the specific GO:0008137 is present.
- **protein binding GO:0005515** (IPI): two entries (JPH3 PMID:32814053; UBQLN? PMID:27226634? actually
  Q5TEU4 PMID:27226634 and P28331/NDUFS8 PMID:15186778... wait check). Per policy, do NOT REMOVE bare
  protein-binding IPIs; MARK_AS_OVER_ANNOTATED (uninformative; real interactions are within Complex I).
- **protease binding GO:0002020** (IEA/Ensembl from rat ortholog) — weak electronic transfer; not core;
  keep as non-core / mark over-annotated (relates to caspase cleavage of complex I subunits in apoptosis,
  cf PMID:15186778 which is actually about NDUFS1 p75). Mark over-annotated.
- **neuronal cell body GO:0043025 / synaptic membrane GO:0097060** (IEA/Ensembl from rat) — these are
  reflections of high neuronal expression, not a distinct localization; keep as non-core.
- **mitochondrial matrix GO:0005759** (10x Reactome TAS) — Complex I peripheral arm protrudes into
  matrix, but the accepted anatomical CC for the protein is the inner membrane (matrix-side peripheral
  membrane protein). Keep matrix as non-core (matrix-facing) but inner membrane (GO:0005743) is the core CC.
- **respiratory chain complex I GO:0045271** (multiple: IBA, IEA, IPI, IMP, IDA) — core complex
  membership; ACCEPT the experimental ones, ACCEPT IBA.
- **BP core**: GO:0006120 mitochondrial electron transport NADH to ubiquinone (IMP PMID:17275378) is the
  core BP. GO:0032981 complex I assembly (IMP PMID:11112787) accepted (mutations impair assembly).
  GO:0009060 aerobic respiration (IBA/NAS) and GO:0015990 electron transport coupled proton transport
  (IBA) — accept but broader/non-core. GO:0042776 proton motive force-driven ATP synthesis (NAS) —
  downstream/indirect; complex I contributes to the pmf, not ATP synthesis per se; mark over-annotated.
</content>
