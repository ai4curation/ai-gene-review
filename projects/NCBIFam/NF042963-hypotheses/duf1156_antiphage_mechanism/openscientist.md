---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-18T13:37:41.055819'
end_time: '2026-07-18T13:54:02.886766'
duration_seconds: 981.83
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
citation_count: 5
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

# Hypothesis: molecular mechanism of the DUF1156 anti-phage defense protein family

You are an independent computational biologist. Determine the **molecular
mechanism** of a bacterial protein family that has been experimentally validated
as an **anti-phage defense system** but whose biochemical activity is not
established.

## What is known (do not assume beyond this)

- The family is NCBI Protein Family **NF042963** (NCBIFAM/PGAP), an *equivalog*
  named "anti-phage-associated DUF1156 domain-containing protein". It has ~151
  members spread across phylogenetically diverse bacteria (Cyanobacteria,
  Firmicutes, Proteobacteria, Deinococcus, Planctomycetes, ...).
- It was validated as conferring **anti-phage defense** by a phage-challenge
  screen: Gao et al. 2020, *Science* 369:1077 (PMID:32855333), "Diverse
  enzymatic activities mediate antiviral immunity in prokaryotes". That screen
  established the **phenotype** (protection against phage) but did **not**
  resolve the molecular mechanism.
- Members are large (~920-1015 aa) multidomain proteins. The defining
  "DUF1156" region is a Pfam domain of unknown function (PF06634).

## Representative sequence (use this for structure/sequence analysis)

UniProt **A0A3B7MFS0** (Thermosynechococcus sichuanensis E542), 1002 aa,
representative of NF042963:

```
MPDRPPTTESPPTLPPRAWAHRPALIERLLPVQKLSAEVYKERMAGAGQTLTALGSYWKGRKPLILAKACILGCLLPATDDPQRDLEIFELLMGMDDASLAARAKKKPTPKEIAAKVTFARLQDFFDISPPQLLLRSAPVDWSNPLYANVKLSWRDDVPLWDRRHLEAELLPKVPYRQRIESLYRPEEVADVHDHIWQRVNAHLGTHAHSFPELIEQLGILRFGHRPRVADTFCGSGQIPFEAARLGCDVYASDLNPIACLLTWGAFHIVGGTPEERAQLEQDQQELVAKVQAEIDQLGIEEDGNGWRAKVFLYCLETRCPQTGWWVPLLPTRVISKGYRVIAELEPEASEQRYRIRIRSGVSDADLKAAEKGTVRSDGRGQDPYLIHTVNGREYRTKISTLRGDYKTPDGKTANRLRRWQKSDFKPHPDDIFQERLYCIQWMRPIANTSRYEYEFREVTAADLERERIVEDYVAKHLTEWQEKGWVPDMPIELGHNTRQPIWERGWTYWHHLFNPRQLLIGSMIRKFSKATDYINYAYALNYFSKLCVWDTSRDNAQNVFYNQALNTFFNYACRSFTQIKPFLVRSFNKYPLIVHCKVNNNDAKSHCVNNDIYITDPPYGDAVKYEEITEFFIAWLRKNPPPEFADWVWDSRRALAIKGEGEEFRRNMVESYRRMRECMADNGLQVIMFTHQSGAIWADMANIVWAAGLQVTAAWYVVTETDSGLRNGSYVKGTVLLVCRKRQGHLSTTRDDLAWDLQEEVEQQVNLLTGLNQQARGWYRDENVFEDADLQMAGYAAALRVLTQYDRIDGRDMTNEALRPRLKGETTFVDELITFAVDIANQHLVPSGLSRDLWKELQPMERFYLKMLDLELRGLKTLDNYQNFAKAFKVRDFYPLMADKRANHARLKSALELGSSLMDSGSEFGGTLVRGILYALMELQQDEDVDVVIQHLSHNLPDFYRQREQVIEVCQYIEHHLRYHRAAEASAARILAEALLHQRLN
```

## The decisive question (scope your work to this)

**What enzymatic activity does this protein carry, and how does that activity
plausibly confer phage defense?** Answer it primarily by **structure-based fold
assignment**:

1. Obtain/predict the 3D structure (an AlphaFold model exists for A0A3B7MFS0)
   and run **Foldseek** against PDB/AFDB to assign the fold of each structural
   module along the ~1000-aa chain. Report the top structural matches per domain
   with confidence.
