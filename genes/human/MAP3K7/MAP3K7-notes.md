# MAP3K7 (TAK1) review notes

## Provenance / process

- 2026-10-05: de-novo review. GOA (223 rows), UniProt and stub YAML fetched earlier; publications cached with
  `just fetch-gene-pmids human MAP3K7` (57/57). Extra PMIDs cached with `just fetch-pmid`:
  8533096 (TAK1 discovery), 14633987 (TAB3), 15327770 (TAB2/TAB3 K63-Ub binding).
- Deep research: the falcon provider is known to fail for this batch (HTTP 402), so it was not attempted.
  No `-deep-research-*.md` file exists for this gene; these notes are built from cached primary literature,
  the UniProt record and the PTHR46716 family review.
- Most key TAK1 papers are cached abstract-only (`full_text_available: false`): 8663074, 9079627, 10094049,
  10702308, 10838074, 10882101, 11460167, 8638164. Full text available for 11865055, 12242293, 12589052,
  14982987, 17079228, 17158449, 19675569, 20538596, 21512573, 25371197, 27426733 and several proteomics screens.

## Identity and architecture

- MAP3K7 / TAK1, 606 aa (isoform 1B is canonical; 4 splice isoforms), TKL-group Ser/Thr kinase; N-terminal
  kinase domain (catalytic K63, HRD D156), C-terminal TAB2/TAB3-binding region (residues ~479-553)
  [PMID:17158449 "residues 479-553 of TAK1 appear to be necessary and sufficient for TAB2/TAB3 interaction"].
- Discovered in a yeast MAPK-pathway complementation screen as a MAPKKK stimulated by TGF-beta and BMP
  [PMID:8533096 "A genetic selection based on a MAPK pathway in yeast was used to identify a mouse protein kinase (TAK1) distinct from other members of the MAPKKK family."].

## Molecular function: MAP3K / Ser-Thr kinase

- Phosphorylates and activates MKK6 and MKK3 (p38 branch)
  [PMID:8663074 "MKK3 was also shown to be a good substrate for TAK1 in vitro."].
- Activates MKK4/SEK1 -> JNK; activated by ceramide
  [PMID:9079627 "Expression of a constitutively active form of TAK1 resulted in activation of SAPK/JNK and SEK1/MKK4, a direct activator of SAPK/JNK."].
- TAK1 complex (TRIKA2 = TAK1+TAB1+TAB2) phosphorylates IKK (IKKbeta) and MKK6 in a K63-ubiquitin-dependent way
  [PMID:11460167 "We find that the TAK1 kinase complex phosphorylates and activates IKK in a manner that depends on TRAF6 and Ubc13-Uev1A."].
- Activation is by autophosphorylation in the activation loop (Ser192; Thr184/Thr187)
  [PMID:10702308 "These results suggest that IL-1 and ectopic expression of TAB1 both activate TAK1 via autophosphorylation of Ser-192."];
  [PMID:10838074 "Autophosphorylation of two threonine residues in the activation loop of TAK1 was necessary for TAK1 activation."].
- Inactivated by PP6 dephosphorylation of Thr187 [PMID:17079228 "PP6 associated with and inactivated TAK1 by dephosphorylation of Thr-187"].
- Other direct substrates: AMPK (in vitro) [PMID:20538596], STING Ser355 [PMID:37832545 "activated TAK1 directly mediates STING phosphorylation on serine 355"],
  Ror2 C-terminus [PMID:18762249]. The 1999 claim that TAK1 phosphorylates NIK [PMID:10094049] predates the
  TAK1->IKKbeta model; NIK is now understood as the non-canonical NF-kB kinase acting independently of TAK1.

## Complex: TAK1-TAB1-TAB2/TAB3

- TAB1 is a constitutive activator [PMID:8638164 "TAB1 and TAK1 were co-immunoprecipitated from mammalian cells."].
- TAB2 links TAK1 to TRAF6 in IL-1 signaling [PMID:10882101 "These results define TAB2 as an adaptor linking TAK1 and TRAF6 and as a mediator of TAK1 activation in the IL-1 signaling pathway."].
- TAB3 is redundant with TAB2 in IL-1 and TNF signaling [PMID:14633987 "These results suggest that TAB2 and TAB3 function redundantly as mediators of TAK1 activation in IL-1 and TNF signal transduction."].
- TAB2/TAB3 NZF domains are K63-polyubiquitin receptors; TAB2 binds ubiquitinated RIP after TNF
  [PMID:15327770 "TAB2 and TAB3 are receptors that bind preferentially to lysine 63-linked polyubiquitin chains through a highly conserved zinc finger (ZnF) domain."].
