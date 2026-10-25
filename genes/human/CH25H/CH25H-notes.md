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

## Paired horse benchmark evidence review

The human reference supplies mechanistic evidence for the corresponding selected horse protein; the human conclusion alone is not validation of the horse sequence. The exact horse comparison is in `genes/HORSE/CH25H/CH25H-bioinformatics/RESULTS.md`. Research reports are source leads; annotation decisions cite the underlying publication or experimentally supported UniProt passages. Unresolved source-specific results retain UNDECIDED.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: full re-review of every existing annotation, the description and core functions of
O95992. ProtNLM2 predictions were not opened or used.

### Identity
- O95992 is the reviewed, canonical UniProt entry (CH25H_HUMAN, 272 aa, single chain
  PRO_0000226801, three predicted TM helices 38-58, 84-104, 121-141, histidine boxes 1-3 intact).
  It is not an isoform, fragment or alternative gene model; the folder is keyed to the canonical product.

### Evolutionary placement
- PANTHER PTHR11863 (STEROL DESATURASE); subfamily PTHR11863:SF213 "CHOLESTEROL 25-HYDROXYLASE"
  (PANTHER 19.0 member index). MSMO1 (Q15800) is in SF225; ERG3/SC5D-type desaturases in SF226.
- PAINT (interpro/panther/PTHR11863/PTHR11863-paint.tsv):
  - PTN002627316 (taxon 117571, Euteleostomi): GO:0001567 cholesterol 25-hydroxylase activity,
    seeded by MGI:1333869 (mouse Ch25h) and UniProtKB:O95992. This is the CH25H-specific node.
  - PTN000221246 (Eukaryota): GO:0000254 C-4 methylsterol oxidase activity, GO:0005789 ER membrane,
    and (in the newer PAINT file, not yet in this GOA snapshot) GO:0016126 sterol biosynthetic process;
    seeds are methylsterol oxidases (MSMO1, ERG25, plant SMOs).
  - PTN002275159 (Eumetazoa): GO:0036197 zymosterol biosynthesis and GO:0006695 cholesterol biosynthesis,
    seeded by mouse Msmo1 (+ zebrafish in the newer file).
- The curators placed the cholesterol 25-hydroxylase grant on the CH25H clade node and placed C-4
  methylsterol oxidation on deep nodes seeded only by MSMO1/ERG25-type members. CH25H inherits the
  deep-node terms mechanically, but its own subfamily diverged in substrate position (side-chain C-25
  of cholesterol, not C-4 methyl of 4,4-dimethylsterols). Only the shared ER-membrane location and
  diiron histidine-box chemistry are family-wide. The PTHR11863 family review agrees (C-4 methylsterol
  oxidase "not supported for CH25H"); no subfamily-placement disagreement found.

### Action changes vs the previous review
- GO:0000254 C-4 methylsterol oxidase activity (IBA): MARK_AS_OVER_ANNOTATED -> REMOVE (wrong activity
  for the CH25H subfamily, not an over-broad one).
- GO:0036197 zymosterol biosynthetic process (IBA): MARK_AS_OVER_ANNOTATED -> REMOVE (CH25H acts on
  cholesterol, downstream of zymosterol; source node seeded by Msmo1 only).
- GO:0005515 protein binding (IPI x2, HuRI): MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE -> REMOVE for
  both rows, per the protein-binding policy; the two rows are now consistent.
- GO:0005829 cytosol (TAS, Reactome): MARK_AS_OVER_ANNOTATED -> REMOVE (integral ER membrane enzyme;
  reaction-compartment artifact).
- GO:0006629 lipid metabolic process (TAS): KEEP_AS_NON_CORE -> MODIFY to GO:0008203 cholesterol
  metabolic process (descendant already carried by IDA).
- GO:0008610 lipid biosynthetic process (IEA): KEEP_AS_NON_CORE retained; no oxysterol/25-HC
  biosynthetic process term exists in GO (label search of local GO for "hydroxycholesterol" and
  "oxysterol" returned only binding, transfer, 7-alpha-hydroxylase and receptor-signalling terms).
- GO:0034340 response to type I interferon (IDA): ACCEPT -> KEEP_AS_NON_CORE (context of deployment
  as an ISG; antiviral effect captured by GO:1903914). Removed from core_functions directly_involved_in.
- Unchanged: ER membrane (ACCEPT x3), cholesterol 25-hydroxylase activity (ACCEPT x6), iron ion binding
  (ACCEPT), cholesterol metabolic process (ACCEPT), negative regulation of viral fusion with host PM
  (ACCEPT x2), B cell chemotaxis (KEEP_AS_NON_CORE x2; CH25H makes the precursor of the EBI2 ligand
  but does no step of chemotaxis), negative regulation of cholesterol metabolic process
  (KEEP_AS_NON_CORE), steroid hydroxylase activity (MODIFY -> GO:0001567).
- No NEW annotations proposed. Candidate "bile acid biosynthetic process" (25-HC feeds CYP7B1 in the
  acidic pathway) was not added: it is a minor route, not curated on CH25H by GO/MGI, and the
  bile_acid_synthesis_ring_modification module lists CH25H only as an upstream oxysterol source.

### Relative to review next
- Mouse Ch25h (Q9Z0F5, MGI:1333869): ortholog, same PANTHER subfamily SF213 and co-seed of PAINT node
  PTN002627316. Extensive mouse experimental work (antiviral, EBI2/7a,25-OHC lymphocyte positioning,
  macrophage inflammasome restraint, Leydig cell differentiation per UniProt By-similarity notes).
  No mouse Ch25h review exists in the repo (genes/mouse has no Ch25h folder).

### Modules
- modules/bile_acid_synthesis_ring_modification.yaml (CH25H named as source of 25-HC for CYP7B1; prose only).
- modules/srebp_signaling.yaml (25-HC as INSIG ligand; CH25H not a part).
