# fasn-1 review notes

## 2026-10-28 initial review

- `just fetch-gene worm fasn-1` resolved P91871 (TrEMBL, unreviewed; PE 1). 15 GOA rows,
  all IBA/IEA; no experimental GO rows on P91871 in GOA.
- `just fetch-gene-pmids` found no PMIDs (none in GOA). Cached manually: 15340492,
  21178429, 21524356, 32550489, 39007804, 16582625, 29567958, 25497095, 41394642,
  41648212 (preprint of 42400361), 42400361.
- No deep-research API; literature synthesis in `fasn-1-deep-research-manual.md`.
- Bioinformatics: `fasn-1-bioinformatics/` -- all human FASN catalytic residues
  conserved in FASN-1 (KS C197/H329/H367, MAT S621, DH H926/D1078, ACP S2248,
  TE S2415/H2591).

### Decisions

- Specific partial-activity MF terms (EC-mapped IEA): ACCEPT. Domain + catalytic
  residue conservation + in vivo C16:0 output [PMID:21178429].
- Broad MF IEA terms (oxidoreductase, transferase, acyltransferase): TOO_GENERAL,
  entailed by the accepted ER/KR, MAT and KS terms.
- monocarboxylic acid metabolic process (ARBA): TOO_GENERAL (fatty acid biosynthetic
  process accepted).
- phosphopantetheine binding: KEEP_AS_NON_CORE (the ACP domain carries the prosthetic
  group; true but an auxiliary/cofactor feature).
- NEW: [ACP] S-malonyltransferase activity (MAT Ser621 conserved; animal MAT is bispecific)
  and cytoplasm (FASN-1::mNG in AC cytoplasm, PMID:39007804).
- Not proposed (NEW-term bar): molting, cuticle development, embryo development,
  eggshell formation, innate immune response, anchor cell invasion. All rest on
  loss-of-function phenotypes downstream of fatty-acid supply; FASN-1 does not perform
  a step of those processes.
- Not proposed: fatty acid synthase complex (homodimer not shown for worm FASN-1).
