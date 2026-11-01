# comEC (Q9KQW8, VC_1879) notes

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `NZ_CWQE01000001.1_287` (*Vibrio cholerae*, 756 aa, including 9 X residues near the N-terminus). Page: https://gene-annotate-dashboard.kbase.us/review/NZ_CWQE01000001.1_287
- Mapping: N16961 reference-proteome entry Q9KQW8 (VC_1879, 752 aa), 100.0% identical over 747 aligned residues (`final_mapping.tsv`; re-checked in `VC_1879-bioinformatics/results.json`).
- Prior names: UniProt "Rec2-related protein" (TrEMBL), eggNOG "membrane metal-binding protein", InterPro/Pfam "Metallo-beta-lactamase superfamily" (PF00753), KEGG K02238 competence protein ComEC.

## Gene directory name: `VC_1879`

The directory is named by locus tag because UniProt gives no gene symbol, only `OrderedLocusNames=VC_1879` (project rule: use the UniProt gene symbol when there is one, else the locus tag). An earlier draft filed it as `comEC`; it was moved back on 2026-10-30. The published name *comEC* (Seitz & Blokesch 2013, PMID:24127573; Watve et al. 2015, PMID:26401962) is kept as an alias, together with `VC1879` and the dashboard id.

## Dashboard LLM call under review

> ComEC/Rec2 inner membrane DNA uptake channel mediating single-stranded DNA translocation during natural transformation. (Tier A; GO:0015267, GO:0005215, GO:0009290, GO:0009294, GO:0005886)

Verdict: **supported**, with one omission and one term that goes further than the evidence.

- GO:0009290 is COR. Direct V. cholerae mutant data show that comEC mutants are non-transformable but accumulate transforming DNA in the periplasm (PMID:24127573).
- GO:0005215 is COR, at a broad level. The companion review annotates GO:0051035 DNA transmembrane transporter activity by ISS.
- GO:0009294 and GO:0005886 are CNN. GOA already holds plasma membrane (IBA + IEA), and DNA-mediated transformation is implied by GO:0030420.
- **GO:0015267 channel activity is UNC.** The ComEC "channel" is a structural prediction (PMID:40985778) and is called "putative" in V. cholerae (PMID:25139903). No ComEC has a pore or transport measurement. The GO term requires energy-independent facilitated diffusion, and the proposed energetics differ: Stedman et al. propose nuclease-driven entry, and ComFA/ComF may pull the strand. The term was extracted from the word "channel" in the call.
- **Omission: the MBL domain.** The annotator wrote that the metallo-beta-lactamase-like domain "does not establish ... a separate catalytic activity". The C-terminal MBL domain is present (residues 506-689) and keeps the ComEC motif II metal ligands (HLDNDH, 556-561). These align to HADQDH in B. subtilis ComEC and HDDNDH in H. influenzae Rec2. The ComEC CTD is a demonstrated Mn2+-dependent DNA nuclease that transformation requires: M. thermoacetica CTD with B. subtilis in vivo (PMID:33772889), and M. glycerini with L. pneumophila in vivo (PMID:40985778). The companion review adds GO:0004536 DNA nuclease activity by ISS. It has not been tested in Vibrio.
- The annotator's "98.8%-identity V. cholerae homolog" is VC1879 itself, as in other batch genes. Its PaperBLAST paper (PMID:26401962) concerns regulation only. The decisive V. cholerae uptake papers (PMID:24127573, PMID:25139903) and the ComEC nuclease papers were not in its evidence.

## GOA review summary

- GO:0005886 IBA and IEA: ACCEPT. GO:0016020 IEA: ACCEPT.
- GO:0030420 establishment of competence (IEA, InterPro2GO): MODIFY to GO:0009290. ComEC does the uptake; it does not establish competence.
- NEW: GO:0009290 (IMP, PMID:24127573), GO:0051035 (ISS), GO:0004536 (ISS).

## Caveats

- All V. cholerae experiments are in strain A1552 (Blokesch lab) or C6706 (Watve et al.), not N16961. The protein sequences are expected to be essentially identical, but this was not checked.
- Regulation differs between strains. Seitz & Blokesch report QstR-dependent comEC expression in A1552. Watve et al. found comEC "<2-fold induced" in C6706 and outside CytR control. The review does not annotate regulation.
- PMID:16357262 (Meibom et al. 2005) is abstract-only in the cache and does not name comEC, so it is not cited. PMID:24391524 (ComEA) was fetched but is not cited.
- ComEC membrane topology has not been determined for any Gram-negative bacterium. Whether the CTD faces the periplasm in Vibrio is predicted, not measured.

## Tooling notes

- `just fetch-fitness VIBCH VC_1879` failed: there is no local FEBA data, and the bulk download failed with exit 1. No fitness data were used.
- `just fetch-gene-pmids` found no PMIDs (the YAML was seeded with only GO_REFs). `just fetch-pmid` was run for 16357262, 24127573, 24391524, 25139903, 33772889, 27318187, 15661011, 26401962, 23663205 and 40985778. Some calls failed at first and succeeded on retry.
- `just deep-research-claude-code` completed (warning "agentapi not found in PATH"). It found Stedman et al. 2025 (PMID:40985778), which was then fetched and used.
- `just validate-terms` on the predictions sidecar fails with "No such slot locus_tag as an attribute of GeneReview". The recipe validates against the GeneReview schema, not PredictionReview. `just validate-predictions`, which runs `validate-prediction-terms`, passes.
- Bioinformatics: `beril run` `20261030T213831Z-vc1879-comec-motifs` ran `VC_1879-bioinformatics/analyze.py` (Biopython via `uv run --with biopython`).
