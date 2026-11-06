from pathlib import Path
from Bio import SeqIO
import json, hashlib
p=Path(__file__).resolve().parent
e=SeqIO.read(p/"AY304485.1.embl", "embl")
f=next(f for f in e.features if f.type=="CDS")
u=SeqIO.read(p.parent/"codA-uniprot.txt", "swiss")
a=f.qualifiers["translation"][0]
assert a==str(u.seq)
print(json.dumps({"deposit":"AY304485.1", "protein":"AAP68832.1", "strain":"ATCC8010", "uniprot":"Q7X2H8", "length":len(a), "exact_match":True, "sequence_sha256":hashlib.sha256(a.encode()).hexdigest()},indent=2))
