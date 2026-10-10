# CDH1 (E-cadherin) — curation notes

## 2026-06-22 — manual PubMed curation of IBA support

Applied the proven manual-PubMed support-finding workflow (asta deprecated, see issue #1599) to the
14 IBA annotations that lacked independent PMID/DOI support. Several already had a `supported_by`
entry pointing at the falcon deep-research file (`file:...`), which is why they were flagged
unsupported — I appended foundational primary PMIDs (verified verbatim against the fetched abstract).

Added independent PMID support to **8 of 14** IBA annotations:

| Term | GO | Reference |
|---|---|---|
| beta-catenin binding | GO:0008013 | PMID:7806582 (β-catenin interacts with E-cadherin) |
| catenin complex | GO:0016342 | PMID:2349235 (uvomorulin/E-cadherin associates with catenins α/β/γ) |
| cadherin binding | GO:0045296 | PMID:20190754 (classical-cadherin strand-swap homophilic binding) |
| cell-cell adhesion mediated by cadherin | GO:0044331 | PMID:3498123 (Nagafuchi/Takeichi 1987) |
| calcium-dependent cell-cell adhesion | GO:0016339 | PMID:3498123 ("Ca2+-dependent intercellular adhesion between epithelial cells") |
| adherens junction | GO:0005912 | PMID:7806582 (E-cadherin in adherens junctions of epithelia) |
| adherens junction organization | GO:0034332 | PMID:3498123 (anti-E-cadherin disperses compact cell colonies) |
| apical junction complex | GO:0043296 | PMID:23643492 (E-cadherin at the epithelial zonula adherens) |

**Historical unresolved judgments (superseded where specified in the 2026-10-10 audit below):**

- **GO:0007043 cell-cell junction assembly** — core E-cadherin function, but I did not locate a clean
  cached *primary* statement specifically about junction *assembly* in a quick search (Adams/Vasioukhin
  live-imaging papers would fit; not fetched). Distinct from the organization term above.
- **GO:0016477 cell migration** — real but context-dependent (E-cadherin suppresses single-cell
  invasion yet enables collective migration); a single IBA "cell migration" is too coarse to anchor
  cleanly to one primary paper.
- **GO:0000902 cell morphogenesis** — broad developmental term; better captured by specific
  morphogenesis processes than a general primary citation.
- **GO:0005737 cytoplasm** — E-cadherin is a plasma-membrane protein with a cytoplasmic *domain*;
  a blanket "cytoplasm" CC is arguably an over-annotation and was not given primary support.
- **GO:0007416 synapse assembly** — the synaptic classical cadherin is largely N-cadherin (CDH2);
  this looks like a phylogenetic over-propagation to CDH1 and was not supported.
- **GO:0016600 flotillin complex** — obscure CC; no clean primary support surfaced; likely
  over-propagated.

Note: unlike the LGALS3 asta run, CDH1's foundational literature (Nagafuchi/Takeichi 1987, the
Ozawa/Kemler catenin papers, Harrison 2010 structure) was trivially recovered by direct PubMed
search — again reinforcing that targeted manual search beats the retrieval-only provider.
## Premetazoan origin (ORIGINS_OF_MULTICELLULARITY, 2026-10-01)

Automated deep research was not run for this section. The sources below were checked
against PubMed, fetched with `just fetch-pmid` and read in the cache. PMID:18276888 and
PMID:20817718 are abstract-only. The rest are full text.

