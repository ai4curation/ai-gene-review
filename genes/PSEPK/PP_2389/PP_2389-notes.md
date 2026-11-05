# PP_2389 (Q88KA1) — curation notes

Reviewed as part of the BERIL "hackathon" project, which checks gene-function calls made by the
KBase gene-annotate dashboard ("Dark Protein Atlas", model `gpt-rosalind-5.5-codex`).

Dashboard gene: `NZ_CP026332.1_3351` (*Pseudomonas putida*, tier A, core protein)
<https://gene-annotate-dashboard.kbase.us/review/NZ_CP026332.1_3351>

## Identity and why the review is filed on Q88KA1

The dashboard's exact sequence belongs to a non-reference-proteome *P. putida* strain whose
UniProtKB entries are deleted ("Not part of a reference proteome"). Following the project
protocol, the review is filed on the closest reference-proteome entry, KT2440 PP_2389 (Q88KA1),
which is **99.6% identical over the full 262 residues** (261/262). The dashboard ID is recorded
as an alias in the review YAML.

## Conclusion

PP_2389 is a soluble, cytoplasmic protein of the YqcI/YcgG family (PF08892, IPR014988,
PTHR40045, COG3403). The best-supported inference is that it is a **cysteine-ligated heme
N-hydroxylase (monooxygenase) with an undetermined substrate**. This is a homology-only
prediction and should be read as a hypothesis to test.

What supports it:

- The family is no longer uncharacterized. Three members have assigned activities, all heme
  N-hydroxylases: AglA N-hydroxylates an arginine conjugate (PMID:35616638), DcsA is required
  for N(omega)-hydroxy-L-arginine formation and is spectroscopically a heme protein
  (PMID:22547619), and GntA mono-oxygenates a tertiary amine with NADPH (PMID:35583956).
- AglA crystal structures (PMID:41221789, PDB 9UB3 and five others) show a non-canonical
  "sandwich" fold with the heme iron ligated by Cys44; the C44 mutant is inactive. The fold has
  no significant DALI similarity to known heme enzymes, so this is a new structural class,
  distinct from P450s.
- DcsA is the closest characterized homolog of PP_2389: **38.4% identity over 224 aligned
  residues**. AglA is 33.6% over 214.
- PP_2389 conserves the functional residues. AglA Cys44 (heme thiolate) maps to PP_2389
  **Cys46**, within the family's conserved FPC motif at 44-46; the heme-propionate salt-bridge
  residues Arg166/Lys196/Arg200 map to Arg167/Arg198/Arg202; and the substrate-gate residues
  Phe152/Arg179/Phe182 map to Phe153/Arg180/Phe183. The C-terminal CPF motif is at 244.
- DeepTMHMM predicts no signal peptide and no transmembrane segment, and the characterized
  members are soluble.

What is unknown, and why I did not go further:

- **No substrate can be named.** Characterized members act on an arginine conjugate, on free
  arginine (only after engineering) and on a tertiary amine. Wild-type AglA is essentially
  inactive on free arginine, so free arginine is not a safe default. GO:0004497 monooxygenase
  activity is therefore the most specific molecular-function term the evidence allows; no EC
  number or substrate-level term is justified.
- **No biosynthetic context.** All six characterized members sit in natural-product gene
  clusters. PP_2389 does not: there is no NRPS, PKS, arginase or phosphonate gene nearby. So the
  closest functional analogy may instead be the uncharacterized "housekeeping" subset of the
  family, which includes the *B. subtilis* founders YqcI (P45944, 31.2% identity) and YcgG
  (P94382, 35.7%).
- Nothing has been measured on PP_2389 or on any *Pseudomonas* family member: no heme content,
  no activity, no localization. The reductase partner that such an enzyme would need is also
  unidentified; PP_2389 has no reductase domain of its own.

## The fitness association: real, accurate, but not specific

The dashboard built its annotation headline around RB-TnSeq fitness. The Fitness Browser web
site returned HTTP 403, so I pulled the KT2440 (orgId `Putida`) data independently from the
BERDL lakehouse copy (`kescience.fitnessbrowser`). Findings (BERIL run
`20261030T211248Z-pp2389-fitness`):

