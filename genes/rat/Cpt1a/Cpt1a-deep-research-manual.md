# Cpt1a (rat, UniProt P32198) - manual literature synthesis

No deep-research API was available for this session; this summary was written by hand
from the cached publications in `publications/` and the UniProt record. Most cached
papers are abstract-only; full text was available for PMID:19136561, PMID:19332540,
PMID:21990363, PMID:31639005 and PMID:31748600.

## Identity
- Carnitine O-palmitoyltransferase 1, liver isoform (L-CPT1, CPT1A), 773 aa, RGD:2396,
  GeneID 25757. Member of the carnitine/choline acetyltransferase family (UniProt
  SIMILARITY; InterPro IPR000542).

## Catalytic activity
- Converts long-chain acyl-CoA plus L-carnitine to acylcarnitine plus CoA (EC 2.3.1.21,
  RHEA:12661), the first committed step of the carnitine shuttle that moves long-chain
  fatty acids into mitochondria for beta-oxidation [UniProt P32198 FUNCTION, ECO:0000269
  PubMed:16908527, 21990363, 24222496; PMID:24222496 "The enzyme carnitine
  palmitoyltransferase 1 (CPT1) catalyzes the transfer of an acyl group from acyl-CoA to
  carnitine to form acylcarnitine"].
- Catalytic residues His473 and Asp477 were assigned from a structural model based on
  carnitine acetyltransferase and confirmed by mutagenesis [PMID:14711372 "We conclude
  that the catalytic residues are His473 and Asp477, while Ser687 probably stabilizes the
  transition state."]. Glu-590 and Glu-603 are also needed for activity [PMID:12826662;
  PMID:12540837].
- Kinetics of expressed rat CPT1A: KM 46.5 uM palmitoyl-CoA, 184 uM carnitine
  (UniProt, PubMed:16908527).

## Regulation by malonyl-CoA
- Inhibited by malonyl-CoA (UniProt ACTIVITY REGULATION). Determinants: Met593
  [PMID:12499375], the N-terminal 18 residues interacting with the C-terminal domain
  [PMID:11790778], the intermembrane-space loop/TM2 boundary [PMID:16908527], and an
  N-terminal Nalpha/Nbeta structural switch responding to membrane curvature
  [PMID:21990363 "Structure-based site-directed mutageneses of native CPT1A suggest Nα to
  be inhibitory and Nβ to be noninhibitory"]. CK2 phosphorylation of Ser741/Ser747
  increases activity and changes malonyl-CoA inhibition [PMID:15247243].
- Malonyl-CoA-insensitive M593S CPT1A sustains beta-oxidation of de novo fatty acids in
  hepatocytes under high glucose/insulin [PMID:19302064].

## Location and topology
- Polytopic integral protein of the mitochondrial outer membrane, two TM segments, both
  termini cytosolic, loop in the intermembrane space [PMID:9169604 "CPT I adopts a bitopic
  topology within the mitochondrial outer membrane"; PMID:16908527]. Import uses a
  noncleavable signal (residues 123-147) downstream of TM2 [PMID:11087756].
- Not targeted to the ER; microsomal CPT activity is mitochondrial contamination
  [PMID:12401113 "It is concluded that L-CPT1 is not targeted to the ER membrane"].
- Exists as hexamer/trimer via TM2 GXXXG motifs [PMID:19136561 "The data indicate that in
  liver mitochondria in vivo CPT1A exists as a hexamer"]. Found in an outer-membrane
  complex with ACSL1 and VDAC [PMID:21622568].

## Physiology (rat perturbation studies)
- Adenoviral overexpression in rat hepatocytes and liver raises beta-oxidation and
  lowers triglyceride content and secretion [PMID:18349115].
- Overexpression in INS1E beta-cells lowers glucose-stimulated insulin secretion
  [PMID:11988095].
- Hypothalamic CPT1 knockdown/inhibition lowers food intake and hepatic glucose
  production [PMID:12754501] - systemic consequences of altered neuronal lipid
  oxidation, not a direct role in these processes.
- Many expression studies (diet, drugs, ethanol, CCl4, hypoxia) show Cpt1a mRNA/protein
  changes [e.g. PMID:33310031, PMID:31953200, PMID:31748600, PMID:19332540]; these are
  expression responses, not functions.

## Activities known only from the human ortholog
- Lysine succinyltransferase activity (ENO1) and ZDHHC4 recruitment to MAVS for type I
  IFN signalling are reported for human CPT1A (UniProt By similarity, P50416); not tested
  in rat.