- Unanchored K63 chains directly activate TAK1 via TAB2 [PMID:19675569 "free Lys 63 polyubiquitin chains, which are not conjugated to any target protein, directly activate TAK1 by binding to the ubiquitin receptor TAB2"].
- GO term GO:0097076 (TGF-beta activated kinase 1 complex) exists, is unrestricted, but has zero annotations in GOA
  (QuickGO, 2026-10-05). ComplexPortal annotates MAP3K7 to the generic GO:1902554 serine/threonine protein kinase
  complex (IPI, PMID:22158122). GO:0097076 is_a GO:1902911 protein kinase complex, but NOT is_a GO:1902554
  (ontology placement gap). Proposed as NEW (part_of GO:0097076) in this review.

## Pathways (upstream inputs)

- IL-1R/TLR (MyD88-IRAK-TRAF6) [PMID:10094049; PMID:12242293 membrane complex II then cytosolic activation].
- TLR3/TRIF -> TRAF6-TAK1-TAB2 -> NF-kB, not IRF3 [PMID:14982987 "DN-TRAF6 and DN-TAK1 blocked poly(I.C)-induced NF-kappaB but not IRF3 activation"].
- TLR4 (ECSIT complex) [PMID:25371197]. TNF via TAB2/TAB3 binding to ubiquitinated RIP1 [PMID:15327770, PMID:14633987].
- TGF-beta: TbetaRI-TRAF6 activates TAK1 (K63-Ub of TAK1 Lys34) -> p38/JNK [PMID:18758450]; TGF-beta-induced apoptosis via TAK1-MKK3-p38 [PMID:12589052].
- TCR: BCL10-MALT1-TRAF6-TAK1 -> IKK, IL-2 [PMID:15125833 "RNAi-mediated silencing of MALT1, TAK1, TRAF6, and TRAF2 suppressed TCR-dependent IKK activation and interleukin-2 production in T cells."].
- NOD2 [PMID:15075345], TRIM5 capsid sensing via free K63 chains [PMID:21512573], STING trafficking [PMID:37832545].

## Disease

- Frontometaphyseal dysplasia 2 / cardiospondylocarpofacial syndrome: MAP3K7 gain-of-function (P485L)
  [PMID:27426733 "it does increase TAK1 autophosphorylation and alter the activity of more than one signaling pathway regulated by the TAK1 kinase complex"].

## Curation decisions summary

- Core MF: GO:0004709 MAP3K activity and GO:0004674 Ser/Thr kinase (IKKbeta, MKK3/4/6/7). GO:0106310 rows accepted.
- GO:0004707 MAP kinase activity (IDA, PMID:11865055): full text shows JNK1 activity was assayed, not TAK1 as a MAPK ->
  MODIFY to GO:0004709.
- GO:0008349 MAP4K activity (Reactome TAS, mouse IEA): Reactome events are TAK1 autophosphorylation; this is not
  MAP4K activity on a distinct MAP3K -> MODIFY to GO:0004674 (autophosphorylation captured by the Ser/Thr kinase term).
- 54 protein-binding IPI rows: REMOVE (uninformative) except MODIFY where a specific partner class is clear
  (E3 ligases -> GO:0031625; PPP6C -> GO:0019903; JIP1 -> GO:0097110; TGFBR1 -> GO:0034713).
- Downstream physiology (osteoblast, bone development, hypoxia, angiotensin, vascular SMC, cell size, cell cycle, ROS)
  from rat/mouse orthology IEA: MARK_AS_OVER_ANNOTATED or KEEP_AS_NON_CORE.
- histone kinase activity / chromatin remodeling IEA (rat): no human evidence; MARK_AS_OVER_ANNOTATED.

## Module consistency (tnf_signaling, nlr_signaling)

- Neither modules/tnf_signaling.yaml nor modules/nlr_signaling.yaml has a MAP3K7/TAK1 part, although both modules'
  falcon deep research names TAK1-TAB2/3 as the kinase relaying K63/M1-ubiquitin scaffolds to IKKbeta and MAPKs.
  The tnf "NF-kappaB and inflammatory output" step is carried by a "TRAF2 signal relay" part, and nlr by
  "RIPK2 inflammatory signal relay"; neither is the kinase that phosphorylates IKKbeta. Discrepancy reported to caller.
