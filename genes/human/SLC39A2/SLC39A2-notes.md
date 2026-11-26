# SLC39A2 (ZIP2) curation notes

UniProt: Q9NP94 (S39A2_HUMAN), 309 aa, multi-pass membrane protein, 8 TM helices.
HGNC:17127. Gene also known as ZIP2. Member of the ZIP transporter (SLC39/TC 2.A.5) family.

## Core function
ZIP2 is a plasma-membrane **zinc influx (import) transporter**: it moves Zn2+ from the
extracellular space into the cytosol. ZIP = import (into cytosol), distinct from the ZnT/SLC30
family which exports zinc out of the cytosol. Direction matters for directional transport terms.

- UniProt FUNCTION: "Mediates the influx of Zn(2+) into cells from extracellular space."
  "The Zn(2+) uniporter activity is independent of H(+)-driving force, but is modulated by
  extracellular pH and membrane potential." Polyspecific: "Also transports other divalent cations
  Zn(2+), Cd2(+), Cu2(+), Co2(+) in the order of decreasing affinity."
  [file:human/SLC39A2/SLC39A2-uniprot.txt CC:FUNCTION]
- CATALYTIC ACTIVITY Rhea:RHEA:29351 Zn(2+)(in) = Zn(2+)(out), physiological direction right-to-left
  (= import). Also Cd(2+) (RHEA:28707).
- Km Zn2+ = 3 uM (PMID:10681536); Km Cd2+ ~1.5 uM (PMID:29791142, PMID:30914478).

## Key literature
- PMID:10681536 (Gaither & Eide 2000): first functional expression of hZIP2; Zn uptake, Km 3uM,
  originally proposed Zn/HCO3- symport (now superseded). PM localization. Expressed in prostate/
  uterine epithelium. Abstract-only in cache.
- PMID:29791142 (Franz 2018): reassessment — ZIP2 is a facilitated divalent metal-ion transporter,
  modulated by extracellular pH and voltage, INDEPENDENT of H+ driving force and HCO3-. Substrate
  order Zn2+ > Cd2+ >= Cu2+ > Co2+; Fe2+ NOT transported. Full text available.
  "we propose that ZIP2 is a facilitated divalent metal ion transporter that can be modulated by
  extracellular pH and membrane potential."
- PMID:30914478 (Gyimesi 2019): structural elements of pH sensitivity + substrate binding;
  mutagenesis of His63 (pH sensor), His175/Glu179/His202/Lys203/Glu276 (transport); Cd Km 1.46uM.
  Full text available.
- PMID:14612438 (Kim 2004): **about mZIP4/hZIP4 (SLC39A4)**, Zn-stimulated endocytosis to vesicles.
  Does NOT assay ZIP2. The GO:0031410 cytoplasmic-vesicle IDA on SLC39A2 citing this paper looks
  like a cross-gene transfer (ZIP4 -> ZIP2). ZIP2 itself is established as a plasma-membrane
  transporter; vesicle localization is not a documented ZIP2 feature.
- PMID:20148757: "Intensive therapies for mantle cell lymphoma" — a lymphoma-therapy REVIEW with no
  relation to zinc transport. Cited as IMP for GO:0005385 (MF) and IDA for GO:0005886 (PM). This is
  a mis-keyed reference (WRONG_REFERENCE). The terms themselves are correct and amply supported by
  other rows; only the citation is wrong. Correct paper unknown (candidate: PMID:10681536).
- PMID:32296183 (Luck 2020, HuRI): high-throughput binary (Y2H) interactome. Source of ~44 bare
  GO:0005515 protein-binding IPI rows (AQP1, AQP6, membrane proteins, etc.). Uninformative per the
  protein-binding policy -> REMOVE.

## Tissue / disease
Expressed in prostate and uterine (and skin/esophagus/seminal vesicle per HPA) epithelium.
Mouse ortholog implicated in keratinocyte differentiation in epidermis (By similarity) — indirect
role via zinc supply; ZIP2 does zinc import, it does not execute differentiation. KEEP_AS_NON_CORE.

## Term calls summary
- Core MF: GO:0005385 zinc ion transmembrane transporter activity (ACCEPT).
- Broad polyspecific divalent-metal transport: GO:0046873 (ACCEPT; Cd/Cu/Co demonstrated).
- Core BP: GO:0071578 zinc ion import across plasma membrane (ACCEPT). GO:0071577 (zinc
  transmembrane transport) MODIFY->GO:0071578 (directional import is the supported mechanism);
  GO:0006829 zinc ion transport MODIFY->GO:0071577/import.
- Core CC: GO:0005886 plasma membrane (ACCEPT).
- Generic parents TOO_GENERAL: GO:0016020 membrane, GO:0030001 metal ion transport,
  GO:0055085 transmembrane transport.
- GO:0070574 cadmium transmembrane transport (KEEP_AS_NON_CORE; genuine secondary toxic substrate).
- GO:0030216 keratinocyte differentiation (KEEP_AS_NON_CORE; indirect via zinc supply).
- GO:0031410 cytoplasmic vesicle (MARK_AS_OVER_ANNOTATED; from a ZIP4 paper, WRONG_REFERENCE).
