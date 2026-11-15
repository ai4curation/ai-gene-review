from pathlib import Path
from Bio import SeqIO
import json
p=Path(__file__).resolve().parent
a=str(SeqIO.read(p/"HMPREF0010_01460.gp", "genbank").seq)
r=json.loads((p/"acinetobacter-betA-strain-query.json").read_text())["results"][0]
b=r["sequence"]["value"]
u=json.loads((p/"UPI0001B8F6A6.json").read_text())
assert a==u["sequence"]["value"]
assert a[19:]==b
assert r["primaryAccession"]=="A0ABX6CCX8"
print(json.dumps({"paper_locus":"HMPREF0010_01460", "paper_era_protein":"EEX04066.1", "paper_era_length":len(a), "current_uniprot":r["primaryAccession"], "current_length":len(b), "current_matches_old_residues":"20-571", "old_extension":a[:19], "exact_571aa_uniprot_crossreferences":[{"accession":x["id"], "active":x["active"]} for x in u["uniParcCrossReferences"] if x["database"].startswith("UniProtKB")], "cloned_start_verified":False},indent=2))
