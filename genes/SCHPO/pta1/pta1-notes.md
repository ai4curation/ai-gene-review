# pta1 evidence notes

Pta1 is a conserved noncatalytic component of the nuclear cleavage and polyadenylation factor complex. It supports cotranscriptional mRNA 3′-end formation and the coupling of RNA cleavage and polyadenylation to RNA polymerase II transcription termination. Its role is organization of the processing machinery, whose cleavage endonuclease and poly(A) polymerase are separate subunits.

## Identity and prediction provenance

PomBase primary symbol pta1, locus SPAC1071.01c, current UniProt Q10222. The supplied pre-release post-processed-2026_02_28k.xml is the source of the reviewed claims; its placeholder sequence, taxonomy and dates are not biological metadata. The current UniProt sequence is not established as the model input. Current API availability and published-list inclusion are separate properties; all biological judgments here concern the preserved original claims.

## Primary evidence inspected

- [PMID:33711009 Structure-function analysis of fission yeast cleavage and polyadenylation factor (CPF) subunit Ppn1 and its interactions with Dis2 and Swd22.] "Holo-CPF consists of two component complexes (Fig 1): a 10-subunit CPF core composed of proteins Ysh1 (the cleavage endonuclease), Pla1 (the poly(A) polymerase), Pta1, Yth1 (a zinc finger protein), Pfs2 (a WD repeat protein), Iss1, Cft1 (a WD repeat protein), Cft2 (a metallo-β-lactamase/β-CASP protein), Ctf1, and Ssu72 (a phosphoprotein phosphatase); and a 3-subunit DPS complex comprising Dis2 (a phosphoprotein phosphatase), Ppn1, and Swd22 (a WD repeat protein)."
- [PMID:16823372 ORFeome cloning and global analysis of protein localization in the fission yeast Schizosaccharomyces pombe.] "Next, we determined the localization of 4,431 proteins, corresponding to approximately 90% of the fission yeast proteome, by tagging each ORF with the yellow fluorescent protein."
- [PMID:1508188 PTA1, an essential gene of Saccharomyces cerevisiae affecting pre-tRNA processing.] "PTA1 was initially defined by a UV-induced mutation, pta1-1, that causes the accumulation of all 10 end-trimmed, intron-containing pre-tRNAs and temperature-sensitive but osmotic-remedial growth."
- [PMID:10523662 Pta1, a component of yeast CF II, is required for both cleavage and poly(A) addition of mRNA precursor.] "Extracts prepared from pta1 mutant strains are impaired in the cleavage and the poly(A) addition of both GAL7 and CYC1 substrates and exhibit little processing activity even after prolonged incubation. However, activity is efficiently rescued by the addition of purified CF II to the defective extracts."

## Evidence limits and adjudication

- GO:0008033 (KEEP_AS_NON_CORE): Budding yeast pta1 mutants accumulate intron-containing pre-tRNAs, supporting the curated orthology-based tRNA-processing association. Extracts retain normal tRNA-splicing endonuclease activity, so this phenotype does not establish Pta1 as a tRNA nuclease or make tRNA processing its principal conserved biochemical role.

Primary reports are interpreted at the species, assay and subunit level. Abstract-only experimental annotations are not rejected because a title foregrounds another subunit. PAINT asserts inheritance from a curated ancestral node; donor count and target self-inclusion are not objections. ARBA overlap is recorded only as provenance, never as biological validation. CNN and LSP reflect established biological knowledge, without asserting training-data membership.

## Provider report appraisal

The Falcon report supports a noncatalytic CPF architectural role; the decisive target CPF composition was verified in PMID:33711009 and ortholog extract complementation in PMID:10523662. Generic CPF network extensions in the report were not assigned as Pta1 core functions.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Evidence: UniProt Q10222, cached publications, PANTHER inventory, QuickGO for orthologs.

### Identity
- Q10222 is the reviewed Swiss-Prot canonical product of pta1 (SPAC1071.01c; alt ORF SPAC4H3.15c), 721 aa, sequence version 3 (revised; PMID:26615217 "SEQUENCE REVISION"; A0AAN2H7U2 and Q9UTR2 are secondary accessions). Single chain PRO_0000116838 1..721; contains the Symplekin/Pta1_N (PF11935) region and IPR021850. Not a fragment, isoform or alternative model. Length is in line with S. cerevisiae Pta1 (Q01329, 785 aa); animal symplekins are longer (human Q92797 1274 aa) with extra C-terminal sequence.

### Evolutionary grounding
- PANTHER: Q10222, S. cerevisiae PTA1 Q01329, human SYMPK Q92797 and mouse Sympk Q80X82 are all in PTHR15245:SF20 (SYMPLEKIN) per interpro/panther/PTHR15245/PTHR15245-entries.csv. The family review interpro/panther/PTHR15245/PTHR15245-review.yaml places pta1 in SF20 too: no disagreement.
- IBA (PTN000391745) propagates only CPF complex membership (GO:0005847). SGD's PTA1 terms include tRNA processing (IMP, PMID:1508188) and termination, but PAINT did not propagate tRNA processing; treated as a deliberate omission.
- SGD MF annotations for PTA1 are only GO:0005515 IPI and GO:0003723 contributes_to (IC); no specific MF exists to transfer, so the ND MF stands.

### Key new evidence (budding yeast ortholog, same subfamily)
- [PMID:19188448 "Furthermore, different regions of Pta1 interact with the CPF subunits Ssu72, Pti1, and Ysh1, supporting the idea that Pta1 acts as a scaffold to organize CPF."]
- [PMID:19188448 "The pta1-Delta75 mutant is defective for snoRNA termination, RNA polymerase II C-terminal domain Ser5-P dephosphorylation, and gene looping but is fully functional for mRNA 3'-end processing."]
- [PMID:10523662 "The cause of the tRNA splicing defect in yeast is not known."]
- [PMID:1508188 "Extracts prepared from pta1-1 strains had normal pre-tRNA splicing endonuclease activity."]

### Changes
- GO:0008033 tRNA processing (ISO): KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED. Necessity phenotype of a nonsense allele, mechanism unknown, likely indirect; no participation evidence; not propagated by PAINT; added propagation_review.
- All other rows (ND MF, nucleus x3, CPF complex x3, termination, co-transcriptional 3'-end processing) remain ACCEPT with rewritten, row-specific reasons; IDA PMID:14617822 kept (abstract about Set1, CPF identification in full text per UniProt).
- Added references PMID:12819204 and PMID:19188448 (newly cached) and the UniProt file; added reference_review to each PMID.
- Description and core function rewritten to describe the symplekin/Pta1 scaffold role; added suggested questions (adaptor MF; tRNA phenotype) and an experiment.
- No NEW terms: a scaffold/adaptor MF lacks direct pombe evidence and no ortholog curator has asserted one.

### Relative
- Closest characterised relative by phylogenetic placement (same subfamily SF20, PAINT donor): S. cerevisiae PTA1 (Q01329). No review in repo (genes/yeast/PTA1 absent). Human SYMPK also absent.
- Modules: modules/dmel_cleavage_polyadenylation.yaml and modules/dmel_histone_mrna_3prime_processing.yaml include the fly ortholog Symplekin (Q8MSU4); no pombe CPF module exists.
