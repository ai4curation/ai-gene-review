# FCGRT (P55899) Curation Notes

## Gene & Protein Identity
- **HGNC Symbol:** `FCGRT` (Synonyms: `FCRN`)
- **UniProt Accession:** `P55899` (`FCGRN_HUMAN`, IgG receptor FcRn large subunit p51 / Neonatal Fc receptor alpha chain)
- **Taxon:** *Homo sapiens* (`NCBITaxon:9606`)
- **Architecture:** 365 amino acids (`39,743 Da` precursor):
  - Signal peptide: residues 1–23 [file:genes/human/FCGRT/FCGRT-uniprot.txt]
  - Mature chain (p51): residues 24–365 [file:genes/human/FCGRT/FCGRT-uniprot.txt]
  - Extracellular topological domain: residues 24–297, comprising MHC class I-like Alpha-1 (24–110), Alpha-2 (111–200), Alpha-3 Ig-like C1-type domain (201–290; `DOMAIN 202..289`), and connecting peptide (291–297), stabilized by intrachain disulfide bonds `Cys119-Cys182` and `Cys221-Cys275` and N-glycosylated at `Asn125` [file:genes/human/FCGRT/FCGRT-uniprot.txt].
  - Transmembrane domain: helical single-pass type I segment at residues 298–321 [file:genes/human/FCGRT/FCGRT-uniprot.txt].
  - Cytoplasmic tail: residues 322–365 (phosphorylated at `Ser334`) [file:genes/human/FCGRT/FCGRT-uniprot.txt].

## Molecular Function & Subunit Assembly
1. **Heterodimerization with Beta-2-Microglobulin (`GO:0030881`):**
   - `FCGRT` encodes the heavy $\alpha$-chain (p51) of the neonatal Fc receptor (FcRn), which obligately pairs non-covalently with the invariant light chain $\beta_2$-microglobulin (`B2M`, p14) to form a functional MHC class I-like heterodimer (`FcRn complex consists of two subunits: p51, and p14 which is equivalent to beta-2-microglobulin. It forms an MHC class I-like heterodimer`) [file:genes/human/FCGRT/FCGRT-uniprot.txt; PMID:31104841, "FcRn is an MHC class I-like protein consisting of a heavy α chain encoded by the FCGRT gene, and a light β2-microglubulin (β2 m) chain encoded by the B2M gene."].
2. **pH-Dependent IgG Binding (`GO:0019864`) and Albumin Binding:**
   - Cloned from human placenta by Story et al. (1994), human FcRn binds the Fc region of monomeric IgG strictly in a pH-dependent manner: high affinity at acidic endosomal pH ($\text{pH } 5.5\text{--}6.0$) and negligible binding at neutral physiological pH ($\text{pH } 7.4$) [PMID:7964511, "Like rat and mouse FcRn, hFcRn binds IgG preferentially at low pH, which may imply that IgG binds hFcRn in an acidic intracellular compartment during transport across the placenta."].
   - In addition to monomeric IgG, FcRn binds serum albumin (`ALB`) at a non-overlapping site in a similarly pH-dependent manner in acidic endosomes, protecting circulating albumin from lysosomal degradation and maintaining serum albumin homeostasis [file:genes/human/FCGRT/FCGRT-uniprot.txt, "In addition of IgG, regulates homeostasis of the other most abundant circulating protein albumin/ALB (PubMed:24469444, PubMed:28330995)."].
3. **Occluded Peptide Groove (`NOT GO:0042605` `peptide antigen binding`):**
   - Although `FCGRT` shares the MHC class I $\alpha_1\text{--}\alpha_2$ platform and $\alpha_3$ Ig-like C1-set fold, its counterpart to the MHC class I peptide-binding groove is narrowed and occluded by side-chain interactions bridging the $\alpha_1$ and $\alpha_2$ helices, so FcRn does not bind or present antigenic peptides (`NOT GO:0042605`, ISS from rat `Fcgrt` `UniProtKB:P13599`; `PMID:10933786`).

## Cellular Localization & Trafficking
- **Endosome Membrane (`GO:0010008`) & Plasma Membrane (`GO:0005886` / `GO:0009897`):**
  - Steady-state FcRn resides predominantly in acidic early/sorting and recycling endosomal membranes and cycles continuously between the endosome membrane and the plasma membrane [PMID:31104841, "Consistently, CD55 was mainly localized on the cell surface, whereas FcRn displayed substantial expression within the cytoplasm, presumably on the endosome membrane"; "FcRn is expressed both on the cell surface and in the cytoplasm."].
  - At the cell surface, the $\alpha_1\text{--}\alpha_3$ ectodomain and associated B2M subunit project into the extracellular space (`GO:0009897` `external side of plasma membrane`); upon endocytosis, this ectodomain faces the acidic endosomal lumen where ligand capture occurs.

