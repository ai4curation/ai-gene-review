# CG4793 / Q8IP30: an inactive protease-like domain in a long secreted protein

The frozen UniProt Q8IP30 sequence contains 910 residues and is identical to the independently fetched RefSeq NP_723941.2 sequence over its entire length. Its SHA-256 is `7d37eca0c1a415aee2585319ca4691c5ea2567988b7f90cb9debd34ec96fab16`. Both accessions identify CG4793 (FlyBase FBgn0028514); the UniProt record also names SPH208 and cSPH128. The RefSeq domain interval around 105–337 is a domain boundary, not a shorter protein length. This is accession/sequence confirmation, not proof of the historical sequence fed to ProtNLM or of the isoform specificity of RNAi experiments.

PROSITE places the sole annotated peptidase S1 domain at Q8IP30 residues 98–340; SignalP predicts residues 1–18 as a signal peptide. The sequence has a long, visibly repetitive C-terminal region extending beyond the peptidase-like domain. No second catalytic domain is annotated. Thus a 910-residue total length does not mean a second active protease compensates for defects in the N-terminal domain.

Global domain alignments to active trypsins P00760 and P00761 map the catalytic His, Asp and Ser to Q8IP30 Glu145, Asn191 and Gly290, respectively. In particular, the catalytic serine is replaced by glycine in the conserved local segment TCKGDGGAPLA. The two controls agree on all three mappings. P00760 aligns 218 residues (30.7% identity), covering 97.8% of its mature chain and 89.7% of the target domain; P00761 aligns 217 residues (31.3% identity), covering 97.3% and 89.3%, respectively. This is substantial domain coverage, not a short motif hit. The histidine region is more divergent and gapped; its precise positional homology is less secure than the well-aligned serine loop. Loss of the serine nucleophile alone strongly contradicts conventional S1 serine endopeptidase activity.

The positive-control alignment of P00761 to P00760 covers both mature chains completely, has 82.1% identity, and recovers the intact His48/Asp92/Ser185 catalytic triad in P00761. The same code therefore distinguishes a retained triad from the substitutions in Q8IP30.

These results support a pseudoenzyme interpretation and refute the intrinsic serine-type endopeptidase prediction for the exact selected Q8IP30 sequence. They do not establish the protein's ligand, direct molecular mechanism, or inability to regulate another protease. In particular, catalytic inactivity does not by itself refute participation in proteolysis as a biological process. The gene-level cellular-immunity experiments must be evaluated separately from the sequence analysis.

## Reproduction and checks

See [README](README.md), [script](align.py), [target results](target-alignment.json), and [active control](control-alignment.json). Inputs and download URLs are recorded in the README; no analysis result is encoded as a script output constant.

- [x] All input records and target domain coordinates are supplied as arguments; outcomes are computed.
- [x] The script was run on a different, active target, P00761.
- [x] Both target and control analyses completed successfully.
- [x] Raw results, alignments, input records, and sequence identity check are retained.
- [x] Conclusions distinguish sequence inference, annotation provenance, and experiments.
