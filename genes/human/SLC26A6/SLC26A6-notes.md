# SLC26A6 (Q9BXS9) review notes

Deep research: `just deep-research-falcon human SLC26A6` failed ("All providers failed"); literature reviewed
manually from PubMed and cached `publications/` files.

## Function
- Apical brush-border anion exchanger (PAT1/CFEX) of intestine, pancreatic duct, proximal tubule
  [PMID:20501439 "PAT-1 was functionally targeted to the apical membrane"].
- Exchange modes: Cl-/HCO3-, Cl-/OH-, Cl-/oxalate (human electroneutral; mouse electrogenic), low sulfate and 36Cl
  rates for the human protein [PMID:15548529 "the very low rates of (36)Cl(-) and [(35)S]sulfate transport by all
  active human SLC26A6 isoforms contrasted with the high rates of the mouse ortholog"].
- PDZ (NHERF) binding via C-terminal TRL [PMID:12444019]; CAII metabolon and PKC regulation [PMID:15990874].
- Oxalate uptake by human SLC26A6 also measured as positive control in PMID:40356774 (Drosophila Neat paper).

## Physiology and disease
- Mediates intestinal oxalate secretion; Slc26a6-null mice: hyperoxaluria, CaOx urolithiasis
  [PMID:16532010 "mice lacking Slc26a6 have a defect in intestinal oxalate secretion resulting in enhanced net
  absorption of oxalate"].
- Human: heterozygous dominant-negative p.R507W causes enteric hyperoxaluria with CaOx stones
  [PMID:35115415 "SLC26A6 inactivation can cause inherited enteric hyperoxaluria with calcium oxalate NL."];
  earlier cohort excluded SLC26A6 as a common cause [PMID:18951670].
- dismech counterpart: kb/disorders/SLC26A6-Related_Hyperoxaluria_and_Nephrolithiasis.yaml
  (GO:0019531 DECREASED; GO:0046724 oxalic acid secretion DECREASED).

## Notable decisions
- REMOVE mannitol transmembrane transport (ISS; neutral polyol, implausible substrate).
- Over-annotated: efflux transmembrane transporter activity, estrous cycle, response to fructose, response to IFN-gamma
  (SLC26A6 is the target of IFN-gamma downregulation, not an effector).
