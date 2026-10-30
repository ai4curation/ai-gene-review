# SSK1 (YLR006C, UniProt Q07084) curation notes

## Identity

- Osmolarity two-component system protein SSK1; 712 aa; C-terminal CheY-like receiver
  (Response_reg, PF00072) domain at 505-647 with phospho-acceptor Asp554
  [file:yeast/SSK1/SSK1-uniprot.txt "DOMAIN          505..647"].
- Non-enzymatic response regulator: [file:yeast/SSK1/SSK1-deep-research-falcon.md
  "Ssk1 itself does not catalyze phosphorylation of Ssk2."]

## Phosphorelay (receiver function)

- Sln1-Ypd1-Ssk1 multistep phosphorelay: [PMID:8808622 "This phosphate is then
  sequentially transferred to Sln1p-Asp-1144, then to Ypd1p-His64, and finally to
  Ssk1p-Asp554."]; [PMID:8808622 "Ypd1p binds to both Sln1p and Ssk1p and mediates the
  multistep phosphotransfer reaction (phosphorelay)."]
- Original identification as a two-component system controlling the osmosensing MAPK
  cascade: [PMID:8183345 "Here we describe a two-component system in Saccharomyces
  cerevisiae that regulates an osmosensing MAP kinase cascade."]
- Logic is derepression: phosphorylated Ssk1 is inactive, unphosphorylated Ssk1 active.
  Phosphorylation-site or Ypd1-binding mutants are hyperactive [PMID:18573873 "In either
  case, unphosphorylated Ssk1 accumulates to activate Ssk2."].
- Ypd1-binding surface is the receiver alpha1 helix / beta1-alpha1 loop (E510, N512, I514,
  I518) [PMID:18573873 "all four of the Ssk1 mutants are completely incapable of binding
  to Ypd1, whereas they can bind to Ssk2."].

## Output: activation of the Ssk2/Ssk22 MAP3Ks

- [PMID:9482735 "The SSK1 C-terminal receiver domain interacts with an N-terminal segment
  of SSK2."]; [PMID:9482735 "Dephosphorylation of SSK2 renders the kinase inactive, but it
  can be re-activated by addition of SSK1 in vitro."] -> direct activator of a protein
  kinase (GO:0030295) and MAP3K binding (GO:0031435).
- UniProt: [file:yeast/SSK1/SSK1-uniprot.txt "SUBUNIT: Interacts with SSK2, SSK22 and
  YPD1."]
- Two-step model: Ssk1 binding relieves autoinhibition, Ssk2 then autophosphorylates and
  becomes Ssk1-independent (PMID:9482735 abstract).

## Self-inhibition / dimer

- [PMID:18573873 "Therefore, Ssk1 has a dual function as both an activator of Ssk2 and an
  inhibitor of Ssk1 itself."]; [PMID:18573873 "Thus, we conclude that the native form of
  Ssk1 in yeast cells is mostly dimeric."]. Model: Ssk1~P/Ssk1-OH heterodimers are
  inactive; only Ssk1-OH/Ssk1-OH dimers efficiently activate Ssk2. This explains why the
  SGD term "regulation of p38MAPK cascade" (not only positive regulation) fits.
- Homodimerization (GO:0042803) is experimentally supported (gel filtration, co-precipitation)
  but SGD curated this paper without adding it; left as a suggested question, not NEW.

## Turnover

- Unphosphorylated Ssk1 is degraded by Ubc7-dependent ubiquitin-proteasome system
  (Sato et al. 2003, PMID:12944490 per UniProt; not cached) [file:yeast/SSK1/SSK1-deep-research-falcon.md
  "Loss of UBC7 impairs Ssk1 degradation and delays Hog1 dephosphorylation, indicating
  that Ssk1 turnover contributes to pathway shutoff after osmoadaptation."]. Horie 2008
  did not detect significant degradation over their time course, and argues degradation
  is a slow (hour-scale) down-regulation mechanism.

## Localization

- Cytoplasm [PMID:14665464 "since Ssk1p appears to be cytoplasmically localized under all
  osmotic conditions tested."]; GFP signal weak, nuclear presence not excluded.

## Peripheral phenotypes

- Low-pH (pH 3.0) actin depolarization depends on the Sln1 branch of HOG
  [PMID:19633059 "Gene deletions on the Sln1p branch of the HOG pathway completely blocked
  actin depolarization, suggesting that Hog1p activation depends mainly on the osmosensor
  Sln1p."]. Abstract-only cache; SGD curator (full text) attributed IMP to SSK1. Ssk1 acts
  as the upstream signalling input; the actin effect is executed by Hog1 and polarisome
  proteins. Kept as non-core.

## Protein-binding (GO:0005515) rows

- Partners: SSK2 (P53599), SSK22 (P25390) -- both MAP3Ks -> MODIFY to GO:0031435.
- Partner YPD1 (Q07688; PCA PMID:18467557, Y2H PMID:18719252) is the phosphodonor Hpt
  protein; its binding is part of the response regulator activity already captured by
  GO:0000156. No informative binding MF exists for Hpt binding -> REMOVE (interaction is
  real and well-established, removal only drops the uninformative term).

## GO-CAM

- No SSK1 entry in gocams/index.tsv. Module modules/scer_hog1_cascade.yaml uses
  GO:0000156 for the Ssk1 tier.
