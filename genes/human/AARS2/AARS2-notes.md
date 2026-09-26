# AARS2 review notes

## Research provenance

- Automated deep research was attempted on 2026-08-08. `just deep-research-falcon human AARS2` failed with Edison HTTP 402, `just deep-research-perplexity human AARS2` failed with HTTP 401 insufficient quota, and `just deep-research-openai human AARS2` failed because model `o3-deep-research-2025-06-26` was unavailable (HTTP 404). No provider-named report was created; this review therefore uses cached primary publications directly.
- Live QuickGO returned 26 rows but 25 normalized review tuples. Two PMID:32296183 protein-binding rows collapse into one tuple, so both partners must remain in `supporting_entities`. The PMID:39322678 lactyltransferase row also carries `has_input` CGAS and `part_of` negative regulation of cGAS/STING signaling; the local 16-column GOA export does not encode that extension, so it was restored from the live record.

## Functional evidence map

- The canonical function is mitochondrial alanine charging. Purified human AARS2 is selective for its cognate mitochondrial alanine tRNA [PMID:32080176, "Hs mt AlaRS charges cognate mt tRNAAla but not mt tRNAs specific for Asp, Leu, or Ser."]. Human cybrid rescue independently increases charged mutant mt-tRNA(Ala) and mitochondrial translation [PMID:30262995, "AARS2 overexpression did not result in a detectable increase of the mutated mt-tRNAAla but caused an increase incharged mt-tRNAAla in mutant cybrids, leading to enhanced mitochondrial translation."].
- Proofreading is a second canonical activity. Recombinant mature human AARS2 directly performs post-transfer Ser-tRNA(Ala) editing [PMID:29228266, "Determination of post-transfer editing of mischarged Ser-tRNAAla showed that the C749A mutant was severely defective in editing while the initial velocity of the post-transfer editing activity of the V760E mutant was only slightly reduced"]. Human AARS2 also performs Gly-tRNA(Ala) editing; an editing-site mutant loses that hydrolysis [PMID:30952159, "Indeed, the result of the post-transfer editing assay showed that hmtAlaRS-R663E was unable to hydrolyze Gly-tRNAAla"]. These support direct IDA recommendations for the Ser- and Gly-specific child terms in addition to the true broad deacylase parent.
- The mature enzyme is monomeric, so no stable complex belongs in the core synthesis [PMID:30952159, "In the present study, we found that hmtAlaRS is a monomer"].
- ATP-dependent protein lactylation is experimentally supported but conditional. AARS2 lactylates PDHA1/CPT2 peptides in an ATP- and lactate-dependent reaction [PMID:38163844, "AARS2 lactylated the synthetic K336-containing PDHA1 peptide as well as the K457/8-containing CPT2 peptide (Fig. 5b; Supplementary information, Fig. S6b) via lactate- and ATP-dependent and pyrophosphate-inhibitable mechanisms."]. The cGAS work reports lactate-induced association, lactylation and inactivation [PMID:39322678, "In response to L-lactate, AARS2 associates with cyclic GMP-AMP synthase (cGAS) and mediates its lactylation and inactivation in cells and in mice."]. However, AARS2 depletion does not reduce basal global lysine lactylation in untreated HEK293T cells [PMID:40835008, "However, the knockdown of either enzyme did not alter Kla levels (Fig. S6, B–E), suggesting the AARS pathway is also not required for global lysine lactylation."].
- The cGAS mechanism has an unresolved localization problem rather than evidence for a routine cytosolic AARS2 pool [file:human/AARS2/AARS2-uniprot.txt, "Given that AARS2 is a mitochondrial protein, it is unclear how it can mediate lactylation of CGAS, which localizes in the cytosol and nucleus."].
- Disease mechanisms are allele-specific. For example, p.Arg580Trp mainly destabilizes the protein rather than abolishing catalytic chemistry [PMID:30285085, "Taken together, our data suggest that the p.Arg580Trp variant impacts on stability of mt-AlaRS protein but not aminoacylation or editing activities"]. Disease phenotypes therefore should not be promoted to core molecular functions.

