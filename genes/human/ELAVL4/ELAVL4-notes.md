# ELAVL4 (HuD) manual curation notes

## Scope and research provenance

- Reviewed the current UniProtKB/Swiss-Prot record P26378, all 30 GOA rows fetched on 2026-07-18, the PANTHER PTHR10352 PAINT record, and the cached primary publications cited by GOA.
- Additional primary literature was cached for the HuD RNA-bound structure, CARM1 regulation, SMN-dependent axonal transport, pancreatic beta-cell translation control, APP/BACE1 regulation, and motor-neuron development.
- The required Falcon command failed with HTTP 402 Payment Required. Its Perplexity-lite fallback failed with HTTP 401 insufficient quota. No provider-named file was authored; the manual synthesis is in ELAVL4-deep-research-manual.md.

## Protein identity, architecture, and isoforms

ELAVL4 encodes HuD, a 385-residue member of the ELAV/Hu RNA-binding family. The reviewed record assigns three RNA recognition motifs (RRM1, residues 51-129; RRM2, 137-217; RRM3, 302-380) separated by a methylation-regulated hinge. The tandem first two RRMs have been crystallized with AU-rich RNA, revealing sequence recognition with a preference for pyrimidine-rich RNA and a central uracil requirement [PMID:11175903, "These structures reveal a consensus RNA recognition sequence that suggests a preference for pyrimidine-rich sequences and a requirement for a central uracil residue"].

UniProt lists six isoforms. All retain the three RRMs, while isoforms 2-5 lack residues 264-277 in the RRM2-RRM3 hinge and several isoforms have alternative extreme N termini. Most functional studies do not resolve endogenous isoforms. This is important because the hinge contains Arg-248, methylated by CARM1, and connects RNA binding to SMN association and neuronal granule recruitment.

## Core AU-rich RNA binding and stabilization

Direct biochemical evidence is unusually strong. HuD binds c-MYC and VEGF 3-prime UTRs in a sequence- and concentration-dependent manner [PMID:10710437, "HuC and HuD bind to the VEGF 3'-UTR regulatory segment (VRS) and to the c- myc 3'-UTR in a specific and concentration-dependent pattern"]. Kinetic analysis showed that stable binding requires an extended AU-rich tract and cooperation among all three RRMs [PMID:10848602, "a single molecule of HuD requires at least three AUUU repeats to bind tightly to the RNA"].

For GAP43, HuD overexpression and recombinant-protein assays establish direct 3-prime-UTR-dependent stabilization, delayed decay, and reduced deadenylation. Long poly(A) tails increase HuD affinity [PMID:12034726, "HuD binds GAP-43 mRNAs with long tails (A150) with 10-fold higher affinity than to those with short tails (A30)"]. AChE and NOVA1 studies independently show target binding and positive effects on transcript abundance, stability, and translation [PMID:12468554, "Immunoprecipitation experiments demonstrated that HuD can bind directly AChE transcripts."; PMID:18218628, "Nova1 mRNA stability and translation are positively and strongly controlled by the nELAV proteins."].

The accepted core molecular-function terms are therefore mRNA 3-prime-UTR AU-rich region binding, mRNA 3-prime-UTR binding, mRNA binding, RNA binding, and poly(A) binding. The generic nucleic acid binding IEA is modified to RNA binding because the RRM architecture and direct biochemistry identify the relevant polymer.

## Nuclear pre-mRNA processing

HuD is not exclusively cytoplasmic. The calcitonin/CGRP study established a nuclear activity for neuronal Hu proteins: binding pyrimidine-rich intronic RNA and opposing TIA1/TIAL1-dependent non-neuronal processing [PMID:17035636, "We show that in neuron-like cells, Hu proteins block the activity of TIA-1/TIAR, two previously identified, ubiquitously expressed proteins that promote the nonneuronal pathway of calcitonin/calcitonin gene-related peptide (CGRP) pre-mRNA processing."]. The broad RNA processing annotation from this paper is modified to regulation of alternative mRNA splicing, via spliceosome (GO:0000381), while the directly assayed pre-mRNA intronic pyrimidine-rich binding annotation is accepted.

The older N-MYC study supports a nuclear pre-mRNA-processing role but is abstract-only and describes the mechanism as putative. Its broad mRNA processing TAS annotation is retained as non-core rather than treated as a defining mechanistic assignment [PMID:10348344, "Thus, we propose that HuD plays a role in the nuclear processing/stability of N-myc pre-mRNA in N-type neuroblastoma cells."].

## Translation is target- and element-dependent

HuD often increases translation together with target stabilization. In human SK-N-F1 cells it enhances APP mRNA stability and polysome loading [PMID:24857657, "In sum, HuD enhanced both the stability and translation of APP mRNA."]. Positive regulation of translation (GO:0045727) is proposed as a new human annotation.

