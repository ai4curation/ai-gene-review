# ATP4 (PfATP4, PF3D7_1211900, UniProt A0A143ZZK9) - curation notes

**Automated deep research was unavailable in this environment (Falcon auth failure,
invalid OpenAI key). These notes are a manual literature review** based on the UniProt
record and the cached full-text/abstract publications in `publications/`.

## Identity and family

- 1264 aa P2-type (cation transport, TC 3.A.3) ATPase with N (nucleotide-binding), P
  (phosphorylation, PROSITE PS00154 DKTGT motif) and A (actuator) domains and a
  10-helix transmembrane domain. PANTHER PTHR43294:SF20 (Na+/K+-ATPase alpha
  superfamily). UniProt (Swiss-Prot, reviewed 2024) names it "P-type
  sodium-transporting ATPase4", EC 7.2.2.3.
- Historically annotated as a Ca2+-ATPase. Dyer et al. 1996 cloned it as PfATPase4 and
  judged it "most analogous to Ca2+ ATPases of the endoplasmic reticulum"
  [PMID:8813672 "reveals that PfATPase4 is most analogous to Ca2+ ATPases of the endoplasmic reticulum"].
  Krishna et al. 2001 expressed it in Xenopus oocytes and reported a Ca2+-dependent
  ATPase activity [PMID:11145964 "The Ca(2+)-dependent ATPase activity of PfATP4 is
  stimulated by a much broader range of [Ca(2+)](free)"] (abstract only).
- That Ca2+ assignment was not confirmed: [PMID:23414762 "There is evidence for it having an associated Ca2+-dependent ATPase activity (Krishna et al., 2001); however, this has not been confirmed (Rottmann et al., 2010), and a Ca2+ transport function has not been demonstrated directly."]
  Spillman et al. explain the history: ENA Na+-ATPases are close relatives of SERCA/PMCA
  [PMID:23414762 "The ENA ATPases are closely related to sarcoplasmic/endoplasmic reticulum Ca2+-ATPases (SERCA) and plasma membrane Ca2+-ATPases (PMCA), leading some Na+-ATPases within this family to be misannotated as Ca2+-ATPases"].

## Function: Na+ efflux pump of the parasite plasma membrane

- Spillman et al. 2013 (Cell Host Microbe): intraerythrocytic parasites sit in a
  high-Na+ host cytosol (because of the new permeability pathways) and keep cytosolic
  Na+ low by ATP-dependent efflux via PfATP4; spiroindolones disrupt this and
  resistance mutations in PfATP4 attenuate the effect
  [PMID:23414762 "The results are consistent with the hypothesis that PfATP4 is a plasma membrane Na+ efflux pump, similar to the ENA Na+-ATPases of other lower eukaryotes, and a target of the spiroindolone class of antimalarials."].
  Inhibition causes Na+-dependent cytosolic alkalinisation, which led to the proposal
  that PfATP4 imports H+ in exchange for Na+ (not directly demonstrated).
- Rosling et al. 2018 (JBC): Na+-dependent, cipargamin-sensitive ATPase activity in
  parasite membranes; Km(Na+) ~16 mM, Km(ATP) 0.23 mM; insensitive to K+ and Ca2+
  [PMID:29986883 "Characterization of the cipargamin-sensitive ATPase activity yielded data consistent with PfATP4 being a Na + transporter that is sensitive to physiologically relevant perturbations of pH, but not of [K + ] or [Ca 2+ ]."]
  [PMID:29986883 "K + was without effect on PfATP4-associated ATPase activity when present at concentrations ranging from 0 to 150 m m ."]
  Plasma membrane location [PMID:29986883 "These parasites were characterized by mutations in PfATP4, a plasma membrane type II P-type ATPase reported to belong to a subclass unique to apicomplexan parasites"].
- Qiu et al. 2022 (Nat Commun): G358S clinical resistance mutation reduces Na+ affinity,
  raises resting [Na+]cyt; equivalent mutation in T. gondii ATP4 behaves similarly
  [PMID:36180431 "PfATP4, and the equivalent mutation in Toxoplasma gondii ATP4, decrease the"].
- Many chemically distinct antimalarials (spiroindolones/cipargamin [PMID:20813948],
  aminopyrazoles [PMID:25322084], dihydroisoquinolones/(+)-SJ733 [PMID:25453091],
  4-cyano-3-methylisoquinolines [PMID:31311978]) select resistance mutations in PfATP4.
  Inhibition leads to Na+ accumulation and osmotic swelling of the parasite
  [PMID:29555632 "Here we show that six structurally diverse PfATP4-associated compounds, including the clinical candidate KAE609 (cipargamin), induce swelling of both isolated blood-stage parasites and intact parasitized erythrocytes."]
  and, for (+)-SJ733, eryptosis-driven host clearance of infected erythrocytes
  [PMID:25453091 "(+)-SJ733 cleared parasites in vivo as quickly as artesunate by specifically inducing eryptosis/senescence in infected, treated erythrocytes."].
  The host-clearance effect is a downstream drug consequence, not a function of PfATP4.

## Structure (2025)

- Haile et al. 2025 (Nat Commun): 3.7 A cryo-EM structure of endogenous PfATP4 from
  CRISPR-tagged parasites; SERCA-like ion-binding site with conserved Na+-coordinating
  residues [PMID:41115914 "The ion-binding site within the TMD is located between TM4, TM5, TM6 and TM8, similar to that of SERCA"];
  discovery of an apicomplexan-specific partner PfABP needed for PfATP4 stability
  [PMID:41115914 "Interestingly, PfABP knockdown also led to a marked reduction in PfATP4 protein levels within 24 h, highlighting a strict dependency of PfATP4 stability on its association with PfABP (Fig."].

## Annotation calls (summary)

- ACCEPT: P-type sodium transporter activity (IBA, IEA); plasma membrane (IBA, IEA).
- MODIFY to GO:0036376 sodium ion export across plasma membrane: sodium ion transport
  (IBA), sodium ion transmembrane transport (IEA), monoatomic ion transmembrane transport
  (IBA, IEA). membrane -> plasma membrane. nucleotide binding -> ATP binding.
  ATP hydrolysis activity -> P-type sodium transporter activity (transporter activity
  subsumes the coupled hydrolysis).
- KEEP_AS_NON_CORE: ATP binding.
- REMOVE: P-type potassium transmembrane transporter activity, potassium ion transport,
  potassium ion transmembrane transport (K+ has no effect on PfATP4 activity; no
  evidence of K+ transport); intracellular calcium ion homeostasis (Ca2+ ATPase
  assignment unconfirmed and superseded; activity insensitive to Ca2+).
- NEW: GO:0006883 intracellular sodium ion homeostasis (PfATP4 itself extrudes the Na+;
  participation, not just necessity).

## Open questions
- Is H+ the counter-transported ion (Na+/H+-ATPase stoichiometry)?
- Does PfABP act as a beta-subunit-like chaperone or a regulator of turnover?
- Role in mosquito / liver stages (Na+ environment differs).
