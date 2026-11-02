# glpK literature and function notes

- GlpK is the E. coli K-12 glycerol kinase, an FGGY-family
  ATP:glycerol 3-phosphotransferase that phosphorylates imported glycerol to
  sn-glycerol 3-phosphate. The glpK22 paper explicitly identifies
  "Escherichia coli glycerol kinase (EC 2.7.1.30; ATP:glycerol
  3-phosphotransferase)" as central to glucose control of glycerol metabolism
  [PMID:8631672].

- The accepted core pathway role is the GlpF-GlpK-GlpD glycerol catabolic
  route: GlpK performs the ATP-dependent trapping step after GlpF-mediated
  glycerol entry, and the product sn-glycerol 3-phosphate feeds the GlpD
  dehydrogenase reaction.

- Glycerol kinase activity is subject to carbon-source control. Unphosphorylated
  EIIA-Glc binds GlpK and inhibits it; Novotny et al. report that "Binding of
  enzyme IIIglc to glycerol kinase is also pH dependent" [PMID:2985549]. The
  follow-up glpK22 study connects loss of allosteric inhibition to loss of
  glucose control of glycerol utilization in vivo [PMID:8631672].

- The zinc-binding signal is regulatory-interface evidence, not evidence that
  free GlpK is a zinc metalloenzyme. Feese et al. found that the IIIGlc-GlpK
  complex creates an intermolecular Zn(II) binding site in which GlpK supplies
  one ligand [PMID:8170944].

- Cytosol is the expected site of GlpK action. Multiple proteomic studies
  assayed E. coli cytosolic fractions or cytosolic native complexes
  [PMID:15911532; PMID:16858726; PMID:18304323].

- PMID:8432702 fetched as abstract-level OpenAlex text and still does not
  expose the localization evidence behind its cytosol row. PMID:13930693 and
  PMID:5335908 have only bibliographic metadata. Rows that depend uniquely on
  those papers were left `UNDECIDED` rather than cited without inspectable
  evidence unless the core glycerol kinase claim was independently supported by
  later literature.
