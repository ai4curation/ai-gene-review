# ASCC2 notes

## 2026-06-03 Proteostasis PN batch review

Fetched human ASCC2 with `just fetch-gene human ASCC2`; GOA seeded 38 review
annotations from 39 GOA rows. Refreshed PMID caching successfully. Falcon deep
research was attempted with `perplexity-lite` fallback; Falcon timed out after
600 seconds and the fallback failed with a Perplexity API quota 401, so no
provider deep-research file was created. This review therefore uses the cached
primary literature, UniProt, Reactome, and the PN projection report directly.

Core synthesis: ASCC2 is a CUE-domain ubiquitin-binding subunit used in two
well-supported ASCC contexts. In the nucleus, ASCC2 recognizes K63-linked
polyubiquitin signals during alkylation damage and helps recruit ASCC repair
machinery [PMID:29144457 "Proper recruitment of the repair complex requires
recognition of K63-linked polyubiquitin by the CUE"]. Loss of ASCC2 impairs
repair kinetics [PMID:29144457 "Loss of this subunit impedes alkylation adduct
repair kinetics"].

In the proteostasis/RQC context, ASCC2 works with ASCC3 and TRIP4 as the human
RQC-trigger complex. Hashimoto et al. identify the trimeric hRQT complex
[PMID:32099016 "The hRQT complex is composed of ASCC3, ASCC2, and TRIP4"].
Juszkiewicz et al. show ASCC disassembles collided ribosomes [PMID:32579943
"disassembles the leading ribosome in an ATP-dependent reaction"]. Narita et al.
connect this to K63-polyubiquitinated uS10 and ASCC2 ubiquitin binding
[PMID:36302773 "ASCC2 specifically interacts with K63-linked polyubiquitin
chains"].

PN projection decision: the PN report projects ASCC2 to `GO:0072344 rescue of
stalled cytosolic ribosome` as already present, and to `GO:0006515 protein
quality control for misfolded or incompletely synthesized proteins` as a
candidate new-to-GOA group-level RQC annotation
[file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv
"ASCC2		Translation|Cytosolic translation|Ribosome-associated QC|Ribosomal
rescue"]. I treated the projection conservatively: keep and support the specific
RQC annotations (`GO:0072344`, `GO:0032790`, `GO:1990116`, `GO:0180022`,
`GO:0070530`), but do not propose adding broad `GO:0006515` because the existing
specific GO annotations already capture ASCC2's proteostasis role.

Annotation decisions:

- `GO:0043130 ubiquitin binding`: MODIFY to `GO:0070530 K63-linked
  polyubiquitin modification-dependent protein binding`.
- `GO:0005515 protein binding`: remove or mark over-annotated depending on
  whether the interaction is high-throughput-only or mechanistically meaningful
  ASCC2-ASCC3 complex evidence.
- `GO:0006260 DNA replication`: REMOVE; the cited evidence supports DNA
  alkylation repair, not ASCC2 involvement in DNA replication.
- Transcription regulation annotations: KEEP_AS_NON_CORE; the ASC-1 complex
  evidence is real [PMID:12077347 "essential role in AP-1, SRF, and NF-kappaB
  transactivation"], but not the core PN-relevant role.

## Falcon deep research findings (2026-06-07)

A Falcon (Edison Scientific) deep-research report was generated on 2026-06-07
(the 2026-06-03 attempt had failed). It does not overturn any existing
annotation decision; it adds mechanistic depth and several primary references
that strengthen the two established core functions. Distinguishing
CONFIRMS / NEW / PROVISIONAL below.

- CONFIRMS (molecular function / CUE specificity): The K63-linkage preference of
  the ASCC2 CUE domain is now backed by quantitative structural/biophysical work
  beyond the references already cited. Lombardi et al. show the CUE domain binds
  K63-linked diUb by contacting BOTH distal and proximal ubiquitin, with strong
  linkage preference (ITC: monoUb Kd ~57 uM; K63Ub2 ~8.7-10.4 uM; K48Ub2 ~98 uM;
  M1/linear diUb ~400 uM), and N-terminal alpha1-helix residues (E467, S470)
  are required for recruitment to alkylation-damage foci
  [PMID:34971705 (Lombardi 2022) "recognizes adjacent ubiquitins in K63-linked
  polyubiquitin"]. Supports the existing GO:0070530 MODIFY/ACCEPT decisions; no
  change needed, but adds a primary structural reference.

- NEW (ASCC2-ASCC3 scaffold interface; disease principle): A dedicated
  structural study maps the ASCC2 N-terminal region (~aa 1-434) as the
  high-affinity (Kd ~3.5 nM) ASCC3-binding module, clasped by the ASCC3
  N-terminal arms, and shows somatic cancer mutations at this evolutionarily
  conserved interface reduce ASCC2-ASCC3 affinity -- a "loss of scaffold
  coupling" disease principle rather than loss of helicase catalysis
  [PMID:33139697 (Jia 2020) "interaction of DNA repair factors ASCC2 and ASCC3
  is affected by somatic cancer mutations"]. This is mechanistic context for the
  ASCC2-ASCC3 interaction (relevant to the GO:0005515 MARK_AS_OVER_ANNOTATED
  decision on PMID:29997253) and to GO:1990391 DNA repair complex. Does not
  change actions; supports representing the interaction via complex/process
  terms rather than generic protein binding.

- NEW (pathway selection / complex modularity): TRIP4 and ALKBH3 bind ASCC3
  mutually exclusively, so the ASCC3 motor is directed either to RQC (TRIP4 /
  RQT complex) or to DNA alkylation repair (ALKBH3 complex); ASCC2 is shared by
  both assemblies as the K63-Ub reader [PMID:37019967 (Jia 2023) "TRIP4 binds
  ASCC3 mutually exclusively with the DNA/RNA dealkylase, ALKBH3"]. This
  reinforces, with a mechanistic basis, why ASCC2 has dual nuclear-repair and
  cytosolic-RQC roles in the review.

- NEW (RQC mechanism refinement): In vitro reconstitution shows ribosomal
  collision is NOT strictly required for ZNF598 ubiquitination or ASCC-mediated
  disassembly; ASCC can split monosomes, polysome queues, and even 48S
  complexes given (i) >=30-35 nt of 3' mRNA downstream of the P site and (ii)
  sufficiently long K63-linked ubiquitin chains on uS10/eS10
  [PMID:38366554 (Miscicka 2024) "Ribosomal collision is not a prerequisite for
  ZNF598-mediated ribosome ubiquitination and disassembly of ribosomal complexes
  by ASCC"]. Consistent with existing GO:0032790 / GO:0072344 / GO:0070530
  decisions; sharpens the mechanism but does not change any action.

- CONFIRMS (RQC synthesis / in vivo vs in vitro tension): A 2024 review
  reiterates ASCC2 CUE-mediated K63-Ub recognition as the recruitment step for
  ASCC ribosome splitting, and notes context-dependence between strong in vitro
  requirement and partial in vivo dispensability of ASCC2 ubiquitin binding
  [PMID:39661518 (Ford 2024) "Ubiquitin-dependent translation control
  mechanisms: Degradation and beyond"]. Supports the existing suggested question
  about whether CUE binding is required under endogenous conditions.

- PROVISIONAL / LOW-CONFIDENCE (disease associations, NOT used to change
  annotations): A pan-cancer analysis reports ASCC2 altered in ~1.8% of 10,967
  tumors with tumor-type enrichments and survival associations
  [PMID(unresolved): Pan et al. 2025, Sci Rep, doi:10.1038/s41598-025-03946-0];
  a prostate-cancer lncRNA/miRNA ceRNA axis (TCONS_00027385/miR-874-5p/ASCC2) is
  preprint-level (doi:10.21203/rs.3.rs-728951/v1) and treated as
  hypothesis-generating only. Open Targets neurodegeneration/diabetes
  associations are GWAS/credible-set level. None of these are used to alter GO
  annotations.

References added to ASCC2-ai-review.yaml (statement-only findings, full text not
fetched): PMID:33139697, PMID:34971705, PMID:37019967, PMID:38366554,
PMID:39661518, PMID:36902118. The Brickner 2019 and Soll 2019 ArXiv/thesis items
and the Soll 2018 JBC paper (already represented as ASCC1 work via PMID:29997253)
were left in notes only. PMIDs for Pan 2025 and the Han 2021 preprint were not
reliably resolved to PubMed IDs and are kept in notes only.
