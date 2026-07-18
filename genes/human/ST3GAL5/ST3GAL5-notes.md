# ST3GAL5 (GM3 synthase) research notes

UniProt: Q9UNP4 (SIAT9_HUMAN). Gene: ST3GAL5 (HGNC:10872); synonyms SIAT9, ST3Gal V.
Taxon: Homo sapiens (NCBITaxon:9606). 418 aa, single-pass type II Golgi membrane protein.

## Identity and core function

ST3GAL5 is **GM3 synthase** = **lactosylceramide alpha-2,3-sialyltransferase**
(CMP-NeuAc:lactosylceramide alpha-2,3-sialyltransferase). It catalyzes the first
committed step of ganglioside biosynthesis: transfer of sialic acid from
CMP-N-acetylneuraminate onto the terminal galactose of lactosylceramide (LacCer)
to make GM3, the simplest ganglioside and the precursor of the a- and b-series
gangliosides.

- RecName / EC: "Lactosylceramide alpha-2,3-sialyltransferase; EC=2.4.3.9"
  [file:human/ST3GAL5/ST3GAL5-uniprot.txt "RecName: Full=Lactosylceramide alpha-2,3-sialyltransferase"]
  [file:human/ST3GAL5/ST3GAL5-uniprot.txt "AltName: Full=GM3 synthase"]
- FUNCTION: "Transfers the sialyl group (N-acetyl-alpha-neuraminyl or NeuAc) from
  CMP-NeuAc to the non-reducing terminal galactose (Gal) of glycosphingolipids
  forming gangliosides"; "Mainly involved in the biosynthesis of ganglioside GM3"
  [file:human/ST3GAL5/ST3GAL5-uniprot.txt "Mainly"]
- Catalytic activity (Rhea RHEA:18417): beta-D-Gal-(1->4)-beta-D-Glc-(1<->1)-Cer
  (= LacCer) + CMP-N-acetyl-beta-neuraminate = ganglioside GM3 + CMP + H+; EC 2.4.3.9.
- Belongs to glycosyltransferase 29 family (CAZy GT29; Pfam PF00777 Glyco_transf_29).
  [file:human/ST3GAL5/ST3GAL5-uniprot.txt "Belongs to the glycosyltransferase 29 family"]

## Enzymatic evidence (primary literature, abstract-only in cache)

- Human GM3 synthase expression cloning [PMID:9822625, abstract]: "isolation of a
  human cDNA whose protein product is responsible for the synthesis of GM3"; "The best
  acceptor substrate for the gene product was lactosylceramide, and cells transfected
  with the cloned cDNA clearly exhibited de novo synthesis of GM3, with a measurable
  decrease in the precursor lactosylceramide." Type II transmembrane topology;
  sialylmotifs L and S. Expression predominant in brain, skeletal muscle, testis.
  This is the basis of the UniProtKB IDA to GO:0047291.
- Mouse orthologue cloning [PMID:10092602, abstract]: "the alpha2,3-sialyltransferase
  (GM3 synthase)"; "Introduction of the cDNA clone into L cells resulted in the
  neo-synthesis of GM3 and high activity of alpha2,3-sialyltransferase. Among
  glycosphingolipids, only lactosylceramide showed significant activity as an acceptor,
  indicating that this gene product is a sialyltransferase specific for the synthesis of
  GM3." (This is the mouse enzyme; used by PINC as TAS source for the human entry.)
- Isoform 3 / broader acceptor use [PubMed:16934889, cited in UniProt only]: can also use
  GalCer, asialo-GM2 (GA2), asialo-GM1 (GA1) as acceptors, less preferentially than
  LacCer; makes GM4/GM2/GM1 from those precursors. N-glycosylated.

## Substrate specificity nuance

The best/physiological acceptor is LacCer -> GM3 (GO:0047291). ST3GAL5 can also sialylate
other galactose-terminating glycosphingolipids (GalCer->GM4; GA2->GM2; GA1->GM1), reported
mainly for the N-terminally extended isoform 3 [file:human/ST3GAL5/ST3GAL5-uniprot.txt
"but can also use"]. The GT29 alpha-2,3-sialyltransferase mechanism is shared with the
ST3GAL1-6 family; hence family-level terms (GO:0008373 sialyltransferase activity;
GO:0003836 beta-galactoside (CMP) alpha-2,3-sialyltransferase activity, which describes the
O-glycan Gal-1,3-GalNAc-R reaction) are correct at the family level but less precise than
the gene-specific GO:0047291 for ST3GAL5.

