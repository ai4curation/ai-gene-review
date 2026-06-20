# ATAD1 Notes

## 2026-06-03 Proteostasis PN review

Falcon deep research was attempted with the required `perplexity-lite` fallback.
Falcon timed out after 600 seconds and the fallback failed with a Perplexity API
quota error, so this review uses cached primary evidence, UniProt, Reactome, and
the local PN projection reports rather than a generated Falcon research artifact.

ATAD1 is a strong fit for the mitochondrial proteostasis batch, but the safest
core term remains the existing specific process `GO:0140570` extraction of
mislocalized protein from mitochondrial outer membrane. The direct ATAD1/Msp1
paper says human ATAD1 limits mitochondrial mislocalization of PEX26 and GOS28
and proposes ATAD1/Msp1 as mitochondrial protein quality-control factors that
promote extraction and degradation of mislocalized tail-anchored proteins
[PMID:24843043 "human ATAD1 limits the mitochondrial mislocalization of PEX26
and GOS28"; PMID:24843043 "promote the extraction and degradation of
mislocalized TA proteins"].

The PN projection report proposes `GO:0035694` mitochondrial protein catabolic
process for ATAD1 from
`Mitochondrial proteostasis|Organelle-specific protein degradation|mitoCPR
pathway`. This is a class-level propagation, and the mapping audit flags this
source as requiring manual gene-level review before changing a review. I accepted
the projected term only as a broad `NEW` candidate because PMID:24843043 supports
degradation as the downstream outcome, not because the PN source alone is
sufficient. I used TAS rather than IMP for this candidate because the cached
paper text supports a traceable degradation claim, while the explicit
protein-level knockout evidence available in the cached abstract is from mouse
tissue. It should not replace `GO:0140570`, which is the sharper mechanism.

Peroxisomal membrane localization is retained as non-core. UniProt reports
peroxisome membrane localization and Reactome lists ATAD1 as a class I
peroxisomal membrane protein bound by PEX19, but the current evidence does not
establish peroxisomal substrate extraction as ATAD1's primary function
[file:human/ATAD1/ATAD1-uniprot.txt "Peroxisome membrane";
Reactome:R-HSA-9603804 "ATAD1 (Liu et al. 2016)"].

The synaptic/behavioral block is treated conservatively. UniProt summarizes
mouse-derived AMPAR trafficking, synaptic plasticity, learning, and memory
biology by similarity, and human ATAD1 encephalopathy provides disease context
[file:human/ATAD1/ATAD1-uniprot.txt "Required for NMDA-stimulated AMPAR
internalization"; PMID:29659736 "ATAD1 encephalopathy and stiff baby syndrome"].
I kept postsynaptic/receptor-internalization terms as non-core and marked the
high-level learning/memory annotations as over-annotations.

## Falcon deep research findings (2026-06-07)

A Falcon (Edison Scientific) deep research report was generated successfully (the
earlier 2026-06-03 run had failed). It largely CONFIRMS the existing review but
adds several mechanistic/translational findings that were not previously cited.
Key synthesis (CONFIRMS / NEW / PROVISIONAL labels are relative to the prior
review):

- CONFIRMS core function. ATAD1/Msp1 is a hexameric OMM AAA+ extractase that
  uses ATP hydrolysis to thread membrane-embedded substrates (especially
  mislocalized tail-anchored proteins, e.g. PEX26/GOS28, and stalled import
  substrates) through its central pore for rerouting or degradation
  [PMID:24843043 "human ATAD1 limits the mitochondrial mislocalization of PEX26
  and GOS28"]. This is already the accepted core (GO:0140567, GO:0140570).

- NEW (human, direct, primary): ATAD1 directly and selectively extracts the
  pro-apoptotic BH3-only protein BIM from mitochondrial membranes to inactivate
  it; extraction is ATP-dependent, requires membrane anchoring, and is selective
  (BIM extracted but not BIK/PUMA/Fis1 under the same reconstituted conditions;
  lost in the catalytic E193Q mutant). This connects ATAD1 to apoptotic priming
  and to a cancer "collateral lethality" with PTEN (10q23 co-deletion):
  ATAD1-null cells/xenografts are hypersensitized to proteasome inhibitors via
  BIM-dependent apoptosis [PMID:36409067 Winter et al. 2022 eLife, doi:10.7554/eLife.82860
  "ATAD1 directly and specifically extracts the pro-apoptotic protein BIM from
  mitochondria to inactivate it"]. This is a genuinely new molecular substrate
  axis and a new disease/translational link not in the prior review.

- NEW (human, structural/mechanistic, primary): Cryo-EM of human ATAD1 bound to
  a peptide substrate shows phylogenetically conserved pore-loop aromatics
  (pore-loop 1 W166/Y167) are required to grip hydrophobic substrate and cannot
  be replaced by aliphatic residues; a C-terminal alpha-helix promotes
  oligomerization, specializing ATAD1 among AAA proteins [PMID:35550246 Wang et
  al. 2022 eLife, doi:10.7554/eLife.73941 "both aromatic amino acids in pore-loop 1
  are required for ATAD1's function"]. Mechanistic support for the dislocase /
  ATP-hydrolysis core via yeast Msp1 structure [PMID:31999255 Wang et al. 2020
  eLife, doi:10.7554/eLife.54031] and processive bidirectional translocase /
  unfoldase activity, dependent on hexamerization and inhibited by Pex3
  [PMID:32541053 Castanzo et al. 2020 PNAS, doi:10.1073/pnas.1920109117].

- NEW/CONFIRMS (pathway coupling): Extracted TA proteins are not obligatorily
  degraded; they can be rerouted to the ER via the GET/TRC (Get3) pathway as an
  intracellular "proofreading" system, or handed to ubiquitin-proteasome
  (Cdc48) clearance [Matsumoto 2023 J Biochem doi:10.1093/jb/mvad025;
  Matsumoto et al. 2019 Mol Cell doi:10.1016/j.molcel.2019.07.006 — yeast Msp1].
  The 2019 Mol Cell DOI did not resolve to a confirmed PMID via PubMed and is
  yeast-focused, so I am NOT adding it to references; kept in notes only.

- PROVISIONAL (homolog, not human): A fission-yeast ATAD1 ortholog (Yta4) was
  reported to inhibit excessive mitochondrial fission by acting on divisome
  components Fis1/Mdv1/Dnm1 — a role beyond proteostasis [He et al. 2023 PLOS
  Biology, PMID:37590302, doi:10.1371/journal.pbio.3002247]. Because this is the
  Schizosaccharomyces homolog rather than human ATAD1, I treat it as
  hypothesis-generating only and do NOT use it to add/modify human annotations.

- PROVISIONAL (preprint / database): A 2024 bioRxiv preprint proposes Msp1
  substrate recognition by hydrophobic mismatch with TMD extraction as the
  rate-limiting step [Fresenius et al. 2024 bioRxiv doi:10.1101/2023.07.11.548587];
  Open Targets lists ATAD1 with hyperekplexia 4 / neurodegenerative terms. These
  are preprint/database-level and explicitly NOT used to change annotations.

- CONFIRMS (neuronal axis): The Wang & Walter 2020 review compiles the
  noncanonical neuronal role — ATAD1/Thorase forms complexes with GluR2 and
  GRIP1 and disassembles GluR2-GRIP1 in an ATP-dependent manner, regulating
  surface AMPAR levels and activity-dependent synaptic downscaling
  [Wang & Walter 2020 Annu Rev Cell Dev Biol doi:10.1146/annurev-cellbio-031220-015840].
  This supports keeping the existing AMPAR/postsynaptic annotations as non-core
  (no change warranted).

Conservative actions taken in the YAML: added the four human-relevant primary
references (PMID:36409067, PMID:35550246, PMID:31999255, PMID:32541053) as
statement-only (full_text_unavailable, no supporting_text since none are cached
locally); added one suggested question (BIM/apoptosis axis) and one suggested
experiment (selective BIM extraction). No existing annotation actions were
changed — all new findings reinforce rather than contradict the current calls.
