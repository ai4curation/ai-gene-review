# CH25H (human) — gene review notes

UniProt: O95992 (CH25H_HUMAN). HGNC:1907. Gene on chr 10q23; intronless single-exon gene.

## Summary of function

CH25H is **cholesterol 25-hydroxylase** (EC 1.14.99.38), an ER-membrane, polytopic
(multi-pass) integral membrane enzyme that hydroxylates cholesterol at C-25 to produce
**25-hydroxycholesterol (25-HC)**, using O2 and a **diiron cofactor** — it is emphatically
**NOT a cytochrome P450 / heme enzyme**.

- Cloning + catalytic activity + membrane topology + not-P450/diiron family:
  [PMID:9852097 "Here, we report the cloning of cholesterol 25-hydroxylase cDNAs from the mouse and human. The encoded enzymes are polytopic membrane proteins of 298 and 272 amino acids, respectively, which contain clusters of histidine residues that are essential for catalytic activity."]
  and [PMID:9852097 "Unlike most other sterol hydroxylases, cholesterol 25-hydroxylase is not a cytochrome P450, but rather it is a member of a small family of enzymes that utilize diiron cofactors to catalyze the hydroxylation of hydrophobic substrates."]
- UniProt confirms the reaction and the diiron cofactor:
  [file:human/CH25H/CH25H-uniprot.txt "Catalyzes the formation of 25-hydroxycholesterol from"] and cofactor "Fe cation" (COFACTOR line, by similarity to Q9Z0F5).
- Belongs to the **sterol desaturase / fatty acid hydroxylase family**; three conserved
  histidine-box motifs (His box 1: 142–146; His box 2: 157–161; His box 3: 238–244) that
  coordinate the diiron center. Pfam PF04116 (FA_hydroxylase); InterPro IPR006694/IPR050307;
  PANTHER PTHR11863 (STEROL DESATURASE). (UniProt FT/DR lines.)

## 25-HC as a regulatory oxysterol

1. **Represses cholesterol/lipid biosynthesis (SREBP pathway).** Overexpression of CH25H
   reduces cholesterol biosynthesis and suppresses SREBP-1/-2 cleavage.
   [PMID:9852097 "Expression of cholesterol 25-hydroxylase in transfected cells reduces the biosynthesis of cholesterol from acetate and suppresses the cleavage of sterol regulatory element binding protein-1 and -2."]
   [PMID:9852097 "cholesterol 25-hydroxylase has the capacity to play an important role in regulating lipid metabolism by synthesizing a co-repressor that blocks sterol regulatory element binding protein processing"]
   UniProt: [file:human/CH25H/CH25H-uniprot.txt "regulating lipid metabolism by synthesizing a corepressor that blocks sterol"].

2. **Interferon-stimulated gene / broad antiviral effector.** CH25H is an ISG; 25-HC has
   broad activity against enveloped viruses and blocks viral membrane fusion.
   - [PMID:33239446 "Cholesterol 25-hydroxylase (CH25H) is an interferon (IFN)-stimulated gene that shows broad antiviral activities against a wide range of enveloped viruses."]
   - Antiviral mechanism = blockade of spike-mediated membrane fusion via altering cholesterol:
     [PMID:33239446 "our data support a model that 25HC suppresses SARS-CoV-2 S protein-mediated fusion, which inhibits virus replication, possibly by altering cholesterol levels."]
   - Catalytic His-His mutant abolishes both 25-HC production and antiviral activity (function is
     enzyme-dependent): [PMID:33239446 "mutant CH25H did not produce 25HC and 7-α, 25-diHC"] and
     [PMID:33239446 "mutant CH25H failed to inhibit VSV-SARS-CoV-2 infection like the wild-type protein"].
     UniProt records this human mutant as 242-His-His-243 → QQ (Histidine box-3), loss of activity
     and loss of anti-SARS-CoV-2 (the paper uses its own H422Q/H423Q numbering for the same residues).
   - Independent confirmation (Wang et al.): CH25H induced by SARS-CoV-2, 25-HC blocks fusion by
     activating ER ACAT and depleting accessible plasma-membrane cholesterol:
     [PMID:32944968 "cholesterol 25-hydroxylase (CH25H), is induced by SARS-CoV-2 infection in vitro and in COVID-19-infected patients."]
     [PMID:32944968 "25HC inhibits viral membrane fusion by activating the ER-localized acyl-CoA:cholesterol acyltransferase (ACAT) which leads to the depletion of accessible cholesterol from the plasma membrane."]