2. From the assigned fold(s), identify the likely **catalytic active site** and
   the **conserved sequence motifs/residues** that support (or argue against) an
   intact catalytic machinery. State whether the catalytic residues are present
   or degraded.
3. Name the most specific **enzyme class / EC** and the mechanism this implies,
   and connect it to a **named anti-phage defense strategy** (e.g. restriction-
   modification, BREX, DISARM, abortive infection, nucleic-acid degradation,
   nucleotide signalling, etc.). Say explicitly what the "DUF1156" module
   contributes and whether it is catalytic or accessory.

Keep other analyses (disorder, targeting, deep phylogeny) light — the fold
assignment + active-site check is the decision. Give a single clear mechanistic
conclusion with confidence, and state the one experiment that would confirm it.

## Output

# Molecular Mechanism of the DUF1156 Anti-Phage Defense Protein Family (NF042963)

## Summary

The DUF1156-containing anti-phage defense family **NF042963** is, at its enzymatic core, a **S-adenosyl-L-methionine (SAM)-dependent DNA methyltransferase**. Structure-based fold assignment of the family representative **A0A3B7MFS0** (*Thermosynechococcus sichuanensis* E542, 1002 aa) resolves a single, intact catalytic module embedded in the middle of the ~1000-residue chain and assigns it, with the highest possible confidence, to a **β-class, site-specific DNA cytosine-N4 methyltransferase (m4C; EC 2.1.1.113)**. Foldseek searches of the AlphaFold model against both AFDB-SwissProt and PDB100 return N4-cytosine-specific DNA methyltransferases (M.MjaII, M.MvaI, and the cyanobacterial M.AvaI) as the top hits at probability 1.0. The catalytic machinery is fully preserved: the Class I methyltransferase motif I glycine loop (FxGxG, F233–G237) and the diagnostic amino-methyltransferase catalytic motif IV (**DPPY**, D617–Y620) converge into a single Rossmann-fold SAM pocket in the model.

Critically, the protein carries **no nuclease fold of any kind** — there is no PD-(D/E)xK, HNH/His-Me finger, GIY-YIG, or m5C-type Pro-Cys motif anywhere in the sequence or structure. The only assignable catalytic fold across the entire 1002-aa chain is the central m4C methyltransferase. The defining **DUF1156 domain (PF06634)** itself is a small N-terminal module with no recognizable catalytic fold, and the C-terminal extension is likewise structurally novel and non-catalytic. Both flanking regions are therefore **accessory** — most plausibly serving DNA/target recognition and scaffolding roles, not catalysis.

The mechanistic conclusion is that this family defends against phages by **epigenetic self versus non-self discrimination**, in the mould of the **BREX / DISARM / restriction–modification** class of modification-dependent defense systems. The methyltransferase marks host DNA at a specific sequence motif via N4-cytosine methylation; unmethylated invading phage DNA lacks this self-mark and is excluded or restricted (with any nuclease/effector step supplied in *trans* by other genes of the defense locus, as in BREX). The single decisive confirmatory experiment is to build a DPPY catalytic-dead mutant (e.g., **D617A / Y620A**) and show that it abolishes both N4-cytosine DNA methylation activity and phage protection. **Overall confidence: high** for the enzymatic identity (m4C DNA methyltransferase); **moderate-to-high** for the specific BREX/DISARM-style modification-dependent exclusion mechanism.

---

## Key Findings

### Finding 1 — The protein is a SAM-dependent DNA amino-methyltransferase with an intact catalytic DPPY active site

The core enzymatic assignment rests on both sequence-motif mapping and 3D geometry. InterPro maps an **S-adenosyl-L-methionine-dependent methyltransferase superfamily domain (IPR029063)** to residues 157–287 of A0A3B7MFS0, within the broader NF042963 family signature (IPR049953, residues ~26–996). Within that window sits the canonical **Class I methyltransferase motif I** — the glycine-rich SAM-binding loop with the signature FxGxG pattern, realized here as **F233-C-G-S-G237** (context `...ADTFCGSGQIPFEA...`). Downstream, the diagnostic **amino-methyltransferase catalytic motif IV, DPPY**, is intact at **D617-P618-P619-Y620** (context `ITDPPYGD`). The DPPY tetrad is the hallmark of adenine-N6 and cytosine-N4 (amino) methyltransferases; its aspartate orients the exocyclic amino group of the target base and its aromatic tyrosine stacks against the flipped-out base, so its presence in undegraded form is strong evidence of an active amino-MTase.

