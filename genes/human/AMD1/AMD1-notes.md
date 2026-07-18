# AMD1 (S-adenosylmethionine decarboxylase proenzyme) — review notes

UniProt: P17707 (DCAM_HUMAN). Gene symbol AMD1 (synonym AMD). HGNC:457. Human, 334 aa.

## Core identity and function

AMD1 encodes **S-adenosylmethionine decarboxylase (AdoMetDC / SAMDC)**, EC 4.1.1.50.
It is the rate-controlling enzyme that produces the **aminopropyl-group donor** for
polyamine biosynthesis. It decarboxylates S-adenosyl-L-methionine (SAM) to
S-adenosyl 3-(methylsulfanyl)propylamine (decarboxylated SAM, dcSAM), which spermidine
synthase (SRM) and spermine synthase (SMS) use to convert putrescine → spermidine →
spermine.

- Catalytic reaction (UniProt CATALYTIC ACTIVITY, Rhea:15981):
  "Reaction=S-adenosyl-L-methionine + H(+) = S-adenosyl 3-(methylsulfanyl)propylamine + CO2"
  EC=4.1.1.50 [file:human/AMD1/AMD1-uniprot.txt].
- Pathway (UniProt PATHWAY): "Amine and polyamine biosynthesis; S-adenosylmethioninamine
  biosynthesis; S-adenosylmethioninamine from S-adenosyl-L-methionine: step 1/1"
  [file:human/AMD1/AMD1-uniprot.txt]. UniPathway UPA00331 UER00451.
- FUNCTION: "Essential for biosynthesis of the polyamines spermidine and spermine.
  Promotes maintenance and self-renewal of embryonic stem cells, by maintaining spermine
  levels." [file:human/AMD1/AMD1-uniprot.txt] (ESC role is ECO:0000250 by similarity to
  UniProtKB:P0DMN7, not human experimental).

## Pyruvoyl cofactor and autocatalytic self-processing (a defining, unusual feature)

AdoMetDC belongs to the small class of **pyruvoyl-dependent** decarboxylases. It is made as
an inactive **proenzyme (zymogen)** that undergoes **autocatalytic (non-hydrolytic
serinolysis)** cleavage at the Glu67–Ser68 bond, generating a **beta chain (1–67)** and an
**alpha chain (68–334)** and converting internal **Ser-68 into an N-terminal pyruvoyl
prosthetic group** on the alpha chain.

- COFACTOR: "Name=pyruvate ... Binds 1 pyruvoyl group covalently per subunit"
  [file:human/AMD1/AMD1-uniprot.txt] (ECO:0000269|PubMed:11583147).
