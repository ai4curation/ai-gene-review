# ereB notes

## 2026-06-13 AMR GO-gap review

Selected because EreB has a simple, high-value enzyme mechanism but GOA only contained high-level antibiotic response. UniProt P05789 names EreB as "Erythromycin esterase type II" and states that it confers resistance by hydrolyzing the lactone ring of erythromycin [file:genes/ECOLX/ereB/ereB-uniprot.txt]. The original sequence paper reports that ereB confers high-level erythromycin resistance by inactivation in E. coli and that the data indicated ereB encodes an erythromycin esterase [PMID:3523438].

The broad parent `GO:0052689` carboxylic ester hydrolase activity is present in the UniProt flat file but not in the fetched GOA TSV. It is acceptable as an interim MF, but the AMR mechanism is macrolide lactone hydrolysis. The AMR mapping file records `ARO:3000320` macrolide esterase as `sssom:NoTermFound` [file:projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml]. The review proposes `erythromycin esterase activity`; scope may need expert choice between erythromycin-specific and broader macrolide lactone esterase.
