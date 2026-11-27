# EGLN3 review notes

UniProt: Q9H6Z9 (EGLN3_HUMAN), gene EGLN3/PHD3. This workstream covers the
EGLN3 activity in GO-CAM `680ad14200007201`, where EGLN3 hydroxylates GPX4 and
blocks its chaperone-mediated autophagic degradation.

Automated deep research could not be generated in this checkout. The Falcon,
Perplexity and OpenAI recipes all resolved through an unavailable `agentapi`
provider surface, so the manual review below uses the cached UniProt record,
the GPX4 GO-CAM paper and selected primary substrate papers.

## Core chemistry

EGLN3 is an Fe(II)- and 2-oxoglutarate-dependent prolyl 4-hydroxylase. Its
UniProt FUNCTION comment summarizes the broad substrate scope as a "Prolyl
hydroxylase that mediates hydroxylation of proline residues in target proteins,
such as PKM, TELO2, ATF4, GPX4 and HIF1A" [file:human/EGLN3/EGLN3-uniprot.txt].
The original HPH/PHD paper identified a conserved family of HIF prolyl
hydroxylases [PMID:11598268 "We identified a conserved family of HIF prolyl
hydoxylase (HPH) enzymes"], and later in vitro work with the three human
HIF-P4Hs showed HIF1A/HIF2A/HIF3A peptide hydroxylation by the isoenzyme set
[PMID:12788921 "All the HIF-P4Hs hydroxylated peptides"].

PHD3 is not only a HIF-alpha enzyme. PKM2 is hydroxylated in a PHD3-dependent
fashion at Pro403/Pro408, and PHD3 knockdown reduces PKM2 coactivator function
[PMID:21620138 "PHD3 knockdown inhibits PKM2 coactivator function"]. HCLK2/TELO2
also associates with and is hydroxylated by PHD3 in the DNA damage response
[PMID:22797300 "HCLK2), associated with and was hydroxylated by prolyl"].

## GPX4 GO-CAM context

The model's EGLN3 activity uses `GO:0031545 peptidyl-proline 4-dioxygenase
activity`, has GPX4 and 2-oxoglutarate inputs, and nests the activity in
`GO:0050821 protein stabilization` and then `GO:0110076 negative regulation of
ferroptosis`. This agrees with PMID:40281343: the cached abstract says that
PHD3-mediated GPX4 Pro159 hydroxylation disrupts HSC70 binding and inhibits
autophagy-mediated degradation [PMID:40281343 "PHD3-mediated GPX4 proline 159
(P159) hydroxylation"; PMID:40281343 "disrupting its binding to HSC70 and
inhibiting autophagy-mediated degradation"].

The protein-stabilization process is the immediate annotation for the EGLN3
reaction. Negative regulation of ferroptosis is downstream but still
evidence-backed as `involved_in`, because the reaction prevents GPX4 loss and
the existing GOA row uses that qualifier. The gene review and model are
therefore consistent for the EGLN3 step.

## GOA fetch

The first `just fetch-gene human EGLN3` attempt returned only a GOA header even
though the 2026-11-04 UniProtKB record already listed curated GO cross-references
for cytoplasm, nucleus, cytosol, nucleoplasm, 2-oxoglutarate-dependent
dioxygenase activity, HIF-proline dioxygenase activity, peptidyl-proline
4-dioxygenase activity, negative regulation of ferroptosis, protein
hydroxylation and protein stabilization [file:human/EGLN3/EGLN3-uniprot.txt
"GO; GO:0031545; F:peptidyl-proline 4-dioxygenase activity; IDA:UniProtKB.";
file:human/EGLN3/EGLN3-uniprot.txt "GO; GO:0110076; P:negative regulation of
ferroptosis; IDA:UniProtKB."].

That first empty GOA file was a transient fetch failure, not evidence that the
annotations were missing upstream. A forced re-fetch on 2026-11-25 recovered 75
GOA rows and seeded 75 current GOA annotations for full review. The final
`EGLN3-ai-review.yaml` therefore reviews those existing rows directly rather
than proposing the GPX4 and HIF chemistry as `NEW`.
