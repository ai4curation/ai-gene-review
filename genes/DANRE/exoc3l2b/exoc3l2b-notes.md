# exoc3l2b notes

## Setup and provenance

- Fetched with `just fetch-gene` on A0A8M9Q5H9 (TrEMBL, RefSeq XP_021328615.1, "Exocyst complex
  component 3-like protein 2 isoform X1", 917 aa); 2 GOA rows (both IEA from InterPro), none with
  a PMID. The PANTHER TGD table lists a different accession for this gene (A0A8M3B147). UniProt
  reports that accession as inactive ("Deleted from sequence source (RefSeq)", checked 2026-09-28),
  and QuickGO returns no annotations for it. This is why the current entry has none of the IBA rows
  that exoc3l2a carries: an accession artefact, not a biological difference. ZFIN ZDB-GENE-100728-5, Ensembl ENSDARG00000030782, chromosome 15.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid, so no `-deep-research-*.md` file exists. Literature searched by hand via Europe PMC
  (see exoc3l2a notes for the queries). `exoc3l2b` itself returns no paper.
- DANRE_DUPLICATION random sample, draw 4 (seed 20260928); paralog exoc3l2a.

## Orthology

Same as exoc3l2a (see `genes/DANRE/exoc3l2a/exoc3l2a-notes.md` and
file:DANRE/exoc3l2a/exoc3l2a-bioinformatics/RESULTS.md): 35.9% identical to human EXOC3L2 and
20.6-21.9% to EXOC3, EXOC3L1, EXOC3L4 and TNFAIP2. Ensembl Compara: human EXOC3L2 ortholog
(one-to-many), one gar ortholog shared with exoc3l2a, one-to-one medaka ortholog; paralog
duplication node Osteoglossocephalai. The PANTHER table's EXOC3L4 call is not supported by sequence.

## Zebrafish literature

- ZFIN curates four wild-type expression rows for exoc3l2b, all from one paper (ZDB-PUB-100518-8
  = PMID:20463035, Piloto and Schilling 2010): neural crest at 5-9 somites (in situ), dorsal
  hindbrain and pharyngeal arches from prim-5 to protruding-mouth (in situ), whole embryo (RT-PCR).
  The paper calls the gene "sec6"; the assignment to exoc3l2b is ZFIN's curation (the probe
  sequence is in the paper's supplementary primer table, which I have not seen).
  [PMID:20463035 "Surprisingly, we found that rab3c, rab12, rab11fip2 and sec6 were all highly enriched in premigratory NC cells at 12 hpf, the same stage at which we performed the microarray and first detected the Ovo1 morphant phenotype ( Fig. 5B-E )."]
  [PMID:20463035 "At earlier stages, expression of all four genes was ubiquitous throughout the embryo but later became enriched in the NC at 12 hpf and in the dorsal hindbrain and pharyngeal arches at 24-72 hpf (data not shown)."]
  "sec6" was up-regulated in Ovo1 morphants (microarray, qPCR) and after dnTcf3 induction:
  [PMID:20463035 "Interestingly, we also found significant upregulation of rab3c, rab11fip2 and sec6 in embryos overexpressing the dnTcf3 transgene when compared with wild-type controls ( Fig. 5F )."]
  Overexpression phenocopy was shown for rab11fip2, not for sec6.
- No mutant, morphant or protein-level study of exoc3l2b.

## Mammalian EXOC3L2

See exoc3l2a notes (PMID:21566143, PMID:36362885, PMID:30327448, PMID:30086153). Of note for the
pair: mouse Exoc3l2 is expressed both in endothelium and in probable cranial neural crest
[PMID:36362885 "GFP expression was also observed in non-endothelial cells, which are most likely cranial neural crest cells (Figure 1c)."].

## Own analyses

Shared pair analysis in `genes/DANRE/exoc3l2a/exoc3l2a-bioinformatics/` (RESULTS.md). exoc3l2b is
the slower-evolving copy (71 lineage-specific changes vs 138 for exoc3l2a against gar), and is
closer to gar (56.2% vs 47.5%). Whole-embryo time course similar to exoc3l2a (both rise from
segmentation to 8-13 TPM at 3-5 dpf). Bgee adult calls broadly overlap exoc3l2a (intestine,
gill, kidney, heart, liver, skin, bone, muscle, granulocytes).

## Annotation decisions

- exocyst (IEA): accepted, as for exoc3l2a.
- exocytosis (IEA): kept as non-core, as for exoc3l2a.
- No NEW rows: the neural-crest in situ data are expression, not function; the Ovo1 paper did not
  test sec6/exoc3l2b function.