- The quoted numbers are exactly right: DL-2-aminobutyrate (N) fitness **+4.007** (t 23.8) and
  **+3.878** (t 19.0); L-methionine (N) **+2.063** and **+1.938**. Two replicates each.
- PP_2389 was measured in 300 experiments. Only 10 pass |fit| >= 1 and |t| >= 4, and **all 10
  are positive** — insertion mutants grow better. Its most negative score is -1.03. The rest are
  L-phenylalanine (N) (+1.41, +1.40), L-leucine (N) (+1.39), levulinate (C) (+1.05),
  4-hydroxyvalerate (C) (+1.03) and 6-aminocaproate (N) (+1.02).
- **The phenotype is not specific to PP_2389.** The divergent LysR-family regulator PP_2390
  scores +4.14 and +4.03 on DL-2-aminobutyrate; the adjacent LysE-family exporter PP_2388 scores
  +3.80 and +3.50; PP_2387 scores +3.87. PP_2389's top cofitness partners are PP_2390 (0.77) and
  PP_2388 (0.69); PP_2388's top partner is PP_2390 (0.93).
- In that experiment, 113 of 4778 genes pass fit >= 1 with t >= 4, and PP_2389 ranks 4th. Many
  complex I (*nuo*) subunits are in the same list, which is a hint that the condition has a
  general cost-of-growth component.
- PP_2389 has **no entry** in the Fitness Browser `specificphenotype` table.
- Gene order (minus strand): PP_2389 (2727324-2728112) sits 3 bp upstream of PP_2388
  (2726695-2727321); PP_2390 is divergent on the plus strand. PP_2388 and PP_2390 also have
  strong *negative* phenotypes on aromatic carbon sources and in bioreactor runs, which PP_2389
  entirely lacks — so insertions in PP_2389 are not simply polar on PP_2388.

Reading: the phenotype is reproducible and real, but it is a gain of fitness on loss, shared
with the regulator and exporter of the same locus. That is the signature of a **costly,
co-regulated module** whose deletion helps under nitrogen stress, not of a gene that helps use
2-aminobutyrate or methionine. It constrains nothing about molecular activity.

## Verdict on the dashboard call

Call: *"Cytoplasmic YqcI/YcgG family protein associated with fitness modulation during
utilization of DL-2-aminobutyrate and L-methionine as nitrogen sources."*

**Recommended verdict: supported but under-called** (dashboard button 3, "under-called"; the
evidence available in the literature supported a more specific call).

Corrected annotation as I would write it:

> YqcI/YcgG family heme-thiolate N-hydroxylase (predicted; conserved Cys46 heme ligand),
> substrate undetermined; cytoplasmic. Encoded with the LysE-family exporter PP_2388 and the
> divergent LysR-family regulator PP_2390, with which it shares a gain-of-fitness phenotype on
> amino acids as nitrogen sources.

What the call got right: the family assignment, the cytoplasmic localization, every fitness
number, and — importantly — its own restraint. The reasoning trace explicitly refuses a
transporter or catabolic-enzyme assignment and notes that beneficial disruption does not
establish a regulatory mechanism. The GO extractor likewise refused to convert the fitness
association into a nitrogen-utilization process term. Both were the right decisions.

Two criticisms:

1. The annotation's headline rests on a fitness association that is not gene-specific. The same
   phenotype belongs to at least three genes of the locus, and the gene has no specific
   phenotype flag. Phrasing it as "associated with fitness modulation during utilization of..."
   invites a reader to infer a catabolic role that the data do not support.
2. More substantively, the call treats the family as functionless. It had the sequence evidence
   for a heme N-hydroxylase and missed it. This is not really the model's fault: the dashboard's
   PaperBLAST panel returned nothing for this protein, and the InterPro and eggNOG descriptions
   it was given still read "uncharacterised" (InterPro IPR014988's description has not been
   updated since AglA was characterized in 2022). The family-characterization literature was
   simply not in the evidence shown.

GO terms predicted by the dashboard (1 term):

