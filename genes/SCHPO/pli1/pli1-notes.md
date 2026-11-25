# pli1 (SPAC1687.05, UniProt O94451) — curation notes

## Identity

- 727 aa, PIAS family (PANTHER PTHR10782:SF4). Domains (UniProt): SAP 18-52, PINIT 108-261,
  SP-RING-type zinc finger 290-371 (Zn-binding residues annotated by PROSITE rule), long disordered
  C-terminus. Ortholog of S. cerevisiae Siz1/Siz2 and human PIAS1-4. The other S. pombe SP-RING
  ligase is Nse2 (Smc5/6 subunit).
- UniProt: "Acts as an E3 ligase mediating SUMO/Smt3 attachment to other proteins"; "Interacts with
  hus5/ubc9"; nucleus.

## Core biochemistry

- [PMID:15359282 "Pli1p, the unique fission yeast member of the SP-RING family, is a SUMO E3 ligase in
  vivo and in vitro"]. RING point mutants "totally or partially reproduce the pli1 deletion phenotypes,
  thus correlating with their sumoylation activity".
- Principal/bulk ligase: [PMID:17209013 "Pli1p, but not the related Nse2p, is the principal SUMO E3
  ligase enzyme involved"]; [PMID:33159083 "the PIAS family E3 ligase Pli1 that promotes 90% of bulk
  SUMOylation and SUMO chain formation"]; [PMID:23936535 "In pli1Δ cells SUMOylation was barely
  detectable"].
- SUMO chains: [PMID:21444718 "Ubc9:SUMO instead promotes global sumoylation and chain formation, via
  the Pli1 E3 SUMO ligase"].
- Substrates (in vivo, Pli1-dependent): condensin Cnd2/Cnd3/Cut3 [PMID:31072933 "the upper bands (for
  Cnd2, Cnd3, and Cut3) (Fig. 1F) disappeared in ∆pli1 deletion mutant cells"]; Top1 in slx8Δ
  [PMID:23936535 "a hyper-SUMOylated form of Top1 does accumulate and that this is dependent on Pli1"];
  Pli1-dependent modification of LinE protein Rec10 (indirect) [PMID:19756689]. Tpz1-K242 SUMOylation
  regulates telomerase [PMID:24711392] but the abstract does not name the E3, so the deep-research
  claim that Tpz1 is a Pli1 substrate is not verified from cached text.
- Pli1 is itself auto-SUMOylated; Ulp1 at the NPC protects it from STUbL/Cdc48-mediated degradation
  [PMID:26221037 "SUMO chain-modified Pli1 is targeted for proteasomal degradation by the concerted
  action of a SUMO-targeted ubiquitin ligase (STUbL) and Cdc48-Ufd1-Npl4"]. Strachan et al. 2023 found
  centromere defects of nup132Δ are not explained by Pli1 destabilisation (Pli1K3R stabilised mutant)
  [PMID:37970674].

## Biological roles

- Centromere: TBZ sensitivity, minichromosome loss, reduced silencing of ura4 at cnt and imr
  [PMID:15359282]. Centromere clustering: pli1Δ abolishes the SUMO-dependent rescue of csi1Δ
  clustering defects in nup132Δ [PMID:37970674 "The rescue was also entirely suppressed by deletion of
  pli1+, repressing global SUMOylation"]. Role is regulatory/modulatory (via Lem2 and other substrates).
- Telomeres: [PMID:15359282 "pli1Delta cells exhibit consistent telomere length increase"];
  [PMID:17209013 "telomere lengthening induced by lack of sumoylation is not due to unscheduled
  telomere-telomere recombination"]; the abstract concludes SUMO "controls the activity of a positive or
  negative regulator of telomerase". No GO telomere annotation is
  present in GOA; PomBase captures this as phenotype. Not added as NEW (regulatory, indirect,
  substrate link to Tpz1 unverified for Pli1).
- Recombination control: pli1Δ hyper-recombination (~12-fold direct-repeat recombination)
  [PMID:23936535]; gene conversion at centromeric repeats [PMID:15359282].
- Stalled forks: [PMID:33159083 "The E3 SUMO ligase Pli1 acts at arrested forks to safeguard integrity
  of nascent strands and generates poly-SUMOylation which promote relocation to NPCs but impede the
  resumption of DNA synthesis by homologous recombination (HR)"]; "The active RFB did not shift to the NP
  nor bound to NPCs in the absence of Pli1"; "an increased level of resected forks in pli1Δ cells".
- STUbL epistasis: [PMID:17762865 "These phenotypes are suppressed by deletion of the major SUMO ligase
  Pli1"]; [PMID:21444718 "this Pli1-dependent SUMO chain formation causes the genome instability
  phenotypes of SUMO-targeted ubiquitin ligase (STUbL) mutants"].
- Meiosis: [PMID:19756689 "Mutation of the SUMO ligase Pli1 caused aberrant LinE formation and reduced
  genetic recombination"].
- ICL repair: [PMID:24192486 "the existence of a third pathway of ICL repair, dependent on the SUMO E3
  ligase Pli1"] — genetic (fan1-d pli1-d cisplatin hypersensitivity, SGA). "Non-recombinational"
  specificity of the PomBase term not explicitly visible in cached text.
- Condensin: pli1 loss-of-function mutations (mostly in SP-RING) suppress condensin ts mutants
  [PMID:31072933].

## Decisions

- protein binding (IPI with Pmt3, PMID:28552615): REMOVE (uninformative; ligase activity from the
  same paper is separately annotated; abstract-only so no specific SUMO-binding MF can be supported).
- No NEW annotations: telomere-length regulation and heterochromatin silencing are real phenotypes but
  likely indirect consequences of bulk SUMOylation; PomBase records them as phenotypes, and the
  specific Pli1 substrates linking to the processes are not established from cached sources.
- Deep research (OpenScientist) is accurate on main points; the Tpz1-as-Pli1-substrate claim and
  Rad9/Rhp6 claim (PMID:17515930) were not verified and are not used.
