# DNAJC30 evidence guide

DNAJC30 has two supported mitochondrial roles: participation in repair of assembled complex I and association with ATP synthase. The repair mechanism remains unresolved at the biochemical-step level. These roles do not establish intrinsic ATPase activity, a stable respiratory-complex subunit or universal ATP-synthase dimer stabilization.

## Primary evidence and assay scope

[PMID:30318146, complete primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC6459420/) — Results on ATP-synthase interaction and the corresponding immunoprecipitation, yeast two-hybrid, localization and mitochondrial-function Methods distinguish the following experiments:

- Full human DNAJC30 bait selected MT-ATP6 and ATP5G2 (now ATP5MC2) in an adult human brain library. ATP-synthase F1 immunoprecipitation from adult human superior temporal cortex mitochondria recovered DNAJC30 and Fo/F1 subunits, with an IgG control.
- The tagged MT-ATP6 co-immunoprecipitation used a codon-optimized nuclear-expression construct with a COXVIII targeting sequence and a C-terminal tag. It is distinct from native complex precipitation.
- Inner-membrane immunogold used macaque dorsolateral frontal cortex. Human brain and cell observations provide complementary mitochondrial evidence; mouse knockout neurons/cortical mitochondria supplied respiration and ATP-production phenotypes.
- ATP-synthase dimer/supercomplex abnormalities in multigene Williams-Beuren samples were not reproduced as that pattern in isolated Dnajc30 knockout. Those samples do not establish a DNAJC30-specific dimer-maintenance function.