Importantly, a systematic search for competing catalytic modules came up empty: there is **no PD-(D/E)xK, no HNH, no GIY-YIG, and no m5C-type Pro-Cys (PCQ) catalytic motif** anywhere in the chain. This means the module is *exclusively* a methyltransferase and specifically an **amino-methyltransferase** (targeting an exocyclic amino group), not a 5-methylcytosine enzyme and not a nuclease.

The AlphaFold model (**AF-A0A3B7MFS0-F1**, mean pLDDT 86.8, with 89% of residues above pLDDT 70) confirms the functional geometry. The motif I glycine loop and the catalytic DPPY, though ~380 residues apart in sequence, **converge into one pocket** in 3D: the Cα–Cα distance between G235 and D617 is only **8.1 Å**, and the entire motif I stretch (residues 230–240) lies within 12 Å of catalytic Asp617. This is exactly the spatial arrangement expected of a Rossmann-fold SAM-methyltransferase active site, where the SAM cofactor (bound by motif I) sits adjacent to the target-base catalytic residues (motif IV). Confidence over the catalytic region is high (motif I region pLDDT ≈ 94.3; DPPY pLDDT ≈ 82.5), so the geometry is trustworthy rather than a low-confidence artifact. **The catalytic residues are present, not degraded.**

Finally, this analysis relocated the DUF1156 domain itself: **IPR009537 / PF06634 maps to a small, separate N-terminal domain (residues ~30–90)**, well outside the catalytic module. The name "DUF1156" therefore labels an accessory sub-region, not the catalytic center of the protein.

### Finding 2 — Foldseek assigns the catalytic module to a β-class N4-cytosine DNA methyltransferase (m4C, EC 2.1.1.113)

Sequence motifs establish "amino-MTase"; structure decides the target base. A **Foldseek** search of the AlphaFold model against AFDB-SwissProt and PDB100 returned, as its highest-confidence hits (**probability = 1.0**), experimentally annotated **N4-cytosine-specific DNA methyltransferases**:

| Foldseek target | Protein | E-value | Query span | Annotated activity |
|---|---|---|---|---|
| Q58843 | Type II MTase **M.MjaII** | 4.7 × 10⁻⁷ | 212–744 | m4C DNA MTase (EC 2.1.1.113) |
| P14244 | Type II MTase **M.MvaI** | 7.7 × 10⁻⁵ | 212–742 | m4C DNA MTase (EC 2.1.1.113) |
| P0A461 / P0A462 | Type II MTase **M.AvaI** (**cyanobacterial**) | 1.6 × 10⁻³ | 207–742 | m4C DNA MTase (EC 2.1.1.113) |

Each of these enzymes catalyzes the reaction *a 2′-deoxycytidine in DNA + S-adenosyl-L-methionine → an N(4)-methyl-2′-deoxycytidine in DNA + S-adenosyl-L-homocysteine* (**EC 2.1.1.113**). The structural alignment spans query residues ~207–744, covering **both** motif I (FCGSG at 233) and catalytic motif IV (DPPY at 617) in one contiguous fold. That single, continuous span containing both motifs — with a large inserted target-recognition region between them — is the defining topology of the **β-class amino-methyltransferases**, in which the motif order along the chain places the catalytic motif IV before the SAM-binding-region-derived recognition insertion, distinguishing β-class enzymes from α- and γ-class amino-MTases.

Two additional details sharpen the call. First, the PDB100 hits (probability ≈ 0.99), which align only the ~586–745 catalytic subdomain, are generic **Class I SAM/O-methyltransferase Rossmann folds** — consistent with, and nested within, the amino-MTase assignment. Second, **M.AvaI is itself a cyanobacterial enzyme** (from *Nostoc/Anabaena*), the same phylum as the representative *Thermosynechococcus* — a phylogenetically coherent top match. Notably, **no m6A-specific (adenine) or m5C (Pro-Cys) enzyme ranked above the m4C hits**, so the structure specifically favors cytosine-N4 over the alternative amino-MTase target (adenine-N6).

### Finding 3 — DUF1156 and the C-terminal extension have no assignable catalytic fold (accessory modules)

To test whether any part of the protein *other* than the central module could be catalytic, per-region Foldseek searches were run against AFDB-SwissProt and PDB100. The **N-terminal region (residues 1–210)** — which contains the DUF1156 domain at residues 30–90 — returned **zero significant structural hits**. The **C-terminal region (residues 745–1002)** likewise returned no real hit (best probability 0.06, E-value 8.3 — spurious). By contrast, the **central region (207–744) matched N4-cytosine DNA methyltransferases at probability 1.0**.

