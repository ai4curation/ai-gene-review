# chk1 (Schizosaccharomyces pombe) — curation notes

UniProt: P34208 (CHK1_SCHPO); PomBase SPCC1259.13; synonym rad27. 496 aa Ser/Thr kinase, EC 2.7.11.1. CAMK family, NIM1 subfamily. Protein kinase domain 10-272; ATP binding 16-24, 38; active site (proton acceptor) D137.

## Core biology

Chk1 is the effector serine/threonine protein kinase of the DNA-damage checkpoint in fission yeast. Discovered as a kinase linking the rad checkpoint pathway to cdc2 [PMID:8497322 "we have identified a novel fission yeast protein kinase homologue which is involved in cell-cycle arrest when DNA damage has occurred or when unligated DNA is present. We have called the gene encoding this protein chk1 for checkpoint kinase"].

It is activated by the Rad3 (ATR ortholog) kinase via direct phosphorylation of Ser-345 [PMID:11553781 "Rad3 and ATM phosphorylate serine-345 of fission yeast Chk1. Mutation of serine-345 (chk1-S345A) abrogates Rad3-dependent phosphorylation of Chk1 in vivo. The chk1-S345A cells are sensitive to DNA damage and are checkpoint defective"]. Activation requires the mediator Crb2, the 9-1-1 clamp (Rad9-Rad1-Hus1), clamp loader Rad17, and Rad4/Cut5 [PMID:11553781 "Chk1 phosphorylation also requires Rad1, Rad9, Rad17, Rad26, Hus1 (14), Rfc3 ... and Crb2/Rhp9"].

### Effector mechanism (G2/M arrest)
Activated Chk1 phosphorylates Cdc25, inhibiting it and preventing mitotic entry [PMID:9278510 "These findings identify Cdc25, but not Wee1, as a target of the DNA damage checkpoint"; "Cdc25 associated with Chk1 in vivo and was phosphorylated when copurified in Chk1 complexes"]. Chk1 also phosphorylates Wee1, the Cdc2-Y15 kinase [PMID:9034337 "p56chk1 can phosphorylate p107wee1 directly in vitro ... in response to DNA damage p107wee1 is phosphorylated by p56chk1 in vivo, and this results in maintenance of Y15 phosphorylation and hence G2 delay"]. The arrest depends on inhibitory Cdc2-Y15 phosphorylation [PMID:9042863 "the G2 DNA damage checkpoint arrest in S. pombe depends on the inhibitory tyrosine phosphorylation of Cdc2 carried out by the Wee1 and Mik1 kinases"]. Chk1 and Cds1 redundantly phosphorylate Cdc25 (S99, S192, S359) promoting 14-3-3 binding [PMID:9774107 "both kinases phosphorylate Cdc25 on the same sites ... Mutation of these residues reduces binding of 14-3-3 proteins to Cdc25 in vitro and disrupts the replication checkpoint in vivo"].

### Distinguish from Cds1
Cds1 = replication checkpoint effector kinase (requires Mrc1). Chk1 = DNA damage checkpoint effector (requires Crb2). [PMID:24006488 "the effector kinases Cds1 and Chk1 are activated by the DNA replication and the DNA damage checkpoint, respectively. The main aim of these kinases is to block cell cycle progression before cells enter into mitosis by phosphorylating and inhibiting the phosphatase Cdc25"]. Chk1 functions redundantly with Cds1 at the replication checkpoint [PMID:9774107 "Chk1 functions redundantly with the kinase Cds1 at the replication checkpoint"].

### Localization
Nucleus (Swiss-Prot subcellular: Nucleus, by similarity). Global localization study and PomBase IDA place it in nucleus/cytoplasm/cytosol [PMID:16823372 global localization]. Chk1 relocalizes to double-strand breaks: Chk1-GFP forms nuclear foci at IR- and HO-induced DSBs that colocalize with Crb2/Rad22 [PMID:22792081 "IR induced the formation of Chk1-GFP nuclear foci ... these foci significantly overlapped with CFP-Crb2 foci"; "our observations suggest that Chk1 is recruited to DSBs"]. Recruitment depends on Crb2 SQ/TQ phospho-motifs and Rad3 [PMID:22792081 "Crb2 recruits Chk1 to double-strand breaks (DSBs) through a direct physical interaction"].

### Transcriptional role (MBF/Cdc10)
Chk1 phosphorylates the MBF core component Cdc10 to repress MBF-dependent (S-phase gene) transcription after DNA damage [PMID:24006488 "Chk1 is activated and phosphorylates Cdc10 at its carboxy-terminal domain. This modification is responsible for the repression of MBF-dependent transcription through induced release of MBF from chromatin"]. Cdc10 phosphorylation at Ser-720/Ser-732. Chk1 detected on chromatin (IDA).

### Additional checkpoints
- G1/M checkpoint: novel Chk1-dependent arrest in G1 in orp1-4 cells [PMID:12186947 "The arrest depends upon the checkpoint Rad proteins and, surprisingly, the Chk1 protein ... a novel role for Chk1, namely to induce and/or maintain Cdc2 phosphorylation upon checkpoint activation in G1"].
- Meiotic recombination checkpoint: persistent meiotic DSBs activate Rad3/Chk1 to extend the telomere bouquet/prophase [PMID:29123917 "Persistent DNA damages, induced during meiotic recombination, activate the Rad3 and Chk1 DNA damage checkpoint kinases and extend the bouquet stage"].
- Negative regulation of G2/M transition: IGI with wee1 [PMID:25533348].

### Interactions
- Crb2 (mediator): [PMID:14739927], [PMID:22792081], [PMID:9278510-context], two-hybrid screens; functional adapter/scaffold for activation/recruitment.
- Rad3 (ATR): [PMID:14739927 "we show direct interaction between Rad3 and Crb2"; Crb2 interacts with both Rad3 and Chk1].
- Rfp1 (Rnf4 homolog): Rfp1 isolated as Chk1-interacting protein in two-hybrid [PMID:17502373 "Rfp1 was isolated as a Chk1-interacting protein in a two-hybrid screen"]; however rfp1/rfp2 maintain normal checkpoint signaling to Chk1 — role is in DNA repair/SUMO, not core Chk1 function.

### Rad3 dependence / caffeine
Caffeine overrides checkpoints by inhibiting Rad3, blocking Chk1 phosphorylation [PMID:10825192 "Caffeine prevented activation of Cds1 and phosphorylation of Chk1 ... did inhibit Rad3"]. Chk1 IDA kinase activity referenced here.

## Annotation assessment summary
- Core MF: protein serine/threonine kinase activity (GO:0004674) — ACCEPT (IDA-supported, multiple papers).
- Core BP: mitotic G2 DNA damage checkpoint signaling (GO:0007095) — ACCEPT.
- protein binding (GO:0005515) bare term — MARK_AS_OVER_ANNOTATED (uninformative); real partners are Crb2/Rad3/Rfp1.
- NOT DNA repair (GO:0006281, negated) — ACCEPT negation (chk1 is checkpoint signaling, not repair per se).
- Localization nucleus/chromatin/site of DSB — ACCEPT; cytoplasm/cytosol — KEEP_AS_NON_CORE (function is nuclear).
- negative regulation of transcription by RNA Pol II (GO:0000122) — ACCEPT as non-core/secondary (MBF/Cdc10).
- meiotic recombination checkpoint (GO:0051598) — KEEP_AS_NON_CORE.
- G1/M-related mitotic DNA damage checkpoint signaling (GO:0044773) — ACCEPT.
- negative regulation of G2/M transition (GO:0010972) — ACCEPT (consequence of checkpoint).
