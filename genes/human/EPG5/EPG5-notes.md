# EPG5 notes (human, Q9HCE0)

Deep research: not run (falcon times out after 600 s in this environment and perplexity-lite is not
installed). Review based on cached publications, the UniProt record and PubMed abstracts.

## Key findings
- Rab7 effector setting autophagosome fusion specificity [PMID:27588602 "EPG5 is recruited to late endosomes/lysosomes by direct interaction with Rab7 and the late endosomal/lysosomal R-SNARE VAMP7/8"].
- Binds LC3 and STX17-SNAP29; stabilizes trans-SNAREs [PMID:27588602 "EPG5 stabilizes and facilitates the assembly of STX17-SNAP29-VAMP7/8 trans-SNARE complexes, and promotes STX17-SNAP29-VAMP7-mediated fusion of reconstituted proteoliposomes"]. Full text not cached (abstract only).
- Vici syndrome; autophagosome clearance block [PMID:23222957 "Further studies showed a severe block in autophagosomal clearance in muscle and fibroblasts from individuals with mutant EPG5"].
- mEPG5 needed for degradative autolysosomes [PMID:20550938 "EI24 and mEPG5 are required for formation of degradative autolysosomes."].
- Autophagy-independent endolysosomal delivery of CpG to TLR9 compartments [PMID:29130391 "Here we show that EPG5 also plays autophagy-independent roles in the trafficking of molecules from the EEs to LEs and lysosomes."].

## Decisions
- nucleotide transport (IMP) -> MODIFY to endosome to lysosome transport: cargo is a CpG oligonucleotide inside vesicles.
- cellular response to dsDNA -> over-annotated; TLR9 pathway kept as non-core (acts upstream).
- NEW: vesicle membrane tethering activity (core MF), small GTPase binding, SNARE binding (all from PMID:27588602).


## 2026-10-24 original-source augmentation

The earlier entries above are retained as historical notes. The current assessment supersedes the earlier dsDNA over-annotation decision and tethering-core confidence; precise sources and access limits are recorded in [EPG5-source-guide.md](EPG5-source-guide.md).

All 12 imported annotations and the three inherited proposed annotations remain in their original order with unchanged source fields. All 33 inherited YAML supporting-text occurrences remain unchanged, as do both splice isoforms. No publication quotations were added. The follow-up adds one directly supported LC3/GABARAP-binding annotation after the 15 historical records. There are now 15 active records: three ACCEPT, four KEEP_AS_NON_CORE, four MODIFY, one UNDECIDED and three NEW; the retired historical proposal retains its UNDECIDED assessment. The computed status is documented with the validation result below.

The 2017 human original establishes RAN association in cell extracts, perinuclear localization, and EPG5-dependent vesicular CpG delivery. Supported generic RAN binding is retained as non-core under campaign policy. Localization is not dismissed because the proposed karyopherin mechanism remains unproven. Nucleotide transport is refined to endosome-to-lysosome transport. The TLR9 phenotype supports a contextual trafficking contribution. The dsDNA-response row remains unresolved: the signaling reagent is single-stranded CpG ODN, while the separate dsDNA baculovirus assay integrates multiple trafficking and expression steps. No reasoning depends on the imported relationship qualifier.

The original 2016 supplement directly demonstrates human-fragment Rab7 binding and binding to SNAREs/assembled SNARE complexes, with human-cell association and knockdown evidence. The proteoliposome lipid-mixing system instead uses worm proteins. The main article remains unavailable; the recovered supplement and main Figure 6 image do not remove that limitation. The inherited small-GTPase-binding and SNARE-binding proposals are retained. The inherited vesicle-tethering proposal is UNDECIDED, not removed: a current valid term requires physical membrane bridging, and the inspected evidence does not isolate this activity for human EPG5.

Independent human structural originals from 2021 and 2025 support elongated architecture and GABARAP interaction. The 2025 full-length-cell and peptide results revise the earlier speculative multivalent LIR model; modeled unresolved loops are not direct structural contacts. Both papers support a tethering model without providing an isolated human membrane-bridging assay. Their normal publication files were genuinely fetched as separate additions; all 16 preexisting archived/runtime publication files remained exact.

The first core now uses directly supported SNARE binding at the lysosomal membrane in autophagosome-lysosome fusion/clearance. The second remains endocytic cargo delivery, with no invented distinct molecular function. No nuclear carrier, kinase, nucleic-acid sensor, transporter, universal binary partner binding or equivalent activity of the shorter splice isoform is inferred.

Actual PAINT topology/MSA and the current IBD export support the cytoplasmic and lysosomal location inferences. The displayed human sequence matches exactly. The imported fusion IBA remains in current QuickGO, but its corresponding IBD was not recovered from that export; the fish record is itself IBA. This provenance gap is explicit, while biological acceptance rests on independently read human originals. No target self-WITH or donor-count objection is used. No negated record was found on the inspected target path within the available IBD export; a separate NOT export was not recovered.

Reviewer reference flags record main-original access rather than modifying normal cache metadata. PMID:27588602 remains main-full-text unavailable despite the recovered supplement; PMID:20550938 remains abstract-only in this assessment. The two new structural references use exact genuinely fetched titles. Original findings and quotations are preserved as prior provenance. The source guide documents the original access and evidence limits. Validation and history records accompany the completed review.


## Inherited proposal withdrawal, 2026-10-24

The inherited curator-authored GO:7770062 vesicle membrane tethering activity proposal is marked `retired: true`. It is withdrawn from active proposed annotations because isolated human membrane-bridging activity remains unresolved. This is retirement of our historical proposal, not a claim that GOA withdrew a source row: the assertion was never among the 12 imported GOA contexts. Its UNDECIDED review, original term/evidence/reference fields and every inherited supporting quotation remain intact at the same YAML paths. No machine-sourced row is retired or altered.

