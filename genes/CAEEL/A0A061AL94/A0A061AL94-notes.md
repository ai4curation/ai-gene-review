# A0A061AL94 (mcm-4, Y39G10AR.14b) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used.

### Identity: fragment / alternative gene model of mcm-4

- A0A061AL94 (TrEMBL, 74 aa) is the product of WormBase model Y39G10AR.14b. Canonical MCM-4 is
  Q95XQ8 (Swiss-Prot, 823 aa, Y39G10AR.14a). The previous draft wrongly named P34579 as the canonical
  entry; P34579 is UNC-47 (vesicular GABA transporter).
- The fragment is identical to Q95XQ8 residues 750-823 and starts at canonical Met750; Ensembl shows
  Y39G10AR.14b.1 as a single-exon model inside the 3' end of the locus
  [file:CAEEL/A0A061AL94/A0A061AL94-bioinformatics/RESULTS.md "The fragment is an exact substring of the canonical protein: canonical residues 750-823, 100% identity,"].
- Missing: C4 zinc finger (269-294), AAA+ ATPase domain (400-735), Walker A/B, all 8 ATP-binding residues,
  arginine finger 602. Only the C-terminal winged-helix region (PF21128 WHD_MCM4) remains.
- The locus-defining cDNAs all encoded the 823-aa protein and northern blotting saw one transcript
  [PMID:21146520 "northern analysis of wild-type mRNA revealed a single transcript consistent with the size of the cDNA."].
  PeptideAtlas support (PE 1) cannot distinguish the fragment, whose sequence is wholly shared with Q95XQ8.
- No PANTHER assignment on the fragment (too short); canonical Q95XQ8 is PTHR11630:SF66 (MCM4).
  The family review interpro/panther/PTHR11630/PTHR11630-review.yaml places SF66 as the MCM4 subfamily
  (representative NEUCR NCU02539); no disagreement, since the fragment is simply unclassified.

### Annotation decisions

- GOA has no annotations for A0A061AL94. The earlier draft carried five author-proposed rows (labelled
  ISS/GO_REF:0000024) for DNA helicase activity, DNA replication initiation, DNA replication, nucleus and
  MCM complex, all transferred from full-length MCM-4 orthologs. All were dropped: the helicase/ATPase
  function needs the AAA+ domain this product lacks, and complex membership, localization and process
  participation of the isolated WHD fragment are untested. These functions belong on Q95XQ8.
- core_functions now states that no independent function is established; no GO terms asserted.

### Relative to review next

- Same-gene canonical: Q95XQ8 mcm-4 (folder would be genes/CAEEL/mcm-4). No review exists in the repo.
- Module context (for the canonical protein, not the fragment): modules/dmel_replication_origin_licensing_activation.yaml (Drosophila MCM2-7 licensing/activation).
