# cheW (E. coli K-12, UniProt P0A964) review notes

## 2026-11-03 session

Deep research: `just deep-research ECOLI cheW --provider perplexity` failed ("Provider 'perplexity' not
available."). `just mod-description-deep-research ECOLI cheW`
skipped ("no MOD provider configured for organism 'ECOLI'"). Review based on cached publications
(most abstract-only; PMID:19547746 and PMID:25060668 full text) and the UniProt record.

Literature search: PubMed esearch queries via eutils for CheW/CheA/chemoreceptor array, CheW polar
localization; no additional PMIDs were needed beyond the GOA set.

### Key evidence
- CheW is the receptor-kinase coupling adaptor: [PMID:1326408 "Receptor directly bound CheW, but receptor-CheA binding was dependent upon the presence of CheW. These observations in combination with our previous identification of a CheW-CheA complex suggest that CheW physically links the kinase to the receptor."]
- Both binding arms are needed: [PMID:11923283 "mutations which eliminate CheW binding to Tar (V36M) or to CheA (G57D) result in a complete inability to form active ternary complexes in vitro and render the CheW protein incapable of mediating chemotaxis in vivo"]
- CheW-CheA binding: [PMID:1992467 "CheW and CheA exhibit reversible binding with the stoichiometry of two CheW monomers per CheA dimer."]
- Core unit stoichiometry: [PMID:21606342 "Purified complexes contained two receptor trimers of dimers and two CheW for each CheA dimer"]
- Receptor-dependent clustering at poles: [PMID:19547746 "Clustering of labeled CheW requires receptors since deletion of high-abundance chemotaxis receptors abrogated clustering of CheW (Figure 3H)."]
- Soluble pool: [PMID:334749 "the cheY, cheW, and cheA (66,000 daltons) polypeptides appeared only in the soluble cytoplasmic fraction"]
- Genetics: [PMID:353036 "Mutants defective in cheA, cheW, cheX, or cheY function swam smoothly, with little or no tumbling"]

### Decisions (27 rows)
- GO:0005515 protein binding (7 IPI): MODIFY -> GO:0060090 molecular adaptor activity for the
  mechanistic papers (PMID:11923283, 1992467, 21606342, 25060668); REMOVE for screens/surveys
  (PMID:16606699 pull-down, 19834901 Y2H, 6448631 crosslink to CheZ).
- GO:0019904 protein domain specific binding (Tsr): MODIFY -> GO:0060090.
- cytoplasm IEA: MODIFY -> cytosol (carried by IDA). cytosol IDA: ACCEPT.
- plasma membrane IDA x2: MODIFY -> GO:0009898 cytoplasmic side of plasma membrane (peripheral via receptors).
- chemotaxis IBA/IEA/IMP: ACCEPT (core).
- signal transduction (IBA, 2x IDA, IEA) and intracellular signal transduction IDA: MODIFY -> GO:0000160
  phosphorelay signal transduction system (CheW enables receptor control of CheA autophosphorylation/phosphotransfer).
- aerotaxis IDA: KEEP_AS_NON_CORE. cell tip IDA: KEEP_AS_NON_CORE.
- establishment of localization in cell IMP: MODIFY -> GO:0043113 receptor clustering (PMID:16856941).
- MCP complex IBA + 3 IDA: ACCEPT (definition names the connector protein).

Core function: GO:0060090 molecular adaptor activity (module MF supported). GO:0030674
protein-macromolecule adaptor activity is a more specific child that also fits; GO:0060090 used
to match the module annoton.
