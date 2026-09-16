# Spt16 ProtNLM function-paragraph review

Status: COMPLETE. Overall assessment: supported established FACT biology with an unresolved specific one-dimer-eviction mechanism. Ten atomic claims are CNN; one is UNC.

## Exact external source

PRE-RELEASE `post-processed-2026_02_28k.xml`; UniProt O94267; ProtNLM2; evidence key 2. The accession is absent from the published pilot list but is accessible through the ProtNLM API. The filename identifies the source export; placeholder dates do not establish a prediction timestamp. Exact evidence metadata: `{"model_score": "0.98", "string_match_text": "Component of the FACT complex, a general chromatin factor that acts to reorganize nucleosomes. The FACT complex is involved in multiple processes that require DNA as a template such as mRNA elongation, DNA replication and DNA repair. During transcription elongation the FACT complex acts as a histone chaperone that both destabilizes and restores nucleosomal structure. It facilitates the passage of RNA polymerase II and transcription by promoting the dissociation of one histone H2A-H2B dimer from the nucleosome, then subsequently promotes the reestablishment of the nucleosome following the passage of RNA polymerase II (By similarity).", "string_match_location": "function_comment", "string_match_type": "substring"}`. The adjacent `spt16-protnlm-source.xml` preserves every source word and score.

> Component of the FACT complex, a general chromatin factor that acts to reorganize nucleosomes. The FACT complex is involved in multiple processes that require DNA as a template such as mRNA elongation, DNA replication and DNA repair. During transcription elongation the FACT complex acts as a histone chaperone that both destabilizes and restores nucleosomal structure. It facilitates the passage of RNA polymerase II and transcription by promoting the dissociation of one histone H2A-H2B dimer from the nucleosome, then subsequently promotes the reestablishment of the nucleosome following the passage of RNA polymerase II.

## Atomic claims

| Original claim fragment | Assessment | Evidence and scope |
|---|---|---|
| Component of the FACT complex | CNN | Direct Spt16-Pob3 interaction and co-purification identify target complex membership (PMID:17614284). |
| a general chromatin factor that acts to reorganize nucleosomes | CNN | Target FACT chromatin effects and recombinant nucleosome-chaperoning assays support nucleosome reorganization (PMID:31837996). |
| mRNA elongation | CNN | Spt16/FACT cooperates with Fft3 during RNAPII elongation through transcribed chromatin (PMID:28218250). |
| DNA replication | CNN | FACT controls replication-coupled parental histone transfer in fission yeast; this is a chromatin contribution to replication, not DNA-polymerase catalytic activity (PMID:38479839). |
| DNA repair | CNN | The broad conserved chromatin role is supported by FACT-genome-stability evidence and fission-yeast Pob3 mutant UV/CPT sensitivity. Those are complex-level phenotypes and do not identify a specific Spt16 repair enzyme or repair pathway (PMID:17614284). |
| During transcription elongation the FACT complex acts as a histone chaperone | CNN | The source correctly attributes activity to the complex. Spt16 contributes to the experimentally demonstrated chaperone activity (PMID:31837996), and direct Spt16 H3-H4 binding is separately established (PMID:18579787). |
| destabilizes | CNN | Fission-yeast Spt16/FACT participates in nucleosome disassembly at transcribed regions (PMID:28218250). Destabilization does not specify complete histone eviction. |
| restores nucleosomal structure | CNN | FACT supports maintenance/reassembly of genic chromatin; target mutants disrupt nucleosome occupancy and transcription fidelity (PMID:31837996). |
| It facilitates the passage of RNA polymerase II and transcription | CNN | The target FACT/Fft3 study directly connects nucleosome dynamics with RNAPII elongation (PMID:28218250). |
| by promoting the dissociation of one histone H2A-H2B dimer from the nucleosome | UNC | This is a specific mechanistic model, not entailed by chaperone activity or generic nucleosome disassembly. Primary yeast FACT experiments demonstrate increased accessibility without dimer displacement (PMID:19683499), and the fission-yeast study explicitly discusses this alternative (PMID:28218250). Dimer loss can occur under some conditions, so the claim is not categorically refuted; its assertion as the target mechanism, including exactly one dimer, is unresolved. |
| then subsequently promotes the reestablishment of the nucleosome following the passage of RNA polymerase II | CNN | Restoration after transcription is consistent with target FACT-dependent chromatin maintenance and suppression of cryptic transcription. This is the conserved reassembly role, and does not validate an obligatory preceding one-dimer eviction step (PMID:23028377; PMID:31837996). |

## Primary-source excerpts

[PMID:17614284 The chromatin-remodeling factor FACT contributes to centromeric heterochromatin independently of RNAi. "Thus Pob3 and Spt16 associate in vivo."]

[PMID:28218250 Chromatin remodeller Fun30(Fft3) induces nucleosome disassembly to facilitate RNA polymerase II elongation. "Fun30Fft3 associates with RNAPII and collaborates with the histone chaperone, FACT, which facilitates RNAPII elongation through chromatin, to induce nucleosome disassembly at transcribing regions during RNAPII transcription."]

[PMID:38479839 Coordination of histone chaperones for parental histone segregation and epigenetic inheritance. "the FACT histone chaperone regulates parental histone transfer to both strands and collaborates with Mcm2 and Dpb3/4 to maintain parental histone H3-H4 density and faithful heterochromatin inheritance."]

[PMID:17614284 The chromatin-remodeling factor FACT contributes to centromeric heterochromatin independently of RNAi. "Cells lacking Pob3 are sensitive to HU, CPT, UV and (mildly) to 6-AU, suggesting DNA replication, DNA repair and transcription phenotypes"]

[PMID:31837996 The Chaperone FACT and Histone H2B Ubiquitination Maintain S. pombe Genome Architecture through Genic and Subtelomeric Functions. "we performed nucleosome chaperoning assays with recombinant FACT and recombinant histone octamers"]

[PMID:19683499 yFACT induces global accessibility of nucleosomal DNA without H2A-H2B displacement. "Second, increased nuclease sensitivity can occur without displacement of dimers from the nucleosome."]

The original paragraph is retained verbatim despite the mechanistic uncertainty. Correctness and novelty are separate: the supported claims describe FACT functions established before this pre-release prediction, and are not novel merely because the source expresses them in prose. The reused Falcon report supplies research leads; decisions above are anchored in the inspected primary sources.
