# SPBC21C3.19 (Rtc3 / SNOR; UniProt Q9P7K6) — curation notes

## Identity

- UniProt Q9P7K6, "SDO1-like protein C21C3.19", 106 aa, PE 3 (inferred from homology).
  Single Pfam SBDS_N domain (PF01172); PANTHER PTHR10927:SF2 "RESTRICTION OF TELOMERE
  CAPPING PROTEIN 3" (i.e. the S. cerevisiae Rtc3/Hgi1 subfamily, not the Sdo1/SBDS
  subfamily). The protein is only the SBDS N-terminal (FYSH) domain plus a short basic
  C-terminal tail; it lacks SBDS domains II and III.
- Named SNOR ("SBDS domain-containing hibernation factor") in PMID:42129552 (Gluc et al.,
  Nature 2026); the paper calls the gene `rtc3`.
- Before 2026 the gene had no gene-specific literature. The only S. pombe experimental data
  were the ORFeome GFP localisation screen (PMID:16823372: nucleus + cytosol, HDA).

## PMID:42129552 — SNOR promotes translation restart after dormancy (full text cached)

All experiments below were done on S. pombe Rtc3 itself (endogenous protein, knock-in
mutants, or recombinant S. pombe protein), except where noted.

### Identification on hibernating ribosomes (in situ cryo-ET, S. pombe cells)

- Cells grown 7 days in EMM 0.5% glucose (glucose-depleted dormancy); 3.38 Å in situ
  subtomogram average of the hibernating 80S; extra density between eEF2 and eIF5A
  "capping the PTC" [PMID:42129552 "we identified an additional electron density with clearly resolved side chains corresponding to a small globular domain positioned between eEF2 and eIF5A, adjacent to RNA helix 69 (H69) and capping the PTC"].
- Sdo1 domain I was the first guess but did not fit [PMID:42129552 "However, this assignment was inconsistent with the resolved side-chain features, and domains II and III were neither supported by density nor structurally compatible, as they would sterically clash with eEF2"].
- Foldseek identified Rtc3 [PMID:42129552 "This analysis identified Rtc3 (SPBC21C3.19), an SBDS domain-containing protein of previously unknown function"].
- AlphaFold model fit, and MS of ribosomes [PMID:42129552 "Consistently, mass spectrometry analysis confirmed the presence of Rtc3 in ribosomes isolated after prolonged glucose depletion"]. The MS data are in Supplementary Table 1 (Figshare) — NOT inspected here (no abundance values seen; whether Rtc3 is also present in day-1 ribosomes is not stated in the main text).
- OMM-associated and cytosolic ribosomes share the same factors [PMID:42129552 "Subclassification of OMM-associated and cytosolic ribosomes using an initial dataset revealed a shared hibernation architecture and no structural differences in ribosome-bound factors"].
- Other factors on the same dormant ribosomes: eEF2, Oga1 (Stm1 orthologue), hypusinated eIF5A [PMID:42129552 "Following glucose depletion, dormant ribosomes associate with SNOR together with Oga1 (Stm1 in S. cerevisiae), eIF5A, and eEF2"].

### Expression (endogenous 2xFlag-tagged SNOR; RT-qPCR)

- mRNA up after 3 days glucose deprivation; protein up by days 4 and 7 [PMID:42129552 "showed a significant increase in SNOR protein levels by days 4 and 7 of glucose deprivation"].
- Specific to glucose-dependent carbon stress [PMID:42129552 "SNOR was selectively upregulated under limiting (0.5% w/v) and high (20% w/v) glucose conditions, but not under standard glucose levels (2%)"]; not induced by 0% glucose, amino-acid or nitrogen deprivation, or 1.1 M NaCl [PMID:42129552 "these data indicate that SNOR induction is specific to glucose-dependent carbon stress and is not a consequence of general nutrient or osmotic stress"].
- Caveat for GO: induction of expression is a response of the gene, not participation; it does not by itself justify a "response to" process term.

### Direct ribosome binding (recombinant S. pombe SNOR + purified S. pombe subunits)

- Co-sedimentation: binds 60S and 80S, not 40S [PMID:42129552 "The binding assays showed that SNOR specifically interacts with the 60S large subunit and intact 80S ribosomes"].
- 2.8–3.5 Å SPA cryo-EM of reconstituted 60S–SNOR: same PTC site as in situ [PMID:42129552 "confirmed that SNOR binds to the PTC of the 60S subunit at the same active site location that is observed in the in situ cryo-ET structure of the hibernating ribosome"].
- Contacts are mostly rRNA [PMID:42129552 "SNOR interacts almost exclusively with rRNA through charged interactions"]; plus uL16 (Rpl10) loop via E43/D46.
- C-terminal 7-residue basic tail inserts into the polypeptide exit tunnel (PET), unlike Sdo1 which inserts its N-terminal domain [PMID:42129552 "This mode of interaction contrasts with that of Sdo1, which inserts its N-terminal domain into the PET"].
- Mutants: K68E and K68E/H96A/R97E reduce binding; H96A/R97E no change; G100STOP (tail deletion) reduces binding less; E43A/D46A enhances binding [PMID:42129552 "These results suggest that highly conserved K68 is the primary contributor to RNA-mediated SNOR binding to the ribosome"].
- Residue numbering checked against Q9P7K6 displayed sequence (v1): K68, H96, R97, G100, E43, D46, S54/N55/N56, Q69/E72/N73, N106 all match the residues stated. Note the paper is internally inconsistent in two places (Fig. 3f legend "E43 and E46" vs text "E43 and D46"; Fig. 4d legend "E70/N73" vs text "Q69, E72 and N73"); the canonical sequence has D46 and Q69/E72/N73 (position 70 is S).
- Also binds human (HEK) ribosomes in vitro (Supplementary Fig. 5, not inspected).