- **GO:0005737 cytoplasm — COR** (confidence 2). Correct and novel: GOA holds no annotations for
  Q88KA1, DeepTMHMM finds no signal peptide or TM segment, and the characterized homologs are
  soluble. Not a localization default — nothing in the sequence points elsewhere.

The companion gene review adds, as NEW by sequence similarity (ISS), GO:0020037 heme binding and
GO:0004497 monooxygenase activity, both hedged in their `reason` fields as homology-only.

## Caveats

- Everything about the enzymology is inference at 34-38% identity, from proteins in
  natural-product pathways that PP_2389 does not share. The alignments are pairwise
  Smith-Waterman, not a curated family MSA or a structure superposition; the Cys46 assignment
  rests on motif correspondence, not on a solved or modelled PP_2389 structure. An AlphaFold
  model of Q88KA1 exists and would be the natural next check.
- Only abstracts were read for PMID:35616638; the AglA full text (PMC12866846) was read for
  residue details.
- No *Pseudomonas* YqcI/YcgG protein has been assayed, and the conservation panel found homologs
  in only one organism, so the dashboard's own breadth evidence says nothing here.
- The obvious experiments: heterologous expression with UV-visible spectroscopy for a
  thiolate-heme Soret band and ferrous-CO shift, as was done for DcsA; and a substrate screen
  over guanidine-containing metabolites (arginine, agmatine, guanidinobutyrate).

## Reproduce

From `~/ai-gene-review` on branch `hackathon/putida-batch` (run `unset VIRTUAL_ENV` first):

```bash
just fetch-gene PSEPK PP_2389 --uniprot-id Q88KA1
just deep-research-claude-code PSEPK PP_2389
for p in 35616638 41221789 22547619 35583956 38810110 31150226; do just fetch-pmid $p; done
# fetch-fitness fails (Fitness Browser returns 403); from projects/hackathon/ instead:
uv run beril run --name pp2389-fitness -- bash -c \
  'python3 -I ~/ai-gene-review/genes/PSEPK/PP_2389/PP_2389-bioinformatics/fb_fitness.py $BERIL_RUN_DIR/data'
uv run beril run --name pp2389-family-align -- bash -c \
  'cd ~/ai-gene-review && unset VIRTUAL_ENV && uv run python -I \
   genes/PSEPK/PP_2389/PP_2389-bioinformatics/family_align.py \
   /home/cmungall/.beril/projects/hackathon/user_data/dashboard_calls/NZ_CP026332.1_3351.fasta \
   $BERIL_RUN_DIR/data'
just validate PSEPK PP_2389
just validate-references genes/PSEPK/PP_2389/PP_2389-ai-review.yaml
just validate-terms genes/PSEPK/PP_2389/PP_2389-ai-review.yaml
just validate-predictions genes/PSEPK/PP_2389/PP_2389-dashboard-predictions-review.yaml
just render PSEPK PP_2389
```

## QC status

All clean: `validate` valid (0 errors), `validate-references` 0 issues (6 snippets, 4 titles
checked), `validate-terms` passed, `validate-predictions` 0 errors / 0 warnings (4 titles,
2 quotes verified), `validate-prediction-terms` no issues, `render` wrote
`PP_2389-ai-review.html`, `validate-history` passed.

## Tooling problems

- `just fetch-gene` timed out once against EBI and succeeded on retry.
- `just fetch-fitness` failed: no FEBA source reachable. `fit.genomics.lbl.gov` returns HTTP 403
  and there is no local FEBA database. Worked around by querying the BERDL lakehouse copy of the
  Fitness Browser (`kescience.fitnessbrowser`) over the MCP REST endpoint.
- That endpoint rejects requests without a browser-like `User-Agent` (HTTP 403) and caps `limit`
  at 1000, so `fb_fitness.py` paginates.
- `DESCRIBE <table>` returns an empty result set through the REST query endpoint; use
  `SELECT *` with a limit to learn a schema. Note that the endpoint lower-cases returned column
  names while accepting camel-case in queries.
- No deep-research API keys are set, so the `claude-code` provider was used.
