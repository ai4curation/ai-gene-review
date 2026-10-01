# UniProt / GO: NOT actin binding (IDA) on vinculin contradicts its cited paper

**Destination:** UniProt GO curation (the row is assigned_by UniProt,
2005-12-21), via the GO annotation tracker.

**Summary.** Human VCL (P18206) carries `NOT|enables GO:0003779 actin binding`
(IDA, PMID:7816144). The cited paper, "F-actin binding site masked by the
intramolecular association of vinculin head and tail domains", shows that the
tail has an F-actin binding site that head-tail association masks in the
closed molecule. That is autoinhibition, not absence of the activity. The
same paper's fragment data show actin binding.

Vinculin's actin filament binding is well established once activation
relieves this masking, for example by talin. This is also shown for sponge
vinculin (PMID:29880641).

**Requested change.** Withdraw the NOT annotation, or replace it with a
positive actin filament binding annotation (GO:0051015) qualified by the
activation requirement.

**Repo references.** `genes/human/VCL/VCL-ai-review.yaml` (REMOVE on the NOT
row; NEW actin filament binding IDA).
