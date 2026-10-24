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

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: full re-review of all 182 existing annotations, description and core functions for Q9P0L0. ProtNLM2 output was not consulted.

Identity: Q9P0L0 is the reviewed canonical human VAPA entry (249 aa, isoform 1). It has the MSP domain (Pfam PF00635), the coiled coil and the C-terminal tail anchor. It is not a fragment or alternative gene model. Isoform 2 (VSP_038648) is a linker-region splice variant; no annotation in GOA is isoform-specific.

Evolutionary grounding: PANTHER PTHR10809:SF155 (VESICLE-ASSOCIATED MEMBRANE PROTEIN-ASSOCIATED PROTEIN A), together with mouse Vapa Q9WV55, rat Vapa Q9Z270, bovine and orangutan VAPA. The paralog VAPB/VAPC (O95292) is in SF12. The family review `interpro/panther/PTHR10809/PTHR10809-review.yaml` places VAPA in SF155 as well, so there is no disagreement. The IBA rows (GO:0043495, ER membrane, plasma membrane, neuron projection development) come from the PAINT family node. GO:0043495 and ER membrane agree with direct human evidence. The plasma-membrane and neurite rows are kept as non-core.

Main changes and reasons:
- GO:0005515 protein binding (100 rows) migrated to the generic protein-binding policy. 11 rows whose source shows FFAT-dependent binding by the partner are MODIFY to GO:0033149 FFAT motif binding: CERT [PMID:16895911 "the CERT/VAP interaction was abolished by mutations in the FFAT motif"], protrudin [PMID:19289470], STARD3 [PMID:24105263], OSBP/ORP2 [PMID:24209621, PMID:25681634, PMID:20178991], VPS13A [PMID:30741634], WDR44 [PMID:32344433] and phospho-FFAT partners [PMID:33124732 "VAP proteins were efficiently pulled down by all the peptides whose FFAT motif was phosphorylated"]. The other 89 rows are REMOVE: interactome screens, viral proteins, VAP family oligomers (already covered by GO:0042803/GO:0046982), and non-FFAT partners. Removing them does not mean the interactions are false.
- The three NOT rows from PMID:18713837 (ER organization, protein folding in ER, ER exit site) are now ACCEPT with summaries that describe the negation. Before, the text read as if it described a positive role.
- COPII-coated vesicle budding is now MARK_AS_OVER_ANNOTATED. The evidence is that VAPA overexpression inhibits budding, which is dominant interference and not participation [PMID:18713837 "overexpression of the two VAP isoforms causes retention of ER membrane proteins by impeding lateral diffusion and their incorporation into transport vesicles"]. ER-to-Golgi vesicle transport is now KEEP_AS_NON_CORE.
- Host-mediated suppression of viral genome replication is REMOVE. The cited abstract assigns suppression to VAP-C, a VAPB splice product, and says VAPA overexpression enhanced HCV replication [PMID:19515777]. The activation term is kept as non-core. Viral release remains UNDECIDED because there is no release assay in the cached text.
- Membrane fusion (TAS, PMID:9657962) is MARK_AS_OVER_ANNOTATED. It was speculation based on VAMP binding ("suggesting possible roles in vesicle fusion"). VAPA is a tether, not a fusion factor.
- NF-kappaB (HMP, PMID:12761501) is MARK_AS_OVER_ANNOTATED. It is an overexpression reporter screen hit.
- Ceramide metabolic process, sphingomyelin biosynthesis, cholesterol homeostasis and regulation of cholesterol transport are downgraded from ACCEPT to KEEP_AS_NON_CORE. VAPA is the ER-side FFAT receptor and catalyses none of these steps. The contact-site lipid transport terms (ceramide, sterol, cholesterol and phospholipid transport) remain ACCEPT under the scaffold/tether case of the participation test, because the transfer depends on the positioning that VAPA provides.
- Core functions: added a third core function, ER-endosome tether activity (GO:0170016) at ER-endosome contact sites [PMID:24105263 "they form an LE-ER tethering complex"], and directly_involved_in processes for the adaptor function. The description now says that VAPA has no intrinsic lipid-transfer activity.

Relative for follow-up: human VAPB (O95292), the nearest well-characterised paralog (PTHR10809:SF12). Mouse Vapa (SF155 ortholog) has only 3 experimental annotations, so it adds little beyond human VAPA. No VAPB review exists in the repo.

Modules: none in `modules/` reference VAPA (only deep-research artifacts mention it). GO-CAMs: gocams/682fbcd000003765 (ORP3/IQSEC1 focal adhesion; VAPA as GO:0043495) and gocams/682fbcd000003781 (OSBPL1A cholesterol transport).
