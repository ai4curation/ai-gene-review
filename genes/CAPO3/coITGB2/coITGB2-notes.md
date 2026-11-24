# coITGB2 (Capsaspora owczarzaki integrin beta 2) - curation notes

Automated deep research was unavailable for this gene (no provider keys); these
notes are compiled manually from the cached publications, the UniProt record, the
PANTHER tree and the bioRxiv preprint of PMID:32857975.

## Identity

- UniProt A0A0D2WRB3 (CAOG_005058; RefSeq XP_004346743.1; EMBL KJE94415.1), 1056 aa,
  unreviewed, "Integrin beta".
- Identical in sequence to D7PE19, the translation of GenBank GU320673
  ("Capsaspora owczarzaki integrin beta 2 mRNA, complete cds"), deposited by
  PMID:20479219. Checked 2026-10-01: the two UniProt FASTA sequences are identical
  (diff of the sequences returned no differences) and NCBI esummary gives the
  GU320673 title above. D7PE19 cites PubMed=20479219 and EMBL GU320673/ADI46543.1.
- The paper's "integrin beta2" maps to CAOG_05058: the bioRxiv preprint of
  PMID:32857975 (DOI:10.1101/2020.02.27.967653, methods) states "β2E3-antigen was
  designed as a region in the stalk of the extracellular domain of the integrin β2
  (CAOG_05058, aminoacid region 733-835)". The cached PubMed record is abstract only,
  so this identification rests on the preprint, read 2026-10-01.
- Also named in PMID:35659869 as one of two integrin-beta genes up-regulated in coYki
  knockout cells ["two integrin-β genes (CAOG_05058 and CAOG_01283) are upregulated in
  coYki -/- cells"].

## Domain architecture and motifs

- UniProt: signal peptide 1-19, single TM helix 985-1006, cytoplasmic tail ~1007-1056;
  Pfam Integrin_beta (PF00362, x2), EGF_2 (x5), Integrin_b_cyt (PF08725); PSI; vWA-like
  beta-I domain (IPR002369).
- Sebé-Pedrós et al. 2010 [PMID:20479219 "The cation-binding motifs MIDAS, ADMIDAS, and
  LIMB, which are located in the extracellular domain ( 35 , 36 ), are well conserved in
  the different nonmetazoan integrin β, except for C. owczarzaki integrin β4"]; β1-β3
  have an expanded cysteine-rich stalk [PMID:20479219 "C. owczarzaki integrin β1, β2,
  and β3 and Amastigomonas sp. integrin β have a clear expansion of the cysteine-rich
  stalk"]; α-interacting and NPXY tail motifs conserved [PMID:20479219 "Both motifs are
  well conserved in C. owczarzaki integrin β1–β3"].
- My own regex check of the A0A0D2WRB3 sequence (UniProt REST FASTA): a DXSXS MIDAS-type
  motif at 123 (DLSGS) and two NPx[YF] motifs in the tail, NPLF at 1035 and NPLY at 1047
  (cf. the two NPxY motifs of animal integrin beta tails). Not deposited as a
  bioinformatics folder; trivial to reproduce.
- Capsaspora has four alpha subunits [PMID:20479219 "we found four integrin β and four
  integrin α genes in C. owczarzaki"]. Heterodimerisation is presumed, not shown
  [PMID:20479219 "Thus, we can assume that they too work as heterodimers and that they
  interact and function similarly to metazoan homologs. Functional analysis will be
  needed to test this hypothesis."].

## Function (Parra-Acero et al. 2020, PMID:32857975)

Abstract (cached): [PMID:32857975 "We show that integrin β2 and its associated protein
vinculin localize as distinct patches in the filopodia."]; [PMID:32857975 "We also
demonstrate that substrate adhesion and integrin localization are enhanced by mammalian
fibronectin."]; [PMID:32857975 "Finally, using a specific antibody for integrin β2, we
inhibited cell adhesion to a fibronectin-coated surface."].

Preprint details (not in cache; DOI:10.1101/2020.02.27.967653):
- Two polyclonal antibodies: anti-β2E3 (stalk, aa 733-835) and anti-β2GP1 (beta-I
  domain, aa 100-403). Only the beta-I antibody blocked adhesion to fibronectin; the
  stalk antibody did not.
- Laminin, collagen I and BSA coating reduced adhesion; the authors infer a
  Capsaspora-secreted protein coats plastic and acts as ligand.
- "Capsaspora does not have an ortholog of fibronectin, but does have proteins with
  fibronectin domains ... as well as secreted proteins with RGD sequences, which are
  candidates for endogenous ligands." So the native ligand is unknown.
- The authors call the patches putative "anchorage sites of adhesion"; they are not
  characterised as focal adhesions (no stress-fibre termini shown).
- They describe β2 as "the major integrin β subunit in Capsaspora".

## Propagation (Track C)

All nine TreeGrafter rows cite PANTHER:PTN002560695. Checked against the PANTHER
treeinfo API for PTHR10082 (2026-10-01): PTN002560695 is the PTHR10082:SF3 node
"INTEGRIN BETA-LIKE PROTEIN 1" with taxonomic range Euteleostomi; its leaves are all
vertebrate ITGBL1 orthologs (human HGNC:6164, mouse, zebrafish...). The tree root
PTN000801545 is Eumetazoa, and the reference tree contains no sponge, choanoflagellate
or Capsaspora sequence. So TreeGrafter placed the Capsaspora protein, a full integrin
beta with TM and cytoplasmic tail, on the vertebrate ITGBL1 clade (ITGBL1 is a
TM-less EGF-repeat protein; human ITGBL1 has an IEA extracellular location). The
attraction is plausibly the expanded cysteine-rich EGF stalk. Human ITGBL1 (O95965)
carries exactly the same set of IBAs (integrin binding, focal adhesion, cell-matrix
adhesion, integrin-mediated signalling, integrin complex, cell surface, cell migration,
cell adhesion mediated by integrin, cell-cell adhesion), mostly inherited from the
family root PTN000801545. The terms are therefore family-wide integrin-beta terms that
arrived via a wrong subfamily graft; whether each fits the Capsaspora protein must be
judged from Capsaspora data. The same node feeds the other Capsaspora betas
(A0A0D2U6H2, A0A0D2VIQ2, D7PE18, D7PE20) and an ichthyosporean protein (A0A0L0G967)
per projects/ORIGINS_OF_MULTICELLULARITY/propagation_audit_spread.tsv.

## Decisions summary

- Accept: plasma membrane, integrin complex (inferred; conserved alpha-interacting
  motif), cell adhesion mediated by integrin (antibody blocking).
- Non-core: membrane, cell surface, integrin binding (alpha-subunit partner untested).
- Modify: cell-matrix adhesion -> cell-substrate adhesion (native ligand unknown; no
  fibronectin ortholog per preprint).
- Over-annotated: focal adhesion (patches in filopodia, not shown to be focal
  adhesions), cell-cell adhesion (no data; aggregation adhesion untested).
- Undecided: integrin-mediated signaling pathway, cell migration (untested).
- NEW: cell adhesion mediator activity (IMP, antibody blocking, PMID:32857975 and preprint DOI:10.1101/2020.02.27.967653, now cached).
- NEW: filopodium (IDA, PMID:32857975).
