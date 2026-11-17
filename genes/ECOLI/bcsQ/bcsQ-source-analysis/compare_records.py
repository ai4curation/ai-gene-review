"""Compare the two preserved local BcsQ records; run from repository root."""
from pathlib import Path
import re,json,hashlib
base=Path('genes/ECOLI')
def sequence(g):
 p=base/g/(g+'-uniprot.txt');text=p.read_text()
 return p,''.join(re.findall('[A-Z]+',text.split('SQ   SEQUENCE')[1].split('\n',1)[1].split('//')[0]))
p,a=sequence('bcsQ');q,b=sequence('bcsQ__P37655')
r={'full_accession':'P0DP92','fragment_accession':'P37655','full_length':len(a),'fragment_length':len(b),'full_positions_10_250_equal_fragment_positions_2_242':a[9:]==b[1:],'full_position_9':a[8],'fragment_position_1':b[0],'raw_sha256':{str(x):hashlib.sha256(x.read_bytes()).hexdigest() for x in [p,q]}}
Path('genes/ECOLI/bcsQ/bcsQ-source-analysis/sequence-comparison.json').write_text(json.dumps(r,indent=2)+'\n')
assert r['full_positions_10_250_equal_fragment_positions_2_242'];print(json.dumps(r,indent=2))
