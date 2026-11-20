# nuoK (E. coli K-12, P0AFE4) notes

## 2026-10-23 / 2026-11-01 review session

Deep-research providers are unavailable in this environment (no API keys), so the
literature was reviewed by hand from cached `publications/PMID_*.md` files and the
UniProt record. Most cached primary papers are abstract-only; experimental GOA rows
whose full text was not seen are deferred to the curator.

Key evidence:
- NuoK E-channel glutamates are needed for coupling: [PMID:15996109 "Mutations of nearly
  perfectly conserved Glu-36 lead to almost null activities of coupled electron transfer
  with a concomitant loss of generation of electrochemical gradient."]
- Membrane-arm structure: [PMID:21822288 "It includes six subunits, NuoL, NuoM, NuoN,
  NuoA, NuoJ and NuoK, with 55 transmembrane helices."]; E-channel: [PMID:36920092
  "ND3/NuoA, ND6/NuoJ and ND4L/NuoK, which form, together with part of ND1, the E-channel
  containing key glutamates"]
- YidC-dependent insertion (basis of the IPI protein binding row, removed under the
  protein-binding policy): [PMID:19959836 "YidC is essential for the insertion of subunit K"]
- Electrogenic NDH-1 vs NDH-2: [PMID:3122832 "NADH dh II) that reacts with NADH
  exclusively whose turnover does not lead to generation of a H+ electrochemical gradient"]

Decisions:
- GO:0050136 (non-electrogenic) REMOVE: wrong UniRule-to-GO mapping for proton-pumping NDH-1.
- GO:0003954, GO:0016651 MODIFY to GO:0008137 (contributes_to); GO:0030964 rows MODIFY to
  GO:0045271; GO:0016020 MODIFY to GO:0005886; GO:1902600 MODIFY to GO:0015990.
- Menaquinone-8 as acceptor under anaerobiosis is not documented in the cached sources;
  left as a suggested question.
- New publications cached: PMID:21822288, PMID:23417064, PMID:36104567, PMID:12460669.
