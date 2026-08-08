# ACAP3 bioinformatics: domain-architecture audit of the IBA WITH/FROM source genes

## Question

All six of ACAP3's phylogenetically inferred (IBA, GO_REF:0000033) annotations are
propagated from PANTHER ancestral nodes whose calls rest on experimental annotations in
other organisms. Those source genes are named in the WITH/FROM column of
`ACAP3-goa.tsv`. A propagated annotation is only as safe as the architectural
equivalence between the source genes and ACAP3, so: **does each source gene actually
carry the ACAP module set?**

## Method

`check_iba_source_architecture.py` resolves every WITH/FROM identifier to a UniProt
accession (the search query used for each is recorded in the script's `SOURCES` table,
so the mapping is auditable), then reads the InterPro cross-references of each entry
from the UniProtKB REST API and tabulates presence/absence of the five ACAP modules:

| InterPro | module |
|---|---|
| IPR045258 | ACAP1/2/3-like (subfamily signature) |
| IPR001164 | ArfGAP domain |
| IPR004148 | BAR domain |
| IPR001849 | PH domain |
| IPR002110 | Ankyrin repeat |

Nothing is hardcoded; the table is regenerated from live UniProt/InterPro records.

```
uv run check_iba_source_architecture.py --markdown
```

## Result (run 2026-07-25)

| source (WITH/FROM) | gene | organism | acc | ACAP1/2/3-like | ArfGAP | BAR | PH | ANK repeat |
|---|---|---|---|---|---|---|---|---|
| - | ACAP3 (target) | Homo sapiens | Q96P50 | yes | yes | yes | yes | yes |
| MGI:MGI:2153589 | Acap3 | Mus musculus | Q6NXL5 | yes | yes | yes | yes | yes |
| UniProtKB:Q15057 | ACAP2 | Homo sapiens | Q15057 | yes | yes | yes | yes | yes |
| RGD:1562939 | Acap2 | Rattus norvegicus | Q5FVC7 | yes | yes | yes | yes | yes |
| WB:WBGene00000565 | cnt-1 | Caenorhabditis elegans | Q9XXH8 | yes | yes | yes | yes | yes |
| PomBase:SPBC17G9.08c | cnt5 | Schizosaccharomyces pombe | Q9UUE2 | yes | yes | yes | yes | **NO** |
| dictyBase:DDB_G0279649 | DDB_G0279649 | Dictyostelium discoideum | Q54WI0 | yes | yes | yes | yes | yes |
| dictyBase:DDB_G0276395 | DDB_G0276395 | Dictyostelium discoideum | Q551Q8 | yes | yes | yes | yes | yes |
| SGD:S000002932 | AGE1 | Saccharomyces cerevisiae | Q04412 | yes | yes | **NO** | **NO** | **NO** |
| AGI_LocusCode:AT5G13300 | AGD3 | Arabidopsis thaliana | Q5W7F2 | yes | yes | yes | yes | yes |
| AGI_LocusCode:AT5G61980 | AGD1 | Arabidopsis thaliana | Q9FIT8 | yes | yes | yes | yes | yes |
| FB:FBgn0004133 | blow (blown fuse) | Drosophila melanogaster | P91678 | **NO** | **NO** | **NO** | yes | **NO** |

## Interpretation

1. **Ten of the eleven source genes are bona fide ArfGAPs.** Everything from
   *Arabidopsis* AGD1/AGD3 through *Dictyostelium*, fission yeast cnt5, worm cnt-1 and
   the mammalian ACAP2/Acap3 entries carries both the ACAP1/2/3-like signature and an
   ArfGAP domain. The centaurin-beta architecture is therefore genuinely ancient, and
   propagation of `GTPase activator activity` and of peripheral-membrane localisation
   across this set is architecturally sound.

2. **`blow` (blown fuse) is the one exception, and it is a stark one.** It has a PH
   domain and nothing else: no ACAP1/2/3-like signature, no ArfGAP domain, no BAR
   domain, no ankyrin repeats. It cannot be an Arf GAP, because it has no GAP domain.
   PANTHER family PTHR23180 (CENTAURIN/ARF) has clustered it in on the PH domain alone.
   `blow` is the source for exactly one ACAP3 annotation — `GO:0030036 actin cytoskeleton
   organization` — where its contribution should be discounted. (The same annotation is
   independently supported by the two *Dictyostelium* ACAPs, which do have the full
   architecture and do have experimental actin annotations, so the term itself survives.)

   The cost of the mis-clustering is visible in the reverse direction too: `blow` now
   carries `GO:0005096 GTPase activator activity` by IBA (GO_REF:0000033) despite having
   no ArfGAP domain and no zinc finger. That reciprocal annotation looks like the
   clearer error, and is worth reporting to the PANTHER/PAINT curators.

3. **Yeast AGE1 is an ArfGAP but not an ACAP.** It has the ArfGAP domain without the
   BAR–PH–ANK modules, consistent with the Alliance ortholog call placing it with
   ASAP1/ASAP2 rather than with the ACAPs. For the generic term `GO:0005096` the
   transfer is harmless; it would not support transfer of any BAR/PH-dependent
   membrane-remodelling function.

4. **Fission yeast cnt5 lacks the ankyrin repeats** but keeps ArfGAP + BAR + PH,
   i.e. the membrane-remodelling core. Its `plasma membrane` IDA is a safe donor.

## Caveats

- InterPro membership is a signature-match statement, not a structural one, and absence of
  a signature is weaker evidence than presence. What makes the `blow` result hard to
  explain away is that **three** independent module families (ArfGAP, BAR, ANK) plus the
  subfamily signature are missing simultaneously, while the one module it does have is the
  same one PANTHER could have clustered on. Length does not by itself settle it: `blow` is
  644 aa against ACAP3's 834 aa, so it is shorter but not too short in principle to carry
  an ArfGAP domain. The argument is the joint absence of four signatures, not the size.
- Mouse Acap3 (Q6NXL5) and *Drosophila* `blow` (P91678) have no Swiss-Prot entry; the
  TrEMBL entries were used. For `blow`, all four TrEMBL isoform entries (A1Z714 644 aa,
  P91678 644 aa, E1JGZ4 637 aa, Q8MSU1 532 aa) carry the identical InterPro pair
  IPR011993 + IPR001849, so the conclusion does not depend on which was chosen.
