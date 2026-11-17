# Fadd (Fas-associated death domain, BG4, CG12297, FBgn0038928; UniProt Q9V3B4) review notes

## Sources and searches (2026-11-16)

- Inputs: `Fadd-uniprot.txt` (Swiss-Prot Q9V3B4, FADD_DROME), `Fadd-goa.tsv` (32 rows),
  `Fadd-deep-research-flybase.md` (FlyBase hand-written description), cached GOA papers.
- GOA fetch note: QuickGO returned HTTP 500 for requests with `includeFields=taxonName`
  on 2026-11-16; the GOA file was regenerated with the project's
  `ai_gene_review.etl.gene.fetch_goa_data`, dropping only that include and filling the
  taxon-name column from taxon id 7227 (see `mei-9-notes.md`).
- PubMed queries run (E-utilities):
  - `(Fadd OR dFADD OR "BG4") AND drosophila` (60 hits, titles scanned)
  - `(Wengen OR Grindelwald OR eiger) AND (death domain OR Fadd OR dFADD OR Dredd) AND drosophila`
  - `Wengen[tiab] AND drosophila`
  - `(Dredd[tiab]) AND (apoptosis OR cell death) AND drosophila`
- Extra papers cached: PMID:41904322 (Winther et al. 2026, STING-FADD), PMID:22549468
  (Meinander 2012), PMID:23721820 (IMD pathway review), PMID:12176339 (Moreno 2002,
  Eiger), PMID:12065414 (Igaki 2002, Eiger), PMID:33824334 (Grnd/Wgn), PMID:19255589
  (dRYBP apoptosis), PMID:11703941 (imd cloning), PMID:9740659 (Dredd cloning). Also read
  and not used: PMID:35810247 (caspase review), PMID:24981286 (Eiger review).

## Protein

