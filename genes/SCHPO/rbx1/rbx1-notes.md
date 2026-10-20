# rbx1 (pip1; SPAC23H4.18c; UniProt O13959) - curator notes

Fission yeast Rbx1/Pip1, the RING-H2 subunit of the cullin-RING ubiquitin ligases.
Not to be confused with human RBX1 (P62877), whose review is a comparator only.

## Identity

- Identified by Seibert et al. as the pombe homologue of HRT1/RBX1/ROC1 and named
  pip1 (pop interacting protein 1) [PMID:12167173 "we identified in the S. pombe genome
  database psh1 (pombe skp1 homologue) and pip1 (pop interacting protein 1), two genes
  encoding proteins with strong similarity to human SKP1 and HRT1/RBX1/ROC1,
  respectively"].
- 107 aa; RING-type zinc finger 52-97; twelve zinc ligands annotated by similarity to
  human RBX1, three zinc ions [file:SCHPO/rbx1/rbx1-uniprot.txt "The RING-type zinc
  finger domain is essential for ubiquitin ligase activity. It coordinates an additional
  third zinc ion."].
- Essential: deletion causes a particularly severe growth defect, which is why Horn et
  al. had to use a pcu4-K680R allele instead [PMID:16024659 "Due to the particularly
  severe growth defects of pip1"].

## SCF (Pcu1) ligases

- Anti-Pip1 antisera co-precipitate all five SCF(Pop1/Pop2) subunits from wild-type
  lysate, and Pip1 co-elutes with Pop1, Pop2, Pcu1 and Psh1 at ~500 kDa
  [PMID:12167173 "Pip1p, Pop1p, and Pop2p antisera co-precipitated all five proteins
  from wild-type cell lysate"; "Size fractionation of total cell lysates prior to
  immunoprecipitation revealed co-elution of Pip1p with Pop1p, Pop2p, Pcu1p, and Psh1p
  in a high molecular weight complex of approximately 500 kDa"].
- The Pip1/Pcu1/Psh1 core is constant across the cell cycle [PMID:12167173 "The
  composition of the core complex Pip1p/Pcu1p/Psh1p did not undergo major variations
  during the cell cycle"].
- Pip1-immunopurified SCF polyubiquitylates phosphorylated Rum1 with E1 + UBC3/CDC34,
  dependent on the F-box protein Pop2 [PMID:12167173 "In the presence of human E1, UBC3,
  ubiquitin, and ATP, SCFPop1p-Pop2p complexes immunopurified with Pip1p antibodies
  converted a small portion of phosphorylated Rum1p into high molecular weight species";
  "Rum1p ubiquitylation was not obtained with Pip1p complexes prepared from cell lysate
  of pop2 deletion strains, proving the F-box protein dependency of this reaction"].
- Recombinant 6His-Pcu1/6His-Rbx1 co-purify as a stoichiometric dimer from insect cells
  and, with Fbh1-Skp1, reconstitute SCF(Fbh1) that ubiquitylates Rad51 with Ubc4
  [PMID:25165823 "To obtain the SpSCFFbh1 complex, we separately purified Fbh1-Skp1 and
  Pcu1 (fission yeast Cullin1)-Rbx1 complexes, mixed them to form the SpSCFFbh1 complex,
  and used these recombinant proteins in an in vitro ubiquitination assay."; "Rad51 was
  ubiquitinated in a Ubc4- and SCFFbh1-dependent manner."]. In vivo, Rad51 is degraded in
  stationary phase in an fbh1-dependent way [PMID:25165823 "Rad51 protein was degraded
  in stationary phase in wild-type cells, but this degradation was blocked by fbh1
  mutations"]. Ubiquitinated Rad51 was not detected in vivo, so the in-cell substrate
  remains inferred.

## Pcu3

- UniProt records interaction with cul3 (Geyer et al. 2003, PMID:14527422, not cached)
  [file:SCHPO/rbx1/rbx1-uniprot.txt "Interacts with cul3."]. The deep-research report
  adds that Pip1 co-immunoprecipitates with neddylated and unneddylated Pcu3 (Zhou et
  al. 2001) [file:SCHPO/rbx1/rbx1-deep-research-falcon.md "Pip1 directly
  co-immunoprecipitates with both neddylated and unneddylated Pcu3."]. No Pcu3 substrate
  is established; no GOA row exists for a Cul3-RING complex and none is proposed.

## CLRC (Pcu4/Cul4) and heterochromatin

- Pip1 and Pcu4 were found in Rik1-TAP purifications by LC-MS/MS, and the preparation has
  E3 activity that co-elutes with Clr4 at ~700 kDa [PMID:16024659 "These results
  demonstrate that the Rik1-TAP preparations contain a functional E3 ligase, consistent
  with the identification of Pcu4 and Pip1 as Rik1-interacting proteins."; "these results
  suggest that the Rik1-TAP preparation comprises an E3 ligase complex that minimally
  consists of Rik1, Raf2, Pcu4, Pip1, and Clr4"].
- Pairwise interaction mapping confirms a CRL4-like arrangement with Pip1 as the
  RING-box protein [PMID:24449894 "Here, we present a pairwise interaction screen that
  confirms a CRL4-like subunit arrangement"; "CLRC is an active E3 ligase in vitro, and
  this activity is necessary for heterochromatin assembly in vivo."]. CLRC is recruited
  to pericentromeric heterochromatin in part by RITS [PMID:24449894 "The histone
  methyltransferase complex CLRC is essential for heterochromatin formation in S. pombe
  and is recruited to pericentromic heterochromatin, in part, by the RITS complex."].
- Purified CLRC ubiquitylates H3 preferentially at K14, and H3K14ub promotes H3K9me by
  Clr4 [PMID:31468675 "Our study revealed that the CLRC preferentially ubiquitylates
  histone H3K14 and, more importantly, that H3K14ub promotes H3K9me generation for
  heterochromatin assembly."; "H3K14ub is likely to be a prerequisite modification for
  H3K9me."]. Important caveat: rbx1 itself was never tested for silencing because it
  is essential [PMID:31468675 "All of these CLRC components except Rbx1 have been shown
  to be required for heterochromatic silencing."]. UniProt nevertheless assigns EC
  2.3.2.27 and the H3K14ub catalytic activity to rbx1 on this paper, and the production
  GO-CAM gomodel:68fac5ed00001906 places histone H3K14 ubiquitin ligase activity
  (GO:0140851) on rbx1, part_of pericentric heterochromatin formation, in pericentric
  heterochromatin - consistent with the GOA rows accepted here.
- The mating-type and subtelomeric heterochromatin rows are PomBase IC inferences from
  CLRC membership; CLRC/Rik1/Clr4 act at all three domains [PMID:16024659 "silencing of
  RNA polymerase II transcription occurs at heterochromatic loci that flank centromeric
  regions ( Allshire et al. 1994 ), within telomeres ( Nimmo et al. 1994 ) and at a
  specific interval within the mating-type locus"].
- Later work (Kim et al. 2024, Nat Commun, not cached) reports Ubc4-CLRC
  mono-ubiquitylation of Clr4 and Bdf2; those data manipulate Ubc4/Cul4/Rik1/Raf, not
  Rbx1, and are noted only in the description of CLRC outputs.

## Localisation

- GFP-Pip1: nucleus and cytoplasm [PMID:12167173 "While Pip1p, Psh1p, Pcu1p, and Pop2p
  were present in both the cytoplasm and the nucleus, surprisingly, GFP-Pop1p was largely
  restricted to the nucleus"]; ORFeome YFP screen: nucleus and cytosol (HDA)
  [PMID:16823372 "we determined the localization of 4,431 proteins"].
- Pericentric heterochromatin (NAS, ComplexPortal) is the site of the CLRC pool.
- GO:0000781 chromosome, telomeric region is a two-step inference (IC subtelomeric
  heterochromatin formation -> inter-ontology link); kept as non-core.

## Curation decisions

- All 30 GOA rows reviewed: 27 ACCEPT, 2 MODIFY, 1 KEEP_AS_NON_CORE, 0 REMOVE.
- Both GO:0005515 protein binding IPI rows (with skp1 from PMID:12167173; with cul1 from
  PMID:25165823) are MODIFY -> GO:0097602 cullin family protein binding, following the
  human RBX1 exemplar and the protein-binding policy: the informative function these
  papers establish is cullin binding to form the CRL catalytic core (the Skp1 contact is
  bridged through Pcu1).
- CLRC-pool rows (GO:0140851, GO:0031508, GO:0140727, IC rows) are accepted on the basis
  that Rbx1 is the catalytic RING of the purified complex, while noting that Rbx1 was
  not individually mutated; a contributes_to qualifier is raised as a question.
- No NEW terms proposed. Neddylation (NEDD8 transferase) is not annotated to rbx1 in
  GOA and no S. pombe paper cached here tests it directly for Rbx1; raised as a
  suggested question/experiment rather than asserted. A Cul3-RING complex term is not
  proposed because the only evidence is interaction, without a demonstrated ligase.
- The history record under history/genes/SCHPO/rbx1/ was not created in this session
  because the task scoped edits to genes/SCHPO/rbx1/ only; it should be scaffolded with
  `just new-history` when the PR is assembled.