## Biological Processes
1. **Epithelial IgG Transcytosis & Humoral IgG/Albumin Salvage (`GO:0002416`):**
   - Transfers maternal passive humoral immunity to the fetus/newborn across placental syncytiotrophoblasts and intestinal epithelial barriers, and recycles monomeric IgG and albumin in vascular endothelial and hematopoietic cells throughout life to extend their serum half-lives [PMID:7964511; file:genes/human/FCGRT/FCGRT-uniprot.txt].
2. **Hijacked Uncoating Receptor for Enterovirus B (Microbial Infection):**
   - Zhao et al. (2019) demonstrated via CRISPR-Cas9 knockout screening and cryo-EM structures that the FcRn heterodimer (`FCGRT` + `B2M`) is hijacked as the universal endosomal uncoating receptor for major Enterovirus B (EV-B) serotypes (including Echovirus 6 and related echoviruses, EV-B85, and CV-A9). The $\alpha_2$ helices of `FCGRT` (residues Q139, R140, Q143, Q144, D145, K146) insert into the viral capsid "canyon" (primarily contacting VP1) and trigger release of the lipid "pocket factor" at acidic endosomal pH ($\text{pH } 5.5$) to initiate capsid uncoating [PMID:31104841]. Because viral uncoating is a pathogen-driven process hijacking the host receptor rather than an evolved host physiological process, it is documented as contextual biology rather than a core endogenous GO biological process of `FCGRT`.

## Annotation Review Summary
- **Accepted Core Annotations:**
  - `GO:0019864` (`IgG binding`, IDA, `PMID:7964511`) -> `ACCEPT`
  - `GO:0030881` (`beta-2-microglobulin binding`, IBA `GO_REF:0000033` & IEA `GO_REF:0000107`) -> `ACCEPT`
  - `GO:0002416` (`IgG immunoglobulin transcytosis in epithelial cells mediated by FcRn immunoglobulin receptor`, NAS, `PMID:7964511`) -> `ACCEPT`
  - `GO:0010008` (`endosome membrane`, EXP `PMID:31104841` & IEA `GO_REF:0000044`) -> `ACCEPT`
  - `GO:0009897` (`external side of plasma membrane`, IBA `GO_REF:0000033`) -> `ACCEPT`
  - `GO:0005886` (`plasma membrane`, IEA `GO_REF:0000044` & ISS `GO_REF:0000024`) -> `ACCEPT`
  - `NOT GO:0042605` (`peptide antigen binding`, ISS `GO_REF:0000024`, `negated: true`) -> `ACCEPT`
- **Modified / Refined Annotations:**
  - `GO:0005576` (`extracellular region`, IBA `GO_REF:0000033` from `PANTHER:PTN002703355`): `FCGRT` is a single-pass type I integral membrane receptor, not a soluble secreted extracellular protein (unlike `AZGP1`/`P25311` in `PTN002703355`). Refined (`MODIFY`) to `GO:0009897` (`external side of plasma membrane`) and `GO:0010008` (`endosome membrane`).
  - `GO:0006955` (`immune response`, IBA `GO_REF:0000033` from `PANTHER:PTN002703355`): Broad ancestral MHC class I-like node annotation; refined (`MODIFY`) to the specific FcRn-mediated immunological transport process `GO:0002416` (`IgG immunoglobulin transcytosis in epithelial cells mediated by FcRn immunoglobulin receptor`).
  - `GO:0016020` (`membrane`, IEA `GO_REF:0000117`): Broad membrane term refined (`MODIFY`) to `GO:0010008` (`endosome membrane`) and `GO:0005886` (`plasma membrane`).
- **Removed Uninformative Annotations:**
  - `GO:0005515` (`protein binding`, IPI `PMID:32296183` with `O00526` UPK2, `Q01453` PMP22, `Q8N6F1-2` CLDN19, `Q92520` FAM3C, `Q9NZG7` NINJ2): Removed per the generic protein-binding policy (`REMOVE`); these are binary yeast two-hybrid hits from the proteome-wide HuRI screen with no established functional significance for FcRn.
- **Proposed NEW Annotations & Ontology Terms:**
  - `GO:0038024` (`cargo receptor activity`, IDA `PMID:24469444`) -> `NEW` (Captures pH-dependent endocytic cargo receptor activity of FCGRT binding serum albumin and monomeric IgG at non-overlapping sites in acidic endosomes; `PMID:24469444`, `file:genes/human/FCGRT/FCGRT-uniprot.txt`).
  - `GO:0001618` (`virus receptor activity`, IDA `PMID:31104841`) -> `NEW` (Captures FCGRT acting as the endosomal uncoating receptor for major Enterovirus B serotypes during microbial infection; `PMID:31104841`, `file:genes/human/FCGRT/FCGRT-uniprot.txt`).
  - `proposed_new_terms`: `albumin transcytosis` (proposed child of `GO:0045056` `transcytosis`, supported by `PMID:28330995` and `file:genes/human/FCGRT/FCGRT-uniprot.txt`, since ancestor `GO:0045056` cannot be proposed as `NEW` alongside existing descendant `GO:0002416`).
