from check_identity import compare, uniprot_sequence
assert uniprot_sequence('SQ   SEQUENCE 4 AA;\n     ACD E 4\n//') == 'ACDE'
assert compare('ACDE','HHACDEGG')['suffix']=='GG'
assert compare('ACDE','ACDF')['exact_full_target_match'] is False
assert compare('ACDE','ACDE')['query_start_1based']==1
print('Four independent positive/negative/parser checks passed.')
