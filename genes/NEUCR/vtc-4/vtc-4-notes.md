# vtc-4: biological evidence

VTC-4 is the catalytic polyphosphate-polymerase subunit of the vacuolar transporter chaperone complex. Its SPX regulatory domain, central VTC catalytic domain, and membrane-spanning region support ATP-dependent polyphosphate synthesis coupled to storage in the vacuolar lumen. Tagged Neurospora crassa VTC-4 occurs in prevacuolar compartments and the tubular and spherical vacuolar network. Conserved fungal Vtc4 mechanisms include inositol-phosphate sensing and contributions to vacuolar membrane traffic.

- fungal-type vacuole membrane: Tagged target VTC-4 is observed with the vacuolar ATPase in prevacuolar compartments and the tubular and spherical vacuolar network, supporting fungal vacuole membrane residence.
- inositol hexakisphosphate binding: The target SPX domain and Vtc4 subfamily assignment justify transfer from the InsP6-bound Chaetomium thermophilum Vtc4 SPX structure, PDB 5IJP. Binding to InsP6 is distinct from claiming it is the most potent physiological activator.
- calmodulin binding: Budding-yeast Vtc4 central-domain binding to calmodulin was tested directly. The conserved Vtc4 central domain supports this partner-binding inference, which is ancillary to polyphosphate polymerization.
- vacuolar membrane: The native fungal VTC-4 localization supports the more specific fungal-type vacuole membrane term.
- endoplasmic reticulum: Budding-yeast VTC occupies the ER and redistributes to vacuoles on autophagy induction. Conserved Vtc4 complex membership supports the IBA/orthology inference as a secondary location; the direct N. crassa experiment establishes vacuolar/PVC localization and does not exclude an ER pool.
- polyphosphate metabolic process: The catalytic Vtc4 subfamily specifically synthesizes polyphosphate by extending a phosphate chain using ATP, making biosynthesis more precise than metabolism.
- polyphosphate biosynthetic process: The target has the Vtc4 catalytic subfamily architecture, distinct from the noncatalytic Vtc2/Vtc3 relatives. Primary structural and mutational characterization of fungal Vtc4 establishes ATP-dependent phosphate-chain polymerization and supports conserved polyphosphate synthesis.
- vacuolar transport: Vtc4 participates in a membrane complex coupling polymer production to vacuolar delivery; its target vacuolar/PVC localization and conserved VTC polymerase-translocation mechanism support vacuolar transport.
- polyphosphate kinase activity: The target has the Vtc4 catalytic subfamily architecture, distinct from the noncatalytic Vtc2/Vtc3 relatives. Primary structural and mutational characterization of fungal Vtc4 establishes ATP-dependent phosphate-chain polymerization and supports conserved polyphosphate synthesis.
- microautophagy: The characterized yeast VTC complex is required for microautophagic vesicle scission. Conserved Vtc4 complex membership supports transfer of this membrane-traffic contribution as a secondary process, distinct from its primary polymerase activity.
- vacuolar transporter chaperone complex: The Vtc4-specific family assignment, SPX-VTC-membrane architecture, and native vacuolar localization support membership in the conserved VTC polymerase/translocation complex.

Primary evidence excerpts

- [PMID:26453652] “Vacuolar
membrane proteins, such as the vacuolar ATPase (VMA-1) and the polyphosphate
polymerase (VTC-4), were observed in the PVCs.”
- [file:NEUCR/vtc-4/vtc-4-primary-excerpts.md] “both tagged proteins in the PVCs and the tubular vacuolar network”
- [file:NEUCR/vtc-4/vtc-4-PDB-5IJP.json] “Crystal structure of the SPX domain of Chaetomium thermophilum Vtc4 in complex with inositol hexakisphosphate (InsP6).”
- [file:NEUCR/vtc-4/vtc-4-uniprot.txt] “DR   InterPro; IPR004331; SPX_dom.”
- [file:NEUCR/vtc-4/vtc-4-primary-excerpts.md] “bound to Cmd1p-Sepharose in the presence and in absence of free Ca2+.”
- [PMID:17079729] “The VTC
complex is present on the ER and vacuoles and at the cell periphery. On
induction of autophagy by nutrient limitation the VTC complex is recruited to
and concentrated on vacuoles.”
- [file:NEUCR/vtc-4/vtc-4-uniprot.txt] “DR   PANTHER; PTHR46140:SF1; VACUOLAR TRANSPORTER CHAPERONE COMPLEX SUBUNIT 4-RELATED; 1.”
- [PMID:19390046] “Nucleotide- and phosphate-bound structures suggest that the enzyme
functions by metal-assisted cleavage of the ATP gamma-phosphate, which is then
in-line transferred to an acceptor phosphate to form polyP chains.”
- [PMID:17079729] “Deletion of the VTC complex blocks microautophagic uptake into vacuoles. The
mutants still form autophagic tubes but the production of microautophagic
vesicles from their tips is impaired.”

