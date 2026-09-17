# Ntrk1 (TrkA) — *Heterocephalus glaber* (naked mole-rat), UniProt A0AAX6QC09

Research journal for the GO annotation review. Every assertion below carries provenance.
Quotes are verbatim substrings of the cited cached publication or of the UniProt record in
this folder.

---

## 1. What the entry itself is

- TrEMBL entry `A0AAX6QC09_HETGA`, 798 aa, `PE 3: Inferred from homology`, derived from RefSeq
  `XP_004871305.1`. Gene name `Ntrk1`. No experimental UniProt evidence of any kind.
- UniProt names it generically `Tyrosine-protein kinase receptor` with
  [file:HETGA/Ntrk1/Ntrk1-uniprot.txt "EC=2.7.10.1 {ECO:0000256|RuleBase:RU000312};"], and
  places it in
  [file:HETGA/Ntrk1/Ntrk1-uniprot.txt "Belongs to the protein kinase superfamily. Tyr protein"]
  kinase family, insulin receptor subfamily.
- The NTRK1-specific identity is nonetheless unambiguous from the domain signatures:
  [file:HETGA/Ntrk1/Ntrk1-uniprot.txt "DR   InterPro; IPR020461; NTRK1."] and
  [file:HETGA/Ntrk1/Ntrk1-uniprot.txt "DR   PANTHER; PTHR24416:SF370; HIGH AFFINITY NERVE GROWTH FACTOR RECEPTOR; 1."].
- Architecture from the feature table: signal peptide 1–33, LRR + two Ig-like domains
  extracellularly, a single TM helix
  [file:HETGA/Ntrk1/Ntrk1-uniprot.txt "FT   TRANSMEM        418..441"], and an intracellular
  protein-kinase domain
  [file:HETGA/Ntrk1/Ntrk1-uniprot.txt "FT   DOMAIN          512..783"].

### Sequence check of the catalytic and docking machinery

Method: residue positions read directly off the `SQ` sequence of
`genes/HETGA/Ntrk1/Ntrk1-uniprot.txt` (798 aa) and cross-checked against the `FT` lines of the
same file. No alignment was performed; no position is asserted from memory.

| Element | Position in A0AAX6QC09 | Observed | UniProt FT corroboration |
|---|---|---|---|
| Gly-rich / ATP pocket | 518–526 | `LKWELGEGA` | `FT   BINDING         518..526` (ATP) |
| β3 catalytic Lys | 546 | **K** | `FT   BINDING         546` (ATP) |
| HRD catalytic Asp | 650–652 (`HRD`), D at 652 | **D** | `FT   ACT_SITE        652` (proton acceptor) |
| DFG motif | 670–672 | `DFG` | — |
| Activation-loop Tyr pair | `DYYRVGG` at 681 → Y682/Y683 | **YY** | — |
| SHC1 docking Tyr (NPQY) | `NPQYFS` at 495 → Y498 | **Y** | `FT   SITE            498` (Interaction with SHC1) |
| PLCG1 docking Tyr | 793 | **Y** | `FT   SITE            793` (Interaction with PLCG1) |
| Position 774 | 774 | **C** (context `...MRGCWQREPQQR`**C**`SIKDVH...`) | — |

Two conclusions follow. (i) The complete catalytic apparatus of a receptor tyrosine kinase —
ATP site, β3 lysine, HRD aspartate, DFG motif, activation-loop tyrosine pair — and both
principal phosphotyrosine docking sites are intact in the naked mole-rat protein. (ii) The
cysteine at 774 is exactly what the primary literature reports for this species (see §2), so
this UniProt entry is the hypofunctional allele, not some divergent assembly artefact.

---

## 2. What the naked-mole-rat literature establishes about THIS protein

The decisive paper is Omerbašić et al. 2016, and we have its full text.

### 2a. The organismal phenotype it explains

