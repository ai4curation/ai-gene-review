# MAPK1 notes

Initial Falcon pass, 2026-05-12. MAPK1/ERK2 started as a fully pending review
with 276 existing annotations, so this pass focuses on the safest term-level
curation rather than attempting a primary-source review of every substrate,
interaction, Reactome, and phenotype annotation.

Core molecular function: MAPK1 is ERK2, an ATP-dependent serine/threonine MAP
kinase. Falcon summarizes the core enzymology as direct ATP-dependent
phosphotransfer [file:human/MAPK1/MAPK1-deep-research-falcon.md "ERK2 is a
Ser/Thr MAPK that transfers the γ-phosphate of ATP to Ser/Thr-Pro motifs; like
other protein kinases it binds ATP in an active-site cleft, with MgATP2−
serving as the relevant phosphoryl donor in vitro."]. I therefore accepted MAP
kinase activity, protein serine/threonine kinase activity, ATP binding, and
protein phosphorylation, while modifying broader or incomplete kinase terms to
the specific MAP kinase/serine-threonine kinase terms.

Core process: the most defensible biological process is canonical ERK/MAPK
cascade signal transduction. Falcon places ERK2 downstream of Ras-RAF-MEK and
growth-factor inputs [file:human/MAPK1/MAPK1-deep-research-falcon.md "ERK2 is
consistently positioned as a downstream effector in the Ras–Raf–MEK–ERK signal
transduction cascade, converting extracellular cues (including growth
factors/serum) into intracellular phosphorylation events and responses."]. I
accepted ERK1 and ERK2 cascade, MAPK cascade, and intracellular signal
transduction, and kept receptor-specific contexts such as EGFR/ERBB/insulin
signaling as non-core.

Core localization: the best-supported localizations are cytoplasmic/cytosolic
localization in unstimulated cells plus stimulus-dependent nuclear
accumulation. Falcon states that ERK is mainly cytoplasmic in quiescent cells
and accumulates in the nucleus after activation
[file:human/MAPK1/MAPK1-deep-research-falcon.md "ERK is predominantly
cytoplasmic in quiescent cells and accumulates in the nucleus after activation
by certain stimuli; nuclear ERK phosphorylates nuclear targets and contributes
to induced gene expression programs."]. I accepted cytoplasm, cytosol, nucleus,
and one nucleoplasm row with this stimulus-dependent caveat. Most repetitive
Reactome cytosol/nucleoplasm rows and more specific compartments remain pending
unless later primary-source review supports a stronger decision.

Over-annotation cautions: Falcon explicitly warns that downstream proliferation,
differentiation, apoptosis, migration, developmental, transcriptional, and
disease terms are often ERK pathway outcomes rather than direct MAPK1
functions [file:human/MAPK1/MAPK1-deep-research-falcon.md "Many sources link
ERK signaling to proliferation/differentiation and disease contexts, but these
are typically emergent outcomes of the pathway rather than direct MAPK1
enzymatic functions."]. I marked a small set of automated broad developmental
or transcriptional annotations as over-annotated and retained some source-backed
downstream processes as non-core.

Protein binding: MAPK1 has many reported interacting partners, but the generic
GO:0005515 term is not useful for this gene. Falcon notes that ERK docking is
motif/exosite-mediated and that generic protein binding risks over-annotation
[file:human/MAPK1/MAPK1-deep-research-falcon.md "Because docking is
motif-driven and structurally/biochemically dissectable, using only “protein
binding” is typically uninformative and risks over-annotation."]. I left the
generic protein-binding rows pending for partner-specific follow-up, while
keeping the more informative phosphatase-binding term as non-core.

Left for later: a source-level review should triage individual substrates,
protein interactions, Reactome location rows, and old TAS/NAS phenotype rows.
Several annotations remain PENDING where I did not inspect the primary
publication.
