"""Download a source file, or extract one specified member of a source ZIP."""
import argparse
from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen
from zipfile import ZipFile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('url')
parser.add_argument('output', type=Path)
parser.add_argument('--member')
args = parser.parse_args()
with urlopen(Request(args.url, headers={'User-Agent': 'ai-gene-review source verification'}), timeout=90) as response:
    content = response.read()
if args.member:
    with ZipFile(BytesIO(content)) as archive:
        content = archive.read(args.member)
args.output.write_bytes(content)
