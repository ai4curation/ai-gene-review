# PP_3231 (Q88HX2), P. putida KT2440: notes

Dashboard protein: [NZ_BCAQ01000003.1_61](https://gene-annotate-dashboard.kbase.us/review/NZ_BCAQ01000003.1_61)
(P. putida, tier B, aux). It is 100% identical to KT2440 PP_3231 (Q88HX2) over 455/455 residues, an exact
sequence match. The exact-match UniParc entries are not in a reference proteome, so the review is filed on
the reference-proteome entry. The dashboard ID is recorded as an alias.

## Conclusion (exploratory)

PP_3231 is an uncharacterized erythromycin esterase (Ere) family protein: Pfam PF05139, CDD cd14728,
PIRSF036794 and PANTHER PTHR31299. It is predicted to be an active, metal-independent carboxylic-ester
hydrolase. Its substrate is unknown, and nothing shows that it hydrolyses macrolides.

- **Catalytic site intact.** BERIL run `20261030T213637Z-pp3231-catalytic-site` mapped the EreC catalytic
  residues (PMID:33741980) onto PP_3231. EreC E47/H50 (general base)/E78/R261/H289 correspond to
  **E60/H63/E91/R268/H297**, and all five are conserved.
- **Identity to characterized relatives.** PP_3231 is about 24-28% identical to each of them: EreA 28.5%,
  EreB 25.9%, EreC 27.8%, EreD 24.0% and Bcr136 27.7%.
- **The catalytic set does not imply macrolide activity.** Bcr136, from *B. cereus*, keeps the same
  catalytic set but is an esterase that cannot inactivate macrolides (PMID:22303981). PP_3231 is no
  closer to the macrolide-inactivating Eres than to Bcr136. It is chromosomal and conserved in
  Pseudomonas, not a mobile resistance element.
- **Fitness.** The data come from BERIL run `20261030T213340Z-pp3231-fitness`, read from the BERDL lakehouse
  `kescience.fitnessbrowser` because the Fitness Browser site returns 403. No phenotype passes
  |fit| >= 1 and |t| >= 4 in 300 experiments, and PP_3231 has no specific-phenotype entry. Cofitness is
  weak (maximum 0.29). No macrolide was ever tested, so fitness neither supports nor refutes a
  resistance role.
- **Neighbourhood.** PP_3230 (phosphoribosyltransferase-domain protein, + strand, ending at 3667057) is
  adjacent and convergently transcribed to PP_3231 (- strand, 3667319-3668686). STRING links the two at score 973, including by fusion. STRING also links PP_3231 to pcm at 900
  (fusion/neighbourhood). The eggNOG/KEGG "protein-L-isoaspartate O-methyltransferase, EC 2.1.1.77"
  label on the dashboard page fits propagation through such fusions. PP_3231 has no methyltransferase
  domain, and this label should be disregarded.

## GO review (`PP_3231-ai-review.yaml`)

- GO:0046677 response to antibiotic (IEA, InterPro2GO): MARK_AS_OVER_ANNOTATED.
- NEW: GO:0016788 hydrolase activity, acting on ester bonds (ISS).
- NEW: GO:0005737 cytoplasm.
- Core function: predicted Ere-family ester hydrolase, substrate unknown.

## Dashboard verdict

The call is "Erythromycin esterase-like family hydrolase, substrate specificity undetermined."
**Recommended verdict: supported.** Corrected annotation: "Erythromycin esterase (Ere) family hydrolase
with an intact His-based catalytic site; substrate unknown, macrolide activity not demonstrated."

- The call correctly withheld erythromycin esterase activity and a resistance role. Its evidence,
  however, contained no catalytic-residue check and no Ere-family biochemistry. The PaperBLAST hits
  were incidental proteomics mentions.
- GO term scores (`PP_3231-dashboard-predictions-review.yaml`):
  - GO:0016787 hydrolase activity: COR (2).
  - GO:0016788 hydrolase activity, acting on ester bonds: COR (2).
  - GO:0005737 cytoplasm: COR (2).
- All three terms are novel, since GOA holds only the antibiotic-response IEA.

## Caveats

- No Ere-family protein closer than about 28% identity has been characterized. Activity is inferred
  from residue conservation, not measured.
- The alignments are pairwise, not a structure superposition.
- Only the abstract of the Morar et al. 2012 paper (PMID:22303981) was read.
- The physiological substrate may be an endogenous or environmental ester. That is speculation.
