# pgm (E. coli K-12, P36938) curation notes

## Deep research

`just deep-research ECOLI pgm --provider perplexity` was attempted on 2026-10-23 and failed:
the perplexity provider is not configured in this environment ("Provider 'perplexity' not
available. Available: falcon, openscientist"). No deep-research file was generated. These
notes were compiled manually from cached publications and the UniProt record.

## Identity and family

- Phosphoglucomutase, EC 5.4.2.2, 546 aa; PANTHER PTHR22573:SF57 (PGM1-type), InterPro
  IPR005852 alpha-D-glucose-specific PGM [file:ECOLI/pgm/pgm-uniprot.txt "DR   InterPro; IPR005852; PGM_a-D-Glc-sp."].
- Active-site phosphoserine Ser146 and Mg2+ ligands Asp304/306/308, transferred by
  similarity from rabbit PGM1 (P00949) in UniProt.

## Biochemistry

- Purified from E. coli by Joshi and Handler (1964) [PMID:14216423; cached record is title-only].
  UniProt curates from this paper: "Reaction=alpha-D-glucose 1-phosphate = alpha-D-glucose 6-phosphate",
  "KM=50 uM for D-glucose-1-phosphate {ECO:0000269|PubMed:14216423}", "Optimum pH is 9",
  "Binds 1 Mg(2+) ion per subunit" [file:ECOLI/pgm/pgm-uniprot.txt].

## Genetics

- Adhya and Schwartz 1971 [PMID:4942754 "Bacteria with strongly depressed phosphoglucomutase (EC 2.7.5.1) activity are found among the mutants of Escherichia coli"]:
  pgm mutants accumulate amylose on maltose and galactose, "grow poorly on galactose", and
  "amino acid- or glucose-grown pgm mutants are sensitive to phage C21, indicating a deficiency in the biosynthesis of uridine diphosphoglucose or uridine diphosphogalactose, or both."
- Lu and Kleckner 1994 [PMID:8083177 "pgm deletion mutant strains are deficient in phosphoglucomutase activity."]
  cloned pgm and showed conservation with yeast, rabbit and human PGMs.
- Hill et al. 2013 [PMID:23935518 "pgm null mutants that are defective in the first step of UDP-glucose biosynthesis"]:
  pgm mutants are ~25% smaller in LB-glucose ("5.66 µm2 while pgm mutants were 4.24 µm2");
  UDP-glucose acts through OpgH, which antagonizes FtsZ assembly. The cell-size phenotype is
  an indirect (signalling) consequence, so no cell-size GO term was proposed.
- 13C-MFA of a pgm deletion: UniProt notes "Increases growth on glucose by 10% but causes a minor decrease in native reaction flux" [file:ECOLI/pgm/pgm-uniprot.txt, from PMID:31390539].

## Secondary activity

- Patel et al. 2019 [PMID:31589605 "These results suggest that E. coli Pgm is also a bifunctional PGM/PNGM when expressed in B. subtilis."]:
  overexpressed E. coli Pgm suppresses a B. subtilis glmR mutant, dependent on Ser45 (the
  position equivalent to PgcA Gly47). Only heterologous genetic evidence; no NEW
  phosphoglucosamine mutase annotation was proposed for E. coli Pgm.

## Localization

- Cytosolic: two proteomic fractionation studies [PMID:15911532; PMID:18304323 "we identified 1103 proteins from the cytosolic fraction of the Escherichia coli strain MC4100"];
  UniProt "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:21778229}".

## Curation decisions (summary)

- GO:0004614 (IBA, IDA, IEA, IMP x2): ACCEPT, core.
- GO:0000287: KEEP_AS_NON_CORE (cofactor).
- GO:0005515 GhrB IPI (Butland 2005 AP-MS): REMOVE under the protein-binding policy.
- GO:0005737: MODIFY to GO:0005829; GO:0005829 (IBA, IDA x2): ACCEPT.
- GO:0005975 (IBA, IEA): MODIFY to GO:0019255 glucose 1-phosphate metabolic process.
- GO:0016868: MODIFY to GO:0004614.
- NEW: GO:0120530 UDP-alpha-D-glucose biosynthetic process; GO:0033499 Leloir pathway.
  Comparator check (QuickGO 2026-10-23): yeast PGM2 (P37012) carries GO:0006011, GO:0019255
  and GO:0019388; human PGM1 (P36871) carries GO:0033499 (IMP).
- Used as an exemplar of the dedicated phosphoglucomutase route (GO:0004614) in
  modules/udp_glucose_and_udp_galactose_biosynthesis.yaml. Note that E. coli Pgm is a
  PTHR22573 (PGM1-type) enzyme, whereas B. subtilis PgcA and P. putida Pgm are PTHR45745
  (PGM2-like); both families supply the same reaction.
