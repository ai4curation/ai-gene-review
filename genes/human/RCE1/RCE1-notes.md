# RCE1 (human) — gene review notes

UniProt: Q9Y256 (FACE2_HUMAN). Gene symbol RCE1 (synonyms FACE2, RCE1A, RCE1B).
HGNC:13721. Chromosome 11. 329 aa.

## Identity and enzyme classification

- RecName in UniProt is "CAAX prenyl protease 2"; also "Farnesylated
  proteins-converting enzyme 2 (FACE-2)", "Prenyl protein-specific endoprotease 2",
  "RCE1 homolog / hRCE1" [file:human/RCE1/RCE1-uniprot.txt "RecName: Full=CAAX prenyl protease 2"].
- EC=3.4.26.1 [file:human/RCE1/RCE1-uniprot.txt "EC=3.4.26.1 {ECO:0000269|PubMed:10085068}"].
  EC subclass 3.4.26 in the IUBMB peptidase nomenclature = **glutamic-type
  endopeptidases**. So EC alone already tells us this is an ENDOpeptidase of the
  glutamic mechanistic class, not a metallo- or cysteine-type protease.
- MEROPS: G05.002; peptidase family/clan **U48** [file:human/RCE1/RCE1-uniprot.txt
  "MEROPS; G05.002"] / [file:human/RCE1/RCE1-uniprot.txt "Belongs to the peptidase U48 family."].
- Pfam PF02517 (Rce1-like); InterPro IPR039731 (Rce1), IPR003675 (Rce1/LyrA-like_dom);
  PANTHER PTHR13046 "PROTEASE U48 CAAX PRENYL PROTEASE RCE1" / SF0 "CAAX PRENYL PROTEASE 2".

## Mechanism — glutamate intramembrane protease (NOT metallo, NOT cysteine)

- RCE1 is a **glutamate-type intramembrane protease**; the yeast/vertebrate structural
  work established a novel IMP class ("glutamate IMPs") with a conserved EExxxR motif;
  a glutamate activates a nucleophilic water and adjacent histidines are catalytically
  required (S. cerevisiae Rce1 E156, H194, H248) [Manolaridis et al. 2013 Nature
  "Mechanism of farnesylated CAAX protein processing by the intramembrane protease
  Rce1", https://www.nature.com/articles/nature12754; Hampton/Dohlman review "Rce1:
  mechanism and inhibition" PMID:29424242; mutational study PMC2937830 requiring
  glutamate and histidine residues].
- Consistent with this, the UniProt feature table lists two catalytic residues as
  "Proton donor/acceptor" (ACT_SITE 175 and 208, by similarity to Q6LZY8) plus two
  transition-state-stabilizer SITE residues (261, 265)
  [file:human/RCE1/RCE1-uniprot.txt "Proton donor/acceptor"] — i.e. general acid/base
  chemistry, not a metal-coordinating HEXXH-type motif.
- Implication for GO MF: the specific mechanistic MF is **glutamic-type peptidase
  activity (GO:0070002)**. (The historically used specific terms — GO:0008319 "prenyl
  protein specific endopeptidase activity", GO:0008487 "prenyl-dependent CAAX protease
  activity", and GO:0070007 "glutamic-type endopeptidase activity" — are all now
  OBSOLETE in the current ontology; verified against local go.db.) Existing GOA MF terms
  that describe the WRONG mechanistic class are: GO:0004222 metalloendopeptidase (IBA,
  IEA) and GO:0004197 cysteine-type endopeptidase (TAS/Reactome). RCE1 is an
  endopeptidase, so GO:0004175 endopeptidase activity is correct-but-general;
  GO:0008238 exopeptidase activity contradicts the endopeptidase EC class.

## Function (what it does)

