---
title: "Draft go-ontology ticket: obsolete GO:0004321"
autolink_gene_symbols: false
---

# Draft go-ontology ticket: obsolete GO:0004321

[← back to the project page](../FATTY_ACYL_COA_SYNTHASE_OBSOLETION.md)

Ready to paste into a new [geneontology/go-ontology](https://github.com/geneontology/go-ontology/issues/new/choose) issue. Counts are from QuickGO and UniProt release 2026_03, retrieved 2026-11-01; see [usage_summary.yaml](usage_summary.yaml).

---

**Title:** Obsolete GO:0004321 fatty-acyl-CoA synthase activity: EC 2.3.1.86 is a fungal multienzyme system, not a single reaction

**Terms**

- GO:0004321 *fatty-acyl-CoA synthase activity* (MF)
- GO:0005836 *fatty-acyl-CoA synthase complex* (CC), which is defined only through GO:0004321 ("A protein complex that possesses fatty-acyl-CoA synthase activity") and has no annotations

**Why**

1. **The source is a system, not a reaction.** GO:0004321 takes its definition from EC 2.3.1.86, whose accepted IUBMB name is "fatty-acyl-CoA synthase system" (alternative name "yeast fatty acid synthase"). The EC comment describes the fungal multienzyme complex of two subunits that together carry out EC 2.3.1.38, 2.3.1.39, 2.3.1.41, 1.1.1.100, 4.2.1.59, 1.3.1.10 and 1.1.1.279. The overall equation is the net of that cycle, run on an α6β6 complex: "The alpha and beta polypeptide chains form the six catalytic domains required for fatty acid synthesis" (PMID:17431175). No single gene product enables it, and each component step already has a GO MF term.
2. **Reaction resources do not use it.** Rhea has the equation as RHEA:22896, but with no EC number and no UniProtKB entries annotated to it. Swiss-Prot's S. cerevisiae FAS1 (P07149) and FAS2 (P19097) give the 2.3.1.86 reaction as free text without a Rhea cross-reference, while each of their partial reactions carries one.
3. **Most current annotations are on proteins that cannot perform it.** Of 17,305 annotations to GO:0004321, about 3,684 (21%) are on fungal FAS subunits. The rest:

   | Annotations | Proteins | Route |
   |---:|---|---|
   | 12,690 | PTHR43605 AMP-forming acyl-CoA ligases (EC 6.2.1) | PAINT IBD on PTN001944787 seeded by one RGD IDA, then IBA and TreeGrafter (geneontology/go-annotation#6642) |
   | 520 | Bacterial modular polyketide and PUFA synthases | EC2GO from EC 2.3.1.86 added by UniProt rule ARBA00048237 |
   | 163 | Other bacterial acyl-CoA ligases | EC2GO from EC 2.3.1.86 typed by genome submitters (e.g. "Long-chain-fatty-acid--CoA ligase, EC=2.3.1.86") |
   | 39 | Other acyl-CoA ligases | IDA, IMP and ISO rows (GeneDB, MTBBASE, TAIR, MGI, RGD) and EnsemblPlants projections |
   | 83 | Oomycete and other non-fungal FAS-like proteins | EC2GO; uncertain |
   | 7 | Unrelated proteins (RNA helicase, titin, …) | EC2GO from submitter EC |
   | 119 | Entries not resolved | EC2GO |

   Several routes arrive at this term independently, and each is a "synthase"/"synthetase" or system/reaction confusion.
4. **Curators do not keep it apart from GO:0004312.** SGD (FAS1, FAS2; IMP, PMID:65153 and PMID:1100391) and PomBase (fas1, fas2; IDA, PMID:9693066) annotate fungal FAS to GO:0004312 *fatty acid synthase activity*, the animal reaction (EC 2.3.1.85, free fatty acid product). InterPro2GO maps the fungal FAS families IPR003965 and IPR026025 to GO:0004312 too. The EC split between the two systems is not used in practice.
5. **The definition has drifted from its source.** GO's equation has "2n NADH + 2n NADPH"; the current EC 2.3.1.86 reaction uses NADPH only.

**Proposal**

- Obsolete GO:0004321 with no `replaced_by`. Suggested `consider`:
  - component activities: GO:0004313 [acyl-carrier-protein] S-acetyltransferase activity, GO:0004314 [acyl-carrier-protein] S-malonyltransferase activity, GO:0004315 3-oxoacyl-[acyl-carrier-protein] synthase activity, GO:0004316 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity, GO:0019171 (3R)-hydroxyacyl-[acyl-carrier-protein] dehydratase activity, GO:0141148 enoyl-[acyl-carrier-protein] reductase (NADPH) activity;
  - the complex: GO:0005835 fatty acid synthase complex;
  - the process: GO:0006633 fatty acid biosynthetic process.
- Obsolete GO:0005836 fatty-acyl-CoA synthase complex, `consider` GO:0005835 (whose synonyms already include "cytosolic type I FAS complex").
- Retire the mappings EC:2.3.1.86 → GO:0004321 (ec2go), RHEA:22896 and MetaCyc FATTY-ACYL-COA-SYNTHASE-RXN.

**Annotations to migrate** (non-IEA, non-IBA)

- Fungal FAS, to the component terms, GO:0005835 and GO:0006633:
  - SGD RCA: FAS1 ×5, FAS2 ×1 and complex CPX-1162 (YeastPathways);
  - PomBase NAS: fas1;
  - ComplexPortal IDA: CPX-1162 (PMID:19679086), CPX-26505 (PMID:9693066);
  - UniProt ISS ×15: dedicated FAS subunits of fungal secondary metabolism (hexA ×2, hexB, stcJ, stcK, pkiB, pkiC, TOXC, TOXH, pigJ, pigK, atnF, atnM, oryfasB, FG00037), by similarity to *A. parasiticus* aflA/aflB or yeast FAS1/FAS2.
- Non-FAS proteins, to delete or repoint to a ligase term (see geneontology/go-annotation#6642): RGD Acsm4 IDA (PMID:12709059); MGI Slc27a3 IMP (PMID:15469937) and its RGD ISO; GeneDB *T. brucei* and *Leishmania* ACS1–4 IDA (PMID:11535136); TAIR 4CLL7, 4CLL9 IDA (PMID:15677481); MTBBASE fadD13 (PMID:20027301), fadD28 (PMID:9098059) IDA; GO_Central ISO on mouse Acsm4.
- 89 IBA rows via PTN001944787, which go-annotation#6642 already asks PAINT to retract.

**GO-CAMs using GO:0004321** (5 activities, all fungal)

- gomodel:678073a900002931 (*S. pombe*): enabled by GO:0005835 fatty acid synthase complex.
- Four SGD YeastPathways imports on FAS1: YeastPathways_FASYN-ELONG2-PWY, YeastPathways_PWY3O-355, YeastPathways_PWY3O-5962, YeastPathways_PWY3O-6336.

The *S. pombe* model uses the term for what it does describe well, the activity of the whole FAS complex. If GO prefers to keep a complex-level term, an alternative to obsoletion is to redefine GO:0004321 explicitly as the activity of the fungal type I FAS complex, to be annotated with `contributes_to` on its subunits, and to remove the EC2GO and Rhea mappings that put it on single proteins.

**One gap.** The fungal MPT domain's final transfer of the acyl chain from ACP to CoA, which is what makes the product an acyl-CoA, has no specific MF term; SGD uses the generic GO:0016409 palmitoyltransferase activity. A new term may be worth considering, but it is not needed for the obsoletion.

**Related, not proposed here.** GO:0004312 follows EC 2.3.1.85, "fatty-acid synthase system", and so has the same character. In animals one multifunctional polypeptide performs the whole cycle, so an `enables` annotation is easier to defend, but its use on fungal FAS (item 4) shows the two system terms are not kept apart.

**Prior discussion:** go-ontology#8102 (2010–2015, closed as out of date) discussed whether GO:0004321 is a process rather than a function; go-ontology#7662. Annotation ticket: go-annotation#6642.
