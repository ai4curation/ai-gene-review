# rbpjb (Danio rerio, A4FTT4, Su(H)B) — curation notes

- Assigned gene was rbpja, but rbpja has no active UniProtKB entry: UniParc shows rbpja-labelled
  accessions Q6YLA3, Q561X6 and A4FTT3 are all inactive (deleted; B3DKP2/F6NXT8 merged into the
  deleted A4FTT3), and `just fetch-gene DANRE rbpja` fails. QuickGO symbol search for rbpja returns
  no zebrafish CSL. The only active zebrafish CSL entry is rbpjb (A4FTT4, annotation score 5), so
  the CSL review was done for rbpjb instead.
- PANTHER PTHR10665 (RECOMBINING BINDING PROTEIN SUPPRESSOR OF HAIRLESS), no subfamily.
- NICD binding: [PMID:21871448 "Wt1a, Foxc1a, and Rbpj can physically interact with each other,
  whereas only Rbpj binds to the Notch intracellular domain (NICD)"]
- Knockdown: [PMID:17098223 "Combined Su(H) gene knockdown caused defects in visceral left/right
  asymmetry, neurogenic lateral inhibition, and symmetrical failure of the segmentation
  oscillator."] Morpholino studies often target both paralogs.
- IBA nodes: PTN000071433 (nucleus, DNA-binding TF activity, cis-reg DNA binding); PTN002580211
  (Notch signaling pathway, MAML1-RBP-Jkappa-ICN1 complex).
- Deep research: first falcon attempt failed (template variables missing, UniProt 429), relaunched.
