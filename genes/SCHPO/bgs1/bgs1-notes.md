# bgs1 (Q10287, SPBC19G7.05c; cps1/drc1) review notes

## Biology summary

- GT48/FKS 1,3-beta-glucan synthase. It is the catalytic subunit responsible for the **linear**
  beta-1,3-glucan of the **primary septum**
  [PMID:39156640 "Bgs1 synthesizes the linear β(1,3)glucan of primary septum at cytokinesis."].
  Not needed for cell integrity [PMID:39156640 "The essential β(1,3)glucan synthase Bgs1 is
  responsible for the synthesis of this minor linear β(1,3)glucan, but is not involved in cell
  integrity."].
- Septum assembly: drc1-191 arrests with a stable ring and no septum [PMID:10545452 "We conclude
  that Drc1p/Cps1p is not required for cell elongation and cell growth, but plays an essential
  role in assembly of the division septum."].
- Localization: tips in interphase, then the contractile ring and septum; mating projection, zygote
  neck, forespore, germinating spore [PMID:12356913 "During vegetative growth, Bgs1p always
  localizes to the growing zones"]. Medial recruitment needs the medial ring and the SIN
  [PMID:12356913]. Bgs1 sits in the plasma membrane next to the ring [PMID:24790095 "SIN signaling
  regulates the accumulation of (1,3)β-d-glucan synthase Bgs1p/Cps1p in the plasma membrane
  adjacent to the contractile ring, where the enzyme synthesizes the primary septum"].
- Delivery: Myo52 [PMID:16421926]; vesicle cargo needing TRAPP-II and the exocyst [PMID:27082518
  "we calculated that ≥11 Bgs1 containing vesicles were delivered to the division site per
  minute during ring maturation"]; Blt1 helps recruitment [PMID:24790095].
- Partners: Ags1 co-IP [PMID:22891259 "physiological Bgs1 and Ags1 coimmunoprecipitate"]; Sbg1
  needed for trafficking [PMID:42786154 "Sbg1 is critical for the trafficking of Bgs1 to the
  plasma membrane"]. The Sbg1-Bgs1 AF3 model is analogous to Ghs2-Bgs3 (prediction only). Ghs2
  localization is unaffected in cps1-191 [PMID:42786154].
- Polarity: redundant with Tea1-Tea4 [PMID:39156640].

## Decisions

- GO:0003843 (IBA/IEA/IMP/ISS): MODIFY -> GO:0140753 linear 1,3-beta-D-glucan synthase activity
  (coordinator suggestion; the linear product is the consistent view in PMID:12356913 and
  PMID:39156640). Caveat: no in vitro assay of purified Bgs1 product linearity.
- GO-CAM gomodel:6918f23700003787 (PomBase) uses GO:0003843 for Bgs1 in GO:0031671 at
  GO:0032153, while the same model gives Bgs4 GO:0140752 (branched). The review suggests updating
  Bgs1 to GO:0140753 (raised as a suggested question). The process and location agree with this
  review.
- General process rows -> GO:0071970 (as for bgs3). Membrane -> plasma membrane. Cell septum ->
  division septum (KEEP_AS_NON_CORE: the septum is wall; Bgs1 is in the membrane lining it).
- Fungal-type cell wall IDA: MARK_AS_OVER_ANNOTATED, not REMOVE (experimental row, abstract only).
  This differs from bgs3, where a keyword NAS row was removed.
- Tip/mating/polarity terms: KEEP_AS_NON_CORE.
- Spore wall: suggested by PMID:12356913 localization only; no NEW row added.
