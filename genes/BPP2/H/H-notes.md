# BPP2 H (P26700 / FIBH_BPP2) Curation Notes

## Summary of Gene Function
- **Gene symbol**: `H`
- **UniProt ID**: `P26700` (`FIBH_BPP2`)
- **Protein**: Probable tail fiber protein gpH (669 aa, 71.5 kDa)
- **Organism**: Bacteriophage P2 (`NCBITaxon:2905681`)

## Literature Evidence
1. **PMID:1531648** (Haggård-Ljungquist et al., 1992, *J. Bacteriol.*):
   - Sequenced P2 gene `H` and demonstrated that `gpH` (669 aa, 71.5 kDa) is the bacteriophage P2 tail fiber protein, sharing conserved regions with the tail fiber proteins of phages Mu, P1, lambda, K3, and T2.
   - Showed that the C-terminal receptor-binding region of P2 `gpH` is highly similar to those of phages Mu and P1, explaining why P2, Mu, and P1 share host range specificity for the *Escherichia coli* lipopolysaccharide (LPS) core oligosaccharide.
   - Quote: `"Gene H probably codes for the distal part of the P2 tail fiber, since the deduced sequence of its product contains regions similar to tail fiber proteins from phages Mu, P1, lambda, K3, and T2. The similarities of the carboxy-terminal portions of the P2, Mu, ann P1 tail fiber proteins may explain the observation that these phages in general have the same host range."`
2. **PMID:12426340** (Christie et al., 2002, *J. Bacteriol.*):
   - Confirmed that `gpH` (and not `gpT`) is the P2 tail fiber protein.
   - Quote: `"Subsequent work, however, established gpH as the P2 tail fiber protein ( 13 )."`

## Annotation Review Decisions
- `GO:0019062` (`virion attachment to host cell`, IEA): **MODIFY** to `GO:0039638` (`lipopolysaccharide-mediated virion attachment to host cell`).
- `GO:0046718` (`symbiont entry into host cell`, IEA): **MODIFY** to `GO:0039638` (`lipopolysaccharide-mediated virion attachment to host cell`) — gpH mediates initial host recognition and attachment to LPS rather than membrane translocation/entry.
- `GO:0098015` (`virus tail`, IEA): **MODIFY** to `GO:0098024` (`virus tail, fiber`).
- `GO:0098024` (`virus tail, fiber`, IEA): **ACCEPT**.
- **NEW** `GO:0039660` (`structural constituent of virion`, IDA, `PMID:1531648`): gpH is the structural subunit of the P2 virion tail fibers.
- **NEW** `GO:0039638` (`lipopolysaccharide-mediated virion attachment to host cell`, ISS, `PMID:1531648`): gpH mediates virion adsorption to the host cell surface via its C-terminal LPS-binding domain shared with phages P1 and Mu.
- **NEW** `GO:0098004` (`virus tail fiber assembly`, IMP, `PMID:1531648`): gpH is required for assembly of the P2 tail fibers in cooperation with chaperone gpG.
