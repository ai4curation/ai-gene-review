# PMAIP1 / NOXA manual notes

## 2026-09-30 apoptosis review

PMAIP1 encodes NOXA, a very short BH3-only BCL2-family apoptosis
regulator. It was originally identified as a p53-induced pro-apoptotic gene
whose BH3 motif controls mitochondrial localization, anti-apoptotic BCL2-family
binding, and caspase-9 activation [PMID:10807576 Noxa, a BH3-only member of the
Bcl-2 family and candidate mediator of p53-induced apoptosis, "When ectopically
expressed, Noxa underwent BH3 motif-dependent localization to mitochondria and
interacted with anti-apoptotic Bcl-2 family members, resulting in the activation
of caspase-9"]. Seo et al. then connected the BH3 and mitochondrial-targeting
regions to cytochrome-c release [PMID:14500711 The molecular mechanism of
Noxa-induced mitochondrial dysfunction in p53-mediated cell death, "two domains
(BH3 domain and mitochondrial targeting domain) in Noxa are essential for the
release of cytochrome c"].

The focused BCL2-family biochemistry makes NOXA an MCL1/BCL2A1-side inhibitor,
not a broad BIM/PUMA-like binder and not a well-established direct BAX/BAK
activator. Chen et al. found that "Noxa bound only Mcl-1 and A1" among the
tested mammalian pro-survival proteins, and that BAD plus NOXA cooperated
because they neutralize complementary pro-survival subsets [PMID:15694340
Differential targeting of prosurvival Bcl-2 proteins by their BH3-only ligands
allows complementary apoptotic function]. Willis et al. showed that NOXA can
bind MCL1, displace BAK, and promote MCL1 degradation, and explicitly noted
that NOXA itself was not detected binding BAX or BAK in that assay
[PMID:15901672 Proapoptotic Bak is sequestered by Mcl-1 and Bcl-xL, but not
Bcl-2, until displaced by BH3-only proteins, "Noxa itself does not directly bind
Bak or Bax"]. Han et al. placed NOXA upstream of the BIM-containing MCL1
checkpoint by showing that endogenous NOXA binding to MCL1 displaces endogenous
BIM [PMID:17374615 Functional linkage between NOXA and Bim in mitochondrial
apoptotic events].

NOXA-MCL1 binding is also linked to MCL1 turnover. Willis et al. reported that
the NOXA/MCL1 interaction promotes MCL1 degradation [PMID:15901672,
"Noxa could bind to Mcl-1, displace Bak, and promote Mcl-1 degradation"], and
Czabotar et al. found that NOXA, unlike BIM, induces proteasomal MCL1
degradation through a determinant in the NOXA BH3 sequence [PMID:17389404
Structural insights into the degradation of Mcl-1 induced by BH3 domains,
"Noxa is a BH3-only protein that can bind and trigger proteasome-mediated Mcl-1
degradation"]. This supports a non-core row to positive regulation of
proteasomal protein catabolism, but the portable molecular function remains
BH3-mediated inhibition of a pro-survival BCL2-family protein.

Several generic `GO:0005515 protein binding` rows should therefore become the
NOXA-side `pro-survival BCL2 family protein inhibitor activity` NTR already
proposed in the BIM and PUMA reviews. The current `GO:0051434 BH3 domain
binding` term is for the groove-side protein, such as MCL1, that recognizes a
BH3 helix; it is directionally wrong for the NOXA BH3 ligand. Lower-affinity or
contextual pro-survival partners are still in scope for this proposed
inhibitor activity: Smith et al. showed that full-length human NOXA has
selectivity but not absolute specificity for MCL1 and can also interact with
BCL2 in bortezomib-treated lymphoid cells [PMID:21454712 Noxa/Bcl-2 protein
interactions contribute to bortezomib resistance in human lymphoid cells],
while van de Kooij et al. directly tested NOXA co-IP with BCL2L10/Bcl-B
[PMID:23563182 Polyubiquitination and proteasomal turnover controls the
anti-apoptotic activity of Bcl-B, "Bim, Bik, Puma and Noxa interacted to a
similar extent with WT and K/R mutant Bcl-B"].

Some source rows are useful but contextual. The hypoxia paper makes PMAIP1 an
HIF1A-induced mediator of hypoxic cell death with ROS and cytochrome-c release
readouts [PMID:14699081 BH3-only protein Noxa is a mediator of hypoxic cell
death induced by hypoxia-inducible factor 1alpha, "Taken together, our data
indicate that Noxa induced ROS-dependent cytochrome c release and caspase-3
activation"], but ROS is a downstream readout, not NOXA's molecular function.
The glucose-starvation paper reports regulation of NOXA by Cdk5 and glucose,
cytosolic sequestration of the phosphorylated protein, and glucose-dependent
apoptosis in hematopoietic cancer cells [PMID:21145489 The proapoptotic
function of Noxa in human leukemia cells is regulated by the kinase Cdk5 and by
glucose]. Those glucose and phosphorylation rows should stay out of
`core_functions`.

Two existing annotations are likely straightforward over-annotations from
papers where NOXA was assayed or induced but was not the proximal effector. In
hypoxic syncytiotrophoblasts, the authors say that `puma` and `noxa` mRNA
levels were unchanged or slightly reduced, whereas BAD tracked the apoptotic
response [PMID:20810912 Hypoxia downregulates p53 but induces apoptosis and
enhances expression of BAD in cultures of human syncytiotrophoblasts,
"mRNA levels of both of these genes were unchanged or slightly reduced"]. In
glioblastoma cells treated with bortezomib plus TRAIL, NOXA is upregulated by
bortezomib, but the paper reports that NOXA knockdown did not protect the cells
and instead assigns the sensitizing mechanism to tBID stabilization
[PMID:21525171 Bortezomib primes glioblastoma, including glioblastoma stem
cells, for TRAIL by increasing tBid stability and mitochondrial apoptosis].

Reactome contributes both useful and noisy PMAIP1 rows. The NOXA translocation
event is relevant and correctly places the protein at the mitochondrial outer
membrane. By contrast, `TP53 stimulates PMAIP1 expression` and
`Transactivation of PMAIP1 by E2F1` are gene-expression events that should not
project cytosolic localization onto the NOXA protein.
