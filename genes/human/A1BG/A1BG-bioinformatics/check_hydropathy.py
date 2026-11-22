"""Recompute a Kyte-Doolittle sliding-window profile from a cached UniProt flat file."""
import argparse
import hashlib
import json
from pathlib import Path
import re

KD = {'A':1.8, 'R':-4.5, 'N':-3.5, 'D':-3.5, 'C':2.5, 'Q':-3.5,
      'E':-3.5, 'G':-0.4, 'H':-3.2, 'I':4.5, 'L':3.8, 'K':-3.9,
      'M':1.9, 'F':2.8, 'P':-1.6, 'S':-0.8, 'T':-0.7, 'W':-0.9,
      'Y':-1.3, 'V':4.2}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('input', type=Path)
parser.add_argument('--window', type=int, default=19)
parser.add_argument('--region-start', type=int, default=1, help='One-based start of region whose maximum is reported')
parser.add_argument('--threshold', type=float, default=1.6)
args = parser.parse_args()
raw = args.input.read_bytes()
body = raw.decode().split('SQ   SEQUENCE', 1)[1].split('\n', 1)[1].split('//', 1)[0]
seq = ''.join(re.findall(r'[A-Z]+', body))
if not 1 <= args.window <= len(seq) or not 1 <= args.region_start <= len(seq)-args.window+1:
    parser.error('Window and region start must identify complete sequence windows')
profile = [sum(KD[aa] for aa in seq[i:i+args.window])/args.window for i in range(len(seq)-args.window+1)]
region = profile[args.region_start-1:]
maximum = max(region)
print(json.dumps({'input': str(args.input), 'input_sha256': hashlib.sha256(raw).hexdigest(),
    'sequence_sha256': hashlib.sha256(seq.encode()).hexdigest(), 'length': len(seq),
    'window': args.window, 'threshold': args.threshold, 'region_start': args.region_start,
    'region_maximum': maximum, 'region_maximum_window_start': region.index(maximum)+args.region_start,
    'above_threshold': [{'start': i+1, 'end': i+args.window, 'score': score}
                        for i, score in enumerate(profile) if score > args.threshold],
    'profile': profile}, indent=2))