**Cadherins predate animals**
- Choanoflagellate genome:
  The genome survey identified at least 23 cadherin-domain genes in M. brevicollis ([PMID:18273011](https://pubmed.ncbi.nlm.nih.gov/18273011/)).
- Abedin & King 2008 (Science 319:946; abstract only):
  The abstract compares the numerous M. brevicollis cadherin genes with metazoan repertoires ([PMID:18276888](https://pubmed.ncbi.nlm.nih.gov/18276888/))
- Nichols et al. 2012 add *S. rosetta* and *Capsaspora*:
  Capsaspora contains a cadherin, placing domain-family origins before its divergence from choanoflagellates and animals ([PMID:22837400](https://pubmed.ncbi.nlm.nih.gov/22837400/))
- The families shared with choanoflagellates are lefftyrins, coherins and hedglings,
  not classical cadherins
  The inferred shared ancestral repertoire includes lefftyrin, coherin and hedgling families ([PMID:22837400](https://pubmed.ncbi.nlm.nih.gov/22837400/)).

**Classical cadherins and their beta-catenin-binding domain are animal-specific**
- The cytoplasmic cadherin domain (CCD) defines a classical cadherin:
  Classical cadherins have a C-terminal cytoplasmic domain involved in beta-catenin association ([PMID:22837400](https://pubmed.ncbi.nlm.nih.gov/22837400/)).
- The authors place classical-cadherin emergence near animal origins, later than the shared premetazoan families ([PMID:22837400](https://pubmed.ncbi.nlm.nih.gov/22837400/))
- The surveyed choanoflagellates lack classical cadherins ([PMID:27189570](https://pubmed.ncbi.nlm.nih.gov/27189570/)).
- Choanoflagellate colonies lack adherens-junction-like structures:
  S. rosetta colonies have cytoplasmic bridges rather than recognizable animal-like cadherin adherens junctions ([PMID:22837400](https://pubmed.ncbi.nlm.nih.gov/22837400/)).
- My own check (`CDH1-bioinformatics/premetazoan_check.py`, output in
  `premetazoan_check_output.txt`, UniProt REST on 2026-10-01): UniProtKB entries with
  Pfam PF01049 (Cadherin_C, the CCD) number 0 in Choanoflagellata, Filasterea and
  Ichthyosporea, against 23,575 in Metazoa.
- In early animals the CCD is conserved:
  The cytoplasmic catenin-binding region is conserved across the surveyed placozoan-to-human sequences ([PMID:20817718](https://pubmed.ncbi.nlm.nih.gov/20817718/)) (abstract only).
  - Sponge (*Oscarella*): the CCD keeps the beta-catenin-contact residues, and a Y2H screen
    recovered the classical cadherin
    The Oscarella beta-catenin bait recovered OcCdh1 in a yeast two-hybrid screen ([PMID:22837400](https://pubmed.ncbi.nlm.nih.gov/22837400/)).
    This is prediction plus Y2H. No in vivo test.
  - Cnidarian (*Nematostella*), direct biochemistry:
    The measured Nematostella cadherin-1 and -2 affinities for beta-catenin were 7.9 and 1.3 nM ([PMID:27189570](https://pubmed.ncbi.nlm.nih.gov/27189570/)).
    Function: alpha-catenin knockdown and calcium removal block re-aggregation of embryonic
    cells
    Alpha-catenin depletion and calcium removal impaired aggregation of dissociated Nematostella cells ([PMID:30629955](https://pubmed.ncbi.nlm.nih.gov/30629955/)).
    The authors conclude the cadherin-catenin complex (CCC) was a working adhesion module
    in the cnidarian-bilaterian ancestor.
- Sponge adhesion may not depend mainly on the CCC
  The study did not establish a direct in vivo adhesive role for the sponge complex ([PMID:27189570](https://pubmed.ncbi.nlm.nih.gov/27189570/)).

**What the premetazoan cadherins might do.** Nichols et al. only speculate: prey capture,
substrate or ECM attachment, collar integrity. One *M. brevicollis* cadherin localizes to
the microvillar collar
A Monosiga cadherin was localized to its microvillar collar ([PMID:22837400](https://pubmed.ncbi.nlm.nih.gov/22837400/)).
The cited historical survey did not establish a function for these choanoflagellate or *Capsaspora* cadherins.

**Classification of CDH1 core functions**

| Core function (existing review) | Classification | Basis |
|---|---|---|
| Calcium ion binding by EC repeats | Ancestral (domain level) | EC domains are present in *Capsaspora* and choanoflagellate cadherins. Calcium binding by those proteins has not been tested; it is inferred from the EC fold |
| Homophilic trans-adhesion (cadherin binding, GO:0045296) | Unresolved before animals; animal-specific in the classical-cadherin form | The EC1 strand-swap interface is classical-cadherin chemistry. No premetazoan cadherin has been shown to be adhesive |
| Beta-catenin binding (GO:0008013) via the CCD | Animal-specific | No CCD outside Metazoa (literature and Pfam count). Shown biochemically in *Nematostella*; predicted plus Y2H in sponge |
| p120/delta-catenin binding (juxtamembrane domain) | Animal-specific (by sequence) | Hulpiau & van Roy abstract: conserved from placozoans. Not tested biochemically outside bilaterians in what I read |
| Adherens junction organization, epithelial polarity, tissue integrity, EMT and tumour suppression | Animal-specific | Choanoflagellate colonies have no adherens-junction-like structures. Tissue-level roles need an animal epithelium |

This agrees with the CTNNB1 and CTNNA1 reviews: classical-cadherin binding is
animal-specific, while an armadillo/alpha-catenin module without cadherins is older
(Dictyostelium; PMID:21393547, cited there). In my reading, the CCC formed when an
existing catenin module was joined to a new transmembrane cadherin
The authors propose that pre-existing cadherin and cytoplasmic catenin modules became coupled during early animal evolution ([PMID:27189570](https://pubmed.ncbi.nlm.nih.gov/27189570/)).
On the cadherin side, E-cadherin's catenin-binding tail is the animal novelty.

**Track C: propagation audit for the CDH1 IBA nodes** (QuickGO,
withFrom=PANTHER:<node>, taxa 28009 / 2687318 / 127916, descendants; run 2026-10-01 by
the script above)

| Node (PAINT taxon) | CDH1 IBA terms on it | Reaches unicellular holozoans? |
|---|---|---|
| PTN000616280 (taxon:33213 Bilateria) | GO:0000902, GO:0005912, GO:0007043, GO:0016339, GO:0034332, GO:0044331 | **Yes: 30 TreeGrafter IEA rows (GO_REF:0000118)** on 3 *S. rosetta* proteins, F2UD23, F2UFV3, F2USU1, all PTHR24027:SF422 |
| PTN008601603 (no taxon in PAINT file; root of the IBDs) | GO:0008013, GO:0016342, GO:0045296, GO:0016477, (GO:0098609) | **Yes: 5 IBA rows** on *M. brevicollis* A9V8Y4 (PTHR24027:SF438) |
| PTN000616414 (taxon:32524 Amniota) | GO:0007416, GO:0016600, GO:0043296 | No |
| PTN002771833 (taxon:117571 Euteleostomi) | GO:0005737 | No |

- Filasterea and Ichthyosporea: 0 hits on all nodes.
- Each *S. rosetta* protein receives 10 terms:
  - GO:0000902 cell morphogenesis
  - GO:0005912 adherens junction
  - GO:0007043 cell-cell junction assembly
  - GO:0008013 beta-catenin binding
  - GO:0016339 calcium-dependent cell-cell adhesion
  - GO:0016342 catenin complex
  - GO:0016477 cell migration
  - GO:0034332 adherens junction organization
  - GO:0044331 cell-cell adhesion mediated by cadherin
  - GO:0045296 cadherin binding
  
  So a node that PAINT labels Bilateria passes its terms, through TreeGrafter, to proteins
  outside it.
- The *M. brevicollis* protein receives GO:0008013 beta-catenin binding, GO:0016342 catenin
  complex, GO:0045296 cadherin binding, GO:0016477 cell migration and GO:0098609 cell-cell
  adhesion.
- None of the four choanoflagellate proteins has Pfam PF01049 (the CCD). Their Pfam domains:
  - F2UD23: Cadherin, EGF_Teneurin, SH2, Vwde
  - F2UFV3: Cadherin, fn2
  - F2USU1: Cadherin, Y_phosphatase (a lefftyrin-like PTPase cadherin)
  - A9V8Y4: Cadherin, EGF_2, SH2, TIG, VWD, Vwde
  
  Beta-catenin binding, catenin complex, adherens junction and adherens junction
  organization are therefore unsupported for all four. These are proteins without the
  binding domain, in organisms with no beta-catenin-family protein (CTNNB1 review) and no
  adherens junctions.
- No organ, tissue or embryonic-development process term reaches a unicellular holozoan from
  these nodes. The animal-specific content is the junction and catenin terms listed above,
  plus GO:0000902 cell morphogenesis and GO:0016477 cell migration (generic, not
  tissue-level).
- Likely root causes:
  - The IBDs on PTN008601603 sit at a node broader than the classical cadherins, in the
    PTHR24027 "CADHERIN-23" family, which pools many cadherin subfamilies.
  - TreeGrafter grafted SF422 choanoflagellate cadherins under the bilaterian
    classical-cadherin node.
  - Error types: `TAXON_CONSTRAINT_VIOLATION` / `PATHWAY_CONTEXT_IGNORED` (the partner,
    beta-catenin, is absent).
- I did not edit any other gene. Human CDH1 rows are unaffected: CDH1 is a bona fide
  classical cadherin with experimental support for each term. I added an evolutionary
  note, without changing the action, to the GO:0008013 IBA row.


## 2026-10-10 — substantive ClinGen campaign audit

This audit starts from the committed CDH1 review at `5398606ad5092d6ed5ebbb668e9391f1f4bfc4c7`, not the unrelated dirty workspace copy. It preserves all 201 original annotation objects (including one inherited proposed annotation), both alternative products, the 238-row GOA file, UniProt record, existing provider reports, pathway file and historical bioinformatics outputs. Partner assertions collapsed by the older seed are retained in the original GOA and exposed in the accompanying evidence extract; no modern source fields were invented to rewrite that seed. The dated journal and tables above are retained; long historical quotations were paraphrased, and current corrections are stated here. The 2026-10-01 evolutionary analysis was not rerun and is not new evidence for changing human PAINT node placement.

The normal publication-fetch command succeeded. A genuine Falcon attempt and the explicitly configured perplexity-lite fallback both reached their bounded timeouts; no report was fabricated. Manual research used the actual primary caches, selected externally accessible Results/Methods, source-linked interaction records and current GO definitions. A cache's full-text flag does not guarantee that its extracted text includes Results. In particular, separate full-text access was needed for EPLIN, flotillin and PTPN23.

The standing [campaign curation instruction](https://github.com/ai4curation/ai-gene-review/blob/f7dc8b60bf8be80744f75955c3c1a3c16bd73888/projects/CLINGEN_MENDELIAN.md#curation-instructions) governs supported generic binding: use `KEEP_AS_NON_CORE` when no better supported molecular function is available; refine when the source supports a meaningful class; retain `UNDECIDED` when the relevant assertion cannot be adjudicated. It does not preserve wrong-protein attributions established from actual experimental constructs. No shared policy or validator was changed.

### Adhesion and junctional organization

The representative core is the calcium-stabilized adhesive ectodomain plus its catenin-binding cytoplasmic scaffold. PMID:11976333 directly tests cadherin-dependent aggregation and migration; PMID:21300292 separates trans adhesion from lateral assembly. Its abstract states that “cis interface mutations disrupt stable junction formation” ([primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3070544/)). The mouse ectodomain structures are distinguished from the full-length human E-cadherin mutant experiments. Calcium binding, beta-catenin association, and p120 association describe CDH1's own activities; kinase, phosphatase, actin-binding or ubiquitin-ligase activities of partners are not transferred to CDH1. No new process annotation is added.

PMID:15240885 Figure5B shows p120/E-cadherin co-immunoprecipitation in transfected L cells and a G-alpha12-dependent increase. Its construct species are not all independently resolved; human p120 source-linked records provide additional support. The baseline's p120/delta-catenin proposal is retained with a shorter source-specific explanation. PMID:16212417 recovers catenin complexes using an E-cadherin intracellular-domain affinity surface; alpha-catenin association is not presented as proof of a direct purified E-cadherin/alpha-catenin interface.

[PMID:29999492](https://pubmed.ncbi.nlm.nih.gov/29999492/) distinguishes primary human keratinocyte imaging of nascent desmosomes from mouse E-cadherin L175D/K14E mutant experiments. It supports a non-core role in early desmosomal organization. The exact CDH1 desmosomal assay in PMID:33596089 was not separately resolved; the original tuple is retained with this independent support explicitly identified. Full PMID:20859650 Figure6 tests human HCT116 E-cadherin depletion and border recruitment of PKP3/PKP2/desmoplakin, with a different plakoglobin result. E-cadherin therefore helps organize the destination rather than merely serving as trafficking cargo.

[PMID:17620337 full primary Results](https://www.researchgate.net/publication/6218270_Ankyrin-G_Is_a_Molecular_Partner_of_E-cadherin_in_Epithelial_Cells_and_Early_Embryos), Figure1C, shows E-cadherin-dependent recruitment of ankyrin-G-GFP to HEK293 membranes, with ankyrin-B as the comparison. Figure3 examines reconstituted catenin/ankyrin complexes. This directly supports the existing protein-localization process at a bounded recruitment/scaffold scope. The normal cache is abstract-only; the separate full primary access is not misrepresented as an enriched cache or a new human embryo experiment.

### Corrections to earlier location judgments

[PMID:24046456 full author-uploaded paper](https://www.researchgate.net/publication/256705606_Flotillin_microdomains_stabilize_cadherins_at_cell-cell_junctions) resolves the old flotillin uncertainty. Figure1B shows reciprocal E-cadherin/flotillin immunoprecipitation in human MCF7 cells; Figure7D shows cholesterol-sensitive association. GO:0016600 expressly allows flotillin-associated proteins, so a permanent structural-subunit requirement was inappropriate. Figure2E identifies E-cadherin/flotillin-2 in lamellipodia and Figure3B their cortical-actin colocalization. The respective source qualifiers are preserved. Figure text and selected Results were inspected, not newly quantified figure pixels.

The broad cytoplasmic terms are not rejected merely because E-cadherin is transmembrane: GO:0005737 includes intracellular organelles. Intracellular trafficking and the cytoplasmic interaction region corroborate retention of the PAINT inference, without claiming a direct free-cytosolic adhesion assay or reconstructing the historical ancestral node. Extracellular retention is grounded in actual released E-cadherin material, including human gastric-cell supernatant experiments in PMID:34742300, rather than the orientation of a membrane-attached ectodomain. These pools are non-core relative to junctional adhesion.

### FZR1/Cdh1 namesake source corrections

Seven removals are based on full experimental source identity, not on paper titles or an assumption that E-cadherin cannot function in neurons. An independent annotation reviewer checked the six strongest chains and separately assessed the seventh with its narrower authentication limit.

| Original index | Preserved source | Actual experimental identity |
|---|---|---|
|43|PMID:20802534; original partner P30260/CDC27|[Full Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC2995849/) identify HA-Cdh1 Addgene11596; the [official depositor record](https://www.addgene.org/11596/) identifies human FZR1, GenBank AF083810.|
|44|PMID:20951947; original partner P30260/CDC27|[Full Figure2E and4C](https://pmc.ncbi.nlm.nih.gov/articles/PMC2957475/) assay the C-terminal IR tail/APC coactivator. A separate current curated APC1 record is not the original CDC27 partner and does not override the construct identity.|
|189|PMID:19822757; original partner O00762/UBE2S|[Full Figure2D–G and Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC2775311/) test a Cdh1 WD40 deletion and purified His-Cdh1 in APC-associated chain elongation.|
|74–76|GO_REF:0000107; rat Q9R0T4/ENSRNOP00000027346 donor; PMID:21186356|[Author-hosted full article](https://iplab.hkust.edu.hk/pdf/Journals%20pdf/2011_02%20NatNeuro.pdf), Figures5D,6,7 and online Methods, tests APC/C-dependent AMPA-receptor regulation and Cdh1ΔWD40. These identify the APC regulator, not E-cadherin.|
|71|GO_REF:0000107; rat Q9R0T4 donor; PMID:23226367|[Full Results/Figures1–3](https://pmc.ncbi.nlm.nih.gov/articles/PMC3511349/) and Methods use Cdh1-APC/Smurf1/p250GAP constructs and rat neuronal Cdh1 RNAi. The exact construct/RNAi sequences were not independently authenticated; no WD40 assay is claimed for this source.|

The genuine rat donor is E-cadherin, so the errors occur in its source annotation chain; it was incorrect to speculate that these human rows simply came from N-cadherin. Conversely, the separate PAINT/electronic synapse-assembly assertions are retained as non-core with their uncertainty about historical construct/node details. A short donor list is not evidence against PAINT.

The other rat donors are source-specific. PMID:16671876 and17120308 measure expression changes after cyclosporin A and tributyltin. PMID:17373711 and12387456 assay E-cadherin during development/sprouting. PMID:20501441 concerns Bifidobacterium treatment, not Listeria; PMID:16997938 measures a rat heparin-related staining response and lists a 2023 correction whose text was not recovered. These electronic process transfers remain or become over-annotated because the inspected expression/localization evidence does not establish E-cadherin performing a step in the respective process. This is a participation boundary, not denial of the measured changes. PMID:12700184 explicitly reports Fer association with N-cadherin rather than E-cadherin; independent human EGFR/FGFR1 associations support the kinase-binding biology while leaving this donor provenance defective.

The same boundary applies to experimental response annotations without dismissing unseen evidence. The abstract of PMID:10868478 reports E-cadherin induction alongside drug-associated invasion/migration changes, but its full CDH1-specific functional assay was not recovered, so that IDA remains undecided. In contrast, the full PMID:12937339 Methods and Figure1 Results were inspected and directly measure LiCl-driven E-cadherin induction with inositol/TSA controls; E-cadherin is the measured output in those experiments. That existing lithium-response process is marked over-annotated for lack of demonstrated participation, not for lack of a real expression change.

The first core now uses GO:0098641, cadherin binding involved in cell-cell adhesion, supported by the actual cell-aggregation assays. The inherited broad mediator row is refined to that activity. The distinct E-cadherin-Fc source row remains a refinement to cadherin binding because soluble-ligand engagement alone does not establish an opposing-cell partner. The calcium core explicitly distinguishes mouse ectodomain structural sites from human junctional experiments.

### Interaction evidence and limits

[CDH1-interaction-evidence.json](CDH1-interaction-evidence.json) preserves the exact original partner accessions, literal selected IntAct/MINT record fields, species, methods, mutation/fragment features, record URLs, retrieval hashes and one official OpenCell CTNNB1-bait/CDH1-prey row. These curated records share provenance with the GOA annotations; repeated assay records, databases and BioPlex releases are not independent replication. Co-IP/AP-MS supports complex association, while proximity ligation is spatial proximity; neither alone establishes an isolated binary interface. The OpenCell prey is a multi-accession protein group and does not resolve P12830-2 separately. The 25-partner fragment screen preserves its four isoform-qualified accessions and fragment features. The breast-cancer interaction source records a CDH1 position243 mutation, whose amino-acid substitution was not invented.

[PMID:18093941 full Results/Figure1](https://pmc.ncbi.nlm.nih.gov/articles/PMC2224173/) shows E-cadherin/EPLIN co-IP in human DLD-1 cells. Reconstitution demonstrates association through alpha- and beta-catenin and no isolated EPLIN/E-cadherin-tail binding. This resolves that source row to non-core generic association with the indirect mechanism explicit. The Src, PKP2-containing collapsed row, exosome, CD46, Armus, negative-adhesion, indole-3-carbinol response and perinuclear-localization assertions remain undecided where their precise original assays could not be adjudicated; absence from a database is not negative evidence. The old removal of PMID:19653274 based on its LEF1 abstract is reversed to uncertainty.

PMID:21724833 ([full Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC3134084/), supplementary Figure13A text) reports capture of E-cadherin by the PTPN23 E1357A trapping domain from pervanadate-treated human-cell lysates. This supports association but not the original cell-adhesion-molecule partner class. Its reported PTPN23 peptide activity differs from [PMID:19340315](https://pmc.ncbi.nlm.nih.gov/articles/PMC2661844/), which tests human protein and finds no WT activity on its substrates, with rescue by S1394A. The association is generalized to GO:0005515 as a non-core destination under the explicit instruction; neither trapping nor the partner name settles physiological catalytic class. No phosphatase activity is assigned to E-cadherin.

All new quotations in the YAML and this entry are short, source-specific anchors. Repeated quotations and the historical excerpts above were counted together; caches and provider outputs were left unchanged. Normal schema, term, reference, best-practice and render checks accompany the finite handoff. DRAFT and justified unresolved assertions describe biological review state; campaign completion still requires ROOT's publication, independent acceptance and passing checks.


The final bounded source peer recovered the genuine PMID:23086448 supplementary PDF (SHA256 `65d9c4f3e8cfa08ef3de9ff3481aba569e571098b593e1877095f29fdcc8077c`, matching the PMC XML checksum). Its Figure4a and legend show alpha-E-catenin detection after CD46 immunoprecipitation in primary human CD4 T cells, with CD3/isotype and gamma-secretase controls. This confirms that assay's identity, but the original P12830–P15529 GOA tuple was not linked to an exact curatorial assay record, so the CDH1 assertion remains undecided. For PMID:23533145, the full main article and Table S2 identity were verified, but the exact exosome protein table could not be recovered through the attempted routes. That HDA becomes undecided; neither passive shedding nor ectodomain release is asserted from an uninspected CDH1 table entry.
