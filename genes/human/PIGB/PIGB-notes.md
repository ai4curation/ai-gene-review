# PIGB (Q92521) review notes

## Identity
- HGNC:8959, PIGB = GPI alpha-1,2-mannosyltransferase 3; AltName GPI mannosyltransferase III (GPI-MT-III); "Phosphatidylinositol-glycan biosynthesis class B protein" (PIG-B).
- 554 aa, multi-pass ER membrane protein. Belongs to glycosyltransferase family 22 (CAZy GT22), PIGB subfamily; Pfam PF03901 (Glyco_transf_22), InterPro IPR005599 (GPI_mannosylTrfase).

## Verified function
- GPI mannosyltransferase III: transfers the **third mannose** (alpha-1,2 linked) from dolichyl-phosphate-mannose (Dol-P-Man) onto the GPI intermediate (Man2 -> Man3) in the ER lumen during GPI-anchor biosynthesis.
- This third mannose is the residue that receives the bridging ethanolamine-phosphate (added by PIGO) to which the mature protein is ultimately attached.
- Original cloning/characterization: Takahashi et al. 1996 [PMID:8861954 "PIG-B ... is involved in transferring the third mannose of the GPI anchor"]; abstract-only in cache (full_text_available: false). Establishes: ER transmembrane protein, ~60-aa N-terminal cytoplasmic portion, large ~470-aa C-terminal lumenal (catalytic) domain; functional site on lumenal side.
- UniProt CATALYTIC ACTIVITY (Rhea:RHEA:61004 and RHEA:61000): Dol-P-Man + Man2-GPI intermediate -> Man3-GPI intermediate + Dol-P + H+. EC 2.4.1.- (ECO:0000305 from PubMed:17311586, 8861954).
- Yeast ortholog is Gpi10p (SGD:S000003110); PMID:17311586 (Wiedman et al., mcd4) provides supporting in vivo characterization of the assembly step.

## GOA MF term
- GOA carries MF terms: GO:0000026 (alpha-1,2-mannosyltransferase activity, IBA), GO:0004376 (GPI mannosyltransferase activity, TAS/Reactome), and GO:0120564 (dol-P-Man:Man(2)GlcN-acyl-PI alpha-1,2-mannosyltransferase activity, IDA PMID:8861954). GO:0120564 is the most specific and exactly matches the characterized reaction -> used as the core MF in core_functions.

## Location
- ER membrane (GO:0005789), multi-pass. Confirmed by PMID:8861954 (IDA) and UniProt SubCell.

## Disease
- Biallelic loss-of-function causes inherited GPI-deficiency: Developmental and epileptic encephalopathy 80 (DEE80, MIM:618580) [PMID:31256876 Murakami et al. 2019] — refractory seizures, global developmental delay/ID, +/- axonal (poly)neuropathy, metabolic abnormality in severe cases. Consistent with reduced cell-surface GPI-anchored proteins.

## Annotation dispositions (summary)
- MF GO:0120564 (IDA) -> ACCEPT (core).
- MF GO:0000026 (IBA, alpha-1,2-mannosyltransferase) -> ACCEPT (correct, less specific parent of the reaction).
- MF GO:0004376 (TAS/Reactome, GPI mannosyltransferase) -> ACCEPT (correct family-level MF).
- MF GO:0016757 (IEA InterPro, glycosyltransferase activity) -> ACCEPT (correct but generic root MF).
- BP GO:0006506 x4 (IBA, TAS, IEA-UniPathway, IDA) -> ACCEPT (core BP).
- CC GO:0005789 x4 (IBA is_active_in, IEA-SubCell, TAS, IDA) -> ACCEPT (core location).
- CC GO:0016020 membrane (NAS PMID:8861954) -> MARK_AS_OVER_ANNOTATED (subsumed by ER membrane; uninformative generic parent).
