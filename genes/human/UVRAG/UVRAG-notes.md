# UVRAG review notes

## Scope

UVRAG is reviewed here in the proteostasis-network neighborhood around class III PI3K complexes and late autophagy/endolysosomal trafficking. PN entries without PMIDs were used only as search/context cues, not as evidence.

## Evidence synthesis

UVRAG is a Beclin 1/class III PI3K complex regulator. The original autophagy paper identifies UVRAG as a "positive regulator of the Beclin1-PI(3)KC3 complex" and states that "UVRAG-mediated activation of the Beclin1-PI(3)KC3 complex promotes autophagy" [PMID:16799551, "positive regulator of the Beclin1-PI(3)KC3 complex"; PMID:16799551, "UVRAG-mediated activation of the Beclin1-PI(3)KC3 complex promotes autophagy"]. The C1/C2 split is important: mammalian Atg14 and UVRAG both bind Beclin 1/Vps34 but "Atg14, and UVRAG are not present in the same complex", supporting UVRAG as the type II/PI3KC3-C2 subunit rather than the ATG14 C1 subunit [PMID:18843052, "Atg14, and UVRAG are not present in the same complex"].

The best-supported PN-relevant process is autophagosome maturation and late endolysosomal fusion. UVRAG "interacts with the class C Vps complex" and that interaction "stimulates Rab7 GTPase activity and autophagosome fusion with late endosomes/lysosomes" [PMID:18552835, "interacts with the class C Vps complex"; PMID:18552835, "stimulates Rab7 GTPase activity and autophagosome fusion with late endosomes/lysosomes"]. Pacer/RUBCNL further links UVRAG to autophagosome-specific PI3KC3/HOPS recruitment: "Pacer recruits PI3KC3 and HOPS complexes to the autophagosome" and the paper explicitly frames this in "autophagosome maturation" [PMID:28306502, "Pacer recruits PI3KC3 and HOPS complexes to the autophagosome"; PMID:28306502, "autophagosome maturation"]. UniProt also summarizes UVRAG as a PI3KC3-C2 subunit that "mediates formation of phosphatidylinositol 3-phosphate" and is "involved in maturation of autophagosomes and endocytosis" [file:human/UVRAG/UVRAG-uniprot.txt, "PI3KC3-C2) that mediates formation of phosphatidylinositol 3-phosphate"; file:human/UVRAG/UVRAG-uniprot.txt, "involved in maturation of autophagosomes and endocytosis"].

UVRAG also has a real endosomal/Golgi-ER trafficking role that should be retained but not mistaken for the PN class III PI3K component term. A PtdIns(3)P/ER tethering study identifies UVRAG as "a phosphatidylinositol-3-phosphate (PtdIns(3)P)-binding protein" and says it "acts as an integral component of the RINT-1-containing ER tethering complex" [PMID:24056303, "phosphatidylinositol-3-phosphate (PtdIns(3)P)-binding protein"; PMID:24056303, "acts as an integral component of the RINT-1-containing ER tethering complex"]. It also connects autophagy to ATG9 transport by reporting that UVRAG works with the "Bif-1-beclin-1-PI(3)KC3 complex to mobilize Atg9 translocation" [PMID:24056303, "Bif-1-beclin-1-PI(3)KC3 complex to mobilize Atg9 translocation"].

SNARE/HOPS binding is specific enough to preserve where GOA has SNARE binding or SNARE complex assembly. UVRAG "mediates viral endocytic transport and membrane penetration through interactions with the class C vacuolar protein sorting (C-Vps) tethering complex and endosomal glutamine-containing SNAREs" and the authors conclude that UVRAG regulates viral entry "by assembling a specific fusogenic SNARE complex" [PMID:24550300, "interactions with the class C vacuolar protein sorting (C-Vps) tethering complex and endosomal glutamine-containing SNAREs"; PMID:24550300, "by assembling a specific fusogenic SNARE complex"]. This virus-entry case is host-pathogen context, but it supports the biochemical SNARE/HOPS interaction axis summarized by UniProt.

The DNA repair and centrosome/chromosome annotations are experimentally supported but non-core for the proteostasis review. UVRAG "promotes DNA double-strand-break repair by directly binding and activating DNA-PK in nonhomologous end joining", and the same study reports that disrupting its centrosome association causes "centrosome instability and aneuploidy" [PMID:22542840, "promotes DNA double-strand-break repair by directly binding and activating DNA-PK in nonhomologous end joining"; PMID:22542840, "centrosome instability and aneuploidy"]. These should be retained as non-core rather than removed.

## Curation calls

- Treat UVRAG as the UVRAG-containing class III PI3K complex II regulatory/adaptor subunit. Replace generic `GO:0035032 phosphatidylinositol 3-kinase complex, class III` and `GO:0032991 protein-containing complex` rows with `GO:0034272 phosphatidylinositol 3-kinase complex, class III, type II`.
- Accept or keep core-relevant rows for `GO:0097352 autophagosome maturation`, `GO:1901098 positive regulation of autophagosome maturation`, `GO:0036092 phosphatidylinositol-3-phosphate biosynthetic process`, `GO:0000149 SNARE binding`, and `GO:0035493 SNARE complex assembly`.
- Keep endosome/lysosome/autophagosome locations, but mark very broad cellular component rows as non-core or over-annotated where more specific locations exist.
- Mark generic `GO:0005515 protein binding` rows as over-annotated. The underlying interactions are often real, but the term is not informative for gene function; the useful annotations are complex membership, SNARE binding, HOPS/class C VPS interaction context, and DNA-PK/centrosome non-core biology.
- Keep DNA repair, NHEJ, DNA-PK colocalization, centrosome cycle, chromosome segregation, and related localization rows as non-core.

## Falcon

Falcon deep research was started for UVRAG on 2026-06-02. The run timed out after the configured 600 seconds and did not produce `UVRAG-deep-research-falcon.md`; the review therefore relies on local UniProt, GOA, Reactome, and cached publication evidence.
