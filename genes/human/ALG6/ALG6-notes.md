# ALG6 (human) curation notes

UniProtKB:Q9Y672 — Dolichyl pyrophosphate Man9GlcNAc2 alpha-1,3-glucosyltransferase; EC 2.4.1.267.
HGNC:23157. 507 aa multi-pass ER membrane protein (UniProt lists 10 TM helices).

> Note: falcon deep research was unavailable (API out of credits, HTTP 402). This review is
> grounded in the UniProt record (`ALG6-uniprot.txt`), the seeded GOA (`ALG6-goa.tsv`), and the
> cached publications under `publications/`. No `-deep-research-falcon.md` was fabricated.

## Core biology

ALG6 is the ER-lumenal alpha-1,3-glucosyltransferase that adds the **first of three glucoses**
to the dolichol-linked oligosaccharide (LLO). It transfers glucose from dolichyl-phosphate-glucose
(Dol-P-Glc; **not** UDP-Glc) onto Man9GlcNAc2-PP-dolichol to give Glc1Man9GlcNAc2-PP-dolichol,
the substrate for the next enzyme ALG8.

- UniProt FUNCTION: "In the lumen of the endoplasmic reticulum, adds the first glucose residue from
  dolichyl phosphate glucose (Dol-P-Glc) onto the lipid-linked oligosaccharide intermediate
  Man(9)GlcNAc(2)-PP-Dol to produce Glc(1)Man(9)GlcNAc(2)-PP-Dol. Glc(1)Man(9)GlcNAc(2)-PP-Dol is a
  substrate for ALG8, the following enzyme in the biosynthetic pathway."
  [ECO:0000269|PubMed:10359825, ECO:0000269|PubMed:25792706]
- CATALYTIC ACTIVITY: RHEA:30635, EC=2.4.1.267; donor = di-trans,poly-cis-dolichyl beta-D-glucosyl
  phosphate (Dol-P-Glc).
- SUBCELLULAR LOCATION: Endoplasmic reticulum membrane; Multi-pass membrane protein.
- Belongs to the ALG6/ALG8 glucosyltransferase family (CAZy GT57; Pfam PF03155 Alg6_Alg8;
  InterPro IPR004856).

Glucosylation of the LLO is required for **efficient transfer** of the glycan to nascent protein by
the oligosaccharyltransferase (OST). Loss of ALG6 causes accumulation of Man9GlcNAc2-PP-Dol and
protein hypoglycosylation.

## Disease

ALG6 deficiency causes **ALG6-CDG / congenital disorder of glycosylation type Ic (CDG1C; MIM:603147)**,
one of the most common CDG-I subtypes. Recessive; many missense/deletion/splice variants (e.g. A333V —
the most common; S478P; delI299; exon-3 skipping). F304S is a common mild/polymorphic allele that can
exacerbate other CDGs. [UniProt DISEASE; PMID:10359825, PMID:10924277, PMID:10914684, etc.]

## Key references (cached; all abstract-only except PMID:33961781)

- **PMID:10359825** (Imbach 1999, PNAS): cloned human ALG6 as ortholog of yeast ALG6 "dolichyl
  pyrophosphate Man9GlcNAc2 alpha1,3-glucosyltransferase"; mutant human ALG6 fails to complement yeast
  alg6 hypoglycosylation; defines CDGS type-Ic. Origin of MF (IDA/IGI/IC), BP, N-glycosylation, and
  lumenal-side localization annotations.
- **PMID:10924277** (Westphal 2000, Mol Genet Metab): "This enzyme is required for the addition of the
  first glucose residue to the lipid-linked oligosaccharide precursor for N-linked glycosylation."
  IDA acts_upstream_of_or_within N-glycosylation.
- **PMID:25792706** (Shrimal & Gilmore 2015, Glycobiology): ALG6-deficient cells assemble
  Dol-PP-GlcNAc2Man9 as largest donor; hypoglycosylation of OST sites. IMP for MF/BP/N-glyc.
