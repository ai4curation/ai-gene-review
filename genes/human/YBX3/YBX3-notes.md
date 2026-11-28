# YBX3 notes

Automated deep research could not run in this workspace: Falcon and the
perplexity-lite fallback were unavailable to `deep-research-client`, and the
only installed provider (`claude_code`) reported a missing login. These notes
therefore record the manual literature pass over the GOA PMID rows and UniProt
text.

Human YBX3/DbpA/ZONAB is a Y-box cold-shock-domain protein with cytoplasmic and
nuclear pools. The original dbpA genomic paper reported cytoplasmic, nuclear,
and perinuclear immunofluorescence (PMID:7628487). The direct modern functional
evidence in GOA comes mainly from PMID:22711822: ZONAB binds specific sites in
the p21/CDKN1A 3'-UTR, and Rho/GEF-H1 signaling induces ZONAB-dependent p21
mRNA stabilization and translation in response to TNF-alpha and hyperosmotic
stress. Those rows support mRNA 3'-UTR binding, 3'-UTR-mediated mRNA
stabilization, positive regulation of cytoplasmic translation, and the cell
stress/survival process annotations as non-core but real.

The ZONAB tight-junction/perinuclear localization and small-GTPase-binding rows
come through ISS to non-human evidence in the same literature neighborhood; they
are plausible but peripheral to the nucleic-acid-binding activity. The
high-throughput PPP1CA and UXT isoform 1 IPI rows are removed only because they
assert bare `GO:0005515 protein binding`. The 2023 UXT paper identifies ZONAB
as a UXT-V1-interacting protein during intestinal epithelial differentiation
(PMID:37608570), but that partner does not warrant an unqualified molecular
function term on YBX3.
