# LINC01587 notes

## 2026-10-08 Tier 4 microprotein review

### Locus and existence
- UniProt Q99440 (CD006_HUMAN), "Uncharacterized protein encoded by LINC01587", AltName
  Protein AC1, synonyms AC1, C4orf6. 93 aa, PE1, but the entry's references are all
  nucleotide-sequence sources (PMID:9016955 mRNA; chr2/4 genomic; MGC cDNA) and the entry
  cites no protein-level study, so the basis for PE1 is not visible in the record. No
  domain, family or transmembrane annotation. Only comment: "Expressed in neuroblastoma".
- HGNC (REST, 2026-10-08): locus_type **RNA, long non-coding**, "long intergenic non-protein
  coding RNA 1587", previous symbol C4orf6. Ensembl ENSG00000082929 biotype **lncRNA**.

### Evidence behind the GOA row
- GO:0007399 nervous system development, TAS (ProtInc), PMID:9016955. The paper is a
  fluorescent differential-display method paper: clones differentially expressed during
  retinoic-acid differentiation of SH-SY5Y neuroblastoma cells [PMID:9016955 "we analyzed
  the gene expression profile in the retinoic acid-induced differentiation of a human
  neuroblastoma cell line SH-SY5Y"]. Abstract-only in cache. An expression change during
  differentiation is not participation in nervous system development, and the paper did not
  study the protein.
- PubMed "LINC01587 OR C4orf6" gave nothing functional (checked 2026-10-08).

### Decision
- REMOVE (Tier 3/4 rule: lncRNA locus, process row with nothing locus-specific; and TAS from
  expression change alone).

### Further PubMed hits (2026-10-08)
- PMID:18454448: a 520-kb homozygous deletion of EVC, EVC2, C4orf6 and STK32B in Ellis-van
  Creveld syndrome patients with borderline intelligence; "loss of the novel genes C4orf6 and
  STK32B causes at most mild mental deficit". Human homozygous loss of the whole locus is
  compatible with at most a mild neurological phenotype, attributable to any of the deleted
  genes.
- PMID:31391130 (C4orf6 p.M1V variant in a familial study) and PMID:36242722 (a circRNA
  named after C4orf6) do not address a protein function.
