# egl-44 (C. elegans) review notes

## Provenance and method

- Automated deep research was not available for this review: no FutureHouse,
  Perplexity or OpenAI keys exist in this environment, so `just deep-research*`
  was not run. The literature search below was done by hand.
- Queries run (2026-11-16):
  - PubMed E-utilities: `egl-44[tiab] OR "EGL-44"[tiab]` (17 hits) and
    `(yap-1[tiab] OR "egl-44"[All Fields] OR "EGL-44"[All Fields]) AND elegans`
    (30 hits); all titles screened.
  - Web search: "egl-44 TEAD Caenorhabditis elegans transcription factor neuron
    fate"; "EGL-44 YAP-1 C. elegans Hippo TEAD"; "Iwasa 2013 YAP-1 EGL-44
    interaction TEAD reporter".
  - Europe PMC open-access status for the GOA papers: none of PMID:11274062,
    PMID:12954713, PMID:23946438, PMID:30291162 is in the open-access subset, so
    the cached copies are abstract-only. PMC pages for PMID:30291162 and the
    Development page for PMID:23946438 were read with a web-fetch tool that
    returns a model-written summary. Findings taken from those summaries are
    marked "(full text, via summary)" below and are not quoted as verbatim.
- WormBase curated description: `egl-44-deep-research-wormbase.md` (fetched
  2026-11-16). UniProt Q19849 (Swiss-Prot, entry version 173).

## Identity and domains