At the initial retirement step, the document contained 14 active annotation records (12 imported and two retained NEW binding proposals) plus one retired unresolved historical proposal. At that step, active actions were six ACCEPT, four KEEP_AS_NON_CORE, one MODIFY, one UNDECIDED and two NEW; the retired record carries the second UNDECIDED assessment. All 33 inherited quotation values and paths remain unchanged. The preexisting suggested question and experiment continue to address whether human EPG5 can bridge membranes directly. This metadata correction makes no new biological assertion and changes neither core function.

Canonical validation on 2026-10-24: normal review validation, strict GO-term validation, computed-status check and HTML rendering all passed. The existing HTML was refreshed; source files and publication caches were preserved.


## Follow-up review, 2026-10-24

The biological summary now names Rab7, VAMP7/8, autophagic SNARE assemblies, fusion specificity, LC3/GABARAP recognition, nucleic-acid delivery and the disease spectrum. The 2,579-residue length and neurodevelopmental disorder with movement abnormalities are also recorded in the unchanged UniProt source. This replaces access-oriented prose in the description with a standalone biological account.

Direct human LC3/GABARAP interaction now has a specific NEW molecular-function annotation, GO:0032182 ubiquitin-like protein binding. PMID:33674710 Figure 2 measures purified full-length human EPG5 binding to the six human ATG8-family proteins; PMID:39809444 Figure 3C tests full-length EPG5 LIR mutants in human cells. The latter supports LIR1 as the main GABARAP-contact determinant without assigning simultaneous binding to both motifs. This addition supplies molecular coverage from direct interaction experiments; it makes no new process assertion.

The specific SNARE-binding core is retained after checking GO:0030674 protein-macromolecule adaptor activity and GO:0043495 protein-membrane adaptor activity. The first requires bringing two or more macromolecules together for coordinated function; the second requires localizing a partner or complex to a membrane. Human EPG5 binding preferentially to an assembled SNARE complex (PMID:27588602 S6O–Q) could reflect recognition or stabilization, while reduced STX17–VAMP7 association after depletion (S6T) does not isolate direct bridging. GABARAP-dependent recruitment of EPG5 establishes recruitment of EPG5 itself, not recruitment of a third partner by EPG5. Together with the worm reconstitution these findings support an adaptor model, but the available human experiments do not resolve its precise molecular operation. This is an evidence-specific judgment, not a general demand for purified human reconstitution before any conserved function can be accepted. Specific SNARE binding is informative and is distinct from generic protein binding. The existing experimental question retains the adaptor/tethering uncertainty.

The endocytic core now states that its molecular activity has not been distinguished from the autophagic Rab7/SNARE mechanism. No additional molecular function is invented to fill that field.


### 2026-10-24: source-specific feedback follow-up

The three existing lysosome contexts are refined to lysosomal membrane using the actual human EPG5 Figure S3 localization in PMID:27588602 and corroborating PMID:29130391 Figure 4. The latter alone resolves the compartment less precisely; the original S3D/I-N evidence supplies the membrane localization. This does not assert an integral membrane topology.

The dsDNA-response annotation remains UNDECIDED after rereading the accessible original. CpG/TLR9 signaling used single-stranded ODN, while baculovirus transduction measured a composite trafficking/expression outcome. The uncertainty concerns the exact dsDNA-specific response, not article access, nor a general prohibition on trafficking contributions to signaling. RAN association remains supported non-core binding under the project's standing policy; its original reference is now explicitly linked in the review.

The SNARE species distinction is documented in the original supplement Methods, not inferred from abbreviations in the S6U/V caption. Protein expression/purification on PDF page 27 identifies C. elegans STX-17/SNAP-29/VAMP-7 separately from human hSTX17/hSNAP29/hVAMP7/hVAMP8. SNARE reconstitution on page 30 uses STX-17/SNAP-29 with VAMP-7 and RAB-7-Sec61β; the lipid-mixing procedure on page 31 uses EPG-5. The human fragment/complex assays in S6O-Q remain independent evidence.

The combined follow-up preserves all 12 imported source contexts, the three historical proposals, both splice isoforms and the exact paths and values of all 33 inherited supporting quotations. One new molecular-binding row brings the current total to 15 active records plus one retired proposal. The three lysosomal-membrane refinements support both core locations.


### 2026-10-24: independent dsDNA-scope adjudication

An independent review reread the accessible human original and inspected Figure 6B (journal page 30). Current GO:1990786 covers cellular state/activity changes caused by dsDNA and has direct parents response to dsDNA (GO:1990784) and cellular response to nitrogen compound (GO:1901699); it is not restricted to immune signaling. The BacMam reporter assay combines delivery, release, nuclear access and expression of a dsDNA template. Both DNA and RNA vectors are impaired, so the experiment does not isolate a dsDNA-elicited host response. At the same time, EPG5 performs positive trafficking work, and a categorical exclusion from the broad response process is not established. UNDECIDED therefore retains a specific unresolved stimulus-versus-template interpretation, rather than claiming the evidence is inaccessible or requiring EPG5 to be a direct DNA sensor. The expert question now identifies that precise boundary and the intended Figure 6B step.

The inherited TLR9/TLR7 supporting quotation is explicitly identified as contextual evidence for the separate single-stranded-ODN signaling experiments, not proof of dsDNA specificity. All 33 inherited quotation values and paths remain exact. Three redundant additional-reference entries were removed; their original PMID and supporting citations remain. Source objects, all actions, products and cores are unchanged. Imported relationship labels do not enter the reasoning.
