# BCAT2: paired evidence notes

Human reference: https://www.uniprot.org/uniprotkb/O15382/entry

Primary source: [PMID:17050531 Human mitochondrial branched chain aminotransferase isozyme: structural role of the CXXC center in catalysis.](https://pubmed.ncbi.nlm.nih.gov/17050531/).

> Mammalian branched chain aminotransferases (BCATs) have a unique CXXC center.
> Kinetic and structural studies of three CXXC center mutants (C315A, C318A, and
> C315A/C318A) of human mitochondrial (hBCATm) isozyme and the oxidized hBCATm
> enzyme (hBCATm-Ox) have been used to elucidate the role of this center in hBCATm
> catalysis. X-ray crystallography revealed that the CXXC motif, through its
> network of hydrogen bonds, plays a crucial role in orienting the substrate
> optimally for catalysis. In all structures, there were changes in the structure
> of the beta-turn preceding the CXXC motif when compared with wild type protein.

The horse sequence comparison is in [BCAT2-bioinformatics/RESULTS.md](BCAT2-bioinformatics/RESULTS.md). Transfer is assessed for this exact accession; human biochemical evidence is not equine experimental validation.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Deep research: `just deep-research HORSE BCAT2 --provider falcon` failed ("Exception: Failed to authenticate", all providers failed). Proceeded with cached literature (PMID:9165094, PMID:17050531, PMID:11264579), the human BCAT2 Swiss-Prot record and the PTHR11825 PAINT data.

### Identity of the benchmark accession (gene-model issue)

A0A9L0TSN4 (452 aa, Ensembl ENSECAP00000090181) is one of several horse BCAT2 gene models (gene ENSECAG00000011310). New analysis: `BCAT2-bioinformatics/compare_models_rereview.py` -> `RESULTS-rereview.md`.

- Residues 60-452 (393 aa) begin at the Met aligned to human Met1 and span the full mammalian enzyme (human O15382 392 aa; mouse/rat/cow 393 aa), including the region of the 27-residue mitochondrial presequence [PMID:9165094 "encode mature proteins of 41.2 and 41.3 kDa with presequences of 27 amino acids"].
- Residues 1-59 are an extra Gly/Arg/Pro-rich, MobiDB-disordered segment (Gly 15, Arg 7, Pro 8) found in no reviewed mammalian ortholog; shared only with other horse models (A0A3Q2HXS7 and several Ensembl translations). Most likely an upstream in-frame start in the GC-rich 5' region, i.e. a gene-model extension, not a functional domain. It places the presequence internally, so import of this exact product is untested.
- All catalytic residues retained: PLP Schiff-base Lys (human K229), CXXC (human C342/C345 = mature C315/C318 of PMID:17050531), curated substrate contacts.
- No catalytic residues or domains missing. No horse model is identical to the Met60-initiated body; F7B9V7 (405 aa) starts at the conserved Met but has an alternative C-terminal exon; Ensembl canonical (ENSECAP00000057595, 480 aa) carries the same extension plus a 28-residue Pro-rich insertion. No Swiss-Prot horse BCAT2 exists, so there is no canonical horse product to designate.

### Evolutionary grounding

- PANTHER PTHR11825:SF39 (mitochondrial BCAT), same subfamily as human O15382, mouse O35855, rat O35854.
- PAINT (interpro/panther/PTHR11825/PTHR11825-paint.tsv): PTN000214535 carries GO:0052654/0052655/0052656 (L-Leu/L-Val/L-Ile transaminase, is_a GO:0004084) and GO:0006550/GO:0006574 (Ile, Val catabolism); PTN000214536 (Eukaryota) carries mitochondrion. Not propagated: leucine catabolic process, matrix, adipocyte/PRDM16 roles; I did not add those.

### Decisions

- GO:0003824 MODIFY -> GO:0004084; GO:0009081 MODIFY -> GO:0009083 (correct but general).
- GO:0004084, GO:0009083 ACCEPT.
- GO:0005739 changed UNDECIDED -> ACCEPT: the gene-level location has strong phylogenetic support. The gene-model caveat is recorded as a suggested question/experiment.
- NEW GO:0030170 pyridoxal phosphate binding (structural evidence PMID:11264579 on ortholog; lysine conserved).
- Did not transfer the by-similarity adipocyte/PRDM16 or keto-acid transporter statements in the UniProt FUNCTION text.

### Relative and family

- Relative: human BCAT2 O15382 (ortholog, same SF39); complete review at genes/human/BCAT2/BCAT2-ai-review.yaml.
- Family review interpro/panther/PTHR11825/PTHR11825-review.yaml: agrees on SF39 placement; its SF39 description reuses family-level text ("comprises branched-chain aminotransferase, BCAT1 and BCAT2 groups"), but BCAT1 is in SF70 (cytosolic), so that wording is loose for the subfamily.
- Modules: modules/branched_chain_amino_acid_catabolism.yaml (BCAT2 transamination step); also mention BCAT in modules/valine_isoleucine_distal_catabolism.yaml, modules/branched_chain_amino_acid_biosynthesis.yaml, modules/ehrlich_pathway.yaml.
