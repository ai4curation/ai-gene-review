# HSPA4 (horse, F6YZJ4) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: F6YZJ4, the full-length (840 aa) product of the Ensembl canonical transcript
ENSECAT00000023133 of horse HSPA4 (gene ENSECAG00000020813). It is the canonical
counterpart of the benchmark entry A0A9L0S5Z5 (exon-skipped 800-aa model, reviewed in
`genes/HORSE/HSPA4/`). Folder named `HSPA4__F6YZJ4` because both accessions share the
HSPA4 symbol. ProtNLM2 output was not consulted.

### Data and tooling
- `just fetch-gene HORSE F6YZJ4 --alias HSPA4__F6YZJ4`: 12 GOA rows (4 IBA, 8 IEA), no experimental rows.
- Deep research FAILED: falcon returned `403 Forbidden` at Edison auth
  (`api.platform.edisonscientific.com/auth/login`), and the perplexity-lite fallback also
  failed. Review proceeded from cached literature and the human HSPA4 review.
- PubMed search for HSPA4/Apg-2/Hsp70-4/HSPH2 with horse/equine/Equus (2026-10-20) found one
  paper, PMID:40949872 (blood transcriptome pre/post racing): HSPA4 among upregulated heat-shock
  hub genes [PMID:40949872 "enabling the identification of the top 10 core genes: HSP90AA1, HSPA4, HSP90AB1, STIP1, KDM6B, HSPA4L, HSPA8, PTGES3, HSPD1, and TCP1"].
  Expression only; no horse functional data exist.

### Evolutionary grounding
- PANTHER PTHR45639:SF6 (HSPA4 orthologs), same subfamily as human P34932
  [file:HORSE/HSPA4__F6YZJ4/HSPA4__F6YZJ4-uniprot.txt "DR   PANTHER; PTHR45639:SF6; HEAT SHOCK 70 KDA PROTEIN 4; 1."].
- Full length, 96.9% identical to human, no human segment missing
  [file:HORSE/HSPA4/HSPA4-bioinformatics/RESULTS-rereview.md "| F6YZJ4 | 840 | 840 | 0.969 | [] |"].
- PAINT nodes: PTN002900795 (Hsp110, GO:0000774); PTN000452854 (Hsp110, cytosol, nucleus,
  protein folding; seeds include P34932 itself). GO:0016887 ATP hydrolysis and GO:0042026
  protein refolding sit only at the conventional Hsp70 node PTN000452648, not at the Hsp110
  nodes: treated as a deliberate curator omission.

### Decisions (consistent with genes/human/HSPA4 review)
- ACCEPT: GO:0000774 (IBA, core MF), GO:0005829 cytosol (IBA; IEA from human IDA PMID:21231916), GO:0006457 protein folding (IBA).
- KEEP_AS_NON_CORE: ATP binding (enables NEF activity), nucleus (IBA), extracellular exosome (Compara IEA from human proteomics).
- MODIFY: cytoplasm -> cytosol; organelle (ARBA) -> nucleus.
- MARK_AS_OVER_ANNOTATED: ATP hydrolysis activity (InterPro2GO; Hsp110 function relies on exchange, not ATPase; PMID:22990239).
- UNDECIDED: protein import into mitochondrial matrix and chaperone-mediated protein complex assembly
  (Compara IEA from human IDAs on PMID:15644312, abstract does not mention HSPA4, full text unavailable;
  human review also UNDECIDED).
- No NEW terms. Hsp70 protein binding (GO:0030544, IPI in human) is implied by NEF activity and was not added.

Nothing in this review is experimentally established in horse; every function is a
transfer from the Hsp110 clade / human Apg2 via PANTHER SF6 and PAINT.
