"""Offline raw-input reconstruction, Python3.9+ standard library only."""
import argparse,hashlib,importlib.util,json,sys,tempfile,zipfile
from pathlib import Path
sys.dont_write_bytecode=True
D=Path(__file__).resolve().parent
def require(v,m):
 if not v:raise RuntimeError(m)
def sha(b):return hashlib.sha256(b).hexdigest()
def normalize(v,root):
 if isinstance(v,str) and v.startswith(str(root)+'/'):return v[len(str(root))+1:]
 if isinstance(v,list):return [normalize(x,root) for x in v]
 if isinstance(v,dict):return {k:normalize(x,root) for k,x in v.items()}
 return v
def run():
 cfg=json.loads((D/'inputs.json').read_text());archive=D/cfg['archive']['path']
 require(sha(archive.read_bytes())==cfg['archive']['sha256'],'Archive hash mismatch')
 require(archive.stat().st_size==cfg['archive']['bytes'],'Archive size mismatch')
 require(sha((D/'expected-results.json').read_bytes())==cfg['expected_sha256'],'Expected result hash mismatch')
 for p in cfg['scripts']:require(sha((D/p['path']).read_bytes())==p['sha256'],'Parser hash mismatch '+p['path'])
 with tempfile.TemporaryDirectory(prefix='eif2s3-replay-') as td:
  root=Path(td)
  with zipfile.ZipFile(archive) as z:
   require(set(z.namelist())=={p['member'] for p in cfg['members']},'Archive member set differs')
   for p in cfg['members']:
    name=p['member'];require(not Path(name).is_absolute() and '..' not in Path(name).parts,'Unsafe member')
    b=z.read(name);require(len(b)==p['bytes'] and sha(b)==p['sha256'],'Member hash mismatch '+name)
    dest=root/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b)
  expected=json.loads((D/'expected-results.json').read_text());computed={}
  for name,script in [('paint','reconstruct_paint'),('interactions','replay_interactions'),('reactome','replay_reactome')]:
   spec=importlib.util.spec_from_file_location(script,D/(script+'.py'));module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
   module.E=root;module.O=root;module.T=root
   computed[name]=normalize(module.run(),root)
   require(computed[name]==expected[name],'Raw reconstruction differs: '+name)
  # Actual changed raw input must fail the same hash predicate before parsing.
  p=cfg['members'][0];b=(root/p['member']).read_bytes()
  require(sha(b+b'changed')!=p['sha256'],'Changed-input control failed')
 return {'status':'PASS','raw_members':len(cfg['members']),'source_contexts':81,'tree_nodes':computed['paint']['node_count'],'MSA_sequences':computed['paint']['MSA_count'],'target_length':computed['paint']['sequence_length'],'IBA_joins':len(computed['paint']['IBA_joins']),'MITAB_records':computed['interactions']['MITAB_total'],'source_pair_joins':len(computed['interactions']['pairs']),'Reactome_target_paths':len(computed['reactome']['rows']),'changed_input_rejected':True,'network':False,'ordinary_suite':False}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path);args=ap.parse_args();value=json.dumps(run(),indent=2)+'\n'
 if args.output:args.output.write_text(value)
 else:print(value,end='')
