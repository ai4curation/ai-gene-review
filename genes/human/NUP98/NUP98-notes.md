# NUP98 (human, P52948) review notes

**Provenance note:** Provider deep research for NUP98 failed (Falcon returned HTTP 402
Payment Required; Perplexity not configured). No `NUP98-deep-research-<provider>.md`
file exists. The synthesis below replaces it and was written by the reviewing agent
from the UniProt record (`NUP98-uniprot.txt`) and the cached publications in
`publications/`. All quotes are verbatim from those sources.

## Gene product and processing

- NUP98 encodes a precursor that is autoproteolytically cleaved. Isoforms 1/2 (the
  ~186-kDa Nup98-Nup96 precursor) yield two distinct nucleoporins, Nup98 (N-terminal,
  FG/GLFG-repeat containing) and Nup96 (C-terminal, a scaffold nucleoporin of the
  Nup107-160 "Y" complex); isoforms 3/4 (Nup98-specific) yield Nup98 only.
  [PMID:10087256 "Proteolytic cleavage of the precursor yields two nucleoporins: Nup98, a previously characterized GLFG-repeat containing nucleoporin, and Nup96."]
  [PMID:12191480 "Both forms are processed into two peptides through autoproteolysis mediated by the C-terminal domain of hNup98."]
- GO annotations to P52948 therefore mix two biologically distinct proteins. Annotations
  concerning the Nup107-160 complex, the NPC outer ring, kinetochores in mitosis, and
  NPC scaffold assembly reflect Nup96; those concerning FG repeats, the permeability
  barrier, Rae1, mRNA export, intranuclear GLFG bodies, DHX9 and transcription reflect
  Nup98. No GOA rows in the current file carry an isoform identifier.

## Nup98: FG-repeat permeability barrier and transport

- Nup98 is a GLFG/FG-repeat nucleoporin; its repeat domain provides docking sites for
  transport receptor-cargo complexes. [PMID:7736573 "Nup98 functions as one of several docking site nucleoporins in a cytosolic docking activity-mediated binding of a model transport substrate."]
- The intrinsically disordered Nup98 FG domain is the dominant component of the NPC
  selective permeability barrier (Xenopus), and Nup98 FG domains from diverse species,
  including human, phase-separate into particles with NPC-like permselectivity.
  [PMID:25562883 "The NPC barrier in Xenopus relies primarily on the intrinsically disordered FG domain of Nup98."]
  [PMID:25562883 "All Nup98 FG phases rejected inert macromolecules and yet allowed far larger NTR cargo complexes to rapidly enter."]
- UniProt: [file:human/NUP98/NUP98-uniprot.txt "NUP98 and NUP96 are involved in the bidirectional transport across the NPC"];
  [file:human/NUP98/NUP98-uniprot.txt "The FG repeat domains in Nup98 have a direct role in the transport."]
- mRNA export: Nup98 binds Rae1 via its GLEBS motif; the Rae1-Nup98 complex binds ssRNA.
  [PMID:20498086 "Rae1 and Nup98 are evolutionarily conserved mRNA export factors"]
  [PMID:20498086 "we demonstrate that the complex possesses single-stranded RNA-binding capability"]
  [PMID:28221134 "Nup98 binds to the mRNA export factors Rae1 and NXF1 (TAP) and it has been shown to mediate mRNA export"]
- Protein import/export: [PMID:28221134 "Nup98 also participates in nuclear import and export of proteins though its interaction with importin-β family members"].
  SARS-CoV-2 ORF6 binds Nup98-Rae1 and blocks STAT1/2 import, rescued by Nup98
  overexpression [PMID:33097660 "strongly suggesting that Orf6 specifically targets Nup98 to block STAT nuclear import"].
  ORF6 also traps host mRNA in the nucleus [PMID:33849972 "ORF6's nuclear entrapment of host mRNA is associated with its ability to copurify with the mRNA export factors, Rae1 and Nup98."];
  VSV M protein targets Nup98 to block mRNA export (PMID:11106761).

## Localization

