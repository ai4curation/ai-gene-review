# SRP40 (YKR092C, P32583) — curation notes

Autonomous AI review journal. Provenance recorded inline as `[PMID:xxxx "verbatim quote"]`
or `[file:...]`. SRP40 is an understudied ("dark") *S. cerevisiae* nucleolar protein.

## Identity and basic facts

- UniProt P32583, `SRP40_YEAST`; SGD S000001800; systematic name YKR092C; ORF YKR412A.
- 406 aa, 41 kDa, acidic pI ~3.9, ~49% serine.
- RecName in UniProt is a historical misnomer: "Suppressor protein SRP40" — named as a
  **weak suppressor of a mutant of the AC40 subunit shared by RNA polymerases I and III**
  (Lalo, Carles, Sentenac, Thuriaux 1993, PMID:8516295, the naming paper). UniProt FUNCTION
  line: "Not known; weak suppressor of a mutant of the subunit AC40 of DNA dependent RNA
  polymerase I and III." SRP40 here = "Suppressor of RNA Polymerase, 40 kDa", NOT signal
  recognition particle.

## Domain / sequence architecture (inline bioinformatic reasoning from the UniProt record)

- The protein is **almost entirely intrinsically disordered**: UniProt annotates
  `REGION 1..335 /note="Disordered" (MobiDB-lite)`, i.e. the N-terminal ~82% of the protein.
- The disordered region is dominated by **serine-rich low-complexity tracts** interspersed
  with **acidic (Asp/Glu) and basic (Lys/Arg) charge clusters** — multiple `COMPBIAS`
  features "Low complexity" and "Basic and acidic residues". The raw sequence shows long
  runs of `SSSSSSSSS...` and `DSDSDSDS...` (serine/aspartate repeats). This is the classic
  Nopp140/Treacle-type acidic-serine-rich (poly-S / SR-like, CK2-substrate) architecture,
  not a folded catalytic domain.
