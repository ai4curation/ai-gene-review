# magi3b (LOC564220) / wu:fi36a10 (magi3a): bioinformatics results

All numbers below come from the scripts in this folder. Each script's output is saved next to it
(`*_output.md`). Run the scripts from the repository root with `uv run python <script>`.
They query UniProt, Ensembl, Bgee and ZFIN live, so reruns against later releases may differ.

| script | output | question |
|---|---|---|
| `protein_compare.py` | `protein_compare_output.md` | identity, per-domain conservation, P-loop |
| `primer_map.py` | `primer_map_output.md` | which gene each name in PMID:35649360 refers to |
| `expression.py` | `expression_output.md` | Bgee and ZFIN expression calls, with gar magi3 |
| `synteny.py` | `synteny_output.md` | double-conserved synteny with gar; Ensembl Compara view of the pair |

## 1. Gene identity and names

The magi3a primers of PMID:35649360 match wu:fi36a10 with 0 mismatches (7-8 mismatches in magi3b), and
the magi3b primers match magi3b (LOC564220) with 0 mismatches (2 and 5 mismatches in wu:fi36a10).
The paper's "magi3a" is therefore ZFIN wu:fi36a10 (NCBI magi3a, GeneID 561689), and its "magi3b" is
ZFIN magi3b (NCBI GeneID 564220, the PANTHER label LOC564220).

## 2. Protein comparison

- LOC564220 (magi3b) is 58.2% identical to wu:fi36a10 over the full length (BLOSUM62 global alignment).
- wu:fi36a10 is closer than magi3b to both gar magi3 (63.5% vs 55.1%) and human MAGI3 (54.5% vs 50.4%).
  The same holds for each medaka co-ortholog, which is closest to its PANTHER-assigned zebrafish partner
  (62.5% and 63.1%).
- All six PDZ domains, both WW domains and the GK-like domain are present in both copies. Identity to
  human MAGI3 per domain is 69-96% for wu:fi36a10 and 69-88% for magi3b. wu:fi36a10 is equal or higher
  in every domain. Between the two zebrafish copies, domain identity is 79-96%. The C-terminal
  disordered tail (human 1104-1481) is poorly conserved in all fish proteins (20-23%).
- Neither zebrafish copy, nor gar or human MAGI3, has a Walker A (P-loop) motif at the position UniProt
  annotates as the ATP-binding site (human MAGI3 121-128 FQKGSIDH; magi3b FQKGSIDH; wu:fi36a10 and gar
  FQKGSLDH). This fits the published view that MAGI GK domains are non-catalytic protein-binding
  modules (PMID:37163606). The UniRule kinase, ATP-binding and nucleotide-binding annotations
  are therefore unsupported.
- The gar protein (W5MYP7) is N-terminally truncated in UniProt. Its PDZ 1 value (3.4%) is a gene-model
  artefact.

## 3. Expression

- Bgee RNA-Seq: wu:fi36a10 has Bgee RNA-Seq expression calls in 22 anatomical entities, magi3b in 9.
  Highest for wu:fi36a10: pharyngeal gill, blastula, skin, early embryo, ovary, intestine. Highest for
  magi3b: retina (score 78.6), blastula, ovary, early embryo, brain.
- Overlap: every magi3b RNA-Seq call is shared with wu:fi36a10. The 13 entities with a call for
  wu:fi36a10 only include heart, intestine, liver, muscle, mesonephros, head kidney, spleen, testis and
  skin.
- Gar magi3 (single copy) has calls in eye, ovary, heart, embryo, brain, testis, skin, mesonephros,
  bone, intestine, liver, gill and muscle. That is a broad pattern resembling wu:fi36a10.
- Caveats: Bgee reports only present calls. A missing call is not evidence of absence, and
  magi3b may be expressed at lower levels in those tissues. The two zebrafish genes were measured in the
  same RNA-Seq libraries, so the comparison between them is fair. The comparison with gar is qualitative.
- ZFIN curated wild-type expression: one RT-PCR record for magi3b (whole organism), none for
  wu:fi36a10.

## 4. Origin of the pair (synteny and gene trees)

`synteny.py`: windows of +/- 1.5 Mb; zebrafish-gar orthology from PANTHER v19; positions from Ensembl
(GRCz11, LepOcu1).

- The gar magi3 window (LG3) holds 62 protein-coding genes.
- The wu:fi36a10 window (chr 23; 78 genes, 56 with a PANTHER gar ortholog) shares two genes with it:
  ptpn22 and RSBN1. These are also MAGI3 neighbours in human.
- The magi3b window (chr 6; 48 genes, 30 with a PANTHER gar ortholog) shares none.
- No gar-window gene has orthologs in both zebrafish windows. There is no double-conserved synteny.
- wu:fi36a10 therefore sits in the region that kept the ancestral MAGI3 neighbourhood. The magi3b region
  is not recognizably its duplicate at this window size. This does not exclude a TGD origin, since
  duplicated blocks often lose most of their second-copy genes or are rearranged, but synteny does not
  confirm it.
- Ensembl Compara classes the pair as within-species paralogs with the duplication at Euteleostomi,
  not at the teleost root. PANTHER places it on Neopterygii|Teleostei with a single shared gar
  co-ortholog. The two gene trees disagree on timing. PANTHER's placement is the one consistent with a
  single gar magi3 gene.
- Mapping note: PANTHER's identifier for wu:fi36a10 (ZFIN ZDB-GENE-030131-6139) has no Ensembl
  cross-reference in ZFIN's ensembl_1_to_1 file, so the script could not attach the gar ortholog to the
  focal gene itself (the "PANTHER gar orthologs ... none" line). panther_tgd_pairs.tsv records gar
  magi3 as its co-ortholog.

## Interpretation (limits)

The two copies keep the same domain set and neither has an obvious loss of function. magi3b is the
more divergent copy in sequence and has the narrower public expression profile. This asymmetry is
consistent with, but does not demonstrate, a degenerating or partitioned magi3b. No quantitative,
tissue-matched comparison (for example in endothelium, where both are detected by qRT-PCR) exists.
