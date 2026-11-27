# ABCB1 (P-glycoprotein / MDR1) curation notes

UniProt: P08183 (MDR1_HUMAN). HGNC:40. Human, NCBITaxon:9606.
EC 7.6.2.2 (xenobiotic-transporting ATPase) and EC 7.6.2.1 (phospholipid-transporting ATPase).

## Overview / core biology

ABCB1 is a plasma-membrane ATP-binding cassette (ABC) exporter of the ABCB
subfamily. It is a single polypeptide of 1280 aa organized as two homologous
halves, each with 6 transmembrane helices and a cytosolic nucleotide-binding
domain (NBD); the two NBDs bind and hydrolyse ATP to power substrate export
through alternating inward-facing/outward-facing conformations.

- Architecture and ATP sites: "mdr is a membrane glycoprotein which includes six pairs of transmembrane domains" and "Each duplicated segment includes a consensus ATP-binding site" [PMID:3768958 "Each duplicated segment includes a consensus ATP-binding site."].
- ATP-driven mechanism from cryo-EM: "The two nucleotide-binding domains form a closed dimer occluding two ATP molecules" and "P-glycoprotein extrudes toxic molecules and drugs from cells through ATP-powered conformational changes" [PMID:29371429 "The two nucleotide-binding domains form a closed dimer occluding two ATP molecules."].

Two biochemically distinct, ATP-dependent activities are established:

1. **Polyspecific drug / xenobiotic efflux pump** (EC 7.6.2.2). The defining
   function: it extrudes a chemically diverse range of hydrophobic drugs and
   xenobiotics out of the cell, producing the multidrug-resistance (MDR)
   phenotype. "high-level expression of a full-length complementary DNA clone in
   an otherwise drug-sensitive cell confers a complete multidrug-resistant
   phenotype" [PMID:3022150 "confers a complete multidrug-resistant phenotype"].
   The outward-facing structure shows "the drug-binding cavity... is reorientated
   toward the extracellular space and compressed to preclude substrate binding"
   (ATP binding, not hydrolysis, triggers release) [PMID:29371429].

2. **Broad-specificity lipid floppase** (EC 7.6.2.1). ABCB1 translocates
   (flops) phospholipids and sphingolipids from the cytoplasmic to the exoplasmic
   leaflet: "MDR1 P-glycoprotein is a lipid translocase of broad specificity";
   short-chain phosphatidylcholine, phosphatidylethanolamine, glucosylceramide
   and sphingomyelin analogs are flopped across the apical membrane
   [PMID:8898203 "the short-chain lipids must have been translocated by the Pgps across the plasma membrane"].
   UniProt lists the RHEA reactions: PE, PC, glucosylceramide and sphingomyelin
   all translocated (in)->(out), i.e. flop (outward), consistent with a floppase
   (not a flippase, which is outward->inward).

## Localization

- Apical / luminal plasma membrane in polarized epithelia and barrier endothelia:
  apical membrane of LLC-PK1 epithelia [PMID:8898203], apical (luminal) membrane
  of enterocytes / Caco-2 [PMID:28408210 "apical localization could be confirmed for ABCB1, ABCC2, and PEPT1."],
  luminal (apical) membrane of brain microvessel endothelium [PMID:18619525],
  modest apical enrichment in retinal pigment epithelium [PMID:31791063 "showed modest apical enrichment"],
  plasma-membrane fraction of the hCMEC/D3 BBB model [PMID:23137377 "present at quantifiable levels in plasma membrane fraction of hCMEC/D3 cells"].
- Localization (plasma membrane vs intracellular/cytoplasmic pools) is regulated;
  C1orf115/RDD1 physically associates with ABCB1 and its loss mis-localizes the
  pump [PMID:35970996 "perturbation of C1orf115 led to mis-localization of ABCB1/MDR1"].
- Detected in extracellular exosomes by large-scale proteomics (urinary
  [PMID:19056867], prostatic-secretion-derived [PMID:23533145]); a membrane-protein
  by-product of vesicle shedding, not a functional site.

## Physiological roles

- Barrier protection: at the blood-brain barrier and blood-CSF barrier ABCB1
  limits CNS entry of substrates by effluxing them back to blood, e.g. Huperzine
  A [PMID:28587984 "ABCB1 but not ABCG2 played a predominant role in the efflux of Huperzine A across BBB"],
  and the anti-Alzheimer candidate DL0410 across MDCK-MDR1 monolayers
  [PMID:28757552 "DL0410 should be a substrate of P-gp, which was also confirmed by P-gp ATPase assay"].
  P-gp/ABCB1 is a defining BBB efflux transporter in BBB reviews [PMID:26590417; PMID:30280653].
