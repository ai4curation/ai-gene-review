# RABGGTB (P53611) — Gene Review Notes

## Identity and family

- HGNC symbol **RABGGTB** (synonym GGTB); UniProt **P53611** (PGTB2_HUMAN), 331 aa, chromosome 1.
- Names: "Geranylgeranyl transferase type-2 subunit beta", "Rab geranylgeranyltransferase subunit beta", "GGTase-II-beta". [file:human/RABGGTB/RABGGTB-uniprot.txt "RecName: Full=Geranylgeranyl transferase type-2 subunit beta"]
- EC 2.5.1.60. [file:human/RABGGTB/RABGGTB-uniprot.txt "EC=2.5.1.60 {ECO:0000269|PubMed:7991565}"]
- Belongs to the protein prenyltransferase subunit beta family. [file:human/RABGGTB/RABGGTB-uniprot.txt "Belongs to the protein prenyltransferase subunit beta"]
- Six PFTB (protein prenyltransferase) repeats forming the α–α barrel catalytic fold (residues 18–302), confirmed by X-ray structures 6O60, 6J6X/6J74/6J7F/6J7X. [file:human/RABGGTB/RABGGTB-uniprot.txt "REPEAT          18..61"]

## Core molecular function: Rab geranylgeranyltransferase (GGTase-II / RabGGTase) catalytic β subunit

RABGGTB is the **catalytic β subunit** of Rab geranylgeranyltransferase (RabGGTase, GGTase-II). Together with the α subunit RABGGTA it forms the catalytic heterodimer ("component B"); a Rab escort protein (REP1/CHM or REP2/CHML, "component A") presents the unprenylated Rab substrate.

- Function: "Catalyzes the transfer of a geranylgeranyl moiety from geranylgeranyl diphosphate to both cysteines of Rab proteins with the C-terminal sequence -XXCC, -XCXC and -CCXX, such as RAB1A, RAB3A, RAB5A and RAB7A". [file:human/RABGGTB/RABGGTB-uniprot.txt "geranylgeranyl moiety from"]
- Catalytic reaction: "geranylgeranyl diphosphate + L-cysteinyl-[protein] = S-geranylgeranyl-L-cysteinyl-[protein] + diphosphate" (RHEA:21240, EC 2.5.1.60). [file:human/RABGGTB/RABGGTB-uniprot.txt "geranylgeranyl diphosphate + L-cysteinyl-[protein] = S-"]
- Direct biochemical demonstration: recombinant Rab geranylgeranyltransferase + REP + [³H]GGpp geranylgeranylate **both** C-terminal cysteines of Rab1A (-XXCC), Rab3A (-XCXC) and Rab5A (-CCXX). [PMID:7991565 "both C-terminal adjacent cysteines were geranylgeranylated"] This is the EXP annotation supporting the MF (GOA row: EXP PMID:7991565 → GO:0004661).
- Zinc cofactor: "Binds 1 zinc ion per subunit"; catalytic Zn²⁺ ligated by residues 238, 240, 290. [file:human/RABGGTB/RABGGTB-uniprot.txt "Binds 1 zinc ion per subunit"] Note the RABGGTB Zn is a genuine catalytic metal (unlike GGTase-I/FTase context in the task prompt — the UniProt record explicitly assigns Zn binding to this subunit).
- Substrate presentation requires REP: "The enzymatic reaction requires the aid of a Rab escort protein (also called component A)." [file:human/RABGGTB/RABGGTB-uniprot.txt "requires the aid of a Rab"]

## Complex membership

- Heterotrimer RABGGTA:RABGGTB:CHM; RABGGTA+RABGGTB = catalytic component B, CHM (REP1) = component A. [file:human/RABGGTB/RABGGTB-uniprot.txt "Heterotrimer composed of RABGGTA, RABGGTB and CHM"]
- GO complex: **Rab-protein geranylgeranyltransferase complex (GO:0005968)**. ISS from Q08603 (rat ortholog) and IBA. ComplexPortal CPX-2919 "Protein geranylgeranyltransferase type II complex".
- Moonlighting: RABGGTB is also the shared β subunit of **GGTase-III** (with the orphan α subunit PTAR1), which geranylgeranylates FBXL2 (Kuchay 2019) and the Golgi v-SNARE YKT6 at Cys194 (Shirakawa 2020). ComplexPortal CPX-26511 "Protein geranylgeranyltransferase type III complex". [file:human/RABGGTB/RABGGTB-uniprot.txt "Part of the GGTase-3 complex, composed of PTAR1 and RABGGTB"]
  - GGTase-III = PTAR1 + β subunit of RabGGTase. [PMID:32128853 "GGTase‐III consists of prenyltransferase alpha subunit repeat containing 1 (PTAR1) and the β subunit of RabGGTase"]
  - GGTase-III geranylgeranylates mono-farnesylated YKT6 → doubly prenylated YKT6, required for Golgi SNARE assembly. [PMID:32128853 "Double prenylation of Ykt6 is essential for the structural and functional organization of the Golgi apparatus"]
  - Gly49 of RABGGTB is essential for YKT6 geranylgeranylation (mutagenesis G49I/L abolishes it). [file:human/RABGGTB/RABGGTB-uniprot.txt "Abolishes geranylgeranylation of YKT6"]
  - Note: Shirakawa 2020 questions whether FBXL2 is a physiological GGTase-III substrate (GGTase-I can prenylate FBXL2; FBXL2 still localizes to membrane in PTAR1-KO cells). [PMID:32128853 "it remains uncertain whether FBXL2 is a physiological substrate for GGTase‐III"]

## Biological process

