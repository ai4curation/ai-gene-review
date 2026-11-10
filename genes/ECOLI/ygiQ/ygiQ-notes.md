# ygiQ (Q46861) notes

## Status of the identification

A first pass of this review (RADICAL_SAM project Phase 2) could not verify that ygiQ is
`rlmX`: only the abstract of Ishiguro et al. was cached, and the abstract names `rlmX`
without giving any former gene name. The review was therefore left as a dark gene with
empty `core_functions`.

The full text of that paper is now cached
(`publications/PMID_41380683.md`, `full_text_available: true`) and settles the question
outright: the screen that found the enzyme was a screen of uncharacterised
methyltransferase candidates, the gene found was `ygiQ`, and the authors rename it in the
same paragraph [PMID:41380683 "screening 15 uncharacterized MTases and 6 known RNA";
"of a plasmid-encoded ygiQ gene, indicating that ygiQ is essential"; "Hereafter, we refer
to ygiQ as rlmX."]. Figure 2A is labelled `ΔrlmX (ΔygiQ)` and the deletion strain used is
the Keio-collection `JW5501` (`E. coli ΔygiQ (Knr) (Keio collection)`), i.e. the b4469 /
Q46861 locus. The review below is rewritten on that basis; no reviewer-run deep research
was available, and the machine-generated OpenScientist report in this folder was used only
after checking it against the full text (see "OpenScientist report" below).

UniProt Q46861 and NCBI Gene 948963 still carry no `rlmX` gene name and no function, so the
gene symbol used in this repository stays `ygiQ` for now.

## Identity and architecture

- 739 aa, UPF0313 family (HAMAP MF_01251; NCBIfam TIGR03904 SAM_YgiQ; PANTHER PTHR32331).
  Pfam PF08497 Radical_SAM_N, PF04055 Radical_SAM (core, ~372-650), PF11842 DUF3362;
  C-terminal 685-739 disordered. CxxxCxxC motif `CFGGCSFC` at 386-393.
  [file:ECOLI/ygiQ/ygiQ-uniprot.txt "Binds 1 [4Fe-4S] cluster. The cluster is coordinated
  with 3 cysteines and an exchangeable S-adenosyl-L-methionine."]
- The paper's own domain assignment matches but adds the cobalamin module that InterPro
  does not recognise: a Cbl-binding domain, the radical SAM (RS) domain and the DUF3362
  domain [PMID:41380683 "as a Cbl-dependent radical SAM enzyme, which is composed"; "of a
  Cbl-binding domain, an RS domain, and a DUF3362"]. Cbl-binding, SAM-binding and
  [4Fe-4S]-binding motifs were located by comparing an AlphaFold2 model of RlmX with
  crystal structures of Cbl-dependent RS MTases [PMID:41380683 "we identified Cbl-binding
  motifs, SAM-binding motifs, and a"].
- Sequence-similarity-network analysis places RlmX homologues (UPF0313) in a different
  subgroup (Mega 10) from the previously known Cbl-dependent RS MTases OxsB, TsrM, TokK and
  Mmp10 (Mega 1), while sharing their N-terminal-Cbl / C-terminal-cluster domain order.
  Homologues are widespread in bacteria and some archaea.

## Reaction and cofactors

- RlmX installs a stereoselective methyl group at carbon 5'(S) of the **ribose** of two 23S
  rRNA residues in the peptidyl-transferase centre: dihydrouridine 2449 (giving D5Sm2449)
  and cytidine 2498 (giving Cm5Sm2498, after RlmM adds the 2'-O-methyl). This is a
  sugar-phosphate **backbone** methylation, not a 2'-O-methylation, and the authors
  describe it as unprecedented [PMID:41380683 "methylation outside the 2′ position,
  representing an unprecedented example of RNA backbone modification. We identified"].
- Mechanism (proposed, by analogy to other Cbl-dependent RS MTases): the [4Fe-4S] cluster
  reductively cleaves one SAM to the 5'-deoxyadenosyl radical, which abstracts the 5'(S)-H
  from D2449 or Cm2498; the methyl group then comes from methylcobalamin, and Cbl(I) is
  remethylated by a **second** SAM [PMID:41380683 "cleaves SAM to generate a 5′ -dAdo
  radical, which abstracts"; "a second SAM molecule to regenerate Me-Cbl (III). In our"].
  So two SAM are consumed per methyl transferred, one as radical source and one as methyl
  donor via Cbl.
- **One** [4Fe-4S] cluster. Iron quantification on reconstituted recombinant protein gave
  3.69 Fe per protein, i.e. a single cluster at ~92% occupancy [PMID:41380683 "revealed
  3.69 iron atoms bound to one recombinant protein"]. Cluster ligands are C386, C390 and
  C393; each single Cys-to-Ala substitution abolishes activity [PMID:41380683 "C390, and
  C393) in the [4Fe-4S] cluster, which resulted in"].
- Cobalamin binding was observed directly on the reconstituted protein by its 320 nm
  absorbance [PMID:41380683 "92% occupancy. We also added methylcobalamin (Me-Cbl) during
  the reconstitution of the holoenzyme. Correct binding of Cbl"], and G160N in the GG motif
  of the Cbl-binding domain abolishes methylation [PMID:41380683 "completely lost
  methylation ability (Figure 2C), highlighting the"].
- Both the cluster and Me-Cbl are needed for an active holoenzyme, and Me-Cbl is the methyl
  donor [PMID:41380683 "either the [4Fe-4S] cluster or Me-Cbl was indispensable for"; "of
  an active holoenzyme. Me-Cbl also functions as a methyl"]. Methyl viologen substitutes
  in vitro for the physiological electron donor (flavodoxin / flavodoxin reductase / NADPH
  are suggested).
- SAM dependence was shown directly, including transfer of a CD3 group from CD3-SAM
  [PMID:41380683 "in a SAM-dependent manner (Figure S7B). Moreover, deuterium-labeled SAM
  (CD3-SAM) was used as a substrate for"], and E525 contacts the SAM ribose; E525A impairs
  activity [PMID:41380683 "Regarding SAM recognition, the side chain of E525 directly
  interacts with the ribose of SAM (Figure S5E). E525A mutation"].
- In vivo the modifications require ferric iron and cobalamin in the medium
  [PMID:41380683 "induced rRNA methylations require both ferric ions and Cbl."].

### The RlmX-specific Cys cluster is NOT a second [4Fe-4S] cluster

C453, C458 and C464 form an RlmX-specific Cys cluster in the RS domain. The authors place
it on the protein **surface** and attribute it to RNA recognition through **zinc** binding,
citing earlier work; all three residues are essential for methylation
[PMID:41380683 "resides on the surface of RlmX and is thought to contribute to"; "RNA
recognition through zinc binding.52 Interestingly, all three"]. No zinc was measured here,
and the iron quantification excludes a second [4Fe-4S] cluster. The OpenScientist report's
two-cluster model is therefore wrong, and this review annotates neither a second cluster
nor zinc ion binding.

## Substrate and timing

- Holo-RlmX methylates **deproteinized** 23S rRNA but not the assembled 50S subunit
  [PMID:41380683 "any methylations in the 50S subunit (Figure 3C), but clearly"], so the
  modifications are installed early in 50S assembly on naked rRNA.
- In vitro transcribed 23S rRNA is a substrate; domain V (G2018-C2628) is the minimum
  efficient substrate, while shorter H89-93 and H89 transcripts are poor
  [PMID:41380683 "introduced into the domain V transcript (G2018-C2628), whereas"; "suggest
  that domain V is a minimum substrate for RlmX-mediated"]. RlmX thus has genuine
  structured-rRNA recognition, not just a local sequence requirement.
- Order of events: for D5Sm2449 the 5'(S)-methylation (RlmX) and dihydrouridylation (YhiN)
  occur in either order; for Cm5Sm2498 RlmX acts first, because prior 2'-O-methylation by
  RlmM blocks the 5'(S)-methylation.

## Physiology

- D5Sm2449, Cm5Sm2498 and ho5C2501 (RlhA) are all elevated under anaerobic growth. `rlmX`
  mRNA is unchanged between conditions; RlmX protein is up, and the enzyme is additionally
  more active anaerobically, plausibly because the cluster is oxygen-sensitive
  [PMID:41380683 "RlmX is activated in anaerobic conditions, probably because"].
- Single `ΔrlmX` grows normally; `ΔrlmX ΔrlhA` is clearly retarded anaerobically and is
  rescued by wild-type `rlmX` but not by the catalytically dead G160N or C390A
  [PMID:41380683 "ΔrlmX/ΔrlhA strain showed clear growth retardation under"].
- Ribosomes from the double knockout are ~half as productive in translation and transfer
  peptide at 64% of the wild-type rate [PMID:41380683 "was decreased significantly, to 64%
  that of WT ribosomes"]; 70S initiation and P-site tRNA binding are unaffected. Cryo-EM
  (PDB 8ZFG vs the double-knockout 70S) shows the modifications stabilise the P-site and
  PTC.
- `ΔrlmX` is less sensitive to erythromycin and clindamycin anaerobically, which the authors
  read as an indirect structural effect, not a resistance mechanism.

## Curation decisions

- Catalysis is now established for Q46861, so the RADICAL_SAM generic-row rule applies in
  its normal branch: GO:0003824 MODIFY to the specific activity; GO:0051536 and GO:0005506
  MODIFY to GO:0051539; GO:0051539 ACCEPT and core.
- GO has no molecular-function term for ribose C5' methylation of RNA: every ribose
  methyltransferase term in GO (searched via QuickGO: GO:0008650, GO:0070039, GO:0070677,
  GO:0030743, GO:0090486, GO:0180021 and the tRNA series) is a 2'-O-ribose term, and the
  children of GO:0008649 rRNA methyltransferase activity are all base terms
  (GO:0016433/4/5/6, GO:0070037). A `proposed_new_terms` entry is used, with GO:0008649 as
  the proposed parent (its definition already admits ribose as the acceptor), and
  `core_functions` points at it via `proposed_molecular_function`.
- NEW rows added: GO:1904047 S-adenosyl-L-methionine binding, GO:0031419 cobalamin binding,
  GO:0019843 rRNA binding, GO:0031167 rRNA methylation. All four are activities RlmX itself
  performs, so the participation test is met; GO:0031167 is the single process term used,
  with GO:0000154 rRNA modification left out as its ancestor.
- Zinc ion binding (GO:0008270) is **not** added: the paper's zinc attribution for
  C453/C458/C464 is explicitly a literature-based expectation ("is thought to"), no metal
  was measured, and the mutant phenotypes are equally consistent with a direct RNA-binding
  role. Recorded as a knowledge gap and a suggested experiment instead.
- No anaerobic-growth or translation process terms are proposed: the growth and
  peptidyl-transfer phenotypes are downstream consequences of the modified ribosome, not
  steps RlmX carries out.
