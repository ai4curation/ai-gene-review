"""Reconstruct source joins and sequence checks from byte-exact public inputs.

No network, gene-function prediction or annotation verdict generation. Python 3.10+;
the workbook reader requires xlrd==2.0.2. Parameters identify input records, not results.
"""
from pathlib import Path
import argparse, base64, csv, gzip, hashlib, io, json, re, zipfile
import xlrd

def sha(data):
    return hashlib.sha256(data).hexdigest()

class Inputs:
    def __init__(self,root):
        self.root=root;self.manifest=json.loads((root/'sources.json').read_text())
        self.entries={r['key']:r for r in self.manifest['inputs']};self.data={}
    def raw(self,key):
        if key not in self.data:
            r=self.entries[key];packed=(self.root/r['path']).read_bytes()
            assert sha(packed)==r['packed_sha256'] and len(packed)==r['packed_bytes'],key
            data=gzip.decompress(packed)
            assert sha(data)==r['sha256'] and len(data)==r['bytes'],key
            self.data[key]=data
        return self.data[key]
    def json(self,key):
        return json.loads(self.raw(key))
    def verify_all(self):
        for key in self.entries:self.raw(key)

def xrefs(row,db=None):
    return [x for group in row.get('withFrom') or [] for x in group['connectedXrefs']
            if db is None or x['db']==db]

def paint(inp,accession,source_rows):
    root=inp.json('tree')['search']['tree_topology']['annotation_node'];nodes=[]
    def walk(node,path):
        path=path+[node['persistent_id']];nodes.append((node,path))
        children=node.get('children',{}).get('annotation_node',[])
        for child in children if isinstance(children,list) else [children]:walk(child,path)
    walk(root,[])
    found=[(n,p)for n,p in nodes if f'UniProtKB={accession}' in n.get('node_name','').split('|')]
    assert len(found)==1,(accession,len(found))
    node,path=found[0];msa=inp.json('msa')['search']['MSA_list']['sequence_info']
    aligned=next(x['sequence']for x in msa if x['persistent_id']==node['persistent_id'])
    sequence=re.sub('[^A-Za-z]','',aligned).upper()
    official=inp.json('uniprot-'+accession)['sequence']['value']
    source_nodes={x['id'] for r in source_rows for x in xrefs(r,'PANTHER')}
    selected=[];all_path=[]
    for i,line in enumerate(inp.raw('ibd').decode().splitlines(),1):
        if line.startswith('!'):continue
        fields=line.split('\t')
        if len(fields)<7:continue
        if fields[1] in path:all_path.append(dict(line_1based=i,fields=fields))
        if fields[1] in source_nodes:selected.append(dict(line_1based=i,fields=fields))
    joins=[]
    for r in source_rows:
        if r['goEvidence']!='IBA':continue
        for x in xrefs(r,'PANTHER'):
            joins.append(dict(annotation_id=r['id'],term=r['goId'],node=x['id'],
                on_target_path=x['id'] in path,literal_IBD_lines=[s['line_1based']for s in selected
                if s['fields'][1]==x['id'] and s['fields'][4]==r['goId'] and s['fields'][6]=='IBD']))
    return dict(accession=accession,node=node['persistent_id'],node_name=node['node_name'],
                tree_nodes=len(nodes),MSA_sequences=len(msa),path=path,sequence_length=len(sequence),
                sequence_matches=sequence==official,literal_source_node_rows=selected,
                all_path_rows=all_path,source_joins=joins)

def interactions(inp,accession,source_rows):
    rows=list(csv.reader(io.StringIO(inp.raw('intact').decode()),delimiter='\t'))
    pairs=[];sequence_checks=[]
    for a in source_rows:
        if a['goId']!='GO:0005515':continue
        partners=[x['id']for x in xrefs(a,'UniProtKB')]
        pmid=a['reference'].replace('PMID:','pubmed:');matches=[]
        for i,r in enumerate(rows,1):
            if len(r)<38 or pmid not in r[8] or 'uniprotkb:'+accession not in r[:2]:continue
            if not any('uniprotkb:'+p in r[:2] for p in partners):continue
            match=dict(line_1based=i,ids=r[:2],detection=r[6],publication=r[8],taxa=r[9:11],
                type=r[11],interaction_id=r[13],confidence=r[14],expansion=r[15],
                biological_roles=r[16:18],experimental_roles=r[18:20],host=r[28],
                checksums=r[32:34],negative=r[35],features=r[36:38])
            matches.append(match)
            for j,identifier in enumerate(r[:2]):
                if not identifier.startswith('uniprotkb:'):continue
                acc=identifier.split(':',1)[1];key='uniprot-'+acc
                if key in inp.entries:
                    u=inp.json(key);seq=u['sequence']['value'];taxon=u['organism']['taxonId']
                elif 'fasta-'+acc in inp.entries:
                    text=inp.raw('fasta-'+acc).decode();seq=''.join(text.splitlines()[1:])
                    taxon=int(re.search(r' OX=(\d+)',text.splitlines()[0]).group(1));key='fasta-'+acc
                else:
                    sequence_checks.append(dict(line_1based=i,accession=acc,status='no saved sequence'));continue
                rid=base64.b64encode(hashlib.sha1(seq.encode()).digest()).decode().rstrip('=')+str(taxon)
                sequence_checks.append(dict(line_1based=i,accession=acc,sequence_source=key,
                    length=len(seq),taxon=taxon,reconstructed_ROGID=rid,observed=r[32+j],
                    matches='rogid:'+rid in r[32+j]))
        pairs.append(dict(annotation_id=a['id'],reference=a['reference'],partners=partners,
                          record_count=len(matches),matches=matches))
    return dict(raw_records=len(rows),source_pairs=pairs,sequence_checks=sequence_checks)

