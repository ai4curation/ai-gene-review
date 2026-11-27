# PA0685 (HxcQ) — curation notes

## Identity

PA0685 is **HxcQ**, the secretin (GspD family) of the *Hxc* type II secretion system of
*Pseudomonas aeruginosa* PAO1 — the outer-membrane channel of the organism's second,
phosphate-regulated T2SS. UniProt Q9I5P0 calls it only "Probable type II secretion system
protein" (a submitter name), but the record places it in the bacterial secretin family,
GSP D subfamily, and the GOA IDA row cites the paper that characterised it under the name
HxcQ.

The system it belongs to was defined in [PMID:11985723 "In this study, we characterized a novel gene
cluster, called hxc for homologous to xcp."], which also identified its substrate: an
*hxcR* mutant under phosphate limitation loses the alkaline phosphatase LapA from the
supernatant while *xcp* mutants retain it. Hxc also exports, in clinical isolates carrying it
instead of LapA/LapB, the DING/PstS-family protein LapC
[PMID:22835944 "We show that LapC is secreted in an Hxc-dependent manner and is under the control of
the PhoB response regulator."].

## The interesting part: HxcQ is a liposecretin

Secretins are large multimers that form the outer-membrane pore, and getting them there
normally requires a dedicated **pilotin**. HxcQ does without one. The GOA IDA row's paper
shows, in order: that HxcQ behaves as a secretin
[PMID:19815547 "We found that HxcQ forms high molecular mass structures resistant to heat and
SDS, revealing its secretin nature."]; that it is lipidated
[PMID:19815547 "Interestingly, we showed that HxcQ is a lipoprotein."]; that the lipid is
required, not decorative
[PMID:19815547 "Construction of a recombinant nonlipidated HxcQ (HxcQnl) revealed that lipidation is
essential for HxcQ function."]; and — the diagnostic result — that removing the lipid
reproduces the phenotype of a secretin stranded without its pilotin
[PMID:19815547 "Further phenotypic analysis indicated that HxcQnl accumulates as multimers in the
inner membrane of P. aeruginosa, a typical phenotype observed for secretins in the absence
of their cognate pilotin."]. Hence
[PMID:19815547 "Our observations led us to the conclusion that the lipid anchor of HxcQ plays a pilotin
role."], confirmed heterologously
[PMID:19815547 "The self-piloting of HxcQ to the OM was further confirmed by its correct multimeric OM
localization when expressed in the heterologous host Escherichia coli."].

Note what the nonlipidated mutant does: it still **multimerises**, just in the wrong
membrane. So lipidation is a targeting determinant, not an assembly determinant — the ring
builds either way.

## Sequence corroboration

803 aa. UniProt independently predicts exactly the lipoprotein the paper demonstrated:
`SIGNAL 1..27`, `CHAIN 28..803`, and two LIPID features on residue 28 —
[file:PSEAE/PA0685/PA0685-uniprot.txt "N-palmitoyl cysteine"] and
[file:PSEAE/PA0685/PA0685-uniprot.txt "S-diacylglycerol cysteine"], from PROSITE-ProRule
PRU00303. The sequence shows the canonical lipobox: residues 25–28 are `V-A-A-C`, fitting
[LVI][ASTVI][GAS]C, with Cys28 the lipidated residue and the first residue of the mature
chain. Two independent instruments, one experimental and one sequence-based, agree.

Domain architecture is a textbook secretin: GspD-like N0 (104–173), three NolW-like
ring-building domains (199–259, 262–331, 339–482) and the secretin β-barrel domain
(566–732).

## Annotation assessment

Eight rows, and they divide cleanly:

- Three on `GO:0015627` (IBA, IDA, InterPro IEA) and two on `GO:0015628` (IBA, InterPro
  IEA): all ACCEPT, reinforcing each other.
- `GO:0009279` cell outer membrane (SubCell IEA): ACCEPT, and unusually well supported for
  an IEA row — the IDA paper demonstrates OM localisation and shows what breaks it.
- `GO:0019867` outer membrane (InterPro IEA): MODIFY to `GO:0009279`, which the gene
  already carries. IPR013356 is GspD-specific and therefore bacterial, so this row's own
  evidence does reach the cell outer membrane.
- `GO:0009306` protein secretion (InterPro IEA from IPR004846): MODIFY to `GO:0015628`.
  See below.
- No molecular function in GOA, so `GO:0008320` is proposed as a NEW IC row, as in the
  merged xcpQ review.

The IBA node PTN000768388 is seeded by XcpQ (P35818), XqhA (Q9I2M7) and HxcQ itself — all
three *P. aeruginosa* secretins. Self-appearance is expected and marks experimental
grounding on the target; not circular.

## The IPR004846 row, and consistency with the other secretins

IPR004846 is "Type II/III secretion system, secretin-like domain" and matches the β-barrel
region. On its own the signature says "secretin of a T2SS **or** a T3SS", so strictly this
row's evidence supports `GO:0009306` plus a disjunction rather than `GO:0015628` outright.
The disjunct is settled by the rest of the evidence on this gene (GspD-specific IPR013356,
the Hxc literature), not by the signature.

The corpus treats this uniformly: every reviewed gene carrying this row MODIFYs it to the
system-specific term — `xcpQ` → `GO:0015628`, `pscC` → `GO:0030254` (T3SS), `IV` →
`GO:0099045`. `xcpQ`'s review states the disjunction in its own reason and MODIFYs anyway,
and its history records run to 2026-11-17, i.e. after the 2026-11-14 ruling that MODIFY
needs the row's own evidence. I follow the convention for consistency across the secretins
and state the reasoning rather than diverge silently; if the ruling should bite here it
should bite on all four together, which is a corpus question and not a judgement about
this gene.

## What is deliberately not annotated

`GO:0044874` **lipoprotein localization to outer membrane** exists, and it is tempting.
It is wrong for HxcQ. That term names what the Lol machinery does; HxcQ is the **cargo**.
The "self-piloting" headline means HxcQ needs no *additional* pilotin, not that HxcQ
performs lipoprotein localisation — the work on the lipid anchor is done by the general
lipoprotein sorting pathway, and supplying a substrate feature is not participation. By
the project's participation test, being the thing a process acts on does not earn the
process term. Raised as a question instead.

Likewise no phosphate-starvation or virulence process term. Hxc is *induced* under
phosphate limitation and an *hxcR* mutant shows reduced pyocyanin and rhamnolipid and
altered biofilm
[PMID:40499597 "The results indicated that the hxcR mutation led
to a decrease in rhamnolipid and pyocyanin production by regulating phosphate
acquisition and the PhoR/PhoB two-component regulatory system."], but HxcQ's work is forming the channel; the exported phosphatase does the
phosphate scavenging and the rest is downstream of losing the system.

Note also `GO:0046658` anchored component of plasma membrane is **obsolete**, so it is not
an option for recording the lipid anchor even if it were apt; and HxcQ is in any case an
integral β-barrel protein, not merely anchored.

## Provider deep research

Not available. `just deep-research PSEAE PA0685` was not attempted separately after
`--provider perplexity` proved unconfigured and `--provider asta` returned HTTP 429 for
PA0681 in the same session. Per project policy these notes stand in place of a provider
file rather than a hand-written file named as one.
