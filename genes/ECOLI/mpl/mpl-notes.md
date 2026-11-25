# mpl (P37773, b4233, yjfG) notes

## Identity
- UDP-N-acetylmuramate--L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptandioate ligase, murein peptide ligase, EC 6.3.2.45 (HAMAP MF_02020; TIGR01081; InterPro IPR005757; PANTHER PTHR43445:SF5). MurCDEF family, Mpl subfamily; closest paralog is MurC.
- No deep-research file; notes from cached publications, UniProt and web search. FEBA fitness fetch failed.

## Function
- Discovered by homology to murC; recycles intact murein tripeptide (accounts for >30% of new wall synthesis); null mutant lacks activity but is viable [PMID:8808921 "A null mutant totally lacked activity but was viable, showing that the enzyme is not essential for growth."].
- Purified His-tagged Mpl: accepts tri-, tetra- and pentapeptides with similar efficiency; L-Lys in place of DAP reduces efficiency [PMID:17384195 "Mpl was found to accept tri-, tetra-, and pentapeptides as substrates in vitro with similar efficiencies"; "Replacement of meso-diaminopimelic acid by L-Lys resulted in a significant decrease in the catalytic efficacy."]. In vivo, mpl/ldcA mutants show tetra- and pentapeptides are also directly reused.
- Kinetics: Km 0.25 mM UDP-MurNAc, 0.1 mM tripeptide, kcat 290 min-1; Mg2+ required (UniProt, ECO:0000269 PubMed:17384195).
- Barreteau et al. 2008 review (web full text): "Mpl participates in the recycling of peptidoglycan by adding the tripeptide l-Ala-γ-d-Glu-meso-A2pm onto UDP-MurNAc."
- Binds ppGpp in ITC as part of a ppGpp-affinity capture screen [PMID:30559427 "Such isotherms were seen in titrations of GmpA, Mpl, Gnd"]; regulatory consequence for Mpl not established.

## Location
- Cytoplasmic (substrates UDP-MurNAc and ATP are cytoplasmic; recovered peptide imported by AmpG / released by AmpD in the cytoplasm). UniProt has an unevidenced "SUBCELLULAR LOCATION: Secreted." line, which drives an IEA to extracellular region (GO:0005576) - a source error.

## Paralog over-propagation check
- GOA has no MurC (GO:0008763) or MurE-type terms on Mpl; only GO:0106418 plus generic ligase terms. IBA node PTN002881276 is Mpl-specific (GO:0106418, peptidoglycan turnover, cytoplasm), matching the module.

## Module
- `modules/peptidoglycan_recycling.yaml` mpl_step: GO:0106418, processes GO:0009254 + GO:0009252, family PTHR43445:SF5, P37773 representative, PTN002881276. Consistent with this review.
