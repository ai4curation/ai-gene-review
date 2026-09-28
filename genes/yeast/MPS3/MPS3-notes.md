# MPS3 (S. cerevisiae, P47069) review notes

Context: budding-yeast SUN comparator for `modules/linc_complex.yaml`. Human comparators: SUN1, SUN2.

## Biology (with provenance)

- Essential INM half-bridge protein; required for first step of SPB duplication in G1; recruits centrin Cdc31 [PMID:12486115 "MPS3 encodes an essential integral membrane protein that localizes to the SPB half-bridge."].
- SUN domain binds Mps2 C-terminus, tethering half-bridge to core SPB [PMID:16923827]; Mps3-Mps2 form a noncanonical, high-stoichiometry LINC at the SPB insertion site; Mps3 is a SPIN component [PMID:30862629].
- Telomere anchoring in S phase via N-terminal acidic domain binding Sir4 [PMID:18039933 "Mps3 functions as an integral membrane anchor for telomeres"]; Ebp2/Rrs1 cooperate for clustering [PMID:21822217].
- Directly binds H2A.Z; H2A.Z needed for INM targeting [PMID:21518795].
- Cohesion establishment with Eco1/Ctf7; Mps3 acetylated by Eco1 [PMID:15355977, PMID:22593213].
- Meiosis: Ndj1 binds Mps3 N-terminus; bouquet [PMID:17495028]; RPMs need NDJ1, MPS3, CSM4 [PMID:18585352]; heterotrimeric t-LINC Mps3-Mps2-Csm4, Csm4-Mps3 physical interaction not detected by TAP (Mps2 bridges) [PMID:32967926].
- mps3-sun lacks SUN domain yet duplicates SPB; meiotic chromosome motion defective [PMID:22017544].

## Decisions

- Protein binding: Mps2 -> GO:0106166; Csm4 -> GO:0140444 (may be indirect via Mps2); Cdc31, Ndj1, Ebp2, Rrs1 -> GO:0043495; H2A.Z (3 rows) -> GO:0042393; Est1, Jem1, Eco1 -> REMOVE.
- ND root MF -> REMOVE.
- Karyogamy, nuclear congression, cohesion, homolog pairing, subtelomeric heterochromatin -> KEEP_AS_NON_CORE.
- NEW GO:0106094 (mitotic Mps3-Mps2 LINC) from PMID:30862629.

## Deep research

`MPS3-deep-research-falcon.md` read and incorporated (t-LINC composition, SPIN, telomere module); added PMID:32967926 and PMID:30862629 after eutils verification.

## Module implications

- Like Sad1, Mps3 is the sole SUN protein and serves both an SPB anchoring LINC (with KASH-like Mps2) and a meiotic telomere LINC (with Mps2+Csm4). Budding yeast KASH partners lack canonical PPPX KASH motifs; the meiotic t-LINC couples to actin (Myo2), not dynein - so the module's "microtubule tethering" complex terms fit imperfectly.
- Mps3's SUN domain is dispensable for SPB duplication but needed for meiotic chromosome motion [PMID:22017544], a notable divergence from the canonical SUN-KASH mechanism.