The MINT records [IM-29041](https://www.ebi.ac.uk/intact/search?query=IM-29041) resolve MT-ATP6 two-hybrid (IM-29041-1; EBI-27023768), MT-ATP6 anti-tag co-immunoprecipitation (IM-29041-13; EBI-27023813), and ATP5MC2 two-hybrid (IM-29041-7; EBI-27023780). IM-29041-15/EBI-27023834 is confocal colocalization and is not counted as a binary binding assay. Target and partner sequence/taxon identifiers match the official products. The native-complex and subunit assays together support [GO:0140260](https://www.ebi.ac.uk/QuickGO/term/GO:0140260), mitochondrial proton-transporting ATP synthase complex binding.

[PMID:33465056, complete primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7954600/) — Results on complex-I repair, complexome profiles and pulse-SILAC turnover, together with the blue-native/MS and cell-culture Methods, establish selective N-module turnover defects in patient fibroblasts and knockout HEK293 cells. Assembled complex I remains present without the expected assembly intermediates. DNAJC30 co-migration at low abundance is consistent with transient association; highlighted N-module interaction links originate in BioPlex. Selective turnover plus physical association supports participation in remodeling an existing complex. Direct extraction of damaged subunits, delivery to CLPXP or HSP70 activation was not reconstituted. The same study found no complex-V activity, abundance or turnover defect in its tested human systems; this limits a universal regulatory mechanism while preserving the earlier binding evidence.

Both complete primary articles were recovered and read separately from the normal publication caches. The cached 2018 representation is incomplete despite its availability metadata; that metadata and all original cache bytes remain unchanged. Source-specific claims above follow the original Results/Methods, not an assumption that every experiment occurs in the cache.

## Human mitochondrial proteomics

[PMID:34800366](https://pubmed.ncbi.nlm.nih.gov/34800366/) provides the human HEK293T fractionation and membrane-association workflow. The [original Table S1 workbook](https://ars.els-cdn.com/content/image/1-s2.0-S1550413121005295-mmc2.xlsx) identifies DNAJC30/Q96LL9 as protein group 9379 in worksheet `(A) All protein groups`, Excel row 322; it also appears in `(B) MitoCoP (1,134 genes)`, row 292.

The target has subtractive Class 1 (mean log2 purified/crude mitochondrial ratio 1.141; sequence coverage 55.525%), spatial Cluster 1 and importomics Class 1 assignments. Carbonate/sonication analysis classifies it as integral, with 94.383% integral and 92.923% membrane-associated fractions. These measurements establish mitochondrial membrane association. They do not independently resolve the inner versus outer membrane; the more specific GO:0005743 refinement uses the independent localization evidence above.

## HuRI binary interactions

[PMID:32296183, original study](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/) describes quadruplicate pairwise retesting and sequence confirmation. The [DNAJC30 IntAct records](https://www.ebi.ac.uk/intact/search?query=Q96LL9) contain 23 current GOA partner products, each with pooling (MI:1112), array (MI:0397) and positive validated two-hybrid (MI:1356) records: 69 records across the selected pairs. Literal target/partner sequence and taxon identifiers were checked. DNAJC30 is the canonical 226-residue sequence in an N-terminal Gal4 fusion context. The study's orthogonal validation is not attributed individually to every pair, and no supplementary threshold is imported from another interactome study.

The table lists the exact partner product and a bounded class assessment from its official record. A partner's activity is not assigned to DNAJC30. All entries retain positive binding evidence, while the grouped historical assertion remains non-core because one class-specific replacement would misrepresent this diverse panel.

| Partner | Literal product | Partner-class scope |
| --- | --- | --- |
| PEX12 | [O00623](https://www.uniprot.org/uniprotkb/O00623/entry) | Peroxisomal biogenesis/RING-associated machinery; no DNAJC30 ligase function inferred. |
| AQP6 | [Q13520](https://www.uniprot.org/uniprotkb/Q13520/entry) | Aquaporin anion channel. |
| EBP | [Q15125](https://www.uniprot.org/uniprotkb/Q15125/entry) | Sterol isomerase. |
| MSMO1 | [Q15800](https://www.uniprot.org/uniprotkb/Q15800/entry) | Sterol methyl oxidase. |
| TMEM52B | [Q4KMG9](https://www.uniprot.org/uniprotkb/Q4KMG9/entry) | Membrane protein; precise biochemical activity unresolved. |
| FAM209A | [Q5JX71](https://www.uniprot.org/uniprotkb/Q5JX71/entry) | Reproductive-system protein; precise biochemical activity unresolved. |
| SLC71A2 | [Q5SR56](https://www.uniprot.org/uniprotkb/Q5SR56/entry) | Transporter-family protein; substrate specificity not established here. |
| MRM1 | [Q6IN84](https://www.uniprot.org/uniprotkb/Q6IN84/entry) | Mitochondrial rRNA methyltransferase. |
| SLC51A | [Q86UW1](https://www.uniprot.org/uniprotkb/Q86UW1/entry) | Organic-solute transporter alpha subunit; requires its partner for normal transport. |
| LRRC25 | [Q8N386](https://www.uniprot.org/uniprotkb/Q8N386/entry) | Leucine-rich-repeat immune-regulatory protein; no single catalytic class assigned. |
| JAGN1 | [Q8N5M9](https://www.uniprot.org/uniprotkb/Q8N5M9/entry) | ER-associated protein involved in secretory-cell biology. |
| TMEM86B | [Q8N661](https://www.uniprot.org/uniprotkb/Q8N661/entry) | Lysoplasmalogenase. |
| KASH5 | [Q8N6L0](https://www.uniprot.org/uniprotkb/Q8N6L0/entry) | Nuclear-envelope motor-associated adaptor. |
| BEST2 | [Q8NFU1](https://www.uniprot.org/uniprotkb/Q8NFU1/entry) | Bestrophin anion channel. |
| GPX8 | [Q8TED1](https://www.uniprot.org/uniprotkb/Q8TED1/entry) | ER glutathione peroxidase-family protein. |
| FATE1 | [Q969F0](https://www.uniprot.org/uniprotkb/Q969F0/entry) | ER/mitochondrial-contact-associated protein. |
| SLC10A4 | [Q96EP9](https://www.uniprot.org/uniprotkb/Q96EP9/entry) | Solute-carrier family member; no specific DNAJC30 transport process inferred. |
| RNF170 | [Q96K19-5](https://www.uniprot.org/uniprotkb/Q96K19/entry) | 116-residue RNF170 product; canonical E3 activity is not automatically transferred to this short product. |
| SIGLEC12 | [Q96PQ1](https://www.uniprot.org/uniprotkb/Q96PQ1/entry) | Siglec-family putative adhesion molecule; ligand specificity is not established by the HuRI pair. |
| MGST2 | [Q99735](https://www.uniprot.org/uniprotkb/Q99735/entry) | Microsomal glutathione transferase. |
| CALN1 | [Q9BXU9](https://www.uniprot.org/uniprotkb/Q9BXU9/entry) | Calcium-binding protein. |
| REEP4 | [Q9H6H4](https://www.uniprot.org/uniprotkb/Q9H6H4/entry) | Microtubule-binding protein involved in ER distribution during mitosis. |
| SLC35H1 | [Q9NQQ7-3](https://www.uniprot.org/uniprotkb/Q9NQQ7/entry) | 394-residue SLC35H1 product; putative transporter assignment does not establish a specific transport activity. |

Neither membrane localization nor lack of a known shared pathway establishes that a positive screen interaction is an artifact. The unresolved issue is native physiological relevance and how to represent this heterogeneous grouped assertion. The [project curation instruction](https://github.com/ai4curation/ai-gene-review/blob/fc7539d95b201d1ca1d56150913ae1896a305a18/projects/CLINGEN_MENDELIAN.md#curation-instructions) supports retaining positive binding as non-core where a justified common refinement is unavailable.

## Orthology, products and the inherited remodeling proposal

The mouse donor [P59041](https://www.uniprot.org/uniprotkb/P59041/entry) carries experimental PMID:30318146 annotations for brain development and regulation of mitochondrial ATP synthesis. Official Ensembl one-to-one orthology joins human ENSP00000378605 and mouse ENSMUSP00000094318; their aligned sequences match the official 226- and 219-residue proteins. The ISS source names P59041; the electronic source additionally names the Ensembl translation. This is an orthology transfer, not a PAINT IBA. Brain development remains non-core; ATP-production regulation is retained with the mouse assay and human-system limits stated above.

[Q96LL9](https://www.uniprot.org/uniprotkb/Q96LL9/entry) records one 226-residue precursor. Transit peptide 1–38, mature chain 39–226, J-domain 49–114 and membrane segment 208–225 are predicted features. Cleavage does not establish alternative splice products, and a J-domain does not by itself establish HSP70 activation.

The existing [GO:0034367](https://www.ebi.ac.uk/QuickGO/term/GO:0034367) NEW proposal originated in [merged PR #4809](https://github.com/ai4curation/ai-gene-review/pull/4809); it is not one of the nine imported GOA triples. Its parent terms concern organization of an existing macromolecular complex. Neither brain development nor ATP-synthesis regulation is its ancestor or descendant. No DNAJC30 activity was found in the captured GO-CAM index. Current CLPX/O76031, CLPP/Q16740 and NDUFAF2/Q8N183 annotations lack this exact term; their proteolysis or assembly roles are not identical to the proposed accessory repair role. That absence is not evidence that curators overlooked a function. The proposal is retained on the independent physical-participation and selective-turnover evidence, with the biochemical step left unresolved. No additional NEW assertion is introduced.

## Regulatory scope and reproducible MitoCoP data

The ATP-synthase core now includes the already accepted [GO:1905706](https://www.ebi.ac.uk/QuickGO/term/GO:1905706) regulatory process. Figure 4F and the ATP-production Methods of the [2018 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC6459420/) use mouse cortical mitochondria, malate, pyruvate, ADP and a kinetic luciferase assay. This supports ATP-output regulation but does not isolate direct complex-V catalytic modulation from respiratory-chain effects. The native human binding evidence and negative complex-V findings in the later human study retain their distinct scopes.

The [factual target extract](DNAJC30-bioinformatics/MitoCoP-DNAJC30.json) retains accession/gene identity, source worksheet/row/column coordinates, classifications, replicate measurements and summary values. It excludes unrelated narrative database fields. It is cited only for the underlying proteomic observations; inner-membrane interpretation still requires independent localization. The workbook identifies a protein group and does not resolve a natural alternative product.

[Source provenance](DNAJC30-bioinformatics/source-manifest.json) gives the original public URL, capture time, byte count and SHA256. The [reader](DNAJC30-bioinformatics/reproduce.py) checks that hash before joining Q96LL9 and DNAJC30 and extracting the named fields. From this gene directory, with `uv` available:

```sh
uv run DNAJC30-bioinformatics/reproduce.py --download --check DNAJC30-bioinformatics/MitoCoP-DNAJC30.json
```

With a previously saved original workbook, replace `--download` with `--workbook /path/to/1-s2.0-S1550413121005295-mmc2.xlsx`. Use `--output /path/to/extract.json` instead of `--check` to regenerate. The saved-workbook reproduction was executed and matched the committed extract. The public-download option is implemented but was not rerun for this follow-up; a changed publisher file fails the hash check rather than being silently substituted. No key or private service is required.
