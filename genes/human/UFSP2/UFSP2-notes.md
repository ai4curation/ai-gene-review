# UFSP2 (Q9NUQ7) research notes

## Summary
UFSP2 (UFM1-specific protease 2) is the principal human UFM1-specific cysteine (thiol-dependent) isopeptidase of the peptidase C78 family (catalytic Cys302). It acts in the UFM1 (ubiquitin-fold modifier 1) conjugation system, where it both processes pro-UFM1 to expose the activating C-terminal glycine and, predominantly, removes UFM1 from conjugated target proteins (deUFMylation). Documented substrates include the ribosomal protein RPL26/uL24, CYB5R3, DDRGK1, MRE11, TRIP4 and CD274/PD-L1. At the cytoplasmic surface of the endoplasmic reticulum, UFSP2 deUFMylates RPL26 on 60S ribosomal subunits, a step required to release the UFM1 E3 ligase complex and recycle 60S subunits after ribosome-associated quality control of stalled ER-translocating ribosomes. Through deUFMylation of CYB5R3 it modulates ER-phagy, and through TRIP4 it influences nuclear-receptor (estrogen receptor) transactivation. Loss-of-function and missense UFSP2 variants cause autosomal-dominant skeletal dysplasias (Beukes hip dysplasia, spondyloepimetaphyseal dysplasia) and a recessive neurodevelopmental/epileptic encephalopathy.

## Core functions (from review)
- **GO:0071567 deUFMylase activity** — UFM1-specific cysteine (thiol-dependent) protease that removes UFM1 from conjugated substrates (deUFMylation), most prominently RPL26/uL24 on ER-associated 60S ribosomal subunits, and also processes pro-UFM1; catalytic residue Cys302.
- **GO:0071567 deUFMylase activity** — deUFMylation of RPL26/uL24 releases the UFM1 E3 ligase from UFMylated 60S subunits, enabling recycling of 60S ribosomal subunits after ribosome-associated quality control of ribosomes that stall during co-translational ER translocation.

## Provenance
Research and verbatim supporting quotes are recorded inline in `UFSP2-ai-review.yaml` (per-annotation `supported_by` and `references` findings). This notes file summarizes the completed review; see the YAML for evidence citations.

## 2026-11-06 ORGANELLES ER batch 4 (endoplasmic reticulum rows)

- Rows: GO:0005783 IBA (is_active_in), IEA (GO_REF:0000120, located_in), IDA PMID:35926457 (is_active_in). All ACCEPT, kept.
- IBA: PAINT IBD on PTN008489070 (taxon 6072), seeds MGI:MGI:1913679, UniProtKB:Q9NUQ7 (self) and WB:WBGene00018160 (interpro/panther/PTHR48153/PTHR48153-paint.tsv).
- IEA: UniProt "Endoplasmic reticulum {ECO:0000269|PubMed:35926457}" plus mouse Q99K23.
- IDA: full text of PMID:35926457 [PMID:35926457 "we identify a role for localization of UFSP2 at the ER via its interaction with the ER resident protein ODR4 for its ability to remove UFM1 from RPL26"; "ODR4 is essential for stabilizing UFSP2 and anchoring it at the ER membrane in proximity to the ribosome."; "Moreover, UFSP2 and ODR4 knockout cell lines were an exact phenocopy in their role in restraining levels of RPL26 UFMylation"].
- is_active_in: justified on both rows; the activity (RPL26 deUFMylation) depends on ODR4-mediated ER localization.
- Topology: no TM or signal peptide; tethered to the cytosolic face by ODR4, so stays at root (no ER membrane row).

## 2026-11-11: tethering route (ORGANELLES rule 7)

The batch 4 call above ("stays at root") is superseded. Rule 7 now gives a soluble protein
stably tethered by an integral-membrane partner the cytoplasmic-side term. UFSP2 qualifies:
- no TM or signal peptide (UniProt features);
- partner ODR4 is a transmembrane ER protein [PMID:35926457 "UFSP2 interacts with odorant response abnormal protein-4 (ODR4), a transmembrane protein that is localized to the ER membrane"];
- endogenous UFSP2 depends on it [PMID:35926457 "UFSP2 protein levels are markedly reduced in ODR4−/− cell lines and vice versa"; PMID:38383785 "Because UFSP2 is unstable when separated from its oligomeric partner and membrane anchor ODR4"];
- it acts on membrane-bound 60S [PMID:38383785 "genetic ablation of UFSP2 leads to a substantial increase in UFMylation of membrane-associated uL24"].

Added a NEW GO:0098554 cytoplasmic side of endoplasmic reticulum membrane IC row; the three root
GO:0005783 rows stay ACCEPT, and the 60S-recycling core function names the cytoplasmic side.
The human ODR4 knockout result is loss of the protein rather than release to the cytosol, so no
off-membrane pool is evident; a partner-dependent release test exists for the worm proteins
(Chen 2014 Fig 8F, see the follow-up below); an ER-marker fractionation of UFSP2 itself is still missing (hence IC).

### 2026-11-11 review follow-up (PR #6297)

- The primary source for the ODR4-UFSP2 complex is Chen et al. 2014 [PMID:24603482 "Thus, ODR-4 and ODR-8 form a physical complex at the ER membrane."; "ODR-4 is a conserved tail-anchored transmembrane protein"], with overexpressed worm proteins in HeLa cells and a human ODR4-UfSP2 co-IP. The anchoring statements in PMID:35926457 ("thought to anchor") and PMID:38383785 ("membrane anchor ODR4 (ref. 2)") cite it, so they are not independent evidence.
- The cached text of PMID:35926457 does not say UFSP2 itself was blotted with an ER marker in its fractions; the location rests on the curated IDA row.
- The rule now requires direct evidence that the protein is at the organelle, a named integral partner, dependence on it, and (d) cytosolic synthesis with no signal, transit or TM feature. UFSP2 meets all four; for (c) the worm release test [PMID:24603482 "This was confirmed by demonstrating that ODR-8 was efficiently released from cells by permeabilization of the plasma membrane, but partially retained when co-expressed with ODR-4"] adds to the human destabilisation result. GO:0098554 is part_of GO:0005789, so it refines rather than avoids the membrane term.
