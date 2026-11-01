# DTD1 re-review: gene-model analysis of A0A2R8YCT7 vs Q8TEA8

- A0A2R8YCT7 length: 127 aa
- Q8TEA8 length: 209 aa
- Identical N-terminal prefix: residues 1-124
- A0A2R8YCT7 tail after divergence: TLF (residues 125-127)
- Q8TEA8 sequence after divergence: GKFGAYMQVHIQNDGPVTIELESPAPGTATSDPKQLSKLEKQQQRKEKTRAKGPSESSKERNTPRKEDRSASSGAEGDVSSEREP (residues 125-209)
- Canonical residues absent from A0A2R8YCT7: 85 of 209

## Canonical features vs divergence point

| Feature | Q8TEA8 interval | Retained in A0A2R8YCT7 |
|---|---|---|
| Mg(2+) binding (ECO:0000269 PubMed:17264083) | 4-4 | yes (identical prefix) |
| Mg(2+) binding (ECO:0000269 PubMed:17264083) | 6-6 | yes (identical prefix) |
| Mg(2+) binding (ECO:0000269 PubMed:17264083) | 28-28 | yes (identical prefix) |
| Beta strand 131-146 (PDB:2OKV) | 131-146 | no (after divergence) |
| Gly-cisPro motif (ECO:0000250 Q8IIS0) | 139-140 | no (after divergence) |
| Disordered C-terminal region (MobiDB-lite) | 142-209 | no (after divergence) |
| Phosphoserine 197 | 197-197 | no (after divergence) |

## Transcript models (Ensembl GRCh38)

### ENST00000377452 (protein_coding, Ensembl canonical=True)

Translation ENSP00000366672 length 209, CDS end 18744252

| Exon | Start | End | Length (nt) |
|---|---|---|---|
| ENSE00001473997 | 18588054 | 18588115 | 62 |
| ENSE00003658417 | 18593731 | 18593821 | 91 |
| ENSE00003504307 | 18596006 | 18596241 | 236 |
| ENSE00003826816 | 18628127 | 18628233 | 107 |
| ENSE00001162838 | 18744100 | 18744271 | 172 |
| ENSE00003899205 | 18763360 | 18766644 | 3285 |

### ENST00000647441 (nonsense_mediated_decay, Ensembl canonical=False)

Translation ENSP00000493969 length 127, CDS end 18620080

| Exon | Start | End | Length (nt) |
|---|---|---|---|
| ENSE00003814832 | 18587942 | 18588115 | 174 |
| ENSE00003658417 | 18593731 | 18593821 | 91 |
| ENSE00003504307 | 18596006 | 18596241 | 236 |
| ENSE00003820992 | 18620067 | 18620113 | 47 |
| ENSE00003691719 | 18628127 | 18628233 | 107 |
| ENSE00003825048 | 18744100 | 18744271 | 172 |
| ENSE00003899205 | 18763360 | 18766644 | 3285 |

## Exons of the target model that do not overlap any canonical exon

- ENSE00003820992 18620067-18620113 (47 nt; length mod 3 = 2)

(Canonical exon end coordinates checked: 6)
