# PGM5 family review notes

PGM5 is the human PGM-related protein/aciculin branch of `PTHR22573:SF27`. The
family is only two reviewed human members on main: catalytic `PGM1`
(`UniProtKB:P36871`, already reviewed) and inactive structural `PGM5`
(`UniProtKB:Q15124`, this review). The existing family review already records
the key split: the root `PTN000501426` phosphoglucomutase IBD is sound for
catalytic PGMs, while `PTN002731341` is the vertebrate PGM5 node with a
supported `GO:0004614` IKR.

Direct human aciculin papers support the PGM5 exception. Belkin et al. 1994
identified a PGM-related 60/63 kDa adherens-junction antigen, found it at focal
contacts, actin-bundle ends, smooth-muscle dense plaques, cardiomyocyte
intercalated discs and striated-muscle myotendinous junctions, and reported no
detectable phosphoglucomutase activity in purified protein [PMID:8175905,
"the purified proteins have no detectable phosphoglucomutase activity"].
Moiseeva et al. 1996 cloned the PGM-related protein, showed that the mutase
active-site consensus is not conserved, and interpreted PGM5 as structural
rather than enzymatic [PMID:8631316, "encodes a protein with a structural rather
than an enzymatic role"]. Belkin and Burridge 1995 provides the dystrophin and
utrophin association and sarcolemma/myotendinous-junction evidence used to
interpret the sarcolemmal IBA [PMID:7890770, "concentrated at the sarcolemma
and at myotendinous junctions"], while the human quadriceps ultrastructure paper
supports the inner-sarcolemma IDA [PMID:10867799, "aciculin was present along
the inner surface of muscle plasma membrane"].

The catalytic InterPro2GO rows mostly reflect fold carryover onto a known
inactive paralog. `GO:0016868` and `GO:0005975` were removed. The Mg-binding
row was instead marked over-annotated because PGM5 keeps the FDADGDR Mg loop
while lacking direct Mg-binding evidence, and the cytosol row was marked
over-annotated because the current PAINT prune is scoped only to plastidic
PGMs. The two PGM5 process IBAs from the zebrafish seed (`GO:0014706` and
`GO:0030239`) were left `UNDECIDED`: the structural location and the
mouse-derived UniProt myofibril/sarcomere statement make a myofibrillar role
plausible, but the cached human literature only localizes PGM5 to mature muscle
junctions and the PTHR22573 family review leaves those two nodes unresolved.

Deep research was attempted with Falcon and a Perplexity Lite fallback, but the
runtime only exposed `claude_code` as a provider, so both configured providers
failed before any report was written.
