# ELOVL3 (Very long chain fatty acid elongase 3) — review notes

UniProt: Q9HB03 (ELOV3_HUMAN). Gene: ELOVL3 (synonym CIG30). 270 aa, chromosome 10.
Species: Homo sapiens (NCBITaxon:9606).

## Identity and family

- RecName "Very long chain fatty acid elongase 3"; AltNames "3-keto acyl-CoA synthase ELOVL3",
  "Very long chain 3-oxoacyl-CoA synthase 3", "Cold-inducible glycoprotein of 30 kDa" (CIG30)
  [file:human/ELOVL3/ELOVL3-uniprot.txt "RecName: Full=Very long chain fatty acid elongase 3"].
- Belongs to the ELO family, ELOVL3 subfamily
  [file:human/ELOVL3/ELOVL3-uniprot.txt "Belongs to the ELO family. ELOVL3 subfamily"].
- EC=2.3.1.199 [file:human/ELOVL3/ELOVL3-uniprot.txt "EC=2.3.1.199"].
- HAMAP-Rule MF_03203 (VLCF_elongase_3).

## Molecular function — the condensation (rate-limiting) step

ELOVL3 catalyzes the first and rate-limiting reaction of the four-step microsomal fatty-acid
elongation cycle, adding 2 carbons per cycle to long- and very-long-chain fatty acids
[file:human/ELOVL3/ELOVL3-uniprot.txt "Catalyzes the first and rate-limiting reaction of the four"].
It is a condensing enzyme acting on saturated and unsaturated acyl-CoAs, with higher activity
toward C18 acyl-CoAs, especially C18:0
[file:human/ELOVL3/ELOVL3-uniprot.txt "Condensing enzyme that exhibits activity toward"]
[file:human/ELOVL3/ELOVL3-uniprot.txt "toward C18 acyl-CoAs, especially C18:0 acyl-CoAs."].

Catalytic reaction (Rhea RHEA:32727, EC 2.3.1.199):
a very-long-chain acyl-CoA + malonyl-CoA + H+ = a very-long-chain 3-oxoacyl-CoA + CO2 + CoA
[file:human/ELOVL3/ELOVL3-uniprot.txt "chain acyl-CoA + malonyl-CoA + H(+) = a very-long-"].
The condensation product (3-oxoacyl-CoA) is then reduced (KAR/HSD17B12), dehydrated (HACD1/2)
and reduced again (TECR) to complete each two-carbon extension.

The best-matching current GO molecular-function term is **GO:0009922 fatty acid elongase activity**,
whose definition IS this reaction: "a very-long-chain acyl-CoA + H+ + malonyl-CoA = a very-long-chain
3-oxoacyl-CoA + CO2 + CoA ... first (condensation) step of the four-step fatty acid elongation cycle"
(OLS GO:0009922). So GO:0009922 is the correct, specific MF (no more-specific chain-length synthase
term exists in GO for this).

### Enzymatic evidence (EXP/IDA)
- Kitazawa et al. 2009 (PMID:19575253): Unifilter-96 GF/C assay; recombinant human ELOVL1,-2,-3,-5,-6;
  "ELOVL1, -3 and -6 preferably elongated the saturated fatty acyl-CoAs"
  [PMID:19575253 "ELOVL1, -3 and -6\npreferably elongated the saturated fatty acyl-CoAs"].
  UniProt cites this for CATALYTIC ACTIVITY (EC 2.3.1.199) and for several Rhea reactions.
- Ohno et al. 2010 (PMID:20937905): "we determined the precise substrate specificities of all the
  ELOVLs by in vitro analyses"
  [PMID:20937905 "we determined the precise substrate specificities of all the\nELOVLs by in vitro analyses"].
  Abstract foregrounds ELOVL1, but the full text characterizes every ELOVL including ELOVL3; UniProt
  cites this paper for ELOVL3 FUNCTION, CATALYTIC ACTIVITY, PATHWAY, SUBCELLULAR LOCATION, GLYCOSYLATION,
  and TISSUE SPECIFICITY. UniProt records ELOVL3 catalytic activity on C16:0, C18:0, C18:1, C18:2, C18:3,
  C20:0, C22:0 acyl-CoAs (RHEA:35315/35319/36511/36503/36523/35327/36507), i.e. saturated, mono- and
  poly-unsaturated substrates, mid-chain C16–C22 range.

## Subcellular location

Endoplasmic reticulum membrane; multi-pass membrane protein (7 predicted TM helices)
[file:human/ELOVL3/ELOVL3-uniprot.txt "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane"].
C-terminal di-lysine motif (266–270) may confer ER localization
[file:human/ELOVL3/ELOVL3-uniprot.txt "The C-terminal di-lysine motif may confer endoplasmic reticulum"].
UniProt EXP subcellular-location and ER IDA are both cited to PMID:20937905.
N-glycosylated (Asn6, Asn110) [file:human/ELOVL3/ELOVL3-uniprot.txt "N-Glycosylated."].

