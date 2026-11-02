# Curation Notes for Escherichia phage T7 gene 4 (DNA primase/helicase, P03692)

## Identity & Sequence Features
- **UniProt ID**: P03692 (`DPRIM_BPT7`)
- **Gene symbol**: `4` (DNA primase/helicase, gp4, EC 5.6.2.3 / EC 2.7.7.101)
- **Length**: 566 AA (Class II protein; produces two overlapping isoforms from in-frame initiation codons: 63-kDa full-length gp4A, 566 AA, and 56-kDa N-terminally truncated gp4B, 503 AA initiated at Met-64)
- **Domains**:
  - `InterPro:IPR013237` / `Pfam:PF08273` (`Zn_Ribbon_Prim`, Zinc-binding domain of primase-helicase, residues 6-57; present in 63-kDa gp4A, absent in 56-kDa gp4B) and `InterPro:IPR048774` / `Pfam:PF21268` (`Helic-prim_T7_N`)
  - `InterPro:IPR006171` (`TOPRIM_dom`) / `InterPro:IPR034154` (`TOPRIM_DnaG/twinkle`) / `Pfam:PF13155` (`Toprim_2`, Toprim RNA polymerase domain of primase, residues 70-245)
  - `InterPro:IPR007694` (`DNA_helicase_DnaB-like_C`) / `InterPro:IPR046394` (`Helic_Prim_T7`) / `InterPro:IPR027417` (`P-loop_NTPase`) / `Pfam:PF03796` (`DnaB_C`, DnaB-like replicative helicase C-terminal domain, residues 272-566)

## Functional Evidence
- **Two overlapping isoforms (gp4A 63-kDa and gp4B 56-kDa), zinc finger, ssDNA binding, dTTPase/ATPase, and 5'-3' DNA helicase**:
  - `PMID:2829184`: Gene 4 encodes two colinear proteins of 63 kDa (gp4A) and 56 kDa (gp4B, lacking the N-terminal 63 residues containing the Cys4 zinc-finger motif). Purified 56-kDa gp4B binds single-stranded DNA in the presence of dTTP, catalyzes DNA-dependent hydrolysis of dTTP (and ATP/NTPs), and possesses 5'-3' DNA helicase activity, whereas the N-terminal 63-residue zinc-binding domain in 63-kDa gp4A is specifically required for template-directed oligoribonucleotide primer synthesis [PMID:2829184, "Like a mixture of the two proteins, the 56-kDa protein binds single-stranded DNA in the presence of dTTP, catalyzes DNA-dependent hydrolysis of dTTP, and has helicase activity. A putative \"zinc finger\" present near the amino terminus of the 63-kDa protein but absent from the 56-kDa protein may play a major role in the recognition of primase sites in the template."].
  - `PMID:9185573`: Isolated C-terminal fragments of gp4 retain hexamerization, dTTPase, and 5'-3' DNA helicase activities [PMID:9185573, "One of these fragments, which is derived from the C-terminal region of the protein, was prepared and shown to retain helicase activity."].
- **DNA-directed RNA primase activity & replisome coordination**:
  - `PMID:11279245`: Ring-shaped gp4 hexamers synthesize tetraribonucleotide primers (`pppACCC`, `pppACCA`, `pppACAC`) at specific recognition sequences (`5'-GTC-3'`) on the lagging-strand template and form a direct complex with T7 DNA polymerase (gp5-thioredoxin) to deliver primers for Okazaki fragment synthesis [PMID:11279245, "Gene 4 of bacteriophage T7 encodes a bifunctional primase-helicase that assembles into a ring-shaped hexamer with both DNA unwinding and primer synthesis activities."].
- **Hexameric lock-washer structure, hand-over-hand DNA unwinding, and replisome interactions**:
  - `PMID:32009150`: Cryo-EM structures of the gp4 helicase domain bound to a DNA fork show a six-subunit spiral lock-washer hexamer encircling the 5'-3' tracking ssDNA strand with 2 nt per subunit, translocating via a sequential hand-over-hand mechanism coupled to NTP hydrolysis [PMID:32009150, "The six subunits of gp4 adopt a spiral lock-washer form that encircles a coil-like DNA (tracking) strand with 2 nucleotides (nt) bound to each subunit."].
  - `PMID:30679383` and `PMID:8528255`: Direct homo-oligomeric hexamer/heptamer interaction (`UniProtKB:P03692`) and direct binding to T7 DNA polymerase gp5 (`UniProtKB:P00581`) within the four-protein T7 replisome [PMID:30679383, "The bacteriophage T7 replisome is easy to reconstitute as it consists of only four proteins—precise interactions of DNA helicase-primase (gp4), DNA polymerase (gp5), single-stranded DNA-binding protein (gp2.5), and Escherichia coli thioredoxin (trx) lead to concerted leading- and lagging-strand synthesis"].

## GO Annotation Review Summary
- `GO:0043139` (`5'-3' DNA helicase activity`, IDA `PMID:2829184`, IDA `PMID:9185573`, IEA `GO_REF:0000120`) -> `ACCEPT` (core function).
- `GO:0003899` (`DNA-directed RNA polymerase activity`, IDA `PMID:11279245`, IEA `GO_REF:0000104`) -> `ACCEPT` (core primase function; note that in GO `DNA-directed RNA primase activity` or `DNA primase activity` is represented here by `GO:0003899` in GOA).
- `GO:0016887` (`ATP hydrolysis activity`, EXP `PMID:2829184`, IEA `GO_REF:0000116`) -> `MODIFY` to `GO:0043139` (`5'-3' DNA helicase activity`, as NTP/ATP hydrolysis directly powers the 5'-3' DNA helicase activity).
- `GO:0003697` (`single-stranded DNA binding`, IEA `GO_REF:0000002`) -> `ACCEPT`.
- `GO:0005524` (`ATP binding`, IEA `GO_REF:0000120`) -> `ACCEPT`.
- `GO:0008270` (`zinc ion binding`, IEA `GO_REF:0000120`) -> `ACCEPT`.
- `GO:0005515` (`protein binding` with `UniProtKB:P00581`, IPI `PMID:30679383`, IPI `PMID:8528255`) -> `REMOVE` (bare `protein binding` removed per GO curation policy; the physical complex with gp5 is captured in `core_functions`).
- `GO:0042802` (`identical protein binding` with `UniProtKB:P03692`, IPI `PMID:30679383`, IPI `PMID:8528255`) -> `ACCEPT`.
- `GO:0039693` (`viral DNA genome replication`, IEA `GO_REF:0000120`) -> `ACCEPT`.
- `GO:0006269` (`DNA replication, synthesis of primer`, IEA `GO_REF:0000043`) -> `ACCEPT`.
- Broad parent terms (`GO:0000166`, `GO:0003677`, `GO:0003678`, `GO:0003824`, `GO:0004386`, `GO:0006260`, `GO:0016740`, `GO:0016779`, `GO:0016787`, `GO:0016853`, `GO:0046872`) -> `MODIFY` to their specific descendants in the annotation set.
