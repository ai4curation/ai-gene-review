# PA4178 (eftM, Q9HWK3) notes

## Literature

No deep-research provider was available; research done by hand. PubMed
E-utilities returned HTTP 500 on 2026-11-05, so the search was limited to the
cached publications (grep of `publications/` for EftM/PA4178).

- PA4178 is EftM, the EF-Tu-modifying enzyme. Purified enzyme trimethylates
  EF-Tu Lys5 with SAM [PMID:26677219 "An in vitro methyltransferase assay was
  employed to show that, in the presence of SAM, EftM directly trimethylates
  EF-Tu."]
- Exclusively Lys5, distributive [PMID:26677219 "EftM exclusively methylates at
  lysine 5 of EF-Tu in a distributive manner"].
- Thermolabile, which explains why the modification appears at 25 but not at
  37 degrees C [PMID:26677219 "Irreversible protein unfolding at 37 °C was
  observed"].
- G50R (clinical isolate PAHM23) abolishes SAM binding and activity.
- Trimethylated EF-Tu binds the host platelet-activating factor receptor and is
  linked to adhesion and invasion (introduction of PMID:26677219, citing earlier
  work).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000010968 | GO:0008168 methyltransferase activity | 10 | 412 (77 taxa) | GO:0008168, IDA, PMID:26677219 (PseudoCAP) | SOUND | Full text read. Purified EftM methylates EF-Tu with SAM; MS maps trimethyl-Lys5. The seed is under-specific (the paper supports GO:0016279), but a descendant is valid IBD evidence for the generic node term. | E. coli UbiE P0A887, human COQ5 Q5HYK3, yeast COQ5 S000004578, Synechocystis MPBQ MTase P74388, A. nidulans LaeA C8VQG9, Candida CAL0000191608, three Arabidopsis loci | Yes. Several seeds are well-characterised methyltransferases; generic methyltransferase activity suits a broad class I MTase node. No GO_CENTRAL defect for this node. |

Separate problem (not a PseudoCAP seed): PA4178 also receives UbiE/COQ5 IBAs
(GO:0008425, GO:0006744) from the child node PTN001297884. These are wrong for
EftM, a protein lysine methyltransferase. Both rows are REMOVE, with one
GO_CENTRAL defect (PROBABLE) recorded on the GO:0006744 row.

## Decisions

- GO:0008168 IDA: MODIFY to GO:0016279 protein-lysine N-methyltransferase activity.
- NEW GO:0018023 peptidyl-lysine trimethylation (IDA, PMID:26677219). EftM is the
  enzyme that does the step.
- GO:0003824 IEA: TOO_GENERAL.
- GO:0017000 antibiotic biosynthetic process (ARBA): REMOVE.
