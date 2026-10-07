# Slc10a1 (rat Ntcp, P26435) curation notes

## Provenance of this review

Automated deep research is **not available in this container**: the Falcon/Edison endpoint
returns `402 Payment Required`, the OpenAI endpoint returns `401 invalid_api_key`, and
`perplexity` is not a registered provider in this checkout. No `-deep-research-*.md` file
was created (per CLAUDE.md, hand-written content must never be named as a deep-research
provider output). The synthesis below was assembled by hand from the cached publications in
`publications/`, the UniProt record `Slc10a1-uniprot.txt`, and the companion human review
in `genes/human/SLC10A1/`.

## Gene identity

- UniProt P26435 (NTCP_RAT), 362 aa; RGD:3681; paralogue Slc10a2/Asbt = RGD:3682
- Family: bile acid:sodium symporter (BASS, TC 2.A.28); InterPro IPR002657
  [`Slc10a1-uniprot.txt` "Belongs to the bile acid:sodium symporter (BASS) (TC 2.A.28)
  family."]
- Glycosylated, multi-pass membrane protein; seven predicted TM domains in the original
  cloning paper [PMID:1961729 "coding for a protein of 362 amino acids (calculated
  molecular mass 39 kDa) with five possible N-linked glycosylation sites and seven putative
  transmembrane domains"]

## Core transport function

- Rat Ntcp was the founding member of the family, cloned by functional expression in
  Xenopus oocytes [PMID:1961729 "A cDNA encoding the rat liver bile acid uptake system has
  been isolated by expression cloning in Xenopus laevis oocytes."]
- It is the hepatocyte Na+/bile acid cotransport system [PMID:1961729 "This uptake process
  is mediated by a Na+/bile acid cotransport system."] and strictly Na+-dependent
  [PMID:1961729 "The cloned transporter is strictly sodium-dependent and can be inhibited
  by various non-bile-acid organic compounds."]
- Km for taurocholate ~25 uM in the cloning paper (UniProt kinetic annotation), ~34 uM in
  stably transfected CHO cells [PMID:9486191 "These cells exhibited saturable Na(+)-dependent
  uptake of [3H]taurocholate [Michaelis constant (K(m)) of approximately 34 microM] that was
  strongly inhibited by all major bile salts, estrone 3-sulfate, bumetanide, and cyclosporin A."]
- Stoichiometry is 2 Na+ per bile salt in the curated UniProt reaction set (RHEA:71875 and
  relatives), all with `ECO:0000269|PubMed:9486191` or `ECO:0000250|UniProtKB:O97736`.
- It is the principal hepatic bile acid *importer* [PMID:12105223 "including the principal
  hepatic bile acid importer, the Na(+)/taurocholate co-transporting polypeptide (Ntcp,
  Slc10a1)."; PMID:28827769 "The transport of bile acids across the basolateral membrane of
  the hepatocytes is mainly mediated by the NTCP."]
- Tissue distribution: liver-dominant, with cross-hybridising transcripts in kidney and
  intestine [PMID:1961729 "Northern blot analysis with the cloned probe revealed
  crossreactivity with mRNA species from rat kidney and intestine as well as from liver
  tissues of mouse, guinea pig, rabbit, and man."]

## Substrate range (rat-specific)

The rat transporter carries all physiological bile salts plus one sulfated steroid, but the
two xenobiotics tested were **inhibitors, not substrates**:

- [PMID:9486191 "These results show that the cloned Ntcp can mediate Na(+)-dependent uptake
  of all physiological bile salts as well as of the steroid conjugate estrone 3-sulfate."]
- [PMID:9486191 "However, there was no detectable Na(+)-dependent uptake of [3H]bumetanide
  or [3H]cyclosporin A."]
- [PMID:9486191 "Hence, Ntcp is a multispecific transporter with preference for bile salts
  and other anionic steroidal compounds."]
- Transcellular transport in the Ntcp/Bsep double transfectant covers the conjugated and
  unconjugated cholates and chenodeoxycholates but not lithocholate [PMID:15297262
  "Transcellular transport of cholate, glycocholate, taurochenodeoxycholate,
  chenodeoxycholate, glycochenodeoxycholate, tauroursodeoxycholate, ursodeoxycholate, and
  glycoursodeoxycholate, but not that of lithocholate was also observed across the double
  transfectant."]

**This is the one place where the rat evidence does not extend the human picture.** In
`genes/human/SLC10A1/`, `GO:0071466 cellular response to xenobiotic stimulus` was MODIFIED
to `GO:0042908 xenobiotic transport`, because human NTCP is a demonstrated rosuvastatin
carrier (PMID:34060352) and is described as participating in hepatic clearance of
xenobiotics (PMID:9458785). The rat substrate-specificity study explicitly failed to detect
uptake of either xenobiotic it tested, so the same MODIFY is **not** available here and the
rat row is removed outright rather than redirected.

## Polarity / localization

- Basolateral (sinusoidal) domain, shown directly by immunohistochemistry in polarized MDCK
  monolayers [PMID:15297262 "Immunohistochemical staining demonstrated that Ntcp was
  expressed at the basolateral domains, whereas Bsep was expressed at the apical domains."]
- Vectorial basal-to-apical bile salt flux requires Ntcp on the basal side [PMID:15297262
  "Basal-to-apical transport of taurocholate across the monolayer expressing only Ntcp and
  that coexpressing Ntcp/Bsep was observed, whereas the flux across the monolayer of control
  and Bsep-expressing cells was symmetrical."]
- The physiological context is stated in the same paper [PMID:15297262 "Bile salts are
  predominantly taken up by hepatocytes via the basolateral Na(+)-taurocholate
  cotransporting polypeptide (NTCP/SLC10A1)"]
- UniProt location: `Cell membrane {ECO:0000250|UniProtKB:Q14973}; Multi-pass membrane
  protein` — i.e. the rat subcellular-location statement is itself an ISS from human, while
  the basolateral specificity rests on the rat/MDCK IDA above.

## Ntcp is heavily *regulated*, and that is not the same as participating

Almost every rat Ntcp paper in this annotation set is a regulation study: the transporter's
mRNA/protein level goes down (occasionally up) in response to inflammation, synthetic
estrogen, ethanol, bile-acid load or diet. The mechanisms identified are all upstream
transcriptional ones, acting *on* the Ntcp promoter:

- Inflammation / IL-1beta via JNK-dependent RXR phosphorylation [PMID:12105223 "IL-1 beta
  treatment of cultured primary rat hepatocytes markedly reduced Ntcp RNA levels and Ntcp
  promoter activity in transiently transfected HepG2 cells."; PMID:12105223 "Bile flow is
  rapidly and markedly reduced in hepatic inflammation, correlating with suppression of
  critical hepatic bile acid transporter gene expression"]
- 17alpha-ethinylestradiol (EE) cholestasis: Ntcp is suppressed, and notably its suppression
  is *not* reversed by AMPK inhibition or FXR overexpression, unlike Bsep/Mrp2/Oatp2
  [PMID:27090119 "Furthermore, the mRNA and protein levels of bile acid transporters, Bsep,
  Mrp2, Ntcp and Oatp2 were significantly suppressed by EE in a dose-dependent manner";
  PMID:27090119 "However, the expression of Oatp2 and Ntcp were not significantly
  up-regulated by pretreatment with CC or over expression of FXR, which indicates other
  mechanisms might be involved in EE-mediated Oatp2 and Ntcp expression."]
- Bile-acid overload (geniposide hepatotoxicity): Ntcp mRNA falls at the toxic dose, read by
  the authors as feedback restriction of uptake [PMID:28827769 "Geniposide at 300 mg/kg also
  suppressed hepatic NTCP mRNA expression which could be a negative feedback mechanism to
  reduce bile acid entry in response to elevated hepatocyte bile acid concentrations";
  PMID:28827769 "The expression of NTCP mRNA was down-regulated by high dose of Geniposide,
  but up-regulated by low dose of Geniposide"]
- High-fat diet: a nuclear-receptor/transporter expression survey whose stated design is
  transcriptional [PMID:25612518 "We hypothesised that high fat feeding would alter the gene
  expression of major hepatic transporters through a dysregulation of the expression of the
  nuclear receptors."; PMID:25612518 "This suggests that a HFD may induce changes in the
  hepatobiliary transport and metabolism of endogenous and exogenous compounds."]
- Alcohol injury / dihydroartemisinin: the paper's own conclusion is about FXR-dependent
  steatosis, with Ntcp appearing only inside an FXR-target expression panel [PMID:27939985
  "In summary, DHA significantly improved alcoholic liver injury by inhibiting hepatic
  steatosis, which was dependent on its activation of FXR in hepatocytes."; PMID:27939985
  "Results demonstrated that DHA rescued FXR expression and activity in alcoholic rat
  livers."]

## Curation decisions and their reasoning

1. **Transport MF and BP rows -> ACCEPT** (`GO:0008508` x3, `GO:0015125` x3, `GO:0015721` x3).
   Rat Ntcp is the original experimental substrate for every one of these claims; the IDA
   rows (PMID:1961729, PMID:15297262) are the primary evidence, the TAS row restates it from
   a review-style introduction, and the IBA/IEA/ISO rows all land on the same, correct term.
   Duplicate GO ids across evidence codes are acceptable per CLAUDE.md.

2. **Localization rows -> ACCEPT** (`GO:0005886` x3, `GO:0016323` x3, `GO:0016020` x2).
   The IBA node for the NTCP-specific sub-clade (`PANTHER:PTN002570905`) is correctly
   basolateral, whereas the broader SLC10 node (`PANTHER:PTN000040759`) asserts only plasma
   membrane — consistent with the apical polarity of the ileal ASBT branch. `GO:0016020
   membrane` is a broad IEA/ISO parent of correctly annotated children and is kept.

3. **`GO:0016323` IDA from PMID:17082223 -> ACCEPT (deferring to the curator).** The cached
   record for that paper is abstract-only and its title and abstract are about Bsep
   (ABCB11) N-glycosylation in MDCK II cells; Ntcp is not named in the abstract. Per
   SKILL.md this is exactly the case where one must not cry mis-attribution: taurocholate
   uptake assays in polarized MDCK II cells require a basolateral uptake carrier, so Ntcp
   co-expression and its basolateral immunostaining are very likely documented in the full
   text the curator read [PMID:17082223 "Removal of glycans decreased taurocholate transport
   activity as determined in polarized MDCK II cells."]. The claim is independently
   established for rat Ntcp anyway by PMID:15297262.

4. **The four IEP "response to X" rows -> REMOVE** (`GO:0031667` response to nutrient levels,
   PMID:25612518; `GO:0043627` response to estrogen and `GO:0071466` cellular response to
   xenobiotic stimulus, PMID:27090119; `GO:0045471` response to ethanol, PMID:27939985).
   IEP = *inferred from expression pattern*: the assertion rests on Ntcp transcript/protein
   levels changing when the stimulus is applied. Under CLAUDE.md, `involved_in` requires that
   the gene product **do some of the work** of the process — catalyse a step, or supply
   structure or cofactor activity a step depends on. Being transcriptionally repressed by a
   stimulus is the opposite: Ntcp is the *target* of the response, not a participant in it.
   PMID:27090119 is the clearest case because it is full-text in the cache and dissects the
   mechanism: the signalling is AMPKalpha1/FXR, and Ntcp is a downstream readout that does
   not even respond to the interventions that rescue the other transporters. Ntcp performs no
   step of nutrient sensing, estrogen signalling, ethanol metabolism or xenobiotic sensing.
   Note also that these four stimuli are mutually redundant as annotations: they are four
   names for the same observation (hepatic Ntcp is down-regulated in cholestatic/metabolic
   liver stress), and the correct representation of that is a `regulation of ...` statement
   about the upstream regulator, or a GO-CAM, not four process terms on the transporter.

5. **`GO:0015721` IEP from PMID:28827769 -> ACCEPT**, not removed. Unlike the four above,
   this IEP row's term is one the gene product genuinely executes, and the same paper states
   it [PMID:28827769 "The transport of bile acids across the basolateral membrane of the
   hepatocytes is mainly mediated by the NTCP."]. The evidence code is weak for the claim,
   but the claim is right and is independently supported by IDA (PMID:1961729) and IBA. The
   distinction between this row and row 4 is precisely the participation test: here Ntcp is
   the entity that performs the transport step.

6. **No `NEW` annotations.** The HBV/HDV receptor function that justified two NEW terms on
   human SLC10A1 does not transfer: rodent Ntcp does not support HBV/HDV entry, which is why
   humanizing the receptor is required in the primate work (see the human notes). Estrone
   3-sulfate uptake (PMID:9486191) is a real rat activity with no non-obsolete GO transporter
   term available, so it is raised as a `suggested_questions` entry rather than asserted.

## Relationship to the human SLC10A1 review

Concordant on everything except point 4 of the human notes:

- Transport, localization and the "response to X" removals agree, and the rat IEP evidence
  *strengthens* the human conclusion: on the human side those three rows were GO_REF:0000107
  transfers from this very gene (UniProtKB:P26435), so removing them here removes the donor
  of the human over-annotations rather than only the copies.
- **Divergence:** human `GO:0071466` was MODIFIED to `GO:0042908 xenobiotic transport`; the
  rat row is REMOVED with no replacement, because PMID:9486191 reports no detectable
  Na+-dependent uptake of either xenobiotic tested in the rat protein. The human MODIFY rests
  on human-specific drug-substrate data and is not contradicted by this; it simply does not
  generalize.
- No GO-CAM model for Slc10a1 was found in `gocams/index.tsv` at review time.
