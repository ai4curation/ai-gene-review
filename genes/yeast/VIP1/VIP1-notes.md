# VIP1 (YLR410W) notes

UniProt Q06685, bifunctional PPIP5K: N-terminal ATP-grasp InsP6/InsP7 1-kinase (EC 2.7.4.24) and C-terminal histidine-acid-phosphatase-like domain [UniProt:Q06685].

## Kinase
- Identified as an IP6/IP7 kinase [PMID:17412958 "Vip1 and Asp1 acted as enzymes that encode inositol hexakisphosphate (IP6) and inositol heptakisphosphate (IP7) kinase activities"]. The 2007 paper originally assigned the new pyrophosphate to the 4/6 position.
- Positional specificity corrected to the 1/3 position (enantiomers not resolved in that work); UniProt and later literature give position 1 [PMID:18981179 "the VIP/PPIP5K enzymes convert inositol hexakisphosphate to 1/3-diphosphoinositol pentakisphosphate"]; with Kcs1 (IP6K) it makes 1,5-(PP)2-IP4 [PMID:18981179 "1/3,5-(PP)2-IP4 is the isomeric structure of the bis-diphosphoinositol tetrakisphosphate that is synthesized by yeasts and mammals"].
- => GO:0000830 (4-kinase) and GO:0000831 (6-kinase) IDA rows from PMID:17412958 are contradicted; GO:0052724 (3-kinase) reflects the unresolved enantiomer.

## Phosphatase domain
- Despite the UniProt CAUTION (predicted inactive), the isolated ScVip1 phosphatase domain is an active inositol pyrophosphate phosphatase [PMID:39966396 "ScVip1PD specifically hydrolyzes 1,5-InsP8 using a conserved phytase active site"]; also in [PMID:31436531 "We found that at low ATP concentrations the ScVip1 phosphatase activity predominates, releasing InsP6"]. Pi inhibits the phosphatase [PMID:31436531 "Pi inhibits the ScVip1-PD phosphatase activity, but promotes synthesis of InsP8 catalyzed by full-length ScVip1."].

## Phosphate signalling
- vip1 extracts fail to support Pho81-dependent inhibition of Pho80-Pho85 [PMID:17412959 "suggesting that Vip1 mediates synthesis of IP 7 relevant to the PHO system"].

## Location
- Cytoplasm (GFP; Huh et al.) [UniProt:Q06685]. Cytoskeleton call also from GFP screen; weak.

## ISS rows from S. pombe Asp1
- "regulation of bipolar cell growth" and "regulation of microtubule cytoskeleton organization" are transferred from Asp1 (O74429); fission-yeast-specific growth mode, no S. cerevisiae data.
