# HMOX2 (Heme oxygenase 2, HO-2) review notes

UniProt: P30519 (HMOX2_HUMAN), 316 aa, human (NCBITaxon:9606). HGNC:5014. EC 1.14.14.18.

## Core biology

HMOX2 encodes heme oxygenase 2 (HO-2), one of the two mammalian heme oxygenase
isozymes. Unlike the stress-inducible HMOX1 (HO-1), HO-2 is **constitutively**
expressed and is the predominant isoform in brain, testis and vascular
endothelium. It is a heme-degrading oxidoreductase anchored in the endoplasmic
reticulum (microsomal) membrane by a single C-terminal transmembrane helix, with
the catalytic domain facing the cytoplasm.

### Molecular function / catalytic activity

HO-2 catalyzes the oxidative cleavage of heme at the alpha-methene bridge carbon,
using O2 and reducing equivalents delivered by NADPH--cytochrome P450 (hemoprotein)
reductase, to produce biliverdin IXalpha, carbon monoxide (CO) and free ferrous
iron (Fe2+).

- UniProt FUNCTION: "Catalyzes the oxidative cleavage of heme" ... "at the
  alpha-methene bridge carbon, released as carbon monoxide (CO)," ... "to generate
  biliverdin IXalpha, while releasing the central heme iron chelate as ferrous iron"
  [file:human/HMOX2/HMOX2-uniprot.txt, ECO:0000269|PubMed:1575508, ECO:0000269|PubMed:7890772].
- CATALYTIC ACTIVITY / Rhea RHEA:21764, EC=1.14.14.18: heme b + 3 reduced
  [NADPH--hemoprotein reductase] + 3 O2 = biliverdin IXalpha + CO + Fe(2+) + ...
  [file:human/HMOX2/HMOX2-uniprot.txt].
- HO-2 heme oxygenase activity was demonstrated directly for the purified recombinant
  human protein: the tryptic fragment "retained the ability to accept electrons from
  NADPH-cytochrome P-450 reductase and the enzymatic activity for conversion of heme to
  biliverdin" [PMID:7890772 "retained the ability to accept electrons from
  NADPH-cytochrome P-450 reductase and the enzymatic activity for conversion of heme to
  biliverdin"]. The catalytic mechanism is similar to HO-1: "the catalytic mechanism of
  heme oxygenase-2 appears to be similar to that of heme oxygenase-1" [PMID:7890772].
- The E. coli-expressed human HO-2 fusion protein "displayed significant heme oxygenase
  activity, which was inhibited by Zn- and Sn-protoporphyrins, known inhibitors of
  eukaryotic heme oxygenase" [PMID:1575508]. UniProt ACTIVITY REGULATION: "Inhibited by
  metalloporphyrins such as Sn- and Zn-" protoporphyrins
  [file:human/HMOX2/HMOX2-uniprot.txt].

Supporting IDA GO annotations: GO:0004392 heme oxygenase (decyclizing) activity
from both PMID:7890772 and PMID:1575508 (both ECO:0000314 IDA).

### Heme binding

HO-2 binds one heme b as substrate; the crystal structure of a truncated human HO-2
(PMID:17965015) defined heme-binding sites, with His45 as the axial (proximal)
iron-binding residue and additional heme-b contacts at residues 154, 199, 203
[file:human/HMOX2/HMOX2-uniprot.txt, BINDING features]. The purified tryptic fragment
"bound one equivalent of heme to form a substrate-enzyme complex" and spectroscopy
indicated "a neutral imidazole of a histidine residue served as the proximal ligand"
[PMID:7890772]. GO:0020037 heme binding (IBA) is well supported.

Note on heme-regulatory motifs: UniProt annotates two HRM repeats (residues 264-269
"HRM 1", 281-286 "HRM 2") [file:human/HMOX2/HMOX2-uniprot.txt, REPEAT features]. These
Cys-Pro motifs are a distinctive feature of HO-2 (absent from HO-1) and are proposed to
confer thiol/heme redox and CO/O2-sensing regulation, but the current GOA set does not
carry a specific HRM/regulatory-heme-binding annotation.

### Biological process

- Heme catabolism: GO:0042167 heme catabolic process and GO:0006788 heme oxidation
  (both from the enzymatic reaction). HO-2 is the constitutive contributor to endogenous
  heme turnover and is the physiological source of CO. Reactome R-HSA-189398 "HMOX1
  dimer, HMOX2 cleave heme" / R-HSA-189483 "Heme degradation": "Heme oxygenases (HMOXs)
  cleaves the heme ring at the alpha-methene bridge to form bilverdin. This reaction
  forms the only endogenous source of carbon monoxide. ... HMOX2 is non-inducible."
  [reactome/R-HSA-189398.md].