3. **Feeds alternative (acidic) bile-acid pathway / immune-cell positioning.** 25-HC is an
   intermediate toward 7α,25-dihydroxycholesterol (7α,25-diHC), a ligand for GPR183/EBI2 that
   guides positioning/chemotaxis of B and T cells. UniProt (By similarity from mouse Q9Z0F5):
   [file:human/CH25H/CH25H-uniprot.txt "an oxysterol that acts as a ligand for the G protein-coupled receptor"].
   Reactome maps CH25H to "Synthesis of bile acids and bile salts" (R-HSA-192105).
   In the antiviral papers, 25-HC → 7α,25-diHC is noted as a T/B-cell chemoattractant:
   [PMID:33239446 "25HC is further converted to 7-α, 25-dihydroxycholesterol (7-α, 25-diHC), an oxysterol that functions as a chemoattractant for T cells and B cells"].

## Localization

ER membrane, multi-pass. [file:human/CH25H/CH25H-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"]
UniProt lists three TM helices (38–58, 84–104, 121–141). The GOA "cytosol" TAS annotation
(Reactome R-HSA-191983) reflects a Reactome reaction location, not the true membrane topology;
ER membrane is the accurate compartment.

## Notes on specific GOA annotations reviewed

- **GO:0001567 cholesterol 25-hydroxylase activity** — the correct, well-supported core MF.
  Present as EXP (PMID:33239446, PMID:9852097), IDA (PMID:32944968), IBA, ISS, IEA — all ACCEPT/consistent.
- **GO:0005506 iron ion binding (IEA/InterPro)** — biologically correct (diiron center); ACCEPT.
  UniProt cofactor is "Fe cation" (ISS from mouse); histidine boxes coordinate the diiron.
- **GO:0000254 C-4 methylsterol oxidase activity (IBA)** — family-level (sterol desaturase / FA
  hydroxylase) IBA leakage from the PANTHER tree; CH25H's demonstrated activity is C-25 hydroxylation
  of cholesterol, not C-4 demethylation of methylsterols. MARK_AS_OVER_ANNOTATED (not the enzyme's function).
- **GO:0036197 zymosterol biosynthetic process (IBA)** — pathway-context IBA leakage; CH25H acts on
  cholesterol, not zymosterol. MARK_AS_OVER_ANNOTATED.
- **GO:0008395 steroid hydroxylase activity (TAS)** — correct but a parent of GO:0001567; MODIFY to the
  specific child.
- **GO:0006629 lipid metabolic process (TAS)** and **GO:0008610 lipid biosynthetic process (IEA)** —
  correct but very general; KEEP_AS_NON_CORE.
- **GO:0035754 B cell chemotaxis (ISS/IEA)** — downstream, indirect (via 7α,25-diHC/EBI2), By similarity
  from mouse; KEEP_AS_NON_CORE.
- **GO:0090206 negative regulation of cholesterol metabolic process (IEA/Ensembl)** — captures the SREBP
  repression role (supported by PMID:9852097); KEEP_AS_NON_CORE (regulatory, downstream of the MF).
- **GO:0034340 response to type I interferon (IDA)** — CH25H is an ISG; ACCEPT as non-core biological context.
- **GO:1903914 negative regulation of fusion of virus membrane with host plasma membrane (IDA x2)** —
  well-supported antiviral BP; ACCEPT.
- **GO:0005515 protein binding (IPI, PMID:32296183)** — from HuRI large-scale binary interactome
  (KRTAP12-4/P60329; OTX1/P32242). Uninformative bare "protein binding"; MARK_AS_OVER_ANNOTATED (do not REMOVE IPI).
- **GO:0005829 cytosol (TAS, Reactome)** — mislocalization artifact of a Reactome reaction location; the
  enzyme is an ER multi-pass membrane protein. MARK_AS_OVER_ANNOTATED.
- **GO:0005789 endoplasmic reticulum membrane (IBA/IEA/ISS)** — correct core location; ACCEPT.

## Disease

Two candidate-gene association studies found LACK of association with Alzheimer's disease
(PMID:15465627, PMID:16157450 per UniProt RN[6]/RN[7]); not a disease gene by these data.
