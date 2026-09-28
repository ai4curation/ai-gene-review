# sad1 (S. pombe, Q09825) review notes

Context: reviewed as a fungal comparative member of `modules/linc_complex.yaml` (SUN component) and the
nucleokinesis module. Human comparators: SUN1, SUN2.

## Biology (with provenance)

- Essential SUN protein; SPB-associated throughout mitosis and meiosis [PMID:7744953 "exclusively associated with the spindle pole body (SPB) throughout the mitotic and meiotic cycles"].
- INM SUN protein pairing with KASH Kms1 to form a LINC [PMID:30462301 "Sad1 is a SUN-domain-containing inner-nuclear-membrane protein, and interacts with a KASH-domain-containing outer-nuclear-membrane Kms1 to form a trans-nuclear-membrane complex"].
- Mitotic partner Kms2; Sad1-Kms2-Ima1 couple centromeric heterochromatin to microtubules [PMID:18692466].
- Centromere clustering: Sad1 + Csi1 link centromeres to the INM near the SPB [PMID:23166349 "we have identified two factors of a molecular link that attaches and clusters centromeres at the inner nuclear envelope near the SPB"]; Sad1 residues 2-60 confer centromere-LINC association [PMID:27889481].
- SPB insertion: Sad1 ring at mitotic entry, first in the ring-assembly order Sad1 > Kms2/Cut12 > Cut11 [PMID:34133218]; "mutation of sad1+ results in SPB insertion errors" [PMID:28619713].
- Meiosis: Bqt1-Bqt2 bridge Rap1 to Sad1 [PMID:16615890]; bouquet linked to SPB via Sad1-Kms1 LINC [PMID:27889481].
- DNA damage: Sad1-Kms1 foci at persistent DSBs, coupling to microtubules [PMID:24943839]; basis of GO:1990612.
- Histone H2A-H2B binding by an N-terminal HBM, crystal structure; peripheral heterochromatin tethering/silencing [PMID:38773107].

## Decisions

- Protein binding rows: Kms1 -> MODIFY GO:0140444 (consistent with human SUN reviews); Bqt1 and Csi1 -> MODIFY GO:0043495 (Sad1 as membrane anchor for telomere/centromere complexes); Sif1, Ufe1 (Y2H screen) and Bqt4 (in vitro peptide, in vivo untested) -> REMOVE as uninformative.
- GO:0034993 IPI with Kms2 -> MODIFY to GO:0106094 (Kms2 is the mitotic SPB KASH partner); IBA GO:0034993 accepted (Sad1-Kms1 is meiotic).
- GO:1990612 verified in QuickGO: "Sad1-Kms1 LINC complex", defined around DSB repair, is_a GO:0034993. Accepted; ontology question raised.
- NEW GO:0042393 histone binding (IDA, PMID:38773107).
- All localization rows accepted; iMTOC and site of DSB kept as non-core.

## Deep research

`sad1-deep-research-falcon.md` read and incorporated (histone binding study, SPB ring model); led to adding PMID:38773107 and PMID:18692466.

## Module implications

- Sad1 confirms the SUN component is deeply conserved: SUN-KASH anchor (GO:0140444), nucleoplasmic partner anchoring (telomeres, centromeres), and meiotic telomere clustering are shared with human SUN1.
- Fungal-specific: SPB anchoring/insertion into a closed-mitosis nuclear envelope (GO:0106166, GO:0140480) and centromere (Rabl) tethering; these are the fungal counterparts of centrosome-nucleus coupling.
- Single SUN protein partners with two KASH proteins in different contexts (Kms2 mitotic/SPB; Kms1 meiotic/DSB), mirroring the variant structure of the module's KASH component.
