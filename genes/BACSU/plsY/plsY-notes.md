# plsY (yneS, BSU18070; UniProt Q45064) — review notes

Part of projects/LIPID_DIVIDE.md (Part B, acyltransferases that accept both enantiomers).

## Sources and search record (2026-11-02)

- No deep-research provider key was available, so no `plsY-deep-research-<provider>.md` was generated.
- `just mod-description-deep-research BACSU plsY` was run: skipped, "no MOD provider configured for organism 'BACSU'".
- PubMed searches: "Palyzová glycerol phosphate enantiomers phospholipids bacteria" (4 hits; PMID:35767906 is the
  2022 J Chromatogr A paper cited by Rieche et al. as Palyzova et al. 2022); "Bacillus subtilis essential genes
  Kobayashi 2003" (PMID:12682299).
- Newly cached: PMID:35767906 (abstract only), PMID:12682299 (abstract only; gene lists are in the full text, not cached).
- Read: PMID:42286214 (Rieche 2026, full text), PMID:17645809 (Yoshimura 2007, full text), PMID:17557823
  (Paoletti 2007, abstract), PMID:19282621 (Hara 2008, abstract), the UniProt record, and the PTHR10434 PAINT
  file (for the plsC comparison).
- Not cached / not read: García-Domínguez & Devos 2026 (PMID:42965973); Palyzová et al. 2025 (PG stereoisomers in
  B. tequilensis, cited by Rieche); Lu et al. 2006/2007 (S. pneumoniae PlsY biochemistry).

## Function: acyl-phosphate:G3P acyltransferase (first acylation)

