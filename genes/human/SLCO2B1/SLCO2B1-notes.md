# SLCO2B1 (OATP2B1 / OATP-B, UniProt O94956) — curation notes

## Summary

SLCO2B1 encodes OATP2B1 (also OATP-B, SLC21A9), a 709-aa, 12-transmembrane-domain
member of the organic anion transporting polypeptide (OATP/SLCO) family
(MFS-type fold; PANTHER PTHR11388; Pfam PF03137 OATP; TCDB 2.A.60 organo anion
transporter family). It is a **sodium-independent, facilitative/secondary-active
plasma-membrane uptake carrier** for amphipathic organic anions. Its best-established
physiological substrates are **steroid sulfate conjugates** — estrone 3-sulfate (E1S/E3S),
dehydroepiandrosterone 3-sulfate (DHEA-S) and pregnenolone sulfate (PregS) — and it
additionally transports bile acids (taurocholate, acidic pH only), eicosanoids
(PGE1, PGE2, PGD2), L-thyroxine, coproporphyrin III, the neuropeptides substance P
and VIP, and a broad range of drugs (statins, fexofenadine, antifolates, etc.).
Transport is markedly **pH-dependent (enhanced at acidic extracellular pH)** and most
likely occurs by **anion exchange** (organic anion uptake coupled to HCO3⁻ / glutamate
efflux). It is expressed at the plasma membrane of hepatocyte sinusoidal/basal membrane,
intestinal enterocytes, placental syncytiotrophoblast (basal), Sertoli cells, brain
capillary endothelium (blood–brain barrier), retina, breast and other tissues.

## Mechanism / molecular function

