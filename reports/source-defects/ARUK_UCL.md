# Source-record defects for ARUK_UCL

3 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P08246 enables GO:0002020 protease binding (IPI, PMID:6980881)
- **Field:** GO_ID
- **Change:** check GO:0002020 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/ELANE/ELANE-ai-review.yaml`

The BHF-UCL annotation represented by QuickGO UniProtKB:P08246!58684890 cites PMID:6980881 with UniProtKB:P08697. P08697 is SERPINF2/alpha-2-antiplasmin, a protease inhibitor rather than a protease or peptidase. The original directly demonstrates human leukocyte elastase cleavage and inactivation of that inhibitor, so the positive enzyme–substrate evidence does not support protease binding as defined by GO:0002020. Please check the source term and retain the demonstrated proteolytic evidence; no replacement specific binding term or mistaken source identifier is asserted.

- **Evidence reference:** PMID:6980881

## 2. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9UQL6 enables GO:0001216 DNA-binding transcription activator activity (IMP, PMID:19071119)
- **Field:** GO_ID
- **Change:** GO:0001216 → GO:0003713 (transcription coactivator activity)
- **Recorded in:** `genes/human/HDAC5/HDAC5-ai-review.yaml`

This IMP row gives HDAC5 DNA-binding transcription activator activity from PMID:19071119. The paper shows that HDAC4/HDAC5 bind the inhibitory domain of HIF-1alpha and increase its transactivation by displacing FIH-1 and favouring p300 binding. HDAC5 has no DNA-binding domain and DNA binding was not tested; the mechanism is that of a transcription coactivator (GO:0003713). GO usage guidance for GO:0003700 directs chromatin enzymes without a DNA-binding domain to transcription coregulator terms.

> These results indicate that HDAC4 and HDAC5 increase the transactivation function of HIF-1alpha by promoting dissociation of HIF-1alpha from FIH-1 and association with p300.
> — PMID:19071119

## 3. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9UQL6 enables GO:0140297 DNA-binding transcription factor binding (IPI, PMID:12242305)
- **Field:** GO_ID
- **Change:** check GO:0140297 (alternatives in the explanation)
- **Recorded in:** `genes/human/HDAC5/HDAC5-ai-review.yaml`

This IPI row (assigned by BHF-UCL) annotates DNA-binding transcription factor binding with WITH/FROM UniProtKB:Q61686 (mouse CBX5, HP1alpha). HP1 is a chromodomain heterochromatin adaptor that binds methylated histone H3, not a DNA-binding transcription factor, so the interaction in PMID:12242305 does not support GO:0140297. No specific GO term for HP1/chromodomain-protein binding was found; the interaction may be better left as a protein-binding row or dropped.

> Here we report that MITR, HDAC4, and HDAC5 associate with heterochromatin protein 1 (HP1), an adaptor protein that recognizes methylated lysines within histone tails and mediates transcriptional repression by recruiting histone methyltransferase.
> — PMID:12242305
