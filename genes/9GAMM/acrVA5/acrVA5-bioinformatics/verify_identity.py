"""Verify the archived AcrVA5 sequence against primary structure/RefSeq records.
Run: uv run python genes/9GAMM/acrVA5/acrVA5-bioinformatics/verify_identity.py
Uses repository requests dependency; no alignment heuristics or gene-name matches.
"""
from pathlib import Path
import hashlib,json,requests
ROOT=Path(__file__).resolve().parents[4]
folder=Path(__file__).resolve().parent
flat=(folder.parent/'acrVA5-uniprot.txt').read_text()
seq=''.join(flat.split('SQ   SEQUENCE',1)[1].split('\n',1)[1].split('//',1)[0].split())
pdb_url='https://data.rcsb.org/rest/v1/core/polymer_entity/6IUF/1'
r=requests.get(pdb_url,timeout=60);r.raise_for_status();pdb=r.json()['entity_poly']['pdbx_seq_one_letter_code_can']
ref_url='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&id=WP_046699157.1&rettype=fasta&retmode=text'
r=requests.get(ref_url,timeout=60);r.raise_for_status();fasta=r.text;ref=''.join(fasta.splitlines()[1:])
assert len(seq)==92 and pdb=='PLGS'+seq and ref==seq
result={'accession':'A0A0U2B867','unisave_version':17,'length':len(seq),'sequence_sha256':hashlib.sha256(seq.encode()).hexdigest(),'pdb_url':pdb_url,'pdb_relation':'Exact 92-aa match after the N-terminal PLGS construct tag','refseq_url':ref_url,'refseq_relation':'Exact 92-aa match','refseq_header':fasta.splitlines()[0]}
(folder/'identity-check.json').write_text(json.dumps(result,indent=2)+'\n')
(folder/'RESULTS.md').write_text('# AcrVA5 construct identity\n\nOfficial UniSave A0A0U2B867 version 17 is a 92-residue protein from Moraxella bovoculi, AAX07_09540. Its full sequence matches RefSeq WP_046699157.1 exactly. PDB 6IUF entity 1 contains the same 92 residues preceded by the PLGS construct tag; no sequence substitutions are required.\n\nThis is a direct sequence comparison, not inference from the ProtNLM protein name. The archival transport script preserves the original record and version metadata, then invokes the normal repository GOA/seed pipeline. Current UniProt marks the accession deleted because it is not in a reference proteome; this is a database inclusion change, not a biological absence.\n\nThe complete source URLs and SHA256 digest are in identity-check.json. Re-run verify_identity.py from the repository environment to reproduce both comparisons.\n')
print(json.dumps(result,indent=2))
