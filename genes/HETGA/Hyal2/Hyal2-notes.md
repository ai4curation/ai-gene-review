# Hyal2 (naked mole rat, *Heterocephalus glaber*) — review notes

UniProt **A0A0P6J1Y4** (TrEMBL, unreviewed), 471 aa, `PE 3: Inferred from homology`.
NCBI taxon 10181. GOA: **45 annotations, all electronic** — mostly `GO_REF:0000107`
(Ensembl Compara orthology projection from human HYAL2 `Q12891` and mouse Hyal2
`O35632`), plus `GO_REF:0000120` (combined ARBA/UniRule/PANTHER), one `GO_REF:0000108`
(inter-ontology inference), and InterPro2GO/UniRule for the carbohydrate term.
There is **no experimental annotation** on this protein and no NMR-specific GO
annotation of any kind.

---

## 1. What the protein is

The NMR record is a straightforward GH56 hyaluronidase-2 ortholog. UniProt places it
in the family — `-!- SIMILARITY: Belongs to the glycosyl hydrolase 56 family.`
[file:HETGA/Hyal2/Hyal2-uniprot.txt] — assigns `EC=3.2.1.35`, and gives the canonical
HYAL2 topology: `SIGNAL          1..20`, `CHAIN           21..471`,
`-!- SUBCELLULAR LOCATION: Cell membrane` with `Lipid-anchor, GPI-anchor`, and
`-!- SUBUNIT: Interacts with MST1R.` InterPro/PANTHER place it at
`PANTHER; PTHR11769:SF6; HYALURONIDASE-2; 1.`

**The catalytic machinery is intact.** UniProt annotates `ACT_SITE        135` with
`/note="Proton donor"`, and residue 135 of the deposited sequence is the glutamate of
the strictly conserved GH56 `DWEHW` motif (positions 133–137 read D-W-**E**-H-W). All
five PIRSR disulfides (47–339, 211–227, 364–375, 369–426, 428–437) are annotated as
present. Nothing in the sequence record suggests a pseudo-enzyme.

For orientation, PMID:38052795 describes the same architecture: *"HYAL2 is a highly
post-translationally modified enzyme. The first 20 amino acids of HYAL2 are predicted
to be a signal sequence that directs the protein to the endoplasmic reticulum35. In
the endoplasmic reticulum, HYAL2 is glycosylated and trimmed to the mature protein
(residues 21–448) with the addition of a glycophosphatidylinositol (GPI) anchor onto
Gly44835."*

