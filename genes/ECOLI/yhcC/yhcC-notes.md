# yhcC (P0ADW6) notes

Deep research was unavailable for this gene (no deep-research provider run; RADICAL_SAM
project Phase 2). Built from cached primary literature (including a 2026 preprint found by
PubMed search), UniProt and a local motif check.

## Identity

- 309 aa radical SAM protein, Elp3/MiaB/NifB-like clan (Pfam PF04055 + PF16199
  Radical_SAM_C; InterPro IPR005911 YhcC-like; NCBIfam TIGR01212). PANTHER
  PTHR11135:SF1 "PROTEIN YHCC".
- The cluster-binding motif is **not** a clean CxxxCxxC: UniProt places the [4Fe-4S]
  ligands at C33, C45 and C48 (ECO:0000250 from Q9X0Z6), and a regex scan of the sequence
  finds no CxxxCxxC; the spacing is C33-x11-C45-x2-C48. Checked locally on the UniProt
  sequence.
- UniProt FUNCTION: [file:ECOLI/yhcC/yhcC-uniprot.txt "In vitro, can cleave
  S-adenosyl-L-methionine into methionine"] and COFACTOR "Binds 1 [4Fe-4S] cluster",
  both ECO:0000269|PubMed:25117543.

## Function: YhcC is the anaerobic MnmL of E. coli

Boswinkle et al. 2026 (bioRxiv preprint, full text cached) assign the function
[PMID:42239373]:

- In vivo: "we find YhcC is necessary for cmnm5s2U demodification in vivo under anaerobic
  growth"; ΔyhcC grown anoxically accumulates cmnm5s2U and makes no mnm5s2U even though
  mnmC is present ["Additionally, cmnm5s2U accumulated in tRNAs extracted from the ΔyhcC
  mutant grown under anoxic conditions despite the presence of mnmC."]; complementation
  restores mnm5s2U, and a C33A cluster-ligand variant does not ["showing that the
  conversion of cmnn5s2U to nm5s2U relies on YhcC catalysis"]. Under aerobic growth ΔyhcC
  has no phenotype, because MnmC1 needs O2.
- In vitro: purified, [4Fe-4S]-reconstituted YhcC binds tRNA ["found that YhcC binds tRNA
  with a KD of approximately 5 μM"] and converts cmnm5s2U to nm5s2U ["providing direct in
  vitro evidence that YhcC catalyzes the cmnm5s2U to nm5s2U reaction on tRNA"], SAM
  dependently.
- Earlier: [PMID:25117543] validated YhcC as a genuine iron-sulfur protein; the preprint
  restates it ["YhcC has also been confirmed to bind a [4Fe-4S] cluster and is capable of
  cleaving SAM to methionine and 5'-deoxyadenosine in the presence of a chemical
  reductant"].
- Regulation: FNR-activated anaerobically; gene neighbour arcB.
- The authors propose renaming the gene ["yhcC should be renamed to mnmL in E. coli and in
  related facultative anaerobes"]. Review keeps the symbol yhcC (current UniProt/GOA
  nomenclature).
- Family context: MnmL was identified in B. subtilis and S. mutans as the YtqA-subgroup
  rSAM enzyme needed for mnm5s2U [PMID:38551342 "a member of the YtqA subgroup of the
  radical Sam superfamily was found to be involved in the synthesis of mnm5s2U in both
  Bacillus subtilis and Streptococcus mutans. This protein, renamed MnmL"].
- Independently cited in a 2026 review [PMID:42517620: "under anaerobiosis, this reaction
  is catalyzed by YhcC, a radical SAM-dependent enzyme that is orthologous to MnmL"].

Caveat: the primary source is a preprint. Evidence is genetic plus in vitro with purified
protein, and it is corroborated by the peer-reviewed B. subtilis MnmL work and by the
review above, so the assignment is treated as established here.

## Ontology gap

No GO MF term exists for the cmnm5s2U -> nm5s2U demodification. Checked QuickGO and OLS
(2026-10-19) for "carboxymethylaminomethyl", "5-aminomethyl-2-thiouridine", "cmnm5",
"methylaminomethyl": the only MF hits are GO:0004808 (the MnmC2 methyltransferase step) and
GO:0141102 (an unrelated 2'-O-ribose methyltransferase). E. coli MnmC (P77182), which
performs the same demodification aerobically, carries only GO:0016645 oxidoreductase
activity, acting on the CH-NH group of donors for its MnmC1 domain. Rhea has the oxidative
version of the reaction (RHEA:72279, with a generic acceptor A) but not a SAM-dependent
one. Proposed a new MF term; BP is covered by GO:0002098 tRNA wobble uridine modification.

## Curation decisions

- GO:0003824 MODIFY to the proposed new term (reaction now known).
- GO:0051536 MODIFY to GO:0051539; GO:0051539 (IDA) ACCEPT and core: catalysis is
  established, so the cluster is the catalytic cofactor.
- NEW: GO:0000049 tRNA binding (IDA, EMSA), GO:1904047 SAM binding (IC, per the project
  convention for members with established catalysis), GO:0002098 tRNA wobble uridine
  modification (IMP; YhcC catalyses a step itself, so participation is satisfied).
- No cytoplasm row added: localization was not determined, only inferred.
