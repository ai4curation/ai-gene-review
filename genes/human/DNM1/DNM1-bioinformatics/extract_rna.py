#!/usr/bin/env python3
"""Extract the literal DNM1 measurement row from a pinned, genuine author thesis."""
import argparse, hashlib, json, re, subprocess
from pathlib import Path

SOURCE_URL = 'https://refubium.fu-berlin.de/bitstream/handle/fub188/9034/Dissertation_Baltz.pdf?sequence=1'
SOURCE_SHA256 = '9294306a7120ef640de2e435840f94dd1b98eb7e4056032eafa36aec3cef16e8'

def extract(pdf):
    data = pdf.read_bytes()
    if hashlib.sha256(data).hexdigest() != SOURCE_SHA256:
        raise ValueError('Source PDF hash differs from the reviewed source; reassess before use')
    text = subprocess.check_output(['pdftotext', '-layout', str(pdf), '-'], text=True)
    hits = []
    for page, body in enumerate(text.split('\f'), 1):
        for line in body.splitlines():
            match = re.match(r'^\s*(I{1,3})\s+DNM1\s+(.*)$', line)
            if match:
                fields = match.group(2).split()
                if len(fields) < 8:
                    raise ValueError('Unexpected target-table shape')
                hits.append({'pdf_page_1based': page, 'class': match.group(1), 'gene': 'DNM1',
                             'L1': fields[0], 'H1': fields[1], 'L2': fields[2],
                             'mean': fields[3], 'iBAQ': fields[4],
                             'remaining_fields_literal': fields[5:], 'raw_line': line.strip()})
    if len(hits) != 1:
        raise ValueError(f'Expected one target row, found {len(hits)}')
    return {'source_url': SOURCE_URL, 'source_sha256': SOURCE_SHA256,
            'source_publication': 'PMID:22681889 original-author thesis table',
            'method': 'pdftotext -layout; literal class/gene row; values retained as strings',
            'records': hits}

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--pdf', required=True, type=Path, help='Saved original PDF downloaded from source_url')
    p.add_argument('--output', required=True, type=Path)
    args = p.parse_args()
    result = extract(args.pdf)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
