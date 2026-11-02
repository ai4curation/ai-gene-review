# USP36 (human, Q9P275) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: USP36 is reviewed as the experimentally characterized reference relative of
donkey A0A9L0JCH5. No ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon human USP36 --fallback perplexity-lite` failed: Edison API
returned `403 Forbidden` at `/auth/login`, and the perplexity-lite fallback also
failed. No deep-research file exists; the review is built from cached primary
literature (full text for PMID:29274341, PMID:27445338, PMID:36912080, PMID:22902402,
PMID:24912190; abstracts for the rest) and the UniProt record.

### Evolutionary grounding

- PANTHER PTHR24006:SF653 (UBIQUITIN CARBOXYL-TERMINAL HYDROLASE 36) contains human
  Q9P275 and mouse B1AQJ2 (interpro/panther/PTHR24006/PTHR24006-entries.csv), so the
  ISS/Compara rows from mouse Usp36 are within-subfamily transfers.
- Yeast Ubp10 (P53874) and fly scrawny (Q9VRP5) are in a different subfamily,
  PTHR24006:SF758, even though PANTHER names it the same. Human USP36 complements
  ubp10 deletion for RNA Pol I stability and pre-rRNA processing
  [PMID:22902402 "USP36, the human ortholog of Ubp10, complements the ubp10Δ allele for RNAPI stability, pre-rRNA processing, and cell growth in yeast"],
  but I did not transfer anything from Ubp10.
- The IBA rows come from deep nodes: PTN002541993 (the family root) for DUB activity,
  nucleus, cytosol and regulation of protein stability, and PTN002541928 for
  regulation of apoptotic process.

### Experimentally established in human (key points)

- Cysteine-type DUB activity: in vitro H2Bub1 deubiquitination, lost in C131A
  [PMID:29274341 "only wt USP361-800 was capable of deubiquitinating H2Bub1 in vitro"];
  c-Myc deubiquitinated in cells and in vitro [PMID:25775507].
- Nucleolar localization through basic C-terminal stretches [PMID:19208757].
- Substrates stabilized: NPM1, FBL [PMID:19208757]; c-Myc [PMID:25775507]; DHX33
  [PMID:29273634]; SOD2 [PMID:21268071]; CEP63 [PMID:35989368].
- SUMO E3 for EXOSC10 K583 in vitro and in cells
  [PMID:36912080 "USP36 markedly increased EXOSC10 SUMOylation by SUMO1 in vitro, demonstrating that USP36 acts as a SUMO E3 for EXOSC10"].
  Proposed as NEW GO:0061665.
- RNA-IP shows that USP36 binds pre-rRNA [PMID:36912080].
- NEDD4L/TrkA/Kv7.2/3 modulation is largely catalysis-independent (the C131S mutant
  also reduces TrkA ubiquitination) [PMID:27445338]. Kept as non-core.

### Decisions worth flagging

- Rows for regulation of rRNA processing and regulation of protein stability: MODIFY to
  the positive terms (GO:2000234, GO:0050821). All the data show a positive direction.
- Chromatin organization (IMP): MODIFY to chromatin remodeling, following the GO
  convention for histone-modifying activities. GO:0016578 histone deubiquitination is
  obsolete in the local go.db.
- Mitophagy screen rows (PMID:24912190): UNDECIDED. USP36 does not appear in the cached
  main text, and there is no follow-up.
- Regulation of apoptotic process (IBA): MARK_AS_OVER_ANNOTATED. Apoptosis after
  knockdown is downstream of nucleolar stress.
- Protein binding rows: DHX33 rows REMOVE (generic; the substrate relationship is
  captured elsewhere). FBXW7 and NEDD4L rows MODIFY to ubiquitin protein ligase binding.
