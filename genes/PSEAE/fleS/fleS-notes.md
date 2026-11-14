# fleS / PA1098 (Q9I4N4) review notes

## Summary of the literature

FleS is a 402-residue sensor histidine kinase (UniProt FLES_PSEAE, reviewed). The record
places a PAS_8 domain in the N-terminal half, a histidine-kinase domain at 188-393 and the
autophosphorylated histidine at position 191 (`FT MOD_RES 191 /note="Phosphohistidine; by
autocatalysis"`, PROSITE rule evidence). The gene lies in the *fleSR* operon upstream of *fliE*.

Primary data, Ritchings et al. 1995 [PMID:7591148], **abstract only** — PMC173697 is a scanned
article and the PubMed MCP returns no body text:

- FleS was identified by sequence: [PMID:7591148 "FleS has a predicted molecular mass of 43.87
  kDa and shows strong homology to histidine kinases which in other two-component systems have
  been shown to be sensor proteins"].
- All experiments listed in the abstract are on *fleR*: a gentamicin-cassette insertion
  [PMID:7591148 "A nonpiliated mutant of P. aeruginosa PAK containing a gentamicin cassette in
  fleR is nonmotile and nonadhesive"], its complementation, a flagellin Western blot and EM of
  the *fleR* mutant.
- The system-level conclusion is stated as a belief: [PMID:7591148 "The fleSR system is believed
  to control both flagellar synthesis and adhesion to mucin"].

UniProt cites PubMed:30877999 (not cached) for a *fleS* mutant with a severe swimming defect and
for FleS/FleR control of flagellar synthesis, adhesion, swarming, motility and antibiotic
resistance, and gives the EC 2.7.13.3 catalytic activity by similarity to *E. coli* AtoS
(ECO:0000250|UniProtKB:Q06067) rather than from direct assay. So no direct kinase assay on FleS
is available to me; the MF rests on the domain architecture plus the IBA.

Related cached material: FleQ (PA1097) is reviewed in `genes/PSEAE/fleQ` and is the master
regulator above FleSR; FleN/PMID:11673434 concerns FleQ, not FleS.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN009166588 | GO:0007165 signal transduction | 7 | 268 (41 taxa) | GO:0000160, IDA, PMID:7591148 (PseudoCAP) | INDIRECT-PHENOTYPE (process right, evidence code wrong) | The *claim* is correct — FleS is the kinase of the FleS-FleR pair — but the cited paper, as far as its abstract shows, characterises FleS only by homology and takes all of its data from a *fleR* mutant. An IDA on FleS is not what those experiments give. Confidence PROBABLE: the abstract positively states that FleS was identified by homology and lists only *fleR* genetics, but the full text is unavailable and could contain a phosphorylation assay. | *E. coli* NtrB (P0AFB5, IDA GO:0004673/GO:0006470), *E. coli* ZraS (P14377, IDA GO:0004673 and IDA GO:0007165), *S. pombe* Mak3 (O74539, IGI GO:0000160), *P. aeruginosa* CbrA (Q9HV74), *E. coli* AtoS (Q06067, IDA GO:0007165), *M. tuberculosis* PdtaS (P9WGL5, IDA GO:0000160) — verified by live QuickGO query 2026-11-05 | Yes. AtoS, ZraS, NtrB and PdtaS carry independent experimental signalling/kinase annotations, and signal transduction suits a histidine-kinase clade. **No GO_CENTRAL defect**; the defect is on the PseudoCAP row only (evidence code). |

FleS also receives the GO:0000155 IBA from the same node (it is not a seed of that IBD; its
seeds are PprA, Mak3, AtoS and PdtaS — see `genes/PSEAE/pprA/pprA-notes.md`, where the
node-level assessment for PTN009166588 is recorded once for this batch).

## Annotation decisions

- GO:0000155 (IEA, IBA): ACCEPT. Complete kinase core with His191, cognate sigma-54 activator
  FleR, well-seeded IBA node.
- GO:0000160 (IDA, PMID:7591148): ACCEPT the claim, with a PSEUDOCAP `WRONG_EVIDENCE_CODE`
  defect (PROBABLE) asking for the code to be checked (ISS, or IMP/IGI if a *fleS* mutant is in
  the full text).
- GO:0004673 (ISS, IEA), GO:0016772 (IEA), GO:0007165 (IEA, IBA): TOO_GENERAL — entailed by
  GO:0000155 / GO:0000160, matching the treatment in `genes/PSEAE/parS`, `genes/PSEAE/PA5484`
  and `pprA`.
