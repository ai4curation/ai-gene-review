# spo13 review notes

## 2026-11-06

### PTHR14430 and PAINT

Spo13 is the short *S. pombe* member of PTHR14430, `PTHR14430:SF4`.
The PTHR14430 PAINT nodes currently visible in the local cache are the broad
Opisthokonta `PTN000374167` Rab-GEF activity node, the fungal `PTN001024876`
cell-tip node, and a vertebrate cytosol node. None are propagated to Spo13 in
the fetched QuickGO rows, which is appropriate: the cell-tip node is seeded by
the long vegetative Sec2 paralog, `PomBase:SPAC23C4.10`, and CGD SEC2, whereas
Spo13 is a short meiosis-specific meiotic outer plaque/SPB Rab GEF.

Yang and Neiman noted the same paralog split directly: most fungi retain both a
short Spo13-like ORF and a long Sec2-like ORF, while budding yeasts appear to
have lost the shorter Spo13-like member.

### Literature read

PMID:18367542 is the foundational Nakase et al. SPB-remodeling paper. The local
cache is abstract-only but includes the direct summary facts used by PomBase:
Spo13 and Spo2 are sporulation-specific, localize to the cytoplasmic side of the
meiotic SPB, are required for SPB modification and FSM initiation, and assemble
in a Spo15 -> Spo2 -> Spo13 hierarchy.

PMID:20130084 is the primary Spo13 GEF paper. It shows that Spo13 has homology
to the budding-yeast Sec2 exchange domain, performs Rab nucleotide exchange in
vitro, acts on Ypt2 rather than Ypt1 or Ypt3 in vitro, and requires the GEF
domain for FSM assembly in vivo.

PMID:27630265 extends the model by placing Ypt3 and Ypt2 at the meiotic SPB and
FSM. It treats Spo13 as the meiosis-specific SPB GEF for Ypt2 and shows that
Ypt3 and Ypt2 SPB localization depends on Spo13.

PMID:28876998 is a later Ypt2-recruitment follow-up. It does not overturn the
GEF assignment; it shows that Spo13's GEF activity is required for efficient
Ypt2 recruitment, that anchored Spo13 is not sufficient to recruit Ypt2 during
vegetative growth, and that efficient recruitment depends on meiosis-specific
regulators including Sid2 and Mug27.

PMID:29813128 is upstream of Spo13. Dms1 is needed to maintain Spo15, Spo2, and
Spo13 at the SPB, but the paper does not change the Spo13 GO calls.

### Annotation decisions

Accept the direct and InterPro `GO:0005085` rows. Spo13 has no PAINT IBA rows,
so the PTHR14430 family check here is an absence check rather than an IBA
over-propagation call.

`GO:0005515 protein binding` is true for Spo13-Spo2 binding but not useful.
Unlike Spo2, Spo13 is not established as a bridging adaptor: Spo2 binds Spo15
and Spo13, while Spo13 does not bind Spo15 directly. Removed this generic MF row
and kept Spo13's GEF as the core molecular activity.

The UniProt SubCell `GO:0005816 spindle pole body` row is a true parent of the
direct meiotic SPB rows, so it is modified to `GO:0035974`. The broad
`GO:0030437 ascospore formation` row is modified to the descendant
`GO:0031322 ascospore-type prospore-specific spindle pole body remodeling`
because the same 2008 study supports the more specific SPB-remodeling process.
