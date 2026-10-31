# yudI (Q9CE84, L19272) notes

## Source of request

Reviewed from the KBase Dark Protein Atlas item
https://gene-annotate-dashboard.kbase.us/review/CP006766.1_2177
(*Lactococcus lactis*, 334 aa, eggNOG name dus). It differs from UniProt Q9CE84
(*L. lactis* subsp. *lactis* IL1403 yudI / L19272, 334 aa) at one position (query E267,
Q9CE84 G267; MG1363 A2RN88 also has E). The review is filed under the IL1403 reference
proteome as `genes/LACLA/yudI`.

Dashboard call (tier A): "DusB-like FMN-dependent tRNA-dihydrouridine synthase
catalyzing reduction of uridine residues in tRNA to dihydrouridine", with GO:0017150
tRNA dihydrouridine synthase activity, GO:0010181 FMN binding and GO:0006400 tRNA
modification. Prior annotations: eggNOG dus, Pfam PF01207, KEGG K05540 (DusB).

**Dashboard verdict: supported.** The call matches the NCBIfam DusB-like (TIGR00737),
PIRSF Dus and Pfam Dus models on the query and all prior annotations. The annotator was
right not to assign a modified position from the single U20 label on a Pseudomonas
Fitness Browser homolog, and right not to turn the heterogeneous stress and carbon-source
fitness data (homologs at 36-43% identity) or the heat-stress expression literature into a
physiological role. One refinement: the process term can be sharpened from GO:0006400 to
GO:0002943 tRNA dihydrouridine synthesis. Scored in `yudI-dashboard-predictions-review.yaml`.

## Evidence

- Family: InterPro IPR004652 DusB-like, IPR001269 Dus family, IPR018517 Dus conserved
  site; NCBIfam TIGR00737; PIRSF006621; Pfam PF01207; PANTHER PTHR45846 (UniProt Q9CE84).
- Catalytic Cys conserved: E. coli DusB C100 -> Q9CE84 C111 (NMGCPVPKV), and every
  E. coli DusB FMN-binding residue is conserved (`yudI-bioinformatics/RESULTS.md`).
- Identity: E. coli DusB 36.4%, DusA 29.0%, DusC 29.5%; B. subtilis Dus1 (BSU00810)
  57.4%, Dus2 (BSU08030) 28.0%; M. capricolum DusB 43.8%. M. capricolum DusB is also
  closer to B. subtilis Dus1 than to Dus2, so YudI most likely sits in the Firmicute DusB1
  subgroup (inferred from pairwise identity, no tree).
- Only one Dus in IL1403 (Q9CE84) and in MG1363 (A2RN88) by Pfam/InterPro search of the
  UniProt reference proteomes.
- In E. coli, DusB makes D17 only [PMID:29294097 "DusC and DusB are mono-site specific
  flavoenzymes involved in D16 and D17 biosynthesis, respectively, while DusA is a U20/U20a
  bi-site specific enzyme"].
- The single DusB of the Mollicute M. capricolum is multisite [PMID:33685366 "DusBMCap
  modifies U17 to D17 but also synthetizes D20/D20a combining therefore both E. coli DusA
  and DusB activities."], and Firmicutes carry DusB1 and DusB2 subgroups [PMID:33685366
  "Mollicutes have retained DusB1 and lost DusB2"].
- B. subtilis has D17, D20, D20a and D47 but only two Dus, with unknown site assignment
  [PMID:32629984 "it is not possible to predict which position each enzyme modifies"].
- Dus cofactor is FMN [PMID:22123979 "Dihydrouridine synthase (Dus) catalyzes the D
  formation of tRNA through reduction of uracil base with flavin mononucleotide (FMN) as a
  cofactor."], so the GOA FAD-binding row (InterPro2GO) is removed and FMN binding added.
- Stress links are indirect: KF147 LLKF_2139 (yudI) expression correlates positively with
  heat-stress robustness [PMID:27973578, table row "LLKF_2139yudItRNA-dihydrouridine
  synthasepositive8.4"]; an L. paracasei transposon mutant in LSEI_2533 was a heat-stress
  hit [PMID:29662477].

## Process notes

- `just deep-research-falcon LACLA yudI --fallback perplexity-lite` failed (both providers
  timed out or errored); the literature review was done manually from PubMed.
- `just fetch-fitness LACLA yudI`: no Fitness Browser organism for L. lactis.
- Faivre et al. 2021 full text was not available (abstract only), so the mapping of
  B. subtilis Dus1/Dus2 onto DusB1/DusB2 is inferred here from identity to M. capricolum
  DusB, not taken from the paper.
