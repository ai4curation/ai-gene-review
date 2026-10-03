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

**Left unsupported (6) — honest:**

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
  [PMID:18273011 "At least 23 M. brevicollis genes encode one or more cadherin domains"].
- Abedin & King 2008 (Science 319:946; abstract only):
  [PMID:18276888 "We found cadherin genes at numbers similar to those observed in complex metazoans in one of the closest single-celled relatives of metazoans, the choanoflagellate Monosiga brevicollis."]
- Nichols et al. 2012 add *S. rosetta* and *Capsaspora*:
  [PMID:22837400 "Our finding of a cadherin gene in C. owczarzaki reveals that cadherins predate the divergence of the C. owczarzaki, choanoflagellate, and metazoan lineages."]
- The families shared with choanoflagellates are lefftyrins, coherins and hedglings,
  not classical cadherins
  [PMID:22837400 "the last common ancestor of metazoans and choanoflagellates contained representatives of at least three cadherin families, lefftyrin, coherin, and hedgling"].

**Classical cadherins and their beta-catenin-binding domain are animal-specific**
- The cytoplasmic cadherin domain (CCD) defines a classical cadherin:
  [PMID:22837400 "classical cadherins are distinguished by the presence of a cytoplasmic cadherin domain (CCD) at the C terminus that regulates interactions with the cytoplasmic protein β-catenin"].
- [PMID:22837400 "In contrast with premetazoan cadherin families (i.e., those conserved between choanoflagellates and metazoans), the later appearance of classical cadherins coincides with metazoan origins."]
- [PMID:27189570 "Choanoflagellates, which are thought to be the closest extant eukaryotic relatives of metazoans, also lack classical cadherins"].
- Choanoflagellate colonies lack adherens-junction-like structures:
  [PMID:22837400 "even in colony-forming S. rosetta , adjacent cells are linked by cytoplasmic bridges and lack structures that resemble the cadherin-based adherens junctions of metazoans"].
- My own check (`CDH1-bioinformatics/premetazoan_check.py`, output in
  `premetazoan_check_output.txt`, UniProt REST on 2026-10-01): UniProtKB entries with
  Pfam PF01049 (Cadherin_C, the CCD) number 0 in Choanoflagellata, Filasterea and
  Ichthyosporea, against 23,575 in Metazoa.
- In early animals the CCD is conserved:
  [PMID:20817718 "whereas its cytoplasmic domain, which binds the armadillo proteins p120ctn and β-catenin, remained quite conserved from placozoa to man"] (abstract only).
  - Sponge (*Oscarella*): the CCD keeps the beta-catenin-contact residues, and a Y2H screen
    recovered the classical cadherin
    [PMID:22837400 "an unbiased yeast two-hybrid screen of O. carmela proteins using Oc_bcat as the \"bait\" recovered OcCdh1 as a binding partner"].
    This is prediction plus Y2H. No in vivo test.
  - Cnidarian (*Nematostella*), direct biochemistry:
    [PMID:27189570 "The Kd for N. vectensis Cad-1 and -2 binding to N. vectensis β-catenin was 7.9 and 1.3 nM, respectively"].
    Function: alpha-catenin knockdown and calcium removal block re-aggregation of embryonic
    cells
    [PMID:30629955 "Cell adhesion is inhibited by α-catenin knockdown and removal of calcium in an ex vivo cell aggregation assay"].
    The authors conclude the cadherin-catenin complex (CCC) was a working adhesion module
    in the cnidarian-bilaterian ancestor.
- Sponge adhesion may not depend mainly on the CCC
  [PMID:27189570 "there is not yet any direct evidence demonstrating a role for the CCC in sponge adhesion"].

**What the premetazoan cadherins might do.** Nichols et al. only speculate: prey capture,
substrate or ECM attachment, collar integrity. One *M. brevicollis* cadherin localizes to
the microvillar collar
[PMID:22837400 "one cadherin (MBCDH1) has been shown to localize to the microvillar collar of M. brevicollis"].
No functional data exist for any choanoflagellate or *Capsaspora* cadherin.

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
[PMID:27189570 "The CCC appears to have arisen from two separate modules: a transmembrane cadherin adhesion module, and a cytoplasmic actin-binding module (α- and β-catenin), both of which existed independently prior to being co-opted into a single complex at an unknown point early in animal evolution"].
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
