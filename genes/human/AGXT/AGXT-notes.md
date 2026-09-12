# AGXT (P21549) review notes

Human alanine--glyoxylate aminotransferase (AGT), HGNC:341. Liver-specific,
peroxisomal, PLP-dependent aminotransferase (class-V PLP family). Deficiency
causes primary hyperoxaluria type 1 (PH1, MIM:259900).

## Core biochemistry / function
- Peroxisomal aminotransferase that transaminates glyoxylate to glycine
  (glyoxylate + L-alanine -> glycine + pyruvate; EC 2.6.1.44) and thereby
  detoxifies glyoxylate, preventing its oxidation to oxalate
  [UniProt P21549 FUNCTION; PMID:23229545 "Failure to transaminate glyoxylate
  to glycine within the peroxisomes, allows glyoxylate to diffuse into the
  cytosol where it is oxidized to the metabolic end product oxalate"].
- Also catalyses serine:pyruvate transamination (EC 2.6.1.51; L-serine +
  pyruvate = 3-hydroxypyruvate + L-alanine) contributing to serine metabolism /
  gluconeogenesis [PMID:10347152].
- Kinetic study concludes the enzyme is "highly specific for catalysing
  glyoxylate to glycine processing, thereby playing a key role in glyoxylate
  detoxification" [PMID:17696873].
- Can also perform beta-elimination of beta-chloro-L-alanine and
  half-transamination of L-cysteine (side reactions) [PMID:18492492].

## Cofactor / structure
- PLP-dependent; PLP covalently bound to Lys209 (Schiff base) [PMID:12899834;
  UniProt MOD_RES 209]. PLP-binding affinity reduced by G82E, minor-allele I340M
  [PMID:17696873, PMID:15802217].
- Active enzyme is a homodimer; N-terminal extension wraps over neighbouring
  subunit and is essential for the active dimer [PMID:22198249, PMID:12899834,
  PMID:10960483, PMID:16971151, PMID:20133649].

## Localization
- Peroxisome / peroxisomal matrix in human liver, randomly dispersed through
  the matrix [PMID:3418107, PMID:9053548, PMID:3709805, PMID:1703535,
  PMID:7813517]. Imported via Pex5p recognising an atypical C-terminal KKL PTS1
  plus ancillary C-terminal targeting info [PMID:22529745, PMID:15911627].
- Species-dependent compartmentalization (peroxisomal in human/rabbit;
  peroxisomal+mitochondrial in rodents; mostly mitochondrial in cat) [UniProt
  CAUTION; PMID:7813517]. Human lost the ancestral N-terminal mitochondrial
  targeting signal by an initiation-codon point mutation [PMID:2363689].
- Disease mistargeting: the minor allele P11L creates a cryptic N-terminal MTS;
  in combination with G170R (and I244T/F152I/G41R) AGT is rerouted to
  mitochondria where it cannot detoxify peroxisomal glyoxylate [PMID:1703535,
  PMID:23229545, PMID:24055001, PMID:26149463].

## Disease
- PH1: calcium-oxalate nephrolithiasis/nephrocalcinosis, oxalosis, ESRD
  [UniProt DISEASE; many variant refs].

## Annotation review decisions (summary)
- Core MF used in core_functions: GO:0008453 L-alanine:glyoxylate transaminase
  activity (exact term in GOA, current OLS label matches).
- L-serine:pyruvate transaminase activity (GO:0004760) kept as accepted
  secondary MF (EC 2.6.1.51, experimentally shown PMID:10347152).
- PLP binding GO:0030170 accepted (secondary). Homodimerization GO:0042803
  accepted (non-core, quaternary structure requirement).
- protein binding GO:0005515 IPIs (IntAct/HuRI Y2H) -> MARK_AS_OVER_ANNOTATED
  (uninformative; mostly keratin/keratin-associated Y2H hits + PEX5 which is the
  real biology but captured as bare protein binding). identical protein binding
  GO:0042802 -> ACCEPT (reflects the biologically real homodimer).
- amino acid binding GO:0016597 (IDA, PMID:18492492) ACCEPT (substrate binding
  demonstrated). transaminase activity GO:0008483 -> MODIFY to GO:0008453
  (parent, too general).
- L-cysteine catabolic process GO:0019448 (IDA PMID:18492492) -> in vitro side
  reaction; KEEP_AS_NON_CORE. L-serine catabolic process GO:0006565 (IDA
  PMID:10347152) KEEP_AS_NON_CORE. L-alanine catabolic process GO:0042853 ->
  L-alanine is the amino donor of the physiological reaction; KEEP_AS_NON_CORE.
- glyoxylate catabolic/metabolic + glycine biosynthetic processes: ACCEPT (core
  BP).
- cytoplasm/cytosol IEA/TAS: AGT is peroxisomal in human; cytosol/cytoplasm
  reflect the pre-import stage / Reactome import reaction. IEA cytoplasm
  (ARBA) is a default-localization over-annotation -> MARK_AS_OVER_ANNOTATED;
  Reactome cytosol TAS KEEP_AS_NON_CORE (import-pathway context).
</content>
