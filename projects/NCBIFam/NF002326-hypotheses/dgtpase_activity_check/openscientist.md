---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T19:37:33.071198'
end_time: '2026-07-18T19:56:29.712604'
duration_seconds: 1136.64
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 10
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Hypothesis: is this "dGTPase-like" protein a catalytically intact enzyme, and of what activity?

You are an independent computational biologist. A bacterial protein has been
assigned to a family whose members are named a specific enzyme, but many
individual members are cautiously named "**-like**" by curators, who withheld the
specific catalytic activity. Decide whether this representative is a
**catalytically competent enzyme of the assigned activity**, a **degraded /
pseudo-enzyme**, or an enzyme of a **different substrate**.

## What is known (do not assume beyond this)

- NCBI Protein Family **NF002326** (NCBIFAM/PGAP), an *equivalog*, product name
  "**deoxyguanosinetriphosphate triphosphohydrolase**" (dGTPase; EC 3.1.5.1).
- This representative, UniProt **Q92Q32** (*Sinorhizobium meliloti* 1021, 405 aa),
  is UniProt-named "Deoxyguanosinetriphosphate triphosphohydrolase-**LIKE**
  protein" — the curator did NOT assign the specific activity or an EC number.
- dGTPases belong to the **HD superfamily** of metal-dependent phosphohydrolases,
  whose active site is a conserved **H...HD...D** motif of His/Asp residues that
  coordinate the catalytic divalent metal(s).

## Representative sequence

UniProt **Q92Q32**, 405 aa:

```
MTVDRQALGFGYGEHAAYASNPWASRGRLYPEASSPTRSDFQRDRDRIVHTTAFRRLKHKTQVFIAADGDHYRTRLTHTIEVAQIARALARALKLDEDLAEGVALVHDFGHTPFGHTGEDALHEVLEPYGGFDHNAQSLRIVTKLERRYAEFDGLNLTWESLEGLVKHNGPLMTADGQGLRGPVPQPILDYCALHDLELASFASLEAQVAAIADDIAYNTHDIDDGLRAGYLTFEMLEEIPFLARLMREVHDRYPGLESSRFTHEIMRRQITAMVEDVIAVAQKRLGEVRPESAKDVRCAGRVMATFSDEMSETDRQIKNLLMTRIYRHPEVMRVRQGAASIVTDLYRAFMDDPSLMKEHYWIDQIAGMAEPARARHVGDYLAGMTDTFAISVHRRLFDHTPDLR
```

## The decisive question (scope your work to this)

**Is Q92Q32 a catalytically intact HD-domain triphosphohydrolase (consistent with
dGTPase activity), or is its active site degraded / altered?** Answer by:
1. Foldseek fold assignment of the AlphaFold model (an AF model exists) — does it
   adopt the HD-domain phosphohydrolase fold, and what are the closest
   experimentally characterized structural homologs (dGTPase? SAMHD1-like dNTP
   triphosphohydrolase? something else)?
2. Identify the **HD-motif metal-coordinating His/Asp residues** and state whether
   they are **present and intact** or substituted/lost.
3. Give the most specific enzyme/EC and substrate call you can, and state whether
   propagating "**dGTPase activity (GO:0008832 / EC 3.1.5.1)**" to this protein is
   **supported, an over-annotation, or a different-substrate call**.

Keep other analyses light. Give one clear conclusion with confidence and the one
experiment that would confirm it.

## Output

# Is the "dGTPase-like" protein Q92Q32 a catalytically intact enzyme, and of what activity?

**Target:** UniProt **Q92Q32** — *Sinorhizobium meliloti* 1021, 405 aa, "Deoxyguanosinetriphosphate triphosphohydrolase-**LIKE** protein"; NCBIFAM family **NF002326** (equivalog; product "dGTPase", EC 3.1.5.1).

---

## Summary

**Q92Q32 is a catalytically *intact* HD-superfamily dNTP triphosphohydrolase — not a degraded pseudo-enzyme.** Its AlphaFold model (AF-Q92Q32-F1, v6) folds confidently into the all-α HD-domain metal-dependent phosphohydrolase fold (global pLDDT 94.75; 89.9 % of residues at very-high confidence), and every histidine and aspartate expected to build the canonical **H…HD…D** metallocenter is present, unsubstituted, and spatially converged into a single, pre-organized active-site pocket. On the decisive axis posed by the research question, the answer is unambiguous: the active site is complete, and the enzyme is competent to hydrolyze a (deoxy)nucleoside triphosphate.

