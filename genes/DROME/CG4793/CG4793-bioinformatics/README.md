# CG4793 catalytic-site analysis

Run `just analyze` here. Python dependencies are pinned in `pyproject.toml`.
`align.py` accepts arbitrary UniProt JSON records, domain coordinates, controls,
and an optional RefSeq FASTA. It reads active sites and mature chains from the
control annotations; no target residues or conclusions are encoded in the script.

Frozen Q8IP30 JSON records were extracted without modification from the project
`fly-benchmark/uniprot.jsonl.gz` and `predictions.jsonl.gz` snapshot (2026-09-08).
The target domain boundaries (98–340) are the PROSITE observation in that record.
Controls were downloaded 2026-09-08 from
https://rest.uniprot.org/uniprotkb/P00760.json and
https://rest.uniprot.org/uniprotkb/P00761.json.
RefSeq was fetched from
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=NP_723941.2&rettype=fasta&retmode=text .
QuickGO definition snapshots use
https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140540 (and the other
GO IDs in the filenames). These are ontology definitions, not biological evidence.

Method: Biopython 1.85 PairwiseAligner global alignment, BLOSUM62, gap open −10,
extension −0.5, target domain vs control's first annotated mature chain. Map the
control's annotated catalytic positions through residue-to-residue columns;
report gaps explicitly. Independent positive-control run uses P00761 as target.
Raw alignments, coverage, identity, and residue maps are in JSON outputs.
This tests catalytic sequence conservation, not three-dimensional folding or
biochemical activity, and does not reconstruct ProtNLM's input sequence.
