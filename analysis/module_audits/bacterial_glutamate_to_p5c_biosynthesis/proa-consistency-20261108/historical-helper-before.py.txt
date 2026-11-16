from pathlib import Path
import copy,datetime,hashlib,json,yaml
ROOT=Path.cwd(); A=Path('analysis/module_audits/bacterial_glutamate_to_p5c_biosynthesis'); OUT=A/'proa-localization-followup-20261107'
REVIEW=Path('genes/BACSU/proA/proA-ai-review.yaml');NOTES=Path('genes/BACSU/proA/proA-notes.md');HTML=Path('genes/BACSU/proA/proA-ai-review.html');HISTORY=Path('history/genes/BACSU/proA/2026-11-07T141916Z-codex-977c55.yaml')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(name,obj):(OUT/name).write_text(json.dumps(obj,indent=2)+'\n')
def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
before=json.loads((OUT/'before.json').read_text());old=before['gene_review'];new=yaml.safe_load(REVIEW.read_text())
payload=lambda d:[{k:v for k,v in row.items() if k!='review'} for row in d['existing_annotations']]
assert payload(old)==payload(new),'ordered original payload changed'
assert len(new['existing_annotations'])==7
old_new=[row for row in old['existing_annotations'] if row.get('review',{}).get('action')=='NEW'];new_new=[row for row in new['existing_annotations'] if row.get('review',{}).get('action')=='NEW'];assert old_new==new_new==[]
changed_rows=[i for i,(a,b) in enumerate(zip(old['existing_annotations'],new['existing_annotations'])) if a!=b]
assert len(changed_rows)==1
idx=changed_rows[0];row=new['existing_annotations'][idx];assert row['term']['id']=='GO:0005737' and row['review']['action']=='MODIFY'
assert row['review']['proposed_replacement_terms']==[{'id':'GO:0005829','label':'cytosol'}]
assert [r for r in new['references'] if r['id']!='PMID:39514317']==old['references'],'prior reference changed'
assert sum(r['id']=='PMID:39514317' for r in new['references'])==1
pub=Path('publications/PMID_39514317.md').read_text();meta=yaml.safe_load(pub.split('---',2)[1]);assert next(r['title'] for r in new['references'] if r['id']=='PMID:39514317')==meta['title']
expected=copy.deepcopy(old);expected['existing_annotations'][idx]=copy.deepcopy(row);expected['references']=copy.deepcopy(new['references']);expected['core_functions'][0]['locations']=[{'id':'GO:0005829','label':'cytosol'}]
added_support=new['core_functions'][0]['supported_by'][0];assert added_support['reference_id']=='PMID:39514317';expected['core_functions'][0]['supported_by'].insert(0,copy.deepcopy(added_support));assert expected==new,'change exceeds permitted semantic scope'
assert NOTES.read_text().startswith(before['notes_before']),'prior journal changed'
protected=[]
for name,b in before['protected_inputs'].items():
 p=Path(name);actual={'sha256':sha(p),'mode':oct(p.stat().st_mode&0o777)};assert actual==b,name;protected.append(name)
h=yaml.safe_load(HISTORY.read_text());assert h['session']['actors'][0]['name']=='codex';assert h['links']['prs']==['https://github.com/ai4curation/ai-gene-review/pull/6160']
checks=json.loads((OUT/'check-results.json').read_text());assert len(checks)==4 and all(c['exit_code']==0 for c in checks)
prior=A/'approved-main-20261107-1356-closeout.json';frozen=json.loads(prior.read_text())['preserved_files_sha256'];superseded=[];unchanged=[]
allowed={str(REVIEW),str(NOTES),str(HTML)}
for p,original_hash in frozen.items():
 current_hash=sha(p)
 if current_hash!=original_hash:
  assert p in allowed,('unexpected prior freeze mismatch',p)
  superseded.append({'path':p,'prior_sha256':original_hash,'successor_sha256':current_hash})
 else:unchanged.append(p)
