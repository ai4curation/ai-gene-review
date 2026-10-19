"""Download the external original PDZ supplement and verify its captured identity."""
from pathlib import Path
import argparse,hashlib,json,urllib.request
BASE=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('destination',type=Path);a=ap.parse_args()
    s=json.loads((BASE/'input-manifest.json').read_text())['external_supplement']
    if a.destination.exists():data=a.destination.read_bytes()
    else:
        request=urllib.request.Request(s['url'],headers={'User-Agent':'EGLN1-evidence-replay/1.0'})
        with urllib.request.urlopen(request,timeout=120)as response:data=response.read()
    if len(data)!=s['bytes']or hashlib.sha256(data).hexdigest()!=s['sha256']:raise ValueError('Downloaded/supplied supplement differs from the authenticated snapshot; no output written')
    if not a.destination.exists():
        with a.destination.open('xb')as f:f.write(data)
    print('Verified',a.destination)
if __name__=='__main__':main()
