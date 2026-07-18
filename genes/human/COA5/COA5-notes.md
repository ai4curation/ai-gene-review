# COA5 (C2orf64 / PET191) review notes

UniProtKB: Q86WW8. Human. 74 aa. HGNC:33848.

## Identity and family
- Small (74 aa) mitochondrial protein of the **PET191 family** (UniProt SIMILARITY: "Belongs to the PET191 family").
- Contains a **CHCH domain (aa 27-65)** with a Cx10C motif (30-41) and a Cx9C motif (47-57), two disulfide bonds (30-57, 41-47) — i.e. a **twin CX9C-family** protein typical of IMS-imported, MIA40/CHCHD4-dependent redox proteins. InterPro IPR018793 (Cyt_c_oxidase_assmbl_Pet191); Pfam PF10203 (Pet191_N); PROSITE CHCH.
- Non-catalytic (no enzymatic activity described; assembly/chaperone-type factor).

## Function (verified)
- **Assembly factor for cytochrome c oxidase (respiratory chain complex IV / CcO)** [UniProt FUNCTION, ECO:0000269|PubMed:21457908, PubMed:35750769].
- Original disease/function paper: Huigsloot et al. 2011 (PMID:21457908, NOT cached locally) — "A mutation in C2orf64 causes impaired cytochrome c oxidase assembly and mitochondrial cardiomyopathy." Establishes an **early step of COX assembly**.
- Nývltová et al. 2022 (PMID:35750769, full text cached): PET191/COA5 is "another IMS-resident twin CX9C protein, PET191 (alias COA5)". Part of the copper/heme metallochaperone modules that regulate CuA (COX2) and CuB (COX1) center biogenesis. PET191 overexpression rescues CcO in COX11-KO cells and elevates COX1/COX2. "PET191 binds Cu in the absence of COX11". "Human PET191 mutations lead to CcO deficiency and fatal hypertrophic cardiomyopathy."
- Reactome (R-HSA-9865449, -9865630, -9865579): COA5 is a subunit of the 9-subunit metallochaperone complex (COA3, COA5, COX10, COX11, COX15, COX16, COX19, SCO1, SCO2) that inserts Cu into MT-CO1 (CuB) / MT-CO2 (CuA) at the mitochondrial inner membrane during Complex IV assembly. These acts are located_in GO:0005743 (mito inner membrane).

## Localization
- **Mitochondrion intermembrane space** [UniProt SUBCELLULAR LOCATION, ECO:0000305|PubMed:35750769]. Consistent with twin CX9C IMS import.
- GOA: GO:0005758 (IMS, IEA UniProt-SubCell), GO:0005739 (mitochondrion, IDA HPA + HTP mito proteome PMID:34800366), GO:0005743 (mito inner membrane, TAS Reactome — the metallochaperone reactions occur at the IM).

## Disease
- **Mitochondrial complex IV deficiency, nuclear type 9 (MC4DN9)** [MIM:616500]; autosomal recessive, fatal infantile hypertrophic cardiomyopathy + complex IV deficiency (fatal infantile cardioencephalomyopathy phenotype). VARIANT A53P (VAR_065499). Orphanet 1561 "Fatal infantile cytochrome C oxidase deficiency."

## Annotation review decisions
- GO:0033617 mitochondrial respiratory chain complex IV assembly (IBA) — **core BP, ACCEPT**. Central verified function.
- Mito localization terms (GO:0005739 mitochondrion x3: IBA/IDA/HTP; GO:0005758 IMS IEA; GO:0005743 inner membrane TAS x3) — **ACCEPT**; IMS is the primary/most-specific curated location; inner membrane reflects where the metallochaperone reactions occur.
- GO:0005515 protein binding (IPI, PMID:25416956 and PMID:32296183) — these are large-scale Y2H binary interactome maps (HuRI etc.); interactors are keratins/KRTAPs/CYSRT1/TCF4 = non-mitochondrial, non-physiological sticky partners. Bare "protein binding", uninformative. Per policy do NOT REMOVE experimental IPIs → **MARK_AS_OVER_ANNOTATED**.

## core_functions
- No informative catalytic/binding MF term is present in GOA (only bare protein binding). COA5 is non-catalytic. Per instructions, omit `function` (do not invent a catalytic MF).
- directly_involved_in: GO:0033617.
- located_in: GO:0005758 (mitochondrial intermembrane space) — the UniProt-curated primary location (also in GOA).