## Curation priorities

- Replace broad nucleotide, nucleic-acid, aminoacyl-tRNA-ligase and tRNA-aminoacylation terms with ATP binding, tRNA binding, alanine-tRNA ligase activity and mitochondrial alanyl-tRNA aminoacylation, respectively.
- Treat the InterPro-derived cytoplasm row as an overly broad localization mapping and prefer mitochondrion; do not use the cGAS report to infer a normal cytosolic or nuclear isoform.
- Mark the merged HuRI protein-binding tuple as over-annotated: the two binary partners are retained for provenance, but neither defines a stable complex or core function.
- Keep the lactyltransferase activity as a genuine conditional secondary activity and the cGAS/STING process as non-core/contextual.
- Add direct human IDA recommendations for GO:0002196 Ser-tRNA(Ala) deacylase activity and GO:0106026 Gly-tRNA(Ala) deacylase activity.

## ClinGen Mendelian re-review — 2026-09-25

This session re-audited all 25 normalized GOA annotations, rather than treating the
pre-existing COMPLETE status as evidence of completion. Live QuickGO again returned
26 rows: the two HuRI partners collapse into one reviewed protein-binding tuple.
Every seeded assertion, evidence code, supporting entity, and cGAS annotation
extension is retained. There are 15 ACCEPT, 7 MODIFY, 2 KEEP_AS_NON_CORE, and 1 REMOVE
decisions; no new annotation rows are proposed.

### Evidence recovered and interpretation corrected

