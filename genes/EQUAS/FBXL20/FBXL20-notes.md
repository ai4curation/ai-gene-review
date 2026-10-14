# FBXL20 (donkey, A0A9L0IQA3) notes

## Sources
- Donkey UniProt A0A9L0IQA3 (unreviewed; names, subunit and location are ARBA predictions, ECO:0000256).
- Human ortholog Q96IG2 (genes/human/FBXL20/FBXL20-uniprot.txt) and human review genes/human/FBXL20/FBXL20-ai-review.yaml.
- Sequence comparison: FBXL20-bioinformatics/RESULTS.md.

## Biology
- FBXL20 is an F-box/LRR substrate receptor of SCF E3 ligases: [file:human/FBXL20/FBXL20-uniprot.txt "Substrate-recognition component of the SCF (SKP1-CUL1-F-box"]; [PMID:34731788 "an F-box protein that serves as a substrate recognition component of the SCF (Skp1_Cul1_F-box) E3 ubiquitin ligase complexes that promote proteasomal degradation"].
- Substrates: VPS34/PIK3C3 after DNA damage, leading to autophagy inhibition [PMID:33234069 "Removal of Vps34 by Fbxl20-mediated ubiquitination leads to inhibition of autophagy."]; PR55alpha/PPP2R2A, a PP2A regulatory subunit [PMID:34731788 "FBXL20 interacts with PR55α in vitro and in vivo"].
- FBXL20 is the paralogue of FBXL2 [PMID:33234069 "Fbxl20 is considered a paralogue for Fbxl2"].
- Mouse ortholog (Scrapper) acts at the presynapse (By similarity in human UniProt: "Role in neural transmission").

## Donkey sequence
- 97.25% identity over the full human length; 12-aa N-terminal insertion upstream of the F-box; C-terminal CAAX-type motif (…CCIIL) identical [file:EQUAS/FBXL20/FBXL20-bioinformatics/RESULTS.md].

## Decisions
- cytoplasm (SubCell mapping): ACCEPT.
- SCF ubiquitin ligase complex (TreeGrafter): ACCEPT.
- SCF-dependent proteasomal ubiquitin-dependent protein catabolic process (TreeGrafter): ACCEPT.
- NEW ubiquitin-like ligase-substrate adaptor activity (GO:1990756), matching the human review's MF.
