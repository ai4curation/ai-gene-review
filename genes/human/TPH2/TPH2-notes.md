# TPH2 (human) — review notes

UniProt: Q8IWU9 (TPH2_HUMAN), 490 aa. HGNC:20692. Gene on chromosome 12.
Source files read: `TPH2-uniprot.txt`, `TPH2-goa.tsv`, `publications/PMID_37608910.md`,
`reactome/R-HSA-209828.md`.

## Identity and catalytic function

- TPH2 is **Tryptophan 5-hydroxylase 2** (Neuronal tryptophan hydroxylase; Tryptophan
  5-monooxygenase 2), EC 1.14.16.4
  [file:human/TPH2/TPH2-uniprot.txt "RecName: Full=Tryptophan 5-hydroxylase 2;"] and
  [file:human/TPH2/TPH2-uniprot.txt "AltName: Full=Neuronal tryptophan hydroxylase;"].
- It is the neuronal paralog of TPH1 and catalyzes the **rate-limiting step of serotonin
  (5-HT) biosynthesis**: BH4/Fe(II)/O2-dependent hydroxylation of L-tryptophan to
  5-hydroxy-L-tryptophan (5-HTP)
  [file:human/TPH2/TPH2-uniprot.txt
   "Reaction=(6R)-L-erythro-5,6,7,8-tetrahydrobiopterin + L-tryptophan + O2"];
  product line [file:human/TPH2/TPH2-uniprot.txt
   "= 5-hydroxy-L-tryptophan + (4aS,6R)-4a-hydroxy-L-erythro-5,6,7,8-"].
- Reactome confirms the rate-limiting nature and cofactor requirement
  [Reactome:R-HSA-209828 "The first and rate limiting step in serotonin (5-HT) biosynthesis is catalyzed"];
  [Reactome:R-HSA-209828 "the hydroxylation of L-tryptophan to 5-hydroxytryptophan"].
- Pathway placement: serotonin biosynthesis, step 1 of 2 (5-HTP is subsequently
  decarboxylated by DDC to serotonin)
  [file:human/TPH2/TPH2-uniprot.txt "PATHWAY: Aromatic compound metabolism; serotonin biosynthesis;"];
  [file:human/TPH2/TPH2-uniprot.txt "serotonin from L-tryptophan: step 1/2."].

## Cofactor / metal

- Cofactor is ferrous iron, Fe(2+)
  [file:human/TPH2/TPH2-uniprot.txt "Name=Fe(2+); Xref=ChEBI:CHEBI:29033; Evidence={ECO:0000250};"].
- Three iron-coordinating residues (BINDING His318, His323, Glu363; "Fe cation")
  [file:human/TPH2/TPH2-uniprot.txt 'ligand="Fe cation"']. Supports the InterPro
  iron-ion-binding annotation (GO:0005506).
- Member of the biopterin-dependent aromatic amino acid hydroxylase family (with PAH, TH)
  [file:human/TPH2/TPH2-uniprot.txt "Belongs to the biopterin-dependent aromatic amino acid"]
  [file:human/TPH2/TPH2-uniprot.txt "hydroxylase family."].

## Structure / domains

- ACT regulatory domain (65-140); central catalytic domain; C-terminal tetramerization
  (leucine-zipper) motif. hTPH2 domain layout per Carkaci-Salli et al.: N-terminal
  regulatory domain (1-150), catalytic domain (~151-465), tetramerization (466-490)
  [PMID:37608910 "TPH2 belongs to a superfamily of aromatic amino acid hydroxylases"].
- These enzymes are iron- and BH4-dependent monooxygenases with a common catalytic
  mechanism [PMID:37608910
   "These enzymes are iron- and tetrahydrobiopterin (BH4)-dependent monooxygenases with a common catalytic mechanism"].
- Interacts with the co-chaperone DNAJC12 (by similarity)
  [file:human/TPH2/TPH2-uniprot.txt "SUBUNIT: Interacts with DNAJC12."].

## Expression / localization

- Brain specific [file:human/TPH2/TPH2-uniprot.txt "TISSUE SPECIFICITY: Brain specific."];
  responsible for CNS serotonin synthesis throughout life
  [PMID:37608910 "responsible for 5-HT synthesis in the brain throughout life"], expressed
  in serotonergic neurons of the brainstem raphe nuclei; also present in enteric neurons of
  the gut [PMID:37608910 "TPH2 is also found within nerve terminals in the small intestine"].
- Subcellular location: cytosolic (soluble tetramer). Reactome annotates the hydroxylation
  reaction/enzyme to cytosol (GO:0005829, TAS). Also annotated is_active_in neuron
  projection (GO:0043005) by phylogeny (IBA) — consistent with 5-HT synthesis at nerve
  terminals.

## Disease / variants (context; not GO annotations)

- rs2887147 A328V/E: A328E has no measurable activity; A328V has reduced Vmax, substrate
  inhibition and reduced stability — this is the IDA source (PMID:37608910) supporting the
  catalytic activity annotation (WT enzyme was assayed as the reference)
  [PMID:37608910 "A328E had no measurable enzyme activity"];
  [PMID:37608910 "the A328V variant had reduced activity"];
  [PMID:37608910 "The recombinant full-length enzyme"].
- Loss-of-function variants (R441H, R303W, P206S) are linked to major depressive disorder,
  ADHD7 and bipolar disorder susceptibility (UniProt DISEASE/VARIANT records); consistent
  with TPH2's role as the rate-limiting CNS serotonin-synthesis enzyme.

## Annotation review summary

Core: MF tryptophan 5-monooxygenase activity (GO:0004510, IDA+IBA); iron ion binding
(GO:0005506, IEA/InterPro); BP serotonin biosynthetic process (GO:0042427); location
cytosol (GO:0005829) / neuron projection (GO:0043005).

IEA parent/family terms treated as non-core-but-correct generalizations:
GO:0004497 monooxygenase activity, GO:0016714 (pterin-dependent oxidoreductase parent),
GO:0009072 aromatic amino acid metabolic process — all correct-but-general ancestors of
the specific TPH2 function; kept (KEEP_AS_NON_CORE) rather than removed, since they are true
generalizations of the enzyme's real activity, not wrong.
