# LIAS (O43766) notes

Part of the RADICAL_SAM project (projects/RADICAL_SAM.md), Phase 1 human.

## Literature sources

The falcon deep-research run failed (authentication 403), so the only deep-research file is
`LIAS-deep-research-asta.md`. That is a retrieval-only Asta output and its retrieved papers are
off-topic (UniProt ID-mapping methods, proteome databases); it contributes no LIAS biology.
The notes below come from cached publications fetched with `just fetch-pmid`, the UniProt
record and the Reactome reaction.

## Identity and family

- Lipoyl synthase, mitochondrial, EC 2.8.1.8, 372 aa precursor with a predicted 1-27
  mitochondrial transit peptide. Radical SAM superfamily, lipoyl synthase family
  (HAMAP MF_00206/MF_03123, TIGR00510 lipA, PTHR10949:SF0).
  [file:human/LIAS/LIAS-uniprot.txt "Belongs to the radical SAM superfamily. Lipoyl synthase family."]
- Two [4Fe-4S] clusters: the radical SAM cluster (Cys137, Cys141, Cys144, CxxxCxxC motif)
  and an auxiliary cluster (Cys106, Cys111, Cys117, Ser352 in UniProt numbering).
  [file:human/LIAS/LIAS-uniprot.txt "Binds 2 [4Fe-4S] clusters per subunit. One cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine."]

## Catalytic activity

- Inserts two sulfur atoms at C6 and C8 of an octanoyl chain amide-linked to a lysine of a
  lipoyl domain. [file:human/LIAS/LIAS-uniprot.txt "Catalyzes the radical-mediated insertion of two sulfur atoms into the C-6 and C-8 positions of the octanoyl moiety bound to the lipoyl domains of lipoate-dependent enzymes"]
- Human LIAS (residues 28-372) purified with two [4Fe-4S] clusters catalyses about one turnover
  on an octanoyllysyl peptide on its own. Excess NFU1 drives more than 5 turnovers by restoring
  the auxiliary cluster. [PMID:36281303 "the protein catalyzes formation of no more than 1 equiv of lipoyl product"]
  [PMID:36281303 "The inclusion of an excess of NFU1 in the LIAS reaction promotes multiple turnovers and generation of more than 5 equiv of lipoyl product"]
- The auxiliary cluster is the sulfur donor and is consumed during catalysis.
  [PMID:36281303 "LSs contain an additional auxiliary [4Fe-4S] cluster from which sulfur atoms are extracted during turnover, leading to degradation of the cluster"]
- Independent human LIAS work: the two clusters have separate roles (radical generation and
  sulfur transfer). ISCU and ISCA2 [2Fe-2S] forms can reconstitute LIAS for full turnover.
  [PMID:33562493 "The enzyme contains two [4Fe-4S] centers (reducing and auxiliary clusters) that promote radical formation and sulfur transfer, respectively."]
- Cluster insertion into the radical SAM site depends on an NFU1-ISCA1 heterodimer.
  [PMID:35343688 "NFU1 and ISCA1 of the mitochondrial iron-sulfur cluster assembly machinery, via forming a heterodimeric complex, are the key factors for the insertion of a [4Fe-4S] cluster into the FeSRS site of LIAS."]
- BOLA3 has no direct effect on cluster transfer from NFU1 or GLRX5 to LIAS in vitro, and ISCA1/2
  enhance turnover only slightly. [PMID:36281303 "BOLA3, previously identified as being critical in the biosynthesis of the lipoyl cofactor in humans and Saccharomyces cerevisiae, has no direct effect on Fe-S cluster transfer from NFU1 or GLRX5 to LIAS"]
- FDX1 is the electron donor that binds LIAS directly and promotes its engagement with
  octanoyl-GCSH. [PMID:37453661 "Here we show that FDX1 directly regulates protein lipoylation by binding the lipoyl synthase (LIAS) enzyme promoting its functional binding to the lipoyl carrier protein GCSH"]

## Pathway placement in humans

- In humans, LIPT2 transfers octanoate from mitochondrial ACP to GCSH. LIAS lipoylates
  octanoyl-GCSH, and LIPT1 is thought to move the lipoyl group on to the E2 subunits of PDH,
  OGDH and BCKDH (and DLD-binding E3BP). This differs from E. coli, where LipA acts on each
  octanoylated carrier protein. [PMID:36281303 "LIPT1, a lipoyltransferase, is believed to distribute the lipoyl appendage to other LCPs"]
  [PMID:37453661 "Second, two sulfurs are added at C-6 and C-8 positions by the lipoyl synthase (LIAS) enzyme, a radical SAM enzyme (23, 24, 25) that uses SAM to initiate the synthesis of lipoic acid on GCSH."]