- Transepithelial (vectorial) drug export across intestinal/renal/hepatic
  epithelia and ADME/drug disposition (Reactome Drug ADME).
- Can export beta-amyloid from BBB endothelium [PMID:26006083 "The ATP Binding Cassette transporter ABCB1 can export the neurotoxic peptide"].

## Regulation / interactions

- NEDD4-1 E3 ubiquitin ligase ubiquitinates ABCB1 and reduces its surface
  density [PMID:26006083 "human ABCB1 is a substrate for human NEDD4-1 ligase"].
- RNF2 (RING-finger E3 ubiquitin ligase) binds the linker region and reduces
  ATPase activity / regulates abundance [PMID:17088979 "RNF2 (RING finger protein 2), an E3 ubiquitin ligase, as a prominent Pgp-interacting protein"].
- LAPTM4B-35 colocalizes/interacts with P-gp to promote efflux [PMID:20711237 "colocalization and interaction of LAPTM4B-35 with multidrug resistance (MDR) 1 (P-glycoprotein, P-gp)"] — a generic interaction, not an informative molecular function for ABCB1.
- PKC-mediated phosphorylation of the P-gp linker regulates cell-volume-activated
  chloride channels: "P-gp is a channel regulator" [PMID:7828597 "P-gp is a channel regulator"] — a moonlighting/regulatory role, non-core.
- Many miRNAs (miR-873, miR-508-5p, miR-9, miR-495, miR-129-5p) target the ABCB1
  3'UTR and modulate the MDR phenotype; these genetic experiments confirm ABCB1's
  drug-efflux function but are regulatory, not new ABCB1 activities
  [PMID:26850595; PMID:23893241; PMID:28260112; PMID:28411377; PMID:25344911].

## Judgement calls recorded in the review

- **GO:0000086 G2/M transition** (IDA, PMID:19384922) and **GO:0072089 stem cell
  proliferation** (IMP, same paper): the paper shows ABCB1 is a surface *marker*
  enriched on proliferating fetal neural stem/progenitor cells
  [PMID:19384922 "showed enrichment of proliferating cells"]; it does not show the
  efflux pump performing work in the cell cycle or in proliferation. Over-annotation.
- **GO:0090555 phosphatidylethanolamine flippase activity** (IDA, PMID:8898203):
  flippase = exoplasmic->cytosolic (inward). ABCB1 flops PE outward, so this is a
  direction (sign) error; MODIFY to GO:0140341 phosphatidylethanolamine floppase
  activity, which the gene already carries from the same paper.
- **GO:0098591 external side of apical plasma membrane** (ISS, PMID:18619525): a
  polytopic transporter embedded in the apical membrane is not peripherally on its
  external side; the biotinylation study labels luminal-surface-exposed epitopes.
  Generalize (MODIFY) to GO:0016324 apical plasma membrane.
- **GO:0016020 membrane** rows: ABCB1 is specifically a plasma-membrane protein;
  the generic "membrane" term is MODIFY -> GO:0005886 plasma membrane.
- **GO:0022857 transmembrane transporter activity** (ISS): the bare root transport
  MF is entailed by the specific xenobiotic/ABC transporter terms = TOO_GENERAL.
- **GO:0005515 protein binding**: RNF2 row MODIFY -> GO:0031625 ubiquitin protein
  ligase binding (RNF2 is an E3 ligase); LAPTM4B row REMOVE (uninformative generic
  binding).
- **GO:0046865 terpenoid transport** (ISS) and **GO:0046943/GO:1905039 carboxylic
  acid transport** (IMP): ABCB1's polyspecific efflux does include taxane
  (diterpenoid) and some carboxylic-acid drugs, so these are kept as non-core
  facets rather than core functions; not removed (don't overrule the experimental
  curator on a plausible substrate class whose full text is unavailable).

## Disease

- Inflammatory bowel disease 13 (IBD13) susceptibility; Encephalopathy, acute
  transient (ENPAT, biallelic loss-of-function); ivermectin toxicity with ABCB1
  nonsense mutations (UniProt DISEASE section).
