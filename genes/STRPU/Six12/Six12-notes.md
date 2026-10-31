# Six1/2 (Strongylocentrotus purpuratus, UniProt H6WNA5) - curation notes

## Identity

- UniProt H6WNA5 (`H6WNA5_STRPU`, unreviewed/TrEMBL, 336 aa, SubName "Six1") is the
  mRNA deposited by the Davidson lab in Dec 2011 (EMBL JQ264781 / AEZ53927.1, RefSeq
  NP_001268684.1, GeneID 576117). Its two RX/RA lines are the unpublished-at-submission
  versions of Ransick & Davidson 2012 ("Cis-regulatory logic driving glial cells
  missing") and Materna et al. ("The regulatory origin of oral and aboral mesoderm",
  published 2013 as "Diversification of oral and aboral mesodermal regulatory states").
- Both papers state that JQ264781 is the corrected coding sequence of the GRN gene
  six1 / six1/2:
  [PMID:22509525 "An updated six1 coding sequence has been filed in GenBank [accession JQ264781]."]
  [PMID:23261933 "The actual 5’ end of the six1/2 sequence differs from the gene prediction SPU_17397 (genbank accession numbers: prox1—JQ956375 , six1/2—JQ264781, z166—JQ945922)."]
- Conclusion: H6WNA5 IS the six1/2 gene of the Davidson endomesoderm/mesoderm GRN
  (also written six1, Six1, Sp-Six1/2, SpSix1/2, gene model SPU_017379/SPU_17397).
  Confidence: high (direct accession match in two primary papers).
- Domain architecture (UniProt FT): SIX1_SD N-terminal Six domain (Pfam PF16878) plus a
  homeobox (PROSITE PS50071, residues 120-180; DNA_BIND 122-181), followed by a long
  His-rich disordered C-terminus. PANTHER PTHR10390 / PTHR10390:SF61 (labels taken
  from the UniProt record, not written from memory). Echinoderms have a single
  Six1/2 gene, co-orthologous to vertebrate SIX1 and SIX2; the Six DNA-binding
  consensus used in cis-regulatory work is GGGTATCA
  [PMID:22509525 "a Six1 consensus sequence, GGGTATCA (UniPROBE, (Newburger and Bulyk, 2009)"].
- The gene was catalogued in the genome-wide survey of S. purpuratus homeobox genes
  (Howard-Ashby et al. 2006, PMID:17055477, abstract only in cache).

## Place in the mesoderm GRN (aboral non-skeletogenic mesoderm, pigment lineage)

Six1/2 is a late-tier regulatory gene of the aboral NSM (pigment cell precursor)
regulatory state, downstream of Delta/Notch -> Gcm -> GataE, whose main documented
output is positive feedback onto gcm.

- Lineage and timing: expressed in the aboral NSM shortly after gataE and z166, with
  its cofactor eya
  [PMID:23261933 "This is soon followed by the homeobox gene six1/2 (Fig. 1A,K; in Fig. 1K,K the opposing oral quadrant is marked by prox1 expression) (Poustka et al., 2007). The six1/2 cofactor eya is also expressed in the aboral NSM (not shown)."].
  WMISH places six1 mRNA in gcm+ pigment cell precursors from mesenchyme blastula and
  in dispersed pigment cells
  [PMID:22509525 "six1 mRNA localizes to the pigment cell precursors as early as the mesenchyme blastula stage (Poustka et al., 2007) and expression is maintained in dispersed pigment cells (Figs. 7A–C)."].
  It is not expressed before late hatched blastula, i.e. after primary specification
  [PMID:22509525 "Clearly, six1, which is not significantly expressed before the late hatched blastula, is functioning at a level in the network that follows primary specification of pigment cell precursors."].
- Inputs: Delta/Notch (indirect) - six1/2 fails without D/N signalling
  [PMID:22306924 "expression of other aboral mesoderm regulatory genes, i.e., the zinc finger gene z166, the six1/2 gene, and the gene encoding its co-factor Eya, also fails in the absence of D/N signaling."];
  Gcm and GataE
  [PMID:23261933 "Fig. 6A also shows that at 24 hpf Gcm MASO significantly depresses six1/2, and the same is true of another recently discovered aboral NSM gene, z166."]
  [PMID:23261933 "Transcript levels of six1/2 and z166 are also greatly reduced in embryos bearing GataE MASO, about equally to embryos bearing Gcm MASO, so gataE is likely to provide direct inputs into these genes of the aboral GRN"]
  [PMID:22509525 "six1 is one of just two transcription factor mRNAs, the level of which is significantly depressed following knockdown of gataE transcripts (Fig. S7)."].
