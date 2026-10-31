# lgt notes

## 2026-10-02

`just deep-research-falcon ECOLI lgt` could not run in this Orca environment because
`agentapi` was not available on `PATH` and no provider API keys were configured, so
this review uses the cached primary literature from `just fetch-gene` plus the
fetched UniProtKB record.

Manual synthesis:

- Lgt is an inner-membrane phosphatidylglycerol--prolipoprotein
  diacylglyceryl transferase. Mao et al. directly solved E. coli Lgt structures
  and report that "Phosphatidylglycerol:prolipoprotein diacylglyceryl
  transferase (Lgt) is an integral membrane enzyme that catalyses the first
  reaction of the three-step post-translational lipid modification"
  [PMID:26729647].
- The chemistry is the first committed lipidation step in bacterial
  lipoprotein maturation: Lgt transfers the diacylglyceryl group from
  phosphatidylglycerol to the conserved lipobox cysteine. Sankaran and Wu
  established that "lipid modification of prolipoprotein involves the transfer
  of diacylglyceryl moiety from phosphatidylglycerol to the sulfhydryl group
  of the cysteine residue with the concomitant formation of sn-glycerol
  1-phosphate" [PMID:8051048].
- The 2008 cytosolic-side annotation should not be treated as a separate core
  compartment. Selvan and Sankaran reported extraction behavior consistent with
  cytosolic-side association [PMID:18602442], but later topology and structural
  work place Lgt as a seven-transmembrane inner-membrane enzyme with a
  membrane/periplasmic catalytic cavity [PMID:22287519; PMID:26729647].
