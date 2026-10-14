# ACL4 notes

## Full-gene specificity re-review, 2026-09-20

All 18 source rows were re-reviewed. Direct target evidence in PMID:26447800 supports Rpl4 capture, shielding, cytoplasmic/nuclear localization and delivery to pre-60S assembly. It states "We conclude that Acl4 has the capacity to recognize Rpl4 in a co-translational manner." This establishes cotranslational recognition but does not by itself settle the noncovalent folding step. PMID:19325107 remained abstract-only after full-text retrieval attempts, so its HGI folding annotation is UNDECIDED rather than rejected from a missing assay. The obsolete unfolded-protein-binding annotation remains MODIFY to the supported carrier-chaperone activity. All five mitochondrial IBAs were reconsidered against PTN002340064: the existing OpenScientist report computed zero transmembrane segments, but it omitted the source contributes_to qualifier on transporter activity. A soluble factor or peripheral complex contributor need not span the membrane. The report did not reconstruct a misplaced PAINT target branch or demonstrate target-specific loss of each activity. Established Rpl4 chaperoning alone is nonexclusive; the mitochondrial inferences are UNDECIDED pending the corrected focused assessment. Current PAINT does not contain the older targeting-sequence-binding row, a version discrepancy rather than biological refutation.

## 2026-10-01 mitochondrial IBA adjudication

Read the corrected OpenScientist mitochondrial-targeting/translocation report, newly cached full
text PMID:28148929, and newer cached PMID:35357307/PMID:39426497. The corrected report preserved
the GO:0008320 `contributes_to` qualifier and evaluated all five mitochondrial IBA rows together.
It still traced the assertions to TOM70/TOM71/TOMM70-style mitochondrial import receptors in
PANTHER:PTN002340064 rather than to target-specific Acl4 evidence. This settles the earlier
UNDECIDED holds: a soluble subunit could in principle contribute to transmembrane transport, but
Acl4 has no demonstrated mitochondrial localization, TOM/TIM/SAM/PAM interaction or import-pathway
phenotype, while direct studies show a soluble cytoplasmic/nuclear Rpl4 carrier-chaperone.

Changed GO:0005741, GO:0008320, GO:0030150, GO:0030943 and GO:0045039 to REMOVE with
PROPAGATION_BAD/WRONG_ORTHOLOG_OR_PARALOG source reviews. The obsolete GO:0030943 row is removed
without replacement: the mitochondrial targeting-sequence binding claim is stale in current PAINT
and target-specific structural work identifies the Rpl4 loop as the Acl4 client.