The interpretation is unambiguous: the **only assignable catalytic fold in the entire 1002-aa chain is the central m4C methyltransferase**. The DUF1156 domain and the C-terminal extension are structurally novel and non-catalytic. In the context of a site-specific DNA methyltransferase, non-catalytic flanking domains typically function as **target-recognition domains (TRDs), DNA-binding/scaffolding modules, or partner-protein interaction surfaces**. The DUF1156 module is therefore best described as **accessory** — it contributes recognition/specificity or complex assembly, not the chemistry of methyl transfer.

### Finding 4 — Defense mechanism: methylation-based self/non-self discrimination, not nucleic-acid degradation

Combining Findings 1–3, the protein's *sole* enzymatic activity is DNA methylation, and it lacks any nuclease. A large (~1000 aa) multidomain protein whose only catalytic output is site-specific DNA methylation is architecturally the signature of the **epigenetic, modification-based anti-phage systems** — **BREX** (BrxX/PglX m6A methyltransferase) and **DISARM** (DrmMII methylase) — rather than of a classical restriction–modification (R-M) system in which a paired endonuclease performs the killing step. In BREX and DISARM, site-specific methylation of host DNA serves as a **self-marker**: incoming phage DNA, lacking the host methylation pattern, is recognized as non-self and excluded or restricted. This is mechanistically distinct from R-M cleavage and consistent with the absence of any nuclease domain in NF042963: **any effector/nuclease step would be supplied in *trans*** by other genes of the defense operon.

---

## Mechanistic Model / Interpretation

### Domain architecture of A0A3B7MFS0 (1002 aa)

```
 N ──[ DUF1156 ]──────[ β-class m4C DNA methyltransferase ]──────────[ C-term ext ]── C
 1    30    90  157         233            617                744    745         1002
      └─PF06634─┘  │      FxGxG(I)        DPPY(IV)             │      └─ no fold ─┘
      accessory    └──── IPR029063 SAM-MTase / Rossmann fold ──┘        accessory
      (recognition   Foldseek → M.MjaII / M.MvaI / M.AvaI (EC 2.1.1.113)  (scaffold /
       / scaffold)   probability = 1.0                                     partner IF)

 Active-site geometry (AlphaFold model AF-A0A3B7MFS0-F1, mean pLDDT 86.8):
   G235(Cα) ── 8.1 Å ── D617(Cα)      motif I loop within 12 Å of catalytic Asp617
   → single Rossmann SAM pocket, canonical amino-MTase active site
```

### Enzyme identity and reaction

- **Enzyme class:** Site-specific DNA **cytosine-N4 methyltransferase** (m4C), β-class amino-MTase.
- **EC number:** **2.1.1.113**
- **Reaction:** 2′-deoxycytidine (in a specific DNA recognition sequence) + SAM → N4-methyl-2′-deoxycytidine + S-adenosyl-L-homocysteine.
- **Catalytic residues (intact):** motif I FxGxG (F233–G237, SAM binding); motif IV **DPPY (D617–Y620)**, orienting the exocyclic N4 amino group of the flipped target cytosine.

### How the activity confers phage defense

```
          HOST GENOME                         INVADING PHAGE DNA
   ───(m4C)C───site───C(m4C)───          ───C───site───C───   (unmethylated)
            │  "self" mark                          │  no self mark
            ▼                                        ▼
   tolerated / replicated normally         recognized as NON-SELF
                                             → excluded / restricted
                                             (effector supplied in trans
                                              by other operon genes, BREX-like)
```

The methyltransferase writes an N4-cytosine mark at its cognate motif throughout the host genome. This epigenetic signature distinguishes self from non-self. Phage DNA entering the cell is not methylated at these motifs and is therefore flagged as foreign, triggering exclusion/restriction. Because NF042963 itself has no nuclease, the model predicts (as in BREX) that the actual DNA-targeting/killing step is carried out by a separate component of the defense system, while NF042963 provides the essential **methylation-based recognition** layer. The **DUF1156 domain and C-terminal extension** most plausibly provide **DNA target recognition and/or complex assembly** — the accessory functions required to methylate a specific motif and to engage partner effectors.

### Where this places the family among named defense strategies

