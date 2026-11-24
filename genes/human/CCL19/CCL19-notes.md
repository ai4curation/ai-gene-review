# CCL19 (C-C motif chemokine 19; ELC, MIP-3-beta) curation notes

- UniProtKB: Q99731 (98 aa; signal peptide 1-21; mature chain 22-98)
- PANTHER: PTHR12015 (SMALL INDUCIBLE CYTOKINE A) / PTHR12015:SF80 (C-C MOTIF CHEMOKINE 19)
- Pathway term: GO:0038119 CCL19-activated CCR7 signaling pathway (child of GO:0038118 C-C chemokine
  receptor CCR7 signaling pathway and GO:0038115 chemokine (C-C motif) ligand 19 signaling pathway; both
  parents carry comments asking curators to use the activated-CCR7 child).
- Campaign: LIGANDS_IN_SIGNALING ("CCL19 signaling" queue item). No deep-research provider was available;
  the literature search below was done by hand (PubMed searches on CCL19/ELC with CCR7, beta-arrestin,
  internalization, plt/plt; plus the GOA-cited papers and the mouse Ccl19 (O70460) source papers behind
  the ISS rows, found by listing O70460 annotations in QuickGO).

## Ligand and receptor

- Cloned as EBI1-ligand chemokine; binds specifically to EBI1, which the authors named CCR7
  [PMID:9153236 "ELC-SEAP was found to bind specifically to an orphan receptor EBI1"]; induces calcium flux
  and chemotaxis of CCR7-transfected cells [PMID:9153236 "ELC-Flag-induced transient calcium mobilization
  and chemotactic responses in EBI1-transfected cells"].
- Chemoattractant for T and B cells only [PMID:9498785 "showed potent chemotactic activity for T cells and
  B cells but not for granulocytes and monocytes"]; Gi-coupled [PMID:9498785 "chemotaxis was completely
  blocked by pertussis toxin"].
- Shares CCR7 with CCL21 [PMID:9507024 "SLC and ELC were essentially equivalent in terms of cross
  desensitization in calcium mobilization via CCR7"].
- Biased agonism: equal G protein activation [PMID:15054093 "Both CCL19 and CCL21 induce G protein
  activation and calcium mobilization with equal potency"], but only CCL19 desensitises CCR7 and recruits
  beta-arrestin [PMID:15054093 "only activation by CCL19, not CCL21, promotes robust desensitization of
  endogenous CCR7"]; ERK activation is beta-arrestin-dependent [PMID:15054093 "The mechanism by which CCL19
  activates ERK1/2 was determined to be beta-arrestin-dependent"]; arrestin 3 is required for CCR7
  internalization after CCL19 only [PMID:18802075 "following depletion of arrestin 3, CCR7/CCL19 failed to
  internalize"].
- Atypical receptors: ACKR4/CCX-CKR [PMID:23341447 "recruitment of β-arrestins to CCX-CKR in response to
  CCL19, CCL21, and CCL25"] (first reported as "CCR10", PMID:10706668) and CCRL2/CRAM [PMID:20002784 "CRAM
  stimulation by CCL19 did not result in typical chemokine-receptor-dependent cellular activation"].

## Expression and in vivo role

- Expressed by T-zone stromal cells together with CCL21; deleted along with Ccl21 in plt/plt mice
  [PMID:11070085 "we show in wild-type mice that ELC is expressed by T zone stromal cells that also make
  SLC"].
- Thymic medullary epithelium; attracts mature thymocytes [PMID:10861057].

## Downstream signaling in target cells (non-core readouts)

- DCs: PI3K-Akt, PLC, calcium [PMID:14592837]; Gi-MAPK module for chemotaxis and Rho/Pyk2/cofilin module for
  speed [PMID:15778365]; prosurvival PI3K-Akt1 and NF-kappaB [PMID:15059845]; Rho kinase in T-cell
  polarisation [PMID:12729902].
- Mouse DCs: maturation and Th1 programming [PMID:15845453]; dendrite extension [PMID:12200351]; endocytosis
  and Cdc42/Rac [PMID:12609829]; JNK [PMID:16027136].

## Key curation decisions

1. MF: chemokine activity (GO:0008009) is the core ligand activity (campaign decision 1). CCR7 chemokine
   receptor binding (ISS) and CCR chemokine receptor binding (IBA) are MODIFY to chemokine activity
   (campaign decision 4). Binding to the atypical receptors CCRL2 (IPI) and ACKR4 (IDA) is kept as non-core
   because it is not signaling ligand activity.
2. CCR10 chemokine receptor binding (IDA, PMID:10706668) is a legacy-name error: the receptor is ACKR4.
   MODIFY to chemokine receptor binding, with a WRONG_TERM source defect.
3. BP: GO:0038119 is accepted as the core pathway; generic cell communication and calcium homeostasis TAS
   rows are MODIFY to it. NEW lymphocyte chemotaxis (PMID:9498785). Comparator check: CXCL12 carries
   T cell chemotaxis (IDA) in QuickGO; the query returned CCL19's own GO:0002407 as a positive control.
   CCL21 has no lymphocyte chemotaxis row either, a likely gap for its review.
4. REMOVE: protein binding (MEOX2 Y2H); eosinophil chemotaxis IBA (CCL19 does not attract granulocytes);
   cellular response to virus IMP (full text: only galectin-9 was perturbed). Cellular response to
   prostaglandin E and response to nitric oxide (the DCs respond, CCL19 is the chemoattractant) are
   MARK_AS_OVER_ANNOTATED rather than removed: both papers are abstract-only here, so the attribution
   stays a PROBABLE/CHECK query (revised after PR review).
5. Mouse ISS rows describing indirect T-cell outcomes of DC maturation (T cell costimulation, T cell
   proliferation, Th1 differentiation, immunological synapse, glycoprotein biosynthesis) are
   MARK_AS_OVER_ANNOTATED; direct DC responses are kept as non-core.
6. UNDECIDED: positive regulation of non-canonical NF-kappaB (PMID:15059845): the abstract shows only
   canonical readouts and the full text was not available.

## Follow-ups (out of scope for this slice)

- CCL21 and CCR7 gene reviews; CCL21 likely needs lymphocyte chemotaxis and GO:0038120.
- PAINT: the eosinophil chemotaxis IBD (PTN008532501) reaches CCL19; check the node placement.
