# Pias1 (mouse, UniProt O88907) - curation notes

## Sources and status

- UniProt record `Pias1-uniprot.txt` (651 aa; PIAS family; SAP, PINIT, SP-RING/Znf-MIZ, SIM).
- Deep research: `Pias1-deep-research-openscientist.md` (not edited). Claims checked against
  cached primary sources before use (see "Integration of openscientist report").
- Cached publications for every PMID in the GOA set; full text available for PMID:16127449,
  PMID:16522640, PMID:22406621, PMID:22539995, PMID:18832723, PMID:23118920, PMID:24061474,
  PMID:34459572. Abstract-only: PMID:16600910, PMID:14611647, PMID:17187077, PMID:15123625,
  PMID:15229330, PMID:15507114, PMID:16816390, PMID:9724754.
- Human ortholog review `genes/human/PIAS1/` used for consistency; decisions mirror it unless
  mouse evidence differs. Human-derived papers reused here (already cached): PMID:9724754,
  PMID:12764129, PMID:15311277, PMID:15657437, PMID:17540171, PMID:20016603, PMID:27099310,
  PMID:36050397.

## Synthesis

### 1. SP-RING SUMO E3 ligase (core)

- UniProt: [file:mouse/Pias1/Pias1-uniprot.txt "Functions as an E3-type small ubiquitin-like modifier (SUMO)"].
- C/EBPbeta in 3T3-L1 adipogenesis [PMID:24061474 "PIAS1 functions as a SUMO E3 ligase of C/EBPβ to regulate adipogenesis"];
  catalytic activity required [PMID:24061474 "the catalytic activity of SUMO E3 ligase was required for PIAS1 to restrain adipogenesis"].
- GATA4 in intestinal cells [PMID:22539995 "PIAS1 promoted SUMO-1 modification of GATA4 on lysine 366"].
- PML and PML-RARA [PMID:22406621 "By performing in vitro SUMOylation assays, we discovered that both PIAS1 and PIASxα SUMOylate PML."].
- FOXA2 [PMID:23118920 "FOXA2 sumoylation and FOXA2 protein levels were increased by PIAS1 SUMO ligase but not a SUMO ligase activity deficient PIAS1 mutant"].
- PPARgamma [PMID:15123625 "we show that the PIAS family proteins, PIAS1 and PIASxbeta, function as E3 ligases"];
  in macrophages [PMID:16127449 "These results suggest that PIAS1/Ubc9-mediated sumoylation is required for PPARγ-dependent transrepression."].
- Nr2c1/Tr2 (UniProt SUBUNIT, PMID:17187077) [file:mouse/Pias1/Pias1-uniprot.txt "Interacts with NR2C1; the interaction promotes its"].

### 2. Inhibitor of activated transcription factors (core)

Mouse genetics is the physiological foundation of this function:
- Pias1-/- mice: [PMID:15311277 "PIAS1 selectively regulates a subset of IFN-gamma- or IFN-beta-inducible genes by interfering with the recruitment of STAT1 to the gene promoter"].
- NF-kB: [PMID:15657437 "PIAS1 blocks the DNA binding activity of p65 both in vitro and in vivo"]; Pias1-/- cells show
  enhanced p65 promoter occupancy and null mice elevated proinflammatory cytokines.
- STAT1 inhibition does not need STAT1 sumoylation [PMID:12764129 "inhibition of STAT1 by PIAS proteins does not require SUMO modification of STAT1"].
- Switched on by IKKalpha phosphorylation at Ser90, which requires PIAS1 ligase activity [PMID:17540171 "IKKalpha, but not IKKbeta, interacts"].
- PPARgamma transrepression of NF-kB targets in macrophages requires PIAS1 (PMID:16127449, PMID:18832723) -
  an indirect, SUMO-dependent route to inflammatory gene repression.

### 3. Context-dependent coactivation / cofactor roles (non-core)

- GATA4 coactivation is ligase-independent [PMID:22539995 "neither GATA4 sumoylation nor the SUMO ligase activity of PIAS1 was required for coactivation of IFABP promoter by GATA4 and PIAS1"].
- Msx1: PIAS1 tethers Msx1 to the nuclear periphery and confers DNA-binding specificity
  [PMID:16600910 "We show that PIAS1 is required for the appropriate localization and retention of Msx1 at the nuclear periphery in myoblast cells"].
