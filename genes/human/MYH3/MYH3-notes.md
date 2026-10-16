# MYH3 (human, P11055) curation notes

## Identity and expression

- MYH3 encodes myosin-3, the embryonic skeletal muscle myosin heavy chain (MyHC-emb), a class II
  sarcomeric myosin. Not to be confused with the unconventional class III myosin MYO3A/B (UniProt
  caution line).
- One of the first MyHCs transcribed in developing human skeletal muscle; re-expressed in regenerating
  fibres and in dystrophic muscle [PMID:2771643 "A 3.4 kb cDNA was isolated that encodes one of the
  first MHCs to be transcribed in human skeletal muscle development"; "Expression of this embryonic MHC
  is a hallmark of muscle regeneration after birth and is a characteristic marker of human muscular
  dystrophies."].
- Fetal skeletal muscle, essentially absent from heart and adult muscle [PMID:1691980 "The mRNAs
  corresponding to clones gtMHC-F and gtMHC-E are abundantly present in fetal skeletal muscle and are not
  present or barely detectable in heart and adult skeletal muscle."].
- Developmental isoforms MYH3 and MYH8 are downregulated after birth and re-expressed during
  regeneration [PMID:26180627 "Most of these genes are also expressed in the developing skeletal muscle,
  including two MyHC isoforms, called embryonic and neonatal (or perinatal) myosins, coded by MYH3 and
  MYH8, respectively"].
- Postnatal persistence in small spinal (interspinal) muscles in mouse [PMID:28205584 "In wild-type mice,
  there was persistent postnatal expression of embryonic myosin in the small muscles joining the neural
  arches of the spine"].

## Molecular function: direct evidence

- Recombinant human MyHC-emb expressed in C2C12 is an actin-activated ATPase that moves actin filaments
  in vitro [PMID:20080549 "In this study we describe a mammalian muscle cell expression system and the
  functional analysis of all six recombinant human type II skeletal muscle myosin isoforms."; "MyHC-Embryonic
  was also determined not to copurify with detectable associated light chains, but was capable of directing
  actin-filament motility"]. Lowest Vmax and slowest filament velocity of the human skeletal isoforms.
- Transient kinetics of human embryonic S1 (WT and FSS mutants R672H, R672C, T178I) [PMID:26945064 "Our
  data suggest that the WT embryonic myosin motor is similar in contractile speed to the slow type I/β
  cardiac based on the rate constant for ADP release and ADP affinity for actin-myosin."; FSS mutants slow
  the ATP hydrolysis step and Vmax: "These mutations therefore seriously disrupt myosin function."].
- Cross-isoform comparison of the ATPase cycle (embryonic vs perinatal and adult isoforms)
  [PMID:31387944 "The perinatal is distinct from the embryonic isoform"].
- Homologous R672C/H in embryonic myosin vs R671C beta-cardiac: divergent effects on molecular power
  (PMID:37425764, bioRxiv preprint, updated in PNAS 2024).
- Patient muscle (adult R672C carriers, where some residual embryonic-myosin expression is inferred)
  shows reduced specific force and slowed/incomplete relaxation [PMID:25740846 "In R672C-containing muscle
  cells, we observed reduced specific force, a prolonged time to relaxation and incomplete relaxation
  (elevated residual force)."].

Conclusion: core MF is microfilament motor activity (GO:0000146) with actin filament binding
(GO:0051015) and ATP hydrolysis (GO:0016887; the term note asks that the motor term also be annotated).
The Reactome-derived "myosin phosphatase activity" (GO:0017018) is the wrong term for the
"ATP Hydrolysis By Myosin" reaction (myosin phosphatase dephosphorylates phosphomyosin); the correct
term is ATP hydrolysis activity.

Light chains: UniProt subunit: hexamer of 2 MHC + 2 ELC + 2 RLC; IQ domain 782-811. MyHC binds the
EF-hand myosin light chains at its IQ lever arm, not calmodulin itself. Resnicow et al. note native
embryonic myosins copurify with light chains [PMID:20080549 "Historically, embryonic myosins fractionated
from muscle sources do copurify with associated light chains"]. The NAS calmodulin binding row is better
expressed as myosin light chain binding (GO:0032027).

## Structural role in the thick filament

- Myosin is "the essential part of the thick filament of striated muscle" [PMID:18695058].
- In mouse developing muscle the Ozz-E3 ligase recognises the rod of MyHC-emb within assembled sarcomeric
  thick filaments, marking it for replacement by neonatal/adult isoforms [PMID:20352047 "We present
  evidence that Ozz binding to the embryonic myosin isoform within sarcomeric thick filaments marks it for
  ubiquitination and proteolytic degradation, allowing its replacement with neonatal or adult isoforms."].
- Following MYH7, location is refined to striated muscle myosin thick filament (GO:0005863) and complex to
  muscle myosin complex (GO:0005859); GO:0008307 structural constituent of muscle proposed NEW (MYH8,
  MYH11 and invertebrate muscle myosins carry it per the MYH7 comparator check).

## Disease

- Dominant motor-domain missense variants: Freeman-Sheldon syndrome (DA2A) and Sheldon-Hall (DA2B3)
  [PMID:16642020 "A structure-function analysis shows that nearly all of the MYH3 mutations are predicted
  to interfere with myosin's catalytic activity."; "congenital contractures are a shared outcome of prenatal
  defects in myofiber force production"]. Additional variants in the ATP-binding pocket, mild myopathy
  postnatally (PMID:18695058).
- Dominant (missense/nonsense) and recessive (compound het, often hypomorph + null) MYH3 variants cause
  spondylocarpotarsal synostosis / CPSFS1A and CPSFS1B (PMID:28205584, PMID:29805041, PMID:35484034).
  Recessive DA without CPSFS features (PMID:38856159).
- Zebrafish smyhc1 R673H model of DA2A: notochord kinks, scoliosis, vertebral fusions; rescued by
  para-aminoblebbistatin, implying hypercontractile/ATPase-driven pathology [PMID:33016623 "Treatment of
  smyhc1R673H/R673H embryos with the myosin ATPase inhibitor, para-aminoblebbistatin, which decreases
  actin-myosin affinity, normalized the notochord phenotype."].
- Tail-domain variant association with atrial septal defect (case-control; PMID:32315303); chick eMYH
  knockdown gives atrial septal defects (PMID:21862559). Human cardiac role is not established (human
  heart expression barely detectable per PMID:1691980).

GO handling: limb/face morphogenesis IC rows derive from the contracture phenotype, which the source
paper itself attributes to defective fetal myofibre force production; these are downstream consequences,
not processes the myosin carries out. Marked over-annotated, consistent with MYH7's handling of
ventricular morphogenesis.

## Developmental roles in model organisms (non-core, judged on evidence)

- Myh3 null mice: altered fibre size, number and type, myogenic progenitor depletion via a
  non-cell-autonomous FGF mechanism; adult scoliosis [PMID:32094117 "Germline loss of MyHC-emb leads to
  neonatal and postnatal alterations in muscle fiber size, fiber number, fiber type and misregulation of
  genes involved in muscle differentiation."].
- Myh3 KO adults: scoliosis, vertebral fusion, reduced muscle weight and grip strength; YAP activation;
  YAP inhibitor partially rescues [PMID:37492882].
- MYH3 missense variants reduce TGFbeta signalling in transfected cells (PMID:28205584).

Judgement: these support a role in skeletal muscle organ development (the TAS muscle organ development
row is refined to GO:0060538 and kept non-core). The signalling effects (FGF, YAP, TGFbeta) are indirect
readouts of a contractile protein's loss and are not proposed as GO process annotations; they are raised
as questions.

## Deep research

- `just deep-research human MYH3 --provider openscientist` completed (MYH3-deep-research-openscientist.md
  plus artifacts; 2026-10-16, ~13 min). The falcon/Edison provider was not used because its
  authentication was failing on the day of curation.
- The report agrees with the primary literature on the core picture: actin-activated Mg-ATPase motor,
  A-band thick filament, hexamer with essential and regulatory light chains, developmental restriction and
  re-expression in regeneration, FSS variants slowing ATP hydrolysis.
- Points not adopted: the report states that fetal MYH3 contractile activity is "essential ... for proper
  joint and craniofacial morphogenesis". That describes the contracture phenotype, a downstream
  consequence of reduced fetal muscle force, so the limb and face morphogenesis rows stay marked
  over-annotated. It also calls patient-cell delayed myofibrillogenesis (PMID:26544689) a "direct
  structural/developmental role"; that is necessity evidence and is not used to assert sarcomere
  organization. Transcriptional regulators of Myh3 (Zeb1/Tle3, miR-501) act on the gene, not by it, and
  do not give MYH3 annotations.
