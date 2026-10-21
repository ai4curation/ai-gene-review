#!/usr/bin/env python3
"""Offline, standard-library ELN evidence replay; does not modify the supplied package."""
from pathlib import Path
import hashlib,io,json,subprocess,sys,tarfile,tempfile
D=Path(__file__).resolve().parent

def main():
 m=json.loads((D/'archive-manifest.json').read_text());data=(D/m['archive']).read_bytes()
 if len(data)!=m['bytes']or hashlib.sha256(data).hexdigest()!=m['sha256']:raise ValueError('Archive integrity mismatch')
 with tempfile.TemporaryDirectory(prefix='eln-evidence-')as tmp:
  root=Path(tmp)
  with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz')as tf:
   members=tf.getmembers()
   if len(members)!=m['members']:raise ValueError('Archive member count mismatch')
   for member in members:
    p=Path(member.name)
    if not member.isfile()or p.is_absolute()or '..'in p.parts:raise ValueError('Unsafe archive member')
    target=root/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(tf.extractfile(member).read())
  r=subprocess.run([sys.executable,'-B',str(root/'reproduce.py')],capture_output=True,text=True)
  if r.returncode:raise RuntimeError(r.stderr)
  print(r.stdout,end='')
if __name__=='__main__':main()