- O2 sensing / response to hypoxia: HO-2 acts as an oxygen sensor for large-conductance
  calcium-activated (BK) K+ channels. "We demonstrate that hemoxygenase-2 (HO-2) is part
  of the BK channel complex and enhances channel activity in normoxia. Knockdown of HO-2
  expression reduced channel activity, and carbon monoxide, a product of HO-2 activity,
  rescued this loss of function." and "HO-2 is an oxygen sensor that controls channel
  activity during oxygen deprivation" [PMID:15528406]. This underpins the GO:0001666
  response to hypoxia IDA annotation and the GO:0005515 protein binding IPI to the BK
  channel alpha subunit (KCNMA1, UniProtKB:Q12791). The plasma-membrane IDA
  (GO:0005886) in the same paper reflects HO-2 being detected in / recruited to the BK
  channel complex at the plasma membrane in the heterologous HEK293 system, not the
  enzyme's principal ER-membrane residence.

- Response to oxidative stress: GO:0006979 (IBA) is a family-level inference. It is more
  strongly established for HO-1 (the inducible, cytoprotective antioxidant isoform); for
  HO-2 the antioxidant/cytoprotective role is real but secondary to its constitutive
  catabolic/CO-producing role. Kept as non-core.

### Subcellular location

- Endoplasmic reticulum / microsomal membrane, single-pass type IV membrane protein,
  cytoplasmic side [file:human/HMOX2/HMOX2-uniprot.txt SUBCELLULAR LOCATION: "Microsome
  membrane" ... "Endoplasmic reticulum membrane" ... "Single-pass type IV membrane
  protein" ... "Cytoplasmic side"]. This is the core catalytic location.
  GO:0005789 endoplasmic reticulum membrane (ISS, IEA, TAS) — ACCEPT/core.
- GO:0016020 membrane (HDA, PMID:19946888) — a large-scale NK-cell membrane-proteome MS
  study; correct but generic; kept as non-core.
- GO:0005886 plasma membrane (IBA; IDA PMID:15528406; TAS Reactome) — HO-2 can be found
  at the plasma membrane in the BK channel complex context; the IBA/TAS generic
  plasma-membrane rows are over-general relative to the ER-membrane core; treated as
  non-core / over-annotation.
- GO:0035579 specific granule membrane (TAS Reactome R-HSA-6799350, neutrophil
  degranulation) — Reactome places HO-2 in the neutrophil specific-granule / degranulation
  cargo set; peripheral relative to the enzyme's ER function; kept as non-core.

### S-nitrosylation / post-translational regulation

HO-2 is S-nitrosylated at Cys265 and Cys282 (within/near the HRM region) by BLVRB
[file:human/HMOX2/HMOX2-uniprot.txt PTM: "S-nitrosylated by BLVRB",
ECO:0000269|PubMed:38056462]. A soluble form arises by proteolytic removal of the
membrane anchor [file:human/HMOX2/HMOX2-uniprot.txt PTM].

## Protein-binding (IPI) annotations

Three GO:0005515 protein binding IPI sources:
- PMID:15528406 (WITH UniProtKB:Q12791 = KCNMA1/BK channel alpha) — biologically
  meaningful HO-2 interaction underpinning O2 sensing. Per policy, bare protein binding
  IPI is marked MARK_AS_OVER_ANNOTATED (uninformative MF term) but the interaction itself
  is real and captured in core-function context (BK channel / O2 sensing).
- PMID:32296183 (HuRI, systematic binary interactome) and PMID:32814053 (neurodegenerative
  disease interactome Y2H) — high-throughput interactome screens producing long,
  heterogeneous partner lists (many ER/membrane proteins, e.g. GET1/O00258, MGST3/O14880,
  SGPL1/O95470, etc.). These are generic "protein binding" rows with no specific functional
  MF; MARK_AS_OVER_ANNOTATED (never REMOVE per policy for IPI protein binding).

## Distinctions from HMOX1 (paralog)

- HMOX1 (HO-1): stress-inducible, cytoprotective/antioxidant, broadly expressed on
  induction; forms ER dimers/oligomers.
- HMOX2 (HO-2): constitutive, abundant in brain/testis/endothelium, harbors HRMs,
  functions in physiological CO production and O2 sensing. Same catalytic reaction.
  Reactome: "HMOX1 is inducible ... HMOX2 is non-inducible." [reactome/R-HSA-189398.md].

## Core function summary

- MF: GO:0004392 heme oxygenase (decyclizing) activity (with GO:0020037 heme binding).
- BP: GO:0042167 heme catabolic process; GO:0006788 heme oxidation.
- CC: GO:0005789 endoplasmic reticulum membrane.
- Additional physiological role: O2 sensing via CO production and BK-channel modulation
  (GO:0001666 response to hypoxia), retained as a secondary/non-core but well-evidenced
  function.
</content>
</invoke>
