---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T22:06:04.471620'
end_time: '2026-07-18T22:19:22.974301'
duration_seconds: 798.5
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 2
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
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

# Is this "uncharacterized" IS630-element protein a DDE transposase? (Foldseek fold call only)

You are an independent computational biologist. Run **one** decisive analysis and
report it concisely — do not broaden the investigation.

## Context (do not assume beyond this)

- UniProt **P16943** (*Shigella sonnei*, 343 aa), UniProt-named "Insertion element
  IS630 **uncharacterized** 39 kDa protein"; NCBIFAM family **NF033545** =
  "IS630 family transposase" (equivalog). Curator assigned no activity.
- Many DNA transposases adopt the **RNase H-like (retroviral integrase / DDE)
  fold** with a catalytic **DDE (Asp-Asp-Glu)** metal-binding triad.

## Representative sequence (UniProt P16943, 343 aa)

```
MPIIAPISRDERRLMQKAIHKTHDKNYARRLTAMLMLHRGDRVSDVARTLCCARSSVGRWINWFTQSGVEGLKSLPAGRARRWPFEHICTLLRELVKHSPGDFGYQRSRWSTELLAIKINEITGCQLNAGTVRRWLPSAGIVWRRAAPTLRIRDPHKDEKMAAIHKALDECSAEHPVFYEDEVDIHLNPKIGADWQLRGQQKRVVTPGQNEKYYLAGALHSGTGKVSCVGGNSKSSALFISLLKRLKATYRRAKTITLIVDNYIIHKSRETQSWLKENPKFRVIYQPVYSPWVNHVERLWQALHDTITRNHQCSSMWQLLKKVRHFMETVSPFPGGKHGLAKV
```

## The single decisive analysis

Fetch the AlphaFold model (AF-P16943-F1) and run **Foldseek** against PDB100 /
AFDB-SwissProt. Report ONLY:
1. the top structural homologs and whether the catalytic core is the **RNase
   H-like / DDE transposase-integrase fold** (with confidence);
2. whether a candidate **DDE (D,D,E) catalytic triad** is present/intact; and
3. a one-line verdict: is "**transposase activity (GO:0004803)**" structurally
   supported for P16943?

Do not run disorder, targeting, phylogeny, or literature surveys. One structural
analysis, one clear verdict, one confirmatory experiment.

## Output

# Is the "uncharacterized" IS630-element protein P16943 a DDE transposase?

## Summary

**Yes — P16943 is structurally a bona fide DDE transposase.** The UniProt-named "Insertion element IS630 uncharacterized 39 kDa protein" from *Shigella sonnei* (343 aa), despite carrying no curator-assigned molecular activity, adopts the **RNase H-like / retroviral-integrase transposase-integrase fold** and possesses an **intact DDE catalytic triad**. A single decisive structural analysis — fetching the AlphaFold model AF-P16943-F1 and querying it with Foldseek against PDB100 and AFDB-SwissProt — resolves the "uncharacterized" label unambiguously.

Every top structural homolog returned by Foldseek is a characterized DDE transposase. Against PDB100, the best hits are Mos1 mariner transposase strand-transfer and paired-end complexes (PDB 5hoo, 4r79, 3hot, 3hos, 4u7b) at E-values of 1e-11 to 1e-10 and probability 1.0, followed by the Sleeping Beauty transposase catalytic domain (5cr4, E=1.3e-7), the IstA transposase (8b4h), and the SETMAR/Hsmar1 transposase (3f2k). Against AFDB-SwissProt, the hits are SETMAR, Mos1, Tc3/Tcb2 transposases, and IS3-family InsF transposases, with E-values reaching 1e-11. There is no competing fold class in the hit list — the structural signal points exclusively to the DDE transposase-integrase superfamily.

Mapping the catalytic residues of the aligned templates onto P16943 identifies a candidate triad of **Asp181, Asp261, and Glu297**. In the AlphaFold model the three carboxylate groups cluster with two-metal RNase H active-site geometry (Asp181–Asp261 = 5.9 Å; Glu297–Asp181 = 6.2 Å; Glu297–Asp261 = 8.9 Å), with all three residues confidently modeled (pLDDT 92–96) within a high-confidence overall model (mean pLDDT 92.5). The catalytic core is therefore intact and correctly configured. The verdict is that **transposase activity (GO:0004803) is structurally supported for P16943.**

