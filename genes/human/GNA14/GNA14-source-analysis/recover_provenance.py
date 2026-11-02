#!/usr/bin/env python3
"""Recover authoritative G14 construct provenance; never substitute for sequence identity."""
from pathlib import Path
import urllib.request,hashlib,json,datetime
base=Path(__file__).resolve().parent
url='https://www.cdna.org/files/catalog.pdf'
data=urllib.request.urlopen(url,timeout=90).read()
assert data.startswith(b'%PDF'), 'Unexpected supplier response'
(base/'Missouri-cDNA-catalog.pdf').write_bytes(data)
(base/'supplier-provenance.json').write_text(json.dumps({'url':url,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)},indent=2)+'\n')
