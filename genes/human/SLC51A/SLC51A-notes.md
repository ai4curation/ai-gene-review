# SLC51A (OSTalpha, Q86UW1) — curation notes

## 2026-10-21 — Full review, independent of the ProtNLM2 predictions

New review of a gene that had no prior folder in this repository. Written as the
experimentally characterised human reference for the DROME/CG6836 (Q9VVV2) relation;
no ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon human SLC51A --fallback perplexity-lite` failed: the falcon
(Edison) provider returned `403 Forbidden — Failed to authenticate`, and the
perplexity-lite fallback then timed out at 600 s. No `-deep-research-*.md` file exists
for this gene. The review was therefore built from the UniProt record, the cached
publications seeded by `just fetch-gene-pmids`, and five further papers located through
PubMed esearch and cached with `just fetch-pmid` (PMID:17650074, PMID:22535958,
PMID:18292224, PMID:31863603, PMID:35462858).

### What is experimentally established in human

- **Obligate heteromer.** Neither subunit transports alone: in *Xenopus* oocytes
  "None of the proteins elicited a transport signal when expressed individually in
  oocytes; however, all nine OSTalpha-OSTbeta combinations ... generated robust estrone
  3-sulfate transport activity" [PMID:12719432]. This is why GOA uses
  `contributes_to` on GO:0015125, and why this review keeps that reading.
- **Substrates (human protein, heterologous assay).** Estrone 3-sulfate; also
  "taurocholate, digoxin, and prostaglandin E2 but not of estradiol
  17beta-d-glucuronide or p-aminohippurate" [PMID:12719432]. UniProt adds DHEA sulfate
  with ECO:0000269|PubMed:16317684. The long list of individual conjugated bile acid
  RHEA reactions in the UniProt entry is `ECO:0000250|UniProtKB:Q8R000`, i.e. transferred
  from mouse, and is treated here as inferred rather than human-experimental.
- **Mechanism.** Sodium-, chloride-, pH- and ATP-independent: "the oocytes demonstrated
  robust substrate efflux and trans-stimulation, indicating that transport occurs by
  facilitated diffusion" [PMID:16317684]; the 2026 structures add
  "voltage-sensitive, bidirectional transport driven by electrochemical gradients"
  [PMID:41606328].
- **Architecture.** Two cryo-EM papers on the human complex, published back to back:
  "two OSTα units form the homodimeric core, with two OSTβ units bound to the
  periphery" [PMID:41606314] and "a symmetric tetramer of heterodimers, with each Ostα
  subunit showing a new seven-transmembrane fold, augmented by a single transmembrane
  helix of Ostβ" [PMID:41606328]. OSTalpha carries the substrate site: it "contains a
  unique cysteine-rich loop with seven palmitoylation sites" that with TM5/TM6 forms
  the bile acid recognition site [PMID:41606314]. The UniProt MUTAGEN block records ~20
  human OSTalpha alanine substitutions that reduce bile acid transport, including the
  palmitoylated cysteines C160–C167 and the C32–C284 disulfide.
- **Localisation.** "Indirect immunofluorescence microscopy localized OSTalpha and
  OSTbeta to the basolateral membrane of mouse, rat, and human ileal enterocytes, renal
  proximal tubular cells, and cholangiocytes" [PMID:16317684].
- **Human genetics.** Biallelic truncating SLC51A variant (premature stop at codon 186)
  in a consanguineous child: "the first demonstration of human OSTα deficiency in a
  child with elevated liver transaminases, cholestasis, liver fibrosis, and congenital
  diarrhea" [PMID:31863603]. OMIM PFIC6.

### What is inferred from mouse / by similarity

- Partner-dependent trafficking and mutual stabilisation are mouse work: "The
  interaction between Ostalpha and Ostbeta was required not only for delivery of the
  proteins to the plasma membrane, but it increased their stability" [PMID:17650074];
  Ostalpha homodimerization in that paper is BiFC in HEK293. Note that human OSTalpha
  did reach the oocyte plasma membrane when expressed alone [PMID:12719432], so ER
  retention of the unpartnered subunit is cell-context dependent — the ER membrane
  annotations are kept as non-core rather than accepted as the site of action.
- The in vivo intestinal requirement is from the Ostalpha knockout: "transileal
  transport of taurocholate was reduced by >80% in Ostalpha(-/-) vs. wild-type mice"
  [PMID:18292224]. Mouse Slc51a is the 1:1 ortholog in the same PANTHER subfamily
  (PTHR23423:SF11), so this is a sound transfer, but it is recorded as mouse evidence.
- Ostbeta knockout mice [PMID:35462858] bear on OSTbeta, not on SLC51A, and are cited
  as context only.

### Evolutionary grounding (for the CG6836 relation, not annotated here)

SLC51A is PTHR23423:SF11. The family PTHR23423 also contains TMEM184A/B/C and fungal
Hfl1-like proteins, so family membership alone does not imply OSTalpha function. The
fly gene CG6836/FBgn0036834 has **no** PANTHER subfamily in release 19.0 and therefore
no PAINT node, so no subfamily-level transfer is possible; the relationship rests on the
MAFFT/NJ tree in `genes/DROME/CG6836/CG6836-bioinformatics/RESULTS.md` and on the
Ensembl Compara list reported in [PMID:20538072], which notes that "the list of putative
OSTα orthologues includes genes from invertebrates such as the sea squirt ..., fruit fly
(Drosophila melanogaster; FBgn0036834), and roundworm". Nothing is transferred from
SLC51A to CG6836 in this review; conversely, nothing about CG6836 is used to support any
human claim. The key caveat for any future transfer is that every established human
function is a property of the OSTalpha-OSTbeta pair, and no OSTbeta homolog is known
outside vertebrates.

### Annotation decisions

- **ACCEPT (core):** GO:0015125 bile acid transmembrane transporter activity
  (`contributes_to`, all three rows), GO:0015721 bile acid and bile salt transport,
  GO:0032782 bile acid secretion, GO:0016323 basolateral plasma membrane,
  GO:0046982 protein heterodimerization activity, GO:0032991 protein-containing complex
  (no specific OSTalpha-OSTbeta complex term exists).
- **KEEP_AS_NON_CORE:** GO:0005789 ER membrane (biosynthetic/transit pool),
  GO:0042803 protein homodimerization activity (structural feature of the assembly).
- **MODIFY:** GO:0005886 plasma membrane and GO:0016020 membrane → GO:0016323; the
  generic GO:0022857 transmembrane transporter activity → GO:0015125; GO:0055085
  transmembrane transport → GO:0015721. The two IBA rows carry a `propagation_review`
  recording that the node calls (PTN000603313 for the surface location, the deeper
  PTN000603211 for generic transporter activity) are right at their nodes and only
  under-specific for this gene.
- **MODIFY on two GO:0005515 rows:** the IPI rows whose partner is UniProtKB:Q86UW2
  (SLC51B) are redirected to GO:0046982, since that interaction is the functional
  heterodimer seen in the structures.
- **REMOVE on three GO:0005515 rows:** ATXN1 (PMID:16713569, PMID:32814053) and DNAJC30
  (PMID:32296183) are high-throughput binary interactions with no reported functional
  consequence for SLC51A; bare protein binding is uninformative. Removal does not assert
  the interactions are false.
- **No NEW terms proposed.** The obvious candidate — a steroid-conjugate transporter
  activity for estrone 3-sulfate and DHEA sulfate, which is genuinely experimentally
  established for the human complex — has no suitable GO term (the branch has
  GO:0015125 for bile acids and nothing for sulfated steroids; searched GO for
  "steroid"/"sulfate" transmembrane transporter terms, nothing fits). Raised under
  `suggested_questions` rather than invented.
