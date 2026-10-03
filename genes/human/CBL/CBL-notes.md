# CBL (P22681) review notes

## 2026-10-01 — initial review (context: FGFR signaling module)

### Core biology
- RING E3 that recognises pTyr substrates via its TKB (SH2-like) domain and activates E2 via RING
  [PMID:10514377 "The c-Cbl protein acted as an E3 that can recognize tyrosine-phosphorylated substrates, such as the activated platelet-derived growth factor receptor, through its SH2 domain and that recruits and allosterically activates an E2 ubiquitin-conjugating enzyme through its RING domain."]
- Autoinhibited; linker Tyr371 phosphorylation activates
  [PMID:22266821 "Cbl ubiquitination activity is stimulated by phosphorylation of a linker helix region (LHR) tyrosine residue."]
- TKB pTyr recognition structures (SPRY2, SPRY4, EGFR, SYK, MET)
  [PMID:18273061 "An obligatory, intrapeptidyl H-bond between the phosphotyrosine and the conserved asparagine or adjacent arginine is essential for binding and orients the peptide into a positively charged pocket on c-Cbl."]
- EGFR: ligase activity drives coated-pit entry [PMID:15465819 "Both the ubiquitin ligase activity of c-Cbl and the UIM of Eps15 were necessary for plasma membrane recruitment of Eps15 and entry of ligand-bound EGFR into coated pits and vesicles containing Eps15."]; RASopathy mutants impair it [PMID:25178484 "the p.K382E, p.D390Y, and p.R420Q lesions impaired CBL-mediated EGFR ubiquitylation and degradation"]
- Proline-rich region binds SH3 adaptors [PMID:15090612 "CIN85 src homology 3 domains specifically bind to a proline-arginine (PxxxPR) motif in Cbl"]
- T cells / LAG3 [PMID:40101708 "LAG3 ubiquitination, mediated redundantly by the E3 ligases c-Cbl and Cbl-b, disrupted the membrane binding of the juxtamembrane basic residue-rich sequence"]

### FGFR / FRS2 evidence (for modules/fgfr_signaling.yaml)
- Newly fetched, PubMed-verified via esearch/esummary: PMID:11997436, PMID:18374639, PMID:21596750.
- FRS2alpha-GRB2-CBL ternary complex; CBL ubiquitinates FGFR and FRS2alpha
  [PMID:11997436 "Grb2 bound to tyrosine-phosphorylated FRS2 alpha forms a ternary complex with Cbl by means of its Src homology 3 domains resulting in the ubiquitination of fibroblast growth factor (FGF) receptor and FRS2 alpha in response to FGF stimulation."]
  Caveat: [PMID:11997436 "the partial inhibition of FGF receptor down-regulation in FRS2 alpha-/- cells indicates that the attenuation of signaling by FGF receptor is regulated by redundant or multiple mechanisms."]
- FGFR2-CBL in rafts (osteoblasts) [PMID:18374639 "FGFR2 and Cbl interact in raft micro-domains at the plasma membrane."]; there CBL ubiquitinates PI3K rather than (only) the receptor.
- TKB-dead G306E reduces FGFR2/PDGFRA ubiquitination in hMSCs [PMID:21596750 "decreased Cbl-mediated PDGFRα and FGFR2 ubiquitination"].
- FGFR3: TD-I mutant ubiquitylation appeared c-Cbl independent [PMID:17509076 "ubiquitylation was markedly increased but apparently independent of the E3 ubiquitin-ligase casitas B-lineage lymphoma (c-Cbl)"].
- Proposed NEW GO:0040037 negative regulation of FGFR signaling pathway (IDA, PMID:11997436).
  Participation: CBL catalyses the ubiquitination. Comparator: CBL already carries GO:0042059 for EGFR;
  SPRY1/2 and SULF1 carry GO:0040037 (QuickGO, human/mouse).

### Decisions worth flagging
- No NOT annotations in GOA for CBL.
- 122 'protein binding' IPI rows: MODIFY to specific binding terms where the paper defines the binding mode
  (SH3, SH2, pTyr, RTK, PTK, PI3K p85, 14-3-3, E2); REMOVE for high-throughput screens and uninformative cases.
- PMID:5668240 (IPI with INPPL1) is a 1968 peracetic acid paper: wrong identifier.
- GO:0043066 IMP (PMID:18070883): REMOVE — full text shows SPRY2 sequesters CBL to preserve survival; CBL acts in the
  pro-apoptotic direction [PMID:18070883 "endogenous hSPRY2-mediated regulation of apoptosis requires c-Cbl and is manifested by the ability of hSPRY2 to sequester c-Cbl and thereby augment signaling via growth factor receptors."]
- GO:0051897 IMP (PMID:17003487): MODIFY to negative regulation (GO:0051898) [PMID:17003487 "Twist haploinsufficiency results in decreased Cbl-mediated PI3K degradation in osteoblasts, causing PI3K accumulation and activation of PI3K/Akt-dependent osteoblast growth."]
- GO:0045742 positive regulation of EGFR signaling (Reactome PTK6 pathway): REMOVE, inverts CBL's role.
- Rat Compara 'response to X' IEAs: REMOVE (expression-type annotations; no mechanism).
- GO:0050821 protein stabilization (IDA PMID:40101708 + ARBA IEA): UNDECIDED; abstract says ubiquitination does not cause degradation.
