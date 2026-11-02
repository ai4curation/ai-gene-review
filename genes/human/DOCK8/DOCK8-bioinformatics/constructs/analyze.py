"""Extract a named library insert and compare its three forward translations to FASTAs.
No protein identity or expected match is encoded. Standard genetic code; exact full
sequence matches only. Vector flanks are reported separately. Python standard library.
"""
import argparse,hashlib,json,pathlib,posixpath,xml.etree.ElementTree as E,zipfile
N={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
BASES='TCAG';AAS='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG';CODE=dict(zip((a+b+c for a in BASES for b in BASES for c in BASES),AAS))
def workbook(p):
 with zipfile.ZipFile(p)as z:
  ss=[''.join(a.itertext())for a in E.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si',N)];rels={a.attrib['Id']:a.attrib['Target']for a in E.fromstring(z.read('xl/_rels/workbook.xml.rels'))};out={}
  for sh in E.fromstring(z.read('xl/workbook.xml')).findall('s:sheets/s:sheet',N):
   xp=rels[sh.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']];xp=xp.lstrip('/')if xp.startswith('/')else posixpath.normpath('xl/'+xp);rows=[]
   for row in E.fromstring(z.read(xp)).findall('s:sheetData/s:row',N):
    cells={}
    for a in row.findall('s:c',N):
     v=a.find('s:v',N);v=v.text if v is not None else None
     if a.attrib.get('t')=='s':v=ss[int(v)]
     elif a.attrib.get('t')=='inlineStr':v=''.join(a.find('s:is',N).itertext())
     if v is not None:cells[a.attrib['r']]=v
    if cells:rows.append({'row':int(row.attrib['r']),'cells':cells})
   out[sh.attrib['name']]=rows
  return out
def fasta(p):
 records=[];name=None;seq=[]
 for line in p.read_text().splitlines():
  if line.startswith('>'):
   if name is not None:records.append((name,''.join(seq)))
   name=line[1:].split()[0];seq=[]
  elif line.strip():seq.append(line.strip().upper())
 if name is not None:records.append((name,''.join(seq)))
 if not records:raise ValueError('No FASTA records: '+str(p))
 return records
def analyze(wp,gene,fastas):
 w=workbook(wp);rows=[r for r in w['Supplementary Table 1']if gene in r['cells'].values()]
 if len(rows)!=1:raise ValueError('Expected one unambiguous library row')
 row=rows[0];ds=[(k,v.upper())for k,v in row['cells'].items()if len(v)>1000 and set(v.upper())<=set('ACGT')]
 if len(ds)!=1:raise ValueError('Expected one unambiguous DNA cell')
 cell,dna=ds[0];trans=[''.join(CODE[dna[i:i+3]]for i in range(f,len(dna)-2,3))for f in range(3)];matches=[];compared=[]
 for fp in fastas:
  for name,seq in fasta(fp):
   compared.append({'accession':name,'length':len(seq),'sequence_sha256':hashlib.sha256(seq.encode()).hexdigest()})
   for frame,t in enumerate(trans):
    at=t.find(seq)
    if at>=0:matches.append({'accession':name,'length':len(seq),'frame_zero_based':frame,'offset_aa':at,'upstream':t[:at],'downstream':t[at+len(seq):]})
 selected={n:[r for r in rs if gene in r['cells'].values()]for n,rs in w.items()if any(gene in r['cells'].values()for r in rs)}
 for rows2 in selected.values():
  for r in rows2:
   r['cells']={k:({'length_nt':len(v),'sha256':hashlib.sha256(v.upper().encode()).hexdigest()}if len(v)>1000 and set(v.upper())<=set('ACGT')else v)for k,v in r['cells'].items()}
 return {'gene':gene,'workbook_sha256':hashlib.sha256(wp.read_bytes()).hexdigest(),'DNA_cell':cell,'DNA_length':len(dna),'DNA_sha256':hashlib.sha256(dna.encode()).hexdigest(),'library_row':row['row'],'compared':compared,'matches':matches,'target_table_rows':selected},dna
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--workbook',type=pathlib.Path,required=True);p.add_argument('--gene',required=True);p.add_argument('--fasta',nargs='+',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);p.add_argument('--dna-output',type=pathlib.Path,required=True);a=p.parse_args();result,dna=analyze(a.workbook,a.gene,a.fasta);a.output.write_text(json.dumps(result,indent=2)+'\n');a.dna_output.write_text('>'+a.gene+'_deposited_DNA_with_vector_flanks\n'+'\n'.join(dna[i:i+80]for i in range(0,len(dna),80))+'\n');print(json.dumps({'gene':a.gene,'matches':result['matches']}))
