# SLC13A5 (NaCT / NaC2 / INDY ortholog) — curation notes

UniProt: Q86YT5 (S13A5_HUMAN), 568 aa. Gene SLC13A5 (syn. NACT), HGNC:23089,
chromosome 17p13. TC 2.A.47.1.9 (DASS / divalent anion:Na+ symporter family),
NADC subfamily. PANTHER PTHR10283:SF109 "NA(+)/CITRATE COTRANSPORTER".

## Core biology (verified)

NaCT is the plasma-membrane, Na+-coupled, high-affinity citrate transporter that
imports extracellular (circulating) citrate into cells. It is the human ortholog
of *Drosophila* Indy and most closely related among human paralogs to the
dicarboxylate transporters NaDC1/SLC13A2 and NaDC3/SLC13A3 (which prefer
dicarboxylates and are basolateral kidney/brain), and the sulfate transporter
NaS1/SLC13A1.

- Cloning + function: "human NaCT mediates the Na(+)-coupled transport of citrate";
  "the transporter is selective for citrate with comparatively several-fold lower
  affinity for other intermediates of citric acid cycle"; "The transport process
  is electrogenic"; Km(citrate) ~650 uM; expressed "most predominantly in the
  liver, with moderate expression detectable in the brain and testis"
  [PMID:12445824].
- It "may facilitate the utilization of circulating citrate for the generation of
  metabolic energy and for the synthesis of fatty acids and cholesterol"
  [PMID:12445824] — i.e. it supplies cytosolic citrate; it does NOT itself perform
  the lipogenic or TCA reactions. Downstream metabolic roles therefore are
  context, not participation.
- Direction/mechanism: Na+-coupled SYMPORT (import), electrogenic, stoichiometry
  "probably 4 Na(+) for each carboxylate" [file uniprot CC:FUNCTION; PMID:12445824].
  Recognizes the trivalent form of citrate. Homodimer, elevator-type transport
  mechanism [file uniprot CC:SUBUNIT; PMID:33597751 cryo-EM]. NOT an
  antiporter/exchanger.
- Substrate range: citrate (primary, tricarboxylate). "Can recognize succinate as
  a substrate, but its affinity for succinate is several fold lower than for
  citrate" [file uniprot CC:FUNCTION; PMID:26324167]. Also transports other TCA
  dicarboxylates (succinate, fumarate, oxaloacetate, 2-oxoglutarate) at much lower
  affinity — curated IDA rows from [PMID:26324167]. These are genuine but secondary
  substrates → non-core.
- NaCT is NOT the mitochondrial citrate carrier (that is SLC25A1). NaCT is purely
  plasma-membrane; a mitochondrial localization row here would be an error. (No such
  row present in GOA.)
- Species difference: "Mouse NaCT had at least 20- to 800-fold higher affinity for
  these intermediates than human NaCT"; human NaCT is "not" fully active at
  physiologic plasma citrate [PMID:26324167]. Does not change the human function;
  informs drug-target translatability.

## Localization (verified PM)

Cell membrane / plasma membrane, multi-pass (11 TM helices by cryo-EM)
[file uniprot CC:SUBCELLULAR LOCATION; PMID:26384929, PMID:30054523, PMID:33597751].
DEE25 mutants variously lose PM localization and/or transport function
[PMID:26384929, PMID:30054523].

## Regulation

Stimulated by Li+ in the presence of Na+; Li+ changes stoichiometry from 4:1 to
2:1 Na+:citrate [file uniprot CC:ACTIVITY_REGULATION; PMID:12826022 (not cached),
PMID:33597751]. Basis of the GO:0071285 "cellular response to lithium ion" row
(cited to PMID:26324167 cation-dependence study). This is a biophysical/
pharmacological property, peripheral to the core transport function → non-core.
Inhibited by PF-06649298 (binds the citrate site) [PMID:33597751].

## Disease (downstream phenotype, not core MF)

Autosomal-recessive Developmental and epileptic encephalopathy 25 with
amelogenesis imperfecta (DEE25 / EIEE25, "SLC13A5 citrate transporter disorder"),
MIM 615905: neonatal seizures, severe developmental delay, tooth hypoplasia
[PMID:24995870, PMID:26384929, PMID:30054523]. "Neurons are considered incapable
of de novo synthesis of tricarboxylic acid cycle intermediates; therefore they
rely on the uptake of intermediates, such as citrate" [PMID:26384929]. Seizure /
neurodevelopment / tooth phenotypes are downstream consequences of loss of citrate
import; they are not functions the protein performs and are not annotated here as
core (no NEW phenotype/process terms warranted — fails the participation test).

## Protein-binding rows

All GO:0005515 rows come from high-throughput binary/AP-MS interactome screens
[PMID:28514442 interactome map; PMID:32296183 HuRI reference binary interactome;
PMID:33961781 BioPlex]. Partners are mostly keratin-associated proteins (KRTAPs)
and other sticky/HT-prone proteins (EEF1A2, CD79A, GOLM1, MDFI, KLHL20, GJA8,
ADAMTSL4, CYSRT1) with no mechanistic link to citrate transport. Per project
protein-binding policy these uninformative bare-binding rows are REMOVE (removal
does not assert the interactions are false). The genuine, structurally supported
self-association (homodimer) is captured instead as a NEW GO:0042802 identical
protein binding row.

## Action summary rationale

- Core MF: GO:0015137 citrate transmembrane transporter activity (substrate-named,
  IDA/IMP/IBA/TAS) + GO:0005343 organic acid:sodium symporter activity (the Na+
  coupling mechanism; no "sodium:citrate symporter activity" term exists in GO —
  confirmed via OLS). Both ACCEPT.
- Core BP: GO:0015746 citrate transport (ACCEPT; a transporter executing its
  transport is core), GO:0035674 tricarboxylic acid transmembrane transport
  (ACCEPT). GO:0035725 sodium ion transmembrane transport is KEEP_AS_NON_CORE
  (Na+ is the coupling ion, not the cargo; aligned with SLC13A3).
- Secondary substrates (succinate/fumarate/oxaloacetate/2-oxoglutarate transport
  and sodium:dicarboxylate symporter / tricarboxylate transporter rows that are
  peripheral) → KEEP_AS_NON_CORE. GO:0015142 tricarboxylic acid transmembrane
  transporter activity kept as core-aligned ACCEPT (citrate is the physiological
  tricarboxylate).
- TOO_GENERAL (imprecise-on-their-own terms, each entailed by a specific term
  asserted here): GO:0016020 membrane, GO:0022857 transmembrane transporter
  activity, GO:0055085 transmembrane transport, GO:0015370 solute:sodium symporter
  activity.
- Plasma membrane rows → ACCEPT (core location, strongly supported).
- No source defects found. No gene-model issues.