Provenance: live API snapshot 2026-09-09T03:00:51.831347+00:00. Complete API prediction JSON and all emitted claim IDs, text, and original evidence are preserved in the source and provenance JSON files. Current sequence/annotation data are separate comparison snapshots. Annotation overlap records known biology, not demonstrated training membership. All seven gene-focused Falcon jobs completed; the provider reports were inspected and useful primary leads checked. Publication retrieval used Europe PMC metadata/XML when the canonical PubMed fetch returned HTTP 429.

The Falcon report missed PMID:26453652 target microscopy and reverses the yeast structural stoichiometry in one passage; neither statement is adopted. PDB/primary experiments support the biological conclusions used here.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q7SCX0 is the full-length canonical product of NCU08110 (771 aa, sequence version 3; SPX 1-151,
VTC catalytic domain, three C-terminal TM helices 672-763). Not a fragment, isoform or alternative gene
model. No N. crassa functional assay of polyP synthesis exists; the only target experiment is
localization [PMID:26453652 "Vacuolar membrane proteins, such as the vacuolar ATPase (VMA-1) and the
polyphosphate polymerase (VTC-4), were observed in the PVCs."].

Evolutionary grounding (new analysis, vtc-4-bioinformatics/RESULTS-rereview.md, script
vtc_placement_rereview.py): MAFFT + NJ tree of SPX-VTC proteins puts VTC-4 with C. thermophilum Vtc4
(80.5% id), then S. cerevisiae Vtc4 / S. pombe vtc4 (~57%), separate from the Vtc2/Vtc3 clade (PANTHER
PTHR46140:SF2), which contains the N. crassa paralog NCU01745 (Q1K5R9). VTC-4 retains all eight yeast
Vtc4 catalytic/ATP-binding positions (UniProt P47075 FT from PMID:19390046), including active-site K462
(= yeast K458), which yeast Vtc2 (I) and Vtc3 (L) have lost. SPX InsP-binding motif conserved.

Correction to the earlier review: the earlier text called PTHR46140:SF1 a "Vtc4 catalytic subfamily
distinct from Vtc2/Vtc3"; SF1 also contains short Vtc1 and Vtc5 entries (see the PANTHER family review
interpro/panther/PTHR46140/PTHR46140-review.yaml), so SF1 membership alone does not justify the catalytic
transfer. The transfer now rests on the tree and the conserved active site. No disagreement on VTC-4's
subfamily placement; I agree with the family review that SF1 is not a sufficient boundary for
polyphosphate kinase activity.

Action changes: inositol hexakisphosphate binding ACCEPT -> KEEP_AS_NON_CORE (regulatory SPX ligand
binding; inositol pyrophosphates are the stronger physiological activators [PMID:27080106]). Vacuolar
transport kept ACCEPT and now justified by synthesis-coupled polyP import [PMID:25315834 "the VTC complex
obligatorily couples synthesis of polyP to its import in order to avoid toxic intermediates in the
cytosol"]; added to core function. All other actions unchanged; reasons added to every row.
PMID:25315834 and PMID:27080106 newly cited.

Relative to review next: S. cerevisiae VTC4 (P47075), same Vtc4 clade (PTHR46140:SF1, NJ tree), the
experimentally characterized catalytic subunit; no review in the repo (genes/yeast/VTC4 absent).
Modules: none in modules/ cover VTC/polyphosphate storage.
