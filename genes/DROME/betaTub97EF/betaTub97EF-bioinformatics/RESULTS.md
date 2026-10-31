# BetaTub97EF exact isoform scope

## Audit Note

This report is retained as a narrow sequence-scope check, not as standalone
biological evidence for `betaTub97EF-ai-review.yaml`. It establishes that the
selected Q8MST5 sequence is identical to RefSeq transcript variant B and differs
from Q9VAX7 only across residues 177-223, while explicitly leaving the paper's
exon-4B/exon-4C transcript mapping unresolved. Use it only for that isoform
caveat; the curated microtubule-function review remains supported by the
primary betaTub97EF papers and conserved beta-tubulin chemistry.

Selected Q8MST5 is 457 residues and is identical to UniProt E1JIZ8 and the RefSeq translation NP_001163753.1 from NM_001170282.2, labeled transcript variant B. Alternate Q9VAX7 is also 457 residues and differs at 13 positions, from 177 through 223, with identical sequence outside that region. Individual differences are retained in results.json.

The 2017 primary paper distinguishes major exon-4B and minor exon-4C forms with different cold responses and overexpression toxicity. RefSeq transcript variant B is not automatically exon 4B, and the exact exon-name correspondence has not been independently established here. Thus cold-induced expression is assigned only to the paper’s major 4B transcript and the gene-level dominant response. Both tested forms retain tubulin function, including partial rescue of betaTub56D loss; their differing toxicity does not refute the broad microtubule-process prediction.
