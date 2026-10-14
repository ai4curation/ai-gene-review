# phg2 (Q54QQ1, DDB_G0283699) — curation notes

## Deep research status

- 2026-10-05: `just deep-research-falcon DICDI phg2 --fallback perplexity-lite` FAILED.
  Falcon (Edison) returned `402 Payment Required`; fallback provider `perplexity` not
  available in this environment. No deep-research file was produced. Notes below are
  built directly from the cached primary literature in `publications/`.

## Cached literature (full-text status)

| PMID | Topic | full_text_available |
|------|-------|---------------------|
| 15194808 | Gebbie 2004, isolation/phenotype of phg2 | true, but cache only holds abstract + intro (results not cached) |
| 16325504 | Blanc 2005, N-terminal PI(4,5)P2-binding domain | false (abstract only) |
| 16769729 | Kortholt 2006, GbpD-Rap1-Phg2 pathway | false (abstract only) |
| 16987957 | Cherix 2006, Phg2-Adrm1 and development initiation | true |
| 17371831 | Jeon 2007, Rap1/Phg2 and myosin II | true |
| 24587195 | Vu 2014, Pyk3/Phg2 and STATc/PTP3 | true |

## Domain architecture (UniProt)

- 1387 aa; TKL-family Ser/Thr protein kinase domain 807-1072.
- N-terminal PI(4,5)P2/PI(4)P-binding region 81-193 (membrane targeting).
- Ras-association (RA/RBD) region in "core" region; Rap1-binding residues ~594-668,
  Adrm1-binding residues 668-755 [PMID:16987957 "the Phg2 core region comprised two separate binding sites, one for Rap1 (residues 594-668), and one for Adrm1 (residues 668-755"].

## Molecular function

- Ser/Thr kinase: [PMID:15194808 "PHG2 encodes a novel serine/threonine kinase with a ras-binding domain"].
  Evidence for activity is indirect: [PMID:17371831 "Gebbie et al. (2004) demonstrated that the expression of Phg2 in Escherichia coli led to the in vivo phosphorylation of bacterial proteins on Ser/Thr residues"],
  but [PMID:17371831 "However, Phg2 purified from bacteria did not exhibit kinase activity under the conditions assayed"].
  Phg2 is required (RA-domain dependent) for phosphorylation of cortical myosin II heavy
  chain in a cytoskeletal kinase assay; MHCK-A overexpression bypasses this; the assay
  cannot tell direct vs indirect [PMID:17371831 "Our assay does not distinguish between Phg2 directly phosphorylating"].
  Phg2 required for PTP3 S747 phosphorylation [PMID:24587195 "In contrast, Myc-PTP3 S747 phosphorylation was nearly completely abolished in the phg2− strain"],
  and binds PTP3 directly in pull-downs [PMID:24587195 "The pull-down results demonstrate a direct interaction between Myc-PTP3 purified from phg2− cells and recombinant GST-Phg2"].
  No direct in vitro kinase assay on a defined substrate is reported -> candidate experiment.
- Rap1-GTP binding via RA domain: [PMID:16769729 "Phg2, a serine/threonine-specific kinase, directly interacts with Rap1 via its Ras association domain"];
  [PMID:17371831 "We confirmed that the Phg2 RA domain preferentially binds Rap1-GTP over Ras-GTP"].
  GOA also has IPI for RasG and RasS from 15194808 (results not in cache; defer to curator).
- PI(4,5)P2 binding: [PMID:16325504 "we identified a new domain interacting with phosphatidylinositol 4,5-bisphosphate"]; required for membrane recruitment and phagocytic function.
- Adrm1 binding (Y2H + GST pulldown) [PMID:16987957].

## Localization

- Plasma membrane / cortex, translocates to cortex on cAMP stimulation, enriched at
  leading edge of chemotaxing cells [PMID:17371831 "Upon chemoattractant stimulation, GFP-Phg2 rapidly and transiently translocates to the cell cortex"].
  Localization independent of RA domain, PI3K and F-actin.
- GFP-Nt-Phg2 (PIP2-binding domain probe) marks macropinosome/phagocytic cup membranes
  until closure [PMID:16325504].

## Biological processes

- Cell-substrate adhesion, phagocytosis (particle binding), motility, actin organization at
  substrate interface [PMID:15194808]. Note discordant adhesion phenotypes between
  backgrounds: DH1 phg2- less adhesive, KAx-3 phg2- more adhesive [PMID:17371831].
- Chemotaxis: phg2-null cells have broad leading edge, lateral pseudopodia, reduced F-actin
  response, excess cortical myosin II [PMID:17371831].
- Negative regulator of nutrient-controlled initiation of development; cell autonomous;
  kinase domain required; later development morphologically normal [PMID:16987957].
- STATc hyperosmotic response: Phg2 needed for full STATc phosphorylation and STATc target
  gene induction, likely via inhibitory phosphorylation of PTP3 S747 [PMID:24587195].

## Curation decisions summary

- Kinase MF annotations accepted (deferring to IDA curators; domain is canonical).
- protein binding IPIs: Ras/Rap -> MODIFY to small GTPase binding; PTP3 -> phosphatase binding;
  Adrm1 -> REMOVE bare protein binding (interaction itself is real; no informative MF term).
- ARBA "anatomical structure morphogenesis" removed: multicellular morphogenesis is normal
  in phg2 mutants [PMID:16987957].
- Mitotic cytokinesis IMP (15194808): results section not cached, and the independent
  phg2-null strain is "not multinucleated" [PMID:17371831] -> UNDECIDED.
