# PP_2043 (Q88L92) notes

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- **Dashboard protein:** `NZ_PJCG01000017.1_25` (*P. putida*, 440 aa), https://gene-annotate-dashboard.kbase.us/review/NZ_PJCG01000017.1_25. It is tier A, in the Dark-Function stratum.
- **Mapping:** the exact-sequence UniProt entries are deleted. The review is filed on KT2440 Q88L92, which is 98.0% identical over 440 aligned residues (query 1–440 to subject 3–442; the subject has a 2-residue N-terminal extension).
- **Frozen evidence** is in `PP_2043-dashboard-prediction-evidence/`:
  - the page and call from run `20261030T210322Z-dashboard-page-nz-pjcg01000017-1-25`;
  - the full evidence JSON, as `dashboard_evidence.json`.
- **Bioinformatics:** `PP_2043-bioinformatics/` holds a copy of the joint pair analysis. Its scripts are in `../PP_2042/PP_2042-bioinformatics/`.

## Conclusion

PP_2043 is a DUF1329 (LolA-like, COG2834) exported protein of **unknown function**.

- **Location:** it is predicted to be soluble in the periplasm. It has a SignalP signal peptide (1–20), no lipobox and no membrane segment, and DeepTMHMM places it in class SP.
- **Context:** it is co-encoded with the DUF1302 outer-membrane beta-barrel PP_2042, apparently in the PP_2042–PP_2044 operon.
- **Unknown:** its cargo, its partners and the process it serves.

## Dashboard verdict: overreach

The call was "Putative adhesin-associated sorting protein of the DUF1329 family involved in adhesin targeting to the outer membrane."

**Corrected annotation:** "DUF1329 family (LolA-like) periplasmic protein of unknown function, co-encoded with DUF1302 outer membrane protein PP_2042."

**Is "involved in adhesin targeting to the outer membrane" supported? No. It is an untested hypothesis, carried over from the paralog.**

1. **The source is a Fitness Browser curator rationale.** The curators argued that DUF1329 is distantly related to LolB and is cofit with a DUF1302 "adhesin", so it might sort the adhesin to the outer membrane. They wrote this for PP_0766 and for orthologs in *P. stutzeri* and *Kangiella*. There is **no reannotation for PP_2043**.
2. **No experiment in any organism shows that a DUF1329 protein targets a protein to the outer membrane.**
3. **The "adhesin" itself is a name transfer** from PA3923 (see PP_2042 notes).
4. **The fitness evidence the annotator cited comes from PP_0766 and its orthologs.** The KT2440 row at 48.2% identity (Tween 20, −3.65) is PP_0766. PP_2043 has no phenotype in 300 experiments (fitness range −0.31 to +0.30) and is not cofit with PP_2042 (r = 0.098).
5. **There is an alternative model.** In the *Castellaniella* AmeABCD system, the DUF1329 protein AmeB is a periplasmic, LolA-superfamily component of an RND system that handles hydrophobic compounds (PMID:30334144). On that model the cargo is a small molecule or lipid, not a protein.

**GO terms:**
- GO:0089705 protein localization to outer membrane: **UNC**.
- GO:0009279 cell outer membrane: **NPI** (DOMAIN_ARCHITECTURE_MISMATCH).
  - The extractor took the target of the proposed process as the protein's own location.
  - PP_2043 has no lipobox, beta-barrel or TM anchor.
  - The annotator itself called it "a soluble exported protein".

## Orthology

| Comparison | Identity |
|---|---|
| PP_2043 vs PA3922 | 52.9% |
| PP_2043 vs PA3421 | 49.9% |
| PP_2043 vs PP_0766 | 48.9% |
| PP_0766 vs PA3922 | 78.0% (reciprocal best hit) |

PP_2043 is in a separate subfamily from the PA3922/PP_0766 pair.

## Caveats

- No experimental data exist for PP_2043.
- The periplasmic location is a sequence prediction.
- Peripheral association with the outer membrane via PP_2042 cannot be excluded.
- Lack of phenotype may only reflect lack of expression in the conditions tested.

## Tooling notes

Same as PP_2042; see `../PP_2042/PP_2042-notes.md`.
- `fetch-gene` failed at the OLS step, so the stub was hand-written.
- Fitness came from BERDL because the Fitness Browser returned 403.
- The deep-research report claims CDD and Gene3D LolA-like cross-references in UniProt. They are absent from the local UniProt file, so that claim was not used.