- **PMID:19946888** (Ghosh 2010): NK-cell membrane proteome MS; supports membrane localization (HDA).
- **PMID:33961781** (Huttlin 2021, BioPlex): interactome AP-MS; ALG6–ALG8 (Q9BVK2) interaction (bare
  protein-binding IPI). UniProt INTERACTION record: "Q9Y672; Q9BVK2: ALG8; NbExp=2".

## Annotation decisions (summary)

- MF **GO:0042281** dolichyl pyrophosphate Man9GlcNAc2 alpha-1,3-glucosyltransferase activity — the
  exact GOA/EC 2.4.1.267 term. ACCEPT (IBA, IMP, IEA). Core MF.
- MF **GO:0004583** dolichyl-phosphate-glucose-glycolipid alpha-glucosyltransferase activity (Reactome
  TAS) — the parent/donor-focused MF; correct chemistry (Dol-P-Glc donor) but less precise than
  GO:0042281 → MODIFY to GO:0042281.
- MF **GO:0016758** hexosyltransferase activity (IEA InterPro) — correct but general grouping → MODIFY
  to GO:0042281 (or KEEP; chose MODIFY, over-general).
- MF **GO:0046527** glucosyltransferase activity (IDA) — correct but general parent → MODIFY to
  GO:0042281.
- MF **GO:0005515** protein binding (IPI, ALG8) — bare protein binding, uninformative → MARK_AS_OVER_ANNOTATED.
- BP **GO:0006488** dolichol-linked oligosaccharide biosynthetic process — core BP. ACCEPT.
- BP **GO:0006487** protein N-linked glycosylation — downstream process ALG6 is required for. ACCEPT.
- CC **GO:0005789** endoplasmic reticulum membrane — correct localization. ACCEPT.
- CC **GO:0098553** lumenal side of ER membrane (IC) — active-site topology; correct. ACCEPT.
- CC **GO:0016020** membrane (HDA proteomics) — correct but general → MODIFY to GO:0005789.
</content>
</invoke>


## 2026-09-27 full source audit (supersedes the earlier decision summary)

This is a complete re-review of the 22 existing annotations, not a new gene seed. The five canonical files matched both imported main `d35dcc30b44924f79c0510b281ae824aa536848a` and live main `30a9290881824baaacab2b681d7808f572c4cef6`; the fresh canonical open-PR search returned zero. The HGNC inventory confirms approved **ALG6 / HGNC:23157**, with no previous symbols or aliases. UniProt Q9Y672 is human ALG6; My046 is its recorded ORF name. All original annotation fields, qualifiers, reference identities and raw files are preserved. There are **17 ACCEPT, 4 MODIFY and 1 REMOVE**, one integrated catalytic core and **zero NEW rows**. No new biological-process term is introduced into the core.

### Evidence access and research provenance

The required default Falcon launch with `--fallback perplexity-lite --timeout 1200` ran concurrently with `just fetch-gene-pmids human ALG6`. Both providers failed while obtaining the normal deep-research-client dependency because PyPI DNS resolution failed. The provider itself did not generate a report. The earlier notes' HTTP 402 observation describes an older attempt, not this run. Logs: `/tmp/ALG6-provider-attempt.log` (exit 1) and `/tmp/ALG6-seeded-fetch.log` (5/5 already cached, exit 0). No provider output was authored or substituted.

The authored citation census comprises the five original PMIDs plus **PMID:10914684** (already cited above) and **PMID:32103179** (new mechanistic context), and three Reactome entries. Ordinary `fetch-pmid 10914684 32103179` reached terminal DNS failures, 0/2 records written; see `/tmp/ALG6-new-sources-fetch.log`. These two real missing-cache requirements keep the review DRAFT. Their identifiers and content were independently checked on primary pages; cache absence is not an incorrect-identifier judgment. No optional unused bibliography in the immutable UniProt record was promoted to supporting evidence. There is no provider report whose citations require a separate expansion.