- 239 aa; N-terminal region 1-105 shared with Dredd (called the "death-inducing domain" by
  Hu and Yang) and a C-terminal death domain 151-237 (UniProt FT; PROSITE PS50017).
  [PMID:10934188 "dFADD contains a death domain that is highly homologous to the FADD death
  domain, and it also shares a novel domain with a Drosophila caspase DREDD, which we call
  death-inducing domain."]
- The N-terminal domain is a death effector domain (DED): structural modelling plus
  interface mutants and co-IP [PMID:41904322 "Thus, our mutational analysis and
  co-immunoprecipitation assays verify the AlphaFold model and confirm that dFADD and DREDD
  interact through a classical death effector domain interaction."]. Dredd binds via its
  DED1 [PMID:22549468 "Intriguingly, we found that the adaptor protein dFADD also selectively
  bound to DED1 ( Figure 2D ), which is in contrast to an earlier report ( Hu and Yang, 2000 )."].
- Dredd's prodomain is not a CARD (InterPro gives Dredd_N / Dredd_2nd families for Q8IRY7,
  no CARD signature), so the FlyBase IPI "CARD domain binding" row names the wrong domain.
- PAINT: all five Fadd IBA rows come from PTN008354262 in PTHR15077, placed at Eumetazoa
  (taxon:6072). Seeds: human FADD Q13158, rat Fadd (RGD:628700), mouse Fadd (MGI:109324), and
  fly Fadd itself for positive regulation of innate immune response.

## Imd pathway (core)

- Binds Imd: [PMID:12433364 "Using a two-hybrid screen in yeast, we have isolated the death
  protein dFADD as a molecule that associates with IMD."]; via death domains [PMID:23721820
  "IMD interacts via its death domain with the Drosophila homolog of FADD called dFADD or BG4
  (Naitza et al."]; interface residues in the Fadd DD [PMID:41904322 "Altogether, these data
  indicate that the residues E220 and Y223 in IMD interact with R171 in dFADD, with a
  contribution of E177."].
- Required for Gram-negative defense and AMP induction; acts between Imd and Dredd
  [PMID:12433364 "loss of dFADD function renders flies highly susceptible to Gram-negative
  infections without affecting resistance to Gram-positive bacteria"]; [PMID:12123572
  "Epistatic studies indicate that dFADD acts between Imd and Dredd."].
- Needed for IKK and JNK activation and Imd cleavage [PMID:16081424 "we find that the
  Drosophila caspase DREDD and its partner dFADD are required for the activation of DmIKK and
  JNK, in addition to their role in Relish cleavage."]; [PMID:20122400 "Here, we show that upon
  immune stimulation the imd protein is rapidly cleaved in a DREDD and FADD dependent manner."].
- Vibrio cholerae gut infection: fadd mutants fail to induce Diptericin but survive better
  [PMID:19046341 "As expected, dipt transcription was not detectable in infected faddEY10870 and
  dreddB118 mutants."]; [PMID:19046341 "Furthermore, mutations in the IMD pathway increased
  resistance to infection whereas mutations in the Eiger/Wengen pathway increased
  susceptibility."]. The defense-response row from this paper is still correct (AMP
  induction needs Fadd); the survival result reflects a cost of Imd activity in this model.

## Antiviral roles

- Sindbis replicon: replication higher in dfadd heterozygotes (PMID:19763182).
- dSTING pathway: Fadd is recruited to activated dSTING oligomers and, with Dredd, is required
  for Relish activation and antiviral activity in vivo [PMID:41904322 "Here, we show that dFADD
  is specifically recruited to activated, oligomeric dSTING to trigger cleavage and activation
  of Relish in a DREDD-dependent but IMD-independent manner."]; [PMID:41904322 "Finally, we
  show that both dFADD and DREDD are required for the antiviral activity of dSTING in vivo."].
  A NEW `GO:0140896 cGAS/STING signaling pathway` row was considered and not added: the
  paper is very recent and the existing virus-defense row already covers the role; recorded as
  a suggested question instead.

## Apoptosis and the absence of death receptors

- Overexpressed Fadd enhances Dredd processing and cell death (PMID:10934188, abstract only;
  assay system not visible).
- In vivo, apoptosis induced by overexpressed dRYBP needs Dredd and Fadd [PMID:19255589
  "requires the function of the pro-apoptotic REAPER, HID and GRIM proteins, the apical caspase
  DREDD, the adaptor dFADD protein as well as TRITHORAX (TRX)"].
- The fly TNF (Eiger) kills through JNK and the apoptosome, not Dredd [PMID:12176339 "Unlike its
  mammalian counterparts, however, the apoptotic effect of Eiger does not require the activity
  of the caspase-8 homolog DREDD, but it completely depends on its ability to activate the JNK
  pathway."].
- Fly TNF receptors lack death domains [PMID:33824334 "although it seems to lack an intracellular
  death-domain or Traf-interacting-motif required for canonical JNK signalling"] (Wengen);
  Grindelwald's intracellular region carries Veli and Traf2 binding domains (same paper).
  There is no CD95/Fas in flies; the receptor upstream of Fadd is PGRP-LC, which recruits Imd,
  not Fadd, directly.
- Non-apoptotic caspase role: spermatid individualization [PMID:14737191 "Together these
  observations argue that dFADD and DREDD participate in individualization."].

## Verdicts on the non-duplicative IBA rows

| Term | Action | One-line reason |
|---|---|---|
| GO:0005123 death receptor binding | REMOVE | Flies have no death-domain TNFRs; Fadd's DD partners are Imd and dSTING |
| GO:0031265 CD95 DISC | REMOVE | CD95/Fas is vertebrate-only; the fly Fadd complex is the PGRP-LC/Imd signalling complex |
| GO:0089720 caspase binding | ACCEPT | Fadd binds the caspase Dredd through DED-DED contact (PMID:10934188, PMID:41904322) |
| GO:0097191 extrinsic apoptotic signaling pathway | MARK_AS_OVER_ANNOTATED | No receptor-initiated Fadd apoptotic pathway in flies; Eiger death is Dredd-independent |

## Description sources

- FlyBase: "adaptor protein that functions downstream of the product of imd and upstream of the
  caspase encoded by Dredd in the immune deficiency pathway" is traced to PMID:12123572 and
  PMID:12433364. VERIFIED. It omits the dSTING antiviral role (2026).
- UniProt FUNCTION: correct (PMID:10934188, PMID:12433364); the apoptosis sentence reflects an
  overexpression assay. No defect recorded.
