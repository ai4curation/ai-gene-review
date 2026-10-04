# ARMCX1 (ALEX1) review notes

## Sources
- Affinage: trust gates clear. Checked against:
  - PMID:28009275 (mouse Armcx1, full text): mitochondrial; enhances RGC mitochondrial transport.
  - PMID:22569362 (abstract): Armcx family is mitochondrial and derived from Armc10; Armcx3 binds Kinesin/Miro/Trak2.
- Mouse Armcx1 (Q9CX83, MGI:1925498) donor rows (QuickGO): EXP mitochondrion (PMID:28009275, PMID:22569362).
- The IBA rows use node PTN001038987, the PANTHER ARMC10/ARMCX node; the axonal-transport IBA is seeded only by mouse Armcx3.

## Decisions
- ACCEPT:
  - Mitochondrion (IBA, IEA, IDA, ISS) and mitochondrial outer membrane (IEA, ISS).
  - Axonal transport of mitochondrion (IBA).
- KEEP_AS_NON_CORE: axon cytoplasm (IEA derived from the process).
- REMOVE: 8 generic protein-binding rows (policy).
- No NEW. The FBXW7/TRIM21 substrate-recruitment claims come from single cancer cell-line studies (PMID:39285446, FBXW7/c-Myc; PMID:41533266, TRIM21/beta-catenin), so they are raised as a question.

## Review round 1 (PR #4193)
- The Miro1 co-IP (PMID:28009275, Fig. 1H) now supports the axonal-transport ACCEPT, the outer-membrane rows and the core function. No new MF was minted from it.
- The suggested question is narrowed to what remains open: direct binding of human ARMCX1 to MIRO1 and TRAK/kinesin.
- The TBI papers PMID:37454781 and PMID:38492796 (abstracts) are cited. PMID:38492796 supports GO:0019896 (knockdown impairs transport and lowers Miro1).
- The mitochondrion rows now have per-evidence summaries; the HPA IDA row is described as the human evidence.
- Other fixes:
  - Trimmed the citation-fragment quote.
  - Noted the PMID:28009275 erratum.
  - PMID:39285446 relevance raised to MEDIUM.
  - PMID:11162520 now has a quoted carcinoma finding and full_text_unavailable.
  - The axon cytoplasm reason now explains why it is kept.
  - Added a participation-versus-regulation sentence.
