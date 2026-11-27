from pathlib import Path
import json,re,hashlib
from Bio.Seq import Seq
p=Path(__file__).parent
x=json.loads((p/'PY79-sequence-proof.json').read_text())
for r in x['records']:
 g={'P54161':'fenA','P94541':'rnhC','O34996':'polA'}[r['accession']]
 s=Path(f'genes/BACSU/{g}/{g}-uniprot.txt').read_text().split('SQ   SEQUENCE',1)[1].split('\n',1)[1].split('//')[0]
 s=''.join(re.findall('[A-Z]+',s))
 assert len(r['exact_PY79_matches'])==1
 m=r['exact_PY79_matches'][0]
 assert str(Seq(m['coding_dna']).translate(table=11,cds=True))==s==m['qualifiers']['translation'][0]
 assert hashlib.sha256(s.encode()).hexdigest()==r['protein_sha256']
 print(g,r['accession'],len(s),'exact PY79 match',m['qualifiers']['protein_id'][0])