- Cleavage site Glu67/Ser68 and pyruvate formation at Ser-68:
  [PMID:2687270 "results indicated that the bond between glutamic acid 67 and serine 68 was
  the site of cleavage"] and [PMID:2687270 "changing serine at position 68 to alanine
  completely prevented both processing and activity"]. Ser-68 is "the residue which is
  converted to the pyruvate prosthetic group".
- Processing mechanism / ester intermediate; Ser-229 and His-243 needed for processing:
  [PMID:10574985 "Mutant S229A failed to process"] and His-243 acts as the base extracting
  the alpha-carbon hydrogen of Ser-68 [PMID:10574985 "His-243 may therefore act as the basic
  residue that extracts the hydrogen of the alpha-carbon of Ser-68"].
- Mature enzyme quaternary structure — UniProt SUBUNIT: "Heterotetramer of two alpha and
  two beta chains" [file:human/AMD1/AMD1-uniprot.txt] (ECO:0000269|PubMed:11583147). Note the
  crystallography paper describes one putrescine and an alpha/beta arrangement per monomer.

## Catalytic mechanism (Schiff base, key residues)

- The pyruvoyl group forms a Schiff base with SAM, facilitating CO2 release:
  [PMID:10029540 "The enzyme forms a Schiff base with substrate, S-adenosylmethionine,
  through the pyruvoyl moiety. This facilitates the release of CO2 from the substrate"].
- Cys-82 is the likely proton donor of the decarboxylation:
  [PMID:10029540 "it was postulated that residue Cys-82 may be the proton donor of the
  decarboxylation reaction catalyzed by S-adenosylmethionine decarboxylase"].
- Glu8, Glu11, Cys82 essential for catalysis; Glu11 also essential for putrescine
  stimulation of processing: [PMID:1917972 "Glu8, Glu11, and Cys82 are essential for
  catalytic activity, with Glu11 also being essential for the putrescine stimulation of
  AdoMet decarboxylase proenzyme processing"].
- Structural basis / substrate binding and inhibition; four-layer αββα sandwich; conserved
  Phe7, Phe223, Glu247, Leu65 position ligand; catalytic Cys82, Ser229, His243 near the
  methionyl group: [PMID:11583147 "The catalytically important residues Cys82, Ser229, and
  His243 are positioned near the methionyl group of the substrate"]. This paper is the source
  of the human AdoMetDC crystal structures and is cited for the IDA MF annotation.

## Allosteric activation by putrescine (regulation)

- Both processing and catalytic activity are stimulated by putrescine (UniProt ACTIVITY
  REGULATION: "Both proenzyme processing and catalytic activity are stimulated by putrescine.
  Catalytic activity is inhibited by iodoacetic acid." [file:human/AMD1/AMD1-uniprot.txt]).
- One putrescine binds per monomer, between the two beta-sheets but far from the active site;
  activation likely conformational/electrostatic:
  [PMID:11583147 "One molecule of putrescine per monomer is observed between the two
  beta-sheets but far away from the active site. The activating effects of putrescine may be
  due to conformational changes in the enzyme, to electrostatic effects, or both"].
- This experimentally supports the IBA "putrescine binding" (GO:0019810) function seen in
  the UniProt DR GO block (IBA:GO_Central) — though putrescine binding is regulatory, not the
  core catalytic MF.

## Localization

- Cytosol. UniProt has no membrane/organelle targeting; DR GO block lists C:cytosol
  (IBA:GO_Central) and Reactome (TAS). Consistent with a soluble cytosolic metabolic enzyme.

## Cloning / expression history

- Human and rat cDNAs cloned; 334-aa human proenzyme; proenzyme processed to ~32k and ~6k
  polypeptides generating pyruvate: [PMID:2460457 "the human proenzyme for this protein
  contains 334 amino acids"] and [PMID:2460457 "the proenzyme is converted to two
  polypeptides of molecular weights about 32,000 and 6,000 in a processing reaction which
  generates the prosthetic pyruvate group"]. This paper (and 2687270, 10029540, 10574985,
  1917972, 11583147) all directly assay/establish AdoMetDC catalytic activity — hence the
  cluster of EXP/IDA/TAS GO:0004014 annotations.

## Protein–protein interactions (high-throughput; low functional relevance)

GOA seeds three IPI "protein binding" and one "identical protein binding" annotations, all
from proteome-scale interactome screens (BioPlex / HuRI). These are NOT informative of core
function:
- PMID:28514442 (BioPlex 2.0, AP-MS) → with UniProtKB:Q96A98 (PTH2). High-throughput.
- PMID:32296183 (HuRI, Y2H binary map) → with UniProtKB:Q8WY91 (THAP4), and self
  (UniProtKB:P17707) for the identical-protein-binding call.
- PMID:33961781 (BioPlex 3.0, AP-MS) → with UniProtKB:Q96A98 (PTH2).
UniProt INTERACTION lists these same partners (PTH2 Q96A98, THAP4 Q8WY91) plus a self
interaction P17707–P17707 (consistent with the known homo-oligomeric assembly). None of these
partners implies a functional role beyond the enzyme's own oligomerization; the specific-partner
"protein binding" IPI calls carry no informative MF. GO:0042802 identical protein binding is
biologically consistent with the (α2β2) heterotetramer / self-association but is not a core
function per se.

## Curation summary (actions)

Core function is unambiguous and strongly experimentally supported for human:
- MF: adenosylmethionine decarboxylase activity (GO:0004014) — many EXP/IDA/TAS annotations → ACCEPT the experimental ones as core.
- BP: spermidine (GO:0008295) and spermine (GO:0006597) biosynthetic process; polyamine
  metabolic process (GO:0006595) — accept (IBA/TAS), non-redundant with the specific ones.
- CC: cytosol (GO:0005829) — accept.
- IEA duplicates of the same MF/BP (InterPro2GO, ARBA/UniRule) are correct but redundant with
  the experimental/IBA calls → KEEP_AS_NON_CORE (not REMOVE; they are biologically right).
- "protein binding" IPI (GO:0005515) → MARK_AS_OVER_ANNOTATED (bare protein binding, HT screens).
- identical protein binding (GO:0042802) → KEEP_AS_NON_CORE (consistent with oligomerization,
  but not the core catalytic function).
