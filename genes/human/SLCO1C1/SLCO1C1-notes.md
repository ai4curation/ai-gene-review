# SLCO1C1 (OATP1C1, Q9NYB5) — curation notes

## Summary / core function

SLCO1C1 encodes OATP1C1 (organic anion transporting polypeptide 1C1; also OATP14,
OATP-F, SLC21A14; "thyroxine transporter"), a 712-aa, 12-transmembrane plasma-membrane
member of the SLCO/OATP (organic anion transporter) family (PANTHER PTHR11388, Pfam
OATP, TC 2.A.60). Unlike most OATPs, which are broad-specificity amphipathic-anion
carriers, OATP1C1 is a **high-affinity, substrate-selective thyroid hormone transporter**
that prefers **T4 (L-thyroxine) and reverse T3 (rT3)** and transports T3 poorly — the
reverse of MCT8/SLC16A2, which prefers T3. Transport is **Na⁺-independent and
facilitative** (OATPs act as electroneutral anion exchangers, coupling substrate uptake to
HCO₃⁻ efflux). OATP1C1 is expressed in brain (capillary endothelium, choroid plexus) and
Leydig cells of testis, and mediates **thyroid hormone entry into the CNS across the
blood-brain and blood-CSF barriers** (together with MCT8), supplying T4 for local
deiodinase conversion.

- High-affinity T4/rT3 transporter: [PMID:12351693 "OATP-F mediates high affinity transport of T(4) and reverse T(3)"] with apparent Km ~90 nM (T4) and ~128 nM (rT3); [PMID:12351693 "Substrates less well transported by OATP-F include T(3), bromosulfophthalein, estrone-3-sulfate, and estradiol-17beta-glucuronide"].
- Substrate selectivity (narrow, unlike other OATPs): [PMID:12351693 "in contrast to most other family members, OATP-F has a more selective substrate preference"]. Structure paper confirms preference: [PMID:40680733 "T4 and rT3, while showing markedly reduced activity for T3"].
- Detailed specificity / deiodinase coupling: [PMID:18566113 "Cells transfected with OATP1C1 showed increased transport of T4 and T4 sulfate (T4S), little transport of rT3, and no transport of T3"] and [PMID:18566113 "Metabolism of T4, T4S, and rT3 by cotransfected deiodinases was greatly augmented in the presence of OATP1C1"] — i.e. OATP1C1 transport is rate-limiting for intracellular TH metabolism (substrate supply to deiodinases), not itself a hormone-generating enzyme.
- BBB role: [PMID:18566113 "OATP1C1 is thought to play a key role in transporting thyroid hormone across the blood-brain barrier"]; UniProt CC:FUNCTION "Facilitates the transport of thyroid hormones across the blood-brain barrier and into glia and neuronal cells in the brain" (ECO:0000269|PubMed:30296914).

## Mechanism: Na⁺-independent, facilitative, pH-insensitive

- OATPs are Na⁺-independent and operate as anion exchangers (HCO₃⁻ counter-flux): [PMID:19129463 "probably by acting as anion exchangers"] and [PMID:19129463 "OATP/Oatp-mediated substrate transport is paralleled by bicarbonate efflux"].
- OATP1C1 is unusual in the family in being **pH-insensitive**, because it lacks the conserved TM3 histidine (His) that confers pH-stimulation on other OATPs: [PMID:19129463 "with the exception of OATP1C1, a low extracellular pH stimulated transport activity"] and [PMID:19129463 "OATP1C1 is lacking a highly conserved histidine in the third transmembrane domain"]. Mutating Gln130→His in OATP1C1 confers gain of pH-sensitivity of E1S transport (UniProt FT MUTAGEN 130).
- Cryo-EM (2025) with T4 bound: OATP1C1 is an MFS-fold transporter in an outward-open conformation; T4 is coordinated by K376 (TM7), N399 (TM8), S562 (TM10): [PMID:40680733 "The K376A mutation completely abolished [125I]-T4 uptake activity without altering the surface expression level compared to WT"]; a lateral gate residue F240 is essential: [PMID:40680733 "The F240A mutation completely abolishes T4 uptake"].

## Localization

