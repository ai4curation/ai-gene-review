# DPM1 review notes

UniProtKB:O60762, human DPM1 (dolichol-phosphate mannosyltransferase subunit 1). 260 aa, chromosome 20. HGNC:3005. Glycosyltransferase 2 family (CAZy GT2, Pfam PF00535, InterPro IPR039528 DPM1-like). EC 2.4.1.83.

Deep research: falcon provider OUT OF CREDITS (HTTP 402) at time of review; no `-deep-research-falcon.md` produced. Review grounded in DPM1-uniprot.txt, seeded GOA, and cached publications/PMID_*.md (all cited PMIDs present; all abstract-only per `full_text_available: false`).

## Core biology (from UniProt + primary literature)

- **Function**: catalytic subunit of the dolichol-phosphate mannose (DPM) synthase complex. Transfers mannose from GDP-mannose to dolichol monophosphate to form Dol-P-Man. [UniProt FUNCTION; PMID:10835346]
  - Reaction (RHEA:21184, EC 2.4.1.83): di-trans,poly-cis-dolichyl phosphate + GDP-alpha-D-mannose = di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate + GDP. [UniProt CATALYTIC ACTIVITY]
- **Dol-P-Man** is the mannosyl donor for: GPI anchor synthesis, lumenal N-glycan mannose additions (ALG3/9/12 branch of the LLO precursor), protein O-mannosylation, and protein C-mannosylation. [PMID:10835346 "generates mannosyl donors for glycosylphosphatidylinositols, N-glycan and protein O- and C-mannosylation"; PMID:9535917; PMID:16280320]
- **Complex**: DPM1 (catalytic) + DPM2 + DPM3. DPM1 lacks a hydrophobic transmembrane domain (unlike yeast Dpm1p) and is tethered to the ER membrane by DPM3 via a C-terminal coiled-coil; DPM2 stabilizes DPM3 and enhances activity ~10x. [PMID:9535917 "lacking a hydrophobic transmembrane domain"; PMID:10835346; PMID:16280320; PMID:9724629]
  - ComplexPortal CPX-6268 "Dolichol-phosphate mannosyltransferase complex"; GO complex term GO:0033185 dolichol-phosphate-mannose synthase complex.
- **Localization**: ER membrane (peripheral/tethered by DPM3). [UniProt SUBCELLULAR LOCATION: Endoplasmic reticulum; PMID:9724629; PMID:16280320]
- **Metal**: binds 1 divalent metal cation (Mg2+/Mn2+/Ca2+), by similarity to Q8U4M3. Multiple GDP-mannose BINDING residues; residue 120 also binds Mg2+/Mn2+. [UniProt COFACTOR/BINDING, ECO:0000250]

## Disease

- **DPM1-CDG / CDG type Ie (CDG1E)**, MIM 608799. Variants R92G, G152V (abolishes DPM3 interaction), S248P. Some patients have dystroglycanopathy-type congenital muscular dystrophy (O-mannosylation defect on alpha-dystroglycan). [PMID:10642597; PMID:10642602; PMID:15669674; PMID:23856421]

## Annotation review decisions (highlights)

- MF: GO:0004582 dolichyl-phosphate beta-D-mannosyltransferase activity = the core catalytic function. ACCEPT all (IBA, IEA, EXP, IGI, IDA). This is the exact current GOA label.
- BP core: GO:0180047 dolichol phosphate mannose biosynthetic process (IDA/ISS) = the most specific/direct BP (the DPM synthesis reaction). ACCEPT. GO:0006488 dolichol-linked oligosaccharide biosynthetic process (IBA/TAS) and GO:0043048 dolichyl monophosphate biosynthetic process are broader/downstream; ACCEPT (upstream-of processes DPM feeds into). GO:0006506 GPI anchor biosynthetic process and GO:0035269 protein O-linked glycosylation via mannose = downstream pathways DPM feeds — KEEP_AS_NON_CORE (via upstream provision of Dol-P-Man mannosyl donor).
- CC: GO:0005789 ER membrane = correct primary location; ACCEPT. GO:0005783 ER (parent) ACCEPT/KEEP_AS_NON_CORE. GO:0033185 dolichol-phosphate-mannose synthase complex ACCEPT (IDA). GO:0016020 membrane = uninformative parent, MARK_AS_OVER_ANNOTATED. GO:0005634 nucleus (HDA, sperm-nucleus proteome) = spurious/contaminant, REMOVE (HDA proteomics artifact, contradicts well-established ER localization; not an experimental functional annotation).
- MF GO:0005515 protein binding IPI x7: bare, uninformative. DPM3 interaction (Q9P2X0) is functionally meaningful but the term is uninformative -> MARK_AS_OVER_ANNOTATED (do NOT remove per policy). Others (MEOX2/Q6FHY5, TDO2/P48775, Q9UNE7) are large-scale/interactome — MARK_AS_OVER_ANNOTATED.
- MF GO:0046872 metal ion binding (ISS, from Q8U4M3): supported by BINDING features (Mg2+/Mn2+ at res 120). KEEP_AS_NON_CORE (real but ancillary to the transferase MF).

