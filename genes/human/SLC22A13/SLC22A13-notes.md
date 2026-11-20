# SLC22A13 (OAT10 / ORCTL3) — curation notes

UniProt: Q9Y226 (S22AD_HUMAN). HGNC:8494. 551 aa, 12-TM MFS protein, SLC22/organic
cation transporter family (TC 2.A.1.19). Chromosome 3p21.3.

## Identity and nomenclature
- Originally cloned as **ORCTL3** (organic cation transporter-like 3) / OCTL1 by homology
  to organic cation transporters [PMID:10072596]. Functionally re-characterized and renamed
  **hOAT10** (organic anion transporter 10) once anion transport was shown [PMID:18411268
  "Hence, hORCTL3 is an organic anion transporter, and we renamed it hOAT10"].

## Core molecular function: apical renal anion antiporter
- **Na+-independent organic anion/anion exchanger (antiporter).** Takes up nicotinate, urate,
  p-aminohippurate and orotate in exchange for intracellular anions. UniProt CC:FUNCTION:
  "Anion antiporter that mediates the transport of urate, orotate and nicotinate in exchange
  for organic or inorganic anions."
- UniProt curates Rhea anion-exchange catalytic activities: urate(out)+(S)-lactate(in),
  urate(out)+succinate(in), urate(out)+glutathione(in), nicotinate(in)+urate(out),
  orotate(out)+carboxylate(in) — all ECO:0000269/ECO:0000305 from the four functional papers.
