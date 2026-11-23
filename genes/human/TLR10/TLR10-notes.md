# TLR10 (human, Q9BXR5) review notes

Sources: UniProt Q9BXR5 (function text is "By similarity" only), GOA (39 rows), cached
publications (GOA PMIDs plus TLR10 functional papers fetched for this review).
Deep-research cross-check: see bottom of file.

## Is TLR10 an inhibitory TLR? (project question 4)

Yes, on the weight of cached primary evidence, with a minority of activating reports.

Inhibitory / non-activating:
- [PMID:20348427 "However, TLR10, alone or in cooperation with TLR2, fails to activate typical TLR-induced signaling, including NF-kappaB-, IL-8-, or IFN-beta-driven reporters"] (abstract only)
- [PMID:25288745 "We demonstrate that TLR10 is a modulatory receptor with mainly inhibitory effects"]; [PMID:25288745 "cotransfection in human cell lines showed that TLR10 acts as an inhibitory receptor when forming heterodimers with TLR2"]
- [PMID:27022193 "This broad TLR suppressive activity affects both MyD88- and TRIF-inducing IFN-β-mediated signaling pathways upstream of IκB and MAPK activation"]; [PMID:27022193 "These results demonstrate that TLR10 functions as a broad negative regulator of TLR signaling"]
- B cells: [PMID:27956526 "We have found that Ab-mediated engagement of TLR10 on primary human B cells suppresses B cell proliferation, cytokine production, and signal transduction"]; B-cell intrinsic by adoptive transfer.
- Monocytes: [PMID:28235773 "We report that TLR10 is preferentially expressed on monocytes and suppresses proinflammatory cytokine production resulting from either TLR or CD40 stimulation"]
- pDCs: [PMID:38995177 "Our data provide the (to our knowledge) first evidence that TLR10 is constitutively expressed on the surface of human pDCs and works as a regulator of their innate response"]
- dsRNA: [PMID:29616030 "Recognition of dsRNA by TLR10 activates recruitment of myeloid differentiation primary response gene 88 for signal transduction and suppression of interferon regulatory factor-7 dependent type I IFN production"]

Activating reports (single labs, knockdown/overexpression):
- Influenza: [PMID:24567377 "TLR10 contributed to innate immune sensing of viral infection leading to cytokine induction, including proinflammatory cytokines and interferons"]
- Listeria: [PMID:24198280 "NF-κB activation was seen to require TLR2 in addition to TLR10"] (abstract only)
- HIV-1 gp41: [PMID:30930906 "Notably, HIV-1 gp41 was recognized as a TLR10 ligand, leading to the induction of IL-8 and NF-κBα activation"]
- Early reporter work with CD4-TLR10 chimera: [PMID:15728506 "by using a recombinant CD4TLR10 molecule we also demonstrated that TLR10 directly associates with MyD88"]

## Propagated positive-signaling terms vs this evidence

- GO:0002224 TLR signaling pathway (IBA PTN002808083; IEA InterPro): KEEP_AS_NON_CORE,
  not REMOVE. TLR10 recruits MyD88 and transduces a signal on engagement, so the generic
  term is defensible; but the output is predominantly inhibitory, which the IBA node
  (seeded by activating TLR1/2/4/6) does not convey. Raised as a PAINT question.
- GO:0071221 cellular response to bacterial lipopeptide / GO:0071723 lipopeptide binding
  (IBA PTN000687445): KEEP_AS_NON_CORE. Supported by TLR10 ectodomain chimera data
  ([PMID:20348427 "TLR10 senses triacylated lipopeptides and a wide variety of other microbial-derived agonists shared by TLR1, but not TLR6"]) but direct binding not measured.
- GO:0035663 TLR2 binding (IBA) and signaling receptor activity: ACCEPT.
- Reactome TAS rows are all plasma membrane (CC); accepted as locations, but the
  underlying Reactome reactions model TLR10 (with TLR5) as activating MyD88-IRAK
  signaling, which the inhibitory data contradict. Raised as a question.
- No positive-regulation-of-cytokine rows exist on TLR10 in GOA, so nothing further to remove.

## NEW annotations
- GO:0034122 negative regulation of toll-like receptor signaling pathway (PMID:27022193;
  also PMID:25288745). Participation: TLR10 is the receptor that transduces the
  suppressive signal / competes for TLR2. Comparator: TYRO3, SMPDL3B, IRAK3 carry
  GO:0034122 in human GOA (QuickGO query, 2026-09-30).
- GO:0030889 negative regulation of B cell proliferation (PMID:27956526).

## protein binding rows
TLR2 (co-IP) -> MODIFY GO:0035663; TLR1 (co-IP) -> MODIFY GO:0035325; isolated-TMD ToxR
rows (PMID:23155421) and Y2H interactome hits WFS1/ATXN3 (PMID:32814053) -> REMOVE.

## Localization
Surface in pDC/B/monocyte (PMID:38995177, PMID:28235773) and endosomal in macrophages
[PMID:29616030 "TLR10 was predominately expressed in endosomes, with the highest expression detected in RAB11A+ recycling endosomes and RAB5+ early endosomes"].
Plasma membrane accepted; endosome not proposed as NEW (single study).

## Deep-research cross-check (2026-09-30)

- **Agrees:** TLR10 as a predominantly inhibitory, orphan TLR (supports the NEW
  `GO:0034122` and the KEEP_AS_NON_CORE handling of propagated activating terms);
  TLR2 and TLR1 heterodimerisation; MyD88 recruitment without NF-kappaB activation;
  PI3K/Akt-IL-1Ra mechanism; B-cell suppression; dual plasma membrane/endosome
  location; minority activating reports (influenza, Listeria, HIV-1 gp41).
- **Adds:** the report emphasises the pDC study (PMID:38995177, already cited):
  antibody engagement suppressed virus-induced IFN-alpha, IFN-lambda and TNF-alpha
  via STAT3/SOCS3 and blocked IRF7 nuclear translocation. Verified in the cached full
  text [PMID:38995177 "The induction of IFN-α and TNF-α by all 4 viruses was
  significantly suppressed upon TLR10-engagement as was the expression of IL6 by SeV,
  and IFN-λ by HSV."]. Because the stimulus is a surrogate agonist antibody and no
  physiological ligand is known, this was raised as a suggested question (GO:0032687
  negative regulation of interferon-alpha production, QuickGO-verified) rather than
  added as NEW. Polymorphism/disease associations and TLR10-transgenic mouse data were
  not used.
- **Conflicts:** the report states in one place that monocytes lack TLR10 and
  elsewhere that monocytes express it; the review follows the primary paper
  [PMID:28235773 "TLR10 is preferentially expressed on monocytes"]. The report also
  describes TLR10 homodimers as "generally" pro-inflammatory, which the cited primary
  papers do not support; not adopted.
- **Changes:** no annotation decisions changed. Added the report to `references`,
  cited it as corroborating context on the NEW `GO:0034122` row, and added one
  suggested question (pDC IFN-alpha suppression).
