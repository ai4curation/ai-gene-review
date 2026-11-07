#!/usr/bin/env python3
"""Reproduce paper-accession, frozen sequence and source-genome primer checks."""
from pathlib import Path
from Bio.Seq import Seq
import json,re,hashlib
root=Path(__file__).resolve().parents[4]
p=Path(__file__).resolve().parent
def upseq(path):return re.sub('[^A-Z]','',path.read_text().split('\nSQ ')[-1].split('\n',1)[1].split('//')[0])
def fasta(path):return ''.join(path.read_text().splitlines()[1:]).replace(' ','')
a=upseq(root/'genes/STRLI/cslA/cslA-uniprot.txt');old=upseq(p/'A0A7U9DT44-unisave-v1.txt');gp=fasta(p/'EOY47900.1.fasta');uparc=json.loads((p/'UPI0001B50C52.json').read_text())['sequence']['value'];nt=fasta(p/'CM001889.1-window.fasta')
g=upseq(root/'genes/STRL6/glxA/glxA-uniprot.txt');gen_a=str(Seq(nt[:1962]).translate(table=11)).rstrip('*');gen_g=str(Seq(nt[1958:]).translate(table=11)).rstrip('*')
primers={'3187-F':'ATGACGTCGACGCCGACGGGCG','3187-R':'TTCCTTACGTCCCCCAAGTCCACCAAGGG','3188-F':'CGCTTCGCGATAGGTACGGCG','3188-R':'CGGCACCCGCACCCACTC','glxABlam-F':'ATGAAAGACCGTGCCGGCCGCCGC'}
checks={}
for name,seq in primers.items():
 target=str(Seq(seq).reverse_complement()) if name.endswith('-R') else seq
 i=nt.find(target);checks[name]={'annealing_sequence_5to3':seq,'genome_match_start_1based':3307657+i if i>=0 else None,'note':'Restriction-site/vector overhang excluded; exact annealing sequence from supplement Table S1.'}
report={'cslA':{'length':len(a),'current_TK24_equals_paper_1326_archived_UniProt':a==old,'current_equals_source_1326_GenBank':a==gp,'current_equals_UniParc':a==uparc,'current_equals_translated_1326_genomic_CDS':a==gen_a,'sequence_sha256':hashlib.sha256(a.encode()).hexdigest(),'source_strain':'1326/66','reference_strain':'TK24','paper_accession':'A0A7U9DT44','current_accession':'A0ABM5R5V5'},'glxA':{'length':len(g),'current_equals_translated_extended_1326_genomic_CDS':g==gen_g,'genomic_interval':'CM001889.1:3309615..3311552','genbank_old_model_length':len(fasta(root/'genes/STRL6/glxA/glxA-source-analysis/EOY47901.1.fasta')),'sequence_sha256':hashlib.sha256(g.encode()).hexdigest(),'supplement_FigS2_Nterminus_matches':g.startswith('MKDRAGRRRARRFAIGTAVVVALAGMNGPWLYRFSTEKYHQYK')},'primers':checks,'construct_limits':'The 2024 synthase assay coexpressed tagged CslA with PelB-GlxA(12-645) in E. coli. The NdeI primer design can add an initiating Met before native CslA; no independently deposited complete engineered plasmid sequence was checked. Exact native sequence identity does not transfer native regulation or phenotype between strains.'}
assert a==old==gp==uparc==gen_a
assert g==gen_g
assert all(c['genome_match_start_1based'] is not None for c in checks.values())
print(json.dumps(report,indent=2))
