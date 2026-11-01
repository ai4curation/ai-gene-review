"""Recover and verify the published bacterial SepRS/SepCysS identities.

Downloads the normal EuropePMC supplemental archive and extracts the methods.
It does not modify gene raw sources. Archive/UniParc checks are separate.
"""
import hashlib
import io
import json
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

import requests

HERE = Path(__file__).resolve().parent
URL = 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5424206/supplementaryFiles'


def main():
    response = requests.get(URL, timeout=180)
    response.raise_for_status()
    archive = zipfile.ZipFile(io.BytesIO(response.content))
    data = archive.read('mbo002173292s2.docx')
    (HERE / 'published-methods.docx').write_bytes(data)
    document = ET.fromstring(zipfile.ZipFile(io.BytesIO(data)).read('word/document.xml'))
    text = '\n'.join(''.join(p.itertext()) for p in document.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'))
    (HERE / 'published-methods.txt').write_text(text)
    provenance = {'pmid':'28487430','source_url':URL,'archive_sha256':hashlib.sha256(response.content).hexdigest(),'member':'mbo002173292s2.docx','member_sha256':hashlib.sha256(data).hexdigest(),'extraction':'DOCX word/document.xml paragraph text; no editorial rewriting'}
    (HERE / 'supplement-provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')


if __name__ == '__main__':
    main()
