# TMF1 (TATA element modulatory factor 1) — research notes

## Context

This review was triggered by [geneontology/go-annotation#6381](https://github.com/geneontology/go-annotation/issues/6381) ("TMF1 annotation review"). Curators (V. Wood, H. Attrill, S. Munro group, L. Breuza, R. Lovering, P. Gaudet) flagged that the human TMF1 GO annotations are still dominated by transcription-related terms (transcription coactivator activity, androgen receptor signaling, positive regulation of transcription by RNA Pol II) that trace back to a small set of late-1990s/early-2000s overexpression studies, while the well-supported biology is now Golgi vesicle tethering (golgin) in retrograde and intra-Golgi vesicle traffic.

FlyBase already updated the *D. melanogaster* TMF1 ortholog to "vesicle membrane tethering activity" via P2GO (per @hattrill in #6381).

## Summary of evidence

### TMF1 is a golgin (vesicle tethering factor) on the trans-Golgi rim

- [PMID:17698061 "TMF signal surrounded Rab6-positive Golgi structures and immunoelectron microscopy revealed that TMF is concentrated at the budding structures localized at the tips of cisternae"]. Knockdown of TMF or Rab6 blocks retrograde transport of Shiga toxin from early/recycling endosomes to the TGN and causes Rab6-dependent displacement of GalNAc-T2 (but not GalT) from the Golgi. The authors conclude "critical roles for TMF in two Rab6-dependent retrograde transport processes: one from endosomes to the Golgi and the other from the Golgi to the ER."
- [PMID:23239882 "the COG complex interacts with two different Rabs in addition to each end of the golgin 'TATA element modulatory factor' (TMF). This allows COG to potentially bridge the distance between the distal end of the golgin and the target membrane thereby promoting tighter docking. Concurrently we show that the central portion of TMF can bind to Golgi membranes that are liberated of their COPI cover."]. Establishes TMF as the long coiled-coil tether that, together with the COG complex, mediates retrograde tethering of intra-Golgi vesicles.
- [PMID:28122620 "for six different golgins, the capture of carriers is mediated by a short region at the N-terminus of the protein... When relocated to mitochondria, TMF captures intra-Golgi transport vesicles, but these contain some proteins from later in the stack than those captured by GMAP-210 and golgin-84."]. Mitochondrial-relocation assay shows that TMF1 acts as a vesicle-capture (tethering) golgin. The first 36 residues of TMF are necessary and sufficient for intra-Golgi vesicle capture; the C-terminal coiled-coil with the Rab6-binding region also contributes capture activity.
- [PMID:36103876 "loss-of-function mutants show that the golgins are individually dispensable, although the loss of TMF recapitulates the male fertility defects observed in mice"]. Drosophila *in vivo* characterisation reaffirms TMF as an intra-Golgi vesicle-capturing golgin with conserved tissue-level functions.

### Mechanism / structure

- TMF is recruited to the Golgi membrane via a C-terminal Rab6-binding coiled-coil (UniProt SUBCELLULAR LOCATION; PMID:17698061; PMID:23239882; PMID:28122620). It contains predicted disordered N-terminus (~residues 1–400) followed by extensive coiled-coil (residues 439–922, 984–1092 per UniProt feature table).
- The N-terminal region has a conserved M-S-W-L/F motif shared with the other intra-Golgi tethering golgins GMAP-210 and golgin-84 [PMID:28122620 "the three golgins that capture intra-Golgi vesicles (golgin-84, GMAP-210 and TMF) share a short motif (M-S-W-L/F) at the very N-terminus"].

### Mouse phenotype consistent with Golgi/secretion role, not transcription

- [PMID:23000399 "TMF/ARA160 is a Golgi-associated protein, which is essential for spermiogenesis... lack of TMF/ARA160 leads to defects in both the testis and the epididymis... serum testosterone levels of TMF(-/-) mice were significantly lower than those of wt mice"]. The endocrine phenotype is consistent with disrupted Leydig cell secretion / spermiogenesis acrosome biogenesis (a Golgi-derived organelle), not with loss of a transcription coactivator.
- [PMID:24639530 "TMF/ARA160 is a multifunctional Golgi-associated protein, which accumulates in colonic enterocytes and goblet cells. Mice lacking TMF/ARA160 (TMF-/-) produce thick and uniform colonic mucus that resists adherent bacterial colonization"]. The colon mucus phenotype is consistent with disrupted Golgi-mediated mucin glycosylation/secretion.

### Transcription-related claims are weak and mostly overexpression-based

- [PMID:1409643 "TMF binds to the human immunodeficiency virus 1 TATA element in gel-retardation assays and inhibits activation of the viral long terminal repeat by the TATA-binding protein in in vitro transcription assays"]. The original cloning paper used HIV-1 LTR reporter and *in vitro* TBP assays; the protein was characterised in a viral context, not in regulation of endogenous cellular genes.
- [PMID:10428808 "Transient transfection assays demonstrated that ARA160 might function as a coactivator for AR-mediated transactivation in human prostate cancer PC-3 cells... ARA160 might represent the first identified androgen-enhanced N-terminal coactivator for the AR"]. Hedged language ("might function"); transient overexpression in PC-3 cells; a Gal4-DNA binding domain fusion to TMF1 reportedly does not work as a dbTF (data not shown), inconsistent with a *bona fide* transcription coactivator activity (GO:0003713 sensu stricto).
- [PMID:12044884 "TMF isoforms differentially localize in the Golgi apparatus and the nucleus"]. Reports interaction with hbrm/hSNF2α and BRG-1/hSNF2β SWI/SNF subunits. The bulk of TMF1 is at the Golgi; nuclear pool is a minor fraction.
- [PMID:15467733 "TMF/ARA160 is a Golgi resident protein whose cellular functions have not been conclusively revealed... TMF/ARA160 can direct the proteasomal degradation of the key cell growth regulator - Stat3"]. Reports a BC-box-mediated role in Stat3 ubiquitination; this is the basis of the regulation-of-proteasomal-protein-catabolic-process annotations.
- The 2025 Pharos status for TMF1 is "Tbio" (proteins with virtually no functional/drug characterisation), reflecting the field's view that transcription coactivator function is not solidly established.

## Implications for GO annotation

| Existing annotation (Aspect) | Recommendation | Rationale |
|---|---|---|
| GO:0005794 Golgi apparatus, GO:0000139 Golgi membrane (CC) | ACCEPT — core | Multiple IDA/IBA studies; UniProt SUBCELLULAR LOCATION; canonical golgin localization. |
| GO:0005829 cytosol (CC, TAS Reactome) | KEEP_AS_NON_CORE | Reflects diffuse cytoplasmic pool described in PMID:15467733; TMF is concentrated at Golgi. |
| GO:0005634 nucleus (CC, IEA) | MARK_AS_OVER_ANNOTATED | A minor isoform-dependent nuclear pool was reported (PMID:12044884) but the protein's primary localization is Golgi; the SubCell-derived IEA over-emphasizes this fraction. |
| GO:0005737 cytoplasm (CC, IEA) | KEEP_AS_NON_CORE | Generic; subsumed by Golgi/cytosol. |
| GO:0005783 endoplasmic reticulum (IBA, IEA-Ensembl) | MARK_AS_OVER_ANNOTATED | TMF mediates retrograde traffic *to* the ER but is not a steady-state ER-resident protein. |
| GO:0006891 intra-Golgi vesicle-mediated transport (NEW) | NEW | Strongly supported by PMID:28122620, PMID:23239882, PMID:36103876. |
| GO:0099041 vesicle tethering to Golgi (NEW) | NEW | Best existing BP for the golgin tethering activity (PMID:23239882, PMID:28122620). |
| GO:0006895 retrograde transport, Golgi to endoplasmic reticulum (NEW) | NEW | Established by PMID:17698061 (Rab6-dependent retrograde traffic). |
| GO:0042147 retrograde transport, endosome to Golgi (NEW) | NEW | Established by PMID:17698061 (Shiga toxin retrograde trafficking). |
| GO:0003713 transcription coactivator activity (IDA, PMID:10428808) | MARK_AS_OVER_ANNOTATED | Single overexpression study with hedged conclusions; Gal4-DBD fusion fails to transactivate; primary biology is at the Golgi. Demote from core; do not delete because a low-level moonlighting role cannot be excluded. |
| GO:0030521 androgen receptor signaling pathway (IDA, PMID:10428808) | MARK_AS_OVER_ANNOTATED | Same single overexpression study; mouse KO testosterone phenotype is more compatible with disrupted Leydig/spermiogenesis secretion than with cell-autonomous loss of an AR coregulator. |
| GO:0045944 positive regulation of transcription by RNA Pol II (IDA, PMID:10428808) | MARK_AS_OVER_ANNOTATED | Inferred from the same single transient transfection assay; not validated by orthogonal assays. |
| GO:0050681 nuclear androgen receptor binding (IPI, PMID:10428808) | KEEP_AS_NON_CORE | The far-Western/co-IP interaction is real, but is a moonlighting feature, not a core function. |
| GO:0061136 regulation of proteasomal protein catabolic process (ISS/IEA) | KEEP_AS_NON_CORE | PMID:15467733 supports a BC-box/Elongin-C-mediated role in Stat3 ubiquitination; this is a discrete moonlighting activity at the Golgi, not the core function. |
| GO:0005515 protein binding (IPI x2) | REMOVE / MARK_AS_OVER_ANNOTATED | Uninformative per project guideline. |

## Suggested new term

A molecular-function counterpart of GO:0099022 ("vesicle tethering" — currently a BP) would let us annotate golgins like TMF1, GMAP-210, golgin-84 and the GRIP-domain golgins to a meaningful MF beyond "protein binding". ValWood (#6381) referred to a prospective "vesicle membrane tethering activity" term (not yet present in GO at time of writing — GO:7770062 returned 404 from the GO API on 2026-05-02). Until such a term is added, GO:0099041 (vesicle tethering to Golgi) is the most informative existing BP, and we record the missing MF in `proposed_new_terms`.
