# Ch25h (mouse, Q9Z0F5) — curation notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

First review of this gene folder. Written without opening any ProtNLM2 prediction file or
prediction-evidence folder; all claims below come from UniProtKB Q9Z0F5, the cached
publications, PANTHER/PAINT data in the repository, and GO/QuickGO lookups.

### Deep research

`just deep-research-falcon mouse Ch25h --fallback perplexity-lite` failed: the Edison API
returned `403 Forbidden` on `/auth/login`, and the perplexity-lite fallback produced no
file either. No `Ch25h-deep-research-*.md` exists for this gene. The review was therefore
built from the literature directly: the three PMIDs GOA cites, plus one paper added by
PubMed search and cached here (PMID:23273844).

### What the mouse protein is

- 298 aa, intron-less gene, polytopic ER membrane protein with three predicted
  transmembrane helices and a fatty-acid-hydroxylase domain (residues 128–263), three
  histidine-box motifs (142–146, 157–161, 238–244), and two N-glycosylation sites
  [file:mouse/Ch25h/Ch25h-uniprot.txt].
- Not a cytochrome P450 — a non-haem diiron oxygenase
  [PMID:9852097 "Unlike most other sterol hydroxylases, cholesterol 25-hydroxylase is not a cytochrome
  P450, but rather it is a member of a small family of enzymes that utilize diiron
  cofactors to catalyze the hydroxylation of hydrophobic substrates."].
- Catalysis requires the histidine clusters
  [PMID:9852097 "clusters of histidine residues that are essential for catalytic activity"];
  UniProt records the `HH->EE` mutation of His242-His243 as loss of function
  (`ECO:0000269|PubMed:9852097`).
- UniProt gives two Rhea reactions (RHEA:21104, RHEA:46132) and EC 1.14.99.38, all with
  `ECO:0000269|PubMed:9852097`, and an Fe cation cofactor from the same paper.
- Expression: low in many tissues, highest in lung
  [PMID:9852097 "The murine gene is expressed at low levels in multiple"]; strongly induced in
  activated macrophages and dendritic cells (below).

### Evolutionary grounding (this governs two REMOVEs)

PANTHER 19.0 classification files in `.cache/panther/PTHR19.0_mouse`:

- `Ch25h` (Q9Z0F5, MGI:1333869) → **PTHR11863:SF213 CHOLESTEROL 25-HYDROXYLASE**
- `Msmo1` (Q9CRA4, MGI:1913484) → **PTHR11863:SF225 METHYLSTEROL MONOOXYGENASE 1**

Human CH25H (O95992) is also PTHR11863:SF213 (`.cache/panther/panther-members-19.0.tsv`),
so mouse and human CH25H are same-subfamily orthologs and transfers between them are sound.

PAINT IBDs for this family (`interpro/panther/PTHR11863/PTHR11863-paint.tsv`):

| node | term | taxon | seeds |
|---|---|---|---|
| PTN002627316 | GO:0001567 cholesterol 25-hydroxylase activity | 117571 Euteleostomi | MGI:1333869, UniProtKB:O95992 |
| PTN000221246 | GO:0000254 C-4 methylsterol oxidase activity | 2759 Eukaryota | MSMO1, ERG25, Candida and Arabidopsis SMOs, Msmo1 |
| PTN000221246 | GO:0005789 ER membrane | 2759 Eukaryota | incl. MGI:1333869 |
| PTN002275159 | GO:0036197 zymosterol biosynthetic process | 6072 Eumetazoa | MGI:1913484 (Msmo1) only |
| PTN002275159 | GO:0006695 cholesterol biosynthetic process | 6072 Eumetazoa | Msmo1, zebrafish msmo1 |

So the subfamily-level node PTN002627316 carries exactly the activity the mouse protein is
known to have, and the two IBA rows this review removes (GO:0000254, GO:0036197) both come
from deeper nodes whose seeds are all methylsterol-oxidase-branch genes. The committed
family review `interpro/panther/PTHR11863/PTHR11863-review.yaml` independently calls the
family `HETEROGENEOUS` and states that "C4 methylsterol oxidase activity is therefore not a
family-wide grant and is not supported for CH25H". Cholesterol has no C-4 methyl group, and
the enzyme acts on finished cholesterol, downstream of zymosterol — so neither term can be
read as merely broad. The ER-membrane IBD at the same deep node is a different matter:
membrane residence really is shared across the family and is independently experimental in
the mouse, so that row is accepted.

Note that mouse Ch25h appearing in its own IBA `WITH/FROM` (PTN002627316 seeds) is expected
and is not circularity: its experimental annotation is one of the descendant evidences the
PAINT curator used to place the node.

### Experimentally established in mouse (as opposed to inferred)

Established **in this species**:

- Cholesterol 25-hydroxylase activity and the diiron/non-P450 chemistry: PMID:9852097
  (mouse cDNA cloned and characterised alongside the human one).
- ER membrane localisation: PMID:9852097, recorded by UniProt with `ECO:0000269`.
- Repression of sterol biosynthesis: Ch25h−/− BMDMs lose 25-HC and accumulate desmosterol,
  lanosterol and 7-dehydrocholesterol
  [PMID:29033131 "indicating that Ch25h acts to repress cholesterol biosynthesis pathway activity"];
  wild-type but not catalytically dead Ch25h represses Sqle
  [PMID:29033131 "Overexpression of Ch25h could repress the sterol biosynthesis enzyme Sqle mRNA, whereas vector and Ch25hmut had no effect"].
  The 1998 paper showed the same in transfected cells
  [PMID:9852097 "the biosynthesis of cholesterol from acetate and suppresses the cleavage of"].
- Type I interferon induction
  [PMID:23273844 "both types of IFNs induced expression of Ch25h within 3hrs"], and
  IFNAR-dependence of TLR-driven induction
  [PMID:23273844 "IFN receptor deficient (ifnar−/−) BMMs had abrogated Ch25h expression when treated with these agonists showing that Ch25h expression is IFN-dependent"].
  GOA carries GO:0034340 only as ISS/ISO/IEA from human, so the mouse evidence is stronger
  than the evidence codes suggest; there is no way to express an evidence-code upgrade in
  this schema, so it is recorded here and in the row's `reason`.
- Antiviral loss-of-function phenotypes
  [PMID:23273844 "Ch25h−/− J2 BMMs displayed 5-fold increased susceptibility to VSV infection"] and
  [PMID:23273844 "Ch25h-deficient mice were more susceptible to MHV68 lytic infection"].
- Lymphoid B-cell positioning
  [PMID:22999953 "In Ch25h−/−, Cyp7b1−/−, and Hsd3b7−/− mice that had been reconstituted with wild-type BM cells, day 2-activated B cells failed to accumulate in outer follicles"].

**Inferred, not established in mouse:** the detailed mechanism by which 25-HC blocks
virus–cell fusion (worked out with purified 25-HC and viral glycoprotein systems, and in
human cells for SARS-CoV-2), and the human-ortholog-sourced GO:1903914 rows. The product is
the same molecule in both species and the mouse genetic phenotypes are consistent, so these
rows are accepted, with the limitation stated in the row.

### Comparator check for B cell chemotaxis (GO:0035754)

QuickGO, mouse annotations to GO:0035754 (queried 2026-10-20): Cxcl13, Xcl1, Il4, Gas6,
Ptk2b, **Ch25h, Cyp7b1 and Hsd3b7** — all three oxysterol enzymes from PMID:22999953,
including Hsd3b7, which *inactivates* the ligand. GO curators therefore treat the enzymes
that shape the 7α,25-OHC gradient as participants in this process, consistently and
deliberately. That settles the row as KEEP (non-core, since the enzyme supplies a precursor
two steps upstream of the chemoattractant and does not migrate or signal itself) rather than
as something to argue with.

### Ontology gap

There is no GO biological-process term for oxysterol or 25-hydroxycholesterol metabolism:
searching GO for `oxysterol` returns only GO:0120021, GO:0141209, GO:0008142, GO:0008396 and
GO:0033783 (all MF or signalling), and `hydroxycholesterol` returns only molecular functions.
So the product side of this reaction can only be expressed as GO:0008203 cholesterol
metabolic process (kept, core) or GO:0008610 lipid biosynthetic process (kept, non-core).
Raised as a `suggested_questions` entry rather than a proposed term, since the right scope
of such a branch is a GO editorial decision.

### Actions summary (27 rows)

- ACCEPT 18 — all GO:0001567 rows (EXP, IBA, IDA, IEA, IMP, ISO, ISS), all GO:0005789 rows,
  all GO:0008203 rows, GO:0005506, GO:0090206, all three GO:1903914 rows.
- KEEP_AS_NON_CORE 5 — GO:0008610, the three GO:0034340 rows, GO:0035754.
- MODIFY 1 — GO:0008395 steroid hydroxylase activity → GO:0001567 (true, but one level less
  specific than the cited paper supports, and the gene already carries the child).
- TOO_GENERAL 1 — GO:0016705 (ARBA; a grandparent of GO:0001567).
- REMOVE 2 — GO:0000254 and GO:0036197, both deep-node IBAs from the methylsterol-oxidase
  branch of PTHR11863 (see above).

No `NEW` terms proposed. The obvious candidates — inflammasome restraint, macrophage
cholesterol homeostasis, antiviral defence at large — are either downstream organismal
consequences of the metabolite, already covered by GO:0090206 and GO:1903914, or would
require asserting participation the enzyme does not perform.
