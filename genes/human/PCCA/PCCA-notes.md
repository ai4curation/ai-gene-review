# PCCA (P05165) review notes

## Schema shape reminders (validated)
- core_functions.directly_involved_in: multivalued list of Term ({id,label}).
- suggested_questions: list of {question: "...", experts: [...]}.
- suggested_experiments: list of {description: "...", hypothesis: "..."}.

## Deep research status
`just deep-research-falcon human P05165` / `uv run scripts/deep_research_wrapper.py`
did NOT produce a `PCCA-deep-research-falcon.md` (falcon wrapper: system python 3.9
chokes on `dict | None`; run via uv started but produced no output/log within the
poll window). Per instructions I did NOT fabricate a `-deep-research-*.md`. Grounded
this review in `PCCA-uniprot.txt`, the seeded GOA, `dismech/kb/disorders/Propionic_Acidemia.yaml`,
and the cached `publications/PMID_*.md`.

## Core biology (verified)
PCCA = biotin-containing alpha subunit of mitochondrial propionyl-CoA carboxylase (PCC),
a biotin-dependent carboxylase. PCC catalyses the first committed, ATP-dependent step of
propionyl-CoA catabolism: propanoyl-CoA + HCO3- + ATP -> (S)-methylmalonyl-CoA + ADP + Pi
(EC 6.4.1.3; RHEA:23720). Holoenzyme = alpha6beta6 dodecamer (~750 kDa) of PCCA (alpha) +
PCCB (beta) [PMID:20725044, PMID:29033250].

- alpha subunit (PCCA) carries the biotin carboxylase (BC) + biotin-carboxyl-carrier
  protein (BCCP) domains; biotin is covalently attached at Lys694 by HLCS; alpha
  catalyses the ATP-dependent carboxylation of biotin. beta subunit (PCCB) supplies the
  carboxyltransferase (CT) activity. UniProt: BC domain 62-509, ATP-grasp 181-378,
  biotinyl-binding 653-728; ACT_SITE 349; ATP/Mg2+/Mn2+ binding sites; biotin at 409/694.
- Substrate: propionyl-CoA (Km 0.29 mM); also butyryl-CoA (-> ethylmalonyl-CoA) at much
  lower rate; minor acetyl-CoA [PMID:6765947, PMID:29033250, UniProt CATALYTIC ACTIVITY].
- Location: mitochondrial matrix (matrix enzyme; loosely bound to inner membrane-matrix
  fraction) [UniProt SUBCELLULAR LOCATION; PMID:10101253; PMID:16023992; PMID:29033250].
  Cleavable N-terminal transit peptide (1-52) [PMID:16023992].
- Pathway: propanoyl-CoA degradation; succinyl-CoA from propanoyl-CoA step 1/3
  (UniPathway UPA00945/UER00908; UniProt PATHWAY). Product methylmalonyl-CoA -> succinyl-CoA,
  a TCA anaplerotic intermediate [PMID:29033250].
- Precursors of propionyl-CoA: cholesterol, valine, odd-chain FA, methionine, isoleucine,
  threonine ("c-VOMIT") [PMID:29033250].

## Disease
Biallelic PCCA (or PCCB) loss-of-function -> propionic acidemia (PA-1, MIM:606054;
MONDO:0011628) [UniProt DISEASE; PMID:10101253; disorder KB]. Autosomal recessive organic
acidemia; toxic organic acid accumulation, metabolic acidosis, hyperammonemia.

## Interactions
- PCCB (P05166): obligate partner in holoenzyme; multiple IntAct/interactome hits
  (PMID:20725044, PMID:33961781, PMID:40205054). These are the biological complex partner.
- MCC / MCCC1 (P23508): IntAct hit (PMID:32296183 HuRI). Cross-carboxylase / likely
  systematic Y2H; MCC is a paralogous biotin carboxylase.
- HLCS / holocarboxylase synthetase (P50747): biotinylates PCCA at K694; PCCA is HLCS
  substrate; enzyme binding (PMID:19157941 uses the PCCA-derived p67 substrate).
- SIRT3/4/5: deacylate/interact with acetylated biotin-dependent carboxylases including
  PCCA (UniProt SUBUNIT; PMID:23438705 - not in GOA).

## Annotation decisions summary
- MF: GO:0004658 propionyl-CoA carboxylase activity (IBA, IEA, IDA PMID:6765947,
  IMP PMID:8434582) -> ACCEPT (core). biotin binding, ATP binding, metal ion binding -> ACCEPT
  (cofactor/substrate, well supported by structure/UniProt features). ligase forming C-C
  bonds (GO:0016885, IEA) -> ACCEPT parent (correct but general). enzyme binding IPI
  PMID:19157941 (HLCS) -> KEEP_AS_NON_CORE (real, but a modification substrate relationship,
  not core enzymatic function).
- CC: mitochondrial matrix (multiple IDA/EXP/IEA/TAS) -> ACCEPT. mitochondrion (IBA/IDA/HTP)
  -> ACCEPT (broader but correct). cytosol (Reactome TAS) -> KEEP_AS_NON_CORE (reflects
  cytosolic apo-precursor before import; not functional site). catalytic complex GO:1902494
  (IPI PMID:20725044) -> MODIFY too general; propose propionyl-CoA carboxylase complex.
- BP: propionate metabolism / propionyl-CoA catabolism. short-chain fatty acid catabolic
  process (GO:0019626, IC) -> MODIFY to propionyl-CoA catabolic process GO:1902859.
  succinyl-CoA biosynthetic process (GO:1901290, IDA PMID:8434582) -> KEEP_AS_NON_CORE
  (downstream product; PCC makes methylmalonyl-CoA, not succinyl-CoA directly). fatty acid
  metabolic process (GO:0006631, NAS) -> KEEP_AS_NON_CORE (broad). branched-chain amino acid
  metabolic process (GO:0009081, NAS) -> KEEP_AS_NON_CORE (Ile/Val/Thr/Met feed in; real
  physiological role but not the direct reaction).
- protein binding (GO:0005515) IPIs: bare term; MARK_AS_OVER_ANNOTATED (per policy, not REMOVE).
  PMID:20725044/33961781/40205054 = PCCB (the genuine complex partner); PMID:32296183 = MCC/HuRI.
</content>