Current local access differs from the historical summary: PMID:10359825 contains the full original Methods/Results/Figure 5 and was read; PMID:33961781 has true full-text metadata but only Introduction/Discussion extracted, so its flag remains false for `full_text_unavailable` and extraction limits are explicit. PMID:10924277, PMID:19946888 and PMID:25792706 have abstract-only local caches. External recovery of the last source does not change that cache flag.

### Original experiments and source-specific decisions

- **PMID:10359825**, [original PMC22030](https://pmc.ncbi.nlm.nih.gov/articles/PMC22030/) and [PubMed identity](https://pubmed.ncbi.nlm.nih.gov/10359825/): cached original Methods and Figure 5 use human ALG6 cDNA expressed in yeast `alg6` and `alg6/wbp1-2` strains. Human wild type improves CPY glycosylation and growth. A333V fails the CPY rescue but retains partial growth rescue, so it is not described as universally inactive. The IGI WITH accession **Q12001 is yeast ALG6, not ALG8**; this is a correction of the prior prose, not a change to the trusted source row. The identity is independently explicit in the original 2020 structure paper's Methods and the [CAZy GT57 characterized entries](https://www.cazy.org/GT57_characterized.html). Human sequence hydrophobicity and pathway location underpin the original membrane inference; the 1999 paper is not a direct topology imaging assay.
- **PMID:25792706**, [original PMC4453865](https://pmc.ncbi.nlm.nih.gov/articles/PMC4453865/): the external indexed original Results, Figure 5 and Methods were recovered with the query `"PMC4453865" "ALG6" "Methods"`. The experiment distinguishes human patient fibroblasts from hamster CHO/MI8-5 cells. Its Methods identify the rescue construct as human ALG6-V5H6; the mutated construct has A333V/S308R. These data support the retained cell-based MF/BP judgments, while the independent STT3B-expression defect limits attribution of the entire MI8-5 phenotype to ALG6. No purified-human-enzyme kinetics are claimed.
- **PMID:10924277**, [PubMed](https://pubmed.ncbi.nlm.nih.gov/10924277/): the accessible abstract describes human alleles tested in ALG6-deficient yeast. Exon-3 skipping fails rescue; the paternal allele restores glycosylation but has transcript/expression limitations. The retained curated N-glycosylation assertion is consistent with the established catalytic step. The ordinary relationship qualifier is preserved but is not used as a substitute for assessing function. Original full-body access was not established.
- **PMID:19946888**, [PubMed](https://pubmed.ncbi.nlm.nih.gov/19946888/): the YTS study isolates and analyzes membranes. The target peptide table was not independently recovered. The broad membrane HDA is **ACCEPT**, supported by independent ALG6 membrane evidence and deference to the source curator; it is not refined to ER membrane using an assay that lacked that resolution. No contamination, erroneous target identification, surface localization or new peptide result is inferred.
- **PMID:33961781**, [PubMed](https://pubmed.ncbi.nlm.nih.gov/33961781/): the study uses AP-MS in 293T and HCT116 cells. The immutable GOA and UniProt identify an ALG6-ALG8 association, but the pair-level supplement was not independently recovered. **REMOVE** applies to generic protein binding's lack of informative MF, not the truth of the reported interaction. No adaptor, stable complex or substrate-channeling term is substituted from co-purification alone.
- **PMID:10914684**, [verified PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/10914684/): additional human cases and yeast complementation support variant-associated LLO defects. The former notes' statement that this is one of the most common CDG forms is historically scoped to the study cohort and is omitted from the current standalone summary; no current prevalence estimate is asserted.
- **PMID:32103179**, [PubMed](https://pubmed.ncbi.nlm.nih.gov/32103179/) and [indexed original PMC8712213](https://pmc.ncbi.nlm.nih.gov/articles/PMC8712213/): the 2020 study already solved yeast ALG6 and reconstituted its activity using synthetic lipid-linked substrates. The Methods specify S. cerevisiae Q12001, expressed using the Sf9 procedure, despite a gene-design phrase about optimization for human expression. Species is defined by the protein construct, not the host or optimization target. The catalytic Asp69 is yeast numbering. The study informs conserved chemistry and revises the suggested experiments toward **human** enzyme/variant assays; it is not reported as an existing human structure. Indexed query: `"PMC8712213" "Expression and purification" "ALG6"` (the broader `"PMC8712213" "Methods" "Pichia"` query also returned the authentic Methods; Pichia is not asserted as the expression host).

### Ontology, PAINT and modeled role

Live [GO:0042281](https://amigo.geneontology.org/amigo/term/GO%3A0042281) defines the first-glucose transfer from Dol-P-Glc onto Man9GlcNAc2-PP-Dol and is a child of GO:0004583, through the glucosyltransferase/hexosyltransferase hierarchy. All four broad MF rows remain **MODIFY** to this specific activity, including the InterPro family mapping. That is a target-specific refinement of true parent assertions, not a claim that the entire ALG6/ALG8 family shares one acceptor. The exact MF and broad-to-specific links were retrieved through indexed AmiGO after direct page timeouts.

Live [GO:0006488](https://amigo.geneontology.org/amigo/term/GO%3A0006488) covers the reactions forming LLO and is part of protein N-linked glycosylation. ALG6 itself performs one of those chemical reactions; retained BP judgments therefore rest on direct participation, not necessity alone. The existing core retains both pathway scopes. Live [GO:0098553](https://amigo.geneontology.org/amigo/term/GO%3A0098553) covers the lumen-facing ER leaflet, including embedded or attached proteins. The core uses this already-seeded location; no broad membrane source annotation is overwritten with finer topology. The older note's count of ten predicted human transmembrane segments is not accurate for the current source file, which lists eleven; neither count is a directly measured human topology. The yeast structure's helix count is not projected onto the human record.

The local PTHR12413 PAINT table places ER membrane and LLO biosynthesis at **PTN000275691**, and the specific ALG6 activity at **PTN000275751**. The source blocks use those verified ancestral nodes only. Human ALG6 among descendant experimental supports is legitimate self-evidence. No phylogenetic failure or lineage loss was found. The local family entry independently places Q9Y672 in PTHR12413:SF1; no family identifier or label was guessed.

Cached GO-CAM **65c57c3400000687**, activity **65c57c3400001187**, already represents human ALG6 with GO:0042281, LLO biosynthesis and lumenal-side ER location; its evidence includes PMID:25792706 and the IC source PMID:10359825. This agrees with the reviewed catalytic role and creates no annotation gap. The model separately includes the next glucosyltransferases. No NEW process, folding role, transporter, oligomeric complex or other activity is proposed.

The official live Reactome pages [R-HSA-446193](https://reactome.org/content/detail/R-HSA-446193), [R-HSA-446202](https://reactome.org/content/detail/R-HSA-446202) and [R-HSA-4724291](https://reactome.org/content/detail/R-HSA-4724291) were checked against their caches. The normal event provides explicit human ALG6 catalyst and lipid donor/acceptor/product. The disease event distinguishes deficient variants and notes residual activity; it does not make the gene-level row a NOT assertion. The parent summary's erroneous terminal “GlcNAcs” wording is not adopted: the three terminal sugars are glucoses. All cache bytes remain intact.

### Integrity and validation

All 22 original source objects and all 13 original reference id/title pairs are preserved. Two verified references are added; no machine annotation or original evidence code is changed. The current reference assessments distinguish identity verification from full-text and supplement access. Quotes are checked against actual source text; historical notes above are retained as a dated record and the explicit corrections here govern the final judgments. Final targeted validation, history validation and render receipts are recorded in the accompanying manifest.

Final targeted validation exited 0 with one warning category consisting solely of the two missing caches (10914684 and 32103179); history validation and HTML rendering passed. Independent substring check verified 47 supporting quotes case-sensitively after whitespace normalization, with zero case-fold-only matches. Fresh final preflight at main `21364698b8b0c1099c7f26384bfd35b13596d282` found all five original ALG6 blobs unchanged and zero open ALG6 PRs.
