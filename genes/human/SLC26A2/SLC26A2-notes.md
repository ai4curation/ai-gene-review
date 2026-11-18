# SLC26A2 (DTDST) curation notes

UniProt: P50443 (S26A2_HUMAN), gene SLC26A2 / DTD / DTDST. 739 aa, SLC26A/SulP
transporter family (TC 2.A.53), STAS domain (568-719), 8 TM helices (UniProt FT).
Cryo-EM structures 7XLM, 8TNW/8TNX/8TNY resolved.

## Core function

SLC26A2/DTDST is a plasma-membrane secondary-active sulfate transporter that
mediates sulfate uptake into cells (notably chondrocytes) as an electroneutral
anion exchanger. Sulfate taken up is used by PAPS synthesis to sulfate
glycosaminoglycans/proteoglycans of cartilage extracellular matrix; loss of
function produces undersulfated proteoglycans and a spectrum of recessive
chondrodysplasias.

- Positional cloning identified it as a novel sulfate transporter whose impaired
  function undersulfates cartilage proteoglycans [PMID:7923357 "encodes a novel
  sulfate transporter. Impaired function of its product is likely to lead to
  undersulfation of proteoglycans in cartilage matrix"].
- UniProt FUNCTION (curated, ECO:0000269 to the four functional papers):
  "Sulfate transporter which mediates sulfate uptake into chondrocytes in order to
  maintain adequate sulfation of proteoglycans which is needed for cartilage
  development"; "Mediates electroneutral anion exchange of sulfate ions for oxalate
  ions and of sulfate and oxalate ions for chloride ions"
  [file:human/SLC26A2/SLC26A2-uniprot.txt].

## Transport mechanism / substrates (PMID:20219950, Heneghan et al. 2010, full text)

Human SLC26A2 expressed in Xenopus oocytes:
- Mediates bidirectional oxalate/SO4(2-) exchange, SO4(2-)/Cl(-) exchange, Cl(-)/Cl(-)
  exchange, and oxalate/Cl(-) exchange [PMID:20219950 "hSLC26A2-mediated bidirectional
  oxalate/SO(4)(2-) exchange"].
- All tested modes are electroneutral [PMID:20219950 "bidirectional SO(4)(2-)/Cl(-)
  exchange were not detectably electrogenic"].
- Nonsaturable low-affinity extracellular Cl(-) dependence; Cl- is the predominant
  physiological counterion [PMID:20219950 "SLC26A2 orthologs exhibited nonsaturable
  extracellular Cl(-) dependence for efflux of intracellular"].
- Regulated by extracellular pH (acidic pHo inhibits), intracellular pH, NH4+, and PKC
  (PKC reduces surface abundance).
- Curated Rhea catalytic activities in UniProt: oxalate(in)+sulfate(out) exchange;
  sulfate(out)+2 chloride(in); oxalate(out)+2 chloride(in); and (by similarity to mouse
  Q62273) bromide/chloride, nitrate/chloride, iodide/chloride — i.e. sulfate and oxalate
  for OH-/Cl-, and Cl- for Br-/I-/NO3- [file:human/SLC26A2/SLC26A2-uniprot.txt].

Oxalate is a genuine but secondary substrate: directly demonstrated oxalate uptake by
human DTDST (~48 pmol/oocyte/h, significant vs control) when used as a positive control
in a Drosophila oxalate-transporter study [PMID:40356774 "Known human oxalate transporters
(SLC26A6, SLC26A2/DTDST) and dPrestin were tested for oxalate uptake"]. Heneghan note it
is "likely a minor contributor to intestinal transepithelial transport of oxalate" — so
oxalate transport is non-core relative to sulfate.

## Localization

- Plasma membrane (cell membrane), multipass. WT protein glycosylated and at the plasma
  membrane in HEK-293 [PMID:15294877 "mutations were expressed on the plasma membrane of
  the cell"]; UniProt SUBCELLULAR LOCATION "Cell membrane {ECO:0000269|PubMed:15294877,
  ECO:0000269|PubMed:7923357}".
- Apical in epithelia: "Apical cell membrane" (UniProt, by similarity to rat O70531);
  immunolocalized to apical pole of human enterocytes and rat renal proximal tubule brush
  border (microvillus) [PMID:20219950 discussion]. Microvillus/apical localization is an
  epithelial sub-location, not the chondrocyte core.
- Detected in urinary/prostatic exosome proteomics (HDA, PMID:23533145) — a
  high-throughput detection typical of plasma-membrane proteins; non-core.

## Mutations / disease

Allelic recessive chondrodysplasia series, severity tracking residual sulfate transport:
achondrogenesis 1B (null/null, lethal), atelosteogenesis 2, diastrophic dysplasia,
recessive multiple epiphyseal dysplasia 4 (partial-function) [PMID:11448940; PMID:15294877;
PMID:8528239]. "transmembrane protein that transports sulfate into chondrocytes to maintain"
adequate proteoglycan sulfation [PMID:11448940].

## Family / IBA judgements

PANTHER PTHR11814 (SULFATE TRANSPORTER); SLC26/SulP family contains both sulfate
transporters (A1, A2, A11) and Cl-/HCO3- exchangers (A3/DRA, A4/pendrin, A6).
`just paint-losses human SLC26A2`: no IRD/IKR loss on the lineage.

- Sulfate transport, plasma membrane, chloride transport, oxalate transport IBAs all have
  direct human experimental support and are kept.
- GO:0140900 chloride:bicarbonate antiporter activity (IBA, node PTN008330351): the IBD
  node is seeded by the dedicated Cl-/HCO3- exchanger paralogs (SLC26A1/A3/A6). SLC26A2's
  own functional characterization does NOT show productive Cl-/HCO3- exchange — HCO3- is
  only a weak (~20%) cis-inhibitor of sulfate uptake [PMID:20219950]. Treated as
  over-annotation extended from the HCO3--exchanger subclade; recorded in propagation_review.

## Downstream developmental roles

chondrocyte differentiation (GO:0002062) and chondrocyte proliferation (GO:0035988) are
ISS/IEA from mouse Q62273 ("Essential for chondrocyte proliferation, differentiation and
cell size expansion", UniProt by similarity). SLC26A2 supplies the metabolic substrate
(sulfate) that these processes require; it does not execute differentiation/proliferation
steps. Kept as non-core (necessity, not participation).
