# DVU_1219 (Q72CR4) notes

Dashboard protein: NZ_CABHLV010000001.1_902 (https://gene-annotate-dashboard.kbase.us/review/NZ_CABHLV010000001.1_902), *N. vulgaris*, tier A.
The exact sequence (UPI0013DF57FD) has no active UniProtKB entry. The review is filed on the Hildenborough reference-proteome entry Q72CR4 (DVU_1219, UP000002194), which differs at one residue (V393M). The folder uses the locus tag because UniProt gives no gene symbol; the existing DESVH folders are named by accession.
GOA for Q72CR4 is empty. UniProt has only the IPR017853/SSF51445 fold and eggNOG COG0366.

## Conclusion (exploratory)

DVU_1219 is a probable envelope lipoprotein with a full GH13 (alpha-amylase-family) fold that lacks the GH13 catalytic acid/base and nucleophile. Its strong fitness phenotypes are shared with an RND efflux system, not specific to metals.

### Family and catalytic residues

- **Family assignment.** InterProScan finds only SUPERFAMILY (trans)glycosidases (123-583, E 2.8e-7) and a Phobius signal peptide (1-40). There is no Pfam, Gene3D or PANTHER match. A full Pfam-A scan without gathering thresholds finds no domain at E <= 10.
- **CAZy subfamily.** dbCAN v5.2.9 gives a single hit, GH13_33 (143-459, i-E 1.8e-50), and no CBM. A literature table places GH13_33 with the trehalose synthase subfamilies. I did not confirm this on the CAZy site.
- **Structure.** Foldseek (AF-Q72CR4, pLDDT 86.9; 91.5 over 123-583) aligns residues ~100-731 to TreS (O06458, E 2.5e-20), amylosucrase and other GH13 enzymes at 11-15% identity.
- **Catalytic residues.** I transferred the UniProt ACT_SITE/SITE positions through the Foldseek alignments:
  - nucleophile Asp → **E351** (17/18 hits)
  - acid/base Glu → **R391** (22/24 hits)
  - transition-state Asp → **D456** (14/16 hits), conserved

  The GH13_33 HMM independently places the same residues at its D (P = 0.47), E (P = 0.42) and D (P = 0.45) states. So the nucleophile and acid/base are lost and the protein is very probably non-catalytic, like the rBAT/4F2hc heavy chains among GH13-fold proteins. That is a prediction; no assay has been done.

### Topology

- Phobius predicts a signal peptide at 1-40. DeepTMHMM (dashboard) predicts 1-41, cleavable, with no membrane segment.
- Residues 39-42 are a LAGC lipobox, and the DeepTMHMM cleavage site falls just before Cys42. The protein is therefore a probable lipoprotein. The dashboard call missed this.

### Fitness

DvH data came from BERDL `kescience.fitnessbrowser`, since `fetch-fitness` returns 403. Run `dvu1219-fitness`.

- **Breadth.** 132 of 757 experiments are strong (|fit| >= 1, |t| >= 4): 117 negative and 15 positive. There are no specific-phenotype calls.
- **Negative conditions.** Molybdate 100 uM (to -3.5), most nitrogen sources including N2 (to -4.35 on serine), FCCP, chlorate, nitrite and chlorite.
- **Positive conditions.** Tungstate in pyruvate media (to +5.39) and nitrate 50 mM (+2 to +3).
- **Tungstate is not consistently beneficial.** It is -1 in MoYLS4 + 2 mM W, and -3.6 to -4 under N2 fixation with W.
- **Cofitness.** DVU3097 (TolC-family OMF) at 0.97; DVU0438 (AcrB) at 0.59; DVU0437 and DVU2439 (MFPs) at 0.56-0.57; nif genes at about 0.36.
- **Molybdate rank.** In MoYLS4 + molybdate only 26-34 genes are sick, and DVU1219 ranks 3rd-4th together with DVU0437, DVU0438 and DVU3097.
- **Published context.** Trotter et al. 2023 (PMID:37065130) describe DVU0437-0438 + DVU3097 as a molybdate-required RND pump that "is probably involved in maintaining cell wall integrity rather than in the efflux of molybdate". DVU1219 is not mentioned there, but its profile matches DVU3097's.
- **Tungstate rank.** The tungstate gain is shared with about 100 genes, led by the DVU0245-0251 cluster, and DVU1219 ranks 9th-22nd.
- **Neighbours.** No genomic neighbour is cofit (r <= 0.33).
- **Orthologues.** The Fitness Browser "orthologs" in Pseudomonas are TreS at BLAST score ratio 0.15, which are not true orthologues.

## Dashboard verdict: **overreach**

- **GO:0016798** hydrolase activity, acting on glycosyl bonds: **NPI** (`PSEUDOENZYME_OVERANNOTATION`). The GH13 fold is right, but the catalytic nucleophile and acid/base are replaced (E351, R391).
- **GO:0097501** stress response to metal ion: **UNC**. The phenotypes are real but are necessity phenotypes. They are pleiotropic and shared with an RND efflux / envelope-integrity module.
- **GO:0005576** extracellular region: **UNC**. Export is right, but a LAGC lipobox points to a membrane-anchored lipoprotein.

**Is Tier A justified?** The fitness data are strong and reproducible, so the protein is not "dark" physiologically. What they support, though, is "required together with the DVU0437-0438/DVU3097 efflux system", not a metal-specific function. Putting "molybdate/tungstate stress responses" in the name overstates what the data show.

**Paste-in correction:**
"GH13_33-family (alpha-amylase-fold) lipoprotein lacking the GH13 catalytic nucleophile and acid/base (E351, R391; probably non-catalytic); strongly cofit with the DVU0437-0438/DVU3097 RND efflux system (r = 0.97 with DVU3097) and, with it, required under molybdate excess; broad envelope-type phenotype (132/757 experiments); function unknown."

## Full review

`DVU_1219-ai-review.yaml` adds one term: NEW GO:0016020 membrane (IC; signal peptide plus lipobox). No MF or BP term is proposed. The core function has a location only, with no molecular function.

## Caveats

- No activity assay exists; inactivity is inferred from the residue substitutions.
- LipoP and SignalP 6 were not run; the lipobox call is a motif match.
- GH13_33 is labelled a trehalose-synthase subfamily only from a review table found by web search; I did not check CAZy directly.
- The cofitness link to the efflux system is correlational.
- The deep research (claude-code) could not reach the Fitness Browser. It agrees on the missing catalytic motifs and on the lipobox, and calls the protein a UniRef50 singleton.

## Tooling

- EBI InterProScan accepted one job; later submissions were blocked by EBI fair use, so the existing job was polled (`iprscan.py ... JOBID`).
- The AlphaFold file server returns 403 to curl user agents.
- BERDL SQL joins were very slow (they timed out), so tables are joined in Python.
- dbCAN HMMs come from `dbcan.s3.us-west-2.amazonaws.com/db_v5-2-9_5-5-2026/`; the bcb.unl.edu download redirects to a landing page.

## QC

- `validate`: pass.
- `validate-references`: 0 issues.
- `validate-terms`: pass, online.
- `validate-predictions`: 0 errors, 12 quotes and 1 title verified.
- `render`: OK.
- `validate-history`: OK (`history/genes/DESVH/DVU_1219/2026-10-31T004332Z-claude-code-472312.yaml`).