## Key Findings

### Finding 1: P16943 adopts the RNase H-like / DDE transposase-integrase fold with an intact D181–D261–E297 catalytic triad

The AlphaFold model AF-P16943-F1 was retrieved and its overall confidence assessed: mean pLDDT of **92.5**, indicating a high-quality, well-folded prediction suitable for structural homology search. The model's backbone was translated into the 3Di structural alphabet and submitted to Foldseek against two reference databases — the experimental structures of PDB100 and the predicted structures of AFDB-SwissProt.

**Structural homology (PDB100).** The Foldseek search returned an unambiguous, coherent set of top hits, all belonging to the DDE transposase-integrase superfamily:

| PDB hit | Identity | E-value | Prob | Description |
|---------|----------|---------|------|-------------|
| 5hoo | Mos1 mariner transposase | 1e-11 | 1.0 | strand-transfer / paired-end complex |
| 4r79 | Mos1 mariner transposase | ~1e-10 | 1.0 | transposase complex |
| 3hot | Mos1 mariner transposase | ~1e-10 | 1.0 | paired-end complex |
| 3hos | Mos1 mariner transposase | ~1e-10 | 1.0 | paired-end complex |
| 4u7b | Mos1 mariner transposase | ~1e-10 | 1.0 | transposase complex |
| 5cr4 | Sleeping Beauty transposase | 1.3e-7 | — | catalytic domain |
| 8b4h | IstA transposase | — | — | transposase |
| 3f2k | SETMAR / Hsmar1 transposase | — | — | transposase |

**Structural homology (AFDB-SwissProt).** The complementary search against predicted SwissProt structures corroborated the PDB result, returning SETMAR, Mos1, Tc3/Tcb2 transposases, and IS3-family InsF transposases, with E-values down to 1e-11.

The convergence of both databases on the same fold family — and specifically on well-studied DDE transposases (Mos1 mariner, Sleeping Beauty, Hsmar1/SETMAR, Tc3, IstA, IS3 InsF) with strong significance (E-values as low as 1e-11, probability 1.0) — constitutes decisive evidence that P16943's catalytic core is the **RNase H-like / retroviral-integrase transposase-integrase fold**. The absence of any non-transposase fold among the top hits removes ambiguity; this is not a borderline or chimeric call.

### Finding 2: A candidate DDE catalytic triad (Asp181, Asp261, Glu297) is present and intact

Establishing the fold is necessary but not sufficient; the defining functional feature of an active DDE transposase is a metal-binding **DDE triad** positioned to coordinate two divalent cations that catalyze DNA cleavage and strand transfer. The catalytic aspartates and glutamate of the aligned templates (Mos1, Sleeping Beauty, Hsmar1) were mapped through their Foldseek alignments onto the P16943 sequence:

- **Catalytic residue 1 → Asp181** (first catalytic aspartate).
- **Catalytic residue 2 → Asp261**, located within the conserved **"IVDNY"** (HDN-type) motif — a diagnostic signature of the second catalytic aspartate in this family.
- **Catalytic residue 3 → Glu297**, located within the **"VNHVER"** motif, 36 residues C-terminal to Asp261 — consistent with the **DD(34)E**-type spacing characteristic of mariner/IS630-related transposases.

Crucially, the three residues do not merely exist in sequence — they converge in three-dimensional space. In the AlphaFold model, the Asp181 and Asp261 carboxylates sit **5.9 Å** apart, Glu297 lies **6.2 Å** from Asp181 and **8.9 Å** from Asp261, and all three residues are modeled with high local confidence (pLDDT 92–96). These inter-carboxylate distances are consistent with the **two-metal-ion RNase H active-site geometry** required to coordinate the pair of catalytic Mg²⁺/Mn²⁺ ions. The triad is therefore not degenerate or disrupted — it is spatially assembled into a functional active site.