Conserved role in the two-step HA catabolic pathway
[PMID:33846452 *"The principal somatic HA-depolymerizing enzymes, i.e. hyaluronidases,
are HYAL1 and HYAL2. HA is degraded at the cell surface by the
glycosylphosphatidylinositol (GPI)-linked HYAL2 into intermediate-size fragments."*;
PMID:38052795 *"HYAL2 hydrolyzes HMM-HA into intermediate length HA1,23, and HYAL1
further degrades small molecules of HA into tetrasaccharides24."*].

---

## 2. The central question: is NMR Hyal2 inactive, weaker, or just scarcer?

The brief's framing matters because the three answers imply different actions. The
answer the literature supports is **"active, modestly weaker, and normally expressed"**.

### 2a. Active — the NMR protein has been cloned and assayed

This is the decisive result and it is easy to miss, because the paper is titled for a
phenotype, not for the gene. PMID:38052795 (Nat Commun 2023) cloned NMR HYAL2 —
*"For overexpression, the coding sequences (CDS) of HAS2, HYAL1, and HYAL2 genes from
mouse, BMR, Shrew, and SNM as well as HYAL2 of NMR were cloned into a piggyBac
vector."* — and tested a NMR/DMR-specific substitution:

> *"A positively selected site G284 was also identified in NMR and DMR HYAL2 (Fig. 3c).
> We tested the effect of this mutation on NMR HYAL2. We did not observe difference
> when HA was incubated for two days, but the size and amount of HA was smaller after
> three days of incubation (Fig. 5i), suggesting that the substitution in G284 also
> contributes to the weaker HYAL2 in NMRs."* [PMID:38052795]

Read carefully: the experiment is **wild-type NMR HYAL2 vs. the G284A revertant**, and
the revertant leaves *smaller* HA. Both constructs degrade HA. So wild-type NMR HYAL2
is a functioning hyaluronidase whose activity the ancestral residue would increase.
The substitution arose in the NMR/DMR ancestor
[PMID:38052795 *"Interestingly, an amino acid replacement A284G occurred in the ancestor
of NMR and DMR that overlapped with the strongest positive selection sites A284K
identified in SNM and EM (Fig. 3c)."*] and lies in the catalytic domain
[*"All the positively selected sites are located in the GHF domain, which is
responsible for the hydrolase activity and HA degradation."*]. This is a **quantitative
attenuation of a retained molecular function**, exactly the case the brief says must
not be converted into a `REMOVE`.

### 2b. Not scarce — expression is normal or elevated

- Skin fibroblasts: *"NMR and DMR cells expressed higher levels of both HAS2 and HYAL2,
  but the fold-change of HAS2 was much higher than that of HYAL2 (Fig. 1e, f)."*
  [PMID:38052795]
- Kidney: *"NMR had a higher expression of HYAL2 and a drastically lower expression of
  HYAL1 in the kidney (Supplementary Fig. S3b)."* [PMID:38052795]
- Lymph node (vs mouse): only 2–3-fold lower, and the authors explicitly discount it —
  *"The RNAseq data obtained in our study seem to rule out a markedly decreased
  transcription of the Hyal2 gene, but we have no information about NMR lymph node
  HYAL2 activity."* and *"It is unlikely that the 2- to threefold lower expression of
  Hyal1 and Hyal2 could explain a large increase in HMW HA in the lymph nodes since
  that anomaly has only been found in a full Hyal2 knockout mouse, and not even in the
  Hyal1 knockout mouse13."* [PMID:33846452]

So "Hyal2 is switched off in the naked mole rat" is not what the data say. If anything
HYAL2 transcript is *up* in the two tissues where it was measured against a
phylogenetically matched control.

### 2c. The tissue-level HAase deficit is real but not attributed to HYAL2

Tian et al. established the phenotype but could not resolve the enzyme:

> *"HAase activity of the naked mole-rat cells was much lower than that of human, mouse
> or guinea pig cells (Figure 2c). Similarly, HAase activity was lower in the naked
> mole-rat tissues than in the mouse tissues (Figure 2d). These results indicate that
> two mechanisms contribute to accumulation of HMW-HA in the naked mole-rat: more
> robust synthesis and slower degradation."* [PMID:23783513]

PMID:33846452 makes the attribution gap explicit: *"Tian et al.24 described a generally
reduced hyaluronidase activity in the NMR tissues and cultured fibroblasts but the
distinction between HYAL1 and HYAL2 was not possible and the lymph nodes were not
directly examined."*

---

## 3. The trap: PMID:23783513's "Hyal2 experiment" uses the **human** cDNA

The Nature 2013 paper does contain Hyal2 experiments — an overexpression construct that
abolishes the cancer-resistance phenotype
[*"naked mole-rat cells expressing H-Ras V12 and SV40 LT and shRNA to HAS2 or
overexpressing Hyal2 formed tumors in mice"*] and an anti-Hyal2 antibody in the
antibody list. But the Methods say what was expressed:

> *"Human Hyal2 cDNA was amplified from pCMV6-HYAL2 (sc117754 OriGene)"* [PMID:23783513]

So the experiment shows that **NMR vHMM-HA is a competent substrate for a human HYAL2**
and that removing vHMM-HA removes cancer resistance. It shows **nothing** about the
catalytic properties, abundance, or physiological role of the *naked mole rat* Hyal2
protein. Any review that reads Fig. 4b as "NMR Hyal2 degrades NMR HA" has transferred a
human result onto the NMR gene. The paper's own closing sentence keeps the enzyme
attribution generic: *"In summary, our results demonstrate that extremely HMW-HA, its
binding to the CD44 receptor, and lower HAase activity play a key role in mediating the
cancer resistance of the naked mole-rat."*

## 4. What the TMEM2 paper (PMID:39009271) does and does not constrain

PMID:39009271 is **abstract-only** in the cache; nothing below is drawn from a Methods
or Results section I have not seen.

It concerns **TMEM2/CEMIP2**, a completely different protein family (G8 + GG domains +
PbH1 repeats — not GH56), and reports that the NMR ortholog is catalytically dead
because of two residue changes:
*"The amino acid residues of nmrTMEM2 (Asn247/Val302) are similar to Asn248/Phe303 of
hTMEM2, and nmrTMEM2-expressing HEK293T cells showed negligible activity."* and
*"Thus, unlike mTMEM2, nmrTMEM2 is not a physiological hyaluronidase. The inability of
nmrTMEM2 to degrade HA might partially account for the high-molecular-weight HA
accumulation in NMR tissues."*

**What it constrains for Hyal2, positively:** it supplies an alternative, better-evidenced
explanation for the degradation half of the vHMM-HA phenotype
[*"Naked mole-rats (NMRs) accumulate abundant high-molecular weight hyaluronan (HA) in
their tissues, suggesting decreased HA degradation."*]. Because the deficit has a
documented owner elsewhere, the pressure to explain it by inactivating HYAL2 disappears.
Combined with §2, the NMR degradation deficit looks like TMEM2 loss (plus sharply reduced
HYAL1 in heart and kidney, PMID:38052795) on a background of a mildly attenuated but
functional HYAL2.

**What it does not license:** transferring "lacks physiological hyaluronan-degrading
activity" to Hyal2. Different gene, different fold, different catalytic residues, and
the two proteins are not interchangeable. It also notes that human TMEM2 is already
non-catalytic, so nmrTMEM2 is not even an NMR-specific novelty in the way NMR HYAL2's
G284 is.

## 5. The `GO:0001618` virus receptor projection is not defensible for this species

Two rows are involved: `GO:0001618 virus receptor activity` (`GO_REF:0000120`,
WITH/FROM `UniProtKB:O35632|ensembl:ENSMUSP00000010191|UniProtKB:Q12891|ensembl:ENSP00000350387`)
and `GO:0046718 symbiont entry into host cell` (`GO_REF:0000108`, WITH/FROM `GO:0001618`)
— the second is a mechanical inter-ontology consequence of the first.

The receptor is for **jaagsiekte sheep retrovirus (JSRV)** and enzootic nasal tumour
virus, ovine/caprine betaretroviruses [PMID:11296287; PMID:12676986]. Three facts make
this a bad transfer to a hystricomorph rodent:

1. **The only rodent ortholog ever tested is negative.** PMID:16191204:
   *"Human Hyal2 binds the envelope (Env) proteins of these viruses and is functional as
   a receptor, but Hyal2 from mice does not bind Env nor does it mediate entry of either
   virus."* and *"Mouse and human Hyal2 are 82% identical at the amino acid level but
   mouse Hyal2 shows 1,000-fold lower JSRV receptor activity."* GOA records this as an
   explicit **`NOT|enables GO:0001618` IDA** on mouse `O35632` (QuickGO, ref
   PMID:16191204). The `GO_REF:0000120` pipeline projected a *positive* onto the NMR
   from a donor set that contains that negated donor.
2. **Receptor competence is not a conserved family property.** It varies by orders of
   magnitude across mammals — PMID:16191204: *"we previously found that bovine Hyal2 acts
   as a weak receptor for JSRV and ENTV compared to sheep or human Hyal2"*.
3. **It is not predictable from sequence at any single site.** The determinants are
   *"localized to the central third of Hyal2"* and act jointly — *"None of the single or
   double mutation reduced the receptor activity of human Hyal2 by more than 10-fold,
   whereas mouse Hyal2 activity is reduced 1,000-fold from that of human Hyal2."*
   [PMID:16191204]. So no residue check on A0A0P6J1Y4 can rescue or refute the transfer;
   only a binding/transduction assay can.

The same paper also removes the "hosts evolve receptor resistance" rationale for
expecting NMR to be permissive or not: *"Together these results provide strong evidence
for conservation of Hyal2 protein sequence but no evidence for positive selection to
resist virus infection."*

Actions taken: `REMOVE` for `GO:0001618` and for the derived `GO:0046718`;
`MARK_AS_OVER_ANNOTATED` (not remove) for the downstream `GO:0009615 response to virus`
and `GO:0051607 defense response to virus`, whose donor evidence is entirely JSRV/ENTV-
specific but which are broader terms not flatly contradicted.

## 6. `GO:0005829 cytosol` is a topology violation

Removed. The mature chain begins at residue 21 after a cleaved signal peptide
(`SIGNAL          1..20`) and is GPI-anchored (`Lipid-anchor, GPI-anchor`), so it faces
the extracellular space or an endosomal/lysosomal lumen — never the cytosolic
compartment, absent retrotranslocation for which there is no evidence in any species.
The human donor annotation is a single IDA from PMID:19366691, the Hyal-2/WOX1 imaging
study, where "cytosol" is most plausibly non-nuclear immunofluorescence. This is a
judgment about the *projection*, not about the human curator's reading of that image.

## 7. The two moonlighting modules

Both are real published biology, both are single-lab, and neither has any NMR data.

**RON/MST1R (human `Q12891`, IPI/IDA PMID:12676986).** *"the HYAL2 receptor protein is
associated with the RON receptor tyrosine kinase (also called MST1R or Stk in the
mouse), rendering it functionally silent"* and RON release *"activates the Akt and
mitogen-activated protein kinase pathways"*. This is corroborated on the NMR record
itself by UniProt's ARBA subunit line `-!- SUBUNIT: Interacts with MST1R.`
[file:HETGA/Hyal2/Hyal2-uniprot.txt]. It grounds `GO:0030971`, `GO:0030294` and
`GO:0051898`, all kept as non-core.

**TGF-β1 / WWOX nuclear relocation (mouse `O35632`, IDA/IPI PMID:19366691).**
*"we determined that TGF-beta1 bound cell surface hyaluronidase Hyal-2 on microvilli in
type II TGF-beta receptor-deficient HCT116 cells, as determined by immunoelectron
microscopy. This binding resulted in recruitment of proapoptotic WOX1 (also named WWOX
or FOR) and formation of Hyal-2.WOX1 complexes for relocation to the nuclei."*
The ligand-binding and response ends (`GO:0050431`, `GO:0071560`) are kept as non-core.
The nuclear/transcriptional end (`GO:0003713` coactivator activity, `GO:0090575`
part_of an RNA Pol II transcription regulator complex, `GO:0045944`, `GO:0042307`) is
marked over-annotated: asserting that a GPI-anchored ectoenzyme is a *structural part of
a transcription factor complex* in an untested species, from reporter and FRET data in
one laboratory, is a claim well beyond what an orthology projection can carry.

## 8. `GO:0033906` vs `GO:0004415` — two mutually exclusive bond specificities

`GO:0004415 hyalurononglucosaminidase activity` is EC 3.2.1.35 (β-1,4 hydrolysis between
GlcNAc and GlcUA); `GO:0033906 hyaluronoglucuronidase activity` is EC 3.2.1.36 (β-1,3
hydrolysis), the leech/hookworm-type mechanism. UniProt assigns the NMR protein
`EC=3.2.1.35` and only that [file:HETGA/Hyal2/Hyal2-uniprot.txt]. The human anchor for
GO:0033906 is one IDA plus a PANTHER IBA, against nine IDAs for GO:0004415. The NMR
enzyme's linkage specificity has never been determined. `GO:0004415` accepted,
`GO:0033906` marked over-annotated.

## 9. Two apparently contradictory results about HYAL2 catalysis, reconciled

Worth recording because it is the source of most confusion in this family. Human HYAL2
carries **both** `GO:0004415 IDA` ×9 and one **`NOT|enables GO:0004415` IDA** from
PMID:11296287, whose abstract says *"we could not detect hyaluronidase activity
associated with or secreted by cells expressing HYAL2, whereas we could easily detect
such activity from cells expressing the related serum hyaluronidase HYAL1."* The
resolution is that HYAL2 is a genuinely weak, acid-requiring enzyme whose activity is
easily missed at neutral pH but is physiologically real: PMID:9712871 *"The HYAL2
protein was shown to have hyaluronidase activity below pH 4."*, and PMID:18772348
*"This protein displays weak in vitro hyaluronidase activity"* yet *"murine HYAL2 has a
physiological activity in vivo that is relevant for craniovertebral bone formation,
maintenance of plasma HA concentrations, and erythrocyte and platelet homeostasis."*
The GO molecular function is therefore correct for HYAL2 orthologs generally, and the
NMR's ~2-fold-ish attenuation at G284 sits well inside that envelope.

## 10. What the affinage human-ortholog record missed

`Hyal2-deep-research-affinage-human-ortholog.md` is an accurate and well-cited record of
the **human** protein (21 dated findings, all human/mouse/Xenopus), and it was useful as
a mechanistic baseline for §7 and §9. Recall gaps that mattered here:

- **Nothing about the naked mole rat.** Expected — affinage is human-only — but it means
  the single decisive result for this review (the NMR HYAL2 G284A assay in
  PMID:38052795) was absent, as were PMID:23783513, PMID:33846452 and PMID:39009271.
- **It softened the one negative result it did cite.** It lists PMID:16191204 as
  *"Amino acid differences in the central third of Hyal2 account for the ~1000-fold
  difference in JSRV receptor activity between human and mouse Hyal2"* — framed as a
  quantitative difference. It does not record that mouse Hyal2 **does not bind Env at
  all**, nor that GOA carries an explicit `NOT` annotation for the mouse. For a review
  of a *rodent* ortholog, that omission is the difference between `ACCEPT` and `REMOVE`
  on `GO:0001618`.
- **Its `mechanism_profile` GO grounding is unusable** and was not imported, per the
  brief. It lists `GO:0140098 catalytic activity, acting on RNA` as a molecular activity
  for a glycoside hydrolase, and `GO:0005739 mitochondrion` as a localization on the
  strength of one staurosporine-apoptosis observation.

## 11. Unresolved

- **Whether NMR Hyal2 contributes materially to the vHMM-HA phenotype at all.** The
  attribution has never been made at the isoenzyme level in NMR tissue
  [PMID:33846452 *"the distinction between HYAL1 and HYAL2 was not possible"*], and the
  only NMR HYAL2 functional datum is a transfected-cell gel with no kinetics. The G284
  effect is described as a difference in HA size after three days, not quantified.
- **Whether NMR HYAL2 is a JSRV receptor.** Untestable from sequence (§5); no assay
  exists. `REMOVE` here is a statement that the *projection* is unsupported, not a claim
  that the NMR protein has been shown to be non-permissive.
- **Whether the RON and WWOX interactions occur in NMR cells.** No NMR data; kept as
  non-core / over-annotated on the strength of the human and mouse work alone.
- **pH dependence in NMR.** HYAL2 needs local acidification to work pericellularly in
  human and rat cells (affinage baseline, PMID:19783662). Nobody has asked whether the
  NMR pericellular pH microenvironment differs — a plausible non-genetic route to
  "lower HAase activity" that would leave the enzyme itself untouched, and one that the
  GO annotations cannot express.

## 12. Terms I did not find

There is no GO term for **setting or regulating the molecular mass distribution of
hyaluronan**, which is precisely the phenotype under selection in subterranean mammals
(PMID:38052795) and the property that inverts CD44 signalling outcomes
[PMID:32398747 *"vHMM-HA (>6.1 MDa) has superior cytoprotective properties compared to
the shorter HMM-HA."*]. GO has `GO:0030212 hyaluronan metabolic process`,
`GO:0030213/GO:0030214` for synthesis and catabolism, and `GO:1900125 regulation of
hyaluronan biosynthetic process`, but nothing on the *product size* axis — even though
it has precedent for length terms elsewhere (`GO:0030832 regulation of actin filament
length`, `GO:0032532 regulation of microvillus length`). Proposed as a new term in the
review YAML.
