# cis4 (Q9HGQ3) — evidence and prediction assessment

Cis4 is a CDF-family zinc transporter that forms a heteromeric complex with Zrg17 in the cis-Golgi membrane. It transfers zinc from the cytosol into the secretory pathway, particularly under zinc-limiting conditions, and thereby supports intracellular zinc balance and Golgi-dependent protein trafficking. Its compartment and low-zinc role differ from the ER zinc transporter Zhf1.

## Evidence and family boundary

The [2008 target study](https://pubmed.ncbi.nlm.nih.gov/18199682/) identifies Cis4 localization at cis-Golgi and its interaction with Zrg17. The [2018 full-text study](https://pubmed.ncbi.nlm.nih.gov/29529046/) uses zinc-sensitive FRET sensors in defined cis4/zrg17/zhf1 mutants: Cis4/Zrg17 is important during zinc limitation; ER-localized Zhf1 is important when zinc is abundant. Thus zinc specificity is supported by target physiology rather than a generic CDF family label. The ER IEA assertion remains unresolved as a possible additional pool; no exclusion experiment establishes that Cis4 can never reside in ER.

These experiments do not establish exact transport coupling, affinity, stoichiometry or complete alternative-metal exclusion. Golgi trafficking and cell-wall phenotypes are downstream consequences of zinc partitioning, not evidence that Cis4 transports magnesium or directly assembles GPI anchors. Falcon agrees on these distinctions; its numerical phenotypes are not copied into curated fields without source verification.

## External ProtNLM statements

[Exact retained output](cis4-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | Zinc transporter | LSP | The correct broad name omits experimentally established cis-Golgi import with Zrg17 and its low-zinc role. Target zinc-sensor and localization experiments establish zinc specificity (PMID:18199682; PMID:29529046). |
| location | Membrane | LSP | A correct but broad compartment: the target is a cis-Golgi membrane transporter. This conclusion comes from target localization and zinc-transport physiology, not simply from a membrane-domain default (PMID:18199682; PMID:29529046). |

## Source quotations

[PMID:29529046](https://pubmed.ncbi.nlm.nih.gov/29529046/):

> Cis4 and Zrg17 form a heterodimeric complex that
> transports zinc into the cis-Golgi.

[PMID:29529046](https://pubmed.ncbi.nlm.nih.gov/29529046/):

> deletion of cis4 or
> zrg17 leads to higher levels of zinc accumulating in the cytosol under
> conditions of zinc deficiency

## Research provenance

The genuine [Falcon report](cis4-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** Q9HGQ3 is the reviewed, canonical, full-length UniProt entry for cis4 (SPAC17D4.03c),
732 aa, 14 predicted TM segments (UniProt FT TRANSMEM 52-72 ... 615-635), with the Cation_efflux
(PF01545) core and the Msc2-like signature (IPR045316). It is not an isoform, fragment or alternative
gene model; no domain or region is missing relative to the gene's product.

**Evolutionary placement.** PANTHER PTHR45755 ("FAMILY NOT NAMED"), subfamily SF4 ("ZINC TRANSPORTER 7").
SF4 also holds budding-yeast Msc2 (Q03455) and vertebrate ZnT7/SLC30A7; vertebrate ZnT5/SLC30A5 sits in
SF1 (`interpro/panther/PTHR45755/PTHR45755-entries.csv`). Note that Cis4 and Msc2 have the long
N-terminal TM extension seen in ZnT5 rather than the short ZnT7 architecture, yet PANTHER groups them with
ZnT7; the subfamily name is therefore not a functional statement about Cis4. The IBA terms for zinc
transporter activity, zinc homeostasis, zinc import into Golgi lumen and Golgi cis cisterna membrane come
from PTN000169508, which spans SF1+SF4 and includes Cis4, Msc2, ZnT5 and ZnT7 as donors; the
Golgi apparatus and cytoplasmic vesicle IBAs come from the deeper PTN000169412. PAINT did not propagate
ZnT5's proton-coupled antiporter activity; I treat that as deliberate and do not assert it.

**Literature.** PMID:18199682 (abstract only cached; PMC full text blocked by captcha here): cis4-1 from
an FK506/MgCl2 sensitivity screen; zinc suppresses phenotypes; Cis4 and Zrg17 physically interact and
share nonadditive phenotypes; Cis4 localizes to cis-Golgi (falcon summary of full text: Cis4-RFP
colocalizes with Rer1-GFP but not Krp1-GFP; MSC2+ZRG17 coexpression rescues). PMID:29529046 (full
text): ZapCY FRET sensors show cis4Δ/zrg17Δ accumulate cytosolic zinc in zinc deficiency, zhf1Δ when
zinc replete. Trafficking/cell-wall/acid-phosphatase/GPI-protein links (incl. Jaiseng 2012,
doi:10.1371/journal.pone.0041946, not cached) are downstream consequences of zinc supply; no process term
for membrane trafficking or GPI-anchor biosynthesis is proposed.

**Annotation decisions (re-examined, essentially unchanged).** Zinc transporter activity (EXP, IMP,
IBA, IEA) ACCEPT; intracellular zinc ion homeostasis (IDA, IMP, IBA, IEA) ACCEPT; zinc ion import into
Golgi lumen (IMP, IBA) ACCEPT; Golgi cis cisterna membrane (IBA) ACCEPT. Generic transport/cation/
homeostasis/membrane/Golgi terms MODIFY to the specific supported terms; zinc ion import into organelle
(IDA) MODIFY to its descendant GO:1904257. ER membrane (UniProt SubCell, no evidence tag) stays
UNDECIDED: Rer1 cycles ER-cis-Golgi and the Msc2 ortholog acts in the ER, so an ER pool is plausible
but unshown. Cytoplasmic vesicle (deep IBA) KEEP_AS_NON_CORE.

**Changes made.** Rewrote description (architecture, Zrg17 heteromer, low-zinc role, trafficking
phenotypes as downstream); added PMID:18199682 abstract quotes as support for localization and
interaction; expanded IBA reasons with node placement; added propagation_review on the Golgi apparatus
IBA; added reference_review for all references and a falcon file reference; added suggested questions and
experiments. No references removed, no files deleted.

**Next relative.** Budding-yeast MSC2 (Q03455): same PANTHER subfamily SF4, a donor to PTN000169508, the
Zrg17-partnered ortholog (ER zinc import with Zrg17), and it complements cis4 with ZRG17. No review in
`genes/yeast/`. Partner Zrg17 (SPBC16E9.14c) is also unreviewed. No module in `modules/` covers
Cis4/Zrg17 or secretory-pathway zinc import.
