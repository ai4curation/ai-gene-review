"""Reproduce RCSB construct-species checks for PMID:31073061.

Run with Python 3. Fetching is explicit; validation never silently refreshes data.
"""
import json
from pathlib import Path
from urllib.request import urlopen

DEST = Path(__file__).resolve().parent / 'structure-provenance'

def main():
    DEST.mkdir(exist_ok=True)
    for entry in ('6OIJ', '6OIK'):
        for entity in ('entry', '1', '2', '3', '4', '5'):
            endpoint = f'entry/{entry}' if entity == 'entry' else f'polymer_entity/{entry}/{entity}'
            with urlopen(f'https://data.rcsb.org/rest/v1/core/{endpoint}', timeout=60) as response:
                data = json.load(response)
            (DEST / f'{entry}-{entity}.json').write_text(json.dumps(data, indent=2) + '\n')

if __name__ == '__main__':
    main()
