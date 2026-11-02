# Pld / A4UZ54

The selected A4UZ54 sequence has 1260 residues, whereas the cloned protein described in [PMID:17156430](https://pubmed.ncbi.nlm.nih.gov/17156430/) has1278. Both catalytic regions are retained in the selected record (592–619 and1072–1099), supporting transfer of the defining phospholipase reaction without assuming every published construct is identical. The article has cached full text; it reports “Pld localized to the cytoplasm and/or to cytosolic vesicles”. [PMID:15883198](https://pubmed.ncbi.nlm.nih.gov/15883198/) provides activity and catalytic-mutant evidence. ProtNLM lipid catabolism is CNN because the characterized phospholipase reaction already establishes the lipid-breakdown biology, while cytoplasm is LSP relative to cytoplasmic vesicle. Existing developmental and phototransduction phenotypes are retained as noncore consequences of the lipid-trafficking mechanism. Phosphatidylinositol binding remains unresolved at the exact ligand level. ARBA reaction and localization text is not independent validation.

## Sequence and research provenance

The selected frozen UniProt record is retained in [Pld-uniprot-source.json](Pld-uniprot-source.json), with the complete original prediction metadata in [Pld-predictions-source.json](Pld-predictions-source.json). It maps the exact accession to this FlyBase gene; current sequence identity does not establish the historical predictor input. Gene-level experiments support conserved functions unless a relevant isoform difference is established. Falcon research was requested with perplexity-lite fallback alongside publication caching. Primary publications and sequence observations, rather than AI summaries or ARBA assertions, support the curated conclusions.

## Provider readback

The completed Falcon report was inspected. Its conventional phosphatidylcholine-specific PLD identification and embryonic vesicle localization agree with inspected primary articles. It quotes the older 1278-residue construct; the selected A4UZ54 sequence is 1260 residues with both catalytic domains retained. The report also describes later photoreceptor recycling studies, which reinforce membrane trafficking but are not needed as independent evidence for the two broad predictions. The exact lipid-catabolism GO ID is absent from GOA, but its biological content is already captured by the characterized PC-hydrolysis reaction; CNN is appropriate without treating BP and MF terms as ontology parent/child.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This section was written without consulting any ProtNLM2 output or prediction-evidence files.

### Identity of the benchmark accession (A4UZ54)

- A4UZ54 (unreviewed, 1260 aa, RefSeq NP_724472.3) is one of several UniProt entries for FlyBase FBgn0286511 (Pld). No Swiss-Prot entry exists. The UniProt gene-centric canonical for the reference proteome is **B7YZT5** (1364 aa, NP_001137610.1); A4UZ54 is listed as a related protein of it. Q7KML4 and Q9BP35 (1278 aa) match the cDNA cloned in [PMID:17156430 "Pld encodes a 1278 amino acid protein"].
- A difflib alignment of the UniProt FASTAs shows that A4UZ54 is identical to Q7KML4 except for an **18-residue deletion after residue 338**, which falls near the C-terminal end of the PX domain (UniProt PX 146-355). B7YZT5 also carries an 86-residue N-terminal extension. A4UZ54 is therefore an **alternative splice isoform**, not a fragment.
- Both HKD catalytic motifs are retained in A4UZ54: HEKIVVID at 597 and HSKLLIAD at 1077, within PLD phosphodiesterase domains 592-619 and 1072-1099. The catalytic mutant H1095N in the 1278-aa numbering corresponds to H1077 here. Activity and trafficking conclusions are made at gene level, and nothing here shows they are isoform-specific.
- GOA attaches the same FlyBase experimental rows to A4UZ54, Q7KML4 and B7YZT5. Only the canonical B7YZT5 also receives the PAINT IBAs: GO:0004630, GO:0009395 phospholipid catabolic process, GO:0060627 regulation of vesicle-mediated transport, GO:0005886 plasma membrane and GO:0031410 cytoplasmic vesicle.

### Evolutionary placement

- The PANTHER HMM subfamily is PTHR18896:SF76 ("PHOSPHOLIPASE"). Its Swiss-Prot members in the cached inventory are yeast SPO14, S. pombe pld1, Dictyostelium pldB, Phytophthora PLD and Arabidopsis PLDzeta1. Human and rodent PLD1 are in SF57 and PLD2 in SF121.
- The PAINT tree places FBgn0286511 at node **PTN001051940** together with human PLD1 (Q13393), PLD2 (O14939), rat Pld1/2 and mouse Pld2. Regulation of vesicle-mediated transport, plasma membrane and cytoplasmic vesicle IBAs are propagated from that node. The PLD-activity IBA comes from the deeper node PTN004499769, which spans plant, fungal, bacterial and animal PLDs. So phylogenetically, fly Pld is the single metazoan PLD1/PLD2 co-ortholog, even though its HMM subfamily label groups it with SPO14/PLDzeta. This review transfers only the family-wide PLD activity (deep node) and PLD1/2-clade vesicle-trafficking roles, and fly-specific experiments support each of those claims.
- The family review interpro/panther/PTHR18896/PTHR18896-review.yaml lists A4UZ54 under SF76, which matches UniProt. Its SF76 description ("classical animal and plant PLDs") does not mention that the Swiss-Prot SF76 members are fungal, amoebozoan, oomycete and plant PLDzeta, or that human PLD1/PLD2 sit in SF57 and SF121 while the PAINT tree groups fly Pld with them. The placements do not conflict, but the description is imprecise.

### Literature used

- PMID:17156430 (full text): PLD activity in HEK293 cells, stimulated by carbachol and ARF1, absent in the H1095N mutant; vesicle localization; Golgi and Neurotactin trafficking defects; delayed cellularization; secondary gastrulation defects in 15 of 78 null embryos.
- PMID:15883198 (full text): reduced ERG sensitivity in the null (about 1.9% of control); localization to the photoreceptor cell body and rhabdomere base; Pld is not light-activated; rescue of norpA degeneration and rdgB signaling.
- PMID:27848911 (Thakur et al. 2016, newly cached, full text): dPLD3.1 null has no in vivo PEth; reduced retinal PA; light-dependent accumulation of Rab7-positive Rh1 vesicles; rescue by catalytically active Pld and by the independent PA source RdgA; Pld-driven clearance requires retromer (Vps35) and Arf1-GTP (garz). FlyBase does not cite this paper for GO.
- The Falcon deep-research report also mentions a 2024 Naik/Raghu domain preprint (PH domain needed for rhabdomere-base targeting; the PX domain binds PI3P). I did not read it, so it is not used as evidence.

### Changes relative to the previous review

- GO:0006629 lipid metabolic process: KEEP_AS_NON_CORE changed to MODIFY, with replacement GO:0006654 (an is_a descendant already carried).
- GO:0007030 Golgi organization: ACCEPT changed to KEEP_AS_NON_CORE. Pld is not at the Golgi at steady state, and the Golgi enlargement reads out a trafficking defect.
- GO:0010004 gastrulation involving germ band extension: KEEP_AS_NON_CORE changed to MARK_AS_OVER_ANNOTATED. This is a downstream phenotype that the authors attribute to cellularization defects.
- GO:0035091 phosphatidylinositol binding: UNDECIDED changed to KEEP_AS_NON_CORE. The GO definition explicitly includes phosphorylated derivatives, so the PX-domain inference fits.
- GO:0035556 intracellular signal transduction: ACCEPT changed to KEEP_AS_NON_CORE.
- NEW GO:2001137 positive regulation of endocytic recycling (IMP, PMID:27848911). Comparator check: the lipid enzyme PLA2G4E carries the term by IMP in human and mouse, and the catalytic-dependent rescue plus retromer epistasis show that Pld does work in the process. Declined: GO:0060627 (an ancestor of GO:0048215, so redundant) and GO:0005886 (embryonic staining was "not observed to localize specifically to the plasma membrane"; PM staining was seen only on overexpression in COS7). I also did not add GO:0009395 phospholipid catabolic process. It is an IBA on the canonical isoform and biologically true, but this review keeps to PA production as the stated process.
- Rewrote the description and split core_functions into the enzyme activity and the two trafficking roles.

### Relative to review next

Following the campaign rule, the canonical gene-centric product **B7YZT5** (1364 aa, same gene) has no review in the repo. It would go under genes/DROME/Pld__B7YZT5. The closest characterised ortholog by PAINT node PTN001051940 is human PLD1 (Q13393), which has no review in genes/human either.

### Modules

No module in modules/ models PLD-derived PA signaling or trafficking in animals. The yeast and pombe pld1 mentions in triacylglycerol_biosynthesis.yaml and cdp_dag_phospholipid_synthesis.yaml are out-of-scope notes, so neither module includes Pld as a part.
