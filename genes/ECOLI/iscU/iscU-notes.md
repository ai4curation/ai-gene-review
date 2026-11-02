# iscU (P0ACD4, E. coli K-12) notes

## Provenance of research

- Provider deep research could not run: `just deep-research-falcon` failed with an
  Edison API 403 authentication error in this container (2026-10-23). No
  `*-deep-research-*.md` file was created. Notes below are from the cached
  publications (`publications/PMID_*.md`) and the UniProt record.

## Function summary

- Scaffold for Fe-S cluster assembly on IscS: UniProt (curated, PubMed:11577100,
  22203963) ["A scaffold on which IscS assembles Fe-S clusters."]; the S-state
  "helps it dissociate from IscS to transfer the Fe-S to an acceptor".
- Sulfur transfer from IscS: [PMID:11577100 "IscS catalyzed transfer of (35)S from
  [(35)S]cysteine to IscU in the absence of additional thiol reagents"]; covalent
  disulfide between IscS Cys328 and IscU Cys63 [PMID:11972033 "We here report that a
  covalent bond is formed between Cys-328 of IscS and Cys-63 of IscU."]; IscU
  stimulates IscS [PMID:11972033 "IscU induced a six-fold increase in the cysteine
  desulfurase activity of IscS"].
- IscS-IscU heterotetramer structure [PMID:20404999 "We have determined the crystal
  structures of IscS-IscU and IscS-TusA complexes"].
- Cluster transfer (chaperone/carrier activity) [PMID:15964837 "Both IscU and IscA
  were found to be capable of multiple cycles of [2Fe2S] cluster formation and
  transfer"]; Michaelis-Menten kinetics with apo-ferredoxin.
- HscA/HscB client [PMID:10869428 "IscU and its iron-sulfur complex (IscU-Fe/S)
  stimulated the basal steady-state ATPase activity of Hsc66 weakly in the absence
  of Hsc20 but, in the presence of Hsc20, increased the ATPase activity up to
  480-fold."].
- [2Fe-2S] to [4Fe-4S] conversion on IscU [PMID:21799759 "the [2Fe-2S]2+ cluster
  dominates the mixture at short times ... but is progressively overwhelmed by the
  [4Fe-4S]2+ cluster as the reaction proceeds"].
- Not a free-iron binder: [PMID:15153099 "has no direct interaction with either Fe(II)
  or Fe(III) ions"]; [PMID:20942799 "IscU ... fails to bind any iron in E. coli cells
  under the same experimental conditions"]. Iron donors proposed: IscA
  (PMID:15247288), CyaY (PMID:19305405, as regulator), IscX (PMID:24810328),
  YtfE (PMID:33995335).
- Zinc stabilises fold [PMID:24917298 "zinc has a strong affinity for IscU"];
  copper toxicity target [PMID:28576762].

## Curation decisions (summary)

- Core MF: GO:0140132 iron-sulfur cluster chaperone activity; BP GO:0016226; CC
  cytosol; complex GO:1990330 IscS-IscU complex. Agrees with the Isc module.
- All 9 GO:0005515 rows REMOVE (protein-binding policy); interactions not disputed.
- iron ion binding / ferrous iron binding / intracellular iron ion homeostasis /
  L-cysteine catabolic process: MARK_AS_OVER_ANNOTATED.
- cytoplasm (IBA, IEA): MODIFY to cytosol. Fe-S cluster binding (IEA): MODIFY to
  2Fe-2S / 4Fe-4S binding and Fe-S cluster chaperone activity.
