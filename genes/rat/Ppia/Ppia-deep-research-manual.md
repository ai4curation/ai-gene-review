# Ppia (rat, P10111) - manual literature synthesis

No deep-research provider was available for this session. This synthesis was written by the
reviewer from cached publications, PubMed abstracts and the UniProt record; provenance is inline.

## Identity

- Rat peptidyl-prolyl cis-trans isomerase A (cyclophilin A, CyPA), 164 aa, RGD:3372, GeneID 25518.
- Single cyclophilin-type PPIase domain (Pfam PF00160; PROSITE PS00170/PS50072; PANTHER
  PTHR11071:SF490 "PEPTIDYL-PROLYL CIS-TRANS ISOMERASE A").
  [UniProtKB:P10111 "Belongs to the cyclophilin-type PPIase family. PPIase A subfamily."]
- Rat N-terminal processing / N-acetylvaline was shown directly (FT MOD_RES 2, ECO:0000269|Ref.7).

## Catalytic activity and cyclosporin A binding (rat protein, direct)

- Malouitre et al. 2009 (PMID:19832699, full text read) expressed and purified recombinant rat
  CyP-A: [PMID:19832699 "For CyP-A, the coding sequence in rat was PCR-amplified with the addition of
  BamH1 and EcoR1 restriction sites"]. They measured PPIase activity and its inhibition by CsA and
  analogues: [PMID:19832699 "The effects of these modifications of CsA on interactions with CyP-D and
  CyP-A were investigated by measuring PPIase inhibition."] and [PMID:19832699 "The binding affinities
  of CsA, SMBz-CsA and mtCsA to CyP-A were similar to those with CyP-D (Figure 1)."]
- The CsA-CyP-A complex inhibits calcineurin in vitro, whereas CyP-A alone slightly activates it:
  [PMID:19832699 "Figure 3 shows that, whereas CyP-A alone produced a small (20%) activation of
  calcineurin, the CsA–CyP-A complex inhibited calcineurin by approx. 70%."] Calcineurin inhibition is
  therefore a drug-gain-of-function property of the CyPA-CsA complex, as originally shown by Liu et al.
  [PMID:1715244 "the complexes cyclophilin-CsA and FKBP-FK506 (but not cyclophilin, FKBP,
  FKBP-rapamycin, or FKBP-506BD) competitively bind to and inhibit the Ca(2+)- and calmodulin-dependent
  phosphatase calcineurin"].

## Extracellular CyPA as a pro-inflammatory ligand (human/mouse evidence)

- Secreted CyPA signals through BSG/CD147 and heparans; signalling requires the rotamase active site
  [PMID:11943775 "we identified CD147 as a cell surface receptor for CyPA and demonstrated that CD147 is
  an essential component in the CyPA-initiated signaling cascade that culminates in ERK activation"];
  [PMID:11943775 "rotamase-defective CyPA mutants failed to initiate signaling events"]. CyPA is
  [PMID:11943775 "a potent neutrophil and eosinophil chemoattractant in vitro and in vivo"].
- CyPA is secreted by VSMC and macrophages in response to oxidative stress and LPS and activates
  endothelial cells [PMID:15130913 "CyPA is secreted from smooth muscle cells and macrophages in
  response to oxidative stress and lipopolysaccharide"]; [PMID:15130913 "Human recombinant CyPA
  activated mitogen-activated protein kinases, including ERK1/2, JNK, and p38 in cultured human
  umbilical vein EC."]; [PMID:15130913 "induced expression of adhesion molecules including E-selectin and
  vascular cell adhesion molecule-1"].

## Platelets (mouse knockout)

- [PMID:24429998 "CyPA-/- platelets exhibited dramatically decreased thrombin-induced platelet
  aggregation"]; [PMID:24429998 "Coimmunoprecipitation studies showed ROS-dependent increased
  association of CyPA and αIIbβ3. This association was dependent upon the PPIase activity of CyPA."]
- [PMID:22740452 "CyPA deficiency strongly blunted activation-induced Ca(2+) mobilization from
  intracellular stores and Ca(2+) influx from the extracellular compartment"].

## Intracellular signalling (UniProt, by similarity to human/mouse)

- Negative regulation of MAP3K5/ASK1, AKT1/NF-kB activation under oxidative stress, FOXO1
  interaction, TARDBP/hnRNP assembly: [UniProtKB:P10111 "Negatively regulates MAP3K5/ASK1 kinase
  activity, autophosphorylation and oxidative stress-induced apoptosis mediated by MAP3K5/ASK1"].

## Virus-related human annotations (donors for rat ISO rows)

Checked in QuickGO (2026-10-28) for human PPIA (P62937): negative regulation of viral life cycle rests
on influenza M1 papers (PMID:19207730, PMID:22347431); negative regulation of K48-linked ubiquitination
on AIP4-mediated ubiquitination of influenza M1 (PMID:30328013); positive regulation of viral genome
replication on HCV replication (PMID:19932913); lipid droplet organization and positive regulation of
protein secretion on HCV secretion with pan-cyclophilin inhibitors (PMID:21711559); plasma membrane
(EXP) on CyPA as a Mycoplasma genitalium adhesin receptor (PMID:29551599); protein-containing complex
on the calcineurin-cyclophilin-cyclosporin crystal structure (PMID:12218175). Mouse neuron
differentiation (IMP, PMID:16352598) comes from a Prp19 splice-variant study in P19 cells in which CyPA
was a two-hybrid partner and a reporter-assay transcriptional activator.
