# Usp12-46 review notes

Accession: Q9VCT9. Module: dmel_usp46_deubiquitinase_complex.

## Literature journal

- Complex and Wg role: [PMID:37798281 "We demonstrate that stabilization of the essential Wingless/Wnt receptor Arrow/LRP6 by the evolutionarily conserved Usp46-Uaf1-Wdr20 deubiquitylase complex controls signaling strength in Drosophila."]
- Mechanism: [PMID:37798281 "By reducing Arrow ubiquitylation and turnover, the Usp46 complex increases cell surface levels of Arrow"]; activators [PMID:37798281 "WDR20 and UAF1 potentiate the activity of USP12 and USP46 by allosterically increasing their catalytic efficiency without increasing their substrate-binding affinity"]; [PMID:37798281 "Wdr20, and to a lesser extent Uaf1, stabilized Usp46, as knockdown of either Uaf1 or Wdr20 reduced Usp46 levels"].
- Notch (Usp12-46): [PMID:22778262 "we identified mammalian USP12 and its Drosophila melanogaster homolog as novel negative regulators of Notch signaling"].

## Decisions (shared across the three subunits)

- GO:1905368 peptidase complex, GO:0090263 positive regulation of canonical Wnt signaling and GO:2000059 negative regulation of ubiquitin-dependent catabolism: ACCEPT for all subunits (no more specific complex term exists in GO).
- Uaf1/Wdr20 core MF GO:0035800 deubiquitinase activator activity (own), contributes_to GO:0004843; Usp12-46 core MF GO:0004843 (own catalytic).
- Usp12-46: GO:0101005 -> MODIFY to GO:0004843; GO:0031647 -> MODIFY to GO:0050821 protein stabilization.
- Uaf1 ubiquitin binding (yeast-donor IBA/ISS) and DSB repair (IBA) kept as non-core.