- Plasma membrane, multi-pass (UniProt SUBCELLULAR LOCATION; cryo-EM; proteomics). Non-polarized at the BBB endothelium: UniProt note "Expressed in both luminal and abluminal membranes of brain capillary endothelial cells. Localized to the apical membrane and basal surfaces of choroid plexus."
- In rodent cerebral microvessels OATP14/Oatp14 localizes to both luminal and abluminal membranes: [PMID:18687783 "Mct8 and Oatp14 proteins localize to both the luminal and abluminal microvessel membranes"]. Note a human/rodent difference in microvessel enrichment: [PMID:18687783 "OATP14 mRNA and protein are strongly enriched in mouse and rat cerebral microvessels but not in human microvessels"].
- Tissue: UniProt TISSUE SPECIFICITY "Highly expressed in brain and in Leydig cells in testis"; also blood-testis barrier (PMID:35307651).

## C-terminal PDZ ligand / interactome

OATP1C1 ends in ...WPGKETQL (class-I PDZ-binding motif). The GOA GO:0005515 rows
(PMID:24550280 PDZ phage display; PMID:36115835 fragmentomics affinity mapping) are a
large panel of PDZ-domain scaffold interactions (DLG1-5, MAGI1-3, SCRIB, TJP1-3, PATJ,
NHERF2/4 (SLC9A3R2/PDZD3), PDZK1, MPP/MPDZ, GRIP1/2, PARD3, APBA1-3, etc.). These are
consistent with PDZ-motif-mediated membrane targeting/scaffolding but are curated only as
bare `protein binding`; per the project protein-binding policy these uninformative
GO:0005515 rows are REMOVE (removal does not assert the interactions are false). A specific
"PDZ-domain binding" adapter function could be proposed if a dedicated study established it.

## Disease

Biallelic SLCO1C1 loss-of-function (p.D252N) associated with severe brain hypometabolism
and juvenile neurodegeneration / transient congenital hypothyroidism (PMID:30296914,
Strømme et al. 2018, UniProt RN[10]). Supports a non-redundant role (with MCT8) in brain
TH supply.

## GO review decisions (rationale)

- **Core MF = GO:0015349 thyroid hormone transmembrane transporter activity** (IDA x2 PMID:12351693, PMID:18566113; IMP PMID:40680733). QuickGO: GO:0015349 is_a GO:0015291 secondary active transmembrane transporter activity is_a GO:0022857. Same core term carried by MCT8 (SLC16A2) and MCT10 (SLC16A10).
- Candidate family MF terms GO:0015347 (sodium-independent organic anion transmembrane transporter activity) and GO:0008514 (organic anion transmembrane transporter activity) are **both OBSOLETE** in current GO (QuickGO), so they are NOT used in core_functions.
- **Ontology point (suggested_question):** OATP1C1 is experimentally facilitative/Na⁺-independent, yet GO:0015349 is placed under GO:0015291 secondary active transmembrane transporter activity; the standalone IBA GO:0015291 row is therefore term-level TOO_GENERAL (entailed by the core), and the placement question is flagged, consistent with the MCT8/MCT10 reviews.
- **Bile acid transporter rows (GO:0015125 MF, GO:0015721 BP; IBA from PANTHER:PTN000147526):** OATP1C1 is substrate-selective for iodothyronines and has no demonstrated bile-acid transport; these are over-propagations from a broad bile-acid-transporting OATP node → MARK_AS_OVER_ANNOTATED.
- **GO:2000611 positive regulation of thyroid hormone generation (IMP PMID:18566113):** OATP1C1 augments deiodinase-mediated TH metabolism by supplying substrate, but does not itself generate hormone; participation test fails (deiodinases do the chemistry) → MARK_AS_OVER_ANNOTATED (upstream/indirect; better modeled as acts_upstream_of).
- **GO:0150104 transport across blood-brain barrier (NAS x2):** OATP1C1 itself performs the transport step across the barrier → core process, ACCEPT (as for MCT8).
- **GO:0043252 sodium-independent organic anion transport (IBA):** accurate family-level mechanism (TH are organic anions; transport is Na⁺-independent), broader than the TH-specific core → KEEP_AS_NON_CORE.
- Generic ancestors GO:0022857 (MF), GO:0055085 / GO:0015291 → TOO_GENERAL; GO:0016020 membrane → TOO_GENERAL.
