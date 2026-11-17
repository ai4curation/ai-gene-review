"""Reproduce the declared gap-penalty sensitivity panel without editing protected inputs."""
from copy import deepcopy
from pathlib import Path
import argparse

import yaml
from sequence_check import analyze

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('config', type=Path)
parser.add_argument('output', type=Path)
args = parser.parse_args()
config = yaml.safe_load(args.config.read_text())
results = []
for opening, extension in config['sensitivity_gap_penalties']:
    varied = deepcopy(config)
    varied['method']['open_gap_score'] = opening
    varied['method']['extend_gap_score'] = extension
    results.append(analyze(varied, Path.cwd()))
args.output.write_text(yaml.safe_dump(results, sort_keys=False))
