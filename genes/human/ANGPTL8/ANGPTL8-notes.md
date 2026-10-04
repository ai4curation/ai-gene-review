# ANGPTL8 notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANGPTL8 (lipasin/RIFL, formerly betatrophin) is a feeding-induced secreted protein that lacks the fibrinogen-like domain (PMID:23150577).
  - It forms a complex with ANGPTL3 that inhibits LPL far more than either protein alone (PMID:29031715).
  - It carries the complex's inhibitory motif; "the major inhibitory activity of this complex derives from ANGPTL8" (PMID:28413163).
  - Hepatic ANGPTL8 acts endocrinally; adipose ANGPTL8 inhibits ANGPTL4 locally (PMID:32730227).
- **Betatrophin:** the original beta-cell paper is retracted (PMID:23623304, retraction PMID:28038792); GOA does not cite it here. The NOT beta-cell-proliferation IDA (PMID:25417115) is correct and accepted.
- **NEW: contributes_to GO:0055102 lipase inhibitor activity** (IDA, PMID:29031715).
  - Participation: ANGPTL8 supplies the inhibitory motif.
  - Comparators: ANGPTL3 and ANGPTL4 carry GO:0055102. No ANGPTL8 ancestor/descendant conflict.
- **Kept as non-core:** positive regulation of protein processing (ANGPTL3 N-terminal fragment release) and signal transduction (auto-inferred from hormone activity).
- **Removed:** the RCHY1 protein-binding IPI (liver Y2H screen).
- **Not used from affinage:** the NF-kB/autophagy claim (single study). (Round 2 correction: the receptor-signaling claims are multi-group; see below.)

## 2026-10-04 round 2 (reviewer comments on #4065)

- **Correction:** I had called affinage's receptor-signaling claims "single-study" without reading those rows. They come from four independent groups: PirB in the liver clock (PMID:31388006), LILRB3 in cardiomyocytes (PMID:35851270), LILRB2 in stellate cells (PMID:36031141) and hepatocellular carcinoma (PMID:37188659), and PirB in hippocampus (PMID:39095838).
  - The signal transduction IEA stays KEEP_AS_NON_CORE, now reasoned and cited on that evidence.
  - The receptor axis is tissue- and disease-specific and secondary to the LPL role.
- **Other fixes:**
  - The GO:0010954 row adds the R59W/cleaved-ANGPTL3 association (PMID:27117576).
  - Core MF ordering fixed.
  - The description mentions receptor signaling.
  - Added a question on how the receptor and LPL roles relate.
