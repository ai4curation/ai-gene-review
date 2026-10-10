# gld1 (SPAC13F5.03c, UniProt O13702) notes

## Identity
- Glycerol dehydrogenase 1, EC 1.1.1.6, iron-containing alcohol dehydrogenase (GldA-type) family [UniProt:O13702 "Belongs to the iron-containing alcohol dehydrogenase"].
- Reaction: glycerol + NAD+ = dihydroxyacetone + NADH + H+ (RHEA:13769) [UniProt:O13702 "Reaction=glycerol + NAD(+) = dihydroxyacetone + NADH + H(+);"].
- Zn2+ cofactor from a 1.9 A crystal structure [UniProt:O13702 "Note=Binds 1 zinc ion per subunit."].
- PANTHER PTHR43616:SF5 (GLYCEROL DEHYDROGENASE 1). No S. cerevisiae ortholog: the budding-yeast glycerol dehydrogenase step is
  carried out by the unrelated aldo-keto reductase GCY1 (NADP-dependent) [PMID:20396879 "No equivalent of S. cerevisiae Gcy1/glycerol dehydrogenase has been identified in S. pombe."].

## Function / pathway
- Required for glycerol assimilation; first step of the DHA route (glycerol -> DHA -> DHAP by dak1/dak2)
  [PMID:20396879 "Deletion of gld1 caused a reduction in glycerol dehydrogenase activity and prevented glycerol assimilation."]
  [PMID:20396879 "The gld1 Delta cells grew on 50 mM DHA as the sole carbon source"].
- S. pombe cannot use glycerol as sole carbon source, but assimilates it alongside other carbon sources
  [PMID:20396879 "in the presence of other carbon sources such as galactose and ethanol, S. pombe could assimilate glycerol"].
- Classical genetics: glycerol-negative mutants that still grow on DHA lack glycerol dehydrogenase
  [PMID:3017714 "The first type of mutants was defective in glycerol dehydrogenase"]. The abstract does not map the mutation to gld1;
  PomBase curators made an IMP from this paper (defer to curator).
- Glucose-repressed, derepressed in scr1 and tup12 mutants [PMID:20396879 "We found that gld1 (+) was regulated by glucose repression"].

## Localization: unresolved
- UniProt subcellular location = Mitochondrion from the ORFeome YFP screen [UniProt:O13702 "SUBCELLULAR LOCATION: Mitochondrion"].
- PomBase instead asserts is_active_in cytosol by IC (GO_REF:0000111, from the ISS to bacterial GldA), and the PomBase GO-CAM
  gomodel:6796b94c00004743 places gld1 GO:0008888 in cytosol.
- Sequence check done during this review (python on the UniProt sequence): residues 1-45
  (MIGPRLCAATPRFPLVSLAHRNSKVFALASSNAVAQRWGKRFYAP) contain 7 Arg/Lys and no Asp/Glu; the first acidic residue is at
  position 47. E. coli GldA lacks this N-terminal extension. This is the composition of a mitochondrial presequence, which
  supports the HTP mitochondrial call. Localization therefore deserves experimental confirmation; I kept the mitochondrion
  IEA and left the cytosol IC undecided.

## Module context
- modules/glycerol_metabolism.yaml, dihydroxyacetone_route, glda_glycerol_dehydrogenase_activity annoton (GO:0008888).
  Module does not give a location for this annoton; GO-CAM says cytosol.
- No S. cerevisiae ortholog review to align with (budding yeast uses GCY1, GO:0047953, a different MF).
