# ERLIN2 (SPFH2 / ER lipid raft-associated protein 2) review notes

UniProt: O94905 (ERLN2_HUMAN), 339 aa. Synonyms SPFH2, C8orf2. HGNC:1356.
Single-pass type II ER membrane protein with a lumenal SPFH/prohibitin (band 7) domain. Band 7/mec-2
family; associates with lipid-raft-like ER domains. Disease: hereditary spastic paraplegia SPG18A/SPG18B
and recessive intellectual disability/joint-contractures syndrome.

## Core biology
1. **ERLIN1/ERLIN2 complex mediating ERAD of IP3 receptors.** SPFH2 (ERLIN2) and SPFH1 (ERLIN1) form a
   ~2 MDa ring-shaped ER membrane complex that binds IP3R tetramers and mediates their ERAD with RNF170.
   [PMID:19240031 "the ER membrane protein SPFH1 and its homolog SPFH2 form a heteromeric approximately 2 MDa complex that binds to IP(3)R tetramers"]
   SPFH2 alone was shown to mediate ERAD of IP3 receptors and other substrates (PubMed:17502376, not cached).
   In complex with ERLIN1, interacts with RNF170. ComplexPortal CPX-7121.
2. **Sterol-accelerated ERAD of HMGCR (gp78/AMFR module).** ERLIN2 promotes sterol-accelerated ERAD of
   HMG-CoA reductase via an AMFR/gp78-containing ubiquitin ligase complex; TMUB1 bridges ERLIN2 to gp78.
   [PMID:21343306 "we identify two ER membrane proteins, SPFH2 and TMUB1, as associated proteins of mammalian gp78"]
   Interacts with AMFR, SYVN1, RNF139, TMUB1, HMGCR.
3. **Cholesterol binding / SREBP regulation.** Like ERLIN1, ERLIN2 restricts SREBP activation and
   regulates cholesterol homeostasis; interacts with SCAP, INSIG1, SREBF1, SREBF2 under sterol sufficiency.
   [PMID:24217618 "Erlins bound cholesterol with specificity and strong cooperativity"]
4. **E3-ligase binding.** ERLIN2 binds the ER ubiquitin ligases RNF170, AMFR/gp78, SYVN1, RNF139, and the
   RNF185/RNF5 module (PubMed:24019521) — informative ubiquitin protein ligase binding.
5. **Lipid-raft ER domains** (PMID:16835267).

## Annotation assessment summary
- ER membrane (GO:0005789) / ER (GO:0005783): core compartment → ACCEPT.
- ERLIN1/2 complex / ERAD of IP3R (GO:0036503 ERAD pathway IDA): core → ACCEPT.
- cholesterol binding (GO:0015485 IBA): core MF → ACCEPT (note: only IBA here, no human IDA, but consistent
  with the erlin family cholesterol-binding evidence in PMID:24217618).
- SREBP signaling / negative regulation cholesterol & fatty acid biosynthesis / regulation cholesterol
  biosynthesis: SREBP/sterol role → ACCEPT.
- ubiquitin protein ligase binding (GO:0031625 IPI PMID:24019521; IEA InterPro): binds RNF185/RNF5 and other
  ER E3 ligases → ACCEPT (informative).
- membrane raft (GO:0045121 IDA/NAS): lipid-raft ER domains → KEEP_AS_NON_CORE.
- **plasma membrane (GO:0005886) TAS Reactome (x13, FGFR1 signaling pathways)**: ERLIN2 is an ER membrane
  protein; plasma-membrane localization is an over-annotation from pathway bulk-membrane curation →
  MARK_AS_OVER_ANNOTATED.
- protein-containing complex (GO:0032991): generic → KEEP_AS_NON_CORE.
- protein binding (GO:0005515) IPI: uninformative → KEEP_AS_NON_CORE (TMEM41B interaction PMID:30352685 etc.).
- Do NOT over-claim catalytic MF: ERLIN2 is a scaffold/lipid-binding SPFH protein.
