# MAT1A (Q00266) review notes

Note: falcon deep research was OUT OF CREDITS (HTTP 402) at review time, so there is no
`-deep-research-falcon.md`. This review is grounded in the UniProt record
(`MAT1A-uniprot.txt`), the seeded GOA (`MAT1A-goa.tsv`), and cached `publications/PMID_*.md`.

## Gene identity
- UniProtKB Q00266, METK1_HUMAN, "S-adenosylmethionine synthase isoform type-1" / AdoMet
  synthase 1 / Methionine adenosyltransferase 1 / MAT-I/III.
- HGNC:6903, GeneID 4143, chromosome 10. EC 2.5.1.6.
- 395 aa. Belongs to the AdoMet synthase (MAT) family.

## Core function
- Catalyzes SAM (AdoMet) synthesis from L-methionine + ATP.
  UniProt CATALYTIC ACTIVITY: "L-methionine + ATP + H2O = S-adenosyl-L-methionine + phosphate
  + diphosphate" (Rhea:RHEA:21080; EC 2.5.1.6; ECO:0000269|PubMed:10677294).
- Unusual two-step reaction, both steps catalyzed by the same enzyme: formation of AdoMet +
  tripolyphosphate (PPPi), then hydrolysis of PPPi to PPi + Pi
  [PMID:23425511 "MAT catalyses the transfer of the adenosyl group from ATP to the sulfur atom
  of Met (L-methionine), in an unusual two-step reaction cleaving at both ends of the ATP
  triphosphate chain"].
- SAM is the principal methyl donor of the cell; committed entry to the methionine cycle
  [PMID:23425511 "MAT constitutes the first reaction step of the essential 'methionine cycle'"].
- Cofactors: 2 Mg2+ and 1 K+ per subunit (UniProt COFACTOR, by similarity to P13444).

## Isoforms / oligomerization
- MAT1A gene product = α1 catalytic subunit. Assembles into MAT I (homotetramer) and
  MAT III (homodimer) [PMID:10677294 "MAT I and MAT III are homotetramers and homodimers of
  the α1 subunit, encoded by the MAT1A gene"].
- Crystal structure of human MAT1A (PDB 2OBV) solved bound to product SAM; dimer of dimers
  [PMID:23425511; UniProt SUBUNIT "Homotetramer (MAT-I); dimer of dimers ... Homodimer (MAT-III)"].
- MAT2A (α2, ubiquitous) is the paralog; MAT II is its product; MAT2B is the regulatory
  β subunit that partners MAT2A (not MAT1A in vivo).

## Tissue / localization
- Liver-specific: "Expressed in liver" (UniProt TISSUE SPECIFICITY, ECO:0000269|PubMed:8393662);
  HPA "Tissue enriched (liver)". MAT1A is the adult-liver isoform.
- Cytosolic (GO:0005829; IBA + Reactome TAS).

## Disease
- Methionine adenosyltransferase deficiency (MATD; MIM 250850) = isolated persistent
  hypermethioninemia, without elevated homocysteine or tyrosine. Usually benign; severe
  (biallelic null) forms have hepatic SAM deficiency and CNS demyelination
  [PMID:10677294 abstract + discussion; PMID:8770875 "Demyelination of the brain is associated
  with methionine adenosyltransferase I/III deficiency"].
- PMID:10677294 characterized MATD missense variants by transient-expression enzyme assays
  (S38N abolishes activity; R264C virtually none; G336R 23%; E344A 12%; I322M 46%), directly
  supporting MF (GO:0004478 IDA) and the SAM-biosynthesis / methionine-catabolism processes (IMP).

## PTM / regulation
- S-nitrosylation of Cys120 inactivates the enzyme (UniProt PTM, by similarity to P13444).
- Formaldehyde reacts with the isoform-specific hyperreactive Cys120 of MAT1A, inhibiting
  activity and lowering SAM [PMID:37917677 "formaldehyde dose-dependent inhibition of SAM
  production through targeting S-adenosylmethionine synthase isoform type-1 (MAT1A), the
  terminal enzyme in SAM biosynthesis, at a privileged, isoform-specific Cys120"].

## Annotation-review reasoning
- GO:0004478 (MF), GO:0006556 (SAM biosynthetic process), GO:0005829 (cytosol): core; ACCEPT
  across IBA/IDA/IMP/TAS lines.
- GO:0009087 L-methionine catabolic process (IMP, PMID:10677294): methionine + ATP -> SAM
  consumes methionine, so this is defensible as the disposal route of methionine via SAM
  synthesis; KEEP (methionine metabolism), non-core relative to the SAM-synthesis framing.
- GO:0051289 protein homotetramerization (IDA, PMID:23425511) and GO:0042802 identical protein
  binding (homodimer/tetramer): supported by the crystal structure and SUBUNIT line; ACCEPT
  homotetramerization; identical protein binding is the MF shadow of the same homo-oligomer.
- GO:0048269 methionine adenosyltransferase complex (part_of): MAT I/III is a homo-oligomeric
  MAT complex; supported. ComplexPortal CPX-3168/CPX-3169 = MAT complex variant 1/3. ACCEPT.
- GO:0005515 protein binding IPIs (PMID:28514442, 32296183, 32814053, 33961781, 40205054):
  high-throughput AP-MS / Y2H interactome screens; uninformative bare "protein binding".
  Per policy: MARK_AS_OVER_ANNOTATED (do not REMOVE experimental IPIs). Note several report
  the MAT1A-MAT2A(P31153) interaction; APP/HTT interactors are from a neurodegeneration screen.
- GO:0005524 ATP binding (IEA, InterPro): true (ATP is a substrate); ACCEPT but non-core (the
  substrate binding is captured within the catalytic MF).
- GO:0051259 protein complex oligomerization (IEA/ARBA): correct but generic vs the specific
  homotetramerization IDA; MODIFY toward GO:0051289.
</content>
