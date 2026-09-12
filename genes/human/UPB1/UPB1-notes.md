# UPB1 (beta-ureidopropionase) — review notes

UniProtKB:Q9UBR1 (BUP1_HUMAN), gene UPB1 (syn. BUP1), 384 aa, chromosome 22q11.2.

## Function (well established)

UPB1 is **beta-ureidopropionase** (N-carbamoyl-beta-alanine amidohydrolase; beta-alanine synthase),
EC 3.5.1.6. It catalyzes the **third and final step of the reductive pyrimidine catabolic pathway**,
downstream of dihydropyrimidine dehydrogenase (DPYD) and dihydropyrimidinase (DPYS).

Reaction (Rhea:RHEA:11184): 3-(carbamoylamino)propanoate + H2O + 2 H+ = beta-alanine + NH4+ + CO2.
Also acts on N-carbamoyl-beta-aminoisobutyrate (3-ureidoisobutyrate) -> beta-aminoisobutyrate + NH3 + CO2
(the thymine-derived branch).

- [PMID:22525402 "ß-ureidopropionase is the third enzyme of the pyrimidine degradation pathway and catalyzes the conversion of N-carbamyl-ß-alanine and N-carbamyl-ß-aminoisobutyric acid to ß-alanine and ß-aminoisobutyric acid, ammonia and CO(2)."]
- [PMID:24526388 "The third step, catalyzed by β-ureidopropionase (βUP) (EC 3.5.1.6), results in conversion of N-carbamyl-β-alanine and N-carbamyl-β-aminoisobutyric acid into β-alanine and β-aminoisobutyric acid, respectively, with concomitant production of ammonia and carbon dioxide."]
- [PMID:29976570 "β-Ureidopropionase (βUP) catalyzes the third step of the reductive pyrimidine catabolic pathway responsible for breakdown of uracil-, thymine- and pyrimidine-based antimetabolites such as 5-fluorouracil."]

Kinetics: Km 15.5 uM for N-carbamoyl-beta-alanine [PMID:10415095]; positive cooperativity, Hill ~2.0
[PMID:11508704]; kcat 0.47/s, pH optimum 6.5 [PMID:29976570]. Expressed cDNA gives high activity
[PMID:10542323].

## Family / structure

Nitrilase (carbon-nitrogen hydrolase) superfamily, BUP family.
- [PMID:24526388 "Higher eukaryotic βUP belong to the nitrilase superfamily of enzymes"]
Catalytic nucleophile Cys233 (UniProt ACT_SITE 233; mutagenesis C233A abolishes activity, PMID:29976570).
Nitrilase-like catalytic tetrad Cys233/Lys196/Glu119/Glu207 (PMID:29976570 abstract).

## Oligomerization

Homodimer -> homotetramer -> homooctamer -> higher oligomers; pH- and ligand-dependent allosteric
regulation. Substrate promotes higher-MW active species; product beta-alanine dissociates to inactive
dimers.
- [PMID:29976570 "Existing as a homodimer at pH 9, the enzyme increasingly associates to form octamers and larger oligomers with decreasing pH."]
UniProt SUBUNIT: "Homodimer, homotetramer, homooctamer; can also form higher homooligomers."

## Zinc — NOT a zinc enzyme (curatorially important)

Early work reported ~0.5 zinc atoms/subunit and predicted a zinc site from sequence [PMID:11508704].
The crystal structure (PMID:29976570) shows NO bound zinc and that the predicted residues are too far
apart to form a site. The GOA "NOT|enables zinc ion binding" IDA (PMID:29976570) correctly negates the
earlier prediction. Supporting text taken from the UniProt CAUTION note (file: reference), since the
PMID:29976570 cache is abstract-only and does not restate the zinc conclusion verbatim.

## Localization

Cytoplasmic/cytosolic (UniProt SUBCELLULAR LOCATION: Cytoplasm; Reactome cytosol). The extracellular
exosome HDA (PMID:19056867) is a large-scale urinary-exosome proteomics detection — real observation but
not the site of function; keep as non-core. IEA cytoplasm (GO:0005737) is the broader parent of cytosol.

## Disease

Beta-ureidopropionase deficiency (UPB1D, MIM:613161), autosomal recessive, N-carbamyl-beta-amino
aciduria; highly variable neurological phenotype (intellectual disability, seizures, hypotonia,
microcephaly) to asymptomatic. Many loss-of-function missense variants (e.g., R326Q common in Japanese
population) act via impaired oligomer assembly / active-site disruption.
- [PMID:22525402 all 6 mutant enzymes had significantly decreased activity; markedly elevated
  N-carbamyl-beta-alanine/aminoisobutyric acid in urine and plasma]
- [PMID:24526388 R326Q high prevalence; E271K and R326Q profound activity decrease]

## GO term notes

- Core MF: GO:0003837 beta-ureidopropionase activity (EXP/IDA/IBA/IEA all agree). Verified label + Rhea.
- Core BP: GO:0019483 beta-alanine biosynthetic process (IDA/IBA/IEA). Note UniProt DR line lists the
  more specific GO:0033396 "beta-alanine biosynthetic process via 3-ureidopropionate" — but that term
  is now OBSOLETE (represents a GO-CAM model), so GO:0019483 is the correct level.
- GO:0046135 pyrimidine nucleoside catabolic process (IMP, PMID:22525402): the enzyme acts on
  N-carbamoyl-beta-alanine (a nucleobase-degradation intermediate), NOT a nucleoside. Better parent is
  GO:0006212 uracil catabolic process / GO:0006208 pyrimidine nucleobase catabolic process. MODIFY.
- in utero embryonic development (GO:0001701) and liver development (GO:0001889): IEA orthology transfer
  from rat (Q03248) via GO_REF:0000107. No evidence UPB1 has a developmental role beyond being a
  metabolic enzyme expressed in liver; keep as non-core (over-annotation candidates from Ensembl transfer).
- protein homodimerization / homooligomerization / homotetramerization: real (structural), supports the
  allosteric mechanism; keep, but oligomerization is a means to catalytic regulation, not the core
  biological function.
