"""Read PMID21533090 supplied XLS tables. Run: uv run --with xlrd python <this file>."""
from pathlib import Path
import json,hashlib
import xlrd
p=Path(__file__).parent;targets={'PIN1':'at1g73590','ABCB1':'at2g36910','ABCB4':'at2g47000'};found=[]
# s005 contains imported GO annotations, not independent evidence.
for f in sorted(p.glob('*.xls')):
 if f.name.endswith('s005.xls'): continue
 for s in xlrd.open_workbook(f).sheets():
  for i in range(s.nrows):
   row=s.row_values(i)
   for g,t in targets.items():
    if t in str(row).lower():found.append(dict(gene=g,file=f.name,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),sheet=s.name,excel_row=i+1,values=row))
(p/'21533090-target-rows.json').write_text(json.dumps(found,indent=2))
for r in found:print(r)