- The **only recognizable folded module is the C-terminal SRP40_C domain**
  (Pfam PF05022, InterPro IPR007718), roughly the last ~70 aa. This is the region that is
  **59% identical to the C-terminus of rat Nopp140** [PMID:8702624 "carboxyl terminus
  exhibits 59% sequence identity to that of Nopp140"]. No enzymatic motif is present; this
  domain family has no assigned catalytic activity.
- **Interpretation:** the sequence is consistent with a scaffold / chaperone / RNP-assembly
  factor that works through disordered, highly-phosphorylatable acidic-serine tracts plus a
  conserved C-terminal interaction module — NOT with a specific enzymatic molecular function.
  A specific biochemical activity cannot be assigned from sequence.

## Post-translational modification

- Extensively phosphorylated by **casein kinase II (CK2)**, like Nopp140, but to a much
  lesser degree than the vertebrate protein [PMID:8702624 "Like Nopp140, SRP40 is
  phosphorylated by casein kinase II, but to a much lesser extent"].
- Multiple mapped phosphosites (large-scale MS): pSer133, pThr289, pSer293, pSer394
  (UniProt MOD_RES; PMID:17287358, 17330950, 18407956, 19779198). Cdk1 substrate
  (PMID:19779198).
- Unusual **serine pyrophosphorylation** by the inositol pyrophosphate 5-IP7
  (5-diphosphoinositol pentakisphosphate): a Mg2+-dependent, enzyme-independent transfer of
  a β-phosphate onto a pre-phosphorylated serine (UniProt PTM; PMID:15604408, PMID:17873058).
  This is a PTM of the protein, not a molecular function *of* the protein.

## What is KNOWN (evidence-supported)

1. **Nucleolar localization.** SRP40 localizes to the yeast nucleolus
   [PMID:8702624 "SRP40 localizes to the yeast nucleolus"]; GOA IDA C:nucleolus from
   PMID:8702624, assigned by SGD. Also nucleolus ISS/IBA. SGD C = nucleolus.
2. **Yeast homolog of rat Nopp140.** Immunologically and structurally related; C-terminus
   59% identical [PMID:8702624 "identifies the yeast SRP40 gene product as immunologically
   and structurally related to rat Nopp140"; "bona fide yeast Nopp140 homolog"]. Rat Nopp140
   functionally complements loss of SRP40 [PMID:12700234 "rat Nopp140 restored growth and
   stability of box H/ACA snoRNAs after genetic depletion of SRP40 ... it is indeed the
   functional homolog of yeast Srp40p"].
3. **Proposed snoRNP chaperone / role in ribosome biogenesis.** Srp40p is "proposed to
   function as a chaperone for over 100 small nucleolar ribonucleoprotein particles that are
   required for rRNA maturation" [PMID:12700234]. Depletion of SRP40 (in the srp40Δ shm2 ade3
   synthetic-lethal background) specifically depletes **box H/ACA snoRNAs**
   [PMID:12700234 "the specific depletion of box H/ACA small nucleolar RNAs from the
   srp40Delta shm2 ade3 strain"]. This links SRP40 to box H/ACA snoRNP stability, i.e. the
   pseudouridylation snoRNP branch of ribosome biogenesis.
4. **Dosage-sensitive, nonessential.** Deletion is viable; SRP40 is "required at a specific
   cellular concentration for optimal growth as indicated by the negative effect on cell
   growth of both overexpression and deletion of its gene" [PMID:8702624]. "Srp40p is a
   nonessential yeast nucleolar protein" [PMID:12700234]. SGD: viable; overexpression
   decreases growth rate. Extensive genetic interaction network (SGD ~284 genes).
5. **Historically a weak suppressor of the RNA Pol I/III AC40 (rpc40) mutant** — the origin
   of the gene name [PMID:8516295]; a genetic, not mechanistic, observation.

The Nopp140 shuttling / NLS-binding "chaperone in ribosome biogenesis" model is a property
established for **rat Nopp140** [PMID:8702624 "Based on its subcellular location, its nuclear
localization signal binding capacity, and its shuttling between the nucleolus and the
cytoplasm, Nopp140 was proposed to function as a chaperone in ribosome biogenesis"]. It is
the basis of the SRP40 ISS annotation to nucleocytoplasmic transport (transferred from the
mammalian ortholog P41777), but the shuttling / NLS-binding activity has NOT been directly
demonstrated for yeast Srp40p itself — the 1996 paper notes yeast/vertebrate disparities in
nucleolar dynamics.

## What is NOT known (the gap)

- **No specific molecular function has been experimentally assigned.** UniProt FUNCTION =
  "Not known"; SGD MF = "molecular_function" (ND, GO:0003674); the protein is disordered with
  no catalytic motif. Whether Srp40p acts as an RNA chaperone, a snoRNP-assembly scaffold, a
  phosphoprotein hub, or a charge-based crowding/condensate component is undetermined.
- **The precise step in ribosome biogenesis is undefined.** SRP40 is linked to box H/ACA
  snoRNP stability *genetically* (in a sensitized srp40Δ shm2 ade3 background), but its direct
  molecular role (which snoRNP components it binds, whether it acts on assembly, stability,
  transport, or recycling) is not established. The chaperone-of-snoRNPs role is stated as a
  *proposal* [PMID:12700234 "proposed to function as a chaperone"].
- **Redundancy / dosage biology unexplained.** Nonessential yet dosage-sensitive in both
  directions; the buffering partner(s) that make it dispensable, and the reason overexpression
  is toxic, are unknown.
- **Nucleocytoplasmic transport role not directly shown in yeast.** The shuttling/NLS-binding
  activity is a Nopp140 (rat) property transferred by ISS; not directly demonstrated for
  yeast Srp40p.

## Annotation-by-annotation plan (GOA, 6 rows)

1. `GO:0005730 nucleolus` IBA (is_active_in, GO_REF:0000033) — ACCEPT. Consistent with IDA;
   phylogenetically robust (Nopp140 family is nucleolar).
2. `GO:0005654 nucleoplasm` IBA (is_active_in, GO_REF:0000033) — KEEP_AS_NON_CORE. Plausible
   phylogenetic transfer (Nopp140/Treacle family members are nucleoplasmic/coiled-body too),
   but the direct yeast evidence is for nucleolus; keep, non-core, secondary location.
3. `GO:0005730 nucleolus` IEA (located_in, GO_REF:0000117 ARBA) — ACCEPT (redundant with IDA;
   electronic confirmation of the well-supported nucleolar localization).
4. `GO:0003674 molecular_function` ND (enables, GO_REF:0000015) — ACCEPT. Honest "no data"
   root MF annotation; correctly reflects that no specific MF is known. This is the honest
   dark-gene MF state; do not fabricate an MF term.
5. `GO:0005730 nucleolus` IDA (located_in, PMID:8702624) — ACCEPT. Core; primary experimental
   localization.
6. `GO:0006913 nucleocytoplasmic transport` ISS (involved_in, PMID:8702624, from
   UniProtKB:P41777 = rat Nopp140) — KEEP_AS_NON_CORE (lean) / consider MARK_AS_OVER_ANNOTATED.
   Rationale: the transport/shuttling role is a rat-Nopp140 property transferred by similarity;
   not directly demonstrated in yeast. It is not wrong on family grounds, but it is peripheral
   and unverified in *S. cerevisiae*. Keep as non-core with a clear caveat rather than REMOVE
   (ISS from a curator-selected ortholog; per guidelines do not REMOVE on paralog/ortholog
   grounds). The core supportable role is nucleolar snoRNP-chaperone/ribosome-biogenesis, not
   the transport aspect. NOTE: ribosome biogenesis (GO:0042254) is a better-supported BP for
   this gene but is not in GOA; capture it via core_functions + proposed reasoning, and note
   the snoRNP/box H/ACA link from PMID:12700234.

## core_functions plan
- Nucleolar localization (CC): GO:0005730 nucleolus — strongly supported (IDA).
- Ribosome-biogenesis / snoRNP-associated role (BP): the best-supported functional statement
  is participation in ribosome biogenesis via box H/ACA snoRNP chaperoning (GO:0042254
  ribosome biogenesis; PMID:12700234). No specific MF term is assignable — leave MF dark and
  document in knowledge_gaps. Avoid `protein binding`.

## References to add
- PMID:8702624 (Meier 1996) — HIGH, VERIFIED (abstract-only; primary yeast localization +
  homology).
- PMID:12700234 (Yang & Meier 2003) — HIGH, VERIFIED (abstract-only; snoRNP-chaperone
  proposal, box H/ACA link, Nopp140 complementation).
- PMID:8516295 (Lalo et al. 1993) — MEDIUM, VERIFIED (gene-naming / AC40 suppressor origin).
- GO_REF:0000015, GO_REF:0000033, GO_REF:0000117 — annotation-method refs.