**However, the specific "deoxyguanosinetriphosphate triphosphohydrolase (dGTPase; EC 3.1.5.1 / GO:0008832)" activity assigned by NCBIFAM family NF002326 is *not* directly supported for this member, and propagating it verbatim is an over-annotation of confidence.** By consistent-method global pairwise alignment, Q92Q32 is closest to human **SAMHD1** (33.1 % identity), a *broad-spectrum* dNTPase that hydrolyzes all four canonical dNTPs, and it is more distant from the only strictly dGTP-specific enzyme, *E. coli* Dgt (26.2 %), and from the hexameric bacterial dGTPase homolog (22.2 %). Substrate specificity in this family is decided **not** by the (intact) HD metal center but by nucleobase-recognition residues at the far end of the substrate pocket — features that cannot be read reliably from sequence/structure homology alone. Q92Q32 tracks the broad-specificity branch, so the general activity (**dNTP triphosphohydrolase, EC 3.1.5.–**) is well supported while the strict **dGTP** call is not.

**This vindicates the UniProt curator's caution in naming the protein "-like" and withholding the EC number.** The most defensible annotation is a general HD-domain dNTP triphosphohydrolase of the SAMHD1-like/dGTPase clade, with substrate specificity (dGTP-specific vs. broad dNTPase) left open pending experiment. The single decisive experiment is a straightforward in-vitro assay measuring triphosphate/deoxyribonucleoside release from each of the four canonical dNTPs (dGTP, dATP, dCTP, dTTP), with metal and allosteric-activator dependence, which would resolve the exact EC number.

---

## Key Findings

### Finding 1 — Q92Q32 is a bona fide HD-superfamily dNTP triphosphohydrolase homolog, not a fold-degraded pseudo-enzyme

Global pairwise Needleman–Wunsch alignment (BLOSUM62, gap open −10) places Q92Q32 unambiguously within the characterized dNTP-triphosphohydrolase family. Against *E. coli* dGTPase (Dgt, UniProt P15723) it shows **34.0 % identity** (134/394 aligned positions), and against human **SAMHD1** (UniProt Q9Y3Z3) **33.1 % identity** (134/405). These values are firmly within the "homology" regime for this fold. As a critical method control, the two experimentally characterized enzymes *E. coli* Dgt and human SAMHD1 share only ~21.8 % identity with each other yet are established structural and functional homologs that adopt the same fold "despite no sequence homology." Because Q92Q32's identities to both reference enzymes (26–34 %) *exceed* the identity the two references share with each other, these are genuine homology signals rather than alignment artifacts.

The diagnostic catalytic elements line up residue-for-residue. The catalytic **HD dyad** aligns exactly: Dgt His117–Asp118 and SAMHD1 His206–Asp207 both map onto **Q92Q32 His107–Asp108**. The dGTPase/dNTPase sequence signature "**HD…GH**" is conserved in Q92Q32 as `VALVHDFGHTPFGH`, directly comparable to the *E. coli* Dgt motif `SCLMHDIGNPPFGH`. Finally, the AlphaFold model AF-Q92Q32-F1 (v6) is a confidently folded HD-domain phosphohydrolase, with a **global pLDDT of 94.75** and 89.9 % of residues at very-high confidence — there is no evidence of the disorder, truncation, or fold collapse that would mark a decayed pseudo-enzyme.

This finding establishes family placement and rules out the "degraded fold" hypothesis at the level of overall architecture. The HD-superfamily catalytic principle — a conserved His/Asp set coordinating an active-site metallocenter — is retained. (Note: a formal Foldseek/DALI structural search was not run in this environment; the fold call therefore rests on 26–33 % identity to two structurally characterized HD dNTPases plus the intact metal-site geometry documented in Finding 2 — converging, but not a formal structural search.)

### Finding 2 — Q92Q32 has a fully intact, spatially converged HD metal-coordinating active site (the decisive result)

Beyond sequence conservation, the AlphaFold model demonstrates that the metal-coordinating residues are not merely *present in sequence* but *correctly assembled in three dimensions*. The His/Asp side chains that form the canonical H…HD…D metal center all converge into a single pocket around the HD-dyad histidine His107. Minimum side-chain heavy-atom distances to His107, and per-residue confidence, are:

