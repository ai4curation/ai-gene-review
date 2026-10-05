# Manual deep research: E. coli lnt

Falcon deep research was unavailable in this Orca environment because `agentapi`
was not on `PATH` and provider API keys were not configured. This manual
research note summarizes the cached evidence used for the E. coli `lnt` review.

`lnt` encodes the inner-membrane apolipoprotein N-acyltransferase that performs
the terminal acyl-transfer step in E. coli lipoprotein maturation. Gupta and Wu
identified apolipoprotein N-acyltransferase activity by assaying conversion of
apolipoprotein to mature lipoprotein, showed phospholipid stimulation of the
activity, and found the enzyme enriched in E. coli inner-membrane fractions
[PMID:2032623]. Robichon et al. showed that conditional `lnt` depletion causes
apolipoprotein forms of Lpp and other outer-membrane lipoproteins to accumulate
in the plasma membrane, and that E. coli Lnt has multiple membrane-spanning
segments [PMID:15513925].

Direct biochemical work purified E. coli Lnt and demonstrated thioester
acyl-enzyme intermediate formation plus N-acylation of apolipoprotein substrate
in vitro [PMID:21676878]. Two later structural studies solved Lnt structures and
placed the catalytic nitrilase-like domain on an integral membrane domain with
the active-site region facing the periplasmic side of the inner membrane
[PMID:28675161; PMID:28885614].

GO lacks a specific valid term for apolipoprotein N-acyltransferase/EC
2.3.1.269 after the old `GO:0016410 N-acyltransferase activity` term became
obsolete. The review therefore keeps the broad parent `GO:0016747
acyltransferase activity, transferring groups other than amino-acyl groups` as
the current molecular-function annotation and proposes a substrate-specific
child term. The high-throughput `GO:0005515 protein binding` rows from affinity
tagging and yeast two-hybrid interactome studies [PMID:15690043; PMID:24561554]
were removed as uninformative GO molecular-function assertions, without
claiming the physical-interaction evidence itself is false.
