# SGPL1 (Sphingosine-1-phosphate lyase 1) review notes

UniProt: O95470 (SGPL1_HUMAN), 568 aa. HGNC:10817. Gene ID 8879. Chromosome 10q22.
EC 4.1.2.27. Belongs to the group II decarboxylase family, sphingosine-1-phosphate
lyase subfamily (PLP-dependent fold-type I; DOPA-decarboxylase-like, CDD cd06450).

## Core molecular function

SGPL1 catalyzes the final, irreversible degradative step of sphingolipid metabolism:
it cleaves phosphorylated sphingoid bases (sphingosine-1-phosphate / sphinganine
1-phosphate) into a long-chain fatty aldehyde ((2E)-hexadecenal or hexadecanal) plus
phosphoethanolamine.

- [file:human/SGPL1/SGPL1-uniprot.txt "Cleaves phosphorylated sphingoid bases (PSBs), such as sphingosine-1-phosphate, into fatty aldehydes and phosphoethanolamine."]
- [file:human/SGPL1/SGPL1-uniprot.txt "Reaction=sphinganine 1-phosphate = hexadecanal + phosphoethanolamine"] with EC=4.1.2.27, Rhea:RHEA:18593.
- [file:human/SGPL1/SGPL1-uniprot.txt "Reaction=sphing-4-enine 1-phosphate = (2E)-hexadecenal + phosphoethanolamine"] (this is the S1P substrate; sphing-4-enine 1-phosphate = sphingosine 1-phosphate).
- Cofactor: [file:human/SGPL1/SGPL1-uniprot.txt "Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326"] — PLP is bound covalently via Schiff base to Lys-353 (MOD_RES 353 "N6-(pyridoxal phosphate)lysine"). K353L mutagenesis abolishes activity (MUTAGEN 353 "K->L: Loss of sphinganine-1-phosphate aldolase activity").
- Pathway: [file:human/SGPL1/SGPL1-uniprot.txt "Lipid metabolism; sphingolipid metabolism."]
- Homodimer: [file:human/SGPL1/SGPL1-uniprot.txt "SUBUNIT: Homodimer."]

The reaction is irreversible and is the ONLY exit route from the sphingolipid
pathway, channeling sphingoid carbon into glycerolipid/ethanolamine-phosphate
metabolism [PMID:11018465 "Sphingosine-1-phosphate lyase catalyzes the last step in sphingolipid breakdown, the cleavage of phosphorylated sphingoid bases such as sphingenine-1-phosphate."]. Reactome likewise: [file:human/SGPL1/SGPL1-uniprot.txt] cross-refs R-HSA-428681 and reactome/R-HSA-428681.md states "The reaction has no reverse counterpart and, thus, irreversibly removes sphingoids from the lipid pool."

The GO MF term for this activity is **GO:0008117** — current GO label "sphinganine-1-phosphate aldolase activity" (a synonym-level naming of the S1P-lyase reaction; EC 4.1.2.27, RHEA:18593). There is no separate GO term "sphingosine-1-phosphate lyase activity" (OLS search returns none as of this review); GOA, UniProt (DR GO), and Reactome all annotate this enzyme with GO:0008117. So GO:0008117 is the correct, canonical MF term.

## Catalytic residues / structure

- Cys-218 and Cys-317 important for cleavage: [PMID:11018465 "Site-directed mutagenesis disclosed the importance of the cysteine residues 218 and 317 for the cleavage reaction."] (UniProt MUTAGEN 218 C->G loss; 317 C->S almost no activity).
- Membrane span near N-terminus not required for catalytic activity of the recombinant soluble domain: [PMID:11018465 "Hydropathy plots revealed the presence of one membrane span near the amino-terminal which is however not required for enzyme activity since recombinant poly-His-tagged lyase, lacking this membrane span, was functionally active."]
- Crystal structure (PDB 4Q6R, 8AYF): homodimeric human S1P lyase with PLP and synthetic inhibitor; active-site directed inhibitors [PMID:24809814 "as seen in the cocrystal structure of derivative 31 with the homodimeric human S1P lyase."]. Km = 5.2 uM for S1P (UniProt BIOPHYSICOCHEMICAL PROPERTIES).

