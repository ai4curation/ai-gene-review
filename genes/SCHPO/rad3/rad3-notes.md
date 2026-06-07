# rad3 (S. pombe) review notes

UniProt: Q02099. PomBase SPBC216.05. Protein kinase rad3, EC 2.7.11.1, 2386 aa. Ortholog of human ATR (and budding yeast Mec1/Esr1). PIKK family, ATM/ATR-related subfamily. Partner subunit Rad26 (ATRIP).

## Identity / family
- Rad3 is the homologue of S. cerevisiae ESR1 (MEC1/SAD3) and Drosophila mei-41; required for all DNA structure checkpoints; member of the 'lipid kinase' (PIKK) subclass that includes ATM. Immunoprecipitated overexpressed Rad3 has associated protein kinase activity. [PMID:8978690 "Rad3 is an inessential member of the 'lipid kinase' subclass of kinases which includes the ATM protein defective in ataxia telangiectasia patients. Mutational analysis indicates that the kinase domain is required for Rad3 function, and immunoprecipitation of overexpressed Rad3 demonstrates an associated protein kinase activity."]
- The human gene ATR (ATM and Rad3-related) was identified as closely related and complements esr1-1. [PMID:8978690 "We have identified a novel human gene (ATR) whose product is closely related to Rad3/Esr1p/Mei-41."]
- Despite PIKK/PI3-kinase sequence similarity, Rad3 is a protein Ser/Thr kinase, phosphorylating S/T-Q (SQ/TQ) motifs. [PMID:11553781 "Rad3, a protein kinase related to human ATM and ATR. These kinases phosphorylate serine or threonine followed by glutamine (SQ/TQ)."] UniProt assigns EC 2.7.11.1 (protein serine/threonine kinase).

## Molecular function
- Protein Ser/Thr kinase: phosphorylates Chk1 at Ser-345 (damage checkpoint). [PMID:11553781 "Here we report that Rad3 and ATM phosphorylate serine-345 of fission yeast Chk1. Mutation of serine-345 (chk1-S345A) abrogates Rad3-dependent phosphorylation of Chk1 in vivo."]
- Phosphorylates Cds1 at Thr-11 (replication checkpoint). [PMID:11313465 "Here we show that in vitro, Rad3 and ATM phosphorylate the N-terminal domain of Cds1 at the motif T(11)Q(12)... Rad3-dependent phosphorylation of Cds1 at threonine-11 is required for Cds1 activation and function."]
- Phosphorylates the mediator Mrc1 (with Tel1). [PMID:14585996 "Mrc1 ... is regulated by Rad3 and Tel1 ... Mutation of six S/TQ motifs ... strongly impairs Mrc1 phosphorylation."]
- Phosphorylates Rad9 (T412/S423). [PMID:15155581 "C-terminal T412/S423 phosphorylation of Rad9 by Rad3(ATR) occurs in S phase without replication stress."]
- Phosphorylates Crb2 (Thr-73, Ser-80) to promote Chk1 association; direct Rad3-Crb2 interaction. [PMID:14739927 "we show direct interaction between Rad3 and Crb2, which is inhibitory to Rad3 activity."]
- Histone H2A kinase (gamma-H2A), redundantly with Tel1. [PMID:15226425 "formation of gamma-H2A redundantly requires the ATR/ATM-related kinases Rad3 and Tel1."] -> PomBase EXP GO:0140995 histone H2A kinase activity.
- Phosphorylates telomere protein Ccq1 Thr-93 (with Tel1). [PMID:22302936 "the telomere protein Ccq1 is phosphorylated at Thr 93 ... by Tel1(ATM) and Rad3(ATR) both in vitro and in vivo ... Rad3 plays a relatively major role."]
- Phosphorylates Mek1 (S12/S14/T15) during meiosis. [PMID:21084840 "Mek1 is phosphorylated at serine-12 (S12), S14 and threonine-15 (T15) by Rad3 (ATR) and/or Tel1 (ATM) kinases that are activated by meiotic programmed double-strand breaks (DSBs)."]
- Kinase domain alone is necessary but NOT sufficient; needs N-terminal sequences (leucine zipper etc.). [PMID:10512862 "the isolated kinase domain does not have kinase activity in vitro and cannot complement a rad3 deletion strain."]

