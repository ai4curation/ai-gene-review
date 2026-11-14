# SLC7A6 (y+LAT2 / Y+L amino acid transporter 2) — curation notes

UniProt: Q92536 (YLAT2_HUMAN), 515 aa, chromosome 16. HGNC:11064. Gene also known as KIAA0245.
TCDB 2.A.3.8.23; APC superfamily, LAT family. PANTHER PTHR11785:SF398.

## Summary of function

y+LAT2 is the **catalytic light chain** of a heteromeric amino-acid transporter (HAT). It is
**disulfide-linked to the heavy chain SLC3A2 (4F2hc / CD98hc)**; the heavy chain is required for
trafficking of the light chain to the plasma membrane while the light chain carries the transport
pore [PMID:11311135 "whereas the transport process itself is catalysed by the light"; PMID:31705628 "that is required for the proper expression of the transporter on the plasma membrane"].
The complex is the system **y+L** transporter (ComplexPortal CPX-8188; GO complex GO:1902495).

Mechanism: **electroneutral, obligatory 1:1 antiport (exchanger)** [UniProt CC:FUNCTION "The transport mechanism is electroneutral and operates with a stoichiometry of 1:1"].
It exchanges intracellular **cationic amino acids** (L-arginine, L-lysine) for extracellular
**neutral amino acids** (L-leucine, L-glutamine, isoleucine, methionine, histidine, cysteine)
**plus Na+**; it also exchanges L-arginine for L-lysine in a **Na-independent** manner
[PMID:10903140 "followed an antiport mechanism"; UniProt CC:FUNCTION "Also exchanges L-arginine with L-lysine in a sodium-independent manner"].
The Na+ requirement is specifically for the **neutral-amino-acid arm** of the exchange (the hallmark
of y+L-type transporters), not a symport of the cationic substrate.
Physiologically the dominant direction is **efflux of cationic amino acids** (arginine export) in
exchange for neutral-AA + Na+ influx [PMID:10903140 "arginine release may be the main physiological function of this transporter."; PMID:31705628 "the influx of neutral amino acids (leucine, glutamine) and sodium, working as an antiport"].
In polarized epithelia the complex sits at the **basolateral** membrane and moves cationic amino
acids from renal/intestinal epithelia toward the bloodstream [PMID:31705628].

Kinetics (UniProt BIOPHYSICOCHEMICAL PROPERTIES): KM ~120 uM arginine (+NaCl), 236 uM leucine,
295 uM glutamine; fibroblast arginine KM 0.145 mM with Vmax 1.479 nmol/min/mg [PMID:31705628].
y+LAT1 (SLC7A7) and y+LAT2 (SLC7A6) share comparable arginine affinity [PMID:31705628 "y+LAT2 in fibroblasts."].

## Tissue expression
Wide distribution: brain, heart, testis, kidney, small intestine, parotis [PMID:10903140 "y(+)LAT2 has a wider tissue distribution, including brain, heart, testis,"]; HUVEC,
monocytes, RPE, carcinoma lines; highly expressed in T lymphocytes [UniProt TISSUE SPECIFICITY]. More
ubiquitous than SLC7A7/y+LAT1 (which is high in monocytes/macrophages, Caco-2, kidney). In LPI
fibroblasts and erythrocytes, y+LAT2 compensates for mutant y+LAT1 [PMID:31705628; PMID:15756301].

## Key per-row reasoning

- **MF core**: L-arginine transmembrane transporter activity (GO:0061459, IDA ×2 + IBA) and the
  antiporter activity L-lysine:L-arginine antiporter (GO:0106439, IDA) are the precise, accepted MF.
  Generic transporter-activity terms (GO:0022857, GO:0015171, GO:0015174 basic AA) are entailed by
  these → TOO_GENERAL.
- **Arginine binding** (GO:0034618, IDA PMID:19562367): substrate-recognition step of the transport
  activity; genuine but subsidiary → KEEP_AS_NON_CORE.
- **Neutral-AA arm**: neutral amino acid transport (GO:0015804) and L-leucine transport (GO:0015820)
  are the influx half of the obligate exchange → ACCEPT. amino acid import across plasma membrane
  (GO:0089718) = influx arm (oocyte uptake of arg/leu/gln demonstrated) → ACCEPT.
- **Ornithine transport** (GO:0015822, IMP PMID:17197568): y+LAT2 siRNA cut ornithine uptake only
  ~22% in RPE cells (CAT-1 dominant) → genuine minor cationic substrate → KEEP_AS_NON_CORE
  [PMID:17197568 "CAT-1 and y(+)LAT2 siRNA, respectively, whereas LAT1 and LAT2 siRNA had no"].
- **Glycine betaine transport** (GO:0031460, ISS/IEA from mouse Q8BGK6): "By similarity" only, narrow
  cumulus-oocyte reproductive context, unverified in human → KEEP_AS_NON_CORE (both rows).
- **Nitric oxide biosynthetic process** (GO:0006809, ISS from rat D3ZMM8): y+LAT2 supplies the NOS
  substrate arginine but does **not** itself catalyse any step of NO synthesis. Supplying a substrate
  is not participation (see CLAUDE.md participation test) → MARK_AS_OVER_ANNOTATED.
- **protein binding** (GO:0005515, IPI PMID:32296183, partner Q9UPQ8=DOLK): bare, uninformative
  HuRI high-throughput Y2H hit (dolichol kinase); no functional meaning → REMOVE (protein-binding
  policy). The biologically meaningful interactor is SLC3A2/4F2hc, modelled via in_complex (GO:1902495).
- **membrane** (GO:0016020, IEA InterPro) → MODIFY → plasma membrane (GO:0005886).
- **plasma membrane** rows (EXP, IBA, IDA/HPA, IEA, TAS ×3): core location → ACCEPT.
- **IBAs**: GO:0003333 and GO:0005886 use the broad APC/amino-acid-transporter node PTN000208507
  (spans yeast MUP1, fly, worm, etc.) — family-level, correct; GO:0003333 is also TOO_GENERAL.
  GO:0061459 IBA uses the y+LAT-specific node PTN002623494 and lists Q92536 in WITH/FROM — that is
  the gene's own experimental grounding (expected, NOT circular).

## LPI note
LPI (lysinuric protein intolerance; MIM 222700) is caused by SLC7A7 (y+LAT1), not SLC7A6. SLC7A6 is
the paralogous, more ubiquitous y+L light chain and a candidate compensatory transporter; it is not
itself a confirmed LPI disease gene [PMID:31705628; PMID:15756301].