- Reactome models a single LIAS reaction on octanoyl-GCSH in the mitochondrial matrix.
  [Reactome:R-HSA-6793591 "Mitochondrial lipoyl synthase (LIAS) mediates the radical-mediated insertion of two sulfur atoms into the C-6 and C-8 positions of the octanoyl moiety bound to glycine cleavage system H protein (GCSH)"]
- GO process: the obsolete GO:0009107 "lipoate biosynthetic process" was replaced by GO:0009249
  protein lipoylation (QuickGO replaced_by). The obsoletion comment says term usage had been
  inconsistent. GO:0009249 has GO:0016992 lipoate synthase activity as part_of, so the MF and BP
  are linked in the ontology.

## Localization

- Mitochondrion, from the transit peptide, HAMAP and the MitoCoP high-confidence proteome
  (PMID:34800366). Mouse Lias was shown to be imported into mitochondria.
  [PMID:11389890 "We have shown that the cDNA encodes a lipoic acid synthase by its ability to complement a mutant of Escherichia coli defective in lipoic acid synthase and that mLIP1 is targeted into the mitochondria."]
- Matrix: inferred from its substrates (GCSH and the 2-oxoacid dehydrogenase E2s are matrix
  proteins) and Reactome TAS. There is no direct sub-mitochondrial fractionation for human LIAS in
  the cached papers.

## Genetics and physiology

- HGCLAS (MIM:614462): homozygous p.Arg249His causes neonatal-onset epilepsy, lactic acidosis and
  glycine elevation, with reduced PDH activity and lipoylation.
  [PMID:22152680 "We identified the homozygous mutation c.746G>A (p.Arg249His) in LIAS in an individual with neonatal-onset epilepsy, muscular hypotonia, lactic acidosis, and elevated glycine concentration in plasma and urine."]
  [PMID:22152680 "A pronounced reduction of the prosthetic group lipoamide was found in lipoylated proteins."]
- Mouse Lias-/- embryos die before E9.5. Maternal lipoate supplementation does not rescue them.
  [PMID:16135825 "Homozygous embryos lacking Lias appear healthy at the blastocyst stage, but their development is retarded globally by 7.5 days postcoitum (dpc), and all the null embryos die before 9.5 dpc."]
- Lias+/- mice are more sensitive to LPS: they show more inflammation and oxidative stress, and
  these effects are attributed to reduced endogenous lipoic acid acting as an antioxidant.
  [PMID:18845616 "Decreased Lias expression was associated with diminished hepatic LA and tissue oxidative stress."]
  This is the source (mouse IMP) of the human ISS rows for inflammatory response, response to
  oxidative stress and response to LPS. These are downstream physiological consequences of lipoate
  deficiency, not processes that LIAS carries out.
- LIAS, FDX1 and the lipoylation pathway feature in copper-ionophore-induced cell death
  (cuproptosis) screens, where lipoylated E2s are the copper target (context in PMID:37453661).
  This is not a LIAS activity.

## Review decisions (summary)

- Core MF: GO:0016992 lipoate synthase activity (IDA PMID:36281303 plus IBA/ISS/IEA). Supporting
  MFs: GO:0051539 4 iron, 4 sulfur cluster binding and GO:1904047 S-adenosyl-L-methionine binding
  (cosubstrate). GO:1904047 has no GOA row, so it is recorded only in core_functions. Under the
  CLAUDE.md MF policy I did not judge it worth a NEW row, since it is entailed by the radical SAM
  mechanism of the accepted activity.
- Core BP: GO:0009249 protein lipoylation. LIAS performs the sulfur-insertion step, so it passes
  the participation test.
- Generic rows treated per the RADICAL_SAM table: GO:0003824 -> MODIFY GO:0016992; GO:0051536 ->
  MODIFY GO:0051539; GO:0051539 ACCEPT. GO:0016783 sulfurtransferase activity is a true parent of
  GO:0016992 (QuickGO is_a chain), so it gets MODIFY -> GO:0016992.
- The obsolete GO:0009107 rows get MODIFY -> GO:0009249 (replaced_by).
- Mouse-phenotype ISS rows (inflammatory response, response to oxidative stress, response to LPS):
  MARK_AS_OVER_ANNOTATED, because they are indirect consequences of lipoate deficiency.

## Open questions

- In human cells, does LIAS act only on octanoyl-GCSH, with LIPT1 then relaying the lipoyl group to
  the E2s, or does it also lipoylate octanoyl-E2 directly?
- Which cluster carrier (NFU1 alone, NFU1-ISCA1, or ISCA2/ISCU) restores the auxiliary cluster in
  vivo, and where does BOLA3 act?
