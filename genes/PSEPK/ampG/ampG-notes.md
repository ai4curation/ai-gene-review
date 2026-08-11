# ampG curation notes

- Q88N61 is a 515-aa multispanning AmpG-family permease
  [file:PSEPK/ampG/ampG-uniprot.txt, "Full=Muropeptide permease AmpG"].
- The P. putida pathway paper explicitly places AmpG-mediated import before
  cytoplasmic processing [PMID:28351914, "The transport of
  anhydro-muropeptides by the permease AmpG"].
- This supports pathway placement but is not a direct transport assay of
  Q88N61. Direct E. coli work shows that AmpG imports soluble muropeptides
  containing GlcNAc-anhMurNAc [PMID:12426329, "for a muropeptide to be imported
  by the AmpG permease, it must contain the disaccharide GlcNAc-anhMurNAc"].
- The live definition of GO:0015647 covers peptidoglycan transfer without the
  lipid-linked restriction of GO:0015648 [GO:0015647, "Enables the transfer of
  peptidoglycans, a class of glycoconjugates found in bacterial cell walls, from
  one side of a membrane to the other."]. Reviewed E. coli AmpG P0AE16 also has
  direct experimental QuickGO support for GO:0015647 from PMID:12426329, so the
  review uses the existing term without claiming a target-specific uptake assay.