## Biological process

- Very-long-chain fatty acid biosynthetic process / fatty acid elongation of saturated,
  monounsaturated and polyunsaturated substrates. UniProt IDA (PMID:20937905) supports
  GO:0042761, GO:0019367, GO:0034625, GO:0034626.
- Cold-induced thermogenesis / brown adipose tissue: mouse Elovl3 mRNA is elevated >200-fold in
  cold-stressed mice; Elovl3-ablated mice cannot hyperrecruit brown adipose tissue and have an
  impaired skin barrier [PMID:16326704 "the mRNA level of the\nfatty acyl chain elongase Elovl3 is
  elevated more than 200-fold in cold-stressed\nmice"] [PMID:16326704 "they were unable to
  hyperrecruit their brown adipose\ntissue"]. Human GO:0120162 (positive regulation of cold-induced
  thermogenesis) is ISS/IEA from mouse Elovl3 (O35949) — kept as non-core (regulatory/physiological
  outcome, not the enzyme's molecular activity).
- Human ELOVL3 tissue: UniProt TISSUE SPECIFICITY says Testis (PMID:20937905)
  [file:human/ELOVL3/ELOVL3-uniprot.txt "TISSUE SPECIFICITY: Testis."]; HPA reports skin-enriched
  expression [file:human/ELOVL3/ELOVL3-uniprot.txt "HPA; ENSG00000119915; Tissue enriched (skin)."].

## Interactions

- Interacts with TECR (Q9NZ01, trans-2-enoyl-CoA reductase), the enzyme catalyzing the fourth step
  of the same elongation cycle [file:human/ELOVL3/ELOVL3-uniprot.txt "Interacts with TECR."], cited to
  PMID:38422897 (structural/biochemical study of TECR-associated VLCFA elongation). This IPI
  (GO:0005515, with UniProtKB:Q9NZ01) is functionally meaningful (elongation-complex partner) but the
  term is bare "protein binding" — informative content belongs in a complex/pathway statement, not MF.
- Second IPI (GO:0005515) from PMID:20937905 is with UniProtKB:Q96G23 = CERS2 (ceramide synthase 2).
  The Ohno paper established CERS2 regulation of ELOVL1 (not ELOVL3) in the abstract; the ELOVL3–CERS2
  pairing is a bare protein-binding IPI and is treated as over-annotation (kept, not removed, per policy).

## Reactome / TAS annotations

- Reactome pathways: Synthesis of very long-chain fatty acyl-CoAs (R-HSA-75876); LA metabolism
  (R-HSA-2046105); ALA metabolism (R-HSA-2046106); brown/beige adipocyte differentiation by EBF2
  (R-HSA-9844594) [file:human/ELOVL3/ELOVL3-uniprot.txt "Reactome; R-HSA-75876; Synthesis of very
  long-chain fatty acyl-CoAs."]. The LA/ALA-metabolism BP terms (GO:0043651, GO:0036109) are
  pathway-level TAS reflecting ELOVL3's ability to elongate C18 PUFA-CoAs; kept as non-core.
- PMID:10970790 (Leonard et al.) is a Reactome EXP source for GO:0009922 on ELOVL3, but its abstract
  describes cloning of HELO1 (=ELOVL2, elongating long-chain PUFAs, on chromosome 6), a paralog, not
  ELOVL3. The GO term (fatty acid elongase activity) is nonetheless correct for ELOVL3; flagged in
  reference_review as a likely wrong-paper attribution but the annotation itself is ACCEPTed because
  the function is right and the class of paper (elongase enzymology) is right.

## Redundancy / over-annotation summary

- GO:0009922 fatty acid elongase activity: appears 4x (IBA, IEA, 3× EXP/TAS). Core MF. Accept the
  experimental instances; keep the IBA; the redundant IEA/TAS duplicates kept but marked as such.
- GO:0016020 membrane (IEA): uninformative parent of the ER membrane location; over-annotation.
- GO:0005783 endoplasmic reticulum (IDA/IEA) and GO:0005789 ER membrane (many TAS/IEA/IBA/EXP):
  location is correct; the ER-membrane granularity is the informative one; ER (whole) and generic
  membrane are less informative parents.
- GO:0030148 sphingolipid biosynthetic process (IBA): ELOVL3 supplies VLC acyl-CoAs that can feed
  sphingolipid synthesis, but this is an ELOVL1-linked role (Ohno); for ELOVL3 it is a downstream
  pathway rather than a direct function — kept as non-core.
- GO:0030497 fatty acid elongation (ARBA IEA), GO:0035338 long-chain fatty-acyl-CoA biosynthetic
  process (IEA/TAS): correct but general; kept as non-core.
- GO:0006636 unsaturated fatty acid biosynthetic process (IEA), and PATHWAY "polyunsaturated fatty
  acid biosynthesis": ELOVL3 does elongate some unsaturated acyl-CoAs, but its higher activity is on
  saturated C18:0; kept as non-core/general.
</content>
</invoke>
