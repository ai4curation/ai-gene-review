# SLC52A1 (RFVT1 / hRFT1) review notes

UniProt: Q9NWF4 (S52A1_HUMAN), 448 aa, gene SLC52A1 (synonyms GPR172B, PAR2, RFT1).
HGNC:30225. TCDB 2.A.125.1.1 (eukaryotic riboflavin transporter family). InterPro
IPR009357 (Riboflavin_transptr); Pfam PF06237. 11 predicted TM helices; one N-glyc
site (Asn178). PE 1 (protein-level evidence).

## Core biology (grounded)

- **Riboflavin (vitamin B2) plasma-membrane uptake transporter.** UniProt FUNCTION:
  "Plasma membrane transporter mediating the uptake by cells of the water soluble
  vitamin B2/riboflavin that plays a key role in biochemical oxidation-reduction
  reactions of the carbohydrate, lipid, and amino acid metabolism"
  [file:human/SLC52A1/SLC52A1-uniprot.txt]. Humans cannot synthesize riboflavin and
  obtain it by intestinal absorption.
- **Transport mechanism / kinetics.** Na+-, potential-, pH-independent facilitated
  diffusion; KM ~1.38 uM for riboflavin (hRFT1) [PMID:20463145
  "The apparent"; UniProt "KM=1.38 uM for riboflavin"]. Overexpression of hRFT1
  increases cellular [3H]riboflavin accumulation; siRNA knockdown decreases uptake
  [PMID:18632736 "Overexpression of hRFT1 and rRFT1, but not"]. Activity strongly
  inhibited by lumiflavin, weakly by FAD [UniProt ACTIVITY REGULATION].
- **Localization = plasma membrane; basolateral in polarized epithelia.**
  UniProt SUBCELLULAR LOCATION: Cell membrane, multi-pass. GFP-hRFT1 in HEK-293 =
  plasma-membrane signal [PMID:18632736 "exhibited a fluorescent"]. In polarized
  Caco-2/MDCK cells hRFT-1 is mainly basolateral [PMID:21854757 (full text) "the
  hRFT-1 is mainly expressed at the BLM"], consistent with mediating riboflavin
  EXIT out of enterocytes toward the bloodstream (hRFT-2/SLC52A3 is the apical
  luminal uptake transporter). So SLC52A1 is not the main apical intestinal uptake
  route; its GO:0016323 basolateral localization is well supported.
- **Tissue expression.** Widely expressed; highest in testis, placenta, small
  intestine [UniProt TISSUE SPECIFICITY; PMID:18632736; PMID:20463145]. Placental
  expression underlies maternal-fetal transfer.
- **Disease.** Riboflavin deficiency (RBFVD; MIM:615026): maternal SLC52A1 defect →
  transient neonatal-onset glutaric aciduria type 2 / multiple acyl-CoA
  dehydrogenase deficiency, reversible with oral riboflavin [UniProt DISEASE;
  PMID:21089064 (not cited in GOA but in UniProt refs)].
- **Neofunctionalized urate transport (primate-specific).** PMID:41759742 (full
  text) shows primate/human SLC52A1 transports urate as well as riboflavin
  ["Functional studies demonstrated the ability of primate SLC52A1"], mediates both
  uptake and efflux ["the mediation of cellular uptake"], and basolaterally in
  enterocytes works with ABCG2 (apical/luminal efflux) to secrete urate into the
  intestine. SLC52A1 arose by duplication from SLC52A2 in primates. This grounds the
  IDA GO:0015143 (urate transmembrane transporter activity) and GO:0015747 (urate
  transport) annotations as genuine core functions, not artifacts.
- **Viral receptor (microbial infection).** Originally identified as huPAR-2, a human
  receptor for porcine endogenous retrovirus PERV-A [PMID:12740431]. UniProt marks
  this as (Microbial infection) FUNCTION and keyword "Host cell receptor for virus
  entry"; it is not a normal endogenous function and is not in the GOA set as an MF
  here (GO:0001618 virus receptor activity is only an IEA-KW in the UniProt DR line,
  not in the GOA TSV), so no action needed.

## Curation decisions summary

- Core MF: GO:0032217 riboflavin transmembrane transporter activity; GO:0015143
  urate transmembrane transporter activity (neofunctionalized, IDA).
- Core BP: GO:0032218 riboflavin transport; GO:0015747 urate transport.
- Core CC: GO:0016323 basolateral plasma membrane (specific, IDA); GO:0005886 plasma
  membrane accepted (parent, many evidences).
- MARK_AS_OVER_ANNOTATED: GO:0005515 protein binding (IPI, HuRI Y2H hits, bare and
  uninformative; NOT removed per policy). GO:0006771 riboflavin metabolic process
  (TAS Reactome pathway grouping — SLC52A1 transports, does not metabolize,
  riboflavin; better captured by GO:0032218).
- No REMOVE actions: all electronic annotations here (plasma membrane, riboflavin
  transporter activity, riboflavin transport) are the gene's own correct core
  functions, so ACCEPT rather than REMOVE.

## References read (cache)

- PMID:12740431 (abstract only) — PERV-A receptor identification.
- PMID:18632736 (abstract only) — cloning/functional characterization of hRFT1.
- PMID:20463145 (abstract only) — comparative hRFT1/2/3; KM 1.38 uM for hRFT1.
- PMID:21854757 (full text) — polarized-epithelia localization; hRFT-1 basolateral.
- PMID:32296183 (full text) — HuRI binary interactome (source of protein binding IPI).
- PMID:41759742 (full text) — SLC52A1 neofunctionalized urate transporter.
- Reactome R-HSA-196843 (Vitamin B2 metabolism), R-HSA-3165230 (SLC52A1,2,3 transport RIB).