- PlsY is the GPAT of the PlsX/PlsY pathway: PlsX converts acyl-ACP to acyl-phosphate, and PlsY transfers the acyl
  group to the sn-1 position of G3P to give LPA [PMID:17557823 "plsY (yneS)
  (acyl-phosphate:glycerol-phosphate acyltransferase)"].
- Acyl donor specificity in B. subtilis membranes: [PMID:17557823 "PlsY was an acylphosphate-specific
  acyltransferase"].
- Genetic loss of activity: [PMID:19282621 "Membrane fractions from B. subtilis cells catalyzed
  palmitoylphosphate-dependent acylation of [14C]-labeled G3P to synthesize [14C]-labeled LPA, whereas those from
  DeltaplsY cells did not."] and [PMID:19282621 "The results indicate unequivocally that PlsY is an acyl-phosphate
  dependent GPAT."]
- In vivo block: [PMID:17645809 "no phospholipids were detectable in yneS-ts cells following a shift to the
  restrictive temperature"]; [PMID:17557823 "The inactivation of PlsY also blocked phospholipid synthesis"].
- Essentiality: the IPTG-dependent yneS strain YNESp fails to grow when depleted, and B. subtilis has no plsB
  [PMID:17645809 "Both plsX and yneS are essential for 1-acyl-G3P synthesis"]; [PMID:17645809 "our results
  demonstrate in vivo that the PlsX/Y pathway is essential for the growth of bacteria lacking plsB"].
  E. coli plsB rescues plsY repression [PMID:19282621 "growth arrests after repression of either a plsY homologue
  or a plsX homologue were overcome by expression of E. coli plsB"].
- G3P is a physiologically limiting substrate in vivo: the yneS-ts phenotype is suppressed by raising intracellular
  G3P (glpD loss, or G3P/glycerol in the medium) [PMID:17645809 "supplementation of the growth medium (LB) with
  0.1% (w/v) G3P, or glycerol, complemented the yneS-ts phenotype"]. This is the only in vivo substrate evidence for
  either enantiomer, and it concerns G3P.
- Regulation: inhibited by acyl-CoA (UniProt, ECO:0000269 PMID:17557823). Two-hybrid suggests PlsX–PlsY
  association [PMID:19282621 "Two-hybrid examinations suggested that PlsY is associated with PlsX"] — not used for a
  GO term (protein-binding policy).

## Location

- Polytopic integral membrane protein: five predicted TM helices (UniProt FT TRANSMEM, ECO:0000255); "a membrane
  protein around 200 amino acids long" [PMID:17645809]. Activity resides in the membrane fraction [PMID:19282621].
  B. subtilis is a monoderm, so membrane = plasma membrane. Rieche: "Although PlsY is located in the membrane"
  [PMID:42286214].

## Stereochemistry (the lipid-divide question)

- In vitro, detergent: BsPlsY and EcPlsY acylate G1P and G3P at similar levels [PMID:42286214 "Remarkably, the
  addition of glycerol 3-phosphate, as well as glycerol 1-phosphate, resulted in the substantial production of
  LPA, with only minor differences in quantities over time."; "it appears there is no major preference of either
  PlsY enzyme for G3P/G1P as substrate"].
- In vitro, liposome-reconstituted (closer to native): G3P clearly preferred, and more so for the Bacillus enzyme
  [PMID:42286214 "However, the levels of (R)-LPA (containing a G3P lipid backbone) were significantly higher
  compared to the levels of (S)-LPA, a difference that was not observed for the enzyme in detergent"; for EcPlsY
  "Again, the levels of produced (R)-LPA were significantly higher than (S)-LPA, but to a much lesser extent as for
  the Bacillus enzyme."]. No kinetic constants were measured [PMID:42286214 "proper kinetic analysis is required"].
- In vivo observation (Řezanka lab only): G1P and G3P detected in B. subtilis and other Gram-positives, and "the
  presence of both enantiomers in the glycerol backbone of some molecular species of PG was revealed"
  [PMID:35767906]. The 4:1 G3P:G1P ratio in that abstract refers to the glycerol phosphates detected, not explicitly
  to the PG backbone; Rieche summarise it as 4:1 to 3:1 for membrane backbones. Abstract only; method details (and
  whether headgroup glycerol was excluded — PG's headgroup glycerol is itself sn-1-linked) could not be checked
  beyond "enzymatic cleavage by phospholipase C". Not independently replicated by another group.
- Inference by Rieche: [PMID:42286214 "As in this microorganism, PlsY is its sole GPAT, the observed in vivo
  heterochirality is in line with our in vitro observations."]. "In line with" is not a demonstration.
- G1P source: B. subtilis AraM/EgsA is the only known G1PDH; it supplies G1P for heptaprenylglyceryl phosphate (PcrB).
  Rieche note G1P biosynthesis routes are incompletely known [PMID:42286214 "At present, there is no other mechanism
  of G1P biosynthesis known"]. No araM knockout or overexpression has been tested for PG backbone chirality.

### Judgement (in vivo vs promiscuity)

Applying the ENZYME_SPECIFICITY tiers: G1P acylation by BsPlsY is not noise-level (near G3P levels in detergent),
so it is not the REMOVE tier. But its physiological use is unshown: (1) the membrane-reconstituted assay shows a
significant G3P preference for the Bacillus enzyme, (2) the only in vivo substrate evidence (yneS-ts suppression)
is for G3P, (3) the in vivo heterochirality rests on one lab's abstract-level report, and (4) the G1P pool feeding
PlsY is unidentified. The logical chain "G1P-backbone PG exists + PlsY is the sole GPAT → PlsY acylates G1P in
vivo" is sound if premise 1 holds, and it is the most parsimonious explanation, but premise 1 is unreplicated.

Decision: propose a GO term (acyl-phosphate glycerol-1-phosphate acyltransferase activity) because GO cannot
currently record even the direct in vitro result (an IDA-quality observation for two orthologs), but do NOT put it
in core_functions and do NOT add a NEW annotation. Record the in vivo question as a BIOLOGY knowledge gap. If an
araM/G1P-dependence experiment confirms G1P-backbone lipids pass through PlsY, the term would become a genuine
secondary (KEEP_AS_NON_CORE-level) function.

## GOA rows (5)

- GO:0043772 IEA (UniRule): ACCEPT, matches the experimentally established reaction.
- GO:0005886 IBA and IEA: ACCEPT (5 TM helices; activity in membrane fraction; monoderm).
- GO:0008654 IEA, GO:0006644 IEA: MODIFY to GO:0006654 phosphatidic acid biosynthetic process (PlsY catalyses the
  first acylation on the way to PA; precise process supported by knockouts).
