# SLC25A38 review notes

UniProt: Q96DW6 (S2538_HUMAN), 304 aa, human. HGNC:26054. Gene on chr 3.

## Identity and family
- SLC25A38 is a member of the mitochondrial carrier (SLC25 / TC 2.A.29) family, "SLC25A38 subfamily"
  [file:human/SLC25A38/SLC25A38-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29) family. SLC25A38 subfamily"].
- Three tandem Solcar (mitochondrial carrier) repeats and six predicted transmembrane helices
  (TRANSMEM 31-56, 89-115, 127-152, 180-203, 219-245, 274-292); classic 6-TM mitochondrial carrier
  architecture (multi-pass inner-membrane transporter). Pfam Mito_carr x3, PROSITE SOLCAR x3, Gene3D
  mitochondrial carrier domain.
- UniProt RecName: "Mitochondrial glycine transporter"; yeast orthologue is Hem25p; also called GlyC
  [file:human/SLC25A38/SLC25A38-uniprot.txt "AltName: Full=Mitochondrial glycine transporter GlyC"].
- HAMAP-Rule MF_03064 defines the SLC25A38 subfamily.

## Molecular function — glycine transport
- UniProt FUNCTION: "Mitochondrial glycine transporter that imports glycine into the mitochondrial matrix"
  [file:human/SLC25A38/SLC25A38-uniprot.txt "Mitochondrial glycine transporter that imports glycine into"].
- CATALYTIC ACTIVITY (a transport reaction, not enzymatic): glycine(in) = glycine(out) (Rhea RHEA:70715,
  ChEBI:57305), evidence PubMed:27476175. This is a facilitated-transport reaction; SLC25A38 is a
  transporter, NOT a catalytic enzyme — do not assign an enzymatic MF.
- PMID:27476175 (Lunetti et al. 2016, J Biol Chem) biochemically characterized reconstituted human
  SLC25A38 and yeast Hem25p as glycine carriers; hem25Δ has reduced ALA/heme/cytochromes, rescued by
  human SLC25A38 [PMID:27476175 "providing evidence that they are mitochondrial carriers for glycine";
  "Hem25p and its human orthologue SLC25A38 are the main mitochondrial glycine transporters required for
  heme synthesis, providing definitive evidence of their previously proposed glycine transport function"].
  This is the IMP/direct experimental basis for GO:0015187 (glycine transmembrane transporter activity)
  and GO:1904983 (glycine import into mitochondrion).
- Best-supported core MF: **GO:0015187 glycine transmembrane transporter activity** (specific;
  IMP from PubMed:27476175; also IBA and IEA). GOA/UniProt do NOT assign a more specific term; this is
  the correct, most-specific MF. (Verified current label via OLS: "glycine transmembrane transporter
  activity".)

## Biological process
- **GO:1904983 glycine import into mitochondrion** — the directional transport process; IMP from
  PubMed:27476175, also IBA/IEA. Verified OLS label: "glycine import into mitochondrion" ("glycine is
  transported from the cytosol into the mitochondrial matrix").
- **GO:0006783 heme biosynthetic process** — SLC25A38 provides the glycine substrate for the first,
  committed step of heme biosynthesis (glycine + succinyl-CoA -> 5-aminolevulinate / ALA, by ALA synthase)
  in the matrix [file:human/SLC25A38/SLC25A38-uniprot.txt "the condensation of"]; abstract of
  PMID:27476175 "glycine is condensed with succinyl coenzyme A to yield δ-aminolevulinic acid".
  PMID:19412178 "demonstrate that SLC25A38 is important for the biosynthesis of heme in eukaryotes"
  (TAS in GOA). Core BP.
- **GO:0030218 erythrocyte differentiation** — SLC25A38 is erythroid-specific and required during
  erythropoiesis [file:human/SLC25A38/SLC25A38-uniprot.txt "Required during erythropoiesis"];
  loss causes ineffective erythropoiesis / sideroblastic anemia. IMP from PubMed:19412178. This is a
  downstream/physiological role (the gene's molecular job is glycine import for heme); keep as non-core
  process context. Note: GO:0030218 label is "erythrocyte differentiation"; SLC25A38's role is really
  supplying heme for hemoglobinization during erythroid maturation rather than driving the
  differentiation program per se — retained as a valid physiological-context annotation.

## Cellular component
- **GO:0005743 mitochondrial inner membrane** — UniProt SUBCELLULAR LOCATION "Mitochondrion inner
  membrane; Multi-pass membrane protein" [file:human/SLC25A38/SLC25A38-uniprot.txt "Mitochondrion inner
  membrane"]. Correct core location (ISS from Q91XD8 mouse orthologue; IEA). Six TM helices consistent
  with multi-pass inner-membrane carrier.
- **GO:0005739 mitochondrion** — general parent of the above; IBA and HTP (PMID:34800366 high-confidence
  mitochondrial proteome). True but less specific than GO:0005743. HTP proteomic localization to
  mitochondria is corroborating. Keep as non-core (subsumed by inner membrane).
- **GO:0016020 membrane** — very general (IEA, UniRule); true but uninformative; over-annotation relative
  to the specific inner-membrane term.

## Disease
- SIDBA2: Anemia, sideroblastic, 2, pyridoxine-refractory (MIM:205950), autosomal recessive
  [file:human/SLC25A38/SLC25A38-uniprot.txt "Anemia, sideroblastic, 2, pyridoxine-refractory (SIDBA2)"].
  SIDBA2 variants (Glu-130, His-134, Pro-187, His-209) reported in PubMed:19412178. Consistent with a
  loss of mitochondrial glycine import -> impaired heme synthesis -> ring sideroblasts.

## Other functional claims (not in GOA)
- UniProt records a second FUNCTION as pro-apoptotic protein ("Appoptosin") based on ECO:0000250
  (sequence similarity to mouse Q91XD8) and induction in Alzheimer brain (PubMed:23115192, INDUCTION only).
  This is by-similarity / correlational, not an experimentally established human MF, and not in GOA; not
  reviewed as an existing annotation here.

## PMID:34800366 note
Large mitochondrial-proteome paper (Morgenstern et al. 2021, Cell Metab). full_text_available: true, but
SLC25A38 is not named in the extracted body text (it appears in the supplementary dataset underlying the
HTP annotation); no verbatim quote available. Localization to mitochondria is consistent with the
carrier's known inner-membrane residence.

## Action summary rationale
- Core MF: GO:0015187 (glycine transmembrane transporter activity).
- Core BP: GO:1904983 (glycine import into mitochondrion), GO:0006783 (heme biosynthetic process).
- Core CC: GO:0005743 (mitochondrial inner membrane).
- Non-core / context: GO:0005739 mitochondrion (general), GO:0030218 erythrocyte differentiation (physiological outcome).
- Over-annotated: GO:0016020 membrane (uninformative general CC).
