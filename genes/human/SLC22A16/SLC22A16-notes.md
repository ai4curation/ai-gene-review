# SLC22A16 (CT2 / OCT6 / FLIPT2, UniProt Q86VW1) — curation notes

## Summary

SLC22A16 encodes the human testis carnitine transporter CT2 (also OCT6, FLIPT2,
"organic cation/carnitine transporter 6"), a 577-residue, 12-transmembrane
plasma-membrane solute carrier of the SLC22 / major facilitator superfamily
organic cation transporter family (TC 2.A.1.19.12). Its physiologically defining,
high-affinity substrate is L-carnitine; it is most strongly and specifically
expressed in testis (Sertoli cells, epididymal luminal epithelium) and bone
marrow, where luminal carnitine secretion/uptake supports sperm maturation. CT2
is polyspecific: beyond carnitine it mediates high-affinity transport of the
polyamine spermidine and of xenobiotic cations/anticancer drugs — doxorubicin
(adriamycin) and the polyamine-bearing bleomycin-A5 — making CT2 expression a
determinant of chemosensitivity in leukemic/testicular tumor cells.

## Protein / family

- UniProt Q86VW1, 577 aa, 12 predicted TM helices (ECO:0000255), multi-pass
  membrane protein; 8 predicted N-glycosylation sites; C-terminal disordered
  region (543–577). [SLC22A16-uniprot.txt FT lines].
- "Belongs to the major facilitator (TC 2.A.1) superfamily. Organic cation
  transporter (TC 2.A.1.19) family." (UniProt SIMILARITY). CDD cd17375
  `MFS_SLC22A16_CT2`; PANTHER PTHR24064 SOLUTE CARRIER FAMILY 22 MEMBER.
- Phylogenetically CT2 "is phylogenetically located between the organic cation
  transporter (OCT/OCTN) and anion transporter (OAT) families" and "represents a
  novel transporter family" [PMID:12089149 "phylogenetically located between the
  organic cation transporter (OCT/OCTN) and anion transporter (OAT) families"].
- Three alternative-splicing isoforms (Q86VW1-1 displayed; -2; -3). Common
  variant M409T (rs12210538).

## Function / transport activity

### Carnitine (defining, high-affinity)
- CT2 is "a novel carnitine transporter (CT2) specifically located in human
  testis" that "mediates the high affinity transport of l-carnitine but does not
  accept mainstream OCT/OCTN cationic or OAT anionic substrates"
  [PMID:12089149 "mediates the high affinity transport of l-carnitine but does
  not accept mainstream OCT/OCTN cationic or OAT anionic substrates"].
- UniProt: "Facilitative organic cation transporter that mediates the transport
  of carnitine as well as the polyamine spermidine ... Mediates the partially
  Na(+)-dependent bidirectional transport of carnitine" (CC:FUNCTION). KM = 20.3
  uM (PMID:12089149) and 8 uM (PMID:20037140) for L-carnitine; pH optimum 8.5.
- Rhea/catalytic: (R)-carnitine(in) = (R)-carnitine(out), ChEBI:16347.
- Physiological role: "l-Carnitine ... plays a pivotal role in the maturation of
  spermatozoa within the male reproductive tract. Epididymal plasma contains the
  highest levels of l-carnitine found in the human body, and initiation of sperm
  motility occurs in parallel to l-carnitine increase in the epididymal lumen ...
  epididymal epithelium secretes l-carnitine into the lumen by an active
  transport mechanism" [PMID:12089149]. Protein "located in the luminal membrane
  of epididymal epithelium and within the Sertoli cells of the testis"
  [PMID:12089149 "located in the luminal membrane of epididymal epithelium and
  within the Sertoli cells of the testis"].

### Spermidine / polyamine (high-affinity secondary)
- "the human l-carnitine transporter hCT2 encoded by the SLC22A16 gene is
  involved in bleomycin-A5 uptake, as well as polyamines" [PMID:20037140].
- Direct kinetics: "hCT2 may act as a high affinity transporter for polyamines";
  spermidine KM = 0.35 uM (vs carnitine KM = 8 uM) [PMID:20037140]. UniProt
  catalytic activity spermidine(in)=spermidine(out) ChEBI:57834.

### Doxorubicin / bleomycin (xenobiotic drugs; chemosensitivity)
- "SLC22A16 is a mediator of doxorubicin uptake in cancer cells ... Xenopus
  oocytes injected with SLC22A16 cRNA import doxorubicin ... The apparent Km
  value for doxorubicin import was 5.2+/-0.4 microM ... stable transfectants of
  leukemic Jurkat cells overexpressing SLC22A16 cells became significantly more
  sensitive to doxorubicin" [PMID:15963465].
- "hCT2 mediates the intracellular uptake of BLM [bleomycin-A5]"; L-carnitine
  competitively blocks F-BLM uptake and siRNA knockdown confers resistance
  [PMID:20037140]. UniProt MISCELLANEOUS: "Involved in the uptake of clinically
  used drugs such as anticancer agents doxorubicin and bleomycin."

## Localization
- Cell membrane (plasma membrane), multi-pass; "Detected in the plasma membrane
  of Sertoli cells and in the luminal membrane of epithelial cells in the
  epididymis" (UniProt CC:SUBCELLULAR LOCATION, PMID:12089149). Confocal of
  hCT2-GFP: "the fusion protein was specifically present on the plasma membrane"
  [PMID:20037140].

## Tissue specificity
- Testis and epididymis (protein level), bone marrow, hematopoietic/CD34+ cells,
  endometrium (secretory phase), leukemia and ovarian clear-cell adenocarcinoma
  cells (UniProt CC:TISSUE SPECIFICITY). HPA "Group enriched (bone marrow,
  testis)".

## Curation reasoning for annotation review

- **Core MF:** carnitine transmembrane transporter activity (GO:0015226, verified
  non-obsolete via QuickGO) is the defining function. Spermidine transmembrane
  transporter activity (GO:0015606) is a genuine high-affinity secondary MF.
  Amine transmembrane transporter activity (GO:0005275) is the live, substrate-
  general term capturing doxorubicin/organic-cation handling (the obsolete
  organic-cation grouping terms GO:0015101 and GO:0015695 are avoided).
- **Core location:** plasma membrane (GO:0005886).
- **Process rows** `carnitine transport`/`carnitine transmembrane transport`/
  `spermidine transmembrane transport` are ACCEPT; root `transmembrane
  transport`/`transmembrane transporter activity`/`membrane` are TOO_GENERAL once
  the specific terms are asserted.
- **Participation test (necessity != participation):** CT2 transports
  carnitine/drugs but does not execute spermatogenesis, fertilization or the drug
  response. `flagellated sperm motility` (GO:0030317) is KEEP_AS_NON_CORE (genuine
  physiological context: CT2 supplies luminal carnitine that sperm need for
  motility); `single fertilization` (GO:0007338) is MARK_AS_OVER_ANNOTATED (too
  distal — carnitine supply is many steps upstream of the fertilization event).
- **`acid secretion` (GO:0046717) IDA:** derives from carnitine (a carboxylate)
  secretion into the epididymal lumen being mapped to the generic "acid
  secretion" term; carnitine is a zwitterion, and the physiological event is
  carnitine transport, already captured by GO:0015879. MARK_AS_OVER_ANNOTATED +
  WRONG_TERM source_defect (repoint to carnitine transport).
- Self-appearance of UniProtKB:Q86VW1 in IBA WITH/FROM reflects experimental
  grounding on the target and is expected, not circular.
