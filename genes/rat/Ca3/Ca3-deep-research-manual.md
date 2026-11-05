# Ca3 (rat carbonic anhydrase III, UniProt P14141) - manual literature synthesis

No deep-research API was available for this session; this synthesis was assembled by hand
from the cached publications in `publications/` and PubMed searches (2026-10-28).

## Identity and family

- Rat Ca3 (RGD:2241, GeneID 54232) encodes carbonic anhydrase III (CA III), a 260-aa cytosolic
  member of the alpha-carbonic anhydrase family (Pfam PF00194; InterPro IPR001148, IPR023561;
  PANTHER PTHR18952:SF127). UniProt: "Belongs to the alpha-carbonic anhydrase family."
- The catalytic zinc is coordinated by His94, His96 and His119 (rat numbering), assigned from the
  crystal structure of S-glutathiolated rat liver CA III (PDB 1FLJ)
  [PMID:11024467 "The crystal structure of the S-glutathiolated CAIII from rat liver reveals covalent adducts on cysteines 183 and 188."].

## Catalytic activity

- CA III is a genuine CO2 hydratase but with low specific activity (~3% of CA II)
  [PMID:15509796 "especially its low specific activity, which is only ∼3% of that of Car2"].
- Recombinant rat liver CA III has the same CO2 hydratase specific activity as the native rat
  liver enzyme [PMID:10845711 "The purified recombinant had the same specific activity as the carbonic anhydrase purified from rat liver, but it had virtually no phosphatase activity."].
- CA III activity was measured directly in rat adipocytes, liver and fat by 18O mass spectrometry
  [PMID:8476041 "CA III enzyme activity measurements made by 18O mass spectrometry"], and in rat
  muscle post-mitochondrial supernatants [PMID:3133407 "CA III activity and content were assayed in the post-mitochondrial supernatant of the three muscles"].

## The phosphatase claim was retracted by its own laboratory

- Cabiscol & Levine (1996) reported a glutathiolation-regulated tyrosine phosphatase activity of
  CA III [PMID:8633035 "Phosphotyrosine is the preferred substrate, although phosphoserine and phosphothreonine can also be cleaved."].
- The same laboratory later showed the activity was a contaminant: recombinant CA III had
  "virtually no phosphatase activity" and further purification separated the two activities
  [PMID:10845711 "We conclude that the phosphatase activity previously considered to be intrinsic to carbonic anhydrase III is actually extrinsic."].
- Restated in the knockout paper [PMID:15509796 "Car3 had been thought to also possess intrinsic tyrosine phosphatase activity, but that was subsequently found to be due to a contaminating phosphatase"].

## Oxidative stress and S-glutathionylation

- CA III carries two reactive surface cysteines (Cys183, Cys188 in the crystal numbering) that are
  S-glutathiolated in hepatocytes under oxidative stress [PMID:11024467 "S-Glutathiolation of carbonic anhydrase III (CAIII) occurs rapidly in hepatocytes under oxidative stress."].
- Overexpression of rat CA III in NIH/3T3 cells lowered ROS and protected against H2O2-induced
  apoptosis [PMID:10064618 "Addition of exogenous H2O2 to cells induced a rapid increase of ROS in control but not in CA III overexpressing cells."],
  [PMID:10064618 "After a 16 h exposure to oxidative stress, the number of apoptotic cells was also reduced in transfectants."].
- shRNA knockdown of CA III in rat nucleus pulposus cells increased caspase-3-mediated death after
  H2O2 and had no effect on pH regulation [PMID:29559661 "Importantly, our results show that CAIII does not function as a classical carbonic anhydrase in regulating intracellular pH, but rather, functions as a potent antioxidant by sequestering ROS and protecting cells from oxidative stress-induced and caspase-mediated death."].
- However, Car3-null mice are viable, have normal lifespan and fat and respond normally to
  hyperoxia [PMID:15509796 "We found that mice lacking the protein had the same response to a hyperoxic challenge as did their wild-type siblings."].
  The organismal role of the antioxidant activity therefore remains unproven.

## Location

- Cytosolic: [PMID:15509796 "Carbonic anhydrase III is a cytosolic protein which is particularly abundant in skeletal muscle, adipocytes, and liver."];
  immunogold in muscle shows random cytoplasmic distribution, not myofibril-bound
  [PMID:3133407 "Immunoblotting of washed myofibril preparations did not show any detectable CA III associated with this structure."].
- Overexpressed rat CA III in NIH/3T3 cells was seen in cytoplasm and nuclei [PMID:10064618 "The protein was localized to cytoplasm and nuclei."].

## Expression responses (rat)

- Extremely abundant in adipocytes (24% of cytosolic protein in lean Zucker rat), decreased in
  obesity [PMID:8476041 "lean Zucker rat adipocytes may represent the richest source of CA III in nature"].
- Leptin decreases and insulin increases expression in adipocytes [PMID:15500001 "It was found that leptin decreased CA III expression while insulin increased it"].
- Strongly down-regulated in liver of ethanol-fed rats [PMID:19239903, PMID:23083309, PMID:25684186],
  by the dioxin-like PenCB [PMID:10900145], up-regulated by high-fat diet [PMID:35108454] and by hypoxia in
  NP cells [PMID:29559661].
- Leaks from muscle during contraction [PMID:1508229].
- Mouse CA III binds Ni/Zn on blots and Ni-chelate columns [PMID:9020864 "A 30 kDa Ni/Zn-binding polypeptide was found to be markedly decreased in the livers of the tx mice."].
