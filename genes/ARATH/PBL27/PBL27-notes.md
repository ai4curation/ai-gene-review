# PBL27 (At5g18610, Q1PDV6) curation notes

## Sources used
- Falcon deep research: `PBL27-deep-research-falcon.md` (used for orientation; claims below traced to cached primary papers).
- PMID:24750441 (Shinya et al. 2014, Plant J) - abstract only cached.
- PMID:27679653 (Yamada et al. 2016, EMBO J) - full text cached.
- PMID:31524595 (Liu et al. 2019, eLife) - full text cached (newly fetched).
- PMID:29907700 (Rao et al. 2018, Plant Physiol) and PMID:29871986 (Bi et al. 2018, Plant Cell) - abstract only (newly fetched); both PMIDs resolved from DOIs via NCBI esearch.
- PMID:32385340 (Uemura et al. 2020, Commun Biol) - full text cached.
- PMID:14506206 (Nuhse et al. 2003) - abstract only; plasma membrane phosphoproteomics (HDA).

## Identity
RLCK subfamily VII (VII-1) member, PBS1-like; Arabidopsis homologue of rice OsRLCK185.
UniProt: palmitoylation at Cys-4/Cys-7 (by similarity) anchors it at the plasma membrane;
catalytic activity (Ser and Thr, EC 2.7.11.1) with ECO:0000269 from PMID:27679653.

## Chitin -> MAPK branch
- PBL27 is "an immediate downstream component of the chitin receptor CERK1" and CERK1
  "preferentially phosphorylated PBL27 in comparison to BIK1" [PMID:24750441].
- Knockout suppresses chitin-induced MPK3/6 activation, callose deposition and resistance
  to fungal and bacterial infection; flg22 contribution "very limited" [PMID:24750441].
- "PBL27 phosphorylates MAPKKK5 in a CERK1‐dependent manner." [PMID:27679653]
- "PBL27 directly phosphorylated only the C‐terminal domain of MAPKKK5" [PMID:27679653];
  phosphosites S617, S622, S658, S660, T677, S685; "The S622A mutation strongly reduces
  phosphorylation by PBL27." -> Ser and Thr substrate residues: protein Ser/Thr kinase.
- Interacts with MAPKKK5 at the PM: "PBL27 interacts with MAPKKK5 at the PM where CERK1 and
  PBL27 form the complex" [PMID:27679653]; weaker interaction with MAPKKK3 (Y2H) [PMID:27679653].
- PBL27 Alternaria phenotype is cited, not re-tested, in PMID:27679653 ("As reported
  previously, lyk5, cerk1, and pbl27 mutations reduce resistance to the fungal pathogen
  Alternaria brassicicola").

### Dispute
- Rao et al. 2018: "RLCK VII-4 members were required for the chitin-triggered activation of
  MAPK" [PMID:29907700]. Per deep research (full text not cached), the pbl27 allele and an
  rlck vii-1 quintuple mutant did not show reduced chitin MAPK activation.
- Bi et al. 2018: RLCK VII members "directly phosphorylate MAPKKK5 Ser-599, which is required
  for pattern-triggered MPK3/6 activation" [PMID:29871986]; PBL27 is not the dominant
  MAPKKK5 kinase in their hands (deep research; full text not cached).
- Conclusion: biochemical activity (MAPKKK5 phosphorylation) is solid; quantitative genetic
  requirement for MAPK activation is contested and likely redundant with RLCK VII-4.
  Keep the GOA IMP MAPK row (curators read full text) but flag the dispute.

## Guard-cell branch (SLAH3)
- "PBL27 has the capacity to phosphorylate SLAH3, of which S127 and S189 are required to
  activate SLAH3." [PMID:31524595]
- "We conclude that PBL27 is the primary kinase that directly phosphorylates SLAH3 for the
  release of anions and functions in an activation status-dependent manner regulated by
  CERK1." [PMID:31524595]
- "consistently stomata of pbl27 mutants showed no closure to chitin either" [PMID:31524595]
- pbl27 does not affect chitin ROS burst; PBL27 does not interact with RBOHD [PMID:31524595],
  consistent with the BIK1-type branch handling ROS.
- Not in GOA -> NEW GO:0090333 regulation of stomatal closure. PBL27 performs the
  phosphorylation step that activates the channel (participation), and the comparator RLCK
  BIK1 carries regulation of stomatal movement for its OSCA1.3 phosphorylation.

## Herbivore branch (HAK1)
- AtHAK1 (At1g06840) interacts with PBL27 (AlphaScreen, BiFC, co-IP) [PMID:32385340];
  pbl27 and hak1 reduce Fr-alpha-induced ethylene/PDF1.2 and herbivore resistance. No
  substrate shown downstream. Non-core; not proposed as NEW.

## Other
- ALR1/PSKR1 phosphorylation in aluminium signalling (Xu 2025, Nature Plants) mentioned only
  in deep research; not cached, not used for annotation.

## Decisions summary
- Protein kinase rows accepted; IDA generic kinase -> MODIFY to Ser/Thr kinase.
- protein binding rows (CERK1 x3, MAPKKK3, MAPKKK5, HAK1): MARK_AS_OVER_ANNOTATED, consistent
  with BIK1 review; interactions are enzyme-substrate relations captured by the kinase MF.
- innate immune response (IMP) -> MODIFY to GO:0002752 cell surface pattern recognition
  receptor signaling pathway (PBL27 is a relay kinase in the CERK1 PRR pathway; matches
  module and CERK1 review).
- Defence response to fungus/bacteria and regulation-of-defence rows: KEEP_AS_NON_CORE
  (phenotype-level; necessity rather than mechanism).
