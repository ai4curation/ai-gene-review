# Provenance: kguE (Q88HH8) GO:0008114 evaluation

## Query 1 — UniProt Q88HH8 (REST JSON)
- Accession Q88HH8 / ID Q88HH8_PSEPK; gene **kguE**; ordered locus **PP_3379**
- recommendedName: **None**; EC in name: **none**
- CATALYTIC ACTIVITY comment: **none**; FUNCTION comment: **none**
- Submission name: **"Epimerase"** with EC **1.1.1.43** attached (self-contradictory)
- Domains: eggNOG **COG1082**; Gene3D **3.20.20.150** (divalent-metal-dependent TIM barrel);
  InterPro **IPR050312** (IolE/XylA/MocC-like), **IPR036237** (Xylose isomerase-like superfamily);
  PANTHER **PTHR12110** (hydroxypyruvate isomerase) / SF53; SUPFAM **SSF51658** (Xylose isomerase-like)
- GO (molecular function): **GO:0008114** F:phosphogluconate 2-dehydrogenase activity — evidence
  **IEA:UniProtKB-EC** (= GO_REF:0000003 ec2go). This is the ONLY MF GO term.
- Sequence length: 259 aa

## Query 2 — kgu operon neighbors (UniProt)
| Locus | Accession | Gene | Submission name | EC |
|---|---|---|---|---|
| PP_3376 | Q88HI1 | ptxD | Phosphonate dehydrogenase | 1.20.1.1 |
| PP_3377 | Q88HI0 | kguT | 2-ketogluconate transporter, putative | — |
| PP_3378 | Q88HH9 | kguK | 2-ketogluconokinase | 2.7.1.13 |
| PP_3379 | Q88HH8 | **kguE** | **Epimerase** | **1.1.1.43** |
| PP_3380 | Q88HH7 | ptxS | HTH transcriptional regulator PtxS | — |
| PP_3382 | Q88HH6 | — | Gluconate 2-dehydrogenase cytochrome c subunit | 1.1.99.3 |

- The **only** KT2440 protein returned for `ec:1.1.1.43` is **kguE itself** — confirming the EC was
  attached to the epimerase gene, not to a genuine NAD(P)-dependent reductase.

## Query 3 — InterPro family definitions
- **IPR050312 (IolE/XylA/MocC-like):** "primarily involved in the metabolism of inositol and its
  derivatives ... catalyse the **dehydration of inosose** ... reversible interconversion of
  2-keto-myo-inositol ... catabolism of rhizopine, **xylose**, and other sugars." → isomerase/
  dehydratase/epimerase family, **not** an NAD(P)-dependent oxidoreductase.
- **IPR036237 (Xylose isomerase-like superfamily):** "β/α TIM barrel ... metal-binding sites."

## Interpretation
EC 1.1.1.43 (6-phospho-D-gluconate:NAD(P)+ 2-oxidoreductase) is a **Rossmann-fold NAD(P)-dependent
oxidoreductase**, structurally incompatible with KguE's metal-dependent TIM-barrel isomerase fold.
GO:0008114 on kguE is therefore an unsupported ec2go carry-over from a self-contradictory EMBL EC
number. The genuine EC 1.1.1.43 (2-keto-6-phosphogluconate reductase, KguD) is a separate enzyme
(Daddaoua 2010 PMID:20581202; del Castillo 2008 PMID:18245293).

## Query 4 — AlphaFold + fold family (Iteration 2)
- **AF-Q88HH8-F1** (model_v6): full-length 259 aa, **mean pLDDT 94.88** → confident, single compact
  domain (real TIM-barrel enzyme, not a fragment/pseudogene).
- KguE signature DBs: Gene3D 3.20.20.150; SUPFAM SSF51658; PANTHER PTHR12110(:SF53);
  InterPro IPR050312/IPR036237. **No Pfam listed; NO NAD-binding/Rossmann (PF03446/PF00393) domain.**
- KT2440 PF03446 (NAD_binding_2 / 6PGDH-β-hydroxyacid-dehydrogenase, Rossmann) family genes:
  PP_4666 mmsB, PP_4299 glxR (EC 1.1.1.60), PP_4043 gntZ (EC 1.1.1.44), PP_2798, PP_1143 — the true
  EC 1.1.1.43 reductase fold lives here, **not** in kguE.
- del Castillo et al. 2007 (**PMID:17483213**): 2-ketogluconate "is transported to the cytoplasm, and
  subsequently **phosphorylated and reduced** to 6-phosphogluconate" → EC 1.1.1.43 = reductase step.

## Query 5 — Family-wide activity survey (Iteration 3)
Reviewed (Swiss-Prot) members of KguE's family **IPR050312**: 75 entries.
- Top names: Inosose dehydratase (36), 3-dehydroshikimate dehydratase (4), Inosose isomerase (4),
  Fructoselysine/D-psicose/D-tagatose/L-ribulose 3-epimerase, Ketose 3-epimerase, C-glycoside
  deglycosidase.
- EC classes present: **4.x (lyases/dehydratases)** — 4.2.1.44 ×38, 4.2.1.118 ×4, 4.1.99.-, 4.1.1.120;
  **5.x (isomerases/epimerases)** — 5.3.99.11 ×4, 5.1.3.41, 5.1.3.30, 5.1.3.31, 5.1.3.35, 5.3.1.36, 5.1.3.-.
- **EC class 1 (oxidoreductases): 0/75. EC 1.1.1.43: ABSENT.**
- Conclusion: no characterized member of this fold is a dehydrogenase → KguE's true MF is a
  carbohydrate epimerase/isomerase/dehydratase, not GO:0008114.

## Reference-context paper
- **PMID:39770733** — Sun et al. 2024, "Characterization and Transcriptional Regulation of the
  2-Ketogluconate Utilization Operon in [Pseudomonas]." Abstract not programmatically retrievable in
  this run; flagged for curator full-text review.
