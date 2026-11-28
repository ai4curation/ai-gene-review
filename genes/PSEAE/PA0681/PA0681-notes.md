# PA0681 (HxcT) — curation notes

## Identity

PA0681 is **HxcT**, the major pseudopilin of the *Hxc* type II secretion system of
*Pseudomonas aeruginosa* PAO1 — the organism's **second**, phosphate-regulated T2SS,
distinct from the quorum-sensing-regulated Xcp system. UniProt Q9I5P4 names it "Type II
secretion system core protein G" (GspG family) on ARBA evidence only; the gene-level
identification as HxcT comes from the Hxc literature.

The *hxc* cluster was named for being **h**omologous to **xc**p
[PMID:11985723 "In this study, we characterized a novel gene
cluster, called hxc for homologous to xcp"], and the same paper established that it is a
genuinely separate secretory pathway: an *hxcR* mutant grown under phosphate limitation
loses a 40 kDa supernatant protein that *xcp* mutants retain
[PMID:11985723 "The protein corresponded to the alkaline phosphatase L-AP, renamed LapA, which
is secreted in an xcp-independent but hxc-dependent manner"], and *hxc* expression is
phosphate-regulated. That was
[PMID:11985723 "the
first report of the existence of two functional type II secretory pathways
within the same organism"].

## Why HxcT is not simply "the Hxc XcpT"

This is the substantive finding about PA0681 and it is what the GOA IDA row rests on.
Major pseudopilins are normally interchangeable between T2SSs; HxcT and XcpT are the
exception [PMID:21586577 "Although major pseudopilins are exchangeable among type II secretion systems, we
show that XcpT and HxcT are not."]. Specifically
[PMID:21586577 "We demonstrate that HxcT does not form a hyper-pseudopilus and is different in amino acid
sequence and multimerization properties."] — the hyper-pseudopilus being the long
cell-surface structure a major pseudopilin builds when overproduced. The divergence is
narrow enough to be reversible by point mutation
[PMID:21586577 "Using structure-based mutagenesis, we observe that five mutations
are sufficient to revert HxcT into a functional XcpT-like protein, which also
becomes capable of forming a hyper-pseudopilus."], and the system as a whole is
horizontally acquired
[PMID:21586577 "Phylogenetic and experimental analysis showed that the whole Hxc system was acquired by P.
aeruginosa PAO1 and other Pseudomonas species through horizontal gene transfer."],
defining a new T2SS subfamily with Hxc as its archetype.

So HxcT *is* a T2SS major pseudopilin — the IBA and the IDA both hold — but its assembly
mode is the diagnostic character that separates Hxc from Xcp. Any annotation that
asserted XcpT-like pseudopilus formation for HxcT would be contradicted by this paper;
nothing in GOA does.

## Sequence

149 aa. The prepilin architecture is textbook: a short positively charged leader
`MDVVQFSSSPKGHRGQRG` (UniProt `SIGNAL 1..18`) ending in the Gly at which prepilin
peptidase cleaves, then the mature N-terminus `FTLIEIMVVVVILGILAAM...` with the
**invariant Glu at mature position 5** and the methylatable Phe1, followed by the
hydrophobic TM segment (`TRANSMEM 20..40`) and the GspG C-terminal domain
(`DOMAIN 41..147`).

UniProt carries a generic PROSITE caution
[file:PSEAE/PA0681/PA0681-uniprot.txt "Lacks conserved residue(s) required for the propagation of"]. **Do not over-read this.** It records that PROSITE declined to
propagate its N-methylation feature, not that the cleavage/methylation motif is absent —
and the motif above is canonical. It is tempting to tie the caution to the five divergent
residues of PMID:21586577, but those are different instruments measuring different things
and no published analysis connects them. Recorded here as an observation, not a claim.

## Annotation assessment

All six GOA rows are sound. Three assert `GO:0015627` (IBA, IDA, InterPro IEA) and two
assert `GO:0015628` (IBA, InterPro IEA); these reinforce rather than duplicate each other
and take the same action. `GO:0005886` plasma membrane is right: in a Gram-negative the
plasma membrane *is* the inner membrane where UniProt places the protein, and an
unassembled pseudopilin is an inner-membrane protein.

The IBA (`PANTHER:PTN000764351`) is seeded by XcpT (Q00514), XcpU (Q00515) and PA0681
itself. Per project policy the target's own appearance in `WITH/FROM` is expected and
marks experimental grounding on the target; it is not circular.

**No GO term exists for the pseudopilus itself** — no `pseudopilus` or T2SS-pseudopilus
class resolves in OLS or in the repository's GO snapshot. `GO:0015627` is therefore the
most specific available cellular-component term and needs no MODIFY. Raised as a
question rather than a proposed term, since the project has no second case to generalise
from.

## What is deliberately not annotated

Hxc secretes the alkaline phosphatase LapA [PMID:11985723 "The protein corresponded to the alkaline phosphatase L-AP, renamed LapA, which
is secreted in an xcp-independent but hxc-dependent manner"] and, in clinical isolates
carrying it instead, the DING/PstS-family protein LapC
[PMID:22835944 "We show that LapC is secreted in an Hxc-dependent manner and is under the control of
the PhoB response regulator."]; an *hxcR* mutant shows reduced rhamnolipid and pyocyanin
and altered biofilm
[PMID:40499597 "The results indicated that the hxcR mutation led
to a decrease in rhamnolipid and pyocyanin production by regulating phosphate
acquisition and the PhoR/PhoB two-component regulatory system."]. None of that becomes a process term for HxcT. The
pseudopilin does the work of **secretion**; the exported phosphatase does the work of
phosphate scavenging, and the regulatory and biofilm phenotypes are downstream of losing
the system. `GO:0015628` is the participation claim that HxcT actually earns.

## Provider deep research

Not available. `just deep-research PSEAE PA0681` was attempted with `--provider
perplexity` (provider not configured in this environment) and `--provider asta`
(HTTP 429 from asta-tools.allen.ai). Per project policy these notes stand in place of a
provider file rather than a hand-written file named as one.
