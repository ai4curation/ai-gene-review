#!/usr/bin/env python3
"""Fetch PANTHER family MSA and convert to aligned FASTA format."""

import json
import sys
from pathlib import Path
import urllib.request


def fetch_msa(family_id: str, output_dir: Path) -> Path:
    """Fetch MSA from PANTHER API and save as aligned FASTA."""
    output_dir.mkdir(parents=True, exist_ok=True)

    url = f"https://www.pantherdb.org/services/oai/pantherdb/familymsa?family={family_id}"
    print(f"Fetching MSA for {family_id} from PANTHER API...")

    with urllib.request.urlopen(url) as response:
        data = json.load(response)

    msa = data['search']['MSA_list']['sequence_info']
    output_file = output_dir / f"{family_id}.afa"

    with open(output_file, 'w') as f:
        for seq in msa:
            pid = seq['persistent_id']
            # Convert dots to dashes for standard gap character
            aligned_seq = seq['sequence'].replace('.', '-')
            f.write(f">{pid}\n")
            # Print in 80-char lines
            for i in range(0, len(aligned_seq), 80):
                f.write(aligned_seq[i:i+80] + "\n")

    print(f"Saved aligned FASTA to {output_file}")
    print(f"Sequences: {len(msa)}")
    print(f"Alignment length: {len(msa[0]['sequence'])}")

    return output_file


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fetch_family_msa.py FAMILY_ID [OUTPUT_DIR]")
        sys.exit(1)

    family_id = sys.argv[1]
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(f"interpro/panther/{family_id}/msa")

    fetch_msa(family_id, output_dir)
