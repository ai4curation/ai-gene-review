# MTCH2 (Q9Y6C9) review notes

Gene: MTCH2 (mitochondrial carrier homolog 2; synonyms MIMP, HSPC032). Human.
UniProt Q9Y6C9, 303 aa. Paralogue: MTCH1 (Q9NZJ7) — reviewed separately in
`genes/human/MTCH1/MTCH1-ai-review.yaml`; the two reviews are written to agree.

## 2026-09-17 update

This file was created as part of an update that folded four papers postdating the
previous version of the review into it: PMID:42308315 (Sci Adv 2026, structure),
PMID:42056306 (Nat Struct Mol Biol 2026, BAX/BAK), PMID:41044057 (Nat Commun 2025,
CPT1) and PMID:40704594 (J Cell Sci 2025, yeast MIM complementation).

## 1. Core molecular function: outer-membrane protein insertase

Established by Guna et al. 2022 with genome-wide CRISPRi, in vitro insertion into
mitochondria from knockout cells, and reconstitution of purified protein into
proteoliposomes
[PMID:36264797 "Cumulatively, the requirement for MTCH2 in vivo and in vitro for TA
insertion, together with its reconstituted insertase activity and physical association
with substrates, rigorously establishes MTCH2 as an insertase for α-helical mitochondrial
outer membrane proteins."]. Substrate range is alpha-helical and broad
[PMID:36264797 "MTCH2’s role also appears to extend to the integration of a broader class
of α-helical proteins into the outer membrane, including signal anchored and multipass
proteins."]; beta-barrels are not MTCH2 substrates.

### Structural mechanism (new)

[PMID:42308315 "We demonstrate that MTCH2 is the defining member of a large family of
mitochondrial outer membrane (OM) insertases."]

[PMID:42308315 "The cryoelectron microscopy structure of the 33-kilodalton human MTCH2
revealed that evolution of its insertase activity required loss of a transmembrane helix,
which created a lipid-accessible hydrophilic groove stabilized by its unique, structured C
terminus."]

[PMID:42308315 "Comparison with the UCP1 structure definitively indicated that unlike a
canonical SLC25, MTCH2 contained only five TMs"]

[PMID:42308315 "we have experimentally shown that MTCH activity relies on a conserved
hydrophilic groove within the bilayer, produced by loss of a TM and stabilized by
evolution of a conserved C-terminal domain"]

This settles the long-running topology disagreement (five TMs, not six) and gives the
activity a physical basis — a groove that lowers the barrier to moving a soluble domain
across the bilayer — rather than leaving "insertase" as a phenotypic label.

## 2. The carrier question: name asserts what nobody has shown

**GOA carries no transporter molecular-function term for MTCH2.** The only MF terms in
`MTCH2-goa.tsv` are GO:0032977 (membrane insertase activity, IDA) and GO:0005515 (protein
binding, IPI x3). That absence is the correct and defensible position.

However, the name "Mitochondrial carrier homolog 2" and the UniProt record push the other
way: `KW Transport` and `DR TCDB; 2.A.29.25.2; the mitochondrial carrier (mc) family`
[file:human/MTCH2/MTCH2-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29)
family."]. UniProt's GO cross-references also include an Ensembl-derived
GO:0042775 (mitochondrial ATP synthesis coupled electron transport) that does not appear
in the QuickGO GOA file.

The structural work argues the transport machinery is gone, not merely unused
[PMID:42308315 "However, they have also lost several transporter elements, such as the
characteristic salt bridges between helices, important for the alternating access mechanism
used for solute transport."] and, importantly, restoring them does not help insertion
[PMID:42308315 "Mutations restoring these salt bridges do not reduce MTCH2’s function"].

No transport assay on purified MTCH2 has ever been published, positive or negative, so
"transport lost" is an inference from structure. Recorded as a `knowledge_gap` and a
`suggested_experiment` rather than asserted. This matches how the MTCH1 review handles the
same question.

## 3. Apoptosis: NOT downstream of the insertase activity

The previous version of this review assumed the apoptotic role was secondary to insertion
("Apoptotic role may be secondary to its insertase activity"; "Likely downstream of
insertase function"). **That assumption is refuted.**

[PMID:42056306 "we map the protein environment of the apoptotic pore using in situ
proximity labeling and identify the mitochondrial carrier homolog protein MTCH2 localizing
nearby BAX and BAK assemblies specifically under apoptotic conditions"]

[PMID:42056306 "The effect of MTCH2 on BAX and BAK oligomerization is independent of its
protein insertase activity."]

Three separate controls make that stick:

1. Insertase-dead mutant [PMID:42056306 "As an alternative approach, we generated the D189R
   mutant reported to abolish MTCH2 insertase activity23 and cotransfected it or wt MTCH2
   with GFP–BAX in MTCH2-KO U2OS cells"].
2. Paralogue control [PMID:42056306 "Furthermore, we found that MTCH1, a paralog of MTCH2
   with insertase activity23, had no effect on GFP–BAK foci growth in ΔBAK U2OS cells
   stably expressing GFP–BAK"].
3. Lipid rescue, pointing at the mechanism
   [PMID:42056306 "Together, these results suggest that it is not the protein insertase
   activity of MTCH2 but its function associated with lipid metabolism that may promote the
   high-order assembly of BAX and BAK during apoptosis."].

The authors are appropriately hedged about how absolute this is
[PMID:42056306 "Altogether, these data indicate that, while the insertase activity of MTCH2
might have a role, it is not essential for the effect of MTCH2 on the regulation of BAX and
BAK high-order oligomers."].

It is also distinct from the older tBID-recruitment role
[PMID:42056306 "Together, these results show that MTCH2 also has a direct effect on BAX and
BAK function independent of its function on tBID recruitment."], and it has downstream
consequences beyond cell death
[PMID:42056306 "MTCH2 depletion decreases not only apoptosis sensitivity but also sublethal
mitochondrial permeabilization during bacterial infection, mitochondrial DNA release into
the cytosol and cGAS-STING activation under impaired caspases."].

**Curation consequence.** GO:0043065 stays `KEEP_AS_NON_CORE`, but for a different reason
than before: not because it is a knock-on effect, but because it is a regulatory biological
process whose *molecular function* is undefined. There is nothing to put in
`core_functions.molecular_function` for it. Recorded as a `knowledge_gap` (MF_DARK).

## 4. Lipid metabolism: a real mechanism, not just a knockout phenotype

[PMID:41044057 "mitochondrial carrier homolog 2 regulates mitochondrial influx of free
fatty acids by modulating the sensitivity of carnitine palmitoyltransferase 1 to
malonyl-CoA through direct physical interaction"]

[PMID:41044057 "Adipocyte-specific ablation of mitochondrial carrier homolog 2 improves
mitochondrial function and whole-body energy expenditure, independent of uncoupling protein
1."]

This upgrades GO:0055088 (lipid homeostasis) from an unexplained ortholog-transferred
phenotype to a role with a named partner. It is still kept non-core: whether the CPT1
effect survives an insertase-dead MTCH2 has not been tested, so it cannot yet be called a
separate activity. Note the thematic convergence with the LPA/MFN2 fusion axis and the
LPA rescue of BAX/BAK assembly — three phenotypes all pointing at MTCH2 and mitochondrial
lipid handling.

## 5. MTCH1 vs MTCH2 and the yeast complementation asymmetry

[PMID:40704594 "Remarkably, MTCH1, but not MTCH2, was able to complement the growth defects
associated with the loss of Mim1 and Mim2."]

This is awkward for a framing in which MTCH2 is *the* insertase, but it does not contradict
MTCH2 insertase activity. The authors attribute the failure to toxicity and mislocalisation
in yeast, not to inactivity:

[PMID:40704594 "In contrast, in mim1Δ cells, most of the MTCH2–HA signal was detected in the
endoplasmic reticulum (ER), with a smaller fraction localized to mitochondria."]

[PMID:40704594 "These results indicate that the cellular toxicity of MTCH2 is dose dependent
and although lower expression improves viability, MTCH2–HA is still unable to complement the
absence of Mim1 as effectively as MTCH1–HA or Mim1 itself."]

MTCH2's insertase activity rests on reconstitution with purified protein in proteoliposomes,
which a heterologous yeast growth assay simply does not address. Conversely, MTCH1 partially
rescues MTCH2 loss in human cells
[PMID:42308315 "we observed that MTCH1 could partially rescue loss of MTCH2 for several
α-helical OM substrates"]. The honest reading: both paralogues are insertases, they are
partially redundant, and they are not interchangeable in every host — which is exactly how
the MTCH1 review reads it too.

## 6. Annotation actions changed in this update

| Term | Before | After | Why |
|---|---|---|---|
| GO:0005739 mitochondrion (IBA, HTP) | MARK_AS_OVER_ANNOTATED | ACCEPT | A correct parent of a correct location; node placement not in dispute. Matches MTCH1. Also clears the missing-`propagation_review` warning. |
| GO:0016020 membrane (IBA) | MARK_AS_OVER_ANNOTATED, no metadata | same action + `propagation_review` | WITH/FROM inspected: MGI:1929260, PANTHER:PTN001324730, UniProtKB:Q9Y6C9. Granularity objection only. MTCH2's own appearance in its own WITH/FROM is expected, not circular. |
| GO:0005515 protein binding (IPI x3) | REMOVE | MARK_AS_OVER_ANNOTATED | Project guidance; these are experimental interaction records. Matches MTCH1. |
| GO:0043065 positive regulation of apoptotic process | KEEP_AS_NON_CORE ("downstream of insertase") | KEEP_AS_NON_CORE (reason rewritten) | Insertase-independence established; kept non-core only because the MF is undefined. |
| GO:0055088 lipid homeostasis | KEEP_AS_NON_CORE ("pleiotropic") | KEEP_AS_NON_CORE (reason rewritten) | Direct CPT1 interaction supplies a mechanism. |
| GO:0010635 regulation of mitochondrial fusion | KEEP_AS_NON_CORE ("MFN insertion") | KEEP_AS_NON_CORE (reason rewritten) | Published mechanism runs through MFN2 and LPA, not through inserting the fusion machinery. |
| GO:7770059 alpha helical protein insertion into OM | absent | NEW | MTCH1 already carries it; the substrate restriction is exactly what was shown for MTCH2. |
| GO:0005515 (PMID:32296183, P56378-2) | missing from review | added | Second GOA row that had been omitted. |
| GO:0005634 nucleus (HDA) | REMOVE | REMOVE (unchanged) | Sperm-nucleus fraction; mitochondrial carry-over. Left alone — the new literature does not bear on it. |

Also fixed: five `supporting_text` entries attributed to the Falcon deep-research file were
paraphrases beginning "Falcon synthesis supports…" and appear nowhere in that file. They
have been replaced with verbatim quotations.

## 7. Open questions

Carried into `suggested_questions` / `suggested_experiments` / `knowledge_gaps`:

1. Should the "Transport" keyword and the "carrier homolog" name be retired, or is transport
   merely unassayed?
2. What is the molecular function behind the BAX/BAK effect — lipid scrambling, lipid
   transfer, something else?
3. Why does MTCH1 but not MTCH2 complement the yeast MIM complex; do the paralogues have
   non-identical substrate ranges in human cells?
4. Is the CPT1 effect separable from insertase activity?
