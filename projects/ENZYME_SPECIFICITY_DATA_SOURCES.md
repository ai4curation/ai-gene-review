# Experimental data sources for enzyme substrate specificity

Follow-up to [`BOLTZ2_SUBSTRATE_SPECIFICITY.md`](BOLTZ2_SUBSTRATE_SPECIFICITY.md), whose conclusion
was: *don't predict substrate specificity with co-folding/affinity models — query the experimental
and curated caches instead.* This project makes those caches **programmatically usable** for gene
review, with small runnable clients in [`enzyme-specificity-data/`](enzyme-specificity-data/).

Companion to [`ENZYME_SPECIFICITY.md`](ENZYME_SPECIFICITY.md) (the curation cases) and
[`STRUCTURE_FUNCTION.md`](STRUCTURE_FUNCTION.md) (structure-based methods).

## The three sources (all verified reachable & working, 2026-06-14)

### 1. SABIO-RK — reaction kinetics (Km, kcat) — **open**
- REST `kineticlawsExportTsv` endpoint, no authentication.
- Returns per-substrate **Km / kcat** with organism, UniProt, and **PubMed IDs** for provenance.
- This is the most direct quantitative substrate-specificity evidence: it states the measured
  preference between candidate substrates.
- Client: `query_sabiork.py` (`--ec`, `--organism`, `--uniprot`, `--summary`, `--tsv`).
- **Demonstrated:** human hexokinase (EC 2.7.1.1) — D-Glucose Km ≈ 4.6×10⁻⁵ M vs D-Fructose ≈
  1×10⁻² M (~200× preference), plus D-Mannose, 2-deoxy-D-glucose, glucosamine, and ATP/ITP/CTP
  phosphate-donor data — i.e. the full specificity profile, measured.

### 2. M-CSA — catalytic mechanism & active-site residues — **open**
- EBI REST API, no authentication; ~1,000 curated reference enzymes.
- Returns catalytic residues (with mechanistic roles), the curated reaction, EC, UniProt.
- Use to verify the **reaction class / mechanism** before changing a molecular-function term
  (addresses the PHYKPL-style "right fold family, wrong reaction" error that kinetics alone won't
  flag).
- Client: `query_mcsa.py` (`--uniprot`, `--ec`, `--json`).
- **Demonstrated:** glutamate racemase (P56868, EC 5.1.1.3) — 6 catalytic residues with roles
  (twin cysteine proton acceptor/donor pair, etc.).

### 3. BRENDA — broad enzyme function & kinetics — **needs free account**
- Largest enzyme database; SOAP API reachable, but requires registration + the `zeep` client.
- Academic use free (check licence). Password sent only as a SHA-256 hash.
- Client: `query_brenda.py` (`--ec`, `--organism`, `--param km|kcat`), reading
  `BRENDA_EMAIL`/`BRENDA_PASSWORD` from the environment. Real SOAP calls, not scraping.
- **Not run here** (no credentials in this environment); SABIO-RK covers the open kinetic need.

## How this plugs into gene review

For an enzyme whose GO substrate term looks too narrow / too broad / mechanistically wrong:

1. `query_sabiork.py --uniprot <acc> --summary` → does the measured Km/kcat profile match the
   annotated substrate, or reveal broader/narrower specificity?
2. `query_mcsa.py --uniprot <acc>` → confirm the reaction class and catalytic residues.
3. (optional) BRENDA for cross-organism breadth.
4. Record findings with **PubMed provenance** in `GENE-notes.md`; if they justify a change, cite the
   specific records in the annotation `review.reason` and pick the action (MODIFY / KEEP_AS_NON_CORE /
   REMOVE) per the `ENZYME_SPECIFICITY` categories.

**Caveats:** kinetic values depend on assay conditions and constructs; multiple records may disagree.
Read and verify the cited papers — never hardcode a single value or over-claim from one record.

## Other relevant caches (not yet wired up)

- **Rhea / MetaCyc / KEGG** — curated reaction scope (substrate sets per reaction).
- **BindingDB / ChEMBL / PDBbind / BioLiP** — experimental binding + ligand-bound structures.
- **UniProt** (already in the pipeline) — `CATALYTIC ACTIVITY`, cofactor, and active-site features.

## Status

- [x] Verified SABIO-RK, M-CSA, BRENDA API reachability and response formats
- [x] Runnable clients for SABIO-RK (open) and M-CSA (open); smoke-tested live
- [x] BRENDA SOAP client (credentials/zeep required; documented, not run here)
- [ ] Apply to a real `ENZYME_SPECIFICITY` case (e.g. LPL1 phospholipase breadth, yegV sugar kinase)
- [ ] Decide whether to add a `just` recipe wrapping these for routine review

Last updated: 2026-06-14
