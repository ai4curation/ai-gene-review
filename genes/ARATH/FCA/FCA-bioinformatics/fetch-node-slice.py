"""Reproduce exact PTN subset; does not reconstruct family membership."""
from pathlib import Path
import requests
nodes = {'PTN000609546','PTN002768817','PTN000391532','PTN008729690','PTN000519834','PTN002509179'}
url = 'https://data.pantherdb.org/ftp/downloads/paint/current/IBD.gaf'
r = requests.get(url, stream=True, timeout=120)
r.raise_for_status()
rows = []
for line in r.iter_lines():
    line = line.decode('utf-8')
    fields = line.split('\t')
    if line.startswith('!') or (len(fields)>1 and fields[1] in nodes):
        rows.append(line)
Path(__file__).with_name('IBD-target-nodes.gaf').write_text('\n'.join(rows)+'\n')