- Nup98 is concentrated on the nucleoplasmic side of the NPC (nuclear basket region) and
  in the NPC core, with a mobile intranuclear pool that accumulates in GLFG bodies.
  [PMID:7736573 "Immunoelectron microscopy showed Nup98 to be asymmetrically located at the nucleoplasmic side of the NPC."]
  [PMID:11839768 "The nuclear basket proteins Nup98 and Nup153 and the cytoplasmic fibril protein Nup358 also were localized at the NE and in intranuclear foci"]
  [PMID:15229283 "Immunogold-labeling for Nup98 also results in preferential labeling of NPC core regions"]
  [PMID:28221134 "Immunofluorescence analysis revealed that Nup98 is visible throughout the nucleoplasm, but can accumulate at intranuclear structures termed GLFG bodies"]
- Nup98 dissociates from NPCs early in prophase and re-assembles in anaphase/telophase
  (PMID:12802065).

## Nup96: scaffold nucleoporin

- Nup96 is a stable member of the Nup107-160 complex (NPC outer rings), essential for NPC
  assembly, and with the complex localizes to kinetochores in mitosis.
  [PMID:15229283 "We show that Nup96 and Nup107 are core elements of the NPC proper that are essential for NPC assembly and docking of Nup153 and Tpr to the NPC."]
  [PMID:15146057 "indicating that most, if not all, Nup96 is stably associated with the Nup107-160 complex during the entire cell cycle"]
  [PMID:15146057 "a specific labeling of Nup96 at kinetochores was already observed during prophase, when Nup96 is mainly localized at the nuclear envelope"]

## Off-pore gene regulation (Nup98)

- Intranuclear Nup98 binds chromatin/transcripts and acts as a cofactor of the helicase
  DHX9, stimulating its ATPase activity and supporting DHX9-dependent transcription and
  splicing. [PMID:28221134 "Importantly, binding of Nup98 stimulates the ATPase activity of DHX9, and a transcriptional reporter assay suggests Nup98 supports DHX9-stimulated transcription."]
  [PMID:28221134 "Nup98 and DHX9 bind interdependently to similar gene loci and their transcripts"]
- NUP98 N-terminal (FG-repeat) fusions to many partners (HOXA9, NSD1, KDM5A, PHF23 etc.)
  are recurrent drivers of AML and other leukemias (UniProt DISEASE notes).

## Disease context (not in description)

- Alzheimer disease: in tangle-bearing neurons Nup98 is reported to mislocalize to the
  cytoplasm with tau, associated with nucleocytoplasmic transport failure (Eftekharzadeh
  et al. 2018, Neuron; not cached here, not cited in the review). This is a pathological
  state; normal Nup98 function is at the NPC and in the nucleoplasm. The core functions
  in the review (FG-repeat permeability barrier, structural constituent of nuclear pore,
  nucleocytoplasmic transport, mRNA export) are the normal functions that such a disease
  node would depend on.

## Curation decisions summary

- Generic `protein binding` IPIs (Rae1, Nup107-160 members, viral ORF6, VSV M,
  interactome screens): REMOVE, except the DHX9 IPI (PMID:28221134), MODIFIED to
  ATPase activator activity (GO:0001671), which the paper directly supports.
- Reactome `cytosol` TAS rows: transport-reaction rows marked over-annotated (Nup98 is a
  pore component, not a cytosolic protein); mitosis-related rows (kinetochore, spindle,
  NPC reassembly) kept as non-core because after nuclear envelope breakdown the Nup96-
  containing Nup107-160 complex and dispersed Nup98 are cytoplasmic.
- `protein carrier activity` and `peptide binding` (IEA from rat Nup98): REMOVE — Nup98
  provides binding sites for transport receptors; it does not deliver cargo.
- `nuclear inclusion body` (aggregate foci): MODIFY to `nuclear body` (GLFG bodies).
- NEW: mRNA export from nucleus (GO:0006406); protein autoprocessing (GO:0016540; the
  C-terminal autoproteolytic domain cleaves its own precursor — the autoprocessing case
  explicitly allowed under proteolysis-type process terms).
