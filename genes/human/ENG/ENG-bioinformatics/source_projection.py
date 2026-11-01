import collections,csv,io,json
FIELDS=['GENE PRODUCT DB','GENE PRODUCT ID','SYMBOL','QUALIFIER','GO TERM','GO NAME','GO ASPECT','ECO ID','GO EVIDENCE CODE','REFERENCE','WITH/FROM','TAXON ID','TAXON NAME','ASSIGNED BY','GENE NAME','DATE']
def need(v,m):
 if not v:raise ValueError(m)
def key(term,ev,ref,qual,entities,acc):
 q=qual.split('|');return(term,ev,ref,next((x for x in q if x!='NOT'),''),tuple(sorted(set(entities)-{''})),'NOT'in q,acc if'-'in acc else None)
def sk(r):return(r['term']['id'],r['evidence_type'],r['original_reference_id'],r.get('qualifier',''),tuple(sorted(r.get('supporting_entities',[]))),r.get('negated',False),r.get('isoform'))
def rk(r):return key(r['GO TERM'],r['GO EVIDENCE CODE'],r['REFERENCE'],r['QUALIFIER'],r['WITH/FROM'].split('|'),r['GENE PRODUCT ID'])
def qk(r):return key(r['goId'],r['goEvidence'],r['reference'],r['qualifier'],[x['db']+':'+x['id']for g in r.get('withFrom')or[]for x in g['connectedXrefs']],r['geneProductId'].split(':',1)[1])
def qrow(r):
 db,acc=r['geneProductId'].split(':',1);wf='|'.join(x['db']+':'+x['id']for g in r.get('withFrom')or[]for x in g['connectedXrefs']);vals=[db,acc,r['symbol'],r['qualifier'],r['goId'],r['goName'],r['goAspect'],r['evidenceCode'],r['goEvidence'],r['reference'],wf,str(r['taxonId']),r['taxonName'],r['assignedBy'],r['name'],r['date']];return dict(zip(FIELDS,vals))
def derive(preflight,enriched,tsv,sources):
 need(enriched['numberOfHits']==len(enriched['results'])==len(preflight)==106,'raw response complete');q=enriched['results'];drop={'goName','taxonName','name'};norm=lambda rs:{r['id']:{k:v for k,v in r.items()if k not in drop}for r in rs};need(norm(q)==norm(preflight),'raw source identity beyond name enrichment')
 order=sorted(range(len(q)),key=lambda i:(0 if q[i].get('goEvidence')=='IBA'else 1,-int(q[i].get('date')or'0'),q[i]['goId']));projected=[qrow(r)for r in q];out=[];seen=set()
 for n in order:
  row='\t'.join(projected[n][k]for k in FIELDS)
  if row not in seen:seen.add(row);out.append(row)
 rebuilt='\t'.join(FIELDS)+'\n'+'\n'.join(out)+'\n';need(rebuilt==tsv,'exact ordinary TSV projection bytes');rows=list(csv.DictReader(io.StringIO(tsv),delimiter='\t'));need(len(rows)==105,'normal TSV count')
 tmap=collections.defaultdict(list);qmap=collections.defaultdict(list)
 for n,r in enumerate(rows):tmap[rk(r)].append(n)
 for n,r in enumerate(q):qmap[qk(r)].append(n)
 need(len(sources)==104 and set(map(sk,sources))==set(tmap)==set(qmap),'seed full coverage');joins=[]
 for n,s in enumerate(sources):
  k=sk(s);need(all(s['term']['label']==rows[j]['GO NAME']for j in tmap[k]),'source term label');joins.append(dict(annotation_index=n,source=s,tsv_indices=tmap[k],raw_indices=qmap[k]))
 tjoins=[dict(tsv_index=n,raw_indices=[j for j,x in enumerate(projected)if x==r])for n,r in enumerate(rows)];need(all(x['raw_indices']for x in tjoins),'all TSV rows mapped')
 return dict(raw_API_count=106,normal_TSV_count=105,seed_source_count=104,joins=joins,tsv_raw_joins=tjoins,tsv_projection_collapses=[x for x in tjoins if len(x['raw_indices'])>1],seed_context_collapses=[dict(annotation_index=x['annotation_index'],tsv_indices=x['tsv_indices'],raw_indices=x['raw_indices'],raw_records=[q[j]for j in x['raw_indices']])for x in joins if len(x['raw_indices'])>1],raw_source_fields_exact_except_requested_name_enrichment=True,ordinary_TSV_bytes_reproduced=True,source_edits=0,scope='The repository TSV projection omits annotation extensions; the seed additionally consolidates context-equivalent dated rows. Full original raw records/extensions remain separately immutable. No extra source annotations were manufactured.')
def quotes(x):return (int('supporting_text'in x)+sum(map(quotes,x.values())))if isinstance(x,dict)else sum(map(quotes,x))if isinstance(x,list)else 0