## Interactor PMIDs (protein binding IPI)
- PMID:10835346 (Q9P2X0=DPM3): the defining complex paper — DPM1-DPM3 direct interaction. Meaningful but term uninformative.
- PMID:16280320 (Q9UNE7 in GOA line): DPM3 tethering paper.
- PMID:10944123 (Q9P2X0=DPM3): PIG-P / DPM2 GPI-GnT regulation paper (abstract does not describe a direct DPM1 binary interaction; IntAct-sourced).
- PMID:23856421 (Q9P2X0=DPM3): DPM1-CDG G152V abolishes DPM3 binding.
- PMID:25416956, 25910212, 32296183 (P48775=TDO2, Q6FHY5=MEOX2): large-scale binary interactome maps (HuRI/Rolland/Luck). Generic.


## Source-based reassessment — 2026-10-18

This entry supersedes the earlier unsupported contamination interpretation, blanket dismissal of screened binding pairs and absolute partner-requirement language. The earlier notes and excerpts remain intact. All 43 historical source dictionaries are preserved. The current 44 raw contexts normalize to those same 43 assertions because two provider/date contexts share the same Dol-P-Man transferase assertion; the duplicate provenance and 18 newly fetched metadata additions are retained separately, without silently replacing historical source fields. No NEW annotation is added.

