# fliI (CC_3040, UniProt P0CAT8) - Caulobacter vibrioides CB15 - review notes

## Identity
- UniProt P0CAT8, 444 aa, locus CC_3040. UniProt RecName "Flagellum-specific ATP synthase", EC=7.1.2.2
  (translocase: ATP + H2O + 4 H+(in) = ADP + Pi + 5 H+(out); assigned from PROSITE PRU10106 ATPASE_ALPHA_BETA
  signature, ECO:0000255). This is the F-type ATP synthase EC, not the export-ATPase EC 7.4.2.8. Both the name
  and the EC are legacy homology-driven labels; FliI is not an ATP synthase.
- UniProt FUNCTION (ECO:0000250): "Probable catalytic subunit of a protein translocase for flagellum-specific
  export, or a proton translocase involved in local circuits at the flagellum." The second clause is an old
  hypothesis; no evidence supports FliI translocating protons.
- Domains: IPR005714 (ATPase T3SS FliI/YscN), IPR022426 / TIGR03498 (FliI clade 3), TIGR01026 (fliI_yscN),
  IPR004100 (F1/V1/A1 alpha/beta N-terminal), IPR000194 (nucleotide-binding), IPR040627 (T3SS ATPase C).
- PANTHER PTHR15184:SF9 ("SPI-1 TYPE 3 SECRETION SYSTEM ATPASE") per `interpro/panther/PTHR15184/PTHR15184-entries.csv`,
  i.e. in a FliI/SctN subfamily, NOT SF71 (F1-beta).

## Caulobacter-specific evidence
- [PMID:9286988 "The mutations in these strains mapped to an operon of two genes, fliI and fliJ, both of which are
  necessary for motility."] Mutants block flagellar assembly at an early stage; fliIJ is a class II flagellar operon.
- [PMID:9286988 "Subcellular fractionation showed that FliI is present both in the cytoplasm and in association with the membrane."]
- [PMID:9286988 "Mutational analysis of FliI showed that two highly conserved amino acid residues in a bipartite ATP binding motif are necessary for flagellar assembly."]
- Abstract only in cache; no purified P0CAT8 enzymology.

## Ortholog (Salmonella) mechanism
- ATPase: [PMID:8943245 "It had an ATPase activity of 0.16 s-1 at 25 degrees C and pH 7, and a Km for ATP of 0.3 mM; Mg2+ was required."]
  Not inhibited by F-, V-, P-type ATPase inhibitors.
- Structure: FliI resembles F1 alpha/beta [PMID:17202259 "the whole structure shows extensive similarities to the alpha and beta subunits of F0F1-ATPsynthase"].
- FliJ is gamma-like and sits in the FliI ring centre [PMID:21278755 "FliJ promotes the formation of FliI hexamer rings by binding to the center of the ring"].
  A rotary-like mechanism is proposed, but the ring is not coupled to an Fo-like proton channel.
- Energy: PMF drives export; proton flux through the export gate, not FliI.
  [PMID:18216858 "the energy of ATP hydrolysis being used to disassemble and release the FliH-FliI complex from the protein about to be exported"];
  [PMID:18216859 "the flagellar secretion apparatus functions as a proton-driven protein exporter and that ATP hydrolysis is not essential for type III secretion"];
  [PMID:21934659 "the export gate complex by itself is a proton-protein antiporter"];
  [PMID:29946050 "FlhA has an ion channel activity, and the FlhA-FliJ interaction enables effective utilization of PMF for protein export"].
- In vitro, ATP hydrolysis by FliI can drive some export without PMF [PMID:29946050 "ATP hydrolysis by FliI can drive the protein export without PMF."].

## Assessment of ATP-synthase-family annotations
- GO:0046933 (IEA TreeGrafter, PTN000390110): REMOVE. FliI does not synthesise ATP, has no Fo partner, sits in SF9
  outside the F1-beta clade (PTN008558586 seeds: E. coli AtpD, ATP5F1B, yeast ATP2, S. pombe atp2). PTN000390110 is
  not an IBD node in the cached PAINT table (`interpro/panther/PTHR15184/PTHR15184-paint.tsv`); likely a TreeGrafter
  graft point inheriting the F1-beta annotation - raised as suggested question.
- GO:0015986 (GO_REF:0000108 from GO:0046933): REMOVE, derived from a wrong MF.
- GO:1902600 proton transmembrane transport (InterPro2GO IPR004100): REMOVE. Proton flux in fT3SS runs via FlhA/export
  gate (a proton-protein antiporter); FliI is a soluble peripheral ATPase. Even the proposed FliI6-FliJ rotary
  mechanism has no proton channel in FliI.
- GO:0046034 ATP metabolic process (InterPro2GO IPR004100): MARK_AS_OVER_ANNOTATED - literal ATP hydrolysis only,
  as energy source for export; the mapping reflects ATP synthase biology.

## Other
- GO:0044781 flagellum organization -> MODIFY to GO:0044780 bacterial-type flagellum assembly (PMID:9286988).
- GO:0009288 flagellum -> MODIFY to GO:0120102 bacterial-type flagellum secretion apparatus (definition names FliI).
- NEW GO:0008564 protein-exporting ATPase activity (def covers Type III ATPases).
