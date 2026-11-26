# glnD (P27249) notes

Provider deep research (`just deep-research`) was NOT run for this gene; these notes
are compiled manually from the cached publications and the UniProt record.

## Function

- GlnD is a single bifunctional enzyme catalysing both uridylylation and deuridylylation
  of PII [PMID:6130097 "The purified enzyme catalyzes the uridylylation as well as the deuridylylation of the regulatory protein PII, demonstrating that a single bifunctional enzyme is involved in the covalent interconversion of PII."]
- Native enzyme is a monomer of ~95 kDa [PMID:6130097 "the native enzyme is a single polypeptide chain of Mr = 95,000 +/- 5,000"].
- Kinetics: [PMID:9737855 "The transferase reaction proceeded by an ordered bi-bi kinetic mechanism, with PII binding before UTP and pyrophosphate (PPi) released before PII-UMP."]
- Glutamine is the main signal: [PMID:9737855 "Glutamine inhibited the transferase reaction by inhibiting the chemistry step, while glutamine provided nonessential mixed-type activation of the uridylyl-removing activity"]
  and [PMID:9737855 "in intact cells the uridylylation state of PII is regulated mainly by the glutamine concentration"].
- Domain architecture: NT domain = UTase, HD domain = UR, two ACT domains = glutamine sensing
  (UniProt CC DOMAIN, ECO:0000269 PubMed:20363937); HD->AA/QN at 514-515 abolishes UR only,
  G93/G94/D107 mutations abolish UTase only (UniProt FT MUTAGEN).
- GlnK is also a substrate [PMID:8843440 "in vivo, the GlnK protein is uridylylated in a glnD-dependent fashion"].

## Physiology

- glnD::Tn10 mutants lack UTase and are glutamine auxotroph-like [PMID:26660 "A glnD::Tn10 strain synthesizes highly adenylylated glutamine synthetase under all conditions of growth"].
- Regulation of glnALG via PII and NtrB [PMID:2865248 "During nitrogen deprivation, uridylyltransferase, the product of glnD, is activated by the intracellular excess of 2-ketoglutarate over glutamine and converts PII to PII-UMP"].

## Curation decisions

- GO:0005515 rows (4): REMOVE per protein-binding policy; the PII interactions are enzyme-substrate.
- GO:0016779 -> MODIFY to GO:0008773.
- GO:0008081 phosphoric diester hydrolase: ACCEPT as the UR activity. No specific GO term for the
  PII uridylyl-removing reaction (RHEA:48600) was found in the local GO db (oaklib go.db) or QuickGO search;
  proposed as a new term.
- No NEW process terms added (protein uridylylation GO:0018177 was considered but not added; the
  MF term already describes the reaction).
- A history record was not created because the task restricted edits to genes/ECOLI/glnD/.
