# SCP2 (human) — curation notes

UniProt: P22307 (SCP2_HUMAN). HGNC:10606. Gene *SCP2* on chromosome 1.

## Bifunctional gene / two protein products

The *SCP2* gene encodes two protein products from alternative promoter usage /
processing, sharing a common C-terminal SCP2 (sterol-carrier) domain:

- **SCPx (SCP-x, 58 kDa; isoform P22307-1)**: an N-terminal **thiolase domain**
  fused to a C-terminal SCP2 domain. It is a peroxisomal **3-ketoacyl-CoA
  thiolase** specialized for **branched-chain (2-methyl) fatty acids** and the
  **bile-acid C27 intermediates (DHCA/THCA)** — substrates the conventional
  peroxisomal thiolase (ACAA1) handles poorly.
  [PMID:17157249 "The SCP2 gene is translated into two protein products: SCPx, a 58 kDa fusion protein comprising an N-terminal thiolase domain and a C-terminal SCP2 domain, and preSCP2, a protein with a molecular mass of about 15 kDa, which is processed into its mature form (mSCP2) by proteolytic cleavage of a 20 residue leader sequence after translocation into peroxisomes"]

- **SCP2 (nonspecific lipid-transfer protein, nsLTP, ~13 kDa mature; isoform
  P22307-2)**: the C-terminal SCP2 domain alone, an intracellular
  **sterol/phospholipid/fatty-acyl-CoA carrier**. Made as preSCP2 (~15 kDa) and
  processed by cleavage of a 20-residue leader after peroxisomal import
  [file:human/SCP2/SCP2-uniprot.txt "preSCP2, a protein with a molecular mass of about 15 kDa, is processed into its mature form (SCP2) by proteolytic cleavage of a 20 residue leader sequence after translocation into peroxisomes"].

The displayed sequence in P22307 is the 547-aa SCPx form; the SCP2 domain is
residues ~433–543 (FT DOMAIN 433..543).

## Thiolase / branched-chain and bile-acid beta-oxidation (SCPx)

- SCPx is the branched-chain beta-ketothiolase that specifically cleaves
  3-oxopristanoyl-CoA — a role the conventional thiolase cannot fulfil.
  [PMID:9245689 "SCPx, a 58 kDa protein with both thiolase and sterol carrier protein activity but unknown function so far, readily reacts with 3-oxopristanoyl-CoA"];
  [PMID:9245689 "the conventional peroxisomal thiolase ... shows poor reactivity towards the 3-oxoacyl-CoA esters of 2-methyl branched-chain fatty acids such as pristanic acid"];
  [PMID:9245689 "SCPx plays a central role in branched chain fatty acid beta-oxidation in peroxisomes"].
- SCPx catalyzes the last (thiolytic) step of peroxisomal beta-oxidation of
  branched-chain fatty acids and of the bile-acid intermediates DHCA and THCA.
  [PMID:10706581 "Sterol carrier protein X (SCPx) plays a crucial role in the peroxisomal oxidation of branched-chain fatty acids"];
  UniProt FUNCTION [Isoform SCPx]:
  [file:human/SCP2/SCP2-uniprot.txt "Catalyzes the last step of the peroxisomal beta-oxidation of branched chain fatty acids and the side chain of the bile acid intermediates di- and trihydroxycoprostanic acids (DHCA and THCA)"].
- The specific thiolytic reaction (choloyl-CoA + propanoyl-CoA ⇌
  trihydroxy-oxo-cholestanoyl-CoA + CoA; EC 2.3.1.176) is the bile-acid step;
  the trimethyltridecanoyl/propanoyl reaction (RHEA:10408) is the pristanate step
  (GO:0050632). [file:human/SCP2/SCP2-uniprot.txt catalytic-activity blocks].
- SCPx (with the conventional thiolase) also participates in beta-oxidation of
  C24:6n-3 during DHA synthesis.
  [PMID:11734571 "the main enzymes involved in beta-oxidation of C24:6n-3 to C22:6n-3 are SCOX, DBP, and both 3-ketoacyl-CoA thiolase and SCPx"].

## Disease (SCPx / SCP2 deficiency = LKDMN, MIM 613724)