| Strategy | Core enzyme | Nuclease in same protein? | Match to NF042963 |
|---|---|---|---|
| Type I/II/III R-M | MTase + endonuclease | Yes | Partial — has MTase, but **no nuclease** ✗ |
| **BREX** | BrxX/PglX **SAM MTase** | No (effector in *trans*) | **Strong** ✓ |
| **DISARM** | DrmMII **methylase** | No (multi-gene) | **Strong** ✓ |
| Abortive infection | diverse toxins/effectors | — | Weak (no toxin/effector fold) ✗ |
| Nucleic-acid degradation | nuclease | Yes | **Excluded** — no nuclease fold ✗ |
| Nucleotide signalling | cyclase / TIR | — | Excluded (no such fold) ✗ |

The architecture — a large, multidomain, SAM-dependent DNA methyltransferase with no accompanying nuclease — aligns most closely with **BREX/DISARM-type modification-dependent exclusion**.

---

## Evidence Base

### Structure- and sequence-derived evidence (this work)

- **Foldseek (AFDB-SwissProt + PDB100):** top hits at probability 1.0 are all m4C DNA methyltransferases — M.MjaII (Q58843), M.MvaI (P14244), and cyanobacterial M.AvaI (P0A461/P0A462), each EC 2.1.1.113.
- **InterPro:** IPR029063 (SAM-dependent MTase superfamily) at residues 157–287; DUF1156 = IPR009537/PF06634 at residues 30–90 (separate accessory domain).
- **AlphaFold model AF-A0A3B7MFS0-F1** (mean pLDDT 86.8): motif I (F233–G237) and catalytic DPPY (D617–Y620) converge in one pocket (G235–D617 Cα = 8.1 Å).

### Supporting literature

