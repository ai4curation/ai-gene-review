# Sur (DROME, Q9VL32) review notes

## Session 1 (create review)

- fetch-gene resolved Q9VL32 (SUR_DROME, FBgn0028675); 10 GOA rows.
- PMID:21690310 cached (abstract only in cache); full text read via PubMed MCP (PMC3216339).
  Gene names are stripped from the PMC text, but the abstract and figure legend identify dSUR as a
  qPCR-down-regulated candidate effector of Cdc42-Tinman with genetic interaction in the heart.
  Phenotype only; no NEW process term.
- PMID:16882722 and 23441090 abstract-only; PMC full text of 16882722 not retrievable.
- Decisions:
  - ABC-type transporter activity (IBA/IEA): MODIFY to potassium channel regulator activity,
    consistent with the human ABCC8/ABCC9 reviews. SUR proteins are channel regulators, no
    transported solute shown. Fly-specific support is oocyte electrophysiology and sulfonylurea
    pharmacology [PMID:10506204; PMID:15372035].
  - transmembrane transport (IBA/IEA): MODIFY to potassium ion transmembrane transport.
  - membrane (IEA): MODIFY to plasma membrane (already carried by IBA).
  - ATP binding, ATP hydrolysis: ACCEPT (Walker A in both NBDs, consensus NBD2 Walker B;
    see Sur-bioinformatics/RESULTS.md).
  - response to hypoxia IMP: KEEP_AS_NON_CORE (physiological knockdown phenotype).
  - NOT chitin biosynthetic process IMP: ACCEPT.
- Not added (NEW bar): heart contraction, sleep, defense response to virus, regulation of
  hormone secretion - all rest on RNAi/expression/pharmacology only.
