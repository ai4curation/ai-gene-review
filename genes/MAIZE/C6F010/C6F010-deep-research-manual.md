# C6F010 (maize ZmrbohD) manual literature research

No deep-research API was available, so this summary was compiled manually from
cached publications and PubMed searches (2026-10-28).

## Identity of the entry

- UniProtKB C6F010 (TrEMBL, PE 2), "Respiratory burst oxidase protein D variant
  alpha", 932 aa, from EMBL EU825209 / ACJ05393.1 (Lin F., Jiang M.).
- NCBI GeneID 100136880 (LOC100136880, "respiratory burst oxidase-like protein D";
  aliases rbohD, Zm00001d052653, GRMZM2G441541; other designation
  "respiratory burst oxidase4"), chromosome 4. NCBI nuccore EU825209 is titled
  "respiratory burst oxidase protein D variant alpha mRNA, complete cds,
  alternatively spliced" and EF364442 "respiratory burst oxidase protein D variant
  beta (rbohD) mRNA"; both link to GeneID 100136880 (NCBI E-utilities, queried
  2026-10-28).
- The cloning paper describes ZmrbohD as "A 2972 bp ZmrbohD transcript was also
  cloned, which had an ORF of 2799 nucleotides, encoding a protein of 932 amino
  acids with a predicted MW of 104.5 kDa" [PMID:19592501], matching C6F010
  (932 aa, 104,497 Da) and the 2972-bp EU825209 record.

## Domain architecture (UniProt C6F010 record)

- NADPH_Ox (PF08414) N-terminal regulatory region, EF-hand (PROSITE PS50222,
  252-287; EF_HAND_1 PS00018), ferric reductase transmembrane domain (PF01794),
  FAD_binding_8 (PF08022) and NAD_binding_6 (PF08030); PANTHER PTHR11972:SF197
  "RESPIRATORY BURST OXIDASE HOMOLOG PROTEIN D".
- Four PIRSR heme-iron axial histidines (461, 475, 564, 577), all His in the
  sequence (C6F010-bioinformatics/RESULTS.md).
- The cloning paper notes that the Zmrboh proteins conserve the gp91phox heme
  histidine pairs in TMD3 and TMD5 and catalytic residues Pro-415 and Asp-500
  [PMID:19592501 "Likewise, TMD3 and TMD5 contained pairs of histidine residues
  that are important for haem binding in human gp91phox"].

## Expression and signalling (maize)

- ABA induces biphasic expression of ZmrbohA-D in leaves; ZmrbohD shows the
  strongest induction [PMID:19592501 "the expression of ZmrbohD in both phase I
  and phase II induced by ABA was the highest among these Zmrbohs genes"].
  Phase II depends on H2O2 and a MAPK cascade (ZmMPK5). Plasma membrane NADPH
  oxidase activity was measured in bulk leaf plasma membranes, not attributed to
  ZmrbohD individually.
- Brassinosteroid induces ZmrbohA-D in leaves; primers for ZmrbohD were designed
  on EF364442 (variant beta of the same gene) [PMID:20693409 "BR treatment
  significantly elevated the expression of ZmrbohA–ZmrbohD in leaves of maize
  plants."]. Late induction requires apoplastic H2O2 and ZmMPK5 activity.

## Probable genetic evidence (ZmRBOH4)

- Zhong et al. 2024 [PMID:38238629] describe ZmRBOH4 as the maize RBOH "most
  closely related to AtRBOHD with 63.3% sequence identity". Its N-terminal domain
  binds and is phosphorylated by the RLCK ZmBLK1, its phosphorylation rises
  during infection, CRISPR knockouts have reduced C. zeina-induced ROS burst,
  reduced plant height and increased gray leaf spot susceptibility. No gene
  identifier is given in the cached text. C6F010 is the closest maize homologue
  of AtRBOHD in our own alignment (67.4%; RESULTS.md) and NCBI gives GeneID
  100136880 the designation "respiratory burst oxidase4", so C6F010 = ZmRBOH4 is
  probable but unconfirmed.

## Ortholog context (Arabidopsis RBOHD)

- AtrbohD/F are plasma membrane NADPH oxidases producing superoxide in the
  defence response [PMID:11756663].
- AtrbohD is activated synergistically by Ca2+ binding to its EF-hands and by
  phosphorylation [PMID:18218618].

## Gaps

- No biochemical assay of ZmrbohD protein, no localization of the maize protein,
  and no functional comparison of the alpha (932 aa) and beta splice variants.
