# gacA notes

## Identity and sequence context

- The requested `gacA` locus in *Pseudomonas putida* KT2440 maps to UniProt `Q88FJ6`; UniProt records the gene name as `uvrY`, the locus tag as `PP_4099`, and the protein name as "Response regulator GacA (Global activator)." The protein is 212 aa long. [file:PSEPK/gacA/gacA-uniprot.txt "GN   Name=uvrY ... OrderedLocusNames=PP_4099 ... DE   RecName: Full=Response regulator GacA ... AltName: Full=Global activator"]
- Domain architecture is consistent with a classic DNA-binding two-component response regulator: an N-terminal response-regulator receiver domain, a C-terminal LuxR-type helix-turn-helix DNA-binding domain, and a predicted phosphoacceptor Asp54. [file:PSEPK/gacA/gacA-uniprot.txt "FT   DOMAIN          3..119 /note=\"Response regulatory\" ... FT   DOMAIN          141..206 /note=\"HTH luxR-type\" ... FT   MOD_RES         54 /note=\"4-aspartylphosphate\""]

## KT2440-focused functional evidence

- The strongest direct KT2440 evidence places the Gac system upstream of adhesin expression and biofilm development. The lapA/lapF study states that "Both lapA and lapF are under the control of the two-component regulatory system GacS/GacA" and concludes that "The two-component system GacS/GacA appears as a master regulator of the process" of biofilm formation in *P. putida*. [PMID:24488315 "Both lapA and lapF are under the control of the two-component regulatory system GacS/GacA"] [PMID:24488315 "The two-component system GacS/GacA appears as a master regulator of the process"]
- A KT2442 mutant screen recovered a `gacS` insertion as a moderate biofilm-defective mutant, reinforcing that the Gac system contributes to biofilm development in the KT2440/KT2442 lineage. [PMID:27190143 "A mutation in gacS, encoding the sensor element of the GacS/GacA two-component system, also had a moderate effect on biofilm formation"]
- A KT2440 c-di-GMP regulatory-network study identified GacA among the global regulators needed for the high-c-di-GMP crinkly/biofilm phenotype. The discussion also states that in KT2440 the GacS/GacA system is essential for `rpoS` expression, which provides a plausible route by which this regulator affects broad lifestyle programs. [PMID:27489550 "Among the bacterial determinants found in this screen are the global transcriptional regulators GacA, AlgU and FleQ"] [PMID:27489550 "the two component system GacS/GacA is essential for the expression of rpoS in KT2440"]
- A 2023 KT2440 study expanded the phenotype space beyond biofilm control and found that K1 type VI secretion system expression is positively regulated by GacS-GacA and opposed by RetS. [PMID:36748579 "Importantly, expression of the K1-T6SS gene cluster is positively regulated by the GacS-GacA two-component regulatory system (TCS) and repressed by the RetS sensor kinase, which inhibits this TCS"]

## Broader Gac/Rsm interpretation

- Reviews of the Gac/Rsm cascade describe GacA/UvrY-family proteins as phosphorelay-activated transcription regulators that induce small RNAs, antagonize Rsm/Csr proteins, and thereby reprogram social behavior and secondary metabolism. This is useful mechanistic context, but strain-specific outputs should not be transferred uncritically into KT2440 curation. [PMID:18047567 "the conserved GacS/GacA (BarA/UvrY) two-component system positively controls the expression of one to five genes specifying small RNAs"] [PMID:11768529 "GacS senses a still-unknown signal and activates, via a phosphorelay mechanism, the GacA transcription regulator, which in turn triggers the expression of target genes"]
- Other *P. putida* strains show the same regulator controlling diverse downstream programs: quorum-sensing gene expression in WCS358, putisolvin biosynthesis in PCL1445, WLIP biosynthesis in RW10S2, and PHA accumulation in CA-3. These support the view that GacA is a pleiotropic lifestyle regulator, but they are secondary to the KT2440-specific biofilm and T6SS evidence. [PMID:15345437 "GacA positively regulating ppuI expression"] [PMID:16109938 "putisolvin biosynthesis of PCL1445 was found to be dependent on the GacA/GacS two-component signaling system"] [PMID:22544260 "Expression of wlpR is dependent on gacS"] [PMID:23291549 "gene homologues of the GacS/GacA-rsm small RNA (sRNA) regulatory cascade"]

## Curation takeaways

- Current GOA terms for phosphorelay signal transduction and transcription-related DNA binding are directionally correct.
- `GO:0003677 DNA binding` is too broad to be a useful core annotation for this protein; `GO:0000156 phosphorelay response regulator activity` and `GO:0003700 DNA-binding transcription factor activity` are more informative.
- The best supported KT2440-specific process term to add is `GO:1900192 positive regulation of single-species biofilm formation`.
- K1-T6SS regulation is real and experimentally supported in KT2440, but I am treating it as secondary/non-core until direct GacA target promoters are mapped in this strain.
- I did not find direct KT2440 evidence in the examined sources showing purified GacA binding a specific promoter or explicitly identifying the cognate `rsmY`/`rsmZ`-like promoters. Any direct promoter-binding language in the review should therefore stay conservative.