## Localization

Golgi apparatus membrane; single-pass type II membrane protein.
[file:human/ST3GAL5/ST3GAL5-uniprot.txt "Golgi apparatus membrane"]
[file:human/ST3GAL5/ST3GAL5-uniprot.txt "Single-"] (Single-pass type II membrane protein)
Topology: cytoplasmic 1-61, TM 62-82 (signal-anchor for type II membrane protein),
lumenal 83-418. GO:0000139 (Golgi membrane) is the appropriate CC; GO:0016020 (membrane)
is a less-informative parent (ProtInc TAS).

## Biological process / pathway

- Ganglioside biosynthetic process (GO:0001574) — first committed step producing GM3,
  the precursor of a-/b-series gangliosides. UniProt IC from GO:0047291 (PMID:9822625).
- Glycosphingolipid biosynthetic process (GO:0006688) — GM3 is a glycosphingolipid;
  ganglioside biosynthesis is a subprocess of GSL biosynthesis (Reactome TAS; PINC TAS).
- PATHWAY: "Glycolipid biosynthesis" [file:human/ST3GAL5/ST3GAL5-uniprot.txt "Glycolipid biosynthesis"].
- GO:0009101 (glycoprotein biosynthetic process) — IBA/InterPro/IEA. This is a
  family-level over-annotation: ST3GAL5's physiological substrates are glycosphingolipids
  (LacCer), NOT glycoproteins. The GT29 family includes protein sialyltransferases, so the
  phylogenetic/domain inference pulls in a glycoprotein term that does not fit this
  gene's demonstrated LacCer->GM3 lipid function.

## Disease

Salt and pepper developmental regression syndrome (SPDRS; MIM:609056), a.k.a. GM3
synthase deficiency / ST3GAL5-CDG / Amish infantile epilepsy syndrome. Autosomal
recessive; infantile-onset severe refractory seizures, failure to thrive, psychomotor
delay/developmental stagnation, cortical blindness, sometimes deafness, and patchy
skin hypo-/hyperpigmentation. Caused by loss-of-function ST3GAL5 variants.
[file:human/ST3GAL5/ST3GAL5-uniprot.txt "Salt and pepper developmental regression syndrome"]
[PMID:15502825] Simpson et al. Nat Genet 2004: "Infantile-onset symptomatic epilepsy
syndrome caused by a homozygous loss-of-function mutation of GM3 synthase."

## Annotation review decisions (summary)

- GO:0047291 lactosylceramide alpha-2,3-sialyltransferase activity (IDA, PMID:9822625):
  ACCEPT — core MF, gene-specific, experimentally demonstrated.
- GO:0047291 (IBA, GO_REF:0000033): ACCEPT — corroborates core MF.
- GO:0001574 ganglioside biosynthetic process (IC from GO:0047291, PMID:9822625):
  ACCEPT — core BP.
- GO:0000139 Golgi membrane (IEA SubCell; and 2x Reactome TAS): ACCEPT — correct location.
- GO:0008373 sialyltransferase activity (IEA; TAS PMID:10092602): family-parent of the
  specific MF -> MODIFY to GO:0047291.
- GO:0003836 beta-galactoside (CMP) alpha-2,3-sialyltransferase activity (2x Reactome TAS):
  describes the ST3GAL family O-glycan reaction, not the LacCer->GM3 reaction ->
  MODIFY to GO:0047291.
- GO:0006688 glycosphingolipid biosynthetic process (Reactome TAS; PINC TAS): correct,
  broader parent of ganglioside biosynthesis -> KEEP_AS_NON_CORE.
- GO:0016020 membrane (ProtInc TAS): uninformative parent of Golgi membrane -> MODIFY to
  GO:0000139.
- GO:0009101 glycoprotein biosynthetic process (IBA; InterPro IEA): over-annotation from
  family/domain inference; substrates are glycosphingolipids not glycoproteins ->
  IBA MARK_AS_OVER_ANNOTATED; InterPro IEA REMOVE.
</content>
</invoke>
