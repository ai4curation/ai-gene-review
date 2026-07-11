# DPYS (dihydropyrimidinase, Q14117) — review notes

## Summary of function
DPYS encodes dihydropyrimidinase (DHP/DHPase; EC 3.5.2.2), the second enzyme of the
three-step reductive pyrimidine catabolic (degradation) pathway, acting downstream of
dihydropyrimidine dehydrogenase (DPYD) and upstream of beta-ureidopropionase (UPB1).
It catalyzes the reversible, Zn2+-dependent hydrolytic ring opening of 5,6-dihydrouracil
to N-carbamoyl-beta-alanine (3-ureidopropanoate) and of 5,6-dihydrothymine to
N-carbamoyl-beta-aminoisobutyrate (3-ureidoisobutyrate).
[file:human/DPYS/DPYS-uniprot.txt "Catalyzes the second step of the reductive pyrimidine
degradation, the reversible hydrolytic ring opening of dihydropyrimidines. Can catalyze
the ring opening of 5,6-dihydrouracil to N-carbamyl-alanine and of 5,6-dihydrothymine to
N-carbamyl-amino isobutyrate."]

- Member of the metallo-dependent hydrolases (amidohydrolase / cyclic amidohydrolase)
  superfamily, hydantoinase/dihydropyrimidinase family (MEROPS M38; Pfam PF01979
  Amidohydro_1). [file:human/DPYS/DPYS-uniprot.txt "Belongs to the metallo-dependent
  hydrolases superfamily."]
- Binuclear zinc metalloenzyme: binds 2 Zn2+ per subunit, bridged by a carboxylated
  (carbamate) lysine (Lys159 -> N6-carboxylysine). PDB 2VR2 (human enzyme with zinc).
  [file:human/DPYS/DPYS-uniprot.txt "Binds 2 Zn(2+) ions per subunit."]
- Quaternary structure: homotetramer.
  [file:human/DPYS/DPYS-uniprot.txt "Homotetramer."]
- Tissue expression: liver and kidney (HPA: group-enriched kidney/liver).
  [file:human/DPYS/DPYS-uniprot.txt "Liver and kidney."]
- Subcellular localization: cytosolic.

## Catalytic activity (RHEA/EC)
RHEA:16121, EC 3.5.2.2: 5,6-dihydrouracil + H2O = 3-(carbamoylamino)propanoate + H(+).
[file:human/DPYS/DPYS-uniprot.txt "EC=3.5.2.2"]

## Disease
Dihydropyrimidinase deficiency (DPYSD, MIM 222748): autosomal recessive disorder of
pyrimidine metabolism, dihydropyrimidinuria, variable phenotype (epileptic/convulsive
attacks, dysmorphism, developmental delay, congenital microvillous atrophy); most
patients asymptomatic. Confers risk of 5-fluorouracil (fluoropyrimidine) toxicity.
[file:human/DPYS/DPYS-uniprot.txt "autosomal recessive disorder of pyrimidine metabolism
characterized by"]
- Mutation analysis of the human gene, first DHP-deficiency mutations; all reduced enzyme
  activity in eukaryotic expression. [PMID:9718352 "Using a eukaryotic expression system,
  we showed that all mutations reduced enzyme activity significantly, indicating that
  these are crucial DHP deficiency-causing mutations."]

## Annotation review reasoning
- Core MF = GO:0004157 dihydropyrimidinase activity (multiple IDA/IMP/IBA/ISS/IEA);
  ACCEPT. Direct experimental support: PMID:10410956 (radiochemical DHP activity assay on
  human liver), PMID:9718352 and PMID:18075467 (expression of variants -> reduced DHP
  activity).
- Core BP = uracil catabolic process (GO:0006212) and pyrimidine nucleobase catabolic
  process (GO:0006208); ACCEPT. thymine catabolic process (GO:0006210) ISS also ACCEPT
  (dihydrothymine is a physiological substrate).
- GO:0008270 zinc ion binding (NAS): ACCEPT, corroborated by PDB 2VR2 structure with 2 Zn.
- Cytosol (GO:0005829) IBA/ISS/TAS + cytoplasm (GO:0005737) IEA: ACCEPT (cytosol precise);
  cytoplasm broad IEA MARK_AS_OVER_ANNOTATED (less precise parent).
- Broad hydrolase MF IEAs (GO:0016787, GO:0016810): parents of GO:0004157;
  MARK_AS_OVER_ANNOTATED (not wrong, but uninformative given the specific activity).
- protein binding (GO:0005515) IPI x2 (PMID:32296183 HuRI binary interactome;
  PMID:32814053 ND Y2H interactome): high-throughput, uninformative bare protein-binding;
  MARK_AS_OVER_ANNOTATED per curation policy (not REMOVE).
- phosphoprotein binding (GO:0051219) IEA (Ensembl Compara from mouse): no functional
  basis in the DHP literature; over-propagated electronic inference -> REMOVE.
- identical protein binding (GO:0042802) ISS: consistent with homotetramer; KEEP_AS_NON_CORE.
- extracellular exosome (GO:0070062) HDA (PMID:19056867 urinary exosome proteome): mass-spec
  detection in urinary exosomes (kidney-expressed); real detection but not the site of
  catalytic function; KEEP_AS_NON_CORE.
