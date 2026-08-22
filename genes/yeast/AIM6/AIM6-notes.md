# AIM6 (YDL237W) — curation notes

Journal of research for the AI GO-annotation review of *Saccharomyces cerevisiae* AIM6.

## Identity (verified from UniProt record)
- UniProt: **Q07716** (AIM6_YEAST), reviewed, 390 aa, PE=1 (evidence at protein level).
- SGD systematic name: **YDL237W**; standard name **AIM6**; SGD:S000002396.
- Name: "Altered inheritance of mitochondria protein 6" (UniProt) / "Altered Inheritance rate of Mitochondria" (SGD). The AIM series was named in the mitochondrial-biogenesis screen of [PMID:19300474].
- Flags: **Precursor**; predicted N-terminal **signal peptide 1–17** (ECO:0000255), mature chain 18–390 (PRO_0000242484). Keyword: Signal.
- Family: "Belongs to the AIM6 family" (a UniProt family essentially defined by this protein and close fungal orthologs, not a characterized enzyme family).

## Domain / fold reasoning (done inline from UniProt DR lines + InterPro API)
InterPro domain matches for Q07716 (from InterPro REST API):
- **IPR017946** homologous_superfamily — "PLC-like phosphodiesterase, TIM beta/alpha-barrel domain superfamily", residues **117–385**.
- **IPR039559** domain — "Altered inheritance of mitochondria protein 6, PI-PLC-like catalytic domain", residues **115–382**.
- **IPR051236** family — "Histone acetyltransferase RTT109-like", residues 80–387.
- CDD: **cd08577** = "PI-PLCc_GDPD_SF_unchar3" ("**Uncharacterized** hypothetical proteins similar to the catalytic domains of Phosphoinositide-specific phospholipase and Glycerophosphodiester phosphodiesterases").
- SUPFAM: SSF51695 (PLC-like phosphodiesterases). PANTHER: PTHR31571 "ALTERED INHERITANCE OF MITOCHONDRIA PROTEIN 6".

Interpretation:
- The mature protein is essentially one domain adopting the **PLC-like phosphodiesterase TIM (β/α)8-barrel fold** — the fold shared by phosphoinositide-specific phospholipase C (PI-PLC) and glycerophosphodiester phosphodiesterases (GDPD). This is the structural basis for the IEA MF annotation GO:0008081 "phosphoric diester hydrolase activity".
- **InterPro itself states "The function of Aim6 is not clear"**, and the CDD source group is explicitly labelled "uncharacterized". So the phosphodiesterase activity is a **fold-level homology prediction only**, from a divergent, uncharacterized subgroup — not an experimentally established activity, and the substrate/specificity is unknown.
- The IPR051236 "Histone acetyltransferase RTT109-like" family match is a **noisy/over-broad PANTHER grouping**; it does NOT imply AIM6 is a histone acetyltransferase (RTT109 is nuclear; AIM6 carries a secretory signal peptide, incompatible with a nucleosomal HAT). Do not annotate to acetyltransferase on this basis.

Inline check of catalytic residues (script over the sequence): the catalytic-domain region carries conserved His/Asp residues consistent with the fold, notably an **"HSHND" motif at H118-S119-H120-N121-D122** (GDPD/PLC-superfamily catalytic-type residues sit at the N-terminal end of the barrel), plus H156 (GHNEAY), H313/H318 (HCGSDHWK), H343 (GAHAL). So catalytic machinery is at least partially retained at the fold level — enough that the phosphodiesterase prediction cannot be confidently *refuted* as a dead pseudoenzyme, but there is no positive evidence for any catalytic activity, substrate, or the "lipid metabolic process" leap.

## What is KNOWN (experimental)
- **Disruption phenotype: impairs respiratory growth** (UniProt CC, ECO:0000269|PubMed:19300474). AIM6/YDL237W was one of the previously uncharacterized ORFs whose deletion gave a mitochondrial-biogenesis/petite phenotype in the Hess et al. quantitative screen. Note: the per-gene datum sits in that paper's Table S2 (not in the cached full text); the cached full text establishes the **screen and its phenotype interpretations** but does not name YDL237W/AIM6 in the running text.
  - [PMID:19300474 "we have identified 100 proteins whose deficiency alters mitochondrial biogenesis and inheritance in Saccharomyces cerevisiae"]
  - The screen explicitly cautions the phenotype does not prove a direct mitochondrial molecular role: [PMID:19300474 "many proteins not localized to mitochondria are vital for regulating mitochondrial function and biogenesis"] and [PMID:19300474 "raise the possibility that these mutants are somehow indirectly affecting biogenesis"].
