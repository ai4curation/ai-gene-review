# mib1 (Mind bomb 1, D-mib, Q9VUX2) — curation notes

Drosophila melanogaster, FBgn0263601, CG5841. 1226 aa. Domains: MIB/HERC2 domains and ZZ zinc
finger (N-terminal substrate-binding region), ankyrin repeats, C-terminal RING fingers.
PANTHER PTHR24202 (family name "E3 UBIQUITIN-PROTEIN LIGASE MIB2"), subfamily
PTHR24202:SF53 (E3 UBIQUITIN-PROTEIN LIGASE MIB1).

## Notch role: ligand E3 ubiquitin ligase (signal-sending cell)

- Positive Notch component required for Neur-independent events [PMID:15829515 "a Drosophila
  ortholog of Mind bomb (D-mib) is a positive component of Notch signaling that is required
  for multiple Neuralized-independent, Notch-dependent developmental processes."]
- Binds Dl and Ser; uses ligase activity to promote ligand endocytosis/activity
  [PMID:15829515 "D-mib uses its ubiquitin ligase activity to promote DSL ligand activity"].
- Wing margin, leg segmentation, vein determination; also modulates lateral inhibition
  [PMID:15760269].
- Required for Ser endocytosis in wing disc [PMID:15760269 "the activity of the D-mib gene is
  required for the endocytosis of Ser in wing imaginal disc cells."]
- Epsin-dependent pathway [PMID:15930117].
- neur mib1 double mutant abolishes signalling [PMID:16093323].
- Ubiquitylates Dl ICD with distinct docking site and lysine preference versus Neur
  [PMID:22162135]; six lysines needed, K742 most important [PMID:40050848 "a combination of
  six Ks in the ICD is required for the full activation of Dl by Mib1, with K742 being the
  most important one."]; follows rules found for human MIB1-JAG1 [PMID:40050848].
- Ubiquitylation by Mib1 releases ligands from cis-inhibition [PMID:28960177].
- Localization: cytoplasm and apical cortex [PMID:15760269 "D-mib co-localized with Ser, Dl,
  and N at the apical cortex"].
- Glycosphingolipid (alpha4GT1 product) suppresses mib1 loss [PMID:20176925].

## Pathway variant notes
- Mib1 is the broadly expressed ligand E3 (ubiquitous in wing disc); Neur is restricted.
  Vertebrates: MIB1 is the essential ligand E3 (zebrafish mib mutants), MIB2 minor.
- D. melanogaster also has Mib2 (FBgn0086442), a paralog seen in the IBA WITH list, which
  functions mainly in muscle integrity (not reviewed here).

## Annotation decisions
- REMOVE: GO:0005515 protein binding (x2 IPI with Dl P10041 and Ser P18168; uninformative).
- All other annotations accepted or kept as non-core.

## Deep research
- falcon run launched; if absent, it did not complete (rate limited API).

## Deep research (falcon) completed
- `mib1-deep-research-falcon.md` generated (retry with longer timeout). Consistent with the
  review; notes bipartite N-box/C-box ligand recognition by the MZM and REP domains (from
  mammalian MIB1-JAG1 structural work) and that Ser signalling is strictly Mib1/ubiquitin
  dependent whereas Dl retains weak ubiquitination-independent activity. Not independently
  verified from primary text here.
