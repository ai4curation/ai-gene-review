from pathlib import Path
from Bio.Seq import Seq
from Bio import SeqIO
import json
p=Path(__file__).resolve().parent
r=json.loads((p/"selected-loci.json").read_text())["regions"]
psi=str(Seq(r[0]["sequence"]).translate())[:-1]
psi="M"+psi[1:]
chi=str(Seq(r[1]["sequence"]).reverse_complement().translate())[:-1]
assert chi==str(SeqIO.read(p.parent/"holC-uniprot.txt", "swiss").seq)
u=SeqIO.read(p.parent.parent/"holD/holD-uniprot.txt", "swiss")
assert psi==str(u.seq)
corrected="M"+psi[31:]
assert len(corrected)==261
assert len(psi[31:])==260
print("HolC exact142aa; HolD old291aa sequence verified; corrected261aa native start and260aa fusion insert mapped.")
