# NijA (Ninjurin A, CG6449; Q8MPP0) - manual literature research

No deep-research API was available for this gene; this summary was compiled by hand from
the cached publications (`publications/PMID_*.md`), the UniProt record and PubMed searches
("Drosophila ninjurin NijA" returned four records: PMID:16815999, PMID:23028562,
PMID:41448502 and its bioRxiv preprint PMID:40777432).

## Identity and structure

- NijA is one of three Drosophila ninjurins (NijA, NijB, NijC). Ninjurins are "small
  proteins of ∼16–27 kDa, with an N-terminal ectodomain and two predicted transmembrane
  domains near the C-terminal end" [PMID:23028562].
- UniProt Q8MPP0 (Swiss-Prot, 245 aa isoform B): extracellular N-terminal region 1-170,
  helical TM segments 171-191 (alpha3) and 212-232 (alpha4); helices alpha1 (135-146) and
  alpha2 (149-165) annotated by similarity to human NINJ1 (Q92982). Pfam PF04923
  Ninjurin; InterPro IPR007007; PANTHER PTHR12316:SF20. Four splice isoforms.

## Cleavage by Mmp1 and anti-adhesion signalling (Zhang et al. 2006)

- NijA was isolated as a yeast two-hybrid partner of Mmp1; binding confirmed by co-IP of
  endogenous proteins and "the endogenous proteins were found to colocalize at the
  tracheal cell surface in larvae" [PMID:16815999].
- "When NijA is expressed in S2 cells, they lose adhesion to surfaces; this adhesion-loss
  phenotype is dependent on the expression and catalytic activity of Mmp1" [PMID:16815999].
- "Our data indicate that Mmp1 releases the N-terminal extracellular domain of NijA. This
  liberated ectodomain promotes the loss of cell adhesion in a cell-nonautonomous manner."
  [PMID:16815999]
- Only the abstract is cached (PMC PDF extraction failed), so assay details behind the
  IDA/IMP/IGI cell adhesion annotations cannot be inspected here.

## Nonapoptotic cell death (Broderick et al. 2012; full text read)

- NijA protein responds to septic injury: whole-adult levels rise about two-fold; in
  larvae it is redistributed to the cell surface of fat body and hemocytes and is
  upregulated by constitutively active Toll (Tl10b) [PMID:23028562 "NijA protein is
  redistributed to the cell surface in larval immune tissues after septic injury and is
  upregulated by the Toll pathway"].
- Null allele NijA-D3: "NijAD3 homozygous mutants were viable and fertile with no obvious
  developmental abnormalities" [PMID:23028562]; no defects in survival after infection,
  antimicrobial peptide induction, melanization or phagocytosis.
- Gain of function: ubiquitous, epidermal, eye or blood-cell expression is lethal;
  hml-GAL4 expression eliminates differentiated hemocytes, which stain with acridine
  orange (a dye that "can only permeate dead cells") [PMID:23028562].
- Death is nonapoptotic: "These dying cells did not display hallmarks of apoptotic cells
  including TUNEL staining and inhibition by p35, indicating that NijA induced
  nonapoptotic cell death." [PMID:23028562]
- In S2 cells NijA kills cells (33% dead at 48 h vs about 9%); this is Mmp1-independent
  ("In contrast to our previous adhesion results, NijA-induced death does not require
  Mmp1") and the ectodomain alone does not kill ("the NijA ectodomain is not sufficient to
  trigger cell death, even though we were able to detect the tagged ectodomain in cells,
  cell lysates, and in the culture medium") [PMID:23028562].
- Killing appears cell-autonomous; an N-terminal deletion and a D140A mutant lose
  killing; "In cultured cells, NijA mutants that cannot localize to the cell surface also
  cannot induce cell death" [PMID:23028562].
- NijA is not required for apoptosis: "indicating that NijA is not an essential component
  of the cell death machinery" (actinomycin D-induced death unaffected by NijA RNAi;
  developmental embryonic head apoptosis normal in the null) [PMID:23028562].

## Family mechanism: plasma membrane rupture (Kayagaki et al. 2021)

- Mammalian NINJ1 is the effector of plasma membrane rupture (PMR) in lytic cell death:
  "Mechanistically, NINJ1 used an evolutionarily conserved extracellular domain for
  oligomerization and subsequent PMR." [PMID:33472215]. Only the abstract is cached; the
  abstract does not mention Drosophila. UniProt and GOA nonetheless cite this paper for
  NijA cytolysis (IDA), so the full text or extended data presumably include a NijA assay;
  this could not be verified here.
- The UniProt FUNCTION line for NijA: "Effector of non-apoptotic necrotic cell death that
  mediates plasma membrane rupture (cytolysis)" (ECO:0000269 PubMed:23028562,
  PubMed:33472215), with the alpha1/alpha2 membrane-insertion mechanism annotated by
  similarity to NINJ1.
- A 2025 zebrafish/mammal paper notes "the fruit fly homolog NijA is also capable of
  inducing cell death" as evidence that PMR activity is conserved [PMID:42481508].

## Glial response to nerve injury (Brashaw et al. 2026)

- NijA is transcriptionally induced in ensheathing glia after olfactory nerve
  transection, dependent on Draper but not Stat92E, AP-1 or Mmp1 [PMID:41448502 "We show
  that injury-induced transcription of NijA in responding glia requires the Draper
  receptor"].
- "In NijA mutants, glia fail to properly infiltrate areas that contain severed olfactory
  nerves, and degenerating axonal debris is not cleared from the CNS." [PMID:41448502]
- This is a loss-of-function phenotype; the molecular role of NijA in glial
  infiltration/engulfment (adhesion? membrane remodelling?) is not established.

## Open questions

- Does endogenous NijA (not overexpressed) execute plasma membrane rupture in any fly
  lytic cell death paradigm?
- Does NijA mediate homophilic adhesion like the original mammalian ninjurin assays, or
  is its adhesion role limited to the Mmp1-released anti-adhesive ectodomain?
- How does NijA act in Draper-dependent glial clearance?
