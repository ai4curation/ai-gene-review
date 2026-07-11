# PGM1 (human, UniProtKB:P36871) review notes

## Core biology
PGM1 = phosphoglucomutase-1 (EC 5.4.2.2), a cytosolic Mg2+-dependent enzyme that reversibly
interconverts alpha-D-glucose 1-phosphate (G1P) and alpha-D-glucose 6-phosphate (G6P) via an
alpha-D-glucose 1,6-bisphosphate intermediate, using a catalytic phosphoserine (Ser117).

- Reaction: alpha-D-glucose 1-phosphate = alpha-D-glucose 6-phosphate (RHEA:23536; ChEBI:58601 / 58225)
  [file:P36871 UniProt CATALYTIC ACTIVITY].
- Cofactor: binds 1 Mg2+ per subunit; coordinated in octahedral geometry by Ser117 + three
  aspartates (288, 290, 292) [PMID:26972339].
- Monomer [PMID:26972339 SUBUNIT].
- Cytoplasmic/cytosolic; 562 aa; alpha-D-phosphohexomutase superfamily.
- Activity regulation: Thr-467 phosphorylation by PAK1 enhances activity [PMID:15378030];
  glucose-1,6-bisP enhances Ser117 phosphorylation [PMID:25288802 / file:P36871].

## Metabolic role
Junction of glycogen metabolism and glycolysis/gluconeogenesis. In glycogenolysis converts the
G1P released by glycogen phosphorylase to G6P; runs in reverse for glycogen synthesis. Also feeds
nucleotide-sugar / galactose (Leloir) and pentose-phosphate pathways.
- "mediates the switch between glycolysis and gluconeogenesis" [PMID:26972339].
- "participates in both the breakdown and synthesis of glucose" [file:P36871 FUNCTION].

## PGM1-CDG (CDG type It / GSD XIV)
Deficiency causes a mixed glycogenosis + congenital disorder of glycosylation: cleft palate,
hepatopathy, hypoglycemia, dilated cardiomyopathy, exercise intolerance, abnormal transferrin
glycosylation. Notably galactose-responsive [PMID:30982613]. Blocked muscle glycogenolysis
mimicking McArdle disease and impaired glycogen synthesis [PMID:28882528].

## Annotation notes
- Many strong MF (IDA/EXP/IBA) supports for GO:0004614 phosphoglucomutase activity.
- GO:0000287 magnesium ion binding: IDA PMID:26972339 (crystal structures with Mg2+) + IEA.
- GO:0005515 protein binding (IPI PMID:21044950, TINF2/Q9BSI4): a genome-wide YFP-complementation
  telomere screen; bare "protein binding" not informative -> MARK_AS_OVER_ANNOTATED (not REMOVE).
- Cytosol/cytoplasm CC well supported (IDA HPA, NAS, Reactome TAS).
- Extracellular region / exosome / granule lumen: secondary "moonlighting"/proteomic localizations
  (HDA exosome, Reactome neutrophil-degranulation granule lumen) -> KEEP_AS_NON_CORE.
- BP: glucose metabolic process, carbohydrate metabolic process, glycolytic process,
  gluconeogenesis, glycogen catabolic process, Leloir/galactose catabolism all consistent with the
  central metabolic-hub role.
</content>
</invoke>
