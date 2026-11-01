# CDKAL1 (Q5VV42) curation notes

Reviewed together with its paralog CDK5RAP1 (Q96SZ6) as the two human radical SAM
methylthiotransferases (MTTases), within the RADICAL_SAM project.

## Sources consulted

- The Asta deep-research file (`CDKAL1-deep-research-asta.md`) is a raw retrieval and none of the
  20 retrieved papers concerns CDKAL1 (Mycobacterium annotation, proteome databases, genome
  assemblies). It was not used for any claim. Falcon deep research failed (auth 403) and was not
  re-run.
- Primary papers fetched into `publications/` for this review: PMID:20584901 (Arragain 2010, full
  text), PMID:21841312 (Wei 2011 JCI, full text), PMID:31941883 (Santos 2020, full text).
- PMID:23048041 (Brambillasca 2012) is abstract-only in the cache.

## Enzyme activity

- CDKAL1 was assigned to the e-MtaB subfamily of MTTases and shown to methylthiolate t6A:
  [PMID:20584901 "These results demonstrate that B. subtilis YqeV/MtaB and human CDKAL1/e-MtaB
  proteins are both functional in vivo and selectively involved in the conversion of t 6 A to
  ms 2 t 6 A."] The assay was heterologous complementation in a miaB-deficient E. coli strain.
- The radical SAM cluster is needed: [PMID:20584901 "This provides, as expected, strong evidence
  that the cluster is required for activity."] (CxxxCxxC triple Cys->Ala mutants of MtaB and
  e-MtaB inactive). The B. subtilis homolog binds two [4Fe-4S] clusters.
- In mammals: [PMID:21841312 "These results demonstrate that mouse Cdkal1 is a methylthiolase that
  converts t 6 A to ms 2 t 6 A in tRNA Lys (UUU)."] ms2t6A was absent from Cdkal1-/- pancreas RNA,
  and the modification is specific to tRNA-Lys(UUU) (tRNA-Lys(CUU) carries only t6A).
- UniProt records EC 2.8.4.5 / RHEA:37075 by similarity to mouse Q91WE6; cofactor: two [4Fe-4S]
  clusters, one with an exchangeable SAM (PROSITE-ProRule PRU00780).

## Location

- Tail-anchored ER membrane protein: [PMID:23048041 "We show that CDKAL1 is a novel member of the
  tail-anchored protein family and exploits the TCR40/Get3-assisted pathway for insertion of its
  C-terminal transmembrane domain into the endoplasmic reticulum."]
- Mouse: [PMID:21841312 "This hydrophobic domain was determined to carry the ER-localization signal
  because deletion of this domain disrupted ER localization (Figure 2 D)."] and endogenous Cdkal1
  in the rough ER fraction of liver.
- Reactome places the catalytic body on the cytosolic face of the ER, so tRNA modification occurs
  on cytosolic tRNA [Reactome:R-HSA-6786571 "CDKAL1 is located on the cytosolic face of the
  endoplasmic reticulum therefore the reaction is presumed to occur in the cytosol"].

## Physiology: decoding fidelity and insulin

- [PMID:21841312 "These results suggest that the 2-methylthio modification ms 2 t 6 A in tRNA Lys
  (UUU) is important for preventing the misreading of its cognate codons, especially when the rate
  of translation is relatively high."] The reporter assay was done in B. subtilis yqeV mutants.
- beta-cell KO mice: Lys misincorporation in proinsulin, less C-peptide, less first-phase GSIS,
  ER stress, glucose intolerance worsened by high-fat diet.
- Authors explicitly say CDKAL1 does not directly regulate secretion: [PMID:21841312 "Considering
  the molecular function of Cdkal1, it is not assumed that Cdkal1 directly regulates these
  functions."]
- Iron link: [PMID:31941883 "As a consequence of reduced Cdkal1 function in Irp2−/− β cells, lysine
  codons in proinsulin are misread and proinsulin processing is impaired, reducing insulin content
  and secretion."]
- CDKAL1 is not a CDK5 regulator despite the name: [PMID:21841312 "However, Cdkal1 neither
  interacted with p35 in HEK293 cells overexpressing p35 nor inhibited Cdk5 activity in vitro"].

## Participation decision on insulin / glucose-homeostasis process terms

GOA has no insulin-secretion or glucose-homeostasis rows for human CDKAL1, and none are proposed
as NEW. The entity that performs proinsulin translation is the ribosome and its tRNAs; the entity
that processes proinsulin is PCSK1/PCSK2/CPE; secretion machinery does the secretion. CDKAL1
modifies a tRNA upstream of all of these, so the knockout evidence is necessity evidence, not
participation. The authors themselves say so (quote above). Recorded as a suggested question
instead.

## Decisions summary

- Generic radical SAM rows follow the RADICAL_SAM treatment table: GO:0003824 and GO:0051536
  MODIFY, GO:0051539 ACCEPT. GO:0016740, GO:0035596 MODIFY to GO:0035598; GO:0006400 and the ND
  root MODIFY to GO:0035600.
- ER and membrane rows MODIFY to ER membrane (GO:0005789); rough ER kept as non-core.
- Three bare protein-binding IPI rows (LCK, WFS1, ATXN3; high-throughput screens) REMOVE per the
  protein-binding policy.
- GO:1990145 maintenance of translational fidelity (IBA) kept as non-core: it is the downstream
  purpose of the modification, consistent with the PAINT node and with PMID:21841312.
- GO:1904047 SAM binding added as a NEW ISS row (PMID:23542644, RimO/MTTase mechanism naming CDKAL1;
  UniProt PRU00780 exchangeable-SAM note), for consistency with LIAS and ELP3.