- Na(+)-independent organic anion transport. [UniProt O94956 CC:FUNCTION, "Mediates
  the Na(+)-independent transport of steroid sulfate conjugates and other specific organic
  anions"]; [PMID:18501590 "uptake of DHEA-S by OATP2B1 was Na(+)-independent"].
- Anion exchange / counter-anion efflux (secondary active, electroneutral). [UniProt
  O94956 CC:FUNCTION, "most likely involves an anion exchange, coupling the cellular uptake
  of organic substrate with the efflux of an anionic compound"; "Hydrogencarbonate/HCO3(-)
  acts as a probable counteranion that exchanges for organic anions"]; [PMID:19129463
  "OATP/Oatp-mediated substrate transport is paralleled by bicarbonate efflux"].
- pH dependence (stimulated at acidic pH). [PMID:14610227 "we observed an increase in V(max)
  with decrease of pH from 7.4 to 5.0"]; [PMID:19129463 "a low extracellular pH stimulated
  transport activity"]. A conserved His in TM3 (His-136) is implicated in pH sensitivity
  (UniProt DOMAIN; PMID:19129463). Note: transport is NOT a classic proton-coupled symport
  in the MCT sense and is Na(+)-, Cl(-)- and glutathione-independent [PMID:14610227
  "OATP-B-mediated uptake of estrone-3-sulfate was independent of sodium, chloride,
  bicarbonate, or glutathione"].
- Multiple binding sites / biphasic (high- and low-affinity) E1S kinetics. [PMID:22201122
  "OATP2B1-mediated uptake of estrone-3-sulfate apparently exhibited biphasic saturation
  kinetics"; "the presence of multiple binding sites on OATP2B1"].
- Structure–function: TM1 and residue W611 (TM11) are critical for transport. [PMID:29871943
  "substitution of L58 with alanine dramatically altered the Km value"]; [PMID:27576593
  "W611 is critical for the function of OATP2B1"].

## Substrates (with ChEBI where used)

- Estrone 3-sulfate (E1S/E3S) — defining, high-affinity substrate; CHEBI:60050.
  [PMID:10873595 "exhibited transport activity for [(3)H]estrone-3-sulfate as a common
  substrate"]; [PMID:11159893 "OATP-B also transported estrone-3-sulfate but not bile salts"].
- DHEA 3-sulfate (DHEA-S) — CHEBI:57905; low affinity (Km>200 µM). [PMID:18501590
  "DHEA-S uptake was... only weakly enhanced in OATP2B1 cells"].
- Pregnenolone sulfate (PregS) — CHEBI:133000. [PMID:16908597 "progesterone enhances the
  OATP2B1-dependent pregnenolone sulfate transport"].
- Taurocholate — CHEBI:36257; transported only at acidic pH. [PMID:14610227 "Transport of
  taurocholic acid and pravastatin by OATP-B was observed only at acidic pH"].
- Prostaglandins PGE1/PGE2/PGD2, L-thyroxine, leukotriene C4, thromboxane B2. [UniProt
  O94956 CC:FUNCTION].
- Coproporphyrin III (OATP biomarker) — CHEBI:131725. [PMID:26383540 "OATP2B1 demonstrated
  meaningful transport of coproporphyrin III (Km = 0.31 µM)"].
- Neuropeptides substance P/TAC1 and VIP (retina/brain). [PMID:25132355 "Substance P and
  vasoactive intestinal peptide were identified as substrates for OATP1A2 and OATP2B1"].
- Drugs: statins (pravastatin, atorvastatin, rosuvastatin, fluvastatin), fexofenadine,
  antifolates (pemetrexed/raltitrexed), aspirin/salicylate, sulfasalazine, glibenclamide,
  etc. [PMID:22021325 "OATP2B1 represents a low-affinity transport route for antifolates"];
  (UniProt DrugBank cross-references).
- Heme / heme analog (newly described). According to PubMed, Unlu et al. 2022 identified
  SLCO2B1 as a plasma-membrane heme importer that enhances cellular iron availability via
  heme oxygenases, predominantly in microglia [PMID:35714613,
  https://doi.org/10.1016/j.molcel.2022.05.024]. UniProt records this as "May act as a heme
  transporter that promotes cellular iron availability via heme oxygenase/HMOX2 and
  independently of TFRC." This paper is not in the local publication cache, so no verbatim
  quote is asserted against it.

## Localization (tissue-dependent; apical vs basolateral debated)

- Plasma / cell membrane, multi-pass. [UniProt CC:SUBCELLULAR LOCATION].
- Hepatocyte basal/sinusoidal membrane. [PMID:11159893 "it is localized at the basolateral
  membrane of hepatocytes"].
- Placental syncytiotrophoblast basal membrane. [PMID:11932330 "at the basal surface of the
  syncytiotrophoblast"].
- Sertoli cell basal membrane (blood–testis barrier). [PMID:35307651].
- Intestinal enterocyte: UniProt flags the apical vs basolateral localization as uncertain.
  Kobayashi et al. report apical [PMID:12724351 "OATP-B was immunohistochemically localized
  at the apical membrane of intestinal epithelial cells in humans"]; Keiser et al. report
  basolateral [PMID:28408210 "Our data provide evidence for a basolateral localization of
  OATP2B1"]. [UniProt CC:CAUTION "The enterocyte localization of SLCO2B1/OATP2B1 remains
  uncertain"]. Both apical and basolateral GO rows are therefore retained.
- Brain capillary endothelium (BBB). [PMID:25132355 "OATP2B1 is expressed in endothelial
  cells of brain capillaries"].

## Protein–protein interactions (C-terminal PDZ motif)

OATP2B1 has a C-terminal class-I PDZ-binding motif; the 20 GO:0005515 "protein binding"
rows (all PMID:36115835, a high-throughput PDZ affinity-mapping interactome) are
interactions with PDZ-domain scaffold proteins (PDZK1, DLG3/4, MPDZ, SCRIB, TJP1,
MAGI1/2, GRIP1/2, PATJ, LNX1/2, APBA1/2, NHERF4, FRMPD2, WHRN, GRID2IP, IL16). These
are bare, uninformative "protein binding" and are removed per the protein-binding policy
(the interactions are not asserted to be false). The functionally characterized one is
PDZK1: [PMID:29752999 "we report an interaction of PDZK1 with OATP2B1, which influences
localization and function of the transporter"]. A more specific MF/mechanism (PDZ-motif–
dependent membrane scaffolding) would be a better annotation than bare protein binding.

## GO ontology note (important for core_functions)

The generic organic-anion MF terms suggested for OATP transporters are **obsolete** in the
current ontology: GO:0015347 (sodium-independent organic anion transmembrane transporter
activity) and GO:0008514 (organic anion transmembrane transporter activity) are both
obsolete with no replacement; GO:0015301 (anion:anion antiporter activity) is also obsolete.
There is currently **no** non-obsolete MF term for steroid-sulfate (E1S/DHEA-S/PregS)
transmembrane transport. Core MF is therefore anchored on the non-obsolete, well-supported
**GO:0015291 secondary active transmembrane transporter activity** (the anion-exchange
mechanism; QuickGO is_a chain: GO:0015291 → GO:0022804 active transmembrane transporter
activity → GO:0022857 transmembrane transporter activity → GO:0005215 transporter activity),
with substrate specificity captured by GO:0015125 (bile acid), GO:0015132 (prostaglandin),
GO:0042910 (xenobiotic), and a **proposed new term** "steroid sulfate transmembrane
transporter activity" for the defining, currently un-termed activity. Supporting BP:
GO:0043252 sodium-independent organic anion transport (non-obsolete).

## Action rationale highlights

- 20× bare GO:0005515 protein binding (PMID:36115835): REMOVE (protein-binding policy).
- GO:0022857 transmembrane transporter activity (16 rows) and GO:0055085 transmembrane
  transport (5 rows): TOO_GENERAL — imprecise on their own once the specific MF
  (GO:0015291) and BP (GO:0043252) terms are asserted; no replacement term per the
  maintainer ruling (2026-11-14).
- GO:0016020 membrane (IEA): TOO_GENERAL (bare "membrane"; plasma membrane asserted).
- GO:0005886 plasma membrane, GO:0009925 basal PM, GO:0016323 basolateral PM, GO:0016324
  apical PM: ACCEPT (direct, well-supported locations; apical/basolateral both kept per
  documented tissue-dependent, debated localization).
- GO:0015291 secondary active transmembrane transporter activity, GO:0043252
  sodium-independent organic anion transport: ACCEPT (core MF and BP).
- GO:0015132 prostaglandin transmembrane transporter activity / GO:0015732 prostaglandin
  transport: KEEP_AS_NON_CORE (genuine but minor substrate class).
- GO:0006805 xenobiotic metabolic process (Reactome TAS): KEEP_AS_NON_CORE (drug-disposition
  role; molecular role is transport, not metabolism).
- GO:0042167 heme catabolic process (Reactome TAS): KEEP_AS_NON_CORE (OATP2B1 imports heme as
  substrate feeding HMOX2; it does not perform catabolic chemistry — PMID:35714613).
- GO:0150104 transport across blood–brain barrier (NAS): KEEP_AS_NON_CORE (tissue-context role
  at BBB endothelium).
- IBA rows (GO:0015291, GO:0016323, GO:0016324, GO:0043252): ACCEPT; the target's own
  UniProtKB:O94956 in WITH/FROM is expected (experimental grounding on the target), not circular.
