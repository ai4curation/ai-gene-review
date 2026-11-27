# elna notes

## 2026-09-27 (claude-opus-5-5, DANRE_DUPLICATION pair review elna/elnb)

- Accession: A0A8N1TQS2 (1164 aa, RefSeq NP_001073532, unreviewed TrEMBL). Sensible: matches
  the 101 kDa / 57-exon Elna of the review [PMID:35216218 "Elna and Elnb are respectively 101 kilodaltons (kDa) with 57 exons and 173kDa with 59 exons"].
  The PANTHER table lists A0A8M6YT25 for elna; a UniProt REST lookup of that accession on 2026-09-27 returned no record.
- GOA: only 2 InterPro2GO IEA (ECM structural constituent; ECM) and 2 root ND rows. No GOA-cited PMIDs.
- TGD origin: [PMID:26783159 "Taken together, these results indicate that genomic locus including eln and limk1 genes was duplicated in the 3R WGD."];
  single eln in all non-teleosts [PMID:41465165 "All non-teleost genomes contain a single eln gene, whereas duplicated elna and elnb genes were found in teleosts"].
- Sequence: closer to human ELN than elnb [PMID:35216218 "Alignments of protein sequences with EMBOSS-Needle (EMBL-EBI) revealed that Elna was closer to human tropoelastin (ELN) than Elnb."]
- Expression broad, like Polypterus eln [PMID:26783159 "As expected, Polypterus had one elastin gene, and its expression was observed in various tissues including OFT, which is similar to that of zebrafish elna"].
- Loss of function: morphant swim bladder defect [PMID:26783159 "elna morphants exhibited a swim bladder defect, where elna expression level is relatively high"];
  germline sa12235 (PTC Tyr88) reduces valve elastin, shortens life [PMID:37408270 "the valves of elnasa12235/+ and elnasa12235/sa12235 mutants were found to have a markedly diminished quantity of elastin"].
  No test of elnb upregulation (transcriptional adaptation).
- Decisions: ND x2 REMOVE; GO:0005201 MODIFY -> GO:0030023; GO:0031012 ACCEPT; NEW GO:0071953 elastic fiber (IDA, PMID:17112714),
  NEW GO:0048251 elastic fiber assembly (IMP, PMID:37408270). Participation: tropoelastin is the structural monomer of the fiber.
  Comparator: mouse Eln has GO:0085029 (IMP); FBN1/FBLN5/EMILIN1/MFAP4 have GO:0048251 (QuickGO, human).
  Not added: bulbus arteriosus development (no elna BA morphology defect), valve/swim bladder process terms (adult degeneration / morphant only).
- Deep research: elna-deep-research-falcon.md present and used as a pointer (its PMIDs-backed claims re-anchored to cached papers).
- Pair page: projects/DANRE_DUPLICATION/pairs/elna_elnb/elna_elnb.md
