# cao-1 (CAO1_NEUCR, Q7S860 / NCU07008) — review notes

## Summary of gene function

CAO-1 is one of two carotenoid cleavage oxygenase (CCO) family members encoded by
*Neurospora crassa* (the other is CAO-2). Despite the family name and the "carotenoid
cleavage oxygenase 1" designation it received when the genome was annotated, CAO-1 is
**not** a carotenoid-cleaving enzyme. It is a **non-heme Fe(II) dioxygenase that cleaves the
interphenyl Cα–Cβ double bond of the stilbenoid resveratrol** (and its dihydroxy derivative
piceatannol), yielding aromatic aldehyde products.

- **Molecular function:** stilbene/resveratrol cleavage dioxygenase. Cleaves *trans*-resveratrol
  → 3,5-dihydroxybenzaldehyde + 4-hydroxybenzaldehyde; cleaves piceatannol →
  3,5-dihydroxybenzaldehyde + 3,4-dihydroxybenzaldehyde. EC 1.13.11.- (incomplete). Uses a
  mononuclear non-heme Fe(II) center coordinated by four His (four-His CCO motif).
- **Biological process:** stilbene catabolism / degradation of the plant phytoalexin resveratrol.
  Expression is strongly induced by resveratrol and is light-independent — the opposite of the
  regulation of genuine carotenoid-pathway genes.
- **Localization:** presumed cytoplasmic (external resveratrol is degraded only intracellularly;
  no degradation halo around colonies, unlike secreted-laccase fungi). No direct GO CC annotation
  exists in GOA.

## Key experimental evidence

### PMID:23893079 (Díaz-Sánchez et al. 2013, Eukaryot Cell) — functional characterization
- CAO-1 was originally hypothesized to make retinal by cleaving β-carotene, but this was disproven:
  [PMID:23893079 "we tested CAO-1 activity with carotenoid substrates that were, however, not converted"]
- [PMID:23893079 "Here, we show that CAO-1 is not a carotenoid or apocarotenoid cleavage enzyme."]
- [PMID:23893079 "it efficiently cleaved resveratrol and its derivative piceatannol"]
- Substrate specificity is narrow: [PMID:23893079 "CAO-1 did not convert five other similar stilbenes, indicating a requirement for a minimal number of unmodified hydroxyl groups in the stilbene background"]
- Regulation opposite to carotenoid genes: [PMID:23893079 "adding resveratrol led to a pronounced increase in cao-1 mRNA levels, while light, a key regulator of carotenoid metabolism, did not alter them"]
- Δcao-1 mutants are not more sensitive to resveratrol; instead cleavage products may be mildly toxic (faster growth of Δcao-1 under sorbose + resveratrol). Basis for the NOT carotenoid-metabolism annotation.

### PMID:28493664 (Sui et al. 2017, Biochemistry) — structure & spectroscopy
- Crystal structures (PDB 5U8X/5U8Y/5U8Z/5U90/5U97) of CAO1 with iron and stilbenoid ligands.
- [PMID:28493664 "The crystal structure of a fungal stilbenoid-cleaving CCO, CAO1, reveals strong similarity between its iron center and those of carotenoid-cleaving CCOs, but with a markedly different substrate-binding cleft"]
- Iron center: [PMID:28493664 "Carotenoid cleavage oxygenases (CCOs) are non-heme iron enzymes that catalyze"] and four-His coordination: [PMID:28493664 "three to four His-derived imidazole units bound to the iron center in each enzyme, consistent with the known four-His coordination motif of CCOs"]
- Substrate (resveratrol/piceatannol) co-crystallized: [PMID:28493664 "Crystals of Co-CAO1 in complex with resveratrol and piceatannol were obtained"]; activity confirmed [PMID:28493664 "The enzymatic activity of CAO1 and NOV2 was assessed as previously described using either resveratrol or piceatannol as a substrate."]
- UniProt binding residues from this structure: resveratrol/piceatannol contacts at His133, His164, His383; catalytic Fe ligands His197, His248, His313, His510.

### PMID:29946976 (Sui et al. 2018) — metal-substituted CCOs; further cofactor characterization (referenced in UniProt COFACTOR, not in GOA).

## Annotation review decisions

| GO term | Evidence | Decision | Rationale |
|---|---|---|---|
| GO:0010436 carotenoid dioxygenase activity | IBA | **REMOVE** | Phylogenetic guess directly refuted by IDA: CAO-1 does not cleave carotenoids. Real MF captured by GO:0016702 IDA. |
| GO:0016121 carotene catabolic process | IBA | **MODIFY → GO:0046272 stilbene catabolic process** | Wrong substrate class; the real catabolic role is on stilbenes (resveratrol). |
| GO:0016702 oxidoreductase … two atoms of oxygen (IEA InterPro) | IEA | **ACCEPT** (KEEP_AS_NON_CORE not needed; core MF) | Correct dioxygenase parent term; consistent with IDA. |
| GO:0016116 carotenoid metabolic process — **NOT** | IDA | **ACCEPT** | Correct negative annotation; carotenoids explicitly tested and not converted. |
| GO:0016702 (IDA PMID:23893079) | IDA | **ACCEPT** | Best available MF term for the demonstrated dioxygenase activity. |
| GO:0016702 (IDA PMID:28493664) | IDA | **ACCEPT** | Structural + spectroscopic confirmation. |
| GO:0005506 iron ion binding | IDA | **ACCEPT** | Non-heme mononuclear Fe(II), four-His center, crystallographically defined. |
| GO:1905594 resveratrol binding | IDA | **ACCEPT** | Resveratrol co-crystallized in active-site cleft. |

## Notable point
This gene is a textbook example of a **misnamed/over-propagated family annotation**: the "carotenoid
cleavage oxygenase" family name and IBA propagation generated a carotenoid MF + process that
experimental work explicitly disproved. The curated GOA already carries the corrective NOT annotation,
and there is no dedicated GO MF term for stilbene/resveratrol dioxygenase activity (candidate new term).
