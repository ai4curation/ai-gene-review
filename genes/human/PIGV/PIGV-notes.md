# PIGV (GPI alpha-1,6-mannosyltransferase 2 / GPI-MT-II) — review notes

UniProtKB: Q9NUD9. HGNC:26031. 493 aa, multi-pass ER membrane protein (8 predicted TM helices).
CAZy GT76 (glycosyltransferase family 76); Pfam PF04188 (Mannosyl_trans2); InterPro IPR007315 (PIG-V/Gpi18).

## Core function (verified)

PIGV is GPI mannosyltransferase II (GPI-MT-II). It transfers the **second mannose**, via an
**alpha-1,6 linkage**, from **dolichyl-phosphate-mannose (Dol-P-Man)** onto the growing GPI
intermediate (Man1-GlcN-(acyl)PI -> Man2-GlcN-(acyl)PI), the seventh step of GPI-anchor
biosynthesis, on the lumenal face of the ER membrane.

- [PMID:15623507 "Here we report the cloning of PIG-V involved in transferring the second mannose in the GPI anchor. Human PIG-V encodes a 493-amino acid, endoplasmic reticulum (ER) resident protein with eight putative transmembrane regions."] — human PIG-V cloning, ER localization, topology; abstract-only cache but full text carries CATALYTIC ACTIVITY, PATHWAY, SUBCELLULAR LOCATION, TOPOLOGY, and mutagenesis (Trp66, Asp67, PP293-294, Gln308, Trp312) per UniProt RN[6].
- [PMID:15720390 "A bioinformatics-based strategy identified the essential Saccharomyces cerevisiae Ybr004c protein as a candidate for the second GPI alpha-mannosyltransferase (GPI-MT-II)."] — yeast Ybr004c/GPI18 = ortholog; human homologue complements yeast (IGI with S. cerevisiae P38211/GPI18).
- UniProt CATALYTIC ACTIVITY: RHEA:60488 (Dol-P-Man + Man1-GlcN-acyl-PI -> Man2-GlcN-acyl-PI). EC 2.4.1.-. PATHWAY: Glycolipid biosynthesis; GPI-anchor biosynthesis (UPA00196).

## GOA MF term
GOA carries the specific term **GO:0120563 dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity**
(IBA GO_REF:0000033; IMP+IGI PMID:15623507; also broader GO:0004376 GPI mannosyltransferase activity and
GO:0000009 alpha-1,6-mannosyltransferase activity as IEA/IGI/TAS). GO:0120563 is a subclass of both broader
terms and is the exact catalytic activity of PIGV — used as the core MF.

## Localization
ER membrane, multi-pass (GO:0005789) — UniProt SUBCELLULAR LOCATION ECO:0000269|PubMed:15623507; also
HPA IDA to ER (GO:0005783).

## Complex
GOA IBA GO:0031501 mannosyltransferase complex (part_of). GPI-MT-II activity is attributed to PIG-V "or a
component of the catalyst" (Reactome R-HSA-162873). Mammalian GPI-MT-II is a complex (PIGV with PIGX/PIGN etc.),
so complex membership is reasonable at IBA level; keep as non-core supporting term.

## Disease
Hyperphosphatasia with impaired intellectual development syndrome 1 (HPMRS1 / Mabry syndrome), MIM 239300:
elevated serum alkaline phosphatase, intellectual disability, seizures, hypotonia, facial dysmorphism.
Variants Q256K, A341E/V, H385P (PMID:20802478). Original Mabry syndrome description PMID:5465362.
(Disease context; not a GOA annotation to review.)

## Protein binding IPI (PMID:32814053)
Large-scale Y2H neurodegenerative-disease interactome. Three bare GO:0005515 protein binding IPIs
(TGFBR2 P37173, CBX5 P45973, SERPINH1 P50454). Uninformative for molecular function; per curation policy
bare protein binding from high-throughput screens -> MARK_AS_OVER_ANNOTATED (not REMOVE). These are unlikely
physiological partners of an ER-lumenal GPI biosynthetic enzyme.

## Schema note
core_functions: directly_involved_in and locations are multivalued (list of Term);
molecular_function and in_complex are single inlined Term.

## Action plan for GOA lines
- GO:0120563 MF (IBA/IMP/IGI) -> ACCEPT (core MF)
- GO:0004376 GPI mannosyltransferase activity (IEA/TAS) -> ACCEPT (correct parent)
- GO:0000009 alpha-1,6-mannosyltransferase activity (IEA/IGI) -> ACCEPT (correct parent)
- GO:0006506 GPI anchor biosynthetic process (IBA/IEA/TAS/IMP/IGI) -> ACCEPT (core BP)
- GO:0005789 ER membrane (IBA/IEA/TAS/IDA) -> ACCEPT (core CC)
- GO:0005783 endoplasmic reticulum (IDA HPA) -> ACCEPT (parent CC; correct but less specific than ER membrane)
- GO:0031501 mannosyltransferase complex (IBA part_of) -> KEEP_AS_NON_CORE
- GO:0005515 protein binding x3 (IPI) -> MARK_AS_OVER_ANNOTATED
