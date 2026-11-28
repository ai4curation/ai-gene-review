# SERPINA6 / corticosteroid-binding globulin bioinformatics

Reproducible placement of reported SERPINA6 (CBG, UniProt P08185) variants on the protein, used by
the gene review (`../SERPINA6-ai-review.yaml`) and by the matching disease curation of
corticosteroid-binding globulin deficiency (MONDO:0012675).

## Run

```bash
uv run 01_fetch_data.py   # downloads inputs into cache/ (network needed); writes cache/MANIFEST.tsv
uv run 02_analyze.py      # offline; writes results.json, tables/*.tsv, RESULTS.md
```

Both scripts carry their dependencies inline (PEP 723), so `uv run` builds the environment.

## Inputs

- `cache/` — UniProt P08185 (JSON, FASTA), EBI Proteins variation, RCSB mmCIF and entry records for the
  human CBG structures 2VDX, 2VDY, 4BB2, 4C41, 4C49 and native rat CBG 2V95, the AlphaFold DB model and
  its AlphaMissense table, gnomAD v4 gene record (GraphQL API), ClinVar esearch/esummary for
  `SERPINA6[gene]`, UniProtKB entries with gene name SERPINA6 (orthologues) and five comparator serpins.
  `cache/MANIFEST.tsv` lists the source URL of every file and the fetch date.
- `variants_literature.yaml` — variants, the reactive-centre-loop register and the elastase cleavage
  site exactly as the cited papers state them. These are inputs transcribed from the literature; the
  script checks each reference residue against the canonical sequence.

## What is computed

1. Numbering: signal peptide length from UniProt, mature = precursor - 22; reference-residue check of
   every literature variant in its stated numbering (and whether the other numbering would also match).
2. Reactive-centre loop register (from the P-sites stated in PMID:19011238), FAMSA alignment to
   alpha-1-antitrypsin, thyroxine-binding globulin, alpha-1-antichymotrypsin and rodent CBG.
3. Steroid-contact residues: heavy atoms within 4.0 A of cortisol or progesterone in 2VDY, 4C49, 4BB2
   (human, cleaved) and 2V95 (rat, native; mapped through the alignment), PDB author numbering mapped
   to UniProt through the mmCIF `_struct_ref_seq` records.
4. Per residue: minimum distance to the steroid, relative accessibility (Shrake-Rupley on the
   AlphaFold model and on cleaved 4C41), AlphaFold pLDDT, identity across one-per-species orthologues,
   mean AlphaMissense score, side-chain neighbours and polar partners, backbone torsions.
5. Population data: gnomAD v4 constraint, predicted loss-of-function alleles, allele frequencies of the
   named variants; ClinVar classifications.

## Limits

- All human crystal structures with a steroid are of reactive-loop-cleaved CBG; the native human state
  is represented only by the AlphaFold model and by rat CBG (2V95). Distances therefore describe the
  site, not the affinity change on cleavage.
- No free-energy or stability calculation is made; the "structural class" column is a rule-based label
  from distance, burial and contacts (thresholds are constants at the top of `02_analyze.py`).
- Glycans are absent from every model, so effects mediated by N-glycans are not captured.
- Orthologue set is whatever UniProtKB names SERPINA6 (reviewed and unreviewed), filtered for >= 90%
  coverage and >= 35% identity to human.