## Subcellular location

ER membrane, single-pass type III membrane protein, catalytic domain on cytoplasmic
side. TOPO_DOM 1-40 lumenal, TRANSMEM 41-61, TOPO_DOM 62-568 cytoplasmic.
- [file:human/SGPL1/SGPL1-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"]
- [PMID:14570870 "The recombinant enzyme was active, localized to the endoplasmic reticulum, and reduced baseline sphingosine and sphingosine 1-phosphate levels."] (EXP/IDA for ER and ER membrane localization).

## Biological role

By irreversibly degrading S1P, SGPL1 terminates S1P signaling, sets tissue-vs-blood
S1P gradients (lymphocyte egress), and pushes the sphingolipid pathway toward exit.
It is a dual modulator of the ceramide/S1P rheostat, promoting stress-induced
ceramide accumulation and apoptosis when overexpressed:
- [PMID:14570870 "sphingosine-1-phosphate lyase overexpression in HEK293 cells decreases sphingosine and sphingosine 1-phosphate amounts but elevates stress-induced ceramide generation and apoptosis. This identifies sphingosine-1-phosphate lyase as a dual modulator of sphingosine 1-phosphate and ceramide metabolism as well as a regulator of cell fate decisions."]
- Lyase activity required to potentiate apoptosis (catalytically inactive enzyme has no effect): [PMID:14570870 "Lyase enzymatic activity was required to potentiate apoptosis, because cells expressing a catalytically inactive enzyme behaved like controls."]
- The apoptotic effect works through the S1P/ceramide balance, not through the reaction products: [PMID:14570870 "In contrast to sphingosine 1-phosphate, the products of the lyase reaction had no effect on apoptosis."]. So the GO:0097190 "apoptotic signaling pathway" (IDA) and GO:0006672 "ceramide metabolic process" (IDA) annotations reflect a downstream/indirect consequence of the catabolic activity, not a distinct molecular function.

Immunology / therapeutic target: S1P lyase inhibition reduces peripheral T-cell
numbers and protects in an MS model — S1PL as target for T-cell-targeted therapy:
- [PMID:24809814 "31 induces profound reduction of peripheral T cell numbers after oral dosage and confers pronounced protection in a rat model of multiple sclerosis."]

Cancer (S1P rheostat): SPL expression/activity lost in prostate tumors, inversely
correlated with SphK1; enforced SPL sensitizes cells to therapy:
- [PMID:22784711 "This enzyme drives irreversible degradation of sphingosine 1-phosphate (S1P)"; "a remarkable decrease in SPL enzymatic activity was found in tumor samples"].

## Disease

Biallelic loss-of-function SGPL1 variants cause an autosomal-recessive syndrome
(UniProt disease "RENI", MIM:617575; also called SPLIS / NPHS14): steroid-resistant
nephrotic syndrome, primary adrenal insufficiency, ichthyosis, immunodeficiency, and
neurological defects; some fetal hydrops/demise.
- [PMID:28165339 "In 7 families with SRNS and facultative ichthyosis, adrenal insufficiency, immunodeficiency, and neurological defects, we identified 9 different recessive mutations in SGPL1, which encodes sphingosine-1-phosphate (S1P) lyase. All mutations resulted in reduced or absent SGPL1 protein and/or enzyme activity."]
- Disease variants mislocalize / lose activity: [PMID:28165339 "Overexpression of cDNA representing SGPL1 mutations resulted in subcellular mislocalization of SGPL1."]. RENI variants R222Q and S346I show decreased protein abundance, increased aggregation, decreased activity (UniProt VARIANT records).
- Cross-species rescue confirms conserved enzymatic function: [PMID:28165339 "expression of WT human SGPL1 rescued growth of SGPL1-deficient dpl1Δ yeast strains, whereas expression of disease-associated variants did not."]
- SGPL1 IMP annotations to GO:0008117 and GO:0030149 (PMID:28165339) are supported: patient/variant loss of enzyme activity ("decreased sphinganine-1-phosphate aldolase activity") plus dpl1Δ yeast complementation directly demonstrate the lyase activity and its role in sphingolipid catabolism for the human protein.

## Protein-protein interactions (GO:0005515 IPI)

- PMID:21903422 (HI5 innate-immunity interactome): SGPL1 appears in the network as an
  interactor within the STING/innate-immunity map; the paper notes "BAT3 and SGPL1
  also regulate cell apoptosis" [PMID:21903422 "Similarly, BAT3 and SGPL1 also regulate cell apoptosis"]. IntAct records the SGPL1–STING1 (Q86WV6) binary interaction from this study. This is a large-scale interactome screen; the SGPL1 partner (STING1) is with/from UniProtKB:Q86WV6.
- PMID:32296183 (HuRI reference binary interactome): high-throughput Y2H yielding many
  binary partners for SGPL1 (AQP3/AQP9/MIP aquaporins, BCL2L2, ERG28, FA2H, IFITM3,
  MARCHF5, STX4/STX8, TMEM97, TUSC5=A5PKU2, etc.). These are systematic all-by-all
  screen hits, mostly ER/membrane proteins; individually low-information.

Bare "protein binding" (GO:0005515) IPI annotations carry no specific molecular
function; per policy they are marked as over-annotated (not removed), and not promoted
to core_functions. No single physiological adapter/complex partner is established for
SGPL1 beyond homodimerization.

## Annotation-level decisions (summary)

- GO:0008117 sphinganine-1-phosphate aldolase activity — CORE MF. Multiple IDA/EXP/IMP
  (PMID:14570870, 22784711, 28165339, 24809814) + IBA + IEA + TAS all converge. ACCEPT
  the experimental ones; IBA/TAS ACCEPT; IEA (RHEA/EC) ACCEPT as consistent.
- GO:0030170 pyridoxal phosphate binding (IEA InterPro) — CORE MF, ACCEPT. PLP is the
  essential cofactor (covalent to Lys-353); consistent with COFACTOR + MOD_RES + PDB.
- GO:0030149 sphingolipid catabolic process — CORE BP. IDA/IMP/IBA/TAS/NAS. ACCEPT.
- GO:0006665 sphingolipid metabolic process (IEA UniPathway) — parent of catabolic
  process; ACCEPT (keep, less specific but correct pathway).
- GO:0006629 lipid metabolic process (IEA ARBA) — very general grandparent; correct but
  uninformative; KEEP_AS_NON_CORE.
- GO:0016830 carbon-carbon lyase activity (IEA InterPro) — correct general MF parent of
  the aldolase/lyase activity; KEEP_AS_NON_CORE (GO:0008117 is the specific term).
- GO:0005783 endoplasmic reticulum / GO:0005789 endoplasmic reticulum membrane —
  location. ER membrane (integral) is the precise term; ER is the parent. Experimental
  (IDA/EXP/HPA) + TAS + IEA + NAS all agree. ACCEPT the membrane term as core location;
  ER (GO:0005783) ACCEPT/KEEP.
- GO:0097190 apoptotic signaling pathway (IDA PMID:14570870) — real but downstream/
  indirect consequence of altering the S1P/ceramide rheostat; KEEP_AS_NON_CORE.
- GO:0006672 ceramide metabolic process (IDA PMID:14570870) — SGPL1 does not act on
  ceramide directly; it raises ceramide indirectly by shifting the rheostat.
  KEEP_AS_NON_CORE (indirect).
- GO:0006631 fatty acid metabolic process (IDA PMID:24809814) — the lyase product is a
  long-chain fatty aldehyde (hexadecenal), which feeds fatty-acid/glycerolipid
  metabolism; a peripheral downstream role. KEEP_AS_NON_CORE.
- GO:0005515 protein binding (IPI x2, PMID:21903422, 32296183) — bare; large-scale
  screens. MARK_AS_OVER_ANNOTATED (not removed, per policy).
</content>
</invoke>
