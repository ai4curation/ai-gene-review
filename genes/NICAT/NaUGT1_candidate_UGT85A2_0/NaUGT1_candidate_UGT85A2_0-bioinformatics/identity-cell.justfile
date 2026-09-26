# Execute from this directory; dependencies are pinned in identity-cell.py.
reproduce:
    uv run --script identity-cell.py --supplement identity-cell-inputs/table-s1.xlsx --genomic identity-cell-inputs/scaffold.gb --target identity-cell-inputs/target.gb --uniprot ../NaUGT1_candidate_UGT85A2_0-uniprot.txt --model-protein OIT31852.1 --primer-label NaUGT1 --output identity-cell.json

control:
    uv run --script identity-cell.py --supplement identity-cell-inputs/table-s1.xlsx --genomic identity-cell-inputs/scaffold.gb --target identity-cell-inputs/target.gb --uniprot ../NaUGT1_candidate_UGT85A2_0-uniprot.txt --model-protein OIT31852.1 --primer-label NaA622 --output identity-cell-control.json
