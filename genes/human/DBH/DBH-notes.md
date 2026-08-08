# DBH (Dopamine beta-hydroxylase) — Review Notes

UniProt: P09172 (DOPO_HUMAN). Gene: DBH. HGNC:2689. Chromosome 9q34.2.
Taxon: Homo sapiens (NCBITaxon:9606).

## Core identity and reaction

DBH = dopamine beta-hydroxylase / dopamine beta-monooxygenase; EC 1.14.17.1.
It catalyzes the penultimate step of catecholamine biosynthesis: hydroxylation of
dopamine at the beta-carbon to give (R)-noradrenaline (norepinephrine).

Catalytic activity (from UniProt CATALYTIC ACTIVITY, RHEA:19117):
"dopamine + 2 L-ascorbate + O2 = (R)-noradrenaline + 2 monodehydro-L-ascorbate
radical + H2O" [file:human/DBH/DBH-uniprot.txt "dopamine + 2 L-ascorbate + O2 = (R)-noradrenaline + 2"].

- Cofactor: Cu(2+). "Binds 2 copper ions per subunit" (CuH electron-transfer site;
  CuM dioxygen-binding/substrate-hydroxylation site) [file:human/DBH/DBH-uniprot.txt
  "Binds 2 copper ions per subunit"]. Confirmed by crystal structure
  [PMID:27152332 "requires two type 2 bound copper ions per subunit to be active"].
- Electron donor: ascorbate (vitamin C). "The reaction also requires two electrons
  provided by two ascorbate molecules" [PMID:27152332 "The reaction also requires
  two electrons provided by two ascorbate molecules"]. UniProt keyword "Vitamin C".
- KW: Copper; Metal-binding; Monooxygenase; Oxidoreductase; Vitamin C;
  Catecholamine biosynthesis.

Family: copper type II, ascorbate-dependent monooxygenase family (with PHM/PAM,
MOXD1, insect TBH) [file:human/DBH/DBH-uniprot.txt "Belongs to the copper type II
ascorbate-dependent monooxygenase family"].

## Function evidence (experimental)

- FUNCTION: "Catalyzes the hydroxylation of dopamine to noradrenaline (also known as
  norepinephrine)" [file:human/DBH/DBH-uniprot.txt "Catalyzes the hydroxylation of
  dopamine to noradrenaline"]. ECO:0000269 from PubMed:27148966, 3443096, 7961964, 8546710.
- PMID:8546710 (Li et al. 1996, Biochem J): recombinant human DBH expressed in
  Drosophila S2 cells and native neuroblastoma DBH purified and compared; enzyme
  activity/kinetics (KM tyramine 1.8 mM). Most activity secreted into culture fluid.
  Basis of EXP/IDA GO:0004500 and the "secreted/extracellular" annotations.
  full_text_available: false (abstract only).
- PMID:7961964 (Kobayashi et al. 1994, JBC): high-level functional expression of human
  DBH in transgenic mice; "existed in the secretory vesicles as both soluble and
  membrane-bound forms" [PMID:7961964 "existed in the secretory vesicles as both
  soluble and membrane-bound forms"]; "catalytically active human DBH enzyme"
  [PMID:7961964 "catalytically active human DBH enzyme"]. Basis of IDA GO:0004500,
  copper binding, secretory granule membrane/lumen, extracellular, dopamine
  catabolic process. Abstract only.
- PMID:3443096 (Lamouroux et al. 1987, EMBO J): cloning + primary structure of human
  DBH from pheochromocytoma; antibodies "precipitate DBH activity"; membrane-bound
  and soluble forms. Basis of IDA GO:0004500 and dopamine catabolic process. Abstract only.
- PMID:27152332 (Vendelboe et al. 2016, Sci Adv): 2.9 Å crystal structure of human DBH
  (PDB 4ZEL); IDA copper ion binding. DOMON domain + CuH/CuM catalytic core +
  dimerization domain; two type-2 coppers per subunit; ascorbate-dependent
  glycoprotein. full_text_available: true.