Together, Findings 1 and 2 satisfy both criteria for a structural functional assignment: the correct global fold and a correctly configured catalytic triad within it.

## Mechanistic Model / Interpretation

The evidence assembles into a coherent mechanistic picture. P16943 is the transposase encoded by insertion sequence IS630, a member of the IS630/*Tc1*/mariner superfamily of DDE transposases. These enzymes catalyze DNA transposition through a conserved chemistry centered on a two-metal-ion RNase H-like active site.

```
   IS630 transposase P16943 — inferred catalytic core
   ================================================

   RNase H-like / retroviral-integrase fold
   (central mixed β-sheet flanked by α-helices)

        Asp181 ......... Asp261 ......... Glu297
          |    5.9 Å       |     8.9 Å       |
          +------ 6.2 Å ---(------)----------+
                    \       |       /
                     \      |      /
                    [ Me²⁺ ][ Me²⁺ ]   <- two divalent metal ions
                        active site

   DD(34)E-type spacing:
     D181 ---- D261 --(34 aa)-- E297
     motifs:        "IVDNY"       "VNHVER"
```

**Catalytic logic.** In DDE transposases, the two aspartates and one glutamate coordinate two divalent metal ions that activate a water nucleophile (for donor-DNA cleavage) and the 3'-OH DNA end (for strand transfer into target DNA). The measured inter-carboxylate distances in P16943 (5.9–8.9 Å) fall within the range needed to bridge two metals in the canonical RNase H geometry, and the DD(34)E spacing matches the mariner/IS630 architecture exemplified by the top templates.

**Why the "uncharacterized" label is a curation artifact, not a biological reality.** UniProt named P16943 an "uncharacterized 39 kDa protein" and assigned no molecular activity because no direct experimental characterization existed for this specific protein. However, NCBIFAM independently places it in family **NF033545** ("IS630 family transposase," an equivalog-level assignment). The structural analysis here reconciles these signals decisively in favor of the family assignment: at the level of three-dimensional fold and active-site chemistry, P16943 is indistinguishable from experimentally validated DDE transposases. The "uncharacterized" descriptor reflects the historical absence of wet-lab data on P16943 itself, not any genuine structural or mechanistic ambiguity.

**Confidence.** The assignment rests on (i) two independent database searches converging on the same fold family, (ii) strong statistical significance (E-values to 1e-11, Foldseek probability 1.0), (iii) an intact and spatially assembled DDE triad, and (iv) uniformly high model confidence (mean pLDDT 92.5; triad residues 92–96). The one residual caveat is that all structural evidence derives from a computational model rather than an experimental structure of P16943, and the triad register was inferred by transitive alignment rather than co-crystallization with metal/DNA.

## Evidence Base

This was a self-contained structural analysis; no external literature was reviewed as citations in the knowledge state (0 papers). The evidence base is therefore the structural data itself, summarized below, together with the identity of the template structures that anchor the fold call.

| Evidence element | Source | Value / Result |
|------------------|--------|----------------|
| Model confidence | AlphaFold AF-P16943-F1 | mean pLDDT 92.5 |
| Best PDB structural homolog | Foldseek vs PDB100 | Mos1 mariner transposase (5hoo), E=1e-11, prob=1.0 |
| Additional PDB homologs | Foldseek vs PDB100 | Sleeping Beauty (5cr4, E=1.3e-7), IstA (8b4h), Hsmar1/SETMAR (3f2k) |
| SwissProt homologs | Foldseek vs AFDB-SwissProt | SETMAR, Mos1, Tc3/Tcb2, IS3 InsF (E to 1e-11) |
| Catalytic triad | Alignment-transfer + 3D model | Asp181, Asp261, Glu297 |
| Triad geometry | AF model measurement | D181–D261 5.9 Å; E297–D181 6.2 Å; E297–D261 8.9 Å |
| Triad local confidence | AlphaFold pLDDT | 92–96 (all three residues) |
| Diagnostic motifs | Sequence | "IVDNY" (D261), "VNHVER" (E297); DD(34)E spacing |

