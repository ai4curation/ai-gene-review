# MIM1 (YOL026C / TOM13), *Saccharomyces cerevisiae* — research notes

UniProt: Q08176 · SGD: S000005386 · 113 aa, 12.8 kDa · single predicted TM helix (residues 39–62)
Pfam PF08219 (TOM13) · InterPro IPR013262 (OMP_MIM1/TOM13_mt) · PANTHER PTHR28241 / PTHR28241:SF1
ComplexPortal CPX-2281 (MIM mitochondrial import complex)

> **Provenance note.** All automated deep-research providers failed in this environment
> (falcon → HTTP 402 Payment Required; perplexity → provider not configured; openai →
> invalid API key), so no `MIM1-deep-research-<provider>.md` file exists. The notes below
> were assembled by hand from the cached publications in `publications/` and from the
> UniProt record. Every assertion carries an inline citation with verbatim supporting text.

---

## 1. Identity and discovery

`YOL026C` was independently named twice in 2004–2005:

- **Tom13**, in a screen for essential outer-membrane proteins of unknown function
  [PMID:15326197 "Tom13, the gene product of YOL026C"].
- **Mim1** (*mitochondrial import 1*), in a proteomic characterisation of the *Neurospora
  crassa* outer membrane whose 14.2 kDa hit was traced to the *S. cerevisiae* orthologue
  [PMID:15608614 "A protein of a molecular mass of 14.2 kDa (NCU01101.1) that had a high
  sequence similarity to Mim1 (mitochondrial import) from Saccharomyces cerevisiae (open
  reading frame YOL026C ) was identified."].

Mim1 is the accepted name; Tom13 survives as a synonym and as the Pfam family name. Note
that despite the "Tom13" name, **Mim1 is not a TOM-complex subunit** — see §3.

## 2. Localisation and topology

Mitochondrial outer membrane, integral, with the N-terminus facing the cytosol.

- Protease-protection and alkaline-carbonate extraction of isolated mitochondria place
  Tom13/Mim1 as an integral outer-membrane protein
  [PMID:15326197 "Tom13 and Tom38 are mitochondrial outer membrane proteins"].
- Independently confirmed by protease shaving of mitochondria carrying an N-terminally
  His-tagged allele: "Mim1 was degraded and could no longer be immunodecorated with
  antibodies against the His tag ( Fig 1E ). Hence, the N terminus of the protein is
  exposed to the cytosol." [PMID:15608614].
- The topology is cytosolic-N / IMS-C with one central α-helical TM segment
  [PMID:28916712 "The 13-kD protein Mim1 contains a predicted central α-helical
  transmembrane segment and exposes its N-terminal domain to the cytosol and its
  C-terminal domain to the intermembrane space"].

UniProt records `Mitochondrion outer membrane` with ECO:0000269 from both PMID:15326197
and PMID:15608614. This is one of the best-supported facts about the protein.

## 3. The MIM complex

Mim1 self-associates into an oligomer that is the bulk of a ~400–450 kDa complex, distinct
from both TOM and TOB/SAM:

- [PMID:15608614 "Mim1 was present in a high-molecular-mass complex of a molecular size of
  about 400–450 kDa, which is distinct from that of the TOM and TOB complexes."] and
  "Therefore, Mim1 is not a Tom or Tob component."
- [PMID:28916712 "Mim1 oligomers form the major constituent of the MIM complex"].

The second, low-abundance subunit is **Mim2** (Q3E798, ~10 kDa, same topology, 1–2 copies
per complex):

- [PMID:22467864 "Mim2 physically and\ngenetically interacts with Mim1, and both proteins
  form the MIM complex."] — this is the reference behind both the `GO:0140595 MIM complex`
  IPI annotations and the `GO:0005515 protein binding` IPI (WITH `UniProtKB:Q3E798`).
- [PMID:28916712 "A second subunit, the 10-kD protein Mim2, possesses the same topology as
  Mim1 yet is present in the MIM complex in lower abundance (one to two copies per
  complex; Dimmer et al., 2012)."]

`GO:0140595 MIM complex` is definitionally about exactly this: "A protein complex located
in the mitochondrial outer membrane that functions as an insertase, mediating the insertion
of alpha-helical proteins from the cytosol into the outer membrane."

## 4. Biological role — insertase for α-helical outer-membrane proteins

The MIM complex is the outer-membrane insertase for α-helically anchored precursors. Client
classes established over ~15 years:

| Client class | Examples | Reference |
|---|---|---|
| Multi-span α-helical | Ugo1, Om14, Scm4 | [PMID:21825073], [PMID:21825074] |
| Signal-anchored (N-terminal anchor) | Tom20, Tom70 | [PMID:17974559], [PMID:18187149] |
| Tail-anchored (C-terminal anchor) | subset | [PMID:32348752] |
| β-barrel, indirectly (late TOM assembly) | Tom40 | [PMID:15326197], [PMID:15608614] |

- [PMID:22467864 "Some of the single-span proteins and all known\nmultiple-span proteins
  are inserted into the membrane in a pathway that depends\non the MOM protein
  Mitochondrial Import 1 (Mim1)."]
- [PMID:32348752 "the mitochondrial import (MIM) complex\ninserts precursors of
  multi-spanning α-helical proteins"] and "We report that the yeast MIM\ncomplex promotes
  the insertion of proteins with N-terminal (signal-anchored) or\nC-terminal
  (tail-anchored) membrane anchors."
- The 2020 study concludes "the MIM complex\nis a major and versatile protein translocase
  of the mitochondrial outer\nmembrane" [PMID:32348752].

MIM also cooperates with the TOM receptor Tom70 to accept precursors — [PMID:32348752 "MIM
interacts with TOM to accept precursor proteins from\nthe receptor Tom70."] — and
UniProt records a direct Mim1–Tom70 interaction from [PMID:21825073].

## 5. Role in TOM complex assembly

This is the phenotype through which Mim1 was discovered, and it is largely a *consequence*
of the insertase activity acting on Tom20/Tom70 plus a late, less well-defined step in
Tom40 maturation.

- Depletion abrogates TOM assembly: [PMID:15608614 "Depletion of Mim1 abrogates assembly of
  the TOM complex"]; the block is downstream of TOB/SAM-mediated Tom40 insertion — "The
  steps in the assembly of the TOM complex requiring Mim1 are located after the
  TOB-complex-dependent insertion of Tom40 into the outer membrane."
- Independently: [PMID:15326197 "Depletion of Tom13 or Tom38 affects assembly of Tom40 and
  porin in the mitochondrial outer membrane in vitro."]
- Receptor specificity: [PMID:17974559 "We report that Mim1 is required\nfor efficient
  membrane insertion and assembly of Tom20 and Tom70, but not Tom22."] — Tom22, being
  tail-anchored and requiring pre-existing Tom receptors, is Mim1-independent here.
- Mim1 physically joins SAM: [PMID:17974559 "We show that Mim1 associates with SAM(core)
  components to a large SAM complex,\nexplaining its role in late steps of the assembly
  pathway of Tom40."], echoed in 2020 as "coupling of MIM and SAM\npromotes early assembly
  steps of TOM subunits" [PMID:32348752].
- Disruption phenotype (UniProt, ECO:0000269|PubMed:17974559): "Leads to reduced levels of
  TOM complex but retains the respiratory chain."

Importantly, the specificity is real, not a generic import collapse: β-barrel machineries
other than TOM are unaffected — [PMID:15608614 "The biogenesis of other outer membrane
complexes containing β-barrel proteins, such as TOB/SAM and porin complexes, was not
affected by the lack of Mim1."], and depletion does not impair import of matrix or inner
membrane clients (mtHsp60, AAC) [PMID:15326197 "Depletion of Tom13 or Tom38 does not affect
import of mtHsp60 or AAC into mitochondria in vitro."].

## 6. The channel activity (basis of GO:0022832) — read carefully

[PMID:28916712] screened yeast outer-membrane proteins for channel activity and reported
Mim1 as one of four new channels. The relevant measurements, verbatim:

- "Upon reconstitution into planar lipid bilayers, Mim1 exhibited a characteristic channel
  activity that was inhibited by Mim1-specific antibodies"
- "We observed a main conductance state of ΔG¯main=580 pS that closed upon application of
  high positive or negative voltages"
- "The Mim1 channel was cation selective with a ratio of PK+/PCl− of 23.5:1 based on a
  positive reversal potential of 53 mV"
- Co-reconstitution with Mim2 reduced selectivity to PK+/PCl− = 11:1 — the channel is
  MIM-complex-relevant, not an artefact of Mim1 alone.

Assessment for curation:

1. **The observation is solid.** Recombinant protein, antibody-inhibited, reproduced with a
   second expression system ("Mim1 synthesized in wheat germ lysate exhibited the same
   channel activity"), modulated by its physiological partner Mim2. SGD's IDA is warranted.
2. **The GO term is imprecise in two ways.** `GO:0022832 voltage-gated channel activity` is
   an unspecified-substrate voltage-gated channel term. The measured behaviour is (a)
   strongly **cation**-selective (23.5:1) and (b) voltage-dependent only in the sense that
   the pore *closes* at high |Vm| — the classic gating description for a protein-conducting
   channel (Tom40, Sam50, Mdm10 all behave this way), not for a signalling voltage sensor.
   `GO:0022843 voltage-gated monoatomic cation channel activity` is the substrate-correct
   child if an ion-channel framing is kept.
3. **The biological reading is protein conduction, not ion conduction.** The authors' own
   framing is "The mitochondrial import component Mim1 forms a channel that is predicted to
   have an α-helical structure for protein import." No physiological ion flux through Mim1
   has been demonstrated; the cation preference is shared with every known protein-import
   channel of this membrane, whose *in vivo* cargo is polypeptide. Treating GO:0022832 as
   MIM1's molecular function would misstate what the protein does.

Downstream consequence: the `GO:0055085 transmembrane transport` IEA (GO_REF:0000108) is
generated *logically* from GO:0022832 via an MF→BP inter-ontology link (WITH/FROM field is
literally `GO:0022832`). It inherits whatever imprecision GO:0022832 carries, and adds
nothing — "transmembrane transport" is far too general to describe MIM1 and does not capture
protein insertion.

## 7. What is missing from GOA

**No molecular function term describes what Mim1 actually does.** The only MF annotations
are `GO:0005515 protein binding` (uninformative by project convention) and `GO:0022832`
(imprecise, see §6). `GO:0032977 membrane insertase activity` — "Binds transmembrane
domain-containing proteins and mediates their integration into a membrane" — is an exact
description of the MIM complex's activity and is supported by [PMID:32348752],
[PMID:21825073] and [PMID:22467864]. It should be proposed.

Because insertase activity is delivered by the Mim1–Mim2 heterocomplex rather than Mim1
alone, `contributes_to` is the appropriate qualifier at the gene-product level.

## 8. Orthology / PANTHER

PANTHER PTHR28241 "MITOCHONDRIAL IMPORT PROTEIN 1", 1248 proteins across 2583 taxa, one
subfamily (SF1). The IBA annotations (GO_REF:0000033) for `GO:0140595` and `GO:0045040`
derive from node `PANTHER:PTN002000670`, and MIM1's own SGD annotation
(`SGD:S000005386`) appears in the WITH/FROM — i.e. *S. cerevisiae* Mim1 is itself one of
the experimentally characterised descendants the PAINT curator used to place the IBD. That
is expected and is a marker of experimental grounding, not circularity. The family is
fungal/eukaryote-restricted; the functional counterpart in higher eukaryotes (MTCH1/2)
lacks sequence homology and is a case of convergent evolution, which is why the family is
narrow.

## 9. Summary of curation judgements

| Term | Evidence | Judgement |
|---|---|---|
| GO:0140595 MIM complex (IPI ×2, IBA) | PMID:22467864, GO_REF:0000033 | ACCEPT — core |
| GO:0045040 protein insertion into MOM (IDA, IMP, IBA) | PMID:32348752, PMID:15608614, GO_REF:0000033 | ACCEPT — core BP |
| GO:0070096 MOM translocase complex assembly (IMP ×2) | PMID:15608614, PMID:17974559 | ACCEPT — core BP |
| GO:0005741 mitochondrial outer membrane (IDA ×3, IEA) | PMID:15326197, PMID:15608614, PMID:28916712 | ACCEPT — core CC |
| GO:0005515 protein binding (IPI) | PMID:22467864 | MARK_AS_OVER_ANNOTATED — uninformative; the real content is MIM complex membership |
| GO:0022832 voltage-gated channel activity (IDA) | PMID:28916712 | MODIFY → GO:0022843 (substrate-correct); flag that protein conduction, not ion conduction, is the physiological role |
| GO:0055085 transmembrane transport (IEA) | GO_REF:0000108 from GO:0022832 | REMOVE — uninformative logical by-product; misrepresents an insertase as a solute transporter |
| **GO:0032977 membrane insertase activity** | not annotated | **PROPOSE** (contributes_to) |
