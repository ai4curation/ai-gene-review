# RFC3 (P38629, YNL290W) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: RFC3 is the closest experimentally characterised relative of the ProtNLM2 benchmark gene
SCHPO/rfc3 (O14003). This review was done without consulting any ProtNLM2 output.

### Deep research

`just deep-research-falcon yeast RFC3 --fallback perplexity-lite` failed: falcon returned
"Failed to authenticate" and the perplexity-lite fallback returned HTTP 401 (insufficient quota).
No deep-research file was produced. The review is based on the cached publications (21 GOA-cited
papers plus PMID:14530260, PMID:15964801, PMID:15201901 fetched for this review) and the UniProt record.

### Evolutionary grounding

- PANTHER: PTHR11669 (RFC / DNA pol III gamma-tau), subfamily PTHR11669:SF9, whose official name is
  "REPLICATION FACTOR C SUBUNIT 5". The pombe benchmark protein rfc3 (O14003) is in the same subfamily
  (family review interpro/panther/PTHR11669/PTHR11669-review.yaml), so S. cerevisiae RFC3 and
  S. pombe rfc3 are orthologs. PANTHER subfamily numbering does not follow yeast gene numbering.
- PAINT nodes: PTN000186209 (RFC small subunits: clamp loader activity, RFC complex, DNA repair),
  PTN000186208 (DNA-templated DNA replication; deeper node including bacterial donors),
  PTN000912313 (Rad17/Ctf18/Elg1 RFC-like complexes; yeast RFC3 SGD:S000005234 is a donor),
  PTN001705380 (nucleus). RFC3 is a donor for several of these; this is expected, not circular.
- DNA clamp unloader activity (GO:0061860): QuickGO shows yeast annotations only on the complex
  (CPX-422, IDA PMID:23499004); IBA rows sit on the large subunits (human RFC1, ATAD5). PomBase gives
  the S. pombe small subunits including rfc3 an IC annotation (PMID:16040599). PAINT did not propagate
  this to the small-subunit node; I treat that as deliberate and did not add a NEW row. It is raised as
  a suggested question.

### Experimentally established in S. cerevisiae (with Rfc3 itself, or its complexes)

- Essential gene; purified Rfc3p alone has ssDNA-stimulated ATPase
  [PMID:8302859 "Purified Rfc3p has an ATPase activity that is markedly stimulated by single-stranded DNA but not by double-stranded DNA or RNA."]
- Rfc3 supplies the arginine finger for the Rfc4 ATP site; strong PCNA contact
  [PMID:14530260 "we use this activity to determine that RFC3 supplies a catalytic arginine to the ATP site of RFC4"]
- Subunit of RFC [PMID:7651383], Rad24-RFC [PMID:10660302 "The 40 kDa species was found by mass spectrometry to contain Rfc2 and Rfc3"],
  Ctf18-RFC [PMID:11389843], Elg1-RFC [PMID:12912927; cryo-EM PMID:38427736].
- Rad24-RFC loads the 9-1-1 checkpoint clamp [PMID:12604797 "the RFC-Rad24 clamp loader loads the Rad17/3/1 clamp around partial duplex DNA in an ATP-dependent process"].
- Ctf18-RFC unloads PCNA [PMID:15964801].

### Complex-level / inferred (not dissected for Rfc3)

- Sister chromatid cohesion: rfc4-ts and rfc5-1 alleles show precocious separation; no rfc3 allele
  tested in the cited papers. Kept as non-core.
- Mismatch repair / DNA repair: via general PCNA loading; review-level (TAS) and IBA. Kept as non-core.
- Leading strand elongation (IDA PMID:1346062) designation is "by analogy" with SV40; RFC acts on both
  strands. Kept as non-core; general strand elongation is core.

### Decisions summary

- All 15 GO:0005515 protein binding IPI rows REMOVE (complex membership is captured by CC terms).
- Cytosol (hypoxia relocalization study) KEEP_AS_NON_CORE.
- All complex, clamp loader, ATPase, ATP binding, replication and nucleus rows ACCEPT.