- 486 aa (isoform a displayed), five isoforms. TEA/ATTS DNA-binding domain
  (residues 88-164, PROSITE PS51088) and a C-terminal YAP-binding domain
  (Pfam PF17725 YBD); PANTHER PTHR11834:SF0 (scalloped/TEAD subfamily). It is
  the single C. elegans TEAD [PMID:31358532 "yap-1 encodes a homolog of
  YAP/Yki, and egl-44 encodes a homolog of TEAD/Sd."].
- Missense alleles in the TEA domain (A91V, A134V n1080, R140Q n998, R145K)
  give the Egl and extra-Q-neuron phenotypes (UniProt FT MUTAGEN).

## Neuronal fate: the EGL-44/EGL-46 repressor

- Original genetics: mutations in egl-44 and egl-46 increase the number of
  touch-receptor-like cells [PMID:8187641 "Mutations in seven genes either
  reduce (lin-14) or increase (lin-4, egl-44, egl-46, sem-4, ced-3 and ced-4)
  the number of touch receptor-like cells."]. mec-3 expression itself is not
  changed in egl-44 mutants [PMID:37281420 "In the egl-44 and egl-46 mutant
  backgrounds, expression pattern was the same as wild-type animals."].
- Cloning: [PMID:11274062 "In egl-44 and egl-46 mutants, two other neurons,
  the FLP cells, express touch receptor-like features."]; [PMID:11274062
  "egl-44 encodes a member of the transcription enhancer factor family."];
  [PMID:11274062 "expression of egl-46 is dependent on egl-44 in the FLP cells
  but not in the HSN cells."]; [PMID:11274062 "Wild-type touch cells express
  egl-46 but not egl-44. Moreover, ectopic expression of egl-44 in the touch
  cells prevents touch cell differentiation in an egl-46-dependent manner."];
  [PMID:11274062 "The sequences of these genes and their nuclear location as
  seen with GFP fusions indicate that they repress transcription of touch cell
  characteristics in the FLP cells."]. HSN: [PMID:11274062 "egl-44 and egl-46
  also affect the differentiation of other neurons including the HSN neurons,
  two cells needed for egg laying."].
- FLP versus TRN: FLP neurons transcribe low levels of TRN mRNAs without
  making the proteins; loss of EGL-44/EGL-46 or ectopic ALR-1 lets them acquire
  TRN traits [PMID:22087002 "Previous studies showed that loss of the EGL-44
  and EGL-46 transcription factors cause the FLP neurons to acquire TRN-like
  traits."].
- Mechanism: [PMID:30291162 "The FLP neurons fail to activate TRN genes,
  however, because a complex of two transcriptional repressors (EGL-44/EGL-46)
  prevents their expression."]; [PMID:30291162 "As EGL-44/EGL-46 also inhibits
  the production of ZAG-1, these proteins form a bistable, negative-feedback
  loop that regulates the choice between the two neuronal fates."]. (Full text,
  via summary:) recombinant EGL-44, and the EGL-44/EGL-46 complex, bound
  sites next to UNC-86/MEC-3 motifs in TRN gene promoters (mec-4, mec-18) in
  EMSA; changing one adenine abolished EGL-44 binding, and a mec-18 reporter
  carrying a binding-site mutation was weakly de-repressed in some FLP cells
  (the summary of the matching mec-4 experiment was ambiguous and is not relied
  on); the two UNC-86/MEC-3 sites in
  the mec-3 promoter were not bound, consistent with PMID:37281420; ALR-1 is
  de-repressed in FLP of egl-44 and egl-46 mutants; the discussion states that
  EGL-44/EGL-46 also activates FLP genes. UniProt summarises the binding as
  [file:worm/egl-44/egl-44-uniprot.txt "Binds to DNA sequence motif
  5'-CATNNNNAAATGCAT-3' as a heterodimer with egl-46"]; the exact motif could
  not be checked against the paper.
- Direct interaction with EGL-46: [PMID:23946438 "The TEAD TF EGL-44, in a
  physical association with the zinc-finger TF EGL-46, instructs cell cycle
  exit after the terminal division."]. (Full text, via summary:) yeast
  two-hybrid maps the N-terminal EGL-44 fragment containing the TEA domain to
  the C-terminal zinc-finger fragment of EGL-46; GST pull-down confirms a direct
  interaction. The Q-lineage phenotype is one extra round of division of QR.ap
  (and the equivalent Q.p descendant), whose daughters both become A/PQR-like
  oxygen-sensing neurons. The paper assigns asymmetric division to HAM-1, not to
  EGL-44 [PMID:23946438 "we showed that the storkhead TF HAM-1 regulates spindle
  positioning and myosin polarization during asymmetric cell division"].
- HOB (male): [PMID:12954713 "male vulva location behavior and expression of
  lov-1 and pkd-2 in the ciliated sensory neuron HOB require the activities of
  transcription factor EGL-46 and to some extent also EGL-44."]. egl-44(n1080)
  is a partial allele (UniProt MUTAGEN).
- PVD: [PMID:29031632 "The known EGL-46 binding partner, the TEAD transcription
  factor EGL-44, is also required for PVD"]; [PMID:29031632 "Finally, our
  results have also identified at least two PVD-expressed markers that are
  redundantly regulated by both MEC-3 and the EGL-44/EGL-46 complex (Figure
  5)."]; [PMID:29031632 "This result confirms the idea that egl-44 and egl-46
  act in a common genetic pathway to mediate PVD 2° branching."].

## Hippo effector: the YAP-1/EGL-44 activator

- YAP-1 binding: [PMID:31358532 "It also showed that YAP-1 binds to EGL-44,
  the worm homolog of TEAD/Sd ( Iwasa et al."]. The YAP-1 paper itself
  (PMID:23396260) is abstract-only here; its abstract does not mention EGL-44.
  UniProt records the interaction as "Interacts with yap-1 (via WW domain)". In
  other animals YAP binds TEAD through its N-terminal TEAD-binding domain, which
  YAP-1 also has [PMID:23396260 "shows sequence similarities to YAP in the
  N-terminal TEAD-binding domain and in the WW domain"]; the WW-domain mapping
  could not be checked.
- Intestinal polarity and larval survival: [PMID:31358532 "We identified
  several alleles of yap-1 and egl-44 that suppress the effects of this
  mutation."]; [PMID:31358532 "These data suggest that induction of polarity
  defects and eventual death in wts-1 mutants requires both YAP-1 and
  EGL-44."]; [PMID:31358532 "Transcriptome analysis identified several target
  candidates of the YAP-1-EGL-44 complex including TAT-2, which encodes a
  putative P-type ATPase."].
- Larval progression: [PMID:41746831 "WTS-1, YAP-1, and the TEAD-like
  transcription factor EGL-44 form a conserved core module required for larval
  development past the L2 stage."]; [PMID:41746831 "We conclude that WTS-1
  represses YAP-1 and EGL-44/TEAD to permit developmental progression, a
  mechanism that is conserved among metazoans."].
- Innate immunity: [PMID:32857822 "we found that the EGL-44/TEAD transcription
  factor and its transcriptional activator YAP-1/YAP (Yes-associated protein)
  were activated when the intestinal barrier was disrupted by infections with
  the pathogenic bacterium Pseudomonas aeruginosa PA14."]; [PMID:32857822
  "Genetic inactivation of yap-1 and egl-44 significantly reduced the survival
  rate and promoted bacterial accumulation in worms after bacterial
  infections."]. This YAP-1 activation is Hippo-independent (PP2A).
- Neuron maintenance: [PMID:40178516 "Loss of yap-1 or egl-44 completely
  restores structural integrity of the wts-1 mutants."]. egl-44 is not
  expressed in wild-type touch cells (PMID:11274062), so where EGL-44 acts in
  this suppression is open.
- Phagosome closure: [PMID:40898783 "followed by new roles for the
  transcription factors YES-associated protein (YAP)-1/YAP and EGL-44/TEAD in
  promoting the localization of SYX-2/syntaxin around the dying TSC remnant."]
  (abstract only).

## Annotation decisions (summary)

- Core MF: Pol II-specific DNA-binding transcription factor activity, used two
  ways: as a repressor with EGL-46 in neurons and as an activator with the
  coactivator YAP-1. Binding to EGL-46 and to YAP-1 are both accepted.
- `positive regulation of exit from mitosis` names the M-to-G1 transition; the
  Q-lineage defect is an extra round of division, so it is modified to
  `negative regulation of neuroblast proliferation`. `asymmetric neuroblast
  division` is marked over-annotated: the paper places EGL-44 in cell cycle
  exit and HAM-1 in asymmetric division.
- `embryonic organ development` (IBA from mouse Tead1/Tead4) is marked
  over-annotated: no embryonic organ defect is reported for egl-44.

## WormBase and UniProt text check

- WormBase: TEAD class, FLP touch-fate repression, HSN, YAP-1 binding, nuclear
  GFP in hypodermis/pharynx/intestine/FLP/HSN, and egl-44-dependent egl-46
  expression in FLP all check out. The TEAD-reporter activation by YAP-1 plus
  EGL-44 could not be read (PMID:23396260 abstract-only). Missing: the
  EGL-46 complex as a DNA-binding repressor, the ZAG-1 loop, the Q-lineage,
  HOB and PVD roles, and all Hippo-pathway roles (intestinal polarity, larval
  progression, immunity).
- UniProt FUNCTION: accurate and detailed for the neuronal roles; omits the
  WTS-1/YAP-1/EGL-44 Hippo-pathway roles (PMID:31358532, PMID:41746831) and
  the immune role (PMID:32857822). The thermal-stress sentence is an author
  statement (ECO:0000303) and the abstract does not show that egl-44 was tested.