- Output (the key functional evidence): Six1 is a positive input into the gcm late
  cis-regulatory module.
  - Cis: the module's two critical elements are Gcm and Six1 consensus sites
    [PMID:22509525 "Cis-perturbation analyses reveal that the two critical elements within this late module are consensus matches to Gcm and Six1 binding sites."];
    deleting the GGGTAT element reduces reporter output and no compensatory Six1
    sites exist in the gcm BAC.
  - Trans: translation-blocking six1-MO
    [PMID:22509525 "injection of 250µM six1-MO resulted in an average three-fold lower peak output of endogenous gcm in real time PCR assays (Table 1)."]
    and the cis and trans results converge
    [PMID:22509525 "The similarity of outcomes from these cis- and trans-perturbations is consistent with a direct interaction of Six1 with this GGGTAT element in the late module. We conclude Six1 is an important regulator of gcm expression in the second phase that begins after PMC ingression."].
  - Network interpretation: gcm-six1 positive intergenic feedback loop stabilising the
    aboral NSM regulatory state
    [PMID:22509525 "These results support the conclusion gcm and six1 comprise a positive intergenic feedback loop in the mesodermal GRN."]
    [PMID:23261933 "This work demonstrated the institution of a feedback relation with six1/2, which serves to stabilize the aboral NSM regulatory state in addition to positive gcm auto-regulation."]
    [PMID:22238426 "A small subnetwork downstream of gcm includes the gatae gene and the six1/2 gene, which feeds back on gcm , as well as on an auto-regulatory feed from gcm onto itself"].
- Loss-of-function phenotype is mild: Six1 depletion does NOT abolish pigment cells
  [PMID:22509525 "injection of 250µM six1-MO did not produce any discernable effect on embryonic development, particularly with regard to pigment cell formation or differentiation."].
  So Six1/2 is a maintenance/stabilising input, not a specification factor; a
  pigment-cell-differentiation BP term is not justified for this gene.

## Later expression: archenteron tip, coelomic pouches and the left-right axis

- At gastrula/pluteus, six1/2 is expressed with eya, pax6, soxE and dach in the aboral
  veg2-derived cells of the archenteron tip and then the LEFT coelomic pouch
  (hydrocoel); this left-sided expression depends on BMP signalling and is excluded
  from the right side by Nodal
  [PMID:23055827 "Comparable expression patterns were observed for the left-sided markers pax6, six1/2, and genes encoding Six1/2 cofactors eya"]
  [PMID:23055827 "The expressions of all examined genes that were normally expressed in the aboral veg2 descendants, including soxE, pax6, six1/2, eya, and dach, were diminished in DM-treated embryos but remained in the single CP when BMP signaling was elevated (Figure 3F)."]
  [PMID:23055827 "the expression of nodal and the left-sided genes soxE, pax6, six1/2, and eya disappeared, which was similar to the effects induced by DM (Figure 3I,J)."]
  [PMID:23055827 "The arrowheads indicate soxE, pax6, six1/2, eya, and dach expression in the left CP in control and in both CPs in SB-505124-treated embryos."].
  Note: six1/2 is a left-sided (BMP-dependent) marker, not a right-sided Nodal
  target; Nodal inhibition makes it bilateral. Expression-only evidence; no Six1/2
  perturbation in this paper, so no left/right BP annotation is proposed.
- Co-expression mapping at the archenteron tip (S. purpuratus) places Six1/2 with SoxE,
  FoxF, Gcm, MyoR and Mef2 in the aboral-anal (AbAn) domain, not in the FoxY/FoxC
  myoblast precursors
  [PMID:24295205 "Finally, the AbAn domain expresses FoxF, Gcm, MyoR, Mef2, Six1/2 and SoxE with some of the genes occupying smaller or larger domains of expression as described before and reported in detail in Figure 5"].
- In Lytechinus variegatus (orthologue; not S. purpuratus), Six1/2 is part of a
  Pax6/Six3/Six1/2/Eya/Dach1 retinal-determination-like subcircuit in the coelomic
  pouch mesoderm that directs homing of the small micromeres; mesoderm-targeted
  Six1/2 knockdown impairs homing, and Six1/2 is upstream of six3, eya and itself
  [PMID:26402456 "Aboral transcription factor, Six1/2, affected homing when knocked down in the mesoderm, as well (n = 17, p < 0.02) and did not affect homing when knocked down in the micromere (n = 11)."]
  [PMID:26402456 "Six1/2 is seen to be upstream of six3, eya, and six1/2."]
  [PMID:26402456 "Knowing that Eya is a transcriptional co-activator of Six1/2, Eya must positively regulate itself, six3, and six1/2 by co-acting with Six1/2."].
  This is a non-cell-autonomous (regulation of migration of another cell type)
  effect in a different species; recorded here as context, not annotated.

## Annotation decisions (summary)

- GOA has only electronic rows (5 IBA from PAINT node PTN000044272, 4 IEA). All are
  consistent with a SIX-family sequence-specific transcription factor; the sea urchin
  cis/trans evidence on the gcm late module supports GO:0000978, GO:0000981,
  GO:0006357 and nucleus. GO:0003677 (DNA binding) and GO:0006355 are generalisations
  of these and are flagged MODIFY to the specific Pol II terms. GO:0005667
  (transcription regulator complex, IBA) is accepted on the Six-Eya cofactor
  relationship, which is documented by co-expression and synergy in sea urchins but
  not by a biochemical complex assay in this species.
- NEW: GO:0001228 (activator activity, IMP+IDA from gcm late-module cis/trans
  perturbation) and GO:0045944 (positive regulation of transcription by RNA pol II,
  IMP). No lineage specification / pigment differentiation BP (knockdown has no
  pigment phenotype; six1 acts after specification). No left/right or cell-migration
  BP (expression-only in S. purpuratus; migration phenotype only in L. variegatus).