- **Protein geranylgeranylation (GO:0018344)** — the direct BP; ISS from Q08603. Double geranylgeranylation anchors Rab GTPases to membranes for vesicle trafficking.
- **RAB geranylgeranylation** Reactome pathway R-HSA-8873719 (in UniProt DR).
- ER→Golgi vesicle-mediated transport (GO:0006888) IBA / protein targeting to membrane (GO:0006612) IBA — downstream/consequence framing; RABGGTB itself is the enzyme, so these are process-level (KEEP_AS_NON_CORE) rather than the core catalytic function.

## Choroideremia context (GO:0007601 visual perception)

- Choroideremia (X-linked retinal degeneration) is caused by mutations in **CHM (REP1/component A)**, NOT in RABGGTB. The deficiency is in component A, not component B. [PMID:8380507 "showed a marked deficiency in the activity of component A, but not component B, of Rab GG transferase"]
- The visual_perception (GO:0007601, TAS PMID:8380507) and protein_modification_process (GO:0036211, NAS PMID:8380507) annotations to RABGGTB derive from a paper about CHM/REP1 (component A). RABGGTB (component B) is not the disease gene; visual_perception is at best a very indirect/pathway-level association and over-annotated for this catalytic subunit. Reference PMID:8380507 is about REP1/CHM, so relevance to RABGGTB is LOW/background.

## Protein–protein interactions (bare GO:0005515 IPI annotations)

Multiple IntAct "protein binding" (GO:0005515) IPI annotations. WITH/FROM partners:
- Q92696 = RABGGTA (α subunit; the biologically meaningful obligate partner). [file:human/RABGGTB/RABGGTB-uniprot.txt "P53611; Q92696: RABGGTA; NbExp=10"]
- Q7Z6K3 = PTAR1 (GGTase-III α subunit). [file:human/RABGGTB/RABGGTB-uniprot.txt "P53611; Q7Z6K3: PTAR1; NbExp=18"]
- Q9UKC9 = FBXL2 (GGTase-III substrate). [file:human/RABGGTB/RABGGTB-uniprot.txt "P53611; Q9UKC9: FBXL2; NbExp=6"]
- P10398 = ARAF (PMID:12620389 Raf Y2H screen; ARAF CRD found to interact with 20 proteins broadly — likely low-specificity). [PMID:12620389 "The cysteine-rich zinc-binding domain (CRD) of Raf was found to interact with all 20 proteins"]
- P57081 = WDR4; Q7Z5A9 = TAFA1; Q86YD3 = TMEM25; Q9UBV7 = B4GALT7; P24592 = IGFBP6 — high-throughput interactome hits (HuRI, BioPlex, OpenCell, etc.), no evidence these are functional.
- PTP4A2 (PRL-2): prenylated PTP4A2 binds RABGGTB and precludes its association with RABGGTA, inhibiting enzyme activity. [file:human/RABGGTB/RABGGTB-uniprot.txt "precludes its association with RABGGTA and inhibits"] (from PMID:11447212, not cached; abstract-only).

All GO:0005515 "protein binding" IPI annotations are uninformative per curation policy (do not tell us the actual function) → MARK_AS_OVER_ANNOTATED (never REMOVE an IPI per policy). The informative content (RABGGTA, PTAR1 partnership) is captured via the complex terms.

## Location

- Cytosol (GO:0005829, Reactome TAS) and cytoplasm (GO:0005737, ARBA IEA) — consistent; RabGGTase is a cytosolic enzyme. Plasma membrane (GO:0005886, Reactome TAS) reflects the site where prenylated substrates/FBXL2 act rather than a stable localization of the enzyme; keep as non-core.

## Electronic MF annotations

- GO:0004663 Rab geranylgeranyltransferase activity — correct core MF (ISS from Q08603; IEA GO_REF:0000120 via EC 2.5.1.60 + InterPro; IBA contributes_to). ACCEPT.
- GO:0004661 protein geranylgeranyltransferase activity — parent of GO:0004663; correct but less specific (EXP PMID:7991565; IEA RHEA). The EXP one is experimentally grounded; MODIFY the general electronic ones toward GO:0004663 where appropriate, but EXP itself supports the specific activity so keep the EXP.
- GO:0008318 protein prenyltransferase activity (IEA InterPro) — correct but general grandparent; over-general.
- GO:0003824 catalytic activity (IEA InterPro) — root-level, uninformative; over-general.
- GO:0008270 zinc ion binding (ISS) — supported: catalytic Zn²⁺ bound by RABGGTB. ACCEPT as non-core molecular detail (or ACCEPT).
- GO:0031267 small GTPase binding (ISS) — RabGGTase engages Rab (small GTPase) substrates (presented by REP); supported. Non-core.

## Summary of key references (cached)

- PMID:7991565 (abstract-only) — biochemistry of di-geranylgeranylation of Rab1A/3A/5A. Supports core MF/BP.
- PMID:31209342 (abstract-only) — GGTase-III = PTAR1 + RABGGTB; geranylgeranylates FBXL2. Supports GGTase-III complex membership.
- PMID:32128853 (full text) — GGTase-III geranylgeranylates YKT6; Golgi SNARE assembly. Supports GGTase-III complex + Golgi function.
- PMID:8380507 (abstract-only) — choroideremia = component A (CHM/REP1) deficiency, NOT component B (RABGGTB). Relevant to CHM, background for RABGGTB.
- PMID:12620389 (abstract-only) — Raf Y2H interactome; ARAF CRD binds many proteins (low specificity). Background only.
- Interactome papers PMID:25416956, 28514442, 32296183, 33961781, 35271311, 40205054 — high-throughput binary/proximity interaction maps; not gene-specific functional evidence.