- Second of the three sequential CAAX post-translational processing steps:
  (1) prenylation of the cysteine (FTase/GGTase-I), (2) **RCE1 proteolysis of the
  C-terminal -AAX tripeptide**, (3) carboxymethylation of the new C-terminal
  prenylcysteine (ICMT) [PMID:10085068 "modification of the cysteine with either a
  15-carbon farnesyl or 20-carbon geranylgeranyl isoprenyl lipid, proteolysis of the
  C-terminal -AAX tripeptide, and methylation of the carboxyl group of the now
  C-terminal prenylcysteine"].
- UniProt FUNCTION: "Proteolytically removes the C-terminal three residues of
  farnesylated and geranylated proteins, leaving the prenylated cysteine as the new
  C-terminus. Is able to process K-Ras, N-Ras, H-Ras, RAP1B and G-gamma-1"
  [file:human/RCE1/RCE1-uniprot.txt "leaving the prenylated cysteine as the new C-"] /
  [file:human/RCE1/RCE1-uniprot.txt "process K-Ras, N-Ras, H-Ras, RAP1B and G-gamma-1"].
- Substrate specificity is for PRENYLATED substrates only: "The protease activity of
  hRCE1 activity was specific for prenylated proteins, because unprenylated peptides
  did not compete for enzyme activity" [PMID:10085068].
- Recombinant hRCE1 processes both farnesylated and geranylgeranylated substrates:
  "farnesyl-Ki-Ras, farnesyl-N-Ras, farnesyl-Ha-Ras, and the farnesylated
  heterotrimeric G protein Ggamma1 subunit, as well as geranylgeranyl-Ki-Ras and
  geranylgeranyl-Rap1b" [PMID:10085068].
- Kinetics: KM = 0.5 uM for farnesyl-Ki-Ras and 0.5 uM for geranylgeranyl-Ki-Ras
  [file:human/RCE1/RCE1-uniprot.txt "KM=0.5 uM for farnesyl-Ki-Ras"].

## Localization

- Endoplasmic reticulum membrane; multi-pass (polytopic) membrane protein
  [file:human/RCE1/RCE1-uniprot.txt "Endoplasmic reticulum membrane"] /
  [file:human/RCE1/RCE1-uniprot.txt "Multi-pass membrane protein"]. UniProt lists 7
  TRANSMEM helices (structural work indicates 8 TMs).
- USP17 and RCE1 co-localize at the ER: "USP17 and RCE1 co-localize at the endoplasmic
  reticulum" [PMID:19188362].
- GOA also carries a plasma-membrane location (TAS/ProtInc PMID:10085068, 2003) and a
  generic "membrane" (HDA, NK-cell membrane proteome PMID:19946888) and a "cytosol"
  (TAS/Reactome R-HSA-5696600). The authoritative subcellular location per UniProt is
  ER membrane; the plasma-membrane call is inconsistent with the current UniProt record
  and the ER localization established by PMID:19188362. Generic "membrane" from a
  large-scale membrane-proteome study is uninformative relative to the specific ER
  membrane term.

## Regulation and physiology (context / non-core)

- Ubiquitinated (K48 and K63 linkages); K48 ubiquitination drives degradation.
  Deubiquitination by USP17L2/USP17 (which removes K63 chains) ABROGATES RCE1
  proteolytic activity toward Ras GTPases [file:human/RCE1/RCE1-uniprot.txt
  "Deubiquitination by USP17L2/USP17 negatively"] and [PMID:19188362 "this effect is
  caused by the loss of RCE1 catalytic activity as a result of its deubiquitination by
  USP17"].
- Because RCE1 processing is required for correct Ras membrane localization and
  activation, loss of RCE1 activity blocks Ras-driven MEK/ERK (RAF/MAP kinase) signaling:
  "USP17 expression blocks Ras membrane localization and activation, thereby inhibiting
  phosphorylation of the downstream kinases MEK and ERK" and "USP17 cannot block
  proliferation or Ras membrane localization in RCE1 null cells" [PMID:19188362].
- Reactome places RCE1 in "RAS processing" and connects it (indirectly, via its Ras
  substrates) to the RAF/MAP kinase cascade [Reactome:R-HSA-9647999; R-HSA-5673001].
  The MAPK-cascade (GO:0000165) annotation is downstream/indirect — RCE1 does not itself
  act in the kinase cascade; it processes the GTPase upstream of it.

## Annotation-review summary (decisions)

MF:
- GO:0008238 exopeptidase activity (IDA, PMID:10085068): MODIFY — the enzyme is an
  ENDOpeptidase (removes an internal -AAX tripeptide; EC 3.4.26.1). "Exopeptidase" is a
  mechanistic mis-class. Experimental, so no REMOVE; propose GO:0070002 (glutamic-type
  peptidase activity) as replacement.
- GO:0004175 endopeptidase activity (IDA, PMID:19188362): ACCEPT (correct, if general);
  the IEA copy (GO_REF:0000117 ARBA) MODIFY to the more specific GO:0070002.
- GO:0004222 metalloendopeptidase activity (IBA GO_REF:0000033; IEA GO_REF:0000002
  InterPro): MODIFY — wrong catalytic class (glutamic, not metallo). Propose GO:0070002.
- GO:0004197 cysteine-type endopeptidase activity (TAS Reactome:R-HSA-9647999): MODIFY —
  wrong catalytic class (glutamic, not cysteine). Propose GO:0070002.

BP:
- GO:0071586 CAAX-box protein processing (IDA PMID:10085068; IMP PMID:19188362; IBA; IEA):
  ACCEPT — this is the core biological process (proteolytic step of CAAX maturation).
- GO:0080120 CAAX-box protein maturation (IEA GO_REF:0000117): KEEP_AS_NON_CORE — broader
  parent process (GO:0071586 is part_of GO:0080120); RCE1 performs only the proteolysis
  substep, not the full maturation.
- GO:0018342 protein prenylation (IDA PMID:10085068): MARK_AS_OVER_ANNOTATED — RCE1 does
  NOT prenylate; it acts AFTER prenylation. Prenylation is done by FTase/GGTase-I. The
  IDA here appears to conflate "CAAX processing" with "prenylation".
- GO:0000165 MAPK cascade (TAS Reactome:R-HSA-5673001): KEEP_AS_NON_CORE — indirect/
  downstream; RCE1 processes Ras upstream of the cascade but is not itself a cascade
  component.

CC:
- GO:0005789 endoplasmic reticulum membrane (IDA PMID:19188362; IBA; IEA; TAS Reactome x2):
  ACCEPT — authoritative core location.
- GO:0016020 membrane (HDA PMID:19946888): KEEP_AS_NON_CORE — correct but uninformative;
  subsumed by ER membrane.
- GO:0005829 cytosol (TAS Reactome:R-HSA-5696600): MARK_AS_OVER_ANNOTATED — RCE1 is a
  polytopic ER membrane protein; the Reactome cytosol placement reflects the reaction
  compartment abstraction, not RCE1 residence.
- GO:0005886 plasma membrane (TAS ProtInc PMID:10085068): MARK_AS_OVER_ANNOTATED — the
  current UniProt record localizes RCE1 to ER membrane; a 2003 ProtInc PM call is not
  supported and likely reflects its Ras substrates' destination rather than RCE1 itself.
  (Experimental? No — this is TAS, author statement; not IDA/IMP.)
</content>
