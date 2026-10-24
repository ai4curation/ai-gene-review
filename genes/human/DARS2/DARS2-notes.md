# DARS2 notes


## 2026-09-08 paired human–horse review



DARS2 is the nuclear-encoded mitochondrial aspartate-tRNA ligase. It activates aspartate with ATP and transfers it to mitochondrial tRNA(Asp), supporting synthesis of mitochondrially encoded respiratory-chain proteins. The enzyme forms a homodimer and contains an N-terminal mitochondrial targeting sequence.

## Substrate and compartment distinctions

Mitochondrial aspartate-tRNA synthetase must accommodate structurally unusual mitochondrial tRNA(Asp); the 2013 structure compares that accommodation with bacterial AspRS. Cross-aminoacylation of bacterial and mitochondrial tRNA(Asp) is a taxonomic/substrate-structure breadth claim, whereas acceptance of tRNA(Asn) is a different aminoacylation-specificity claim. The human GOA includes the latter, so the original experiments matter. The inspected 2013 full text did not settle that point and the 2005 characterization is abstract-only in the cache. Retaining uncertainty is appropriate. Matrix localization is the primary placement, but additional membrane-associated or extracellular activities cannot be dismissed just from that default.

## Decisive inspected evidence

From [PMID:15779907](https://pubmed.ncbi.nlm.nih.gov/15779907/):

> Both belong to the expected class of synthetases, have a dimeric organization, and aminoacylate Escherichia coli tRNAs as well as in vitro transcribed human mitochondrial tRNAs.

## Evidence inventory

- [PMID:15779907: Toward the full set of human mitochondrial aminoacyl-tRNA synthetases: characterization of AspRS and TyrRS.](https://pubmed.ncbi.nlm.nih.gov/15779907/). [DOI:10.1021/bi047527z](https://doi.org/10.1021/bi047527z). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.
- [PMID:23275545: Thermodynamic properties distinguish human mitochondrial aspartyl-tRNA synthetase from bacterial homolog with same 3D architecture.](https://pubmed.ncbi.nlm.nih.gov/23275545/). [DOI:10.1093/nar/gks1322](https://doi.org/10.1093/nar/gks1322). Full text is available in the repository cache.

## Transfer to the selected horse protein

The exact target is [A0A9L0SB67](https://www.uniprot.org/uniprotkb/A0A9L0SB67/entry), not an arbitrary horse record with a matching name. The reproducible [paired-sequence analysis](../../HORSE/DARS2/DARS2-bioinformatics/RESULTS.md) records identity, coverage and internal gaps. It supports homology but is not a reciprocal orthology test. Molecular properties are transferred only with the relevant domain, targeting and paralog constraints. The prediction-time sequence is not independently verified.

## Open evidence questions

The following annotation scopes need source-specific follow-up: aspartate-tRNA(Asn) ligase activity, mitochondrial membrane, obsolete mitochondrial asparaginyl-tRNA aminoacylation, protein binding. Experimental annotations are not removed merely because a cached abstract omits the gene or a specific assay. High-throughput protein-binding rows require their actual partner or complex context before replacement with an informative molecular function.


Research provenance: external Falcon/Edison was attempted with Perplexity fallback. Some requests returned HTTP 429 and fallback returned insufficient-quota HTTP 401; successful external reports are preserved separately. Primary-source manual synthesis is explicitly labeled manual where no external report was available.


## 2026-10-16 source-specific augmentation

All 54 original annotation source objects were manually assessed with their source identifiers, evidence, partners and qualifiers retained. The resulting decisions are 21 ACCEPT, 16 MODIFY, eight TOO_GENERAL, six KEEP_AS_NON_CORE and three UNDECIDED; no NEW assertion is proposed. The [source-evidence guide](DARS2-source-evidence.yaml) records the reconstructed raw sources and the exact assay/access limits. The earlier human–horse notes above are historical; this augmentation concerns the human record and does not change the separate horse review.

### Catalysis, products and compartments

The defining activity remains ATP-dependent attachment of aspartate to mitochondrial tRNA(Asp). The recovered [2007 original](https://doi.org/10.1038/ng2013) uses E. coli tRNA(Asp), while the [2013 study](https://pubmed.ncbi.nlm.nih.gov/23275545/) directly compares bacterial and human mitochondrial tRNA(Asp). Its non-cognate terminology is a species comparison, not evidence of tRNA(Asn) charging. The full [2005 original](https://pubmed.ncbi.nlm.nih.gov/15779907/) remains inaccessible after bounded attempts. Its specific tRNA(Asn) and YARS2 claims are therefore unresolved; later Asp assays do not establish an absolute inability to use Asn tRNA.

The official 645-residue precursor and annotated 48–645 chain (598 residues) were reconstructed exactly. The targeting peptide is predicted; the experimental I41 truncation is a different construct. The [2018 fractionation study](https://pubmed.ncbi.nlm.nih.gov/30006346/) supports soluble and electrostatically attached peripheral membrane pools, but its soluble fraction combines matrix and intermembrane space and its membrane fraction combines inner and outer membranes. The matrix core uses the established translation context rather than claiming a resolved measurement of charging flux. The [2025 imaging and lysate assays](https://pubmed.ncbi.nlm.nih.gov/40814755/) support mitochondrial localization and DARS2-dependent charging; confocal colocalization alone does not resolve a membrane face. Original [MitoCoP Table S1](https://pubmed.ncbi.nlm.nih.gov/34800366/) contains direct DARS2 subtractive, spatial and importomics measurements and classifies membrane association as Peripheral.

### Interactions and propagation

The exact partner identities, products, 123 interaction records and 90 scoped reference-sequence hashes were checked. [BioPlex](https://pubmed.ncbi.nlm.nih.gov/28514442/) co-purification, [crosslinking](https://pubmed.ncbi.nlm.nih.gov/30021884/), [MAC-tag](https://pubmed.ncbi.nlm.nih.gov/29568061/) proximity, [HuRI](https://pubmed.ncbi.nlm.nih.gov/32296183/) binary assays and [CFTR MaMTH](https://pubmed.ncbi.nlm.nih.gov/35156780/) are distinguished. Positive associations support enzyme, chaperone, collagen or transporter partner classes where warranted. The remaining positive generic associations are retained as contextual under the standing project policy, without converting proximity into purified binding or transferring a partner's catalytic role to DARS2. The [CFTR proximity study](https://pubmed.ncbi.nlm.nih.gov/36012204/) uses mutant constructs; it does not establish wild-type DARS2 regulation of CFTR.

The actual 844-node PTHR22594 tree, 22-node target path, three on-path IBD records, 37 current donor records and two complete ARBA rule objects were reconstructed. Human self evidence is legitimate descendant grounding. The current ARBA00026908 lacks a complete target match; this boundary is explicit and does not negate independently supported ligase chemistry. ARBA00026971 has a complete match. The obsolete process term is refined without alleging a failed evolutionary placement.

### Scope and provenance

Independent annotation/core input covered the four substrate claims (ROOT), all 11 HuRI claims (Bloc) and a separate critique of the substrate assessment (Bloc). The remaining judgments and cross-source synthesis were performed here. Original source caches, all source dictionaries, UniProt, provider output and this notes prefix were preserved. Four missing publications were genuinely cached; the shared PMID:24275569 bytes match the qualified pending source exactly. No pending family-cache variant was silently adopted. Inherited excerpts are retained as supplied evidence; no new external quotation was added. Actual source scopes are recorded even where a cache claims full text but omits Methods or target tables.

The [2024 immune experiments](https://pubmed.ncbi.nlm.nih.gov/39039092/) motivate a question about extracellular DARS2, but delivery-assisted recombinant-protein experiments do not establish a physiological receptor or a separate secreted-ligand core. Ordinary validation and independent whole review remain pending at this scientific freeze; subsequent results will be appended.


### Whole-review refinement before validation

The independent whole read identified two accepted associations whose known partner classes were already sufficiently established: the HSPD1 proximity source and CFTR mutant proximity source now receive the same chaperone/transporter class refinements as their corroborating assays. Their proximity, variant and direct-contact limits remain explicit. This changes two review actions only; every historical source field remains exact. The source-evidence file is explicitly an authored synthesis, not independent primary evidence.


### Final independent review and validation outcome

The complete 54-row review, all 22 reference assessments and the single catalytic core were independently read. A separate saved-source core/product assessment checked the operative 2007, 2013, 2018 and 2025 evidence, the original MitoCoP cells and the delivery limits of the 2024 immune experiments. No further scientific correction was requested. These are AI-agent reviews, not a human expert sign-off. Public evidence locators now use actual interaction accession identifiers and primary section/table locations; the guide remains an authored synthesis.

All six final normal phases passed: schema/source/reference/best-practice validation, the CI-equivalent validation command, ordinary status initialization/check, term checks and rendering. The ordinary updater derived DRAFT after the inherited COMPLETE mismatch was preserved. Three unresolved assertions remain explicit. Nine advisories are disclosed: six positive generic-binding exceptions under the standing project policy, two source-specific action differences for the Asn-related terms, and one retained but uncited provider-report advisory. All 53 protected source/context files and 291 isolated runtime files remained exact; no ontology-cache drift occurred. The final HTML was regenerated after this append and the public-locator correction.


## Finite interaction follow-up, 2026-10-16

The published review on PR #5060 was reconsidered against formal review 5548570487 and detail 6216629668. Rows 12 (PMID:29568061, HSPD1 BioID) and 28 (PMID:36012204, mutant-CFTR proximity labeling) now retain the original generic positive associations as KEEP_AS_NON_CORE. These assays label neighboring proteins; their source-specific judgments no longer borrow the chaperone/transporter refinement from independent AP-MS, crosslink or MaMTH assays. The stronger source rows retain those refinements. No interaction is declared absent or artifactual. This supersedes the two proximity-row refinements described in the earlier whole-review paragraph, which remains preserved above.

Row 19 retains MODIFY to collagen binding. The exact Q4VAQ0 construct is an unreviewed 427-residue COL8A2 sequence with collagen-family and sequence support. Its three IntAct records are EBI-23719907 (MI:1112 pooling), EBI-24688931 (MI:1356 validated two-hybrid) and EBI-24012672 (MI:0397 array), rather than three pooling records. The saved GO:0005518 definition does not require extracellular matrix contact or a mapped collagenous-region interface. This class refinement makes no claim about mature assembled collagen, endogenous mitochondrial/extracellular encounters or a pair-specific orthogonal assay. The other six enzyme-class refinements remain, with compartment and construct limits; binding does not imply catalytic regulation.

The protected UniProt catalytic-activity record explicitly attributes EC:6.1.1.12 and tRNA(Asp) charging to PMID:15779907 with ECO:0000269. This supports the cognate Asp reaction and is now discussed alongside GO:0050560's tRNA(Asx)/EC:6.1.1.23 scope. The original 2005 substrate panel remains uninspected, so rows 50 and 52 remain UNDECIDED. Obsoletion of GO:0070145 is separate from the unresolved Asn premise. No human GatCAB-absence claim is made.

The authored source guide remains available as navigation in references and the gene directory, but its bare self-citations have been removed from supported_by. All primary-source associations, 35 inherited quotation occurrences, 54 literal source objects, 22 reference identities, product information and the single catalytic core are preserved. The guide corrects spacing and records these dispositions and public source locators. This follow-up introduces no NEW annotation, new source cache or new quotation. ROOT performs derived rendering and the final publication checks after accepting this finite packet.


## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Context: ProtNLM2 benchmark target Q6PI48 (cohort HORSE40 + HORSE40_HUMAN_PAIR). No ProtNLM2 file or output was opened or used.

### Identity
Q6PI48 (SYDM_HUMAN) is the reviewed, canonical Swiss-Prot entry: 645 aa precursor, no alternative-product comment, predicted transit peptide 1-47 and chain 48-645. It carries the full domain set (OB-fold anticodon-binding PF01336, GAD insertion PF02938, class II catalytic PF00152). It is not a fragment, isoform or alternative gene model.

### Evolutionary grounding
- PANTHER PTHR22594:SF5 "ASPARTATE--TRNA LIGASE, MITOCHONDRIAL" (UniProt and the PANTHER 19.0 member files agree). SF5 also contains E. coli AspS (P21889), yeast MSD1 (P15179), S. pombe dar2, fly AspRS-m, worm dars-2, mouse Dars2 (Q8BIP0) and Arabidopsis At4g33760. That makes this the bacterial-type, discriminating AspRS lineage.
- The PAINT IBDs for GO:0004815, GO:0006422 (PTN000502597) and mitochondrion (PTN000502598) use MSD1, AspS and DARS2 itself as donors. PAINT did not propagate GO:0050560 (non-discriminating Asp-tRNA(Asx)) to this node. I treat that omission as a deliberate decision.
- Human mitochondria have their own AsnRS, NARS2 (Q96I59, PTHR22594:SF34). So a non-discriminating DARS2 is neither expected nor needed.
- Family review interpro/panther/PTHR22594/PTHR22594-review.yaml places DARS2 in SF5 and scopes annotation to the mitochondrial AspRS lineage. No disagreement.

### Changes in this pass
1. **GO:0005515 protein binding.** Following the protein-binding policy, 15 rows were changed to REMOVE:
   - 11 HuRI rows (PMID:32296183)
   - 2 GAPDHS rows (BioPlex PMID:28514442, PMID:33961781)
   - the HSPD1 BioID proximity row (PMID:29568061)
   - the two CFTR rows (MaMTH PMID:35156780, proximity PMID:36012204)

   The earlier "enzyme binding", "collagen binding" and "transmembrane transporter binding" refinements described the partners, not anything DARS2 does. Most partners also sit in compartments DARS2 does not occupy (ER, secretory vesicles, cell surface, testis cytosol). Removing a row does not mean the interaction is false. Three HSPD1 rows (AP-MS x2, crosslinking) stay MODIFY to GO:0051087, because Hsp60 is a matrix chaperonin that shares DARS2's compartment and the pair recurs across methods. The YARS2 IPI (PMID:15779907) stays UNDECIDED because the full text could not be read.
2. **GO:0031966 mitochondrial membrane** (IDA/IEA/IMP) changed from ACCEPT to KEEP_AS_NON_CORE. The peripheral pool is real (PMID:30006346: salt/carbonate-extractable). The catalytic core location remains the matrix.
3. **GO:0050560 aspartate-tRNA(Asn) ligase (PMID:15779907)** changed from UNDECIDED to MODIFY to GO:0004815. This now matches the PMID:17384640 row. The grounds are the SF5/PAINT placement, NARS2 being present, and UniProt curators assigning only EC:6.1.1.12 with ECO:0000269 to this same paper. The IC row on obsolete GO:0070145 depends on it, so it was changed from UNDECIDED to MODIFY to GO:0070127, matching the 2013 row. Caveat: the full 2005 text was not read. Revisit if it contains a direct tRNA(Asn) charging assay.
4. Specific verbatim quotes were added for the 2025 activity row (PMID:40814755) and the homodimer rows (PMID:23275545). The description was rewritten as a project-independent summary: structure, matrix/peripheral pools, FBXO24/acetylation turnover, reported extracellular release, LBSL/CMT disease. The deep-research file is now cited for the core-versus-moonlighting framing.

Unchanged after re-examination: core function (GO:0004815 in GO:0005759, directly involved in GO:0070127), the TOO_GENERAL handling of broad IEA terms, the mitochondrion/matrix ACCEPTs, and ATP/tRNA binding and homodimerization. No NEW annotations. The 2024 extracellular/immune findings (PMID:39039092) stay a suggested question. They are not a process annotation, because the experiments relied on delivery reagents.

### Relative to review next
Yeast MSD1 (P15179, SGD:S000006025) is the mitochondrial AspRS ortholog in the same PANTHER subfamily (SF5). It is a direct PAINT donor for both the ligase and mitochondrion IBDs. It has no review in the repo. Mouse Dars2 (Q8BIP0, SF5) and E. coli AspS (P21889, SF5) are also unreviewed.

### Modules
modules/mitochondrial_trna_charging_and_initiator_formylation.yaml includes DARS2 (GO:0004815, Reactome R-HSA-380229).