- SGD locus summary (web, 2026): **"Protein whose biological role and cellular location are unknown."** Verified ORF, non-essential. Additional deletion phenotypes catalogued at SGD (from various high-throughput datasets): inability to grow on glycerol, increased competitive fitness on fermentable medium, altered heat-stress survival, decreased H2S production with excess cysteine — all HTP, none establishing a molecular function.
- Protein-level evidence (PE=1): detected by mass spectrometry ([PMID:29897761], proteogenomics of S. cerevisiae) and present in abundance datasets (~6,000 molecules/cell per SGD). Confirms the protein exists and is expressed; says nothing about function.
- **ER localization in the SWAp-Tag/LoQAtE datasets.** The AIM6/YDL237W LoQAtE record
  was manually checked on 2026-08-22. N-terminal NOP1pr-GFP and TEF2pr-mCherry constructs
  were classified as ER, and the N-terminal NATIVEpr-GFP construct (which restores the
  native promoter and native signal peptide) was classified as ambiguous/ER. The original
  C-terminal GFP signal was below threshold. The native-promoter result and the independent
  N-terminal constructs agree with AIM6's predicted signal peptide, so ER localization is
  supported, but it remains high-throughput tag-based evidence rather than proof of topology
  or catalytic residence. [PMID:29988094 describes the SWAT libraries and cautions that 636
  proteins differed between N- and C-terminal tagging; PMID:24150937 describes the LoQAtE
  atlas and its gene-level localization records.]

## What is NOT known
- **Molecular function**: unknown. Only a fold-based PI-PLC/GDPD-like phosphodiesterase *prediction* (IEA). No demonstrated catalytic activity, no substrate, no assay. The specific claim "phosphoric *diester* hydrolase" and the "lipid metabolic process" inference (borrowing PI-PLC's lipid substrate) are unsupported over-reaches from the divergent fold.
- **Cellular localization/topology**: ER localization is supported by the high-throughput
  SWAp-Tag/LoQAtE datasets and is consistent with the predicted N-terminal signal peptide.
  The protein's membrane topology, signal-peptide cleavage, and precise ER subcompartment
  remain unknown. The N- versus C-terminal tag discrepancy warrants caution, but the data no
  longer support describing AIM6's cellular location as wholly unknown.
- **Biological role / mechanism behind the AIM screen phenotype**: unknown. The petite/respiratory phenotype places AIM6 loss upstream of normal respiratory competence, but whether this is a direct role in mitochondrial biogenesis or an indirect/pleiotropic effect (e.g. via a secretory-pathway or lipid-related activity) is undetermined.

## Annotation plan
GOA has 5 annotations:
1. GO:0006629 lipid metabolic process — IEA (InterPro, IPR017946).
   KEEP_AS_NON_CORE: retain the intended superfamily prediction, since PI-PLC and GDPD branches
   both participate in lipid metabolism and ER localization is compatible, but no AIM6 lipid
   substrate or metabolic effect has been demonstrated.
2. GO:0008081 phosphoric diester hydrolase activity — IEA (InterPro, IPR017946).
   KEEP_AS_NON_CORE: the PLC/GDPD-like fold and retained candidate catalytic scaffold make the
   broad activity a defensible computational prediction, but the AIM6-specific family has no
   experimental catalytic anchor. Do not narrow to PI-PLC or GDPD activity.
3. GO:0003674 molecular_function — ND (SGD). ACCEPT as the historical root/ND placeholder;
   the superfamily-based molecular-function prediction remains unassayed.
4. GO:0005575 cellular_component — ND (SGD). ACCEPT as the historical root/ND placeholder,
   now superseded by a proposed high-throughput ER annotation.
5. GO:0008150 biological_process — ND (SGD). ACCEPT (root/ND placeholder).
6. GO:0005783 endoplasmic reticulum — proposed NEW/HDA from PMID:29988094 and the gene-level
   LoQAtE record. The native-promoter and two additional N-terminal variants agree on ER;
   retain a tag-orientation caveat.

core_functions: record the experimentally supported ER location and the PLC/GDPD-like fold, while
keeping the MF/BP claims explicitly predicted and unverified. Knowledge gaps remain the primary
deliverable.

## Deep research provenance
Falcon deep research was attempted twice (`just deep-research-falcon yeast AIM6`) and both attempts
failed: first attempt timed out after 600s (Edison/falcon endpoint) and the perplexity-lite fallback
returned HTTP 401 (quota exceeded); retry disconnected (RemoteProtocolError, exit 143). No
`AIM6-deep-research-*.md` file was produced, and per project policy I did NOT fabricate one. This
review is therefore grounded in: the UniProt record (Q07716), the GOA TSV, the cached full text of
PMID:19300474 (verbatim-quoted), and manually verified public resources (SGD locus page, InterPro
IPR039559 / IPR017946 REST API, CDD cd08577, PANTHER PTHR31571). All non-PMID assertions are recorded
here with their source.

OpenScientist hypothesis research was subsequently run through the public
`just gene-hypothesis-research` wrapper for GO:0008081. It independently concluded that the term is
partially supported as a computational prediction and should be retained without upgrade or
narrowing. Its numerical AlphaFold-distance and pan-family audit claims were not accompanied by
executable analysis provenance, so those details remain leads rather than independently reproduced
facts. The report also missed the AIM6-specific LoQAtE ER calls; the review corrects that omission
using PMID:29988094, PMID:24150937, and the gene-level atlas record.
