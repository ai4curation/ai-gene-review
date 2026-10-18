# Human VAPA evidence notes

The completed Falcon report identifies VAPA as an ER receptor/tether rather than a lipid carrier. Independent primary inspection confirms this: [PMID:33124732](https://pubmed.ncbi.nlm.nih.gov/33124732/) supplies structures, FFAT peptide-binding experiments and contact-site reconstitution; [PMID:24209621](https://pubmed.ncbi.nlm.nih.gov/24209621/) distinguishes the VAPA anchor from the lipid-transfer domain in OSBP. Lipid-transport BP annotations can therefore be mechanistically appropriate without claiming intrinsic lipid-transporter MF.

[PMID:18713837](https://pubmed.ncbi.nlm.nih.gov/18713837/) tests VAPA overexpression, ER cargo transport and microtubule association, including rescue by FFAT peptide. [PMID:10523508](https://pubmed.ncbi.nlm.nih.gov/10523508/) supports peripheral VAP-33/occludin localization. These sources support the core and several ancillary annotations. Protein-folding, early membrane-fusion, NF-kappaB-screen and opposing viral-direction annotations require more detailed source-specific resolution and remain UNDECIDED. IPI interaction rows are retained as non-core observations rather than being converted automatically into core FFAT interactions.

The human/horse alignment preserves the MSP domain and membrane anchor and identifies a horse linker insertion corresponding to the human alternative-splicing region. This explains why the shared MSP-domain name cannot transfer the nematode sperm-filament mechanism. See the horse prediction review for the exact original text and assessment.

## 2026-09-26: does GO:0160214 (ER-PM adaptor activity) apply?

Context: ER_PM_TETHERING_OBSOLETION project (GO:0061817 ER-PM tethering obsoleted; MF replacement GO:0160214). VAPA carries no GO:0061817 annotation in GOA, so nothing needs repair.

- OLS definition of GO:0160214: "The binding activity of a molecule that brings together a plasma membrane with an endoplasmic reticulum membrane, via membrane lipid binding, to establish membrane contact sites and mediate exchange and communication." Contrast GO:0170016 ER-endosome tether activity, which explicitly allows "or by interacting with an endosome protein" (VAPA already carries GO:0170016 by IDA).
- Biology: VAPA does sit at ER-PM contacts as the ER half of FFAT-partner bridges. [PMID:32234213 "The PH domain binds PI(4,5)P2 at the PM, while the central FFAT motifs bind ER-anchored VAP-A (and/or VAP-B), bringing the two membranes into close proximity and allowing lipid exchange."] The PM lipid binding in this bridge is the partner's (ORP3 PH domain), not VAPA's.
- Comparator check (QuickGO annotation search, `goId=GO:0160214&goUsage=exact`, IEA rows filtered out; re-run 2026-09-27, 1003 total hits, 12 non-IEA). The 12 rows:
  - UniProtKB:Q8IUY3 GRAMD2A (human) IDA PMID:29469807 (UniProt)
  - UniProtKB:Q3V3G7 Gramd2a (mouse) ISS GO_REF:0000024 (UniProt); ISO GO_REF:0000119 (GO_Central)
  - UniProtKB:D3ZIZ1 Gramd2a (rat) ISO GO_REF:0000121 (RGD)
  - UniProtKB:Q7XA06 SYT3 (Arabidopsis) IDA PMID:33944955 (TAIR)
  - UniProtKB:O60119 scs2 (S. pombe) IDA PMID:23041194; IMP PMID:26877082; EXP PMID:39110593 (PomBase)
  - UniProtKB:Q10484 scs22 (S. pombe) IDA PMID:23041194; IMP PMID:26877082; EXP PMID:39110593 (PomBase)
  - UniProtKB:O95292 VAPB (human) ISS GO_REF:0000024 (UniProt)

  No human ORP (OSBPL3/5/8) or ESYT has it experimentally. So GO curators have applied it to VAP orthologs in fission yeast, which conflicts with a strict reading of the "via membrane lipid binding" clause.
- GO-CAM check (`gocams/`):
  - `gocams/682fbcd000003765` ("Regulation of focal adhesion assembly: OSBPL3 transports PI4P and PC between PM and ER (Human)", production) is curated from PMID:32234213 itself (ECO:0000314). It types VAPA (Q9P0L0) as GO:0043495 protein-membrane adaptor activity occurring in GO:0005789 ER membrane. GO:0140268 ER-PM contact site appears in the model on partner activity nodes (IQSEC1, OSBPL3), not on VAPA. A curator who modelled this exact contact from this exact paper reached the same conclusion as this review. This is the strongest support for not adding GO:0160214.
  - `gocams/68fac5ed00002250` ("Phosphatidylinositol and phosphatidic acid transport by PITPNM1 in ER-PM MCS", production, UniProt-contributed) has human VAPB (O95292) as a GO:0160214 activity node, with ISS evidence (ECO:0000250, GO_REF:0000024, with MGI:1928744) on its enabled_by and occurs_in GO:0140268 associations. So the VAPB precedent is a GO-CAM activity node as well as a GAF row. This sharpens the question, since VAPA and VAPB are the same kind of FFAT receptor.
- CC asymmetry in VAPA GOA: VAPA is_active_in GO:0140284 ER-endosome membrane contact site (IDA PMID:41741634) and GO:0160258 ER-trans-Golgi network membrane contact site (IDA PMID:34688657, PMID:39106189), but has no GO:0140268 ER-PM contact site row. The MF annotations have the same shape: VAPA has GO:0170016 ER-endosome tether activity (IDA), whose definition allows bridging "by interacting with an endosome protein", and no ER-PM term, whose definition requires lipid binding. GOA's GO:0043495 IDA row for VAPA also cites PMID:32234213, the same paper used here.
- Decision: do not add GO:0160214 as NEW for VAPA. Its mechanism (FFAT receptor on the ER side) is already captured by the core GO:0043495 protein-membrane adaptor activity; the term definition names PM lipid binding that VAPA does not perform; and the PomBase/VAPB precedent is recorded as a suggested question rather than propagated by us.
