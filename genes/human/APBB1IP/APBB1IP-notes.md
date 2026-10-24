# APBB1IP (RIAM) notes

## Biology
- RIAM is a Rap1-GTP effector adaptor of the MRL family [PMID:15469846].
  - Binds talin directly through its N-terminal helices; integrin activation needs both Rap1 and talin binding (human constructs) [PMID:19098287].
  - Rap1-RA-PH crystal structure, with Glu212 as the specificity determinant [PMID:24287201].
  - Unmasks the talin head [PMID:25520155].
  - Is part of the MRL-integrin-talin complex at protrusion tips [PMID:26419705].
  - Its PH domain binds PIP2, regulated by Src phosphorylation [PMID:33275877].
- T cells: binds SKAP-55, which relocalizes RIAM after TCR stimulation [PMID:17403904].
- Knockout mice:
  - Loss of leukocyte beta2-integrin activation [PMID:26337492].
  - Defective lymphocyte trafficking, with platelets intact [PMID:26324702].
- Focal adhesion disassembly [PMID:22946047].

## GOA calls
- **Cytosol:** 21 Reactome TAS rows, plus IBA, IEA and HPA IDA → ACCEPT.
- **Other locations accepted:** plasma membrane, focal adhesion, lamellipodium. Cytoskeleton (IEA) → MODIFY to actin cytoskeleton (review round).
- **IBA rows:**
  - Location rows come from MRL node PTN000133590 (mouse Apbb1ip, human RAPH1, human APBB1IP).
  - Adaptor and intracellular signal transduction come from deep node PTN001343226, seeded by Grb10/Grb14. Both accepted.
- **T cell receptor complex (IEA from mouse) → REMOVE.** RIAM sits in the separate ADAP/SKAP-55 module.
- **Protein binding:**
  - ZDHHC17 (Y2H screen) → REMOVE.
  - TRIM9 (PMID:22084112, abstract-only Drosophila Asap paper) → UNDECIDED.
- **NEW:** small GTPase binding (IDA), talin binding (IDA), positive regulation of integrin activation (IMP).
  - The comparator check for the last: RAP1B carries GO:0033625 (IMP), and FERMT3 carries GO:0033622. RIAM performs the talin recruitment and unmasking itself.
- Review round (PR #4154): signal transduction (IEA) → MODIFY to GO:0033625 positive regulation of integrin activation (it was redundant with the IBA).