- First patient: torticollis, dystonic head tremor, cerebellar signs,
  leukencephalopathy, azoospermia; plasma pristanic-acid accumulation and
  abnormal bile-alcohol glucuronides in urine; thiolytic SCPx activity deficient
  and no SCPx protein by western blot; homozygous frameshift.
  [PMID:16685654 "the first known patient with a deficiency of sterol carrier protein X (SCPx), a peroxisomal enzyme with thiolase activity, which is required for the breakdown of branched-chain fatty acids"];
  [PMID:16685654 "Metabolite analyses of plasma revealed an accumulation of the branched-chain fatty acid pristanic acid, and abnormal bile alcohol glucuronides were excreted in urine"];
  [PMID:16685654 "In cultured skin fibroblasts, the thiolytic activity of SCPx was deficient, and no SCPx protein could be detected by western blotting"].

## Lipid-transfer / sterol-carrier function (SCP2 domain)

- SCP-2 transfers cholesterol and phospholipids between membranes; role in
  intracellular lipid trafficking.
  [PMID:15449949 "Sterol carrier protein-2 (SCP-2) facilitates cholesterol (Ch) and phospholipid (PL) transfer/exchange between membranes and appears to play a key role in intracellular lipid trafficking"].
- It can also traffic cholesterol- and phospholipid-derived hydroperoxides
  (LOOH), accelerating dissemination of peroxidative damage and promoting loss of
  mitochondrial membrane potential.
  [PMID:15449949 "SCP-2 accelerates 7alpha-OOH transfer from SUVs to isolated mitochondria and that this enhances peroxide-induced loss of the mitochondrial membrane potential"].
- SCP-2 binds cholesterol and phosphatidylinositol; the N-terminal presequence
  modulates ligand binding and targeting.
  [PMID:15182174 "Since sterol carrier protein-2 (SCP-2) binds both cholesterol and phosphatidylinositol"];
  cross-linking by photoactivatable free cholesterol and a mitochondrial
  presequence are described in [PMID:18465878].
- Direct high-affinity ligands include long-chain fatty acyl-CoAs (not the
  carnitine esters). [PMID:17418802 "The observation that LCFA-CoAs are high affinity ligands for SCP2 was confirmed, while LCFA-carnitines were demonstrated for the first time not to interact with SCP2"].
- SCP2 directly interacts with caveolin-1, implicated in trafficking cholesterol
  and PI to caveolae/rafts.
  [PMID:15182174 "SCP-2 (but not PITP) selectively interacted with caveolin-1, both within the cytoplasm and at the plasma membrane"].
- ER→PM cholesterol transfer role in fibroblasts; reduced in patient fibroblasts
  (UniProt FUNCTION [Isoform SCP2], PubMed:7642518, not cached here beyond
  UniProt).

## Localization / peroxisomal import

- SCP2 is a bona fide peroxisomal matrix protein (PTS1 = C-terminal -AKL), imported
  by PEX5; import is strictly PTS1-dependent.
  [PMID:21375735 "receptor-cargo binding and SCP2 transfer into the peroxisome are absolutely dependent on the presence of the PTS1"];
  the SCP2/PEX5 co-crystal is the model PTS1 receptor–cargo structure
  [PMID:17157249 crystal structure of Pex5p(C) with mSCP2].
- nsLTP is correctly localized to peroxisomes and processed to mature form even in
  RCDP fibroblasts.
  [PMID:1347505 "non-specific lipid transfer protein (nsLTP), another peroxisomal protein synthesised as a larger precursor, is localised in peroxisomes and is present as the mature protein in RCDP fibroblasts"].
- UniProt also records SCP2 (transfer form) in cytoplasm, ER and (weakly)
  mitochondrion; SCPx is peroxisome only.

## Notes on annotation actions

- Core MFs: **GO:0050632** (propionyl-CoA C2-trimethyltridecanoyltransferase =
  branched-chain 3-oxopristanoyl-CoA thiolase; has EXP support PMID:9245689,
  16685654, 11734571) and **GO:0120020** (cholesterol transfer activity, IMP).
  GO:0003988 / GO:0050633 are more-general or in-vitro chain-length variants of
  the same thiolase activity (ISS/IEA) — kept but non-core.
- Core BPs: fatty acid beta-oxidation (GO:0006635), bile acid biosynthetic /
  metabolic process, intracellular cholesterol transport / sterol transport.
- Bare "protein binding" IPIs (GO:0005515) and high-throughput interactome hits
  are marked over-annotated (not informative); the caveolin-1 and PEX5-related
  interactions are real but better captured elsewhere.
- Mass-spec "membrane" (HDA, NK-cell membrane proteome) and mitochondrion IEA/ISS
  are non-core / likely over-annotations for a peroxisomal matrix + cytosolic
  lipid-transfer protein.
