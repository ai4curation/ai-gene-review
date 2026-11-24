# magi3b (LOC564220) notes

Directory name `LOC564220` follows the PANTHER v19 label. Current names: ZFIN `magi3b`
(ZDB-GENE-060503-301, chromosome 6); NCBI Gene 564220 `magi3b`; Ensembl ENSDARG00000025974.
UniProt A0A8M6YYZ5 (TrEMBL, 1406 aa). Paralog: wu:fi36a10 (NCBI/RefSeq `magi3a`, ZFIN still
`wu:fi36a10`). Reviewed as part of DANRE_DUPLICATION batch 3 (random sample).

## Deep research

Deep research was not available for this batch (Edison returned 402 Payment Required, and the
OpenAI key is invalid). I searched the literature myself through Europe PMC for "magi3b",
"magi3a", "magi3 AND zebrafish", "LOC564220" and "wu:fi36a10".

## Literature (zebrafish)

- **America et al. 2022 (PMID:35649360)**, the only paper that studies both copies by name.
  - Y2H screen with the Gpr124 intracellular domain: [PMID:35649360 "Three interactors (Prickle1b, Magi3a, and Dlg4a) could be confirmed in this secondary mapping screen."]
  - Both copies are expressed in sorted endothelial cells: [PMID:35649360 "dlg4b, magi3a, and magi3b transcripts could readily be amplified, while dlg4a transcripts were not (Figure S2B)."]
  - F0 crispants: [PMID:35649360 "Targeting magi3a, magi3b, or dlg4b, but not dlg4a, partially impaired brain vascularization (Figures 4H and 4I), in agreement with the expression data."]
  - Not additive: [PMID:35649360 "This lack of additive effect suggests that Dlg4b, Magi3a, and Magi3b act within the same pathway, in which they are individually required."]
  - The paper's magi3b in situ primers match ZFIN magi3b (LOC564220) with 0 mismatches
    (file:DANRE/wu_fi36a10/wu_fi36a10-bioinformatics/RESULTS.md).
- **Choksi et al. 2014 (PMID:25139857)**: Foxj1-target screen. A "magi3" morphant had shorter kidney
  motile cilia, and ZFIN attached this to magi3b.
  [PMID:25139857 "We found that the loss of six genes – BX470211.1, Dr.81747 (GLB1L2 in human), ect2l, magi3, si:ch211-71m22.1 and si:dkey-26i13.8 (KIF18B in human) – showed a significant (P<5.0×10−7, Student's t-test, two-tailed) reduction in the length of motile cilia in the kidney tubules"]
  The GFP-tagged protein was not ciliary. It was cytoplasmic/nuclear/membrane:
  [PMID:25139857 "whereas the remainder appeared to localize to a combination of the cytoplasm, nucleus and cell membrane"]

## Family background

- MAGI GK domains are degenerate: [PMID:37163606 "Unlike other MAGUK GKs, which are composed of three subdomains including guanosine monophosphate (GMP)–binding, LID, and CORE subdomains, MAGI GKs lack the last two subdomains"]
- The UniProt "ATP-binding" segment (118-125) has no Walker A motif (FQKGSIDH) in either copy
  (RESULTS.md). The kinase, transferase, ATP binding and nucleotide binding IEA rows are therefore removed.
- Human MAGI3 at tight junctions, with PTEN: [PMID:10748157 "localizes to epithelial cell tight junctions"]

## Sequence and expression (my analyses; file:DANRE/wu_fi36a10/wu_fi36a10-bioinformatics/RESULTS.md)

- 58.2% identity to wu:fi36a10 (compare_pair.py). magi3b is the more divergent copy: 55.1% to gar
  magi3 vs 63.5% for wu:fi36a10.
- Both copies keep every domain. The C-terminal disordered tail is poorly conserved everywhere
  (about 20%).
- Bgee RNA-Seq: magi3b has 9 calls (highest in retina); wu:fi36a10 has 22 calls; every magi3b call is shared.

- Synteny (synteny_output.md): wu:fi36a10 sits next to ptpn22 and RSBN1, as gar magi3 does. The magi3b
  region shares no gar-window gene, and there is no double-conserved synteny. Ensembl Compara dates the
  split to Euteleostomi. The TGD origin is PANTHER tree-based only.

## Decisions

- Kinase / transferase / ATP / nucleotide binding (UniRule IEA): REMOVE (pseudo-GK).
- Cilium IMPs: KEEP_AS_NON_CORE (single-morpholino screen).
- Localization IBA/IEA/IDA: ACCEPT. Signal transduction IBA: ACCEPT (general).
- No NEW terms. ZFIN curated only adgra2 from PMID:35649360. The magi3 data are F0 crispants, so I
  did not add a brain angiogenesis term (see "do not add what curators declined").