Naked mole-rats do not develop NGF- or inflammation-induced heat hyperalgesia
[PMID:18232734 "But NGF also failed to produce heat hyperalgesia both acutely (<4 h) and
chronically (>24h)"]. Critically, the 2008 phenotype paper already ruled out simple receptor
loss: [PMID:18232734 "The lack of NGF-induced thermal hyperalgesia cannot be explained by a
lack of functional NGF receptors, because we were able to observe a robust stimulation of
neurite-growth in cultured small and medium sensory neurons that were also stained positive
for the NGF receptor TrkA"], with the effect seen at
[PMID:18232734 "In the presence of 500 ng/ml of NGF, sensory neurons elaborated extensive
neurites and the same cells were positive for the trk A receptor"].

**This is the single most important sentence in the whole dossier for GO purposes:** NGF
binds and signals through naked mole-rat TrkA well enough to drive neurite outgrowth in the
animal's own sensory neurons.

### 2b. The receptor is expressed on naked mole-rat nociceptors

[PMID:27732851 "Immunohistochemistry confirmed that IB4-negative sensory neurons are TrkA
positive in mouse and naked mole-rat"]; of cultured naked mole-rat sensory neurons the authors
[PMID:27732851 "found that 50% (34/68 cells) were TrkA positive"]. Independently confirmed in
2025: [PMID:40705105 "IB4 binding and TrkA expression also define largely distinct populations
in NMR DRG neurons"].

### 2c. The receptor was cloned; sequence divergence maps to the kinase domain

[PMID:27732851 "We cloned the naked mole-rat TrkA cDNA from mRNA isolated from sensory neurons
(nmrTrkA). The nmrTrkA sequence was identical to that predicted from the naked mole-rat genome
assembly"]. Alignment across 27 mammals showed
[PMID:27732851 "There was significant sequence divergence in the extracellular TrkA domains,
including the juxtamembrane NGF-binding domain; however, the intracellular sequences within
the kinase domain were highly conserved"] and, importantly,
[PMID:27732851 "All tyrosine residues important for receptor activation were conserved in all
the species, including the naked mole-rat."]

The species-specific change: [PMID:27732851 "There was just one amino acid change that appeared
to be unique to naked mole-rat, which was a leucine (rat) to cysteine substitution at position
774"] — matching the C at position 774 found in A0AAX6QC09 (§1). The overall claim is
[PMID:27732851 "Between one- and three-amino-acid substitutions in the kinase domain of the
naked mole-rat TrkA are sufficient to render the receptor hypofunctional, and this is
associated with the absence of heat hyperalgesia."]

**Note the numbering caveat.** The paper states position 774 with rat numbering as the
reference. That the naked mole-rat UniProt entry also carries a Cys at its own position 774 is
a coincidence of near-identical lengths (798 vs 799 aa), not something the paper asserts. Both
facts are recorded separately above; neither is inferred from the other.

### 2d. What "hypofunctional" was actually measured on

This is the crux for curation, so the assays are itemised precisely:

1. **Native nociceptors.** [PMID:27732851 "in naked mole-rat IB4-negative sensory neurons, NGF
   never sensitized TRPV1 currents"] (100 ng/mL NGF, 5 min). This is an *absence of TRPV1
   sensitisation*, not an absence of receptor function.
2. **Full-length nmrTrkA in oocytes at 100 ng/mL NGF.** [PMID:27732851 "the same NGF
   concentration produced a significantly smaller sensitization of TRPV1 currents in oocytes
   injected with nmrTrkA and ratTrpv1 cRNA"], with equal receptor protein
   [PMID:27732851 "Comparable amounts of rat and naked mole-rat TrkA protein were present in
   membranes isolated from X. laevis oocytes"]. So: *smaller*, not *absent*.
3. **Dose–response — the deficit is surmountable.** [PMID:27732851 "When oocytes were
   stimulated with 1,000 ng/mL NGF, activation of the naked mole-rat TrkA receptor produced a
   degree of sensitization similar to that observed with rat TrkA"], the authors concluding
   [PMID:27732851 "the naked mole-rat TrkA molecule is less efficient at initiating
   sensitization with NGF concentrations of ∼100 ng/mL"]. A right-shifted dose–response curve
   that reaches the wild-type maximum is the textbook signature of *reduced efficiency*, not
   *lost function*.
4. **The lesion is intracellular, not in ligand binding.** A chimera (rat ectodomain, naked
   mole-rat TM + kinase domain) reproduced the deficit — summarised by the later review as
   [PMID:32206859 "Indeed experiments using naked mole-rat TrkA and a chimeric TrkA
   (extracellular rat/intracellular naked mole-rat) further showed that activation of the naked
   mole-rat TrkA receptor is much less efficient at producing NGF-induced TRPV1 sensitization,
   thus indicating that the deficit lies in the intracellular domain"]. Consequently the
   possibility that human recombinant NGF simply binds the naked mole-rat ectodomain poorly was
   experimentally excluded as the explanation.
5. **Receptor autophosphorylation.** [PMID:27732851 "NGF stimulation triggered rapid
   phosphorylation of Tyr674/675 in rat TrkA, but not in chimeric TrkA"] — but in the same
   experiment [PMID:27732851 "the Tyr674/675 residues in both chimeric TrkA and rat TrkA
   displayed strong basal receptor phosphorylation in the absence of NGF"], which the authors
   attribute to overexpression-driven dimerisation. **The naked mole-rat kinase domain is
   therefore catalytically competent**; what is blunted is the *ligand-driven increment*.
6. **Downstream phospho-proteome.** NGF still upregulated a large phosphopeptide set through
   the naked mole-rat intracellular domain, just fewer of them:
   [PMID:27732851 "significantly more phosphopeptides were upregulated in NGF-treated cells
   with rat TrkA (361/2,239 [16.8%]) compared to cells with chimeric TrkA (270/2,007 [13.5%]"].
   Specific effectors: [PMID:27732851 "there was a stronger activation of specific
   phosphopeptides from Erk2 (MAPK1, pTyr-187) and Erk1 (MAPK3, pTyr-204)"] with rat TrkA;
   [PMID:27732851 "western blotting for phosphorylated Erk in HEK293 cells transfected with rat
   or chimeric TrkA after NGF stimulation revealed reduced levels of phospho-Erk protein after
   stimulation of the chimeric receptor"]; and
   [PMID:27732851 "We observed a stronger increase in the abundance of p38-α
   derived-phosphopeptides containing the pTyr182 residue after stimulation of rat TrkA
   compared to chimeric TrkA"].

   Every one of these is a **reduced**, not abolished, output. The naked mole-rat intracellular
   domain does couple NGF stimulation to ERK1/2 and p38α — less efficiently than rat.

### 2e. Development and survival outputs are preserved

[PMID:27732851 "It thus appears that the signaling capacity of the naked mole-rat TrkA is
sufficient to support the survival and functional development of sensory neurons during
embryonic development"], and
[PMID:27732851 "The maintained efficacy of the naked mole-rat TrkA receptor at very high NGF
concentrations is consistent with our previous observation that NGF (500 ng/mL) promotes
neurite outgrowth of both mouse and naked mole-rat sensory neurons in culture"].

There *is* a chronic in-vivo consequence, but it is postnatal and correlative:
[PMID:27732851 "a hypofunctional TrkA receptor in the naked mole-rat is associated with a
striking paucity of unmyelinated C-fibers in adult peripheral nerves"], while at P3
[PMID:27732851 "the number of unmyelinated C-fibers counted in cross-sections from the purely
cutaneous saphenous nerve and the mixed common peroneal nerve from naked mole-rats was between
2- and 3.5-fold higher than the number observed in adult nerves"]. The authors are explicit
that this is a postulate, and note the confound that the Mashona mole-rat shares two of the
three kinase-domain variants yet retains C-fibers.

### 2f. NGF signalling is not globally dead in the adult animal

[PMID:27732851 "NGF signaling in adult naked mole-rat is still capable of producing mechanical
hyperalgesia, a process that does not involve TRPV1"]. Two independent lines confirm the
narrowness of the defect: the naked mole-rat retains a functional purinergic pain pathway
(PMID:32478202) and its sensory neurons are still sensitised by artemin/GFRα3
[PMID:40705105 "This lack of NGF-induced neuronal sensitization and thermal hyperalgesia
results from hypofunctional signaling of the NGF receptor, tropomyosin receptor kinase A
(TrkA)."] — i.e. other sensitising pathways work, bounding what the TrkA deficit explains.

---

## 3. Curation consequences

### 3a. A quantitative signalling deficit does not abolish a GO molecular function

`GO:0004714 transmembrane receptor protein tyrosine kinase activity`,
`GO:0005030 neurotrophin receptor activity`, `GO:0043121 neurotrophin binding`,
`GO:0005524 ATP binding` and `GO:0038180 nerve growth factor signaling pathway` are all
**retained** in this species and should be `ACCEPT`ed:

- ligand binding is not the lesion (chimera experiment, §2d.4);
- catalytic competence is demonstrated by basal activation-loop autophosphorylation (§2d.5)
  and by an entirely intact catalytic apparatus in the sequence (§1);
- the receptor reaches rat-equivalent output at 1,000 ng/mL NGF (§2d.3);
- it drives neurite outgrowth in the animal's own neurons at 500 ng/mL (§2a).

`REMOVE` for any of these would be a category error: GO functions are qualitative capability
statements, and every one of these capabilities is positively demonstrated for the naked
mole-rat protein. The right place to record "less efficient at physiological NGF
concentrations" is `review.reason`, the `description`, and `suggested_experiments` — not the
action field.

### 3b. "No NGF-induced nociceptor sensitisation" is a phenotype, not a GO function

The organism-level observation is the *absence* of heat hyperalgesia and the *absence* of NGF
sensitisation of TRPV1. GO annotates what a gene product does, not what an animal fails to do.
There is no defensible GO term for "fails to sensitise TRPV1", and a `NOT` annotation would be
wrong too, because the receptor *does* sensitise TRPV1 — at 1,000 ng/mL NGF (§2d.3) — so the
negation is not qualitative. I have therefore written **no** annotation encoding the pain
phenotype, and instead recorded it as prose in `description` and as a `suggested_question`.

### 3c. The downstream BP terms, one by one

| Term | Does the naked-mole-rat evidence contradict, attenuate, or not address it? |
|---|---|
| `GO:0038180` NGF signaling pathway | **Attenuates.** Pathway operates; efficiency reduced at ~100 ng/mL. `ACCEPT`. |
| `GO:1990090` cellular response to NGF stimulus | **Confirms.** Neurite outgrowth in NMR neurons on NGF. `ACCEPT`. |
| `GO:0010976` positive regulation of neuron projection development | **Confirms, in this species.** [PMID:18232734, Fig. S2]. `ACCEPT`. |
| `GO:0031175` neuron projection development | Correct but the receptor's role is regulatory; `MODIFY` → `GO:0010976`. |
| `GO:0043524` negative regulation of neuron apoptotic process | **Attenuates.** Embryonic sensory-neuron survival is supported (§2e); a postnatal C-fibre deficit suggests the activity is weaker, not absent, and the apoptotic mechanism was never demonstrated. `ACCEPT` with caveat. |
| `GO:0051897` positive regulation of PI3K/AKT | **Does not address.** The 2016 proteomics measured ERK1/2 and p38α, never AKT/PI3K output. The only PI3K contact is a speculation: [PMID:27732851 "Tyrosine 751 has been implicated in binding of the p85 subunit of phosphoinositide 3-kinase"] combined with [PMID:27732851 "insertion of a cysteine for a leucine at position 774 in the naked mole-rat TrkA receptor may alter the efficiency of phosphorylation or recognition of the flanking"] tyrosines. That is a hypothesis about the branch most likely to be affected — not evidence for or against the annotation. `KEEP_AS_NON_CORE`. |
| ERK1/2 branch | **Measured, and reduced but present.** Not currently annotated; added as `NEW` (`GO:0070374`). |

### 3d. Why `GO:0070374` is added as NEW rather than left implicit

The 2016 SILAC/phosphoproteomics and the anti-phospho-ERK western are the only direct
measurements anywhere of what the *naked mole-rat* TrkA intracellular domain does downstream,
and they show ERK1/2 activation on NGF stimulation (reduced relative to rat, but present, §2d.6).
Leaving that unannotated would discard the one downstream branch this species has actual data
for while keeping the PI3K/AKT branch that it has none for. The caveat that the assay used a
rat-ectodomain chimera in HEK293 cells is recorded in the annotation's `reason`.

### 3e. Root-level and redundant parents

`GO:0000166` (nucleotide binding), `GO:0016740` (transferase activity), `GO:0016301` (kinase
activity), `GO:0004672` (protein kinase activity), `GO:0004713` (protein tyrosine kinase
activity), `GO:0016020` (membrane), `GO:0005770` (late endosome) and `GO:0007169` (cell surface
RTK signaling pathway) are all true, all uninformative, and all have a strictly more specific
sibling already present in the same GOA set. Each is `MODIFY`ed onto that specific term. None
is removed: they are not wrong, merely shallow.

### 3f. One label discrepancy, deliberately left asymmetric

`GO:0043235` appears in the review under two different labels, and this is intentional. GOA
and the live QuickGO record both call it **"signaling receptor complex"**, and that is the
label carried on the existing annotation, whose ids and labels are machine-sourced and must
not be rewritten. The repository's local ontology cache is a version behind and still calls it
**"receptor complex"**; `core_functions` term labels *are* hard-checked against that cache, so
the `in_complex` slot uses the older label to avoid a spurious validation warning. Same term,
same claim, two ontology releases.

### 3g. Validation status

`just validate HETGA Ntrk1` passes with **no errors** and one warning, deliberately left:
*"No annotations reference available deep research files."* Clearing it would require putting
the affinage record into an annotation's `supported_by` with a quoted sentence, which the
review brief explicitly forbids — a provider sentence is a lead, not evidence, and this
particular record is about the human orthologue. The affinage file is instead cited through
`additional_reference_ids` on the four annotations whose family-level basis it actually
supplies (early/late/recycling endosome membrane and PI3K/AKT), and assessed in full in
`references[].reference_review`. The warning is the correct outcome here, not a defect.

---

## 4. Assessment of the affinage human-ortholog record

`Ntrk1-deep-research-affinage-human-ortholog.md` is the Affinage record for **human NTRK1
(P04629)**, deliberately fetched as a conserved-mechanism baseline because Affinage refuses
non-human species.

**What it is good for.** An excellent, densely cited mechanistic map of the conserved receptor:
the D5/IgC2 NGF-binding hot spot, ordered bi-bi kinetics, Y490/Y785 docking, IRS-1/2 → p85-PI3K
recruitment, N-glycosylation gating surface delivery, STX8 Golgi→PM transport, GGA3/Arf6
recycling sustaining NGF-induced AKT, retrograde MVB-derived signalling endosomes, and
TRAF4/Nedd4-2 ubiquitin control. That corpus is what makes the endosome-membrane and
receptor-complex annotations in this GOA set credible as family-level transfers.

**What it decisively missed — and this is the recall observation.** The record contains **zero**
occurrences of "naked mole-rat", "Heterocephalus", or PMID:27732851 across all 34 citations.
It therefore misses, entirely: the hypofunctional allele, the L→C substitution at 774, the
right-shifted NGF dose–response, the reduced ERK1/2 and p38α coupling, and the whole reason
this gene is interesting in this species. This is not a defect of the provider — it is
human-only by construction — but it means the affinage record is **useless as the evidential
basis for any species-specific call here**, and every naked-mole-rat claim in this review is
anchored to PMID:27732851 / PMID:18232734 / PMID:32206859 / PMID:40705105 instead.

**One genuinely useful lead it did surface** (recorded as a lead, not as evidence, because the
paper is not in `publications/`): PMID:24623787, a knock-in mouse deleting the KFG
juxtamembrane element, which raises TrkA levels/activity and produces *enhanced thermal
sensitivity and inflammatory pain without changing DRG neuron numbers*. That is the exact
mirror image of the naked mole-rat: TrkA output up → thermal hyperalgesia up; TrkA output down
→ thermal hyperalgesia absent. It is a strong independent argument that TrkA signalling
*strength* is the rate-limiting variable for thermal hyperalgesia, which is precisely the
2016 paper's thesis.

**Do not import its `mechanism_profile` GO ids.** They collapse to coarse parents
(`GO:0140096`, `GO:0016740`, `GO:0140657`, `GO:0060089`, `GO:0048018`) — and one of them,
`GO:0048018 receptor ligand activity`, is flatly wrong for a receptor: TrkA is the receptor,
not the ligand. Every term in this review was grounded independently against QuickGO.

---

## 5. What I could not resolve

1. **NGF binding affinity of the naked mole-rat ectodomain was never measured.** The chimera
   experiment shows the ectodomain is not the *cause* of hypofunction, but no Kd, Scatchard, or
   SPR measurement on naked mole-rat TrkA exists. `GO:0043121 neurotrophin binding` is accepted
   on functional grounds (NGF-driven neurite outgrowth, and rat-equivalent sensitisation at
   1,000 ng/mL), not on a direct binding assay. Recorded as a `suggested_experiment`.
2. **PI3K/AKT output in naked mole-rat TrkA is entirely unmeasured** — see §3c. Kept, not core.
3. **The subcellular-trafficking annotations** (early/late/recycling endosome membrane, axon,
   receptor complex) have no naked-mole-rat evidence of any kind. They are ARBA / UniProt-SubCell
   / TreeGrafter transfers resting on the human/rat literature summarised in the affinage record.
   Nothing in the naked-mole-rat data contradicts them and the receptor is demonstrably surface-
   expressed and NGF-responsive, so they are kept as non-core rather than removed. If the L774C
   change altered receptor trafficking or turnover this is exactly where it would show, and no
   one has looked.
4. **Whether the adult C-fibre loss is apoptotic** is not established — the 2016 paper says
   "postulate". So `GO:0043524` is accepted on the conserved neurotrophic-survival function plus
   the explicit statement that embryonic survival is supported, not on the C-fibre data.
5. **Which of the one-to-three kinase-domain substitutions is causal** is unresolved by the
   paper itself; no single-variant reversion experiment was done.
