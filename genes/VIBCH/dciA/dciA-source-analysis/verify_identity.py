from pathlib import Path
import json, hashlib, re, yaml
root=Path(__file__).resolve().parent
entry=json.loads((root/'9TZF-entry.json').read_text())
assert entry['rcsb_primary_citation']['pdbx_database_id_PubMed']==42927770
uniprot=json.loads((root/'uniprot-AAF95538.json').read_text())['results'][0]
assert uniprot['primaryAccession']=='Q9KPH3'
raw=(root.parent/'dciA-uniprot.txt').read_text()
seq=''.join(re.findall('[A-Z]+',raw.split('SQ   SEQUENCE',1)[1].split('\n',1)[1].split('//')[0]))
entities={}
for eid,accession,expected in [('1','Q9KUY7',json.loads((root/'Q9KUY7.json').read_text())['sequence']['value']),('2','Q9KPH3',seq)]:
 d=json.loads((root/f'9TZF-entity{eid}.json').read_text())
 assert d['rcsb_polymer_entity_container_identifiers']['uniprot_ids']==[accession]
 pdbseq=d['entity_poly']['pdbx_seq_one_letter_code_can']
 assert pdbseq==expected
 assert d['rcsb_entity_source_organism'][0]['ncbi_taxonomy_id']==243277
 entities[eid]={'accession':accession,'sequence_length':len(expected),'sequence_identical':True,'sequence_sha256':hashlib.sha256(expected.encode()).hexdigest(),'source_taxon_id':243277,'source_strain':d['rcsb_entity_source_organism'][0]['scientific_name']}
assert seq==uniprot['sequence']['value']
gp=(root/'AAF95538.1.gp').read_text();gpseq=''.join(re.findall('[a-z]+',gp.split('ORIGIN',1)[1].split('//')[0])).upper();assert gpseq==seq
proof={'status':'PASS','pdb':'9TZF','primary_pmid':42927770,'entities':entities,'DciA_GenBank_accession':'AAF95538.1','DciA_locus':'VC_2395','DciA_reference_sequence_identity':True,'scope':'Deposited full polymer-entity sequence and primary source taxonomy; not every residue is necessarily modeled. Donor source strain is established by deposit, not assumed from the alignment accession.'}
(root/'identity-proof.yaml').write_text(yaml.safe_dump(proof,sort_keys=False,width=100));print(proof)
