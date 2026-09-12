# SPCS3 (Signal peptidase complex subunit 3) — review notes

UniProt: P61009 (SPCS3_HUMAN), 180 aa; aka SPC22/23, "Microsomal signal peptidase 22/23 kDa subunit". HGNC. Single-pass type II ER membrane protein (TM 12-32), large C-terminal lumenal domain (33-180). N-glycosylated in vivo.

## Core identity / function
- One of three non-catalytic accessory subunits (SPCS1, SPCS2, SPCS3) of the ER signal peptidase complex. Catalytic = SEC11A / SEC11C.
  - UniProt FUNCTION: "Essential component of the signal peptidase complex (SPC) which catalyzes the cleavage of N-terminal signal sequences from nascent proteins as they are translocated into the lumen of the endoplasmic reticulum (PubMed:27499293, PubMed:34388369). Essential for the SPC catalytic activity, possibly by stabilizing and positioning the active center of the complex close to the lumenal surface (By similarity)." [UniProt P61009]
  - Note: of the three accessory subunits, SPCS3 is described as ESSENTIAL for SPC catalytic activity (vs SPCS1 dispensable, SPCS2 enhancing). Still NOT itself the catalytic subunit — catalysis is in SEC11. It contributes a large lumenal domain and is thought to stabilize/position the active center.
  - UniProt SUBUNIT: "Component of the signal peptidase complex paralog A (SPC-A) ... Within the complex, interacts with SEC11A or SEC11C and SPCS1."
- Cryo-EM: [PMID:34388369] identifies SPCS3 in both SPC paralogs (PDB 7P2P/7P2Q).
- PMID:27499293 (proteolysis IDA): study of regulated alternative translocation of TM4SF20 and CREB3L1 cleavage. Full text not in cache (abstract-only). It is cited by UniProt as experimental FUNCTION support and assigned SPCS3 an IDA "proteolysis" (GO:0006508) annotation by UniProt. Per guidelines, do not REMOVE an experimental IDA from full text we cannot see; treat as supporting the SPC proteolytic role.

## Secondary / non-core
- GO:0019082 viral protein processing (IMP, PMID:27383988): flavivirus host-factor role — "Plays an important role in virion production of flaviviruses such as West Nile virus, Japanese enchephalitis virus, Dengue virus type 2 and Yellow Fever virus." Real experimental phenotype; secondary.
- Numerous bare protein binding IPI entries: intra-complex (SEC11A P67812, SEC11C Q9BY50, SPCS1 Q9Y6A9, SPCS2 Q15005) plus high-throughput interactome captures with disease/aggregation-prone proteins ATXN1 (P54253), HTT (P42858). All bare protein binding -> KEEP_AS_NON_CORE.

## Annotation assessment
- GO:0005787 signal peptidase complex (IBA, IEA, IPI/ComplexPortal) — CORE, ACCEPT.
- GO:0005789 ER membrane (IEA, IDA, ISS, TAS) — CORE localization, ACCEPT.
- GO:0005783 endoplasmic reticulum (IEA ARBA; IDA LIFEdb) — correct but less specific than ER membrane; ACCEPT (IDA fusion-protein localization) / the IEA ARBA also ACCEPT. Keep as supporting localization.
- GO:0016020 membrane (IEA) — generic; KEEP_AS_NON_CORE.
- GO:0045047 protein targeting to ER (IBA) — mis-specified; MODIFY -> GO:0006465 signal peptide processing.
- GO:0016485 protein processing (IDA, ComplexPortal) — ACCEPT; core process (GO:0006465 more specific).
- GO:0006508 proteolysis (IDA, PMID:27499293) — general parent of signal peptide cleavage; SPCS3 essential for SPC catalytic activity but not itself catalytic. ACCEPT as supporting the proteolytic role (experimental IDA; don't downgrade an experimental annotation), but note it's a general term; keep as non-core relative to the specific signal peptide processing. Use KEEP_AS_NON_CORE (general term, redundant with protein processing/signal peptide processing).
- GO:0019082 viral protein processing (IMP, PMID:27383988) — viral host-factor; KEEP_AS_NON_CORE.
- GO:0005515 protein binding (many IPI) — KEEP_AS_NON_CORE (bare protein binding).

## Core function summary
Essential non-catalytic accessory subunit of the ER signal peptidase complex; single-pass type II ER membrane protein with a large lumenal domain that stabilizes/positions the catalytic center, required for SPC activity in signal peptide processing of preproteins. Secondary flavivirus host-factor role in viral protein processing/virion production.

## Falcon deep-research findings (incorporated 2026-06)

- **New, notable:** SPCS3 is an **antiviral restriction factor against chikungunya virus (CHIKV)**, an alphavirus distinct from the previously documented flaviviral host-factor role. In human macrophages, SPCS3 was identified as a CHIKV **E1 glycoprotein-binding** protein with anti-CHIKV activity [PMID:39261662 "signal peptidase complex subunit 3 (SPCS3) and eukaryotic translation initiation factor 3 subunit K (eIF3k) as E1-binding host proteins with anti-CHIKV activities"]. The positively selected E1 residue V220 is required for virion production and its mutation attenuates E1 binding to the restriction factors SPCS3 and eIF3k [PMID:39261662 "E1 residue V220, which has undergone positive selection, is indispensable for CHIKV production in macrophages, as its mutation attenuates E1 interaction with the host restriction factors SPCS3 and eIF3k"]. Falcon reports this anti-CHIKV activity is **peptidase-independent** (SPCS3 overexpression did not alter CHIKV polyglycoprotein cleavage) - i.e. a possible moonlighting function. (Verified PubMed; not cached.)
- HCV assembly interactome: **SPCS3 appears in the HCV E2 accessory interactome**, and the authors note SPCS1/SPCS3 were previously recognized as important for flavivirus particle production and HCV [PMID:38230952]. Reinforces the secondary viral host-factor role already captured (flavivirus IMP, PMID:27383988). (Verified PubMed; not cached.)
- Falcon's structural synthesis (Liaci 2021 = PMID:34388369, already cited) details SPCS3-specific architecture: a luminal **beta-sandwich (ASF1-like) domain** that "embraces" SEC11 and stabilizes the Ser-His-Asp catalytic triad, plus TM helices forming the inner lining of the membrane-thinning "TM window" (~26% thinning; ~15 A window). SPCS3 also reported highly N-glycosylated (Asn~141). Consistent with existing "essential for SPC catalytic activity by stabilizing/positioning the active center"; no new reference needed.
- The "SPC quality-control" framing (SEC11A/C + SPCS3 as the catalytic core; SPCS1 as recruitment/exosite for cryptic noncanonical sites; ~1500 candidate substrates) derives from Zanotti 2023, a PhD thesis (doi:10.11588/heidok.00033417, no PMID, not peer-reviewed primary literature). Not added as a reference (unverifiable as PMID); logged here only.
- Background reviews (Verhaegen & Vermeire 2024 npj Viruses) note SPCS1 and SPCS3 identified as essential flavivirus host factors and list ER-targeted antiviral inhibitors (cavinafungin, cotransins, apratoxins); background only, no gene-specific SPCS3 finding beyond what is captured. Not added.
