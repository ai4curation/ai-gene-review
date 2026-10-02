# eef1db notes (Danio rerio, eukaryotic translation elongation factor 1 delta b; UniProt A0A8M2B7W1)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 3, random sample)

**Deep research:** not available for this gene (Edison/Falcon returned 402 Payment Required;
the OpenAI key is invalid). Not attempted, per instructions. No `-deep-research-*.md` file
exists. Literature searched by hand (see `../eef1da/eef1da-notes.md`). **No zebrafish-specific
functional paper exists for either paralog.**

Accession: A0A8M2B7W1 (TrEMBL, 578 aa, RefSeq models XP_005160975.1/XP_017207982.1,
chromosome 20) holds all 6 GOA rows (IEA/IBA only). Other eef1db entries include short
isoforms Q5SPD1 (274 aa) and Q5SPD0 (298 aa). Paralog eef1da. Human ortholog EEF1D (P29692).
Shared sequence and expression analysis: `../eef1da/eef1da-bioinformatics/RESULTS.md`.

### Protein
- GEF region 80.7% identical to human (88/109), 89.0% to eef1da; leucine zipper 52.8% to human.
- Long model carries a 281-aa N-terminal segment before the core; 259 positions align to the
  human eEF1BdeltaL extension at 34.7% identity, modestly above a shuffle control (max 31.8%).
  Weak evidence of homology; the model is computational.
- Human background: [PMID:36576126 "The gene EEF1D encodes the eEF1Bδ subunit of the eEF1B complex."]
  [PMID:8334168 "The human EF-1 delta sequence shows a strong conservation in its C-terminal domain."]
  [PMID:42230146 "Although EEF1D and EEF1B2 share a conserved C-terminal GEF domain, these two GEF proteins are not redundant."]

### Expression
- Bgee: same 29 entities as eef1da, high scores throughout; slightly higher than eef1da in
  retina, brain, eye, somite and presomitic mesoderm; lower in maternal/early stages.
- ZFIN: whole-organism in situ, Thisse high-throughput (ZDB-PUB-040907-1).

### Annotation decisions
- All 6 rows ACCEPT, identical to eef1da (same PAINT node PTN000174394, same InterPro mappings,
  conserved catalytic region).
