# Manual research synthesis: kal-1 (Q7S7W0)

This report was researched manually on 2026-09-09 after provider failure. It is not a Falcon or Perplexity report. Sources inspected include the complete current UniProt sequence/features, the seeded GO annotations, the preserved prediction/donor records where applicable, and the primary publications cited below.

## Biological synthesis

KAL-1 is a homeodomain-containing transcriptional regulator in Neurospora crassa. Its conserved homeodomain supports sequence-specific DNA binding and nuclear transcriptional regulation. Deletion of kal-1 alters colony morphology, connecting its regulatory role to fungal growth and differentiation.

## Direct and comparative evidence

- file:NEUCR/kal-1/kal-1-uniprot.txt: “DR   Pfam; PF00046; Homeodomain; 1.”

## Primary phenotype scope

PMID:16801547 is cached with abstract only; its PubMed figures were separately inspected at https://pubmed.ncbi.nlm.nih.gov/16801547/. Figure 3 includes the exact caption excerpt: “Colony morphology of wild type and Δkal-1:NCU03593.” This confirms the locus-to-symbol mapping and a colony phenotype comparison, not a biochemical DNA-binding assay. Figure 2 identifies NCU03593 as a homeobox gene. DNA-binding function is supported by the diagnostic homeodomain and curated phylogenetic inference; the PANTHER family’s HHEX name does not transfer mammalian tissue biology. The full paper could not be downloaded through the cache/PMC route; no unseen promoter specificity is claimed.

## Annotation implications

- GO:0000977: ACCEPT. The sequence contains a diagnostic homeodomain (Pfam PF00046; PROSITE domain residues 75–135), supporting sequence-specific DNA binding by a transcriptional regulator. The curated phylogenetic inference places its activity in RNA polymerase II regulation; no exact recognition motif or individual target promoter is inferred.
- GO:0000978: ACCEPT. The sequence contains a diagnostic homeodomain (Pfam PF00046; PROSITE domain residues 75–135), supporting sequence-specific DNA binding by a transcriptional regulator. The curated phylogenetic inference places its activity in RNA polymerase II regulation; no exact recognition motif or individual target promoter is inferred.
- GO:0000981: ACCEPT. The sequence contains a diagnostic homeodomain (Pfam PF00046; PROSITE domain residues 75–135), supporting sequence-specific DNA binding by a transcriptional regulator. The curated phylogenetic inference places its activity in RNA polymerase II regulation; no exact recognition motif or individual target promoter is inferred.
- GO:0003677: ACCEPT. The sequence contains a diagnostic homeodomain (Pfam PF00046; PROSITE domain residues 75–135), supporting sequence-specific DNA binding by a transcriptional regulator. The curated phylogenetic inference places its activity in RNA polymerase II regulation; no exact recognition motif or individual target promoter is inferred.
- GO:0006355: ACCEPT. The sequence contains a diagnostic homeodomain (Pfam PF00046; PROSITE domain residues 75–135), supporting sequence-specific DNA binding by a transcriptional regulator. The curated phylogenetic inference places its activity in RNA polymerase II regulation; no exact recognition motif or individual target promoter is inferred.
- GO:0006357: ACCEPT. The sequence contains a diagnostic homeodomain (Pfam PF00046; PROSITE domain residues 75–135), supporting sequence-specific DNA binding by a transcriptional regulator. The curated phylogenetic inference places its activity in RNA polymerase II regulation; no exact recognition motif or individual target promoter is inferred.
- GO:0005634: ACCEPT. The conserved homeodomain and transcriptional regulator placement support nuclear function. This is a family-based inference; a direct KAL-1 imaging experiment was not identified.
- GO:0030154: KEEP_AS_NON_CORE. The curated differentiation inference is consistent with the kal-1 deletion phenotype affecting colony morphology in Figure 3 of the Neurospora transcription-factor knockout study. It describes a developmental output of the transcription factor rather than its DNA-binding mechanism.
