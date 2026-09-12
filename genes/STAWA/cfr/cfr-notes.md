# cfr notes

## 2026-06-13 AMR GO-gap review

Selected because Cfr illustrates a subtle but important specificity gap: the existing GO parent captures rRNA adenine methyltransferase activity, but the resistance-conferring Cfr activity is A2503 C8 methylation, not the RlmN-like C2 activity. UniProt A2AXI2 names the enzyme "23S rRNA (adenine(2503)-C(8))-methyltransferase" and says it specifically methylates position 8 of adenine 2503 in 23S rRNA [file:genes/STAWA/cfr/cfr-uniprot.txt]. The RNA paper identifies 8-methyladenosine as the Cfr product and states that resistance is provided by methylation at the 8 position [PMID:19144912].

The fetched GOA has several broad or wrong electronic terms. `GO:0016433` and `GO:0070475` are good current parents; tRNA modification/methylation should be removed for Cfr. The AMR mapping records `ARO:3000202` as `sssom:NoTermFound` because `GO:0070040` is the C2/RlmN activity and no C8-specific Cfr term exists [file:projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml]. The review proposes `23S rRNA A2503 C8 methyltransferase activity`.
