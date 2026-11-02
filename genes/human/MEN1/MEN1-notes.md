# MEN1 (menin, human, UniProt O00255) - curation notes

**Deep research status:** automated deep research (falcon / Edison) FAILED with an
authentication error on 2026-10-24, and no other provider key was usable. No
`-deep-research-*.md` file exists for this gene. The notes below come from my own
reading of the cached publications in `publications/`, the UniProt record
(`MEN1-uniprot.txt`), cached Reactome entries, and QuickGO queries (2026-10-24).

## Why this gene was reviewed

Rule FRR:0009 (projects/FUNCTION_REQUIREMENT_RULES.md) flagged menin's
"DNA-binding transcription activator activity" (GO:0001216) annotation: human GOA has
it as IEA (GO_REF:0000107, Ensembl Compara transfer from mouse O88559). Menin has no
recognized sequence-specific DNA-binding domain.

### Tracing the IEA (QuickGO, 2026-10-24)

- Human row: GO:0001216 IEA GO_REF:0000107, WITH UniProtKB:O88559 / ensembl:ENSMUSP00000058149.
- Source on mouse menin O88559: **GO:0001216 IDA PMID:14992727, assigned_by UniProt**.
  PMID:14992727 (Hughes et al. 2004) shows menin co-purifies with an MLL2/Ash2L H3K4
  methyltransferase complex, binds Ser5-phosphorylated Pol II, is ChIP-bound at Hoxc8, and
  Men1-null cells lose Hoxc6/Hoxc8 expression ["Chromatin immunoprecipitation experiments
  reveal that menin is bound to the Hoxc8 locus."; "menin activates the transcription of
  differentiation-regulating genes by covalent histone modification"]. Nothing in it shows
  sequence-specific DNA binding by menin. The activity it supports is a coactivator /
  scaffold activity, not a DNA-binding TF activity -> source defect on the UniProt mouse
  row (GO:0001216 -> GO:0003713 transcription coactivator activity).
- Other mouse-sourced IEAs examined at the same time:
  - GO:0043565 sequence-specific DNA binding <- mouse IDA PMID:20956546 (MGI). Onodera et
    al. 2010 is a ChIP study: "TrxG complex associated with the TrxG component Menin binds
    to the whole GATA3 gene locus". Locus occupancy by a complex is not sequence-specific
    DNA binding -> source defect (MGI).
  - GO:0140608 cysteine-type endopeptidase activator activity <- mouse IDA PMID:14688275
    (MGI). Schnepp et al. 2004: "loss of menin reduces the expression of procaspase 8";
    menin raises caspase-8 levels (expression), it does not bind and activate the protease
    -> source defect (MGI).
  - GO:0003677 DNA binding <- mouse IDA PMID:14992727 and PMID:24824656 (MGI). Human has a
    direct IDA for dsDNA binding (PMID:15331604), so the generic term is true.
  - GO:0000781 chromosome, telomeric region <- mouse IDA PMID:12203793 (BHF-UCL): meiotic
    telomere localization only [PMID:12203793 "found that it localizes exclusively at
    telomeres"; "menin does not specifically associate with telomeres in somatic cells"].

## DNA binding: non-specific, not TF-like

- La et al. 2004 [PMID:15331604 "Here we show that menin directly binds to double stranded
  DNA in a sequence-independent manner."]; binds Y-form, branched and 4-way junction DNA
  ["It also binds a variety of DNA structures, including Y-structures, branched structures,
  and 4-way junction structures."]; binding needs positively charged residues of NLS1/NLS2
  in the C-terminus; random-sequence probes bind and poly dI/dC competes ["menin not only
  binds to DNA in a non-sequence specific fashion"]. Disease truncations (R527X, M558X)
  lose DNA binding and fail to repress proliferation.
- Milne et al. 2005 [PMID:15640349 "Menin has been shown to bind nonspecifically to DNA;
  however, the mechanisms responsible for its recruitment to specific chromosomal sites are
  not known."]
- Locus targeting is through partners: MLL1-LEDGF (chromatin anchoring), JunD, c-Myb/GATA-3,
  SMAD3, NF-kB.

## Core biology

1. **Scaffold/adaptor of MLL1/MLL2 (KMT2A/KMT2B) H3K4 methyltransferase complexes.**
   [PMID:14992727 "menin is associated with a histone methyltransferase complex containing
   two trithorax family proteins, MLL2 and Ash2L"]; [PMID:15199122 "Menin, a product of the
   MEN1 tumor suppressor gene, is also a component of the 1-MDa MLL complex."];
   [PMID:17500065 "Menin is shared by MLL and MLL2 complexes only"]. Crystal structures:
   [PMID:22327296 "menin acts as a scaffold protein to assemble a menin-MLL1-LEDGF ternary
   complex to coordinating gene transcription"]. MLL fusion oncoproteins need menin
   [PMID:16239140 "oncogenic MLL fusion proteins retain an ability to stably associate with
   menin through a high-affinity, amino-terminal, conserved binding motif"]. This
   dependency is the basis of menin-MLL inhibitors (PMID:22936661, MI-2/MI-2-2).
2. **Coactivator of target genes** (Hox genes, CDKN1B/p27, CDKN2C/p18, GATA3):
   [PMID:15640349 "Menin activates transcription by means of a mechanism involving
   recruitment of MLL to the p27Kip1 and p18Ink4c promoters and coding regions."];
   [PMID:15199122 "Abrogation of menin expression phenocopies loss of MLL and reveals a
   critical role for menin in the maintenance of Hox gene expression."];
   [PMID:20484083 "c-Myb, GATA-3, and Menin form a core transcription complex that regulates
   GATA-3 expression"].
3. **Corepressor of JunD (AP-1) and NF-kB**: [PMID:9989505 "Menin repressed transcriptional
   activation mediated by JunD"]; the same pocket binds JunD and MLL1 [PMID:22327296 "The
   menin-JUND interaction blocks JUN N-terminal kinase (JNK)-mediated JUND phosphorylation
   and suppresses JUND-induced transcription."]; [PMID:11526476 "Menin represses
   p65-mediated transcriptional activation on NF-kappaB sites"]; hTERT repression
   [PMID:12837246 "the tumor suppressor Menin, is a direct repressor of hTERT"];
   [PMID:23784080 "JunD and menin form a repressor complex of hTERT transcription"].
4. **Location**: nucleus [PMID:9465067 "menin is located primarily in the nucleus"],
   chromatin and nuclear matrix [PMID:12874027]. Minor cytoplasmic pools (cleavage furrow
   with NMHC II-A, PMID:14508515; Pem, PMID:11500056).

## Peripheral / context-dependent

- TGF-beta/SMAD3 signaling (PMID:11274402), osteoblast differentiation via JunD
  (PMID:15563473), Th2 differentiation via GATA3 (PMID:20484083).
- DNA damage: FANCD2 association (PMID:12874027), relocation to chromatin after UV via
  ATR-CHK1 (PMID:16690369), S-phase checkpoint with CHES1/FOXN3 (PMID:16951149). No
  evidence that menin carries out a DNA repair step.
- JNK: Gallo et al. show menin does not affect JNK/ERK activation but blocks
  phosphorylation of Jun/Elk-1 targets [PMID:12226747 "Kinase assays show that Menin
  overexpression does not interfere with activation of either ERK2 or JNK1"], so
  "negative regulation of JNK cascade" overstates.
- Reactome places menin in ER lumen only through the generic FAM20C-substrate reaction
  (R-HSA-8952289); menin is a nuclear protein, so that row was removed.

## Review decisions (summary)

- GO:0001216 IEA -> MODIFY to GO:0003713 transcription coactivator activity, plus source
  defect on mouse O88559 UniProt IDA row.
- GO:0043565 IEA -> REMOVE (+ MGI source defect); GO:0140608 IEA -> REMOVE (+ MGI source defect).
- GO:0000976 rows (IBA, IDA, IEA) -> MARK_AS_OVER_ANNOTATED: ChIP occupancy reflects
  recruitment by DNA-binding partners, not sequence-specific binding by menin.
- Protein binding: JunD and NF-kB rows -> MODIFY to transcription corepressor activity;
  c-Myb/GATA-3 rows -> MODIFY to transcription coactivator activity; MLL1 row from the
  structure paper -> MODIFY to protein-macromolecule adaptor activity; other rows REMOVE as
  uninformative.