## Biological process — checkpoints
- Apical sensor kinase of DNA damage and DNA replication (DNA synthesis) checkpoints. rad3-136 fails G2 arrest after gamma-irradiation and fails to maintain dependence of mitosis on completion of DNA synthesis; also role in DNA repair. [PMID:1594599 "the mutant cells are unable to arrest in the G2 phase of the cell cycle after DNA damage by gamma-irradiation and are also incapable of maintaining the dependence of mitosis upon the completion of DNA synthesis. ... The rad3+ gene is also likely to play a role in DNA repair."]
- Required for all DNA-integrity checkpoint responses; forms stable Rad3-Rad26 complex; Rad26 phosphorylation is the first biochemical marker of Rad3 function (DNA-damage recognition). [PMID:10559981 "Here we report a stable association between Rad3 and Rad26 in soluble protein extracts. Rad26 shows Rad3-dependent phosphorylation after DNA damage ... Rad3-related checkpoint kinases may have a direct role in DNA-damage recognition."]
- Replication checkpoint: Cds1 activation requires Rad3 + Mrc1; two-stage mechanism. [PMID:16618806 "Activation of Cds1 is known to require the upstream kinase Rad3 and the mediator Mrc1."]
- Intra-S checkpoint generated when forks encounter damage; depends on six checkpoint-Rad proteins, Cds1, Rad4/Cut5. [PMID:12032307 "The slowing of S phase depends strongly on the six checkpoint-Rad proteins, on Cds1, and on Rad4/Cut5."]
- Mus81/Rhp51/Rqh1 epistatic pathway downstream of Cds1 for S-phase DNA damage checkpoint slowing. [PMID:19037101] (rad3 IMP for mitotic intra-S DNA damage checkpoint signaling).
- Hsk1/Cdc45 needed for replication-stress checkpoint via Rad3-Mrc1. [PMID:21099360 "replication fork arrest activates the replication checkpoint effector kinase Cds1 ... through the Rad3(ATR/Mec1)-Mrc1(Claspin) pathway."]

## Meiotic checkpoints
- Meiotic DNA replication checkpoint requires the mitotic checkpoint Rad genes and Cds1. [PMID:10521402 "The mitotic checkpoint Rad genes and the Cds1 protein kinase are required for the DNA replication checkpoint during meiosis."]
- Meiotic recombination checkpoint / bouquet stage: persistent meiotic DSBs activate Rad3 and Chk1, extending bouquet stage. [PMID:29123917 "Persistent DNA damages, induced during meiotic recombination, activate the Rad3 and Chk1 DNA damage checkpoint kinases and extend the bouquet stage beyond the chromosome oscillation period."]
- Positive regulation of initiation of premeiotic DNA replication; Rad3/Tel1->Mek1 cascade. [PMID:21084840] (IMP).

## Telomeres
- Rad3 (with Rad26) is one of two pathways (Rad3/Rad26 and Tel1/Rad32) required to maintain telomeres and prevent chromosome circularization; Rad3 associates with telomeres by ChIP. [PMID:12196391 "Rad3/Rad26 and Tel1/Rad32 represent two pathways required to maintain telomeres and prevent chromosome circularization ... Rad3, Rad1, Rad9, Hus1, Rad17, Rad32, and Ku70 associate with telomeres."]
- Telomere maintenance via Ccq1 Thr-93 phosphorylation recruiting telomerase. [PMID:22302936]
- Kinase-INDEPENDENT role: Rad3-Rad26 complex recruits Tel1 to telomeres independent of Rad3 kinase domain. [PMID:20140190 "the Rad3(ATR)-Rad26(ATRIP) complex contributes to the recruitment of Tel1(ATM) independently of Rad3(ATR) kinase activity."] IGI with this (telomere maintenance, with rad26/SPBC6B1.09c? actually WITH PomBase:SPBC6B1.09c).