def workbook(inp,accession,source_rows):
    archive=zipfile.ZipFile(io.BytesIO(inp.raw('supplement-23414517')))
    symbols={g.get('geneName',{}).get('value') for g in inp.json('uniprot-'+accession).get('genes',[])}
    partners={x['id'].split('-')[0]for r in source_rows if r['reference']=='PMID:23414517'
              for x in xrefs(r,'UniProtKB')}
    output=[]
    for member in archive.namelist():
        if not member.endswith(('2044-5040-3-3-S1.xls','2044-5040-3-3-S2.xls')):continue
        data=archive.read(member);book=xlrd.open_workbook(file_contents=data)
        for sheet in book.sheets():
            selected=[];target_rows=0
            for i in range(sheet.nrows):
                values=sheet.row_values(i)
                has_target=accession in values if member.endswith('-S1.xls') else bool(values and values[0] in symbols)
                if not has_target:continue
                target_rows+=1
                if member.endswith('-S1.xls'):
                    # Original columns D/I are the two UniProt participants.
                    is_selected=len(values)>8 and accession in [values[3],values[8]] and any(p in [values[3],values[8]]for p in partners)
                else:is_selected=True
                if is_selected:selected.append(dict(row_1based=i+1,values=values))
            output.append(dict(member=member,sha256=sha(data),sheet=sheet.name,
                               rows=sheet.nrows,columns=sheet.ncols,
                               target_rows=target_rows,selected_rows=selected))
    return output

def project(inp,accession,paint_only):
    quickgo=inp.json('quickgo');rows=quickgo['results']
    assert quickgo['pageInfo']['total']==1 and len(rows)==quickgo['numberOfHits']
    source_rows=[r for r in rows if r['geneProductId']=='UniProtKB:'+accession]
    result=dict(target=accession,source_annotation_count=len(source_rows),
                paint=paint(inp,accession,source_rows))
    mapped=inp.json('panther-geneinfo')['search']['mapped_genes']['gene']
    if mapped.get('mapped_id_list')==accession:
        result['family_mapping']=dict(accession=mapped['mapped_id_list'],
            panther_family=mapped['family_id'],panther_subfamily=mapped['sf_id'],
            uniprot_pointers=[x['id']for x in inp.json('uniprot-'+accession)['uniProtKBCrossReferences']
                             if x['database']=='PANTHER'])
    if paint_only:return result
    result['interactions']=interactions(inp,accession,source_rows)
    result['workbooks']=workbook(inp,accession,source_rows)
    result['partner_identifiers']=[dict(accession=u['primaryAccession'],
        gene_symbols=[g.get('geneName',{}).get('value')for g in u.get('genes',[])],
        taxon=u['organism']['taxonId'],sequence_length=u['sequence']['length'])
        for k in sorted(inp.entries)if k.startswith('uniprot-')for u in [inp.json(k)]]
    result['term_definitions']=[dict(source=k,result=inp.json(k)['results'][0])
        for k in sorted(inp.entries)if k.startswith('GO')]
    return result

def main():
    p=argparse.ArgumentParser();p.add_argument('--input-dir',type=Path,default=Path(__file__).resolve().parent)
    p.add_argument('--accession',default='O75923');p.add_argument('--paint-only',action='store_true')
    p.add_argument('--output',type=Path);p.add_argument('--check',type=Path)
    a=p.parse_args();inp=Inputs(a.input_dir);inp.verify_all();result=project(inp,a.accession,a.paint_only)
    text=json.dumps(result,indent=2)+'\n'
    if a.check:assert a.check.read_text()==text,'Saved output differs'
    if a.output:a.output.write_text(text)
    i=result.get('interactions',{})
    print(json.dumps(dict(status='PASS',inputs=len(inp.entries),target=a.accession,
        tree_nodes=result['paint']['tree_nodes'],sequence_length=result['paint']['sequence_length'],
        sequence_matches=result['paint']['sequence_matches'],
        source_rows=result['source_annotation_count'],interaction_records=i.get('raw_records'),
        sequence_checks=len(i.get('sequence_checks',[])),
        matching_sequences=sum(x.get('matches',False)for x in i.get('sequence_checks',[])))))

if __name__=='__main__':main()