- The supported command `uv run ai-gene-review fetch-pmid 21549344 --force` recovered
  the foundational paper's full text. Figure 3D shows mitochondrial targeting of
  human AARS2-GFP in HEK293T cells. Its variant-specific charging/editing defects were
  **homology-model predictions**, and the authors did not detect mitochondrial
  translation defects in the cultured patient cells under the tested conditions.
  Earlier review prose incorrectly treated those predicted catalytic defects as
  measured. The IMP annotations remain biologically supported by subsequent human
  enzymology and cybrid experiments; the source code and original reference stay intact.
  [PMID:21549344](https://pubmed.ncbi.nlm.nih.gov/21549344/),
  [PMID:32080176](https://pubmed.ncbi.nlm.nih.gov/32080176/),
  [PMID:30262995](https://pubmed.ncbi.nlm.nih.gov/30262995/).
- The cGAS paper's [publisher full text](https://www.nature.com/articles/s41586-024-07992-y)
  was accessible by a normal HTTP request on this date, although the PubMed/PMC
  fetcher still caches only its abstract. Figure 3 and Extended Data Figure 4
  document human AARS2 biochemistry; Extended Data Figure 5h reports AARS2-dependent
  cGAS lactylation in human THP1 cells and mouse RAW264.7 cells. Extended Data Figure 5g reports
  endogenous AARS2–cGAS proximity in HeLa cells treated with 25 mM NaLac for 24 h.
  This supports the conditional human mechanism without resolving precursor versus
  mature AARS2 or its mitochondrial-import/access route. The review's full-text
  availability and reference assessment now distinguish website access from cache
  completeness. The quoted full-text snippet uses the schema's explicit
  `supporting_text_fulltext` field and is not presented as a cached quote.
- The production [GO-CAM 66f5faaa00000026](../../../gocams/66f5faaa00000026/66f5faaa00000026-src.yaml)
  already models AARS2 ATP-dependent lactyltransferase activity in negative regulation
  of cGAS/STING, with cGAS as substrate, **without an AARS2 compartment**. That supports
  retaining the reaction while preserving the location gap. Hypoxia-associated
  cytosolic AARS2 in PMID:38163844 was measured in mouse cells; it is not basal human
  localization evidence. No cytosol/nucleus annotation was added.

### Annotation and core-function decisions

| Evidence group | Decision and reason |
| --- | --- |
| Mitochondrion (IBA, IEA, two IDA, HTP; 5 rows) | ACCEPT; human targeting, reviewed immunofluorescence, proteomics, and enzyme biology agree. |
| Alanine-tRNA ligase (IBA, IEA, IMP; 3 rows) | ACCEPT; purified human enzyme and human cybrid rescue establish the reaction. |
| Mitochondrial alanine charging (IBA, IMP; 2 rows) | ACCEPT; AARS2 performs the organelle-specific reaction directly. |
| Aminoacyl-tRNA deacylase (IBA; 1 row) | MODIFY to the experimentally established Ser-tRNA(Ala) and Gly-tRNA(Ala) activities. |
| Broad nucleotide, nucleic-acid and aminoacyl-tRNA-ligase terms (IEA; 3 rows) | MODIFY to ATP binding, tRNA binding and alanine-tRNA ligase, respectively. |
| Cytoplasm and broad aminoacylation processes (IEA; 3 rows) | MODIFY to mitochondrion and mitochondrial alanyl-tRNA aminoacylation. Cytoplasm includes mitochondria and is not a false localization. |
| ATP binding, zinc binding, translational fidelity (IEA; 3 rows) | ACCEPT; direct chemistry, conserved editing-site architecture, and proofreading assays support these features. Zinc occupancy itself was not directly measured in the cited human study. |
| Protein binding (IPI; 1 merged row) | REMOVE as uninformative under the current protein-binding policy; this does not dispute the reported HuRI interactions. |
| ATP-dependent lactyltransferase (IEA, IDA; 2 rows) | ACCEPT as a conditional secondary activity, constrained by substrate and lactate context. |
| Negative cGAS/STING regulation (IEA, IDA; 2 rows) | KEEP_AS_NON_CORE; direct human evidence plus mouse genetics supports a conditional regulatory outcome. |

The two prior NEW proofreading rows were redundant descendants of an existing
GO:0002161 assertion. Their exact catalytic claims are retained as proposed
replacements on that row, with primary human evidence. Live QuickGO confirms that
GO:0002196 and GO:0106026 are current children of GO:0002161. The core synthesis now
represents the two substrate-specific editing reactions separately and preserves
the distinction between post-transfer glycine hydrolysis and pre-transfer editing.
No broad or disease-phenotype process annotation was added.

All 17 propagation reviews now identify proximate sources and explain their
relevance. IBA provenance uses the supplied ancestral PTN, not a donor count or a
claim of circularity from self-inclusion. Live InterPro entries verify the domain
mappings, UniProt verifies mouse Q14CH7/Aars2 and its experimental lactylation and
cGAS terms, and UniRule/ARBA API records verify the supplied rules. UR000375824 is a
eukaryotic AlaRS rule rather than a mitochondrion-only rule. The general source
mappings support the biology even when a human-specific term refinement is useful.

The key scope boundary from PMID:40835008 remains: depletion of AARS2 did not reduce
basal global lysine lactylation in the tested HEK293T model. It does not refute the
conditional substrate-specific mitochondrial or cGAS reactions. The ovarian and
cardiac disease papers remain contextual evidence, not additional core functions.

### Research workflow

`just fetch-gene-pmids human AARS2` completed concurrently with the requested
Falcon research attempt and verified all 14 cited PMIDs were cached. The foundational
full text was subsequently refreshed through the publication tool, not hand-edited.

The automatic research attempt reached a terminal failure: Falcon timed out after
600 seconds, then the configured perplexity-lite fallback returned HTTP 401
`insufficient_quota`. Neither provider produced a report; no provider-named file was
created manually. The primary-source review above proceeded independently.

Validation: `just validate human AARS2` passes with no warnings; history schema
validation passes; the gene HTML was regenerated. A direct comparison to the base
review confirms all 25 machine-seeded annotation bodies are unchanged, and every
propagation block now has source status and an explanatory comment.