assert {x['path'] for x in superseded}==allowed
proof={'status':'PASS','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'base_head':'fac0eff742ca6162198945aec4a75deaa6735226','ordered_rows':7,'machine_rows':7,'historical_NEW_before':0,'historical_NEW_after':0,'authored_NEW_added':0,'all_original_fields_including_qualifiers_preserved':True,'ordered_original_payload_sha256':digest(payload(new)),'changed_review_row_zero_based_index':idx,'action_change':'GO:0005737 ACCEPT -> MODIFY, replacement GO:0005829','prior_references_unchanged':True,'source_title_exact_match':True,'only_author_core_change':'location cytoplasm -> cytosol; one comparative support added','prior_notes_preserved_as_prefix':True,'protected_byte_and_mode_inputs':len(protected),'protected_paths':protected,'raw_files_unchanged':2,'publication_bytes_unchanged':True,'prior_manifest':str(prior),'prior_manifest_sha256':sha(prior),'prior_manifest_entries':len(frozen),'prior_entries_unchanged':len(unchanged),'explicit_successor_overrides':superseded,'checks':checks,'full_validation':'NOT_RUN_SCOPED_FOLLOWUP'}
dump('preservation-proof.json',proof)
report='''# ProA localization follow-up — PR6160

Completed the authorized narrow correction at base fac0eff742ca6162198945aec4a75deaa6735226. BACSU ProA's existing GO:0005737 row is now MODIFY with replacement GO:0005829, and its author core location is cytosol. PMID39514317 was added once with the exact cached title, a source review and a localization finding.

This is explicitly a comparative inference: native-locus E. coli ProA-msfGFP microscopy plus target HAMAP localization and soluble reductase architecture, not a Bacillus localization assay. The prior rationale incorrectly treated possible transient intracellular associations as excluding cytosol; the existing ontology response expressly includes protein complexes in that compartment. Presence or absence of a separate GOA row does not settle the biological inference.

All seven ordered machine annotation payloads, including every qualifier and supporting entity, are unchanged. There were zero historical NEW rows and none were added. Only the cytoplasm row's review changed; all other reviews and all prior reference assessments are semantically identical. Core chemistry and processes are unchanged. Earlier notes remain an exact prefix, and 57 protected pre-existing files retain bytes and modes, including both raw records, the publication, old histories and old audit receipts.

The prior 180-path closeout seal remains unchanged as a historical receipt. Exactly three of its covered files have authorized successor hashes: ProA review, notes and rendered HTML. The other 177 remain identical. The preservation proof records both old and new hashes rather than rewriting any prior manifest.

Focused `just validate BACSU proA`, generated-history validation and rendering passed. The record-section helper reported zero changes. No full-corpus validation, commit or push was performed. The new history uses actor codex, model gpt-6 and links PR6160. The stage manifest lists only the four gene/history products and additive follow-up artifacts; root owns project metadata, publication and PR response.
'''
(OUT/'report.md').write_text(report)
extra=[OUT/'stage-paths.json',OUT/'stage-path-hashes.json',OUT/'handoff.json']
paths=sorted(set([str(REVIEW),str(NOTES),str(HTML),str(HISTORY)]+[str(p) for p in OUT.iterdir() if p.is_file()]+[str(p) for p in extra]))
dump('stage-paths.json',paths)
dump('handoff.json',{'status':'SEALED_READY_FOR_ROOT_INTEGRATION','report':str(OUT/'report.md'),'preservation_proof':str(OUT/'preservation-proof.json'),'stage_paths':str(OUT/'stage-paths.json'),'stage_path_hashes':str(OUT/'stage-path-hashes.json'),'path_count':len(paths),'checks':'4/4 PASS','rows':7,'new_rows':0,'protected_inputs_unchanged':len(protected),'prior_closeout_unchanged_entries':len(unchanged),'explicit_overrides':superseded,'history':str(HISTORY),'no_further_owned_writes':True,'limits':'No full corpus run. Root handles project metadata, commit/push and PR response.'})
hashes={p:sha(p) for p in paths if p!=str(OUT/'stage-path-hashes.json')};dump('stage-path-hashes.json',hashes)
print(json.dumps({'status':'PASS','path_count':len(paths),'protected_inputs':len(protected),'prior_manifest_unchanged':len(unchanged),'successor_overrides':len(superseded),'handoff_sha256':sha(OUT/'handoff.json'),'seal_sha256':sha(OUT/'stage-path-hashes.json')},indent=2))
