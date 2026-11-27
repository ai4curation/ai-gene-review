"""Compare a frozen UniProt sequence with complete RCSB entity and ENA translations."""
import argparse, json, re
from pathlib import Path

def uniprot_sequence(text):
    return ''.join(re.findall('[A-Z]+', text.split('SQ   ', 1)[1].split('\n',1)[1].split('//',1)[0]))

def compare(target, query):
    start = query.find(target)
    return {'target_length':len(target),'query_length':len(query),
            'exact_full_target_match':start >= 0,'query_start_1based':start+1 if start>=0 else None,
            'prefix':query[:start] if start>=0 else None,'suffix':query[start+len(target):] if start>=0 else None}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('uniprot');ap.add_argument('sources',nargs='+');a=ap.parse_args()
    target=uniprot_sequence(Path(a.uniprot).read_text());out={}
    for source in a.sources:
        p=Path(source)
        if p.suffix=='.json':
            j=json.loads(p.read_text());query=j['entity_poly']['pdbx_seq_one_letter_code_can']
            out[p.name]={'comparison':compare(target,query),'sources':j.get('entity_src_gen',[])}
        else:
            matches=[]
            for block in re.split(r'\nFT   CDS ',p.read_text())[1:]:
                block=re.split(r'\nFT   \S',block,1)[0]
                m=re.search(r'/translation="([^"]+)"',block)
                if m:
                    query=re.sub(r'[^A-Z]','',re.sub(r'(?m)^FT\s+', '',m.group(1)))
                    result=compare(target,query)
                    if result['exact_full_target_match']:matches.append(result)
            out[p.name]={'matching_translations':matches}
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
