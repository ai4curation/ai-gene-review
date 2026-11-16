# cbrA / PA4725 (Q9HV74) review notes

## Summary of the literature

CbrA is a 983-residue hybrid protein: an N-terminal solute:sodium symporter (SSSF/SLC5)
transporter domain of 12-13 predicted transmembrane helices (UniProt lists TRANSMEM features
through residue ~451), then a PAS domain and a C-terminal HisKA/HATPase kinase core of the NtrB
type. The UniProtKB entry is unreviewed, and its FUNCTION-level statements are ARBA-derived
(including, incorrectly for the whole protein, "Belongs to the sodium:solute symporter (SSF)
family"), so I did not use them as evidence.

Primary data:

1. Nishijyo, Haas & Itoh 2001 [PMID:11401699], **abstract only**. Discovery of CbrA-CbrB:
   [PMID:11401699 "cbrA and cbrB mutants of strain PAO were found to be unable to use several
   amino acids (such as arginine, histidine and proline), polyamines and agmatine as sole carbon
   and nitrogen sources"]; architecture [PMID:11401699 "The amino-terminal half (490 residues) of
   CbrA appears to be a sensor membrane domain, as predicted by 12 possible transmembrane
   helices"]; conclusion [PMID:11401699 "the CbrA-CbrB system controls the expression of several
   catabolic pathways"]. The experiments named in the abstract are mutant growth phenotypes,
   *aot-argR* induction, histidase and proline dehydrogenase assays, complementation and primer
   extension — i.e. genetics, not a phosphorylation assay.
2. Yeung, Bains & Hancock 2011 [PMID:21169488], abstract only: [PMID:21169488 "The cbrA deletion
   mutant was completely unable to swarm while exhibiting an increase in biofilm formation"],
   plus cytotoxicity and antibiotic-resistance phenotypes and a swarming microarray. These are
   the two PseudoCAP IMP rows (GO:2000147, GO:1900232).
3. Ortholog biochemistry, **full text cached**: Wirtz et al. 2020 on *P. putida* KT2440
   [PMID:32214184 "we show that CbrA and CbrAΔSLC5 can autophosphorylate at His766 and transfer
   the phosphoryl group to CbrB"] and [PMID:32214184 "It is demonstrated that CbrA can bind and
   transport L-histidine."] / [PMID:32214184 "We demonstrated that the SLC5 domain of CbrA
   transports L-histidine"]. Zhang et al. 2015 on *P. fluorescens* SBW25 reach the same
   conclusion genetically [PMID:26148710 "implicated CbrA in histidine uptake"], and find SSSF
   mutations that separate transport from signalling. Monteagudo-Cascales et al. 2019
   [PMID:31235731] dissect the TM and PAS domains of *P. putida* CbrA in signalling.

So the kinase and transporter functions are established for the orthologs and inferred here;
neither has been assayed on the *P. aeruginosa* protein in anything I could read.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN009166588 | GO:0007165 signal transduction | 7 | 268 (41 taxa) | GO:0000160, IDA, PMID:11401699 (PseudoCAP) | INDIRECT-PHENOTYPE (process right, code queried) | CbrA really is the sensor kinase of the CbrA-CbrB pair, and the *P. putida* ortholog autophosphorylates and phosphorylates CbrB, so the claim is accepted. The cited paper, however, describes only sequence analysis, mutant growth phenotypes, complementation and primer extension in its abstract; IMP or IGI would fit. Confidence **SUSPECTED**: this rests on what the abstract does not say, and a 2001 two-component paper could well contain a phosphorylation gel in the full text. | *E. coli* NtrB (P0AFB5), *E. coli* ZraS (P14377, IDA GO:0007165), *E. coli* AtoS (Q06067, IDA GO:0007165), *S. pombe* Mak3 (O74539), *M. tuberculosis* PdtaS (P9WGL5, IDA GO:0000160), *P. aeruginosa* FleS (Q9I4N4) — verified by live QuickGO query 2026-11-05 | Yes. Four seeds have independent experimental kinase/signalling annotations. **No GO_CENTRAL defect** for this node; see `genes/PSEAE/pprA/pprA-notes.md`, where the node-level assessment for PTN009166588 is recorded once for this batch (pprA, fleS, cbrA all sit under it). |

## Annotation decisions

- GO:0000155 (IEA, IBA): ACCEPT — full kinase core, well-seeded node, ortholog biochemistry.
- GO:0000160 (IDA, PMID:11401699): ACCEPT the claim, with a PSEUDOCAP `WRONG_EVIDENCE_CODE`
  defect at SUSPECTED.
- GO:0022857 / GO:0055085 (InterPro2GO from the SSSF domain): **MODIFY** to
  GO:0005290 L-histidine transmembrane transporter activity and GO:1903810 L-histidine import
  across plasma membrane. The transporter domain is real and its substrate is known in two
  Pseudomonas orthologs; the generic terms are less precise than the evidence allows. Both
  replacements rest on ortholog data, which is stated in the reasons.
- GO:0006355 (InterPro2GO, regulation of DNA-templated transcription):
  MARK_AS_OVER_ANNOTATED. The transcriptional work is done by CbrB and by the CrcZ/CrcY sRNAs;
  the kinase acts upstream. This matches the treatment of the sensor kinases parS and KinB,
  where regulation terms were not transferred to the kinase.
- GO:1900232, GO:2000147 (IMP, PMID:21169488): KEEP_AS_NON_CORE — downstream phenotypes of a
  global metabolic regulator. GO has no "regulation of swarming motility" term (only
  GO:0071978 bacterial-type flagellum-dependent swarming motility), so GO:2000147 is as
  precise as available.
- GO:0005886 (IBA): ACCEPT, 12-13 TM helices. GO:0016020 (IEA): TOO_GENERAL.
- GO:0004673, GO:0016301, GO:0016740, GO:0016772, GO:0007165 (IEA/IBA): TOO_GENERAL, entailed by
  GO:0000155 or GO:0000160, consistent with parS, KinB, pprA and fleS.

## Knowledge gap not filed

Whether *P. aeruginosa* CbrA itself transports histidine is unmeasured, but that is a question
for a wet-lab experiment on a known activity of the orthologs rather than a genuine unknown of
the family, so it is recorded as a suggested experiment, not a `knowledge_gaps` entry.