DPM1 catalyzes transfer of mannose from GDP-mannose to dolichyl phosphate, producing Dol-P-Man. It does not phosphorylate dolichol to make Dol-P. The core therefore describes GO:0180047 and the catalytic contribution to the physiological synthase complex. Imported `enables` qualifiers remain unchanged. In [PMID:10835346](https://pmc.ncbi.nlm.nih.gov/articles/PMC212771/), human DPM1-containing complexes purified from JY25 cells were reconstituted in PC/PE liposomes. The synthase assay did not add exogenous Dol-P. Separate hamster-host experiments with human DPM1/DPM3 and rat DPM2 show lower activity without DPM2 when DPM3 is overexpressed; they do not establish isolated unanchored human catalysis or an absolute three-subunit requirement. The [PMID:9724629 engineered membrane-anchor experiment](https://pubmed.ncbi.nlm.nih.gov/9724629/) likewise did not remove DPM3.

The official [O60762 record](https://www.uniprot.org/uniprotkb/O60762/entry) contains one 260-residue primary sequence, with initiator-methionine removal and acetylated Ala2 on the annotated mature chain 2–260. The 259-residue processed chain is not another splice isoform or a demonstrated separate function. Metal-binding structural evidence in [PMID:28743912](https://pmc.ncbi.nlm.nih.gov/articles/PMC5526996/) concerns the archaeal donor Q8U4M3; human topology and assay conditions are not imported from it.

The human sperm-nuclear observation is positive contextual evidence. The [author thesis](https://diposit.ub.edu/server/api/core/bitstreams/748602ae-3122-4398-88b1-5043df608fcb/content), Table 8.1 on physical PDF page 194 (printed page 193), identifies DPM1/O60762 with 13.1% sequence coverage and two peptides. Its nuclear-isolation and MS-identification Methods were read. This does not establish a nuclear enzymatic role, but ER association alone cannot identify the peptides as contamination. The independent ER-membrane localization remains the active core location. Current HPA XML contains tissue staining but no target ICC/IF cell records, so it is not cited as direct ER-specific imaging.

The [executed interaction audit](DPM1-bioinformatics/interaction-audit/RESULTS.md) retains exact participant identities and all 42 raw MITAB fields. TDO2 enzyme identity and the sequence-confirmed MEOX2 clone support bounded binding-class refinements, without assigning their downstream metabolic or transcriptional functions to DPM1. The MEOX2 difference is one glutamine within canonical residues 81–84, outside the homeobox; the repeat prevents assigning a unique deletion position. The three DPM3 associations remain positive non-core complex contacts under the [project binding policy](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions). Free-DPM1/CHIP association is explicitly supported by the complete PMID:16280320 abstract; its full assay details remain inaccessible. The current IntAct record for that PMID instead concerns human DPM1 and hamster DPM3, and is not substituted for a STUB1 pair.

PAINT's literal placements and target alignment support the inherited synthase activity and ER location. Target experimental evidence among the descendants is legitimate, not circular. Downstream glycosylation processes remain contextual donor-supply biology. Reactome's normal and variant failed-reaction contexts are separately identified in the [source guide](DPM1-source-guide.md); none assigns the separate lipid-flipping step to DPM1. Reduced DPM1–DPM3 binding in the G152V experiment is not complete loss, and the patient's glycoepitope phenotype supplies independent human O-mannosylation context.

The source guide distinguishes normal cache flags from separately recovered originals and identifies actual read scopes. Existing caches, provider files and previous history are unchanged. Configured Falcon and fallback attempts failed with authentication/quota responses; no provider report was fabricated. Manual evidence supplies this reassessment. New source excerpts were not added; inherited excerpts are preserved and are not represented as a new quotation allowance.


## 2026-10-18 — review follow-up: catalytic role and source presentation

This entry supersedes the earlier description of the core as a conservative complex contribution. DPM1 provides the mannosyltransferase chemistry, while DPM3-mediated anchoring and DPM2-mediated support affect its native activity. The core now uses `molecular_function` for GO:0004582 and retains the DPM synthase complex. This does not assert activity of an isolated unanchored human monomer or establish that DPM3 was absent from the anchor-fusion experiment.

The DPM2-stability excerpt previously attached to DPM1–DPM3 binding and the GPI-donor excerpt attached to controlled co-immunoprecipitation have been removed from those claims. The related co-IP finding now points to the actual PMID:10944123 Figure 5A/Results and human JY5 controls. The EC-label excerpt has also been removed. Correct reference-only anchors preserve the scientific evidence without duplicating the existing DPM3 quotation.

The positive sperm-nuclear observation remains non-core. Judit Castillo Corullón’s registered 2014 thesis supplies the DPM1/O60762 Table 8.1 record (13.1% coverage, two peptides), its article linkage and relevant preparation/identification Methods. The [portable source record](DPM1-source-evidence.md) gives the public URL, checksum and page locators. CTAB/digitonin isolation, washing and microscopy support the reported preparation; they do not establish a DPM1-specific nuclear mechanism or permanent residence. The thesis procedure-efficiency estimate (~99%) is distinct from the article abstract’s 99.9% purity claim. Neither contamination nor a nuclear catalytic activity is inferred. The generic 403-protein and unrelated ER excerpts no longer serve as the target-specific row’s support.

The validated TDO2 and MEOX2 binary pairs retain their bounded partner-class refinements. These do not imply native colocalization, DPM1 transcriptional regulation or transfer of the partner’s enzymatic activity. The metal-binding ISS row now directly cites the archaeal Q8U4M3 structural and biochemical source, PMID:28743912, without treating its human inference as circular or a direct measurement of human metal occupancy. All 43 source assertions, annotation actions, replacements and product data remain unchanged. This follow-up introduces no quoted source text.


### 2026-10-18 — Thesis catalogue identifier correction

The registered thesis citation now uses its [institutional HTML catalogue record](https://diposit.ub.edu/dspace/handle/2445/60858), with persistent identifier [2445/60858](https://hdl.handle.net/2445/60858). Its exact catalogue title contains *espermatozoïde*. The catalogue issue date is 2014-09-19; July 2014 is the date printed in the PDF, not the catalogue issue date. The item’s ORIGINAL bundle links the same PDF bitstream already read, with matching size and checksum. The direct PDF link, SHA-256 and target-data locators remain in [DPM1-source-evidence.md](DPM1-source-evidence.md). This is a bibliographic identity correction; the scientific findings and annotation decisions are unchanged.