- PMID:27148966 (Cubells et al. 2016, PLoS ONE): human DBH BAC fully rescues all Dbh
  -/- mouse phenotypes and "restored normal catecholamine levels" [PMID:27148966
  "restored normal catecholamine levels to the peripheral organs and brain of"].
  Basis of IMP norepinephrine biosynthetic process. full_text_available: true.

## Localization

Secretory (chromaffin) granules / synaptic vesicles of noradrenergic and adrenergic
cells; exists as membrane-bound and soluble forms; soluble form is secreted with
catecholamines by exocytosis.
- UniProt SUBCELLULAR LOCATION: secretory vesicle lumen; chromaffin granule lumen;
  Secreted; secretory vesicle membrane (Single-pass type II membrane protein);
  chromaffin granule membrane.
- Reactome R-HSA-209891: "The enzyme exists in the secretory vesicles as both soluble
  and membrane-bound forms. The soluble form is secreted with catecholamines by
  exocytosis whereas the membrane-bound form is recycled into the vesicles."
- Topology: N-terminal cytoplasmic (1-16), TM signal-anchor (17-37), intragranular
  lumenal domain (38-617). Type II single-pass membrane protein; proteolytic cleavage
  after the anchor releases the soluble form.

## Physiology / disease

- DBH deficiency = Orthostatic hypotension 1 (ORTHYP1; MIM:223360), autosomal
  recessive. Noradrenaline and adrenaline undetectable; dopamine elevated.
  [PMID:2880016 "Noradrenaline and adrenaline were undetectable in plasma, urine,
  and cerebrospinal fluid (CSF), but dopamine was 7-fold to 12-fold normal"];
  [PMID:2880016 "Dopamine-beta-hydroxylase was undetectable in plasma and CSF"].
  Pathogenic variants V101M, D114E, D345N [file:human/DBH/DBH-uniprot.txt
  "VARIANTS ORTHYP1 MET-101; GLU-114 AND ASN-345"].
- Dbh -/- mice: embryonic lethality, cold intolerance (impaired BAT thermogenesis via
  UCP1), behavioral defects. [PMID:9139828 "unable to induce thermogenesis in brown
  adipose tissue through uncoupling protein (UCP1)"]. Basis of the ISS/IEA
  "positive regulation of cold-induced thermogenesis" — a downstream physiological
  consequence of NE deficiency, not DBH's direct molecular action; kept non-core.

## Interactions (protein binding IPIs)

- ATP7A (Q04656) — [PMID:26199316] dysbindin/BLOC-1–ATP7A copper pathway.
  ATP7A is the copper transporter that loads copper into the secretory pathway;
  physiologically relevant to DBH cofactor supply, but the GO term captured is the
  bare, uninformative GO:0005515 "protein binding".
- HuRI (PMID:32296183) and the neurodegenerative-disease Y2H interactome
  (PMID:32814053) contribute a large set of bare "protein binding" IPIs (NOTCH2NLC,
  ALDH1A1, KRT19, PIK3R1, HNRNPK, etc.). High-throughput; no functional MF meaning.
  These are the IntAct partners listed in the UniProt INTERACTION block.

## Curation summary

Core MF: dopamine beta-monooxygenase activity (GO:0004500); copper ion binding
(GO:0005507); L-ascorbic acid binding (GO:0031418).
Core BP: norepinephrine biosynthetic process (GO:0042421).
Core CC: secretory granule membrane (GO:0030667); secretory granule lumen
(GO:0034774); chromaffin granule membrane (GO:0042584); extracellular region/space
(secreted soluble form).

Non-core kept: dopamine catabolic process (GO:0042420) — same reaction viewed as
substrate consumption; positive regulation of cold-induced thermogenesis (downstream
NE physiology); locomotory behavior, behavioral response to ethanol, chemical
synaptic transmission (all downstream NE-dependent behaviors from ortholog/TAS).
Over-annotations: bare "protein binding" IPIs; generic "catalytic activity",
"monooxygenase activity", "membrane", "cytoplasm".
