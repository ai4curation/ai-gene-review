# ygiQ (Q46861) notes

No reviewer-run deep research was available (RADICAL_SAM project Phase 2). An
OpenScientist report (`ygiQ-deep-research-openscientist.md`) appeared during the review
and was read critically; see below. Everything else is from UniProt, PubMed, Europe PMC
and NCBI Gene.

## Identity and family

- 739 aa, UPF0313 family (HAMAP MF_01251; NCBIfam TIGR03904 SAM_YgiQ; PANTHER
  PTHR32331). Domains: Pfam PF08497 Radical_SAM_N (N-terminal), PF04055 Radical_SAM
  (core, residues 372-650), PF11842 DUF3362 (C-terminal); C-terminal 685-739 disordered.
- Radical SAM CxxxCxxC motif CFGGCSFC at 386-393 (checked on the UniProt sequence; UniProt
  features are ECO:0000255 sequence-model predictions)
  [file:ECOLI/ygiQ/ygiQ-uniprot.txt "Binds 1 [4Fe-4S] cluster. The cluster is coordinated
  with 3 cysteines and an exchangeable S-adenosyl-L-methionine."]. 14 Cys in total.
- UniProt has no function, no experimental evidence; protein existence by homology.
- InterPro IPR020612 "Methylthiotransferase conserved site" matches (it drives the
  GO:0051539 IEA row), but YgiQ is not an MTTase (no TRAM domain, UPF0313 family).

## Literature

- PubMed "ygiQ OR YgiQ OR UPF0313" (2026-10-19): 0 hits. NCBI Gene 948963 links only
  genome/annotation papers.
- y-ome paper: ygiQ is co-expressed (module M21) with translation genes
  [PMID:30698741 "module M21 includes the y-ome gene ygiQ whose only annotation is
  membership in the radical SAM protein superfamily"; "they are generally associated with
  protein translation"]. Co-expression only.

## OpenScientist report: critical check

The report asserts that ygiQ is rlmX, the cobalamin-dependent radical SAM
methyltransferase that methylates ribose C5'(S) of D2449 and Cm2498 of 23S rRNA under
anaerobiosis (Ishiguro et al., Mol Cell 2025/2026, PMID:41380683).

What I could verify:
- PMID:41380683 is real and its abstract says exactly that an E. coli gene named rlmX
  encodes such an enzyme [PMID:41380683 "We identified the rlmX gene, encoding a
  cobalamin-dependent radical S-adenosylmethionine (SAM) methyltransferase responsible for
  these methylations."].
- The abstract does not name ygiQ, b4469 or Q46861. Full text is paywalled (no PMC; cell.com
  and ScienceDirect 403). PubMed returns no hit for ygiQ. UniProt Q46861 (entry version
  2026-09) and NCBI Gene 948963 have not been updated to rlmX; UniProt has no rlmX gene
  name anywhere. Europe PMC text-mining of the abstract finds rlhA but no ygiQ. A 2026
  review (PMID:42517620) and a 2026 NAR paper (PMID:42598854) cite RlmX but neither gives
  its old name.
- So the ygiQ = rlmX identity is unverified. The report's specific statements that
  "Deletion of ygiQ abolishes both modifications, and they are restored by plasmid-borne
  ygiQ" and that the paper "formally renamed" ygiQ are not in any text I could access and
  appear to be extrapolations. A web search summary of the paper's full text mentioned that
  RlmX has one [4Fe-4S] cluster, which conflicts with the report's two-cluster model
  (the second "Cys453/458/464 triad" is the report's own inference; residues C453, C458 and
  C464 do exist in the sequence but nothing shows they bind a cluster).
- Plausibility by elimination: of the 20 E. coli K-12 radical SAM proteins (UniProt,
  IPR007197/IPR058240), the only ones without assigned chemistry are AslB, YdeM (anSME
  family), PflC, YbiY, YjjW (glycyl radical activase family), YhcC (now MnmL) and YgiQ.
  YgiQ is the only one whose family could plausibly be a cobalamin-dependent methylase, so
  the identity is a reasonable hypothesis, but InterPro does not report a B12-binding
  domain in YgiQ.

## Curation decisions

- Treat ygiQ = rlmX as an unverified hypothesis: no NEW rows (no rRNA methyltransferase
  MF, no rRNA modification BP, no SAM binding, no cobalamin binding) until the gene
  identity is confirmed from the primary paper.
- Generic rows per RADICAL_SAM rule (no reaction established for Q46861): GO:0003824 and
  GO:0051539 KEEP_AS_NON_CORE; GO:0051536 MODIFY to GO:0051539; GO:0005506 iron ion
  binding MODIFY to GO:0051539 (lateral, as for GO:0046872 in the rule).
- If the identity is confirmed, the review should add: rRNA (ribose C5') methyltransferase
  activity (check GO for a term; likely needs a proposed new term), cobalamin binding,
  SAM binding, 4Fe-4S core, and rRNA modification / rRNA methylation process.