- **High-affinity nicotinate transporter** [PMID:18411268 "hOAT10-expressing Xenopus laevis
  oocytes showed uptake of [(3)H]nicotinate, [(3)H]p-aminohippurate, and [(14)C]urate";
  "Nicotinate transport by hOAT10 ... saturable with Michaelis constants (K(m)) of 22 and 44
  microm ... hOAT10 may be the molecular equivalent of the postulated high affinity nicotinate
  transporter in kidneys and intestine"]. Km ~22 µM (oocytes), ~44-48 µM (Caco-2).
- **Urate transporter** (low-affinity): Km 558 µM (pH 6.4) [PMID:35462902]; urate uptake
  trans-stimulated by L-lactate, pyrazinoate, nicotinate; urate(-)/glutathione exchange
  detected [PMID:18411268 "hOAT10-mediated [(14)C]urate uptake was elevated by an exchange with
  l -lactate, pyrazinoate, and nicotinate. Surprisingly, we have detected urate(-)/glutathione
  exchange by hOAT10"]. Cyclosporine A enhanced urate uptake (molecular basis for CsA-induced
  hyperuricemia).
- **Orotate transporter** [PMID:35144162 "human OAT10 has been demonstrated to operate for
  orotate transport"]. Biphasic kinetics (high-affinity Km 36.3 µM; low-affinity Km 3.65 µM per
  UniProt note) and Cl−-dependent; "Orotate transport by OAT10 was found to be kinetically
  saturable with a biphasic characteristic and dependent on Cl-." The rat ortholog does NOT
  transport orotate (species difference). No specific GO term exists for orotate transport
  (QuickGO search returns none) → proposed_new_term.

## Location
- **Apical (brush-border) membrane of renal proximal tubular cells.** UniProt CC:SUBCELLULAR
  LOCATION: "Apical cell membrane"; multi-pass membrane protein. Immunohistochemistry on human
  kidney localizes OAT10 to the apical side of proximal tubular cells [PMID:35462902;
  PMID:31780526 "reported expression of OAT10 on the apical membrane of the renal proximal
  tubular cells"]. Strongly expressed in kidney (proximal convoluted tubule, cortical collecting
  duct), weaker in brain, heart, intestine.

## Physiology: renal urate reabsorption and gout
- OAT10 acts as a **renal urate re-absorber** on the apical membrane, a URAT1-like role
  [PMID:35462902 title "OAT10/SLC22A13 Acts as a Renal Urate Re-Absorber"; "our data indicate
  that OAT10 is involved in the renal urate reabsorption in renal proximal tubules from urine"].
- The dysfunctional missense variant **R377C (rs117371763; c.1129C>T)** is an almost-null urate
  transporter and is associated with **lower gout risk** (OR=0.67) and lower serum urate
  [PMID:31780526 "the urate transport activity of R377C variant-expressing cells was close to
  that of mock cells, demonstrating that this variant disrupts OAT10's function as a urate
  transporter"; "we conclude that OAT10 is a urate reabsorption transporter on the apical side
  of the renal proximal tubular cells"]. R377C has no effect on protein level or localization.
- OAT10 is a potential urate-lowering drug target; inhibited by losartan and lesinurad
  [PMID:35462902].
- UniProt: "Shows similar transport characteristics as the urate/orotate renal antiporter
  SLC22A12/URAT1 and may act as a compensator of SLC22A12/URAT1 in certain conditions."

## The ORCTL3 "anticancer gene / apoptosis" literature — critical appraisal
- **PMID:19282870**: ectopic overexpression of ORCTL3 induces apoptosis specifically in
  transformed/tumor cells (H-ras/v-src NRK, HeLa, HEK293T, prostate lines) but not normal cells,
  via an ER-stress mechanism; the ORCTL3-ECFP fusion localized to **ER, Golgi and plasma
  membrane** ["This fusion protein was found at the endoplasmic reticulum (ER), the Golgi and the
  plasma membrane ... indicating that the ORCTL3 protein transport conforms to the known internal
  route of plasma membrane proteins"]. The authors explicitly state apoptosis is **independent of
  transporter activity** and the ER/Golgi signal is biosynthetic transit of a plasma-membrane
  protein, not functional residence. ORCTL3 is down-regulated in renal carcinomas.
  → ER and Golgi IDA rows reflect overexpressed-fusion transit through the secretory pathway, not
  endogenous organelle residence (CLAUDE.md "ER: transit is not residence") → MARK_AS_OVER_ANNOTATED.
  → The paper has **no T-cell experiments**; the GOA term GO:0002854 "positive regulation of T
  cell mediated cytotoxicity directed against tumor cell target" is a mis-assignment (the
  phenomenon is cell-autonomous, overexpression-induced tumor-specific apoptosis) → REMOVE +
  source_defect.
- **PMID:24769897**: ORCTL3 binds and inhibits **stearoyl-CoA desaturase-1 (SCD1)**, reducing the
  desaturation index (18:1n-9/18:0), as the mechanism of its tumour-specific apoptosis; human
  ORCTL3 is notably weaker than mouse ORCTL3 ["human ORCTL3 interacted slightly weaker than mouse
  ORCTL3 with SCD1"; "the degree of cell death attainable with human ORCTL3 remained significantly
  below the mouse ORCTL3"]. The SCD1 interaction/desaturation-index reduction is a real
  measurement but observed under overexpression and is peripheral to the renal transport core →
  KEEP_AS_NON_CORE for GO:0045922 negative regulation of fatty acid metabolic process.

## GO term obsolescence (QuickGO-verified 2026-11)
- OBSOLETE (avoid): GO:0008514, GO:0015347, GO:0015301 (organic-anion grouping MF terms),
  GO:0015711 (organic anion transport BP). Do NOT re-propose a grouping NTR.
- NON-OBSOLETE live terms used: GO:0015143 (urate transmembrane transporter activity),
  GO:0090416 (nicotinate transmembrane transporter activity), GO:0015297 (antiporter activity),
  GO:0015747 (urate transport), GO:2001142 (nicotinate transport), GO:0016324 (apical plasma
  membrane).

## Core functions summary
1. Apical renal organic-anion/anion antiport (mechanism: GO:0015297 antiporter activity;
   substrates urate, nicotinate, orotate, p-aminohippurate exchanged for intracellular
   lactate/succinate/glutathione/nicotinate).
2. Urate transmembrane transport (GO:0015143) → renal urate reabsorption (gout-relevant).
3. Nicotinate transmembrane transport (GO:0090416) — high-affinity renal/intestinal nicotinate
   uptake, feeding NAD+ salvage.
4. Orotate transmembrane transport (no GO term; proposed_new_term).
