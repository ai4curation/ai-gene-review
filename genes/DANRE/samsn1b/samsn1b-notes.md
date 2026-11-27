# samsn1b notes

## Provenance and setup

- Record: A0A8M2BH30 (TrEMBL, 676 aa, RefSeq XP_005169221.2 isoform X1), ZFIN ZDB-GENE-041010-135
  (synonym zgc:103427), Ensembl ENSDARG00000078647 (chr10).
- Paralog: samsn1a (B3DH22). DANRE_DUPLICATION batch 4 random pair (PANTHER `TGD_tree`; Ensembl
  Compara duplication node Osteoglossocephalai).
- Deep research was not available (Edison 402 Payment Required; OpenAI key invalid). Literature
  searched by hand in Europe PMC; see samsn1a-notes.md for queries. No paper mentions samsn1b in
  its text beyond gene lists; no functional study exists.

## Mammalian SAMSN1

See genes/DANRE/samsn1a/samsn1a-notes.md. Key points with provenance:
- [PMID:15381729 "HACS1 associates with tyrosine-phosphorylated proteins after B cell activation and binds in vitro to the inhibitory molecule paired Ig-like receptor B."]
- [PMID:19923443 "Purified splenic B cells from Hacs1(-/-) mice showed increased cell proliferation on BCR (B-cell receptor) stimulation."]
- [PMID:11536050 "Immunostaining and cellular fractionation studies localized the HACS1 protein predominantly to the cytoplasm."]

## Expression and protein (file:DANRE/samsn1a/samsn1a-bioinformatics/RESULTS.md)

- ZFIN curated in situ (Thisse et al. 2004 direct submission, ZDB-PUB-040907-1): epiphysis (pineal)
  from 14-19 somites to high-pec; retinal photoreceptor layer at day 5. No curated blood or
  macrophage expression (those are samsn1a records).
- E-ERAD-475: small gastrula peak (5 TPM), silent through pharyngula, 10-17 TPM in larvae.
- Bgee RNA-seq: highest in retina (89.3) and granulocyte (88.4); also spleen, head kidney, gill,
  intestine, testis.
- Protein 37.8% identical to samsn1a; SH3 77.4% identical to human SAMSN1; SAM 60%.
- Compara gives samsn1b no medaka orthologue (medaka's single copy is assigned to samsn1a).

## Annotation decisions

- Three root ND rows accepted as accurate placeholders.
- Two IBA process rows accepted, as for samsn1a; bulk RNA-seq keeps samsn1b in hematopoietic
  tissues, so there is no expression argument for loss of the immune role.
