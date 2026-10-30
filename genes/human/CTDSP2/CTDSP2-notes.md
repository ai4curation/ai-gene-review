# CTDSP2: exact-sequence caution

The selected horse F7A4N8 is 174 aa and maps to VGNC:16932 / ENSECAG00000018788. Human CTDSP2 O14595 is 271 aa with an FCP1-homology domain and catalytic Asp107/Asp109. The alignment matches the horse N-terminus through about residue 84; the remainder diverges and does not retain the human catalytic domain. No InterPro phosphatase or kinase domain is listed in the selected horse record. Absence of an annotation alone is not proof of absent function, but the actual sequence discontinuity makes ordinary whole-protein functional transfer unsafe.

[PMID:12721286](https://pubmed.ncbi.nlm.nih.gov/12721286/), DOI [10.1074/jbc.M301791200](https://doi.org/10.1074/jbc.M301791200), describes the small CTD phosphatase family: “preferentially catalyze the dephosphorylation of Ser5 within the consensus repeat.” The abstract foregrounds SCP1; it cannot alone establish which CTDSP2 assays were performed. The existing human CTDSP2 experimental annotation is retained with this access limitation rather than rejected for paralog misattribution. [PMID:15681389](https://pubmed.ncbi.nlm.nih.gov/15681389/) is the REST/neuronal silencing source in the curated record.

The abnormal horse model does not establish evolutionary loss or a pseudoenzyme: transcript/exon validation and an alternative full-length horse product are needed before distinguishing a genuine isoform from a gene-model problem. The input used at prediction time is not separately recovered. Do not label this WRONG_INPUT_SEQUENCE without such evidence. A completed human Falcon report has been inspected; horse-specific Edison is not indicated by the genome-only identification sources.

## Research synthesis

The human Falcon report identifies CTDSP2-specific Smad1 C-terminal dephosphorylation and nuclear localization in PMID:16882717, distinguishing these observations from CTDSP1 membrane palmitoylation and from the different CTDSPL2 paralog. Some SCP1/SCP2 depletion experiments are combined, so they support participation without proving uniqueness. This reinforces the phosphatase identity of human CTDSP2 but cannot restore the absent catalytic region in the selected horse model.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Identity: benchmark accession O14595 is the reviewed, canonical human CTDSP2 product (271 aa, FCP1-homology domain 97-255, DXDX(T/V) nucleophile Asp107 and proton donor Asp109, Mg2+ ligands 107/109/218). Not an isoform, fragment or alternative gene model. (The section above concerns the paired horse F7A4N8 model, not this accession.)

Evolutionary placement: PANTHER PTHR12210 (Dullard protein phosphatase), subfamily SF187 (human CTDSP2, mouse Ctdsp2 Q8BX07, rat Ctdsp2 M0R5X1). Paralogs: CTDSP1 SF139, CTDSPL SF43, CTDSPL2 SF173 (PANTHER 19.0 classification files). PAINT IBD for GO:0008420 at PTN000954535 seeded by O14595 and Q9GZU7 (CTDSP1); only the MF was propagated from this node (no BP/CC), and the broader GO:0004721 IBD sits at PTN000258719 with an IRD NOT over the Tim50 clade (family review). No disagreement with the PTHR12210 family review, which names CTDSP2 as reference protein and asserts no subfamily for it.

Evidence used:
- PMID:12721286 (abstract-only): SCP family Ser5 CTD phosphatases; curator IDA for CTDSP2 retained.
- PMID:16724108: "Small carboxyl-terminal domain (CTD) phosphatase 2 (SCP2) was identified and verified as a protein that interacts with the androgen receptor (AR)." SCP2 silencing increased PSA transcription and gave earlier Ser5 CTD phosphorylation.
- PMID:16882717: "In Xenopus embryos, SCP2/Os4 and human SCP1, 2, and 3 cause selective dephosphorylation of Smad1 compared with Smad2, inhibiting BMP- and Smad1-dependent transcription". Only an IntAct IPI is in GOA from this paper.
- PMID:15681389: "REST/NRSF recruits SCPs to neuronal genes that contain RE-1 elements".
- PMID:25990325 (Kloet 2015, newly cached, full text): CTDSP2 is a FOXO target; overexpression arrests the cell cycle via Ras/p21 dependent on phosphatase activity. Overexpression phenotype only; no process annotation added.
- PMID:22210897 (miR-26 host genes; mouse Ctdsp2 IDA in MGI for G1/S): combined miRNA/host-gene effects; not transferred.

Decisions (changed from previous version):
- GO:0004722 IEA: MODIFY -> ACCEPT (covers Smad1 C-terminal dephosphorylation, which has no more specific term; GO:0008420 is_a GO:0004722).
- GO:0016791 IEA: MODIFY to GO:0008420 + GO:0004722.
- GO:0005515 rows: KEEP_AS_NON_CORE was non-compliant with the protein-binding policy. AR (PMID:16724108) -> MODIFY to GO:0050681 nuclear androgen receptor binding; Smad1 (PMID:16882717) -> MODIFY to GO:0004722; Tax, CDCA3, N4BP3, LCN2 high-throughput rows -> REMOVE.
- GO:0006357 IEA: ACCEPT -> MODIFY to GO:0000122 negative regulation of transcription by RNA polymerase II.
- NEW GO:0030514 negative regulation of BMP signaling pathway (PMID:16882717): CTDSP2 performs the inactivating dephosphorylation itself. Comparator: PPM1A has GO:0030512 IDA (PMID:16751101); no SCP paralog has the BMP term, which reflects no GO curation of this paper (IntAct IPI only).
- Nucleus, nucleoplasm, protein dephosphorylation, and the three GO:0008420 rows: ACCEPT.

Relative for next review: human CTDSP1 (Q9GZU7), the paralog co-seeding PTN000954535 and the best-characterised SCP; no review in repo. Mouse Ctdsp2 (same SF187) has only one IDA paper (PMID:22210897).
