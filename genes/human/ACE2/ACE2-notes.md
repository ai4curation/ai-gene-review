# ACE2 notes

Provider-based deep research was attempted before this review but could not run because the configured Falcon and Perplexity providers were unavailable and Claude Code was not logged in. I therefore used the cached ACE2 GOA seed, cached PubMed/Reactome sidecars, the ACE2 UniProtKB record, the ACE2 PAINT-loss report, and the SARS-CoV-2 entry GO-CAM review as the evidence base for this manual review.

## Core functions

ACE2 was cloned as an ACE homolog and experimentally characterized as a captopril-insensitive, zinc-dependent carboxypeptidase: Tipnis et al. report that soluble ACEH cleaved angiotensin I and II, did not cleave bradykinin or Hip-His-Leu, and "functions exclusively as a carboxypeptidase" [PMID:10924499]. Donoghue et al. independently identified an ACE-related carboxypeptidase that converts angiotensin I to angiotensin 1-9 [PMID:10969042], and Vickers et al. extended the substrate profile to angiotensin II, apelin, kinins, dynorphin and casomorphins [PMID:11815627].

ACE2 also has a noncatalytic intestinal brush-border role with SLC6A19/B0AT1. Kowalczuk et al. showed that coexpressing B0AT1 with ACE2 dramatically increased B0AT1 surface expression in Xenopus oocytes and that peptide substrate addition to ACE2/B0AT1 oocytes caused sodium-leucine cotransport currents, establishing a metabolic complex in which ACE2 acts as the peptidase and B0AT1 as the neutral amino-acid transporter [PMID:18424768]. Camargo et al. then showed that intestinal B0AT1 expression depends on ACE2 in small intestine [PMID:19185582].

The ACE2 ectodomain is a coronavirus receptor. SARS-CoV first established this receptor role [PMID:14647384], SARS-CoV-2 spike binds ACE2 through its RBD [PMID:32132184; PMID:32225176], and the review source for the GO-CAM ACE2 entry activity explicitly says SARS-CoV-2 infection is mediated by the ACE2 entry receptor [PMID:36228039]. This receptor function is not ACE2 peptidase chemistry.

## GO-CAM consistency

GO-CAM `6796b94c00004996` activity `gomodel:6796b94c00004996/6796b94c00005130` currently types ACE2 as `GO:0004175 endopeptidase activity`, puts that activity `part_of` `GO:0098670 entry receptor-mediated virion attachment to host cell`, and connects it to S2 fusogenic activity. ACE2 is a carboxypeptidase in the renin-angiotensin system, but its SARS-CoV-2 attachment function is `GO:0001618 virus receptor activity`; the model already makes viral spike provide ACE2 as input to host-cell-surface receptor binding. A later GO-CAM review PR should mark the ACE2 activity inconsistent with this gene review until the MF is changed from `GO:0004175` to `GO:0001618`.

## Evidence gaps

`PMID:33453855`, the IntAct source on four ACE2 `GO:0005515 protein binding` rows, could not be fetched by the local `fetch-pmid` command on 2026-11-24. Those rows were left `UNDECIDED` rather than accepted or removed.
