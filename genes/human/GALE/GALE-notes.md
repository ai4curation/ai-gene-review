# GALE (human) — curation notes

UniProtKB: Q14376 (GALE_HUMAN), HGNC:4116, 348 aa. Gene on chromosome 1.

## Core biology (from UniProt Q14376, verified)

GALE is the cytosolic, NAD+-dependent UDP-galactose 4-epimerase (galactowaldenase)
catalysing the **fourth (recycling) step of the Leloir pathway** of galactose
catabolism. It is a **bifunctional** enzyme:

- EC 5.1.3.2 — reversible epimerization of **UDP-alpha-D-glucose <-> UDP-alpha-D-galactose**
  (Rhea:RHEA:22168). This regenerates UDP-glucose consumed by GALT and supplies
  UDP-galactose for glycoconjugate synthesis.
- EC 5.1.3.7 — reversible epimerization of **UDP-N-acetyl-alpha-D-glucosamine <->
  UDP-N-acetyl-alpha-D-galactosamine** (Rhea:RHEA:20517). Relevant to protein/lipid
  glycosylation (UDP-GalNAc supply). This second activity is present in the human
  enzyme but NOT in the E. coli ortholog (P09147): "Contrary to the human enzyme, the
  E.coli ortholog ... does not catalyze the epimerization of UDP-N-acetylglucosamine to
  UDP-N-acetylgalactosamine ... the sugar-binding pocket of the active site is 15% larger
  for the human enzyme" [UniProt Q14376 MISCELLANEOUS; PMID:11279032].

UniProt FUNCTION: "Catalyzes two distinct but analogous reactions: the reversible
epimerization of UDP-glucose to UDP-galactose and the reversible epimerization of
UDP-N-acetylglucosamine to UDP-N-acetylgalactosamine. The reaction with UDP-Gal plays a
critical role in the Leloir pathway of galactose catabolism ... Both UDP-sugar
interconversions are important in the synthesis of glycoproteins and glycolipids."
[ECO:0000269|PubMed:22654673].

- **Cofactor**: tightly bound NAD(+) (one per monomer) [PMID:10801319, PMID:22654673].
  Extensive NAD(+) BINDING features (residues 12-14, 33-37, 66-67, 88, 92, 161, 185).
- **Subunit**: Homodimer [PMID:10801319, PMID:16302980]. Self-interaction Q14376-Q14376
  reported in IntAct (NbExp=7).
- **Active site**: Tyr157 (proton acceptor); Ser132 catalytic; substrate-binding residues.
- **Location**: cytosolic (Reactome R-HSA-70369 "Cytosolic UDP-galactose 4-epimerase ...";
  GO cytosol IBA/TAS). No signal peptide, TM, or organellar targeting.
- **Pathway** (UniProt): Carbohydrate metabolism; galactose metabolism (UniPathway UPA00214).

## Disease

- **Galactosemia 3 / epimerase-deficiency galactosemia (GALAC3, MIM:230350)** — autosomal
  recessive. Ranges from benign **peripheral** form (enzyme deficiency limited to
  circulating blood cells) to rare severe **generalized** form (undetectable activity in
  all tissues; growth restriction, intellectual disability). Many characterized missense
  variants reduce UDP-Gal epimerase kcat/kcat/Km (e.g. V94M generalized, ~30-fold decrease)
  [UniProt DISEASE; PMID:16302980; PMID:9973283; PMID:11279193].
- **Syndromic thrombocytopenia 13 (THC13, MIM:620776)** — AR macrothrombocytopenia with
  gray platelets, variably leukopenia/anemia, mitral valve malformation, pyloric stenosis,
  impaired intellectual development. Linked to disrupted N-glycosylation and thrombopoiesis
  (via the UDP-GalNAc/GlcNAc epimerase side of GALE) [PMID:30247636, PMID:33510604,
  PMID:34159722, PMID:36395340]. Note THC13 case PMID:33510604 is described as "altered
  N-glycosylation with relative preservation of the Leloir pathway", underscoring the
  glycosylation (UDP-GlcNAc/GalNAc) role.

## dismech Galactosemia.yaml
Confirms GALE deficiency = one of three Leloir-pathway galactosemia enzymes; phenotype
"ranges from benign peripheral form to severe generalized form resembling classic
galactosemia" (MONDO:0009257 galactose epimerase deficiency).

## Annotation review reasoning

Existing GOA (18 lines):
- GO:0003978 UDP-glucose 4-epimerase activity: IBA (GO_REF:0000033), IEA
  (GO_REF:0000120, EC 5.1.3.2/RHEA:22168), IDA (PMID:16302980). CORE MF. ACCEPT all.
- GO:0003974 UDP-N-acetylglucosamine 4-epimerase activity: IEA (GO_REF:0000120, EC
  5.1.3.7/RHEA:20517). This is the second, human-specific bifunctional activity, well
  supported by UniProt/PMID:22654673/PMID:11279032. ACCEPT (core secondary MF).
- GO:0006012 galactose metabolic process (IEA), GO:0033499 galactose catabolic process
  via UDP-galactose Leloir pathway (IBA + IEA GO_REF:0000107), GO:0019388 galactose
  catabolic process (IDA PMID:16302980): all BP for galactose catabolism/Leloir; ACCEPT.
  GO:0033499 is the most specific/informative (Leloir).
- GO:0005829 cytosol: IBA + 2x TAS (Reactome). ACCEPT (cytosolic enzyme).
- GO:0042803 protein homodimerization activity: IPI PMID:16302980. ACCEPT — active enzyme
  is a homodimer (structurally & biochemically established). More informative than bare
  identical protein binding.
- GO:0042802 identical protein binding: 5x IPI from high-throughput interactome maps
  (IntAct; Q14376-Q14376 self-interaction). Not wrong (reflects the homodimer) but a
  low-information molecular-function term duplicated 5x from HT screens. MARK_AS_OVER_ANNOTATED;
  the homodimer is better captured by GO:0042803.

Missing but supported (candidate NEW): NAD binding (GO:0051287) — tightly bound cofactor,
extensive structural evidence (PMID:10801319, PMID:22654673, UniProt BINDING features).

## core_functions (author-supplied ids; strictly validated — current ontology labels)
- MF GO:0003978 UDP-glucose 4-epimerase activity; directly_involved_in GO:0033499
  galactose catabolic process via UDP-galactose, Leloir pathway; location GO:0005829 cytosol.
- MF GO:0003974 UDP-N-acetylglucosamine 4-epimerase activity (bifunctional; glycoconjugate
  UDP-sugar supply); location GO:0005829 cytosol.
</content>
