# ATG1 (S. cerevisiae, P53104, YGL180W) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: ATG1 is being reviewed as the experimentally characterised reference
member of the PAINT Atg1/ULK node PTN000681272 (PANTHER PTHR24348, subfamily
PTHR24348:SF22 per the UniProt PANTHER cross-reference). No ProtNLM2 output was
consulted.

### Deep research

`just deep-research-falcon yeast ATG1 --fallback perplexity-lite` failed:
falcon returned "Edison API request failed: Failed to authenticate" (HTTP 403)
and the perplexity-lite fallback also failed. No deep-research file exists; the
review was built from the cached publications (34 PMIDs, 20 with full text) and
the UniProt record.

### Evolutionary grounding

- UniProt: PANTHER PTHR24348:SF22 (family PTHR24348
  "SERINE/THREONINE-PROTEIN KINASE UNC-51-RELATED"); InterPro IPR045269
  Atg1-like, IPR022708 Atg1-like_tMIT, Pfam PF12063/PF21127 (ATG1-like MIT1/2).
  "Belongs to the protein kinase superfamily. Ser/Thr protein kinase family.
  APG1/unc-51/ULK1 subfamily."
- PAINT (`interpro/panther/PTHR24348/PTHR24348-paint.tsv`): SGD:S000003148
  (ATG1 itself) is a seed for the PTN000681272 IBDs GO:0000407, GO:0005776,
  GO:0005829, GO:0016020, GO:0000045, for the PTN000681273 IBDs GO:0034727
  (sole seed), GO:0042594, GO:0061709, and for PTN002805221 GO:0004674 and
  GO:0005737. It is not a seed for GO:0010506 (regulation of autophagy),
  GO:0000423 (mitophagy) or GO:0034045 on those nodes. So every IBA on ATG1
  is backed by yeast experimental data except mitophagy and regulation of
  autophagy, and those are directly supported by yeast experiments anyway
  (PMID:19793921 for mitophagy; PMID:28821724, PMID:33536246 for regulation).
- For this gene, every core claim rests on experiments in S. cerevisiae
  itself. Nothing in this review is transferred from another species.

### Experimentally established in S. cerevisiae

- **Protein Ser/Thr kinase activity** (direct): in vitro autophosphorylation
  lost in kinase-dead D211A; consensus-motif peptide arrays; direct
  phosphorylation of Atg9 [PMID:24440502 "The multimembrane-spanning protein
  Atg9 is a direct target of this kinase essential for autophagy."]; of Atg4,
  which inhibits Atg4 [PMID:28821724 "Here we show that phosphorylation by Atg1
  inhibits Atg4 function"]; re-phosphorylation of Atg13 to end autophagy under
  long starvation [PMID:33536246 "termination is mediated by re-phosphorylation
  of Atg13 by the Atg1 protein kinase"]. Kinase activity is raised by
  starvation or rapamycin and by Atg13 binding [PMID:10995454].
- **Autophagosome formation**: required for autophagosome formation and
  autophagic vesicle accumulation [PMID:9190802, PMID:9224897]; the Atg1
  complex organises the PAS [PMID:18287526]; Atg1-Atg13-Atg17 complex tethers
  Atg9 vesicles in vitro [PMID:26753620]; the Atg8-binding AIM/LIR (aa 429-432)
  is needed for full autophagy and for Atg1 delivery into autophagosomes
  [PMID:22778255, PMID:22885598].
- **Kinase-independent role**: an analog-sensitive allele showed kinase
  activity is needed for Cvt transport of prApe1 but not for import via
  autophagy, so Atg1 also has a structural role in autophagosome nucleation
  [PMID:12589048]. Kinase activity is still needed for full Atg9-dependent
  autophagy [PMID:24440502], so the two findings fit a model in which some Atg1
  functions need catalysis and others do not.
- **Cvt pathway**: required [PMID:10995454, PMID:12589048].
- **Selective autophagy types (deletion phenotypes)**: mitophagy
  [PMID:19793921], reticulophagy/macro-ER-phagy [PMID:26181331], piecemeal
  microautophagy of the nucleus [PMID:18701704], late nucleophagy
  [PMID:22768199]. These are atg1-null phenotypes that the core
  autophagosome-formation machinery explains. They are true process
  memberships (Atg1 works in the autophagosome-forming step of each), but they
  are not separate Atg1 functions.
- **Location**: cytosol [PMID:9190802]; PAS [PMID:11689437, PMID:15659643,
  PMID:18497569]; isolation membrane and vacuole-IM contact site
  [PMID:23549786]; autophagosomes via Atg8 [PMID:22885598].
- **Complex**: Atg1-Atg13-Atg17-Atg29-Atg31 [PMID:15743910, PMID:24793651,
  PMID:26753620].

### Points of care for transfer to relatives

- The kinase-independent scaffold role and the Cvt pathway are yeast/fungal
  findings. The Cvt pathway is restricted to a fungal clade (GO:0032258 taxon
  constraint NCBITaxon:147537), so do not transfer it outside Saccharomycotina.
- The Atg13/Atg17 binding mode via tandem MIT domains [PMID:24793651] needs the
  C-terminal MIT domains (Pfam PF12063/PF21127). Check that a relative has
  them before transferring complex membership.
- Specific substrates (Atg9, Atg4, Atg13) are yeast-established. Atg9
  phosphorylation is conserved to ULK1 per the authors, but this has to be
  checked case by case.

### Action decisions (summary)

- GO:0034045: QuickGO reports it obsolete ("Annotations should be moved to
  phagophore membrane (GO:7770114) ... or ... GO:0000407 ... GO:0061908");
  OLS and the local go.db still list it as active (a known disagreement
  between GO services). Both rows were set to MODIFY → GO:0000407 / GO:0061908,
  which the gene already carries by IDA.
- All bare GO:0005515 rows were set to REMOVE under the protein-binding policy.
  The one exception is the Atg8 row (PMID:22885598, P38182), which was set to
  MODIFY → GO:0032182 ubiquitin-like protein binding (direct LIR-dependent
  binding of Atg8).
- Broad terms (protein kinase activity, autophagy, response to starvation,
  autophagy of mitochondrion) were set to MODIFY toward the specific supported
  descendants.
- No NEW annotations were added.