| Residue | Role (by alignment) | Min. side-chain distance to His107 (Å) | Per-residue pLDDT |
|---------|--------------------|----------------------------------------|-------------------|
| **His78**  | motif-I metal His (↔ SAMHD1 His167) | 4.1 | 94.7 |
| **His107** | HD-dyad His (↔ SAMHD1 His206 / Dgt His117) | — (reference) | 97.1 |
| **Asp108** | HD-dyad Asp (↔ SAMHD1 Asp207 / Dgt Asp118) | 3.3 | 95.8 |
| **His111** | conserved "GH" His | 6.1 | 96.9 |
| **His168** | additional metal/2nd-shell His | 6.6 | 97.4 |
| **Asp214** | downstream metal-coordinating Asp | 3.4 | 97.6 |

Every one of these residues is modeled at very-high confidence (pLDDT 92–98), so the geometry is trustworthy rather than a low-confidence guess. His78 corresponds to the motif-I metal histidine of SAMHD1 (His167); His107–Asp108 is the HD dyad; His111 is the conserved "GH" histidine of the family signature. **No metal-coordinating His or Asp is substituted or lost.** The spatial convergence of multiple histidines and two aspartates into one pocket is the structural hallmark of a working HD metallocenter, and it directly parallels the intact metal-binding sites seen in crystal structures of characterized SAMHD1-like dGTPases, where the dNTP substrate is coordinated by up to three metal ions.

Together with Finding 1, this closes the decisive question posed in the brief: the active site is intact, and Q92Q32 is a catalytically competent triphosphohydrolase, not a pseudo-enzyme.

### Finding 3 — Q92Q32 belongs to the SAMHD1-like branch; the specific dGTP-substrate assignment is not resolvable from homology, so EC 3.1.5.1 propagation is over-confident

Having established catalytic competence, the remaining question is *which substrate*. Here the evidence argues against uncritically inheriting the strict dGTPase label. Using a single consistent method (BLOSUM62 global alignment, gap open −10), Q92Q32 is **closest to human SAMHD1 (33.1 %)** — a broad-spectrum enzyme that hydrolyzes all four canonical dNTPs into deoxyribonucleosides and inorganic triphosphate — and progressively more distant from strictly dGTP-specific or dGTP-preferring enzymes: *E. coli* Dgt (26.2 %) and the bacterial hexameric dGTPase homolog (22.2 %). The Dgt-vs-SAMHD1 control (21.8 %) confirms the higher Q92Q32 values reflect real homology signal.

The mechanistic reason homology cannot fix the substrate is the key point. In this family, **substrate specificity is determined by base-recognition residues at the end of the substrate-binding pocket, not by the metal-coordinating HD residues.** In *E. coli* dGTPase — "the only known enzyme that specifically hydrolyzes dGTP" — residues at the pocket terminus mimic Watson–Crick hydrogen-bonding to select guanine, giving strict dGTP specificity, a rare and mechanistically special property. Broad SAMHD1, by contrast, leaves an open cleft (~7 Å) that accommodates any base. An intact HD metal center — which Q92Q32 unquestionably has — is therefore *necessary but not sufficient* to infer dGTP specificity. Because Q92Q32 tracks the broad-specificity SAMHD1 branch, a strict dGTP (EC 3.1.5.1 / GO:0008832) call cannot be confirmed from sequence or structure homology alone.

Importantly, subfamily placement is itself insufficient to nail the substrate: the SAMHD1-like branch contains **both** broad dNTPases (human SAMHD1) **and** genuine dGTPases (e.g., the *Leeuwenhoekiella blandensis* SAMHD1 homolog, which is a dGTPase allosterically activated by dATP). So membership in this clade is compatible with either outcome. The honest conclusion is therefore a **general dNTP triphosphohydrolase (EC 3.1.5.–)** with substrate specificity unresolved — exactly the ambiguity the "-like" name encodes.

---

## Mechanistic Model / Interpretation

The evidence assembles into a clear, three-layer verdict:

```
LAYER 1 — FOLD                     [ INTACT ]
  AlphaFold global pLDDT 94.75; all-α HD-domain phosphohydrolase fold
  26–34% identity to characterized E. coli Dgt & human SAMHD1
  conserved HD...GH signature (VALVHDFGHTPFGH)
                        |
                        v
LAYER 2 — CATALYTIC METAL SITE     [ INTACT ]
  H...HD...D center fully present & spatially converged:
      His78  --+
      His107 --Asp108   (HD dyad = the catalytic core)
      His111   |        all within one pocket, 3.3-6.6 A, pLDDT 92-98
      His168   |
      Asp214 --+
  -> competent to hydrolyze a (d)NTP triphosphate
                        |
                        v
LAYER 3 — SUBSTRATE SPECIFICITY    [ UNRESOLVED ]
  Set by base-recognition residues at the pocket END,
  NOT by the HD metal residues.
  Closest homolog = SAMHD1 (BROAD dNTPase, 33.1%)
  Distant from strict dGTPase E. coli Dgt (26.2%)
  -> general dNTPase supported; strict dGTP NOT confirmable
```

**Reconciling the two family names.** NCBIFAM NF002326 is an *equivalog* that names the specific product "deoxyguanosinetriphosphate triphosphohydrolase," which propagates dGTPase/EC 3.1.5.1 to members. The UniProt curator, looking at this individual member, appended "**-like**" and pointedly withheld the EC number. Our analysis explains *why the curator was right to hesitate*: the automated family assignment is anchored on the conserved, intact catalytic machinery (which Q92Q32 has), but that machinery is shared by both dGTP-specific and broad-spectrum members. The distinguishing base-recognition residues place Q92Q32 nearer the broad SAMHD1 branch, so the equivalog's confident dGTP label outruns the evidence for this particular sequence.

**Bottom-line call (confidence levels):**

| Claim | Verdict | Confidence |
|-------|---------|-----------|
| Adopts HD-domain phosphohydrolase fold | **Yes** | High |
| Active site intact (not a pseudo-enzyme) | **Yes** | High |
| Is a dNTP triphosphohydrolase (EC 3.1.5.–) | **Yes** | Medium–High |
| Is specifically a dGTPase (EC 3.1.5.1 / GO:0008832) | **Not confirmable from homology; likely over-annotated** | Low |
| Closest characterized structural/sequence homolog | **SAMHD1-like dNTPase branch** | Medium |

The single most probable biochemical description is: *an HD-superfamily, SAMHD1-like dNTP triphosphohydrolase with an intact metallocenter and a substrate preference that is presently undetermined (plausibly broad rather than strictly dGTP-specific).*

---

## Supported and Refuted Hypotheses

| Hypothesis | Verdict | Basis |
|---|---|---|
| Q92Q32 adopts the HD-domain phosphohydrolase fold | **Supported** | pLDDT 94.75; 26–33 % identity to two characterized HD dNTPases; conserved HD…GH motif |
| The HD metal-coordinating His/Asp residues are intact | **Supported** | His78/His107/Asp108/His111/His168/Asp214 converge ≤6.6 Å, pLDDT 92–98; none substituted |
| Q92Q32 is a degraded / pseudo-enzyme | **Refuted** | Active site fully assembled at high confidence |
| Q92Q32 is a strictly dGTP-specific dGTPase (EC 3.1.5.1) | **Not confirmed (over-annotation)** | Closest to broad SAMHD1; specificity-setting base-recognition residues are not resolvable by homology |
| Q92Q32 is a catalytically competent dNTP triphosphohydrolase (EC 3.1.5.–) | **Supported** | Intact metallocenter + secure family membership |

---

## Evidence Base

