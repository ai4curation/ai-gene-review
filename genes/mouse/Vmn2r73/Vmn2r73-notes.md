# Vmn2r73 (A0A3B2WCZ5): evidence and exact-input prediction review

The domain-containing name is supported, but the glutamate GPCR function paragraph assigns autonomous membrane signaling to a product lacking the required seven-transmembrane module.

## Input identity and functional boundary

A0A3B2WCZ5 is 496 residues, compared with the 851-residue Vmn2r73 reference D3Z7M3 linked to the same MGI gene. The first 429 residues are identical. A later 43-residue segment retains 41 identities, but the complete reference seven-transmembrane region is absent. Sparse matches in a global alignment of the alternative tail do not constitute a transmembrane module. The signal peptide and ligand-binding domain are retained.

## Biological evidence

- [PMID:30675062 — Structural insights into the activation of metabotropic glutamate receptors.](https://pubmed.ncbi.nlm.nih.gov/30675062/): Class C receptor signaling requires a seven-transmembrane module distinct from the extracellular ligand-binding region; the experimental study concerns mGlu5 rather than Vmn2r73.

> the GPCR-defining 7TM domain

- [PMID:9288755 — A novel family of putative pheromone receptors in mammals with a topographically organized and sexually dimorphic distribution.](https://pubmed.ncbi.nlm.nih.gov/9288755/): The founding rat V2R study identifies a receptor family related to, but distinct from, metabotropic glutamate receptors.

> genes encoding seven transmembrane receptors with sequence similarity with
> Ca2+-sensing and metabotropic glutamate receptors

## Exact non-GO claims

The complete emitted record is preserved in [Vmn2r73-protnlm-source.json](Vmn2r73-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Receptor ligand binding region domain-containing protein

CNN (CS 2). The wording identifies the retained receptor ligand-binding region without claiming that an intact GPCR or a particular ligand specificity is present. The exact sequence retains this annotated domain in the same-gene reference.

### Function

> G-protein coupled receptor for glutamate. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of down-stream effectors. Signaling inhibits adenylate cyclase activity

NPI (CS 0). The compound claim requires an autonomous G-protein-coupled receptor, whereas the exact input lacks the seven-transmembrane signaling module. The extracellular class C fold also does not establish glutamate specificity or inhibition of adenylate cyclase. The emitted donor accession is Q14833; it does not substitute for domain completeness in the target. [Sequence analysis](Vmn2r73-bioinformatics/RESULTS.md); [class C signaling study](https://pubmed.ncbi.nlm.nih.gov/30675062/).

No GO or EC term was emitted in this record; the name, function and location assessments above constitute its prediction review.

## Family integration

V2R family membership and retention of its ligand-binding region are separable from an intact class C receptor architecture. A partial gene product can preserve family identity while losing the domain needed for the ancestral activity. Neither the V2R designation nor similarity to glutamate receptors establishes the ligand of this particular product.

## Evidence limits

No assay or localization study of the exact 496-residue product was found. The genuine Falcon report describes conventional seven-transmembrane receptor biology but does not account for this input sequence boundary; its full-length signaling conclusions cannot be transferred. The 1997 V2R publication is abstract-only in the cache. Stable expression and any accessory role of the shortened product remain unresolved.

Exact sequence mapping: [Vmn2r73-bioinformatics/RESULTS.md](Vmn2r73-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This entry was written during a re-review that deliberately ignored the ProtNLM2 predictions; the earlier sections above, including the ProtNLM2 claim assessments, are retained unchanged.

### 2026-10-20 full re-review

#### Product identity

- A0A3B2WCZ5 is 496 aa, Ensembl ENSMUSP00000156768 / transcript ENSMUST00000232965
  (Vmn2r73-203), **not** the Ensembl canonical transcript. The canonical product is
  ENSMUSP00000076687 (ENSMUST00000077478, Vmn2r73-201; 851 aa), UniProt D3Z7M3. Eight
  UniProt TrEMBL entries exist for the locus (475-851 aa) (Ensembl REST lookup; UniProt
  search `gene_exact:Vmn2r73`).
- Re-ran a reproducible global alignment that reads the target sequence from the UniProt flat
  file and the canonical sequence from `Vmn2r73-same-gene-reference.json`
  [file:mouse/Vmn2r73/Vmn2r73-bioinformatics/RESULTS.md "| 1-429 | 1-429 | 429 |"].
  Residues 1-429 are identical; the 9-Cys segment (ref 506-548) is retained at 430-472;
  the remaining 24 residues are a divergent tail. None of the seven reference TM helices is
  retained, and a Kyte-Doolittle 19-residue scan finds no hydrophobic window except the
  signal peptide.
- Conclusion: an alternative-transcript product encoding a soluble ectodomain (signal
  peptide + VFT + NCD), missing the entire 7TM signaling module. It is an isoform of the
  gene in this folder, not a different gene.

#### Evolutionary placement

- PANTHER PTHR24061 (CALCIUM-SENSING RECEPTOR-RELATED), subfamily SF413 "VOMERONASAL 2,
  RECEPTOR 66-RELATED". UniProt search for SF413 members returns only rodents (Mus, Rattus,
  Peromyscus, Neotoma, Apodemus, hamsters, jerboa, vole); mouse members are Vmn2r66-Vmn2r79,
  i.e. a rodent-specific family-A V2R expansion. No member of SF413 has experimental data
  and no SF413 member has an IBA/PAINT annotation in GOA for this product.
- Nearest characterised V2Rs are in different subfamilies: Vmn2r116 (E9Q6I0, SF398; ESP1
  receptor), Vmn2r26 (Q6TAC4, SF536), Vmn2r1 (O70410, SF546, family C). Global identity of
  canonical Vmn2r73 to them is 47.6%, 36.8% and 29.6% respectively (scratch alignment,
  consistent with Vmn2r116 being the closest characterised family-A relative). Because they
  are in different PANTHER subfamilies, their ligands (ESP1, MHC peptides) are not
  transferable.
- PANTHER family review `interpro/panther/PTHR24061/PTHR24061-review.yaml` places Vmn2r73 in
  SF413, consistent with UniProt; no disagreement. That review is centred on this truncated
  product.

#### Literature

- Falcon deep research: no Vmn2r73-specific ligand, localisation, signaling or knockout data;
  everything is V2R-family inference, and the report treats the canonical 7TM receptor.
- PMID:9288755 (abstract): V2Rs are "seven transmembrane receptors with sequence similarity with
  Ca2+-sensing and metabotropic glutamate receptors".
- PMID:30675062 (full text): class C "VFT is connected to the 7TM domain by means of the CRD,
  which provides a semi-rigid linker between the ligand binding and 7TM (signaling) domains".

#### Decisions

- GO:0004930 GPCR activity (IEA InterPro): REMOVE for this product (no 7TM).
- GO:0007186 GPCR signaling (IEA): MARK_AS_OVER_ANNOTATED (accessory role untested).
- GO:0005886 plasma membrane (ARBA SubCell "multi-pass") and GO:0016020 membrane (IEA):
  MARK_AS_OVER_ANNOTATED; product predicted soluble/secreted.
- No core functions asserted: nothing about this product's function is established.
- Previous version of this review and notes was built around a function-prediction
  evaluation; it was rewritten here independently of those predictions and the
  bioinformatics script was changed to take the target sequence from the UniProt record.

#### Modules

- No module in `modules/` covers vomeronasal receptors or V2R signaling.