## 2026-11-11 re-review (Gac phosphorelay module completion)

- Earlier supporting_text entries in the review were paraphrases rather than quotations; all were replaced with verbatim quotes from cached publications and the UniProt record.
- Direct transcriptional targets in KT2440: Rsm-titrating sRNAs. Huertas-Rosales et al. 2021 identified KT2440 rsmY and rsmZ and found conserved GacA binding sites upstream of both [PMID:33693029 "conserved GacA binding sites, involved in transcriptional regulation of Rsm-titrating RNAs in other Pseudomonas species (Brencic et al., 2009) could be identified in the regions upstream rsmY and rsmZ"]. This is the best KT2440-level support for GacA as a sequence-specific transcriptional activator. The adhesin and T6SS outputs are downstream and probably indirect (via Rsm proteins, RpoS and FleQ) [PMID:27489550 "the two component system GacS/GacA is essential for the expression of rpoS in KT2440"].
- Cognate-kinase biochemistry comes from the E. coli orthologs [PMID:11022030 "Phosphorylated BarA, in turn, acts as an efficient phosphoryl group donor to UvrY but not to the non-cognate response regulators ArcA, PhoB, or CpxR."].
- Action changes: GO:0003677 DNA binding is TOO_GENERAL (entailed by GO:0000976, accepted). GO:0000976 is ACCEPTED, not non-core: the LuxR-type HTH domain and the conserved upstream GacA boxes support it. GO:0006355 is MODIFIED to GO:0045893 because GacA is an activator.
- Deep research: the codex and falcon files in this folder were used; no new provider run.

## 2026-11-16 — TF batch 2: signaling and target evidence

Re-reviewed all four machine-seeded GO rows and the previous authored proposals. Primary sources replace notes/provider paraphrases as annotation evidence. The receiver and HTH assignments in the preserved UniProt record are computational; predicted Asp54 phosphorylation is not a KT2440 phosphotransfer measurement. Core cis-regulatory binding stays core despite limited direct-target evidence. DNA binding refines to TF activity; response-regulator activity remains a separate IC proposal. The duplicate authored TF proposal and weakly supported cytosol proposal were withdrawn.

[PMID:27489550, Genetic Dissection of the Regulatory Network Associated with High c-di-GMP Levels in Pseudomonas putida KT2440] full text identifies cfcT-5 as PP_4099/gacA. Table 3 reports loss of crinkling, floccules and increased biofilm with multicopy rup4959, and methods describe the KT2440 gacA/pMIR203 complementation construct. The retained positive-biofilm-regulation IMP is conditional on this regulatory assay. GacA does regulatory work; it does not execute adhesion or matrix synthesis.

[PMID:24488315, Roles of cyclic Di-GMP and the Gac system in transcriptional control of the genes coding for the Pseudomonas putida adhesins LapA and LapF] is abstract-only locally. The exact support is “Both lapA and lapF are under the control of the two-component regulatory system GacS/GacA”. The sidecar therefore records system-level control with unknown target-specific signs and unresolved directness.

[PMID:36748579, Transcriptional organization and regulation of the Pseudomonas putida K1 type VI secretion system gene cluster] full text tests a gacS mutant, not gacA. Positive PS/PV regulation is explicitly a Gac-system inference to GacA, with no demonstrated GacA occupancy. Named KT2440 RsmX/Y/Z promoter contacts are not asserted from the conserved Gac/Rsm model.

Provider reports/artifacts, UniProt/GOA and existing publication caches were preserved verbatim. Existing Falcon research was reused, not regenerated. FEBA retrieval failed because no local database or remote source was reachable; no fitness artifact was fabricated. PSEPK has no applicable MOD-description source. Annotation-reviewer consultation was read-only; one writer performed the curation.

## 2026-11-25 — Merge reconciliation

Preserved both preceding review accounts. PMID:33693029 identifies conserved GacA motifs upstream of KT2440 rsmY/rsmZ, but its EMSA measures Rsm–RNA binding, not GacA–DNA binding. Thus the older “direct transcriptional targets” wording describes candidate targets; the batch statement that no named promoter evidence was found is superseded by this motif evidence. Neither establishes physical directness, so no experimentally direct sidecar edge is added.

Retained all incoming references and primary findings. PMID:11022030 directly demonstrates E. coli BarA/UvrY phosphotransfer, supporting ISS for GO:0000156 alongside conserved KT2440 receiver architecture. The source UniProt record assigns Q88FJ6 to PTHR43214:SF3; the family entry table assigns E. coli UvrY P0AED5 to that subfamily. No KT2440 phosphorylation assay is implied.

Retained the batch's GO:0003677 MODIFY to GO:0003700, with GO:0000976 separately covering the DNA-binding branch. The incoming standalone GO:0003700 proposal is consolidated into that replacement, preserving its primary evidence. The incoming cytosol proposal remains withdrawn under the batch's conservative localization policy: soluble architecture and provider prose do not independently establish localization. The conditional biofilm regulation remains in core_functions because GacA performs regulatory work, while the secretion machinery is downstream. Incoming promoter-EMSA and sRNA-reporter experiment details are retained.