The template structures themselves constitute the mechanistic reference frame: Mos1 mariner transposase (multiple strand-transfer and paired-end complexes), Sleeping Beauty transposase, Hsmar1/SETMAR, Tc3, IstA, and IS3-family transposases are all experimentally established DDE enzymes whose catalytic triads and RNase H-like folds are documented in the PDB. P16943's high-significance match to this entire cohort — and to nothing outside it — is what supports the functional inference.

## Limitations and Knowledge Gaps

1. **Computational, not experimental, structure.** All conclusions rest on an AlphaFold prediction, not an experimentally determined structure of P16943. While the model is high-confidence (mean pLDDT 92.5) and the active-site residues are well-modeled (pLDDT 92–96), AlphaFold does not model bound metals, DNA, or the conformational changes that accompany catalysis.

2. **Inferred triad register.** The identities of the catalytic residues (Asp181, Asp261, Glu297) were assigned by transferring template catalytic positions through Foldseek alignments and by matching diagnostic sequence motifs, not by direct experimental mutagenesis or co-crystallization. Although the assignment is internally consistent (correct fold, correct motifs, correct geometry), the exact register could in principle differ by one or two residues.

3. **No metal/DNA complex.** The two-metal-ion geometry is inferred from inter-carboxylate distances in the apo model. Actual metal coordination and DNA binding were not modeled or measured.

4. **Activity vs. structure.** Structural competence for catalysis does not guarantee that P16943 is an *active* transposase in vivo. IS elements frequently accumulate mutations that inactivate the transposase while preserving the fold. This analysis establishes that the catalytic machinery is *structurally intact*, but full-length in-frame integrity, promoter activity, and the state of the terminal inverted repeats of the host IS630 element were outside the scope of this single decisive analysis (and were deliberately not investigated, per the study design).

5. **Deliberately narrow scope.** By design, disorder prediction, subcellular targeting, phylogeny, and literature survey were not performed. The verdict addresses only the fold and catalytic-triad question.

## Proposed Follow-up Experiments / Actions

The single most informative confirmatory experiment is **site-directed mutagenesis of the predicted catalytic triad coupled to a transposition assay**:

1. **Confirmatory experiment (primary).** Express recombinant P16943 and test in vitro transposition (or an in vivo papillation/mating-out assay) of a mini-IS630 substrate carrying the element's terminal inverted repeats. Then generate the **D181A, D261A, and E297A** single mutants (and the triple mutant). If the wild-type is active and each alanine substitution abolishes strand-transfer/cleavage activity, the DDE triad assignment and GO:0004803 are experimentally confirmed. This directly tests both the register (which residues) and the mechanism (metal-dependent catalysis).

2. **Metal-dependence check.** Assay activity as a function of Mg²⁺ vs. Mn²⁺ and demonstrate loss of activity under metal chelation (EDTA), consistent with a two-metal RNase H mechanism.

3. **Structural validation (optional).** Where feasible, determine an experimental structure (X-ray/cryo-EM) of P16943, ideally as a paired-end/strand-transfer complex with metal and DNA, to verify the modeled active-site geometry and metal coordination.

4. **Curation update.** On the basis of the structural evidence (and pending the mutagenesis result), P16943's UniProt annotation could be advanced from "uncharacterized" toward "IS630 family DDE transposase," aligning it with its NCBIFAM NF033545 equivalog assignment. The GO term **transposase activity (GO:0004803)** is structurally supported and should be flagged for review with an appropriate evidence code (e.g., inferred from structural/sequence model).

---

### Bottom line

The AlphaFold model of P16943 (mean pLDDT 92.5) matches, by Foldseek, **exclusively DDE transposases** — Mos1 mariner (5hoo, E=1e-11, prob 1.0), Sleeping Beauty (5cr4), IstA, Hsmar1/SETMAR, Tc3, and IS3 transposases — confirming the RNase H-like / retroviral-integrase transposase-integrase fold. An **intact DDE catalytic triad (Asp181, Asp261, Glu297)** is present, with the three carboxylates clustered in two-metal active-site geometry (5.9–8.9 Å apart; all pLDDT 92–96) and DD(34)E-type spacing. **Transposase activity (GO:0004803) is structurally supported** for this "uncharacterized" IS630 protein.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)