# HSPA13 / STCH (P48723) research notes

## Identity
- Heat shock 70 kDa protein 13 / STCH ("stress-70 protein chaperone, microsome-associated 60 kDa"; "microsomal stress-70 protein ATPase core"), 471 aa, ~52 kDa precursor with N-terminal signal/leader (1-22). HSP70 family.
- Encodes the "ATPase core" of a microsomal stress-70 protein [PMID:8131751 "Stch encodes the 'ATPase core' of a microsomal stress 70 protein."].

## Atypical / non-canonical HSP70 features (KEY)
- Contains the HSP70 nucleotide-binding/ATPase domain but has a ~50-residue insertion in the ATP-binding domain and TRUNCATES the C-terminal peptide (substrate)-binding region [PMID:8131751 "has a 50 residue insertion within the ATP-binding domains and truncates the carboxyl terminal peptide-binding region."].
- UniProt FUNCTION: "Has peptide-independent ATPase activity." [file:human/HSPA13/HSPA13-uniprot.txt].
- ATPase activity is INDEPENDENT of peptide stimulation, unlike BiP/DnaK [PMID:8131751 "In contrast to purified BiP and dnaK, however, STCH demonstrates ATPase activity that is independent of peptide stimulation."]. Because it lacks the canonical substrate-binding domain, classic HSP70 substrate-refolding (foldase) activity is NOT expected; IBA terms transferred from canonical HSP70s (protein refolding, ATP-dependent protein folding chaperone, protein folding chaperone) are likely over-annotations for STCH.

## Localization
- Microsome / endoplasmic reticulum; migrates as a 60 kDa species enriched in membrane-bound microsome fraction [file:human/HSPA13/HSPA13-uniprot.txt "SUBCELLULAR LOCATION: Microsome. Endoplasmic reticulum."; PMID:8131751 "is enriched in a membrane-bound microsome fraction."]. Has a hydrophobic leader/signal sequence.
- GOA also has IBA nucleus, plasma membrane, cytosol (transferred from the broad HSP70 PANTHER family) - these conflict with the documented ER/microsomal localization and should be treated cautiously (likely over-annotation by family transfer).
- extracellular exosome (HDA, PMID:19199708): proteomic detection in exosomes; non-core.

## Expression / induction
- Constitutively expressed in all tissues; induced by calcium ionophore A23187 but NOT by heat shock [PMID:8131751 "constitutively expressed in all human cell types and is induced by incubation with the calcium ionophore A23187, but not by exposure to heat shock."]. HPA: low tissue specificity.

## Interactions / function
- Binds a family of ubiquitin-like (UbL) proteins (ubiquilins) via a short peptide in its ATPase domain [PMID:10675567 "two human ubiquitin-like (UbL) proteins that bind to a short peptide within the ATPase domain of the Hsp70-like Stch protein."]. These = Chap1/Dsk2 (UBQLN-like) and Chap2/scythe (BAG6-related). UniProt SUBUNIT: "Binds UBQLN2." IntAct partners: UBQLN1 (Q9UMX0), UBQLN2 (Q9UHD9), UBQLN4 (Q9NRR5), SGTA (O43765), SGTB (Q96EQ0), CRYGA, B4GALT5. Suggests roles in protein quality control / ubiquitin-proteasome and ER-associated degradation rather than classic refolding.
- The UbL interaction links HSP70-like ATPase family to cell-cycle and apoptosis regulation [PMID:10675567].

## GO review plan
- ATPase activity (GO:0016887, IBA; ATP binding GO:0005524 IEA): ACCEPT - genuine, peptide-independent ATPase is the documented MF.
- ER (GO:0005783, IEA-SubCell): ACCEPT - documented microsomal/ER localization.
- protein refolding (GO:0042026, IBA); protein folding chaperone (GO:0044183, IBA); ATP-dependent protein folding chaperone (GO:0140662, IEA InterPro - note: this term is in the DR lines but not in goa.tsv stub annotations) : MARK_AS_OVER_ANNOTATED / MODIFY - STCH truncates the peptide-binding domain and has peptide-INDEPENDENT ATPase; classic foldase/refolding is not supported and these are family-transfer over-annotations.
- heat shock protein binding (GO:0031072, IBA): KEEP_AS_NON_CORE / ACCEPT - plausible HSP70-family interaction; weakly supported for this paralog.
- nucleus, plasma membrane, cytosol (IBA, broad HSP70 family): MARK_AS_OVER_ANNOTATED - conflict with documented ER/microsome localization.
- protein binding (IPI) WITH UBQLN1/2/4 etc: MODIFY a representative to "ubiquitin-like protein... binding"? The cleanest informative term: these are ubiquilins (UBL-domain shuttle factors). Use "K63-linked..."? No. Safest specific: many partners are co-chaperones (SGTA/SGTB) and ubiquilins. KEEP_AS_NON_CORE the generic high-throughput ones; the UBQLN ones reflect a genuine, documented interaction -> could MODIFY to "ubiquitin protein ligase binding"? Not accurate. Keep most as KEEP_AS_NON_CORE; note UBQLN interaction in findings.
- extracellular exosome (HDA): KEEP_AS_NON_CORE.
- intracellular membrane-bounded organelle (TAS PMID:8131751): consistent with ER/microsome; KEEP_AS_NON_CORE (generic).

## Core function
- Microsomal/ER-associated atypical HSP70-family ATPase with peptide-independent ATPase activity (GO:0016887 / ATP binding GO:0005524), functioning in protein quality control in association with ubiquilin (UbL) shuttle factors and SGT co-chaperones, rather than as a classical substrate-refolding foldase.
</content>

## Full-gene specificity re-review, 2026-09-20

All 20 source rows and the core synthesis were re-reviewed. PMID:36244454 was read in full: ER-luminal proximity labeling and microsomal enrichment support a principal tested ER pool, but cytosolic TTR mistargeting is not localization of HSPA13 itself and the experiment does not establish exclusive residence. PMID:33672238 uses human STCH with murine NKCC2 in a heterologous system and infers a cytoplasmic-side interaction, not an independently measured soluble pool. Nuclear, plasma-membrane and cytosolic IBAs are therefore UNDECIDED pending separate compartment assessment. PAINT PTN002500132 currently retains nucleus/cytosol IBDs; the plasma-membrane row differs between GOA and the current table. The existing folding report was read, including its explicit "No direct in vitro chaperone assay for HSPA13" and failure to access full tree topology. Canonical substrate-binding-domain loss is real, but GO:0044183 also covers assistance through a protein-containing complex. PMID:36244454 identifies ER chaperone/translocon associations and reports that BiP overexpression can also impair translocation, undermining the report's use of an antagonistic overexpression phenotype as universal exclusion. Folding/refolding remain UNDECIDED; heat-shock-protein binding and broad organelle localization are accepted. The unsupported ubiquitin-like-protein-binding core was withdrawn: PMID:10675567 explicitly says "While the N-terminal UbL domains were not essential for Stch binding" and instead identifies a required Sti1-like repeat. Binding a ubiquilin/BAG6-family protein is not automatically binding a small conjugating ubiquitin-like protein. Generic protein-binding rows were removed for lack of functional information, without denying the interactions. No source annotation was deleted or new annotation manufactured.