**[PMID: 39979294](https://pubmed.ncbi.nlm.nih.gov/39979294/)** — *Molecular basis of foreign DNA recognition by BREX anti-phage immunity system.* This paper establishes the core principle underlying the proposed mechanism: "**Anti-phage systems of the BREX (BacteRiophage EXclusion) superfamily rely on site-specific epigenetic DNA methylation to discriminate between the host and invading DNA.**" It further specifies that "**defense and methylation require BREX site DNA binding by the BrxX (PglX) methyltransferase employing S-adenosyl methionine as a cofactor**." These statements provide direct precedent that a large, SAM-dependent DNA methyltransferase can be the mechanistic core of a validated anti-phage system that works by self/non-self methylation — exactly the architecture and cofactor dependence found for NF042963.

**[PMID: 29085076](https://pubmed.ncbi.nlm.nih.gov/29085076/)** — *DISARM is a widespread bacterial defence system with broad anti-phage activities.* This work shows that "**the B. paralicheniformis DISARM methylase modifies host CCWGG motifs as a marker of self DNA akin to restriction-modification systems.**" This is the exact modification-based, motif-specific self-marking mechanism proposed for the DUF1156 family, in the context of a multi-gene defense system where the methylase provides the recognition layer.

**[PMID: 32338761](https://pubmed.ncbi.nlm.nih.gov/32338761/)** — *Phage T7 DNA mimic protein Ocr is a potent inhibitor of BREX defence.* This paper reinforces that BREX "self versus non-self differentiation requires methylation of specific asymmetric sites in host DNA by BrxX (PglX) methyltransferase," and that the phage counter-defense protein Ocr "physically associates with BrxX methyltransferase" — evidence that the methyltransferase is the functional heart of exclusion-type defense and a target for phage antagonists. It supports the view that NF042963's methyltransferase is the defensive engine.

**[PMID: 40921744](https://pubmed.ncbi.nlm.nih.gov/40921744/)** — *Multigenerational proteolytic inactivation of restriction upon subtle genomic hypomethylation in Pseudomonas aeruginosa.* This study underscores the general logic that methylation-based systems must methylate self DNA to avoid autoimmunity ("This post-translational regulation prevents self-DNA targeting, which is a risk due to stable genomic hypomethylation"). It contextualizes why a dedicated, high-fidelity DNA methyltransferase (as found in NF042963) is central to modification-based defense.

### Original phenotype reference

The family's anti-phage phenotype was established by **Gao et al. 2020, *Science* 369:1077 ([PMID: 32855333](https://pubmed.ncbi.nlm.nih.gov/32855333/))**, "*Diverse enzymatic activities mediate antiviral immunity in prokaryotes*," which validated protection against phage but did not resolve the molecular mechanism. This report supplies the mechanistic assignment that the screen left open.

---

## Limitations and Knowledge Gaps

1. **No wet-lab confirmation of methyltransferase activity.** The assignment is entirely computational (sequence motifs + AlphaFold model + Foldseek). Enzymatic activity, cofactor binding, and the modified base (m4C vs. an unexpected m6A) have not been measured biochemically.

2. **Recognition sequence unknown.** The specific DNA motif methylated by the family is not determined. Without it, the "self-mark" cannot be mapped, and the trans-acting effector (if any) cannot be predicted from motif context.

3. **The trans-effector is inferred, not identified.** The BREX/DISARM analogy predicts a separate nuclease/effector encoded elsewhere in the operon. The genomic neighborhood of NF042963 members was not analyzed here; whether a cognate effector exists (BREX-like) or whether methylation alone suffices (a pure exclusion/replication-block mechanism) is unresolved.

4. **Function of the DUF1156 and C-terminal modules is inferred.** Foldseek found no structural homolog for either accessory region, so their assignment as target-recognition/scaffolding is by analogy to MTase architecture rather than by direct evidence. They could instead mediate partner-protein contacts or signal transduction.

5. **m4C vs. m6A specificity carries residual uncertainty.** Although the top Foldseek hits are all m4C enzymes and no m6A enzyme outranked them, both use the DPPY/amino-MTase chemistry; discriminating N4-cytosine from N6-adenine definitively requires biochemical mapping of the modified base.

6. **Single representative analyzed.** Only A0A3B7MFS0 was examined structurally. Conservation of the DPPY (motif IV) and FxGxG (motif I) motifs and domain architecture across all ~151 family members was not verified by a family-wide multiple sequence alignment.

---

## Proposed Follow-up Experiments / Actions

1. **Decisive confirmatory experiment (catalytic-dead mutant).** Construct **D617A** and/or **Y620A** (DPPY motif IV) point mutants and a motif-I control (e.g., G235A). Show in the native or a heterologous host that these mutants **abolish both (a) DNA N4-cytosine methylation and (b) phage protection**, while the wild type retains both. Loss of protection upon catalytic inactivation would establish that methyltransferase activity is required for defense — the single cleanest test of the model.

2. **Direct biochemistry.** Express and purify the recombinant protein (or its central module); assay SAM-dependent DNA methyltransferase activity in vitro (³H-SAM transfer into a defined dsDNA substrate, or enzyme-coupled assays) and confirm the **modified base is N4-methylcytosine** by LC-MS/MS of digested DNA.

3. **Recognition-motif mapping.** Use **SMRT (PacBio) or Nanopore methylation sequencing** of host DNA from cells expressing the wild-type vs. catalytic-dead protein to identify the cognate methylation motif and confirm genome-wide self-marking.

4. **Operon / trans-effector analysis.** Examine the genomic neighborhoods of NF042963 members for co-encoded nuclease/effector or ATPase genes (BREX/DISARM signature genes), to determine whether defense is exclusion-only or requires a trans-acting effector.

5. **Family-wide conservation check.** Build a multiple sequence alignment of all ~151 NF042963 members and confirm strict conservation of motif I (FxGxG) and catalytic motif IV (DPPY), plus the accessory DUF1156 domain, to verify the mechanism generalizes beyond the single representative.

6. **Phage counter-defense test.** Assess whether the T7 DNA-mimic protein **Ocr** (a known BREX/R-M inhibitor) neutralizes NF042963-mediated defense, which would further tie the family to the BREX/exclusion class.

---

## Conclusion

The NF042963 / DUF1156 anti-phage family is, mechanistically, a **site-specific SAM-dependent DNA cytosine-N4 methyltransferase (m4C; EC 2.1.1.113)**. Structure-based fold assignment identifies a single intact catalytic module (β-class amino-MTase) with a fully preserved SAM-binding motif I (FxGxG, F233–G237) and catalytic motif IV (DPPY, D617–Y620) forming one Rossmann-fold active site; Foldseek's top matches at probability 1.0 are all N4-cytosine DNA methyltransferases. The protein contains no nuclease and no other catalytic fold, and the DUF1156 domain plus C-terminal extension are accessory (recognition/scaffolding). The family therefore most plausibly confers phage defense by **methylation-based self versus non-self discrimination in the BREX/DISARM/restriction–modification mould** — writing an N4-cytosine self-mark on host DNA so that unmethylated invading phage DNA is excluded/restricted, with any effector step supplied in trans. **Confidence is high for the enzymatic identity and moderate-to-high for the modification-dependent exclusion mechanism.** The definitive confirmation is a DPPY catalytic-dead mutant (D617A/Y620A) that abolishes both methylation and phage protection.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)