### eIF5A

- Tripartite SNOR–eIF5A–uL1 interface; SNOR N106 hydrogen-bonds the hypusine of eIF5A [PMID:42129552 "The hypusine moiety forms hydrogen-bond interactions with N106 in the C-terminal region of SNOR"].
- Cooperative co-pelleting with 60S [PMID:42129552 "when added together, recovery of both SNOR and eIF5A in the ribosomal pellet increased compared with either factor alone"].

### In vitro translation (rabbit reticulocyte lysate — heterologous)

- Purified SNOR represses reporter synthesis in RRL; triple mutant does not [PMID:42129552 "The addition of purified SNOR to the RRL reaction significantly reduced levels of Flag reporter compared with the bovine serum albumin (BSA) control"].
- Interpretation: occupying the PTC/P-site region of a heterologous ribosome is expected to block translation; the authors explicitly argue SNOR is not a canonical hibernation factor [abstract: "Rather than acting as a canonical hibernation factor, SNOR licenses dormant ribosomes for rapid translational restart"]. I do not annotate translation repressor activity or ribosome hibernation from this heterologous assay.

### In vivo function (rtc3Δ::ura4+ and knock-in point mutants at the endogenous locus)

- No growth defect in 2%, 0.5% or 0.02% glucose [PMID:42129552 "observed no major growth defects under any condition"]. (Background knowledge, not from this paper and not cited here: loss of the Sdo1/SBDS 60S-maturation factor causes a growth defect in yeast, so the lack of any growth phenotype is at least not what a biogenesis role would predict.)
- Polysomes collapse to 80S by day 7 in all strains (shutdown does not need SNOR).
- Restart after 2 h glucose re-addition fails in rtc3Δ, binding-deficient K68E/H96A/R97E and G100STOP [PMID:42129552 "These results demonstrate that SNOR association with the ribosome and its C-terminal tail are both required for translation restart"].
- Viability loss from day 4 of glucose depletion; pronounced by day 7; granulated, vacuolated morphology [PMID:42129552 "By day 7, all mutant strains exhibited pronounced viability defects"].
- GC7 (hypusination inhibitor) halves restart in WT; additive viability defect with rtc3Δ [PMID:42129552 "SNOR-knockout cells treated with GC7 exhibited reduced viability already at day 1 of glucose depletion and a markedly more severe growth defect by day 7, consistent with an additive effect"].
- Note: the additive (not epistatic) viability effect suggests SNOR and hypusinated eIF5A are not a single linear pathway, despite the authors' "cooperation" framing.

### Not ribosome biogenesis

- [PMID:42129552 "SNOR shares homology with Sdo1 (SBDS in humans), a ribosome biogenesis factor during late stages of assembly36,41. Rather than participating in ribosome biogenesis, SNOR binds the PTC of dormant 80S ribosomes and inserts its C-terminal tail into the PET."]
- The paper did not directly assay 60S maturation (eIF6/Tif6 release) in rtc3Δ. The case against the ISS ribosome-biogenesis row is: (i) domain architecture (no domains II/III, which in SBDS/Sdo1 are needed with EFL1 for eIF6 release), (ii) PANTHER places it in the Rtc3 subfamily (SF2), not Sdo1/SBDS, (iii) no growth defect of rtc3Δ (weak, indirect argument), (iv) the only characterised binding mode is on mature 80S/60S in dormancy.

## Curation decisions (summary)

- MF ND: stale -> REMOVE (nd_case STALE); NEW ribosomal large subunit binding (GO:0043023, IDA).
- nucleus HDA/IEA: KEEP_AS_NON_CORE (small 12 kDa protein; GFP fusion can diffuse; no nuclear function).
- cytoplasm IEA: MODIFY -> cytosol (GO:0005829), already carried by HDA.
- cytosol HDA: ACCEPT.
- ribosome biogenesis ISS (from human SBDS Q9Y3A5): REMOVE.
- NEW: cytosolic ribosome (GO:0022626, IDA); positive regulation of cytoplasmic translation
  (GO:2000767, IMP); cellular response to glucose starvation (GO:0042149, IMP).
- Considered and not added: cytosolic ribosome hibernation (GO:0141014) — authors argue
  against a canonical hibernation role and the only translation-repression evidence is in
  heterologous RRL; translation repressor activity — same reason; rRNA binding — structural
  contacts only, no free-rRNA assay.

## Open items / not accessed

- Supplementary Table 1 (ribosome MS abundances, Figshare 10.6084/m9.figshare.31350286),
  Supplementary Figs 3, 5–8 and Extended Data Figs 3, 7, 9 images were not available as text.
- PomBase gene name: the cached GOA still uses the systematic name SPBC21C3.19; the paper uses
  rtc3/SNOR.