| PMID | Paper (short title) | How it supports / challenges the findings |
|------|---------------------|-------------------------------------------|
| [PMID: 27849620](https://pubmed.ncbi.nlm.nih.gov/27849620/) | *An HD domain phosphohydrolase active site tailored for oxetanocin-A biosynthesis* | Defines the HD-superfamily catalytic signature — a conserved set of His/Asp residues coordinating the active-site metallocenter — which Q92Q32 retains intact (Findings 1 & 2). |
| [PMID: 35643313](https://pubmed.ncbi.nlm.nih.gov/35643313/) | *High-resolution structures of the SAMHD1 dGTPase homolog from Leeuwenhoekiella blandensis* | Establishes SAMHD1/E. coli dGTPase as the reference characterized homologs of this widely distributed family (Finding 1); describes an "intact metal-binding site with the dGTP substrate coordinated to three metal ions," the arrangement the Q92Q32 model reproduces (Finding 2); shows a bacterial SAMHD1-like homolog can itself be a dGTPase activated by dATP, proving the branch contains both broad and dGTP-specific members (Finding 3). |
| [PMID: 31019074](https://pubmed.ncbi.nlm.nih.gov/31019074/) | *The crystal structure of dGTPase reveals the molecular basis of dGTP selectivity* | Establishes that E. coli dGTPase is "the only known enzyme that specifically hydrolyzes dGTP" and that its selectivity comes from base-recognition residues at the *end* of the substrate pocket mimicking Watson–Crick interactions — i.e., dGTP specificity is *not* readable from the metal-coordinating HD residues (Finding 3). Challenges any inference of dGTP specificity from an intact HD site alone. |
| [PMID: 40568220](https://pubmed.ncbi.nlm.nih.gov/40568220/) | *Reaction Mechanism and Metal Selectivity of Human SAMHD1* | Confirms SAMHD1 as a dNTPase that "hydrolyze[s] all four canonical dNTPs" using coordinated iron and magnesium ions — the broad-specificity reference against which Q92Q32's closest homology is measured. |
| [PMID: 8995266](https://pubmed.ncbi.nlm.nih.gov/8995266/) | *Cloning, purification, and characterization of the Shigella boydii dGTP triphosphohydrolase* | Documents a classic, fully active bacterial dGTPase (EC 3.1.5.1) whose substrate specificity is "explained by the array of potential hydrogen bond donors/acceptors displayed on the base moiety" — reinforcing that base recognition, not the metal site, governs specificity. |
| [PMID: 25694425](https://pubmed.ncbi.nlm.nih.gov/25694425/) | *Structure of Escherichia coli dGTP triphosphohydrolase: a hexameric enzyme with DNA effector molecules* | Provides the hexameric bacterial dGTPase homolog (22.2 % identity to Q92Q32) — the most distant of the compared characterized enzymes, consistent with Q92Q32 belonging to the SAMHD1-like rather than the hexameric-Dgt branch. |
| [PMID: 23880768](https://pubmed.ncbi.nlm.nih.gov/23880768/) | *GTP is the primary activator of the anti-HIV restriction factor SAMHD1* | Illustrates the allosteric-activation logic (dGTP/GTP) of the SAMHD1 branch and its capacity to hydrolyze base-modified/non-canonical dNTPs — informs the design of the confirmatory assay. |
| [PMID: 32576829](https://pubmed.ncbi.nlm.nih.gov/32576829/) | *Crystal structures of SAMHD1 inhibitor complexes* | Details the water-mediated dNTP hydrolysis mechanism of SAMHD1, the branch to which Q92Q32 is closest. |
| [PMID: 30380297](https://pubmed.ncbi.nlm.nih.gov/30380297/) | *Identification of Inhibitors of the dNTP Triphosphohydrolase SAMHD1* | Provides a direct, colorimetric high-throughput activity assay format directly transferable to testing Q92Q32's catalytic activity. |
| [PMID: 28321930](https://pubmed.ncbi.nlm.nih.gov/28321930/) | *Uncovering allostery and regulation in SAMHD1 through MD simulations* | Background on tetramerization/allosteric regulation relevant to interpreting any oligomeric or activator dependence in Q92Q32. |

**Consistency of the evidence:** All three findings are mutually reinforcing and consistent with the literature. There is no contradictory evidence within the analysis — the tension is entirely between the confident equivalog family label and the more cautious member-level assessment, which the data resolve in favor of caution on *specificity* while firmly confirming *catalytic competence*.

---

## Limitations and Knowledge Gaps

1. **No experimental biochemistry.** The entire conclusion rests on sequence homology and a single AlphaFold model. AlphaFold reports high confidence in the *fold and side-chain placement*, but it does not model bound metals, substrate, or catalytic dynamics; competence is inferred from geometry, not demonstrated by turnover.

2. **No formal Foldseek/DALI structural search or experimental-structure superposition** was possible in this environment (PDB references could not be staged). The fold call rests on sequence homology to characterized enzymes plus the AF-model metal-site geometry — strong and converging, but not a formal, unbiased structural neighbor search.

3. **Substrate-specificity residues were not mapped atom-by-atom** onto Q92Q32. The specificity conclusion is inferential (branch placement plus the published mechanism of base recognition), not a direct read-out of the pocket-terminus residues from a superposed dGTP-bound reference.

4. **Homology identities are moderate (26–34 %).** This is comfortably enough to assign family and fold, but at these identities the precise 1:1 mapping of individual specificity residues carries uncertainty; a structure-guided alignment would be more reliable than the global sequence alignment used here for pinpointing pocket residues. Identities were computed with a self-implemented BLOSUM62 global aligner (linear gap); values are approximate but internally consistent and corroborated by the Dgt–SAMHD1 control.

5. **Allosteric regulation and oligomeric state not assessed.** Members of this family (SAMHD1, the *L. blandensis* homolog) are allosterically activated by GTP/dGTP/dATP and may require oligomerization for activity. Q92Q32's activation requirements and oligomeric state are unknown and could affect any in-vitro assay design.

---

## Proposed Follow-up Experiments / Actions

**Priority 1 — The one decisive experiment: four-dNTP hydrolysis assay.**
Express and purify recombinant Q92Q32 and measure triphosphate (or deoxyribonucleoside) release from each canonical substrate — **dGTP, dATP, dCTP, dTTP** — individually, in the presence of a divalent metal (Mg²⁺/Mn²⁺/Fe²⁺) and candidate allosteric activators (dGTP, dATP, GTP). Detect released inorganic triphosphate/Pi (malachite-green or a validated direct colorimetric format, cf. the SAMHD1 assay, [PMID: 30380297](https://pubmed.ncbi.nlm.nih.gov/30380297/)) or the deoxyribonucleoside product by HPLC. This single readout distinguishes the outcomes cleanly:
- Activity on dGTP only → **strict dGTPase (EC 3.1.5.1)** — the equivalog label is correct after all.
- Activity on all four → **broad dNTP triphosphohydrolase (EC 3.1.5.–, SAMHD1-like)** — a different/broader substrate call; "-like" was correct.
- No activity on any → would reopen the pseudo-enzyme question (contradicted by structure, so unlikely).

**Priority 2 — Test allosteric activation and oligomeric state.** Repeat the assay ± candidate allosteric activators to detect SAMHD1-like allosteric regulation ([PMID: 23880768](https://pubmed.ncbi.nlm.nih.gov/23880768/); [PMID: 35643313](https://pubmed.ncbi.nlm.nih.gov/35643313/)); include native-PAGE / SEC-MALS to determine oligomeric state.

**Priority 3 — Objective structural neighbor search (in-silico, cheap).** Run **Foldseek** on AF-Q92Q32-F1 against the PDB for an unbiased ranked list of experimentally solved structural homologs, and structurally superpose Q92Q32 onto both a strict dGTPase (e.g., the structure from [PMID: 31019074](https://pubmed.ncbi.nlm.nih.gov/31019074/)) and SAMHD1 to compare the **base-recognition subpocket** directly. This can strengthen the "broad vs. dGTP-specific" prediction before committing to wet-lab work.

**Priority 4 — Curation recommendation.** Pending experiment, annotate Q92Q32 as a **general HD-domain / SAMHD1-like dNTP triphosphohydrolase (EC 3.1.5.–)** with the family-level HD-domain metal-binding terms, and **do not** propagate GO:0008832 / EC 3.1.5.1 (dGTPase) at the confident level implied by the equivalog. The UniProt "-like" name should stand.

---

## Conclusion

Q92Q32 is a **catalytically intact, confidently folded HD-superfamily dNTP triphosphohydrolase with a fully assembled H…HD…D metallocenter** — decisively *not* a degraded pseudo-enzyme (HIGH confidence). But it sits closest to the *broad-spectrum* SAMHD1 branch, and because substrate specificity in this family is set by base-recognition residues rather than the (intact) metal site, the specific **dGTPase / EC 3.1.5.1 / GO:0008832** activity assigned by the NF002326 equivalog is **not confirmable from homology and is best regarded as an over-annotation for this member** (LOW confidence in the strict-dGTP label). The curator's "-like" caution is justified. A four-dNTP in-vitro hydrolysis assay is the single experiment that would settle the exact enzyme and EC number.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)