## Localization
- Nucleus (UniProt subcellular location). ATR-ATRIP (Rad3-Rad26) complex; ComplexPortal CPX-26412. [PMID:10559981]
- Chromatin/nuclear chromosome: Rad3 anchored to chromatin via Cdc18 during stalled replication. [PMID:17531813 "when DNA replication stalls, Cdc18 persists in a chromatin-bound complex including the checkpoint kinases Rad3 and Rad26 ... Cdc18 ... anchors Rad3 to chromatin to ensure long-term checkpoint maintenance."]
- Associates with meiotic chromosomes (asynapsed axes) — based on mammalian Atr ortholog work. [PMID:8843195 "Atr is found at sites along unpaired or asynapsed chromosomal axes."] NOTE: this paper is about mammalian Atr/Atm, not directly S. pombe Rad3; the GO:0000228 nuclear chromosome IDA on PomBase to PMID:8843195 is by analogy and weak for the pombe gene.
- ChIP at telomeres -> chromosome, telomeric repeat region. [PMID:12196391, PMID:20140190]
- nucleolus IDA (PMID:18180284) and cytosol HDA (PMID:16823372) — high-throughput, low-specificity; the MCM paper (18180284) is about MCM-checkpoint interactions, the nucleolus claim is weakly supported; cytosol HDA from ORFeome screen contrasts with the well-established nuclear/chromatin function.

## Action plan summary
- Core MF: protein serine/threonine kinase activity (GO:0004674) — ACCEPT (many IDA/IMP). protein serine kinase (GO:0106310 RHEA) ACCEPT/non-core. histone H2A kinase (GO:0140995) ACCEPT (specific substrate MF). protein kinase activity (GO:0004672) — general, KEEP/ACCEPT as parent but prefer 0004674. kinase activity (GO:0016301), and IEA 0004674 InterPro — general/redundant -> KEEP_AS_NON_CORE or ACCEPT generic; mark less informative ones.
- protein binding (GO:0005515) -> bare protein binding, REMOVE/MARK (uninformative; Crb2 interaction better captured elsewhere).
- Core BP: DNA damage checkpoint signaling (GO:0000077) ACCEPT; mitotic G2 DNA damage checkpoint (GO:0007095) ACCEPT; mitotic intra-S DNA damage checkpoint (GO:0031573) ACCEPT; mitotic DNA replication checkpoint (GO:0033314) ACCEPT; mitotic DNA damage checkpoint (GO:0044773) ACCEPT.
- Meiotic: GO:0033315 meiotic G2/MI DNA replication checkpoint ACCEPT(non-core?); GO:0051598 meiotic recombination checkpoint ACCEPT/non-core; GO:1904514 positive reg premeiotic DNA replication initiation KEEP_AS_NON_CORE.
- Telomere maintenance (GO:0000723) ACCEPT/non-core; chromosome, telomeric repeat region (GO:0140445) ACCEPT.
- DNA repair (GO:0006281) KEEP_AS_NON_CORE (indirect, via checkpoint).
- chromatin remodeling (GO:0006338) IEA from H2A kinase logic -> MARK_AS_OVER_ANNOTATED/REMOVE (Rad3 phosphorylates H2A but is not a chromatin remodeler).
- intracellular signal transduction (GO:0035556) ARBA IEA -> KEEP_AS_NON_CORE (generic parent).
- regulation of double-strand break repair (GO:2000779) NAS ComplexPortal -> KEEP_AS_NON_CORE.
- Localization: nucleus ACCEPT; ATR-ATRIP complex (GO:0070310) ACCEPT (core); chromatin (GO:0000785) ACCEPT; chromosome (GO:0005694) IBA ACCEPT; nuclear chromosome (GO:0000228) — weak (analogy paper) -> KEEP_AS_NON_CORE/UNDECIDED; nucleolus (GO:0005730) MARK_AS_OVER_ANNOTATED; cytosol (GO:0005829) HDA MARK_AS_OVER_ANNOTATED (Rad3 acts in nucleus on chromatin).