HuD can instead repress translation when it binds a 5-prime UTR. In mouse pancreatic beta cells, HuD binds a conserved 22-nucleotide Ins2 5-prime-UTR element; silencing increases reporter and endogenous insulin translation without increasing RNA abundance, and knockout and transgenic mice show reciprocal insulin phenotypes [PMID:22387028, "HuD overexpression decreased Ins2 mRNA translation and insulin production, and conversely, HuD silencing enhanced Ins2 mRNA translation and insulin production."]. Because the experiments are on mouse Elavl4/Ins2, mRNA 5-prime-UTR binding (GO:0048027) and negative regulation of translation (GO:0017148) are proposed for human ELAVL4 with ISS, not IDA or IMP.

## Neuronal localization and protein-RNA adaptor activity

The cytoplasm, perikaryon, axon, dendrite, and growth-cone locations are consistent across curated orthology transfers, UniProt mappings, and direct neuronal studies. Human HuD also binds SMN through the SMN Tudor domain, and the interaction is needed to recruit HuD and its RNA targets to neuronal granules [PMID:21088113, "the interaction between HuD and SMN is required for proper recruitment of HuD and its mRNA targets in neuronal RNA granules"]. Primary-motor-neuron imaging independently shows SMN-HuD cotransport in axonal granules [PMID:21389246, "time-lapse microscopy revealed SMN cotransport with HuD in live motor neurons"]. These data support the PAINT protein-RNA adaptor activity IBA, although the generic ribonucleoprotein complex term is retained as non-core because it does not identify a specific stable complex.

Animal genetics connects this RNA-regulatory machinery to neuronal differentiation, axon branching, dendrite formation, and motor function. Zebrafish HuD mutants have reduced motor-axon branches and dendrites, while HuD expression rescues SMN-deficient phenotypes [PMID:29061699, "Novel mutants reveal that HuD is also necessary for motor axonal branch and dendrite formation."]. These organismal phenotypes contextualize the core molecular functions but are not promoted to direct human experimental annotations.

## Existing annotation decisions

| GO term | Rows | Decision | Rationale |
|---|---:|---|---|
| GO:0035925 mRNA 3-prime-UTR AU-rich region binding | 4 | ACCEPT | Direct biochemical, reporter, and neuronal target evidence |
| GO:0140517 protein-RNA adaptor activity | 1 | ACCEPT | PAINT plus SMN-dependent RNA-granule recruitment |
| GO:0070935 3-prime-UTR-mediated mRNA stabilization | 2 | ACCEPT | Direct GAP43 decay and deadenylation experiments |
| GO:0003676 nucleic acid binding | 1 | MODIFY to GO:0003723 | True but uninformative relative to direct RNA evidence |
| GO:0003723 RNA binding | 1 | ACCEPT | Defining RRM-mediated activity |
| GO:0003730 mRNA 3-prime-UTR binding | 4 | ACCEPT | All four sources support target 3-prime UTR binding |
| GO:0005737 cytoplasm | 3 | ACCEPT | Direct and orthology-supported localization |
| GO:0030424 axon | 2 | ACCEPT | Orthology and primary motor-neuron imaging |
| GO:0030425 dendrite | 2 | ACCEPT | Orthology and neuronal genetics |
| GO:0030426 growth cone | 1 | ACCEPT | Curated UniProt mapping and primary-neuron evidence |
| GO:0043204 perikaryon | 2 | ACCEPT | Curated orthology and neuronal distribution |
| GO:1990904 ribonucleoprotein complex | 1 | KEEP_AS_NON_CORE | Correct but generic; HuD forms several target-specific mRNPs |
| GO:0003729 mRNA binding | 1 | ACCEPT | Fundamental and independently established |
| GO:0006396 RNA processing | 1 | MODIFY to GO:0000381 | Direct evidence is specifically alternative pre-mRNA processing |
| GO:0008143 poly(A) binding | 1 | ACCEPT | Curated IDA; long poly(A) tails strongly increase HuD affinity |
| GO:0097158 pre-mRNA intronic pyrimidine-rich binding | 1 | ACCEPT | Direct CALCA intronic-element experiments |
| GO:1905870 positive regulation of 3-prime-UTR-mediated mRNA stabilization | 1 | ACCEPT | NOVA1 stability is positively controlled by nELAV/HuD |
| GO:0006397 mRNA processing | 1 | KEEP_AS_NON_CORE | Abstract supports a putative N-MYC nuclear-processing role |

## New-term recommendations

- GO:0005634 nucleus; IDA from direct nuclear Hu-protein localization and alternative-processing experiments (PMID:17035636).
- GO:0045727 positive regulation of translation; IMP from direct ELAVL4 depletion/polysome and reporter experiments in human neuroblastoma cells (PMID:24857657).
- GO:0048027 mRNA 5-prime-UTR binding; ISS from mouse HuD/Ins2 biochemical and cellular experiments (PMID:22387028).
- GO:0017148 negative regulation of translation; ISS from mouse beta-cell knockdown, overexpression, reporter, polysome, and in-vivo experiments (PMID:22387028).

## Open issues

- Resolve which of the six human isoforms are expressed in neuronal subtypes and whether the 264-277 hinge deletion changes CARM1/SMN regulation, granule transport, or target selection.
- Define what determines whether HuD stabilizes and activates a target through its 3-prime UTR or represses translation through a 5-prime-UTR element.
- Separate direct human ELAVL4 functions from conserved developmental phenotypes currently supported mainly by mouse and zebrafish genetics.
