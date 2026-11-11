# EGR2 database evidence replay

This Python-standard-library analysis reconstructs the source identities behind the EGR2 PAINT, mouse-ortholog, HCFC1 interaction and Reactome assertions. It reports evidence and its scope; it does not choose annotation actions.

```sh
python reproduce.py --output /tmp/EGR2-results.json --compare results.json
```

The default input is the included `inputs.tar.gz`. Alternatively, provide a directory containing the exact files named in `input-manifest.json`:

```sh
python reproduce.py --inputs-dir /path/to/saved-inputs --output /tmp/EGR2-results.json --compare results.json
```

The archive and each input must match their recorded SHA-256 hashes. Results are computed from the complete saved inputs, not hardcoded counts. Unexpected identities, incomplete donor pagination, missing target membership or altered input bytes cause an explicit error. Python 3.10 or newer is sufficient; no package installation or network access is needed for replay.

`input-manifest.json` records official source URLs and acquisition metadata. The full IBD file is an exact reused official snapshot; its current download URL may now serve a newer release. The archive contains database responses and that IBD snapshot, not original article bodies. Original publications remain separately cited in the review and source guide. Source databases retain their own terms and attribution requirements.

Reference-sequence ROGIDs are compared independently of assayed fragment coordinates. A matching human database parent sequence does not prove that an experimental Krox20 insert was human. Reactome paths distinguish input from expression output and alternative sets from complexes. The annotations' source dictionaries are included only to define which target assertions are being traced.
