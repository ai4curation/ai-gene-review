# DNAJC6 (O75061) research notes

## Identity
- Auxilin (auxilin-1); DnaJ homolog subfamily C member 6. 913 aa.
- Domains: N-terminal tensin-type phosphatase (PTEN-like) domain (aa 55-222) + C2 tensin-type domain (228-366) [PTEN/C2 module]; long disordered clathrin-binding middle region; C-terminal J domain (aa 849-913) [file:human/DNAJC6/DNAJC6-uniprot.txt "DOMAIN 849..913 /note=\"J\""].
- Neuronal-specific (brain/retina enriched); cyclin-G-associated kinase GAK is the ubiquitous homolog.

## Function (UniProt FUNCTION + PMID:18489706, 20160091)
- Co-chaperone that recruits HSPA8/HSC70 to clathrin-coated vesicles (CCVs) and promotes the ATP-dependent dissociation of clathrin from CCVs; participates in clathrin-mediated endocytosis of synaptic vesicles and recycling [uniprot FUNCTION].
- Binds tightly to clathrin cages (1 auxilin per triskelion); HSPA8:ATP then binds, ATP hydrolysis dismantles the cage. J domain mediates HSPA8 interaction and is required for basket dissociation [uniprot DOMAIN].
- PMID:18489706 (Hirst et al.): "Auxilin is a cofactor for Hsc70-mediated uncoating of clathrin-coated vesicles (CCVs)"; depletion of both auxilins inhibits clathrin-mediated endocytosis and causes nonproductive clathrin cages.
- PMID:20160091 (Yim et al.): auxilin KO mouse; "auxilin and ... GAK ... act as cochaperones to support the Hsc70-dependent clathrin uncoating of clathrin-coated vesicles"; specialized role in synaptic vesicle recycling.

## Phosphatase
- Annotated EC 3.1.3.- "May act as a protein phosphatase and/or a lipid phosphatase." The PTEN-like phosphatase domain is generally considered catalytically inactive/degenerate in auxilin (acts as a phosphoinositide-binding targeting module). Keep phosphatase MF cautiously / non-core; it is speculative ("May act").

## Interactions
- HSPA8/HSC70 (ATP-dependent; stimulates ATPase); CLTC (clathrin heavy chain, Q00610; IPI PMID:29735704); AP2A2; DNM1(GTP). 
- PMID:29735704 (Nguyen & Krainc): LRRK2 phosphorylates auxilin at Ser-loc in clathrin-binding domain -> disrupted SVE in PD dopaminergic neurons. (Note: paper text says Ser627; UniProt residue Ser-570 in canonical numbering. The IPI is CLTC.)

## Disease
- PARK19A (juvenile-onset, autosomal recessive) and PARK19B (early-onset) Parkinson disease [PMID:22563501, 23211418, 26703368, 26528954]. Loss-of-function -> impaired synaptic vesicle endocytosis in dopaminergic neurons.

## Curation judgment
- Core MF: (1) clathrin binding / clathrin heavy chain binding (GO:0030276 / GO:0032050) — direct, ISS-supported and IPI with CLTC; (2) HSP70/HSC70 co-chaperone (heat shock protein binding GO:0031072 / ATPase activator) — J domain recruits & stimulates HSPA8.
- Core BP: clathrin coat disassembly / synaptic vesicle uncoating / clathrin-dependent endocytosis (IMP for human; ISS/IBA for the rest). ACCEPT the IMP and IBA; ISS duplicates ACCEPT/KEEP_AS_NON_CORE.
- Cytosol (many redundant Reactome TAS) and CCV / vesicle / postsynaptic density localizations: ACCEPT (clathrin-coated vesicle, cytoplasm) or KEEP_AS_NON_CORE.
- protein binding IPI (CLTC, Q00610): MODIFY to clathrin heavy chain binding (GO:0032050) — informative MF.
- phosphoprotein phosphatase activity (IEA-KW): speculative degenerate phosphatase; MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE.