- TBP binding via a conserved 39-aa C-terminal region [PMID:16522640 "Endogenous PIAS1 and TBP co-immunoprecipitated from nuclear extracts"].

### 4. DNA damage (from human; ISO)

- [PMID:36050397 "PIAS1 is recruited to damaged chromatin, which facilitates MRE11 SUMOylation to enhance MRE11 stability by antagonizing ubiquitylation."]
- [PMID:20016603 "we show that PIAS1 and PIAS4 promote DSB repair and confer IR resistance"]

### 5. Localization

Nucleus/nucleoplasm, nuclear speckles (ISS), PML bodies [PMID:27099310 "PIAS1 is a constituent PML-NB protein."];
partial synaptic co-localization in cultured hippocampal neurons
[PMID:34459572 "The results indicate partial co-localization of PIAS1 and PIAS3 with synaptic markers in hippocampal neurons and much rarer occurrence in cortical neurons."].

## Judgements on specific rows

- Protein binding (6 IPI): MODIFY Msx1 -> DNA-binding transcription factor binding; PPARgamma ->
  peroxisome proliferator activated receptor binding; Nr2c1/Tr2 -> nuclear receptor binding (UniProt
  states the interaction promotes Tr2 sumoylation); TBP -> TBP-class protein binding. REMOVE Sufu (Y2H
  hit, not confirmed in the abstract) and PML (substrate recognition already captured by SUMO ligase
  activity and protein sumoylation).
- fat cell differentiation (IDA PMID:24061474) -> MODIFY to negative regulation of fat cell
  differentiation: overexpression inhibits and knockdown promotes adipogenesis.
- positive regulation of protein localization to cell periphery (IDA PMID:16600910) -> MODIFY to
  protein localization to nuclear periphery (GO:1990139): the paper concerns the nuclear periphery, not
  the cell periphery (plasma membrane region). The human IEA row projected from this one was
  MARK_AS_OVER_ANNOTATED in the human review; that remains defensible but the root cause is this
  term choice.
- ubiquitin protein ligase activity (IEA, EC 2.3.2.27 mapping) -> REMOVE; UniProt uses the RING-type
  EC for SUMO E3s, but PIAS1 is a SUMO, not ubiquitin, ligase.
- transcription corepressor activity (ISO) -> MODIFY to transcription regulator inhibitor activity,
  JAK-STAT pathway (ISO) -> MODIFY to negative regulation, positive regulation of protein sumoylation ->
  MODIFY to protein sumoylation (same as human).
- Knockout/knockdown phenotypes (visual learning, spermatogenesis, G1/S, apoptosis, proliferation,
  protein-DNA complex assembly): PIAS1 does not execute these processes; they are downstream of
  transcription-factor sumoylation/inhibition -> MARK_AS_OVER_ANNOTATED (as human). Smooth muscle
  differentiation, positive regulation of transcription, synaptic locations -> KEEP_AS_NON_CORE.
- The innate-immunity phenotype of Pias1-/- mice (PMID:15311277) is captured mechanistically by
  negative regulation of JAK-STAT signalling and NF-kB signalling; no immune-process NEW term proposed.
- NEW: negative regulation of canonical NF-kappaB signal transduction (GO:0043124), IMP from Pias1-/-
  cells/mice (PMID:15657437). Participation: PIAS1 itself binds p65 and blocks its DNA binding.
  Comparator (QuickGO 2026-10, mouse, exact term): Nfkbie, Nfkbid, Tnfaip3 and Hdac1 carry GO:0043124.
  Mirrors the human NEW.

## Integration of openscientist report

Verified against cached sources: STAT1 promoter-recruitment blockade (PMID:15311277), p65 DNA-binding
blockade (PMID:15657437), SUMO-independent STAT1 inhibition (PMID:12764129), Ser90/IKKalpha
(PMID:17540171), PML-NB constituent (PMID:27099310), C/EBPbeta substrate (PMID:24061474).
Not verified (not cached) and not used for annotations: PNKP, Hes-1, AICD substrates, MK2 Ser522,
GSK3beta/HECTD2 degradation, GBP clone (PMID:9177271). Note the report omits that PIAS1 is NOT the
STAT1 E3 [PMID:12764129 "PIASx-alpha, but not PIAS1, functions as an E3 ligase"].

## Open questions

- Which inflammatory phenotypes of Pias1-/- mice depend on E3 activity vs binding-based inhibition?
- Is PIAS1 tethering of transcription factors (Msx1) to the nuclear periphery a general mechanism?
