# G9JWI6 (NvDelta, Nematostella vectensis) — curation notes

## Identity

- UniProt G9JWI6 (unreviewed, TrEMBL), gene name `delta`, "Delta-like protein", 613 aa,
  EMBL AEW42992.1, sequence from Marlow et al. 2012 (PMID:22155407).
- Accession was chosen by UniProt REST search (organism_id:45351, Pfam PF01414 DSL); it is the
  only Nematostella DSL protein with the MNNL + DSL + EGF + TM architecture that is named `delta`
  and linked to the Marlow 2012 paper. Other DSL proteins in the proteome (A7SHY0, A7SHX3,
  A7RML5, Rdsl1 G9JWJ5, Rdsl2 G9JWJ4, several NEMVEDRAFT fragments) are paralogous DSL
  proteins / gene-model fragments and were not reviewed.
- Domains (UniProt features): signal peptide 1-39, MNNL (Notch_ligand_N, PF07657/IPR011651),
  DSL 179-223, EGF-like repeats 225-404, TM 442-463, cytoplasmic tail 464-613.
- PANTHER: PTHR24049 (CRUMBS FAMILY MEMBER) / PTHR24049:SF30 (no subfamily name).

## Literature

- Marlow et al. 2012 identified the single Delta gene: [PMID:22155407 "we were able to confirm
  one of these genes to be the Delta ligand. NvDelta possessed all characteristic domains of
  bilaterian Delta or Serrate notch ligands: a DSL domain, EGF repeats and a transmembrane domain"]
- Expression: salt-and-pepper ectodermal cells, then tentacle ectoderm and mesenteries
  [PMID:22155407 "At metamorphosis, Nvdelta is restricted to tentacular ectoderm and the
  endodermal component of the developing mesenteries."]
- Layden & Martindale 2014 (EvoDevo): Delta overexpression suppresses NvashA, and the suppression
  is DAPT-sensitive (Notch-dependent); Delta MO phenocopies Notch MO.
  [PMID:25705370 "This demonstrates that NvNotch and NvDelta are both required to repress NvashA in
  the embryonic ectoderm."]; [PMID:25705370 "To determine if the suppression of NvashA by Nvdelta
  required NvNotch, we treated Nvdelta:venus injected animals with DAPT."]
  Delta overexpression did not induce Nvhes genes [PMID:25705370 "Similarly, injection of the
  Nvdelta:venus mRNA failed to induce expression of any of the Nvhes genes."] — this is the basis
  for the "non-canonical (Su(H)/Hes-independent)" interpretation, which Richards & Rentzsch 2015
  partly dispute [PMID:26443634 "current data do not allow for a definitive conclusion on the
  mechanism of signalling in Nematostella neurogenesis."]
- Feedback: DAPT increases NvDelta expression [PMID:26443634 "NvDelta is also increased, whereas
  NvHes2 and NvHes3 are downregulated."]
- Germ-layer boundary role (2025): delta in mesoderm vs notch in ectoderm; endoderm induced at the
  interface [PMID:40858588 "Finally, we show that endodermal fate is induced in a single row of
  cells at the interface between the Notch-expressing ectoderm and the Delta-expressing mesoderm."]

## Assessment

- Core role: membrane-bound DSL ligand that activates NvNotch in trans (lateral inhibition of
  neural/cnidocyte differentiation; lateral induction of endoderm at the mesoderm boundary).
- No direct biochemical binding assay exists for NvDelta–NvNotch; `Notch binding` rests on
  domain architecture (MNNL + DSL = receptor-binding module) plus Notch-dependent gain-of-function.
- "Secreted"/extracellular region IEA is inconsistent with the single-pass TM architecture.

## Deep research

- `just deep-research-falcon NEMVE G9JWI6 --alias delta --fallback perplexity-lite` launched
  2026-09-30; see status in the report. Review based on cached full-text publications above.
