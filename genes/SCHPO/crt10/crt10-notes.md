# crt10 notes

Identity: crt10, UniProt O42996; current PomBase systematic identifier is recorded in the benchmark cohort. The UniProt sequence is the reviewed current record, whereas the source XML uses placeholder taxonomy and sequence fields. Those placeholders are not biological evidence.

## ProtNLM source provenance

Source: PRE-RELEASE post-processed-2026_02_28k.xml. The exact entry is in `crt10-protnlm-source.xml`. No entry belongs to the published 26,856-record pilot list. Current API availability does not change the original source version.

The XML evidence keys, model scores, string-match hydration metadata and alignment accessions/scores are retained verbatim in that source file. Assessments use current sequence features and primary sources; annotation overlap and ARBA output do not independently validate a prediction.

## Biological evidence and interpretation

UNC: Crt10 has a diagnostic CRT10 domain and a documented orthologous role in Rtt101-Mms1-dependent nonfunctional rRNA decay. This supports a relationship to cullin-mediated ubiquitination, but does not establish residence in the specific Cul4-RING E3 complex in fission yeast. The XML claim is a low-scoring phmmer transfer from Arabidopsis WDR5B Q9SY00 (model_score 0.11; phmmer_score 66.0); shared WD-repeat architecture does not demonstrate the relevant cullin partner or conserved subfamily function. Direct target-complex evidence or defensible orthology connecting this complex membership is missing. The claim is neither validated nor conclusively refuted.

[PMID:25534857 "We herein demonstrated that another accessory component, Crt10 was required for 25S NRD, but not for DNA repair, suggesting that this accessory component specifies the function of the E3 complex differently."]

[file:SCHPO/crt10/crt10-uniprot.txt "DR   InterPro; IPR014839; Crt10."]

UNC: The exact UV-B response prediction is not supported by the reviewed target annotations. Its source is a TMalign comparison to Arabidopsis DHU1 Q8GYY7 (model_score 0.11; chain-normalized scores 0.56569 and 0.36277), rather than a demonstrated conserved UV-B response mechanism. The experimentally characterized budding-yeast Crt10 directs nonfunctional 25S rRNA decay and is dispensable for the DNA-repair assay examined in that study, which does not exclude every possible UV-B response. Shared WD-repeat structure alone cannot validate this wavelength-specific phenotype in fission yeast. Target UV-B experiments or a conserved mechanistic link are missing, so UNC is appropriate.

[PMID:25534857 "We herein demonstrated that another accessory component, Crt10 was required for 25S NRD, but not for DNA repair, suggesting that this accessory component specifies the function of the E3 complex differently."]

[file:SCHPO/crt10/crt10-uniprot.txt "DR   Pfam; PF08728; CRT10; 1. DR   Pfam; PF00400; WD40; 1."]


## Research-provider audit

The Falcon report was read alongside its cited primary studies and the current sequence/GOA evidence. Its negative literature search is not evidence that a curated target-specific observation does not exist. In particular, the report does not recover the target localization evidence in PMID:16823372; the reviewed UniProt record explicitly cites it. The current PomBase identifier mapping and orthology annotations resolve identity or inherited functions more specifically than the report's ambiguous-symbol caveats. The report's coatomer speculation is not a demonstrated pathway. The CRT10 domain and PomBase nonfunctional-rRNA-decay ISO assertion are weighed against the primary Crt10 study (PMID:25534857).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output and prediction-evidence files were not opened or used for this re-review.

### Identity

- Benchmark accession O42996 is the reviewed, canonical UniProt entry for SPBC27B12.05 (ORF alias pi073), 482 aa. It is not an isoform, fragment or alternative gene model. The UniProt sequence caution concerns an older EMBL CDS (BAA21455.1, "Erroneous gene model prediction"), not the current entry.
- Budding-yeast Crt10 (Q08226, YOL063C, SGD:S000005424) is 957 aa, so the pombe protein is about half its length. Similarity is confined to the Crt10-specific C-terminal region: O42996 342-400 aligns with Q08226 796-851 (file:SCHPO/crt10/crt10-bioinformatics/RESULTS-rereview.md).

### Evolutionary grounding

- PANTHER places O42996 in PTHR19876:SF20 (family COATOMER; subfamily name PRE-MRNA-SPLICING FACTOR PRP46-LIKE). UniProt gives no PANTHER family for budding-yeast Crt10, so there is no shared PANTHER subfamily or PAINT node and no IBA for this gene. The SF20 name describes neither Prp46 splicing nor coatomer function for this protein. I transferred nothing from the family name.
- New reciprocal phmmer analysis (`crt10-bioinformatics/reciprocal_phmmer.sh`, output `reciprocal_phmmer_output.txt`, summary `RESULTS-rereview.md`): each yeast proteome has exactly one PF08728 protein. The O42996 C-terminal region (260-482) has Q08226 as its only S. cerevisiae hit (E=4.6e-4), and Q08226 has O42996 as its only S. pombe hit (E=2.1e-4). For full-length O42996, the generic WD40 hits rank above Crt10 (rank 20/29). The analysis therefore supports the PomBase one-to-one ortholog call, but the similarity is weak.
- PomBase transferred only nonfunctional rRNA decay (ISO). It did not transfer the budding-yeast complex membership (RTT101-MMS1-CRT10 cullin-RING ligase) or the RNR transcription phenotypes. I respect that omission and add no NEW terms.

### Annotation decisions

- GO:0003674 ND: ACCEPT. There is no characterized molecular activity in fission yeast.
- nucleus (HDA, IEA), cytosol (HDA), cytoplasm (IEA): ACCEPT, from the ORFeome localization (PMID:16823372) that UniProt cites as ECO:0000269.
- cytoplasm HDA PMID:22146723: changed from UNDECIDED to ACCEPT. This curator HDA comes from a screen whose abstract reports cytoplasm as the majority class. It agrees with PMID:16823372, and I have no basis to second-guess it.
- nonfunctional rRNA decay ISO: ACCEPT. The basis is now stated explicitly: PomBase orthology plus the reciprocal phmmer result. In budding yeast, Crt10 is the targeting subunit of the ligase that carries out the decay [PMID:25534857 "We herein demonstrated that another accessory component, Crt10 was required for 25S NRD, but not for DNA repair, suggesting that this accessory component specifies the function of the E3 complex differently."].
- I replaced the description and core function text. I also replaced a suggested question that referred to UV-B exposure: that question came from the earlier prediction-driven review and has no basis in the literature for this gene.

### Family and modules

- interpro/panther/PTHR19876/PTHR19876-review.yaml uses O42996 as the SF20 representative. Its SF20 description says the "member inventory contains COPI alpha/beta-prime, LIS1 and Mdv1 proteins", but in the cached entries those proteins are in other subfamilies (for example yeast COPA P53622 is in SF1 and COPB2 P41811 is in SF2), and O42996 is the only reviewed SF20 entry. The family review also does not mention that budding-yeast Crt10 has no PANTHER assignment. I did not edit the family review; these issues are reported to the orchestrator.
- No modules/ file mentions crt10, Crt10/Rtt101 or GO:0070651.

### Next relative

- Budding-yeast CRT10 (Q08226) is the ortholog; the basis is the PomBase curated ortholog plus reciprocal sole matches. It is experimentally characterized (PMID:25534857, PMID:16600900, PMID:18704118 per UniProt), and there is no review for it under genes/yeast/.
