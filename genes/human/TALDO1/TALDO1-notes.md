# TALDO1 (human) review notes

UniProtKB: P37837 (TALDO_HUMAN). Gene: TALDO1 (HGNC:11559; synonyms TAL, TALDO, TALDOR). 337 aa. Chromosome 11p15.4-p15.5.

## Core biology

TALDO1 is **transaldolase** (EC 2.2.1.2), the enzyme catalysing the rate-limiting
step of the **non-oxidative branch of the pentose phosphate pathway (PPP)**. It
transfers a three-carbon dihydroxyacetone unit between sugar phosphates via a
Schiff-base intermediate on an active-site lysine, catalysing the reversible reaction:

sedoheptulose-7-phosphate + D-glyceraldehyde-3-phosphate <-> erythrose-4-phosphate + beta-D-fructose-6-phosphate

[UniProt FUNCTION: "Catalyzes the rate-limiting step of the non-oxidative phase in the pentose phosphate pathway. Catalyzes the reversible conversion of sedoheptulose-7-phosphate and D-glyceraldehyde 3-phosphate into erythrose-4-phosphate and beta-D-fructose 6-phosphate"]. Rhea:RHEA:17053; ChEBI substrates/products CHEBI:16897, 57483, 57634, 59776. UniPathway UPA00115/UER00414.

This links the PPP back to glycolytic intermediates (F6P, GA3P), allowing the cell to
balance ribose-5-phosphate production (for nucleotides) with NADPH generation via the
oxidative branch, and to recycle sugar phosphates back into glycolysis/gluconeogenesis.

Active site: ACT_SITE 106 (proton donor/acceptor), ACT_SITE 142 (nucleophile; Schiff-base
intermediate with substrate). Belongs to transaldolase family, Type 1 subfamily. TIM-barrel
fold (Gene3D 3.20.20.70). Homodimer (PDB 1F05, PMID:10869557).

## Catalytic activity evidence (experimental)

- PMID:8955144 (Banki 1996): TAL is "a key enzyme of the reversible nonoxidative branch of
  the pentose phosphate pathway (PPP)". Overexpression/knockdown of TAL in Jurkat cells shifts
  the balance between oxidative and non-oxidative PPP branches, altering NADPH and GSH levels
  and apoptosis sensitivity. FUNCTION + CATALYTIC ACTIVITY cited by UniProt (EC 2.2.1.2).
- PMID:18687684 (Schneider 2008): F->Y active-site mutation confers fructose-6-phosphate
  aldolase activity; "we show that a homologous replacement has a similar effect in the human
  transaldolase Taldo1 (aldolase activity, 14 units/mg)". Confirms human TALDO1 transaldolase
  activity biochemically (basis of the IDA on GO:0004801). Also cited by UniProt for EC 2.2.1.2.
- PMID:18498245 (Qian 2008): TAL-deficient (TALDeltaS171) human lymphoblasts — "Sedoheptulose
  7-phosphate was accumulated, whereas G6P (glucose 6-phosphate) was depleted". Loss-of-function
  evidence tying TALDO1 to the non-oxidative PPP (basis of FlyBase IMP annotations to
  GO:0004801 and GO:0009052). Note the annotations are attributed to human TALDO1 by FlyBase;
  the human TALDeltaS171 patient-cell metabolic phenotype directly supports the enzyme role.

## Localization

- Cytosol / cytoplasm: strongly supported. UniProt SUBCELLULAR LOCATION: cytoplasm; Reactome
  places transaldolase in cytosol; FlyBase IDA GO:0005829 (PMID:18498245). This is the primary
  site of PPP metabolism.
- Nucleus: isoform 1 shuttles between nucleus and cytoplasm via importin alpha/beta (KPNA1/KPNA4)
  and CRM1 export; N-terminal 10 aa are the NLS (By similarity to rat Q93092; PMID:27703206
  describes two isoforms with differential nucleocytoplasmic distribution). Nuclear localization
  is real but represents a regulatory/moonlighting distribution rather than the site of the core
  catalytic PPP function; IBA is_active_in nucleus is over-broad for the core function.
- Extracellular exosome (GO:0070062, HDA): high-throughput proteomic detection in exosome
  preparations (PMID:23533145 prostatic secretion exosomes; PMID:20458337 B-cell exosomes).
  Cytosolic metabolic enzymes are commonly co-purified in exosome proteomes; not a functional
  location for transaldolase catalysis. Keep as non-core.

## Protein-binding IPIs (all bare GO:0005515)

- PMID:21044950 (TERF2IP/RAP1, Q9NYB0): BiFC telomere-interactome screen — TALDO1 flagged as a
  candidate telomeric interactor; large-scale screen, not a characterized functional interaction.
- PMID:32814053 (HTT, P42858): neurodegenerative-disease Y2H interactome map. UniProt lists both
  HTT and TERF2IP IntAct interactions.
- PMID:25854864 (BAP31/BCAP31, listed as Q77YB1 in GOA WITH/FROM): BAP31 interaction study
  (RSV SH protein). AgBase IPI.
These are all uninformative "protein binding" and derive from high-throughput/interactome data.
Per curation policy, mark as over-annotated rather than removed (do not assert wrong-gene).

## Disease

Transaldolase deficiency (TALDOD; MIM 606003), autosomal recessive. Variants: Ser171del
(VAR_011511; PMID:11283793 — "liver cirrhosis associated with a new inborn error in the pentose
phosphate pathway") and R192C (VAR_086514; PMID:25388407). Clinical: growth retardation,
dysmorphism, cutis laxa, congenital heart disease, hepatosplenomegaly, liver cirrhosis/fibrosis,
telangiectases, pancytopenia/thrombocytopenia, hemolytic anemia, bleeding tendency; often
neonatal/infantile onset. Elevated polyols (erythritol, arabitol) and sedoheptulose in body fluids.

## Curation decisions summary

- Core MF: GO:0004801 transaldolase activity (accept IBA, IDA, IMP, EXP; IEA/TAS accept).
- Core BP: GO:0009052 pentose-phosphate shunt, non-oxidative branch (accept IBA/IMP/IEA).
  GO:0006098 pentose-phosphate shunt (parent) accept as IEA.
- CC: cytosol GO:0005829 core (accept IDA/TAS/IEA). cytoplasm GO:0005737 accept (broader).
- nucleus GO:0005634: keep as non-core (regulatory shuttling / proteomics), not core catalytic site.
- extracellular exosome GO:0070062: keep as non-core (proteomic co-purification).
- GO:0006002 fructose 6-phosphate metabolic process, GO:0019682 glyceraldehyde-3-phosphate
  metabolic process (Ensembl IEA): accept — these are the substrate/product metabolic processes
  of the transaldolase reaction, correct but redundant with the PPP terms; keep as non-core-ish/accept.
- GO:0030246 carbohydrate binding, GO:0048029 monosaccharide binding (Ensembl IEA): the enzyme
  binds sugar-phosphate substrates, but these binding terms are uninformative relative to
  transaldolase activity; mark as over-annotated.
- GO:0005975 carbohydrate metabolic process (InterPro IEA, ProtInc TAS): correct but very general
  parent of PPP; accept (IEA allowed to be broad) / non-core.
- protein binding IPIs: MARK_AS_OVER_ANNOTATED (uninformative, HT interactome).
