# CLPP (human, Q16740) review notes

## Session 2026-10-09

Chosen from `projects/MITOTOL.md` (Chen et al. 2026, PMID:42822426): human CLPP is the human half
of the ClpXP/ClpYQ non-homologous protease pair.

### Deep research

`just deep-research-falcon human CLPP --fallback perplexity-lite` was launched at the start of the
session (timeout 1500 s). See the end of this file for its outcome. The review below was built from
my own literature research (PubMed MCP plus cached publications), not from a deep-research file.

### Identity and structure

- Peptidase S14 (ClpP) family, MEROPS S14.003; PANTHER PTHR10381:SF11. Transit peptide 1-56;
  nucleophile Ser153, His178 (UniProt). S153A/C abolishes protease activity [PMID:11923310 via UniProt].
- Two heptameric rings with 7-fold symmetry, matrix-localized, tending to associate with the inner
  membrane [PMID:10525407 "the mammalian homologue of ClpP is located in the mitochondrial matrix"].
- Crystal structure: active sites sequestered in the chamber; N-terminal peptides line the axial
  channel and are needed for activity [PMID:15522782 "Mutation or deletion of these residues causes a
  drastic decrease in ClpX-mediated protein and peptide degradation."]. The 28-residue C-terminal
  extension is mammal-specific.
- Alone, human CLPP is a heptamer with almost no activity; ATP-bound CLPX converts it to an active
  tetradecamer [PMID:16115876, paraphrase: In the reported preparation, CLPP alone had minimal peptide cleavage and no protein degradation; ATP-bound CLPX favored the active double-ring assembly.].
- Reconstituted human ClpXP is an ATP-dependent protease; substrate choice is set by CLPX
  [PMID:11923310 "Our results establish that human ClpX and ClpP constitute a bone fide ATP-dependent
  protease"].

### Substrates and roles

- Mitoribosome assembly via ERAL1 (mouse): Clpp loss causes ERAL1 to stay bound to the 28S subunit,
  impairing 55S assembly and translation; wild-type but not S149A (mouse numbering) CLPP rescues
  [PMID:27797820, paraphrase: ERAL1 accumulation contributes to defective small-subunit maturation after mouse Clpp loss.].
- OXPHOS proteins: BioID interactors include respiratory chain subunits; SDHA proposed substrate in
  AML [PMID:26058080, paraphrase: Functional assays nominate SDHA as a substrate relevant to respiration in the tested AML cells.].
- Heme-bound ALAS1 (via Reactome R-HSA-9838289, citing Kubota 2016, Nomura 2021). The ALAS activation
  role belongs to CLPX, not CLPP (see `genes/human/CLPX`).
- PINK1: ClpXP was one of four proteases found in an RNAi screen for PINK1 turnover; ClpXP knockdown
  did not stabilize PINK1 at the surface [PMID:22354088]. Peripheral.

### UPRmt

- C. elegans clpp-1 is needed for UPRmt signalling [PMID:17925224].
- In mice, CLPP is not required for UPRmt [PMID:27154400 "our results clearly show that mammalian CLPP
  is neither required for, nor it regulates the UPR(mt) in mammals"]. Loss of CLPP even improved
  DARS2-deficient cardiomyopathy. Reactome still asserts UPRmt involvement by inference from worm and
  rat; I did not add GO:0034514.

### Disease

- Perrault syndrome 3: homozygous T145P, C147S, splice variants [PMID:23541340]; Y229D [PMID:25956234].
- Clpp-/- mice: infertility, hearing loss, growth retardation, CLPX and mtDNA accumulation
  [PMID:23851121 "Thus, murine Clpp deletion represents a faithful Perrault model."].

### Pharmacology

- Imipridones (ONC201, ONC212) bind CLPP non-covalently in hydrophobic pockets between subunits and
  hyperactivate it, degrading respiratory chain proteins and killing cancer cells [PMID:31056398 "We
  identified imipridones as potent activators of ClpP."]. Resistance mutation D190A.
- Independent target identification of CLPP for ONC201/TR compounds by affinity chromatography
  [PMID:31021596].
- Not annotation material for normal function (drug response), but confirms the docking-pocket
  activation mechanism.

### Evolutionary context (PMID:42822426)

- LECA mitochondria likely had both ClpXP and ClpYQ (HslUV), lost in complementary patterns; humans
  keep ClpP, several pathogens keep ClpQ (an essential candidate target in P. knowlesi). This is
  comparative/computational and says nothing about CLPP's molecular function; used at LOW relevance.
  "Absent in humans" means the ClpYQ family is absent, not ATP-dependent matrix proteolysis.

### Curation decisions (summary)

- Core MF: serine-type endopeptidase activity (GO:0004252); ATPase binding (GO:0051117) for CLPX docking.
- Core BP: mitochondrial protein catabolic process (GO:0035694); protein quality control (IBA).
- Core CC: mitochondrial matrix; mitochondrial endopeptidase Clp complex (GO:0009841).
- GO:0004176 ATP-dependent peptidase activity accepted (EC 3.4.21.92 is the ClpP enzyme), with a
  question on contributes_to (CLPX supplies ATP hydrolysis).
- GO:0009368 IDA/IPI -> MODIFY to GO:0009841; IBA kept at family level.
- protein binding: CLPX IPIs -> MODIFY to ATPase binding; 22 HTP Y2H pairs (HuRI, neurodegeneration
  interactome) -> REMOVE as uninformative.
- GO:0008233 peptidase activity TAS (cloning paper) -> MODIFY to GO:0004252.
- membrane protein proteolysis (PINK1) and identical protein binding -> KEEP_AS_NON_CORE.
- No NEW annotations. Mitoribosome assembly raised as a question (mouse evidence; regulatory vs
  participatory is unclear).
- No GO-CAM model in `gocams/index.tsv` contains CLPP.

### Deep research outcome

The `just deep-research-falcon` wrapper reported "Provider falcon timed out after 600s", then the
perplexity-lite fallback failed ("Provider 'perplexity' not available"), and the recipe exited 1.
However, the orphaned falcon client kept running and wrote `CLPP-deep-research-falcon.md` itself at
16:02 (duration 1578 s). That file is genuine tool output, not written by me. I cross-checked it
after the main review and added three of its sources after verifying them against cached text:

- Complex I N-module salvage [PMID:32242014, paraphrase: Mouse ClpXP promotes preferential renewal of the complex I N-module independently of much of the remaining complex.].
- Perrault variant biochemistry [PMID:30150665 "The Y229D mutant not only inhibited CLPP-peptidase
  activity, but unexpectedly also prevented CLPX-docking"]; T145P disrupts oligomerization.
- Phosphoserine degrons recognized by CLPX [PMID:39879245 "We demonstrated that phosphorylated serine
  (pSer) targets substrates to ClpX and facilitates their degradation by ClpXP in biochemical assays."].

Falcon also cites a 2026 Nat Commun study (Aljghami et al.; CHCHD2, ALAS1, TFAM as human ClpXP
substrates, PDIP38 adaptor). I did not find or cache its PMID and did not cite it in the review.
Falcon's report that CLPP knockdown blunts ONC201 responses and that dordaviprone received FDA
accelerated approval (Aug 2025) is drug-response context only and was not used for annotation.

## Merge with concurrent review on main (2026-10-09)

An independent CLPP review landed on main at the same time (PR #4426, mitochondrial UPR module
work). It agreed on 53 of 55 annotation actions, made the same UPRmt call (no GO:0034514 for human
CLPP, per PMID:27154400), and had no `proposed_new_terms`. The two differences:

- GO:0008233 peptidase activity (TAS, PMID:8543061): main ACCEPT as correct-but-general; this
  review MODIFY to GO:0004252 serine-type endopeptidase activity. Kept MODIFY.
- GO:0009368 endopeptidase Clp complex (IBA): main MODIFY to GO:0009841; this review ACCEPT,
  because the PAINT node spans bacterial and plastid Clp complexes and the family term is the
  right level for an inherited annotation (the IDA/IPI rows are MODIFY in both). Kept ACCEPT.

This version (30 references, ATPase binding as a second core function) was kept as the merged
review.

## Session 2026-10-11: source-specific campaign review

The current review preserves all 55 original source assertions in their original order, the absence of an alternative-products field, and all 30 original reference identities. The new reference to PMID:25956234 is a genuine cached record for the citation already present in the historical notes. Its abstract reports an exon-6 variant without naming Y229D; residue-specific biochemical conclusions instead use PMID:30150665.

Four historical quotation blocks above have been replaced by cited paraphrases to respect the aggregate quotation limit. The exact inherited notes and YAML remain in the authenticated baseline packet, and no earlier history record was changed. This supersession concerns those quotation blocks only. The scientific clarifications below supersede the earlier blanket claims about screen interactions, isolated CLPP oligomerization and mammalian UPRmt.

### Performed activity and core

Direct human reconstitution, active-site mutagenesis and original structural work support one integrated serine-protease core [PMID:11923310; PMID:15522782]. CLPP cleaves peptide bonds; CLPX supplies ATP hydrolysis, unfolding and substrate delivery. Existing ATPase-binding annotations remain valid and are integrated into that mechanism. The 2004 structure and 2018 biochemical work require condition-specific oligomer wording rather than a universal claim that isolated CLPP is only heptameric [PMID:15522782; PMID:30150665]. Mature-protein and precursor residue numbering are distinguished.

Phosphoserine-dependent substrate selection belongs to CLPX, while CLPP supplies degradation [PMID:39879245]. Mouse ERAL1 turnover and respiratory complex I N-module renewal support quality-control context, but no additional human mitoribosome-assembly process is proposed [PMID:27797820; PMID:32242014]. Human patient alleles show different combinations of peptide-cleavage, assembly and CLPX-coupling defects [PMID:30150665]. The experimental suggestions therefore address residual function in native mitochondrial context rather than presuppose a shared defect.

### Interactions and propagation

All 22 positive screen pairs are retained or refined under the campaign policy. Exact IntAct records distinguish the HuRI source [PMID:32296183] from the neurodegenerative-disease interaction screen [PMID:32814053]. Eight partner-class refinements identify growth factor, PP2A, E3 ligase, transcription coactivator, membrane transporter, cytoskeletal component, GTPase and protease binding. These are assay-scoped pair classifications; none transfers the partner's catalytic or cellular function to CLPP. PSMB1 is non-catalytic, and binding its subunit does not prove binding to an assembled proteasome. Nuclear import factors are not automatically transmembrane solute transporters.

The tested RBPMS, ABI2 and DNM2 isoforms and the APP, SNCA, HTT, TARDBP and GDAP1 mutation/fragment features are retained in the source index. Global orthogonal-validation subsets in the publications are not attributed to every individual CLPP pair. PAINT judgments use direct human biochemistry and current source records, with historical node placement and alignments explicitly uninspected. A target in its own source list is legitimate experimental grounding. The unresolved WormBase lookup and ambiguous Arabidopsis mapping are retained as provenance limits rather than negative biological evidence.

### PINK1, stress responses and access limits

The selected PMID:22354088 cache lacks Results despite its full-text flag. The authentic original article was recovered separately. Its CLPP knockdown result is positive but accompanied by substantial respiratory and viability defects; MPP-specific rescue and protease-protection findings cannot be transferred to CLPP. The membrane-protein processing annotation remains non-core, with no direct PINK1 cleavage-site claim.

The previous mammalian UPRmt generalization is narrowed to the tested mouse Dars2-deficient cardiac and human SPG7-depletion models [PMID:27154400]. Worm CLPP-1 results remain organism-specific [PMID:17925224]. No new human UPRmt process is added.

Original external evidence was inspected for PMID:11923310, PMID:15522782, PMID:22354088 and PMID:32814053 while their selected repository caches were preserved. The full PMID:16115876 source remains inaccessible; its complete abstract supports the reported association. The specific PMID:34800366 supplementary CLPP table row remains uninspected, although independent human localization supports the broad mitochondrial annotation. The PMID:39879245 supplementary Methods appendix was not recovered; claims are limited to the inspected Results and legends. Exact read ranges, source URLs, hashes and literal record locators are summarized in [the source index](CLPP-source-evidence.json). Long primary text remains in the temporary evidence packet.

### Research and verification provenance

A genuine isolated fetch produced the same 55 source objects as the inherited review. The new Falcon attempt timed out after 90 seconds; the explicit Perplexity fallback returned an HTTP 401 quota failure. No new provider report was fabricated. The pre-existing genuine historical Falcon file and all fetched publication, UniProt, GOA and Reactome bytes remain unchanged. The GO-CAM index contains no Q16740 activity. The final review adds no NEW annotation. Quotation totals are audited across YAML, these notes and the compact source index; the index contains provenance and structured-source facts without repeating primary quotations.


## Follow-up: evidence anchors and binding-class precision (11 October 2026)

The preceding review remains the historical account. Its quotation reduction was broader than the four long notes blocks: the prior baseline YAML contained 80 annotation-level, 12 reference-finding and 7 core supporting-text fields (99 total), whereas the first amendment retained five annotation anchors. Those quotation-field changes did not remove the 55 source assertions. The earlier four-block notes repair and these YAML quote changes are distinct and are now explicitly disclosed. This follow-up restores concise catalytic-site, oligomer/complex and ATPase-association anchors and provides an attributed external-primary excerpt file. The aggregate quotation limit is a text-reuse constraint for this work, not a biological curation rule or evidence that unquoted findings are false. Existing notes and histories have not been rewritten.

Supported generic interactions follow the explicit ClinGen project instruction in [Curation instructions, lines 2976–2978](https://github.com/ai4curation/ai-gene-review/blob/2eff94596d470eb70bbb3ccc7469bab754a1a7c6/projects/CLINGEN_MENDELIAN.md#L2976-L2978). Positive, correctly scoped pairs remain non-core when a more specific class is unresolved. This does not establish a native encounter between mitochondrial CLPP and every screen partner. Exact human Y2H records and construct limits remain the evidence; the policy does not substitute for them.

The eight challenged/class-comparison decisions were checked against the actual GO definitions and partner products. PPP2CA remains protein-phosphatase-2A binding at the catalytic-protein level, without asserting holoenzyme binding. GRN and DTX2 retain the established bound growth-factor and E3-ligase classes. RBPMS-C is supported by the exact product record and the original Smad association/tethered-reporter study [PMID:17099224](https://pubmed.ncbi.nlm.nih.gov/17099224/), with its possible post-transcriptional contribution preserved. PLSCR4 is supported by the direct human reconstitution described in the complete original abstract [PMID:23089641](https://pubmed.ncbi.nlm.nih.gov/23089641/), rather than its name alone. These classes assign binding to CLPP, not the partner's biochemical or signaling activity.

The ABI2 isoform-2 pair remains positive but is now non-core generic binding. A regulatory WAVE/SCAR role and retained domains do not by themselves settle the exact tested product's membership as a cytoskeletal component; the strongest localization evidence specifically names isoform 1. In contrast, GO:0050840 explicitly covers binding an extracellular-matrix component. The EFEMP1 and EFEMP2 pairs therefore receive that narrower class, without claiming extracellular CLPP localization or matrix remodeling. DNM2 and ATXN3 refinements remain unchanged.

The full 2002 author manuscript, 2004 original structural PDF and 2020 interaction-screen author PDF are publicly linked in the corresponding reference assessments and source index. External full access remains distinct from the protected abstract-only caches. The 2005 complete abstract's isolated-heptamer and CLPX-induced complex observations remain positive and preparation-specific; later isolated-oligomer results qualify universality rather than erase the older observations. No new process, enzymatic core or assertion was added. Current experimental donor premises remain positive, while uninspected historical PAINT entities are explicitly unresolved.
