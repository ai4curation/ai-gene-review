# PfCRT (Q8IBZ9, PF3D7_0709000) — curation notes

> **Provenance note:** automated deep research was unavailable in this environment
> (Falcon auth failure, invalid OpenAI key), so **no `*-deep-research-*.md` file was
> generated**. What follows is a **manual literature review** performed by reading the
> UniProt flat file, the cached publications under `publications/`, and additional
> primary papers fetched into the cache with `ai-gene-review fetch-pmid`.

## 1. Identity and family

- UniProt `CRT_PLAF7` / Q8IBZ9, 424 aa, 10-TM integral membrane protein of the
  digestive-vacuole (food-vacuole) membrane of *Plasmodium falciparum* 3D7.
- Family assignment is bioinformatic: CRT belongs to a previously undefined family
  within the drug/metabolite transporter (DMT) superfamily
  [PMID:15240840 "falling within the drug/metabolite transporter superfamily"]. That
  paper is explicitly a sequence analysis, not an experimental study
  [PMID:15240840 "The function of CRT is not known and the protein was originally described as a"
  transporter simply because it possesses 10 transmembrane domains].
- 3D7 is the **chloroquine-sensitive wild-type** allele; the resistance-associated
  isoforms (Dd2, 7G8, Ecu1110, carrying K76T etc.) are different alleles of the same
  gene. Several annotations on Q8IBZ9 derive from experiments on **mutant** isoforms,
  which matters for how strongly they apply to the reference (3D7) protein.

## 2. Localization

- The founding genetic/transfection paper localized the protein to the digestive
  vacuole by immuno-labelling
  [PMID:11090624 "This transmembrane protein localizes to the parasite digestive vacuole (DV), the site of CQ action"].
- UniProt records "Vacuole membrane ... Multi-pass membrane protein" and notes
  "Localizes to the parasite digestive vacuole, the site of chloroquine action."
- Trafficking to the DV membrane is signal-dependent and the protein is a
  phosphoprotein; T416 phosphorylation is implicated in sorting
  [PMID:20015114 "suggest that phosphorylation of threonine 416 is a possible deciding signal for the sorting"].
  That study is the source of the ER (GO:0005783) IDA — an early biosynthetic
  transit compartment, not a functional site.
- GO has `GO:0020020 food vacuole` ("Vacuole within a parasite used for digestion of
  the host cell cytoplasm") but **no "food vacuole membrane" term**; the generic
  `GO:0005774 vacuolar membrane` is currently the most precise membrane term
  available (see proposed new term).

## 3. Native (physiological) function

The natural substrate question was unresolved for two decades; heterologous systems
gave contradictory answers (Cl- channel, H+ pump, cation channel, GSH transporter,
Fe2+/Fe3+ transporter) — enumerated and criticized in
[PMID:32764664 "a glutathione transporter32, a non-specific transporter of inorganic and organic cations as well as of many other metabolites33, or an Fe2+/Fe3+ transporter34"].

The best-supported current model: PfCRT exports host-haemoglobin-derived **peptides
of 4–11 residues** from the DV lumen to the parasite cytosol:

- [PMID:32764664 "We show that PfCRT functions to export host-derived peptides 4–11 residues in length from the parasite’s DV, and that the protein does not behave as a non-specific transporter of other metabolites and/or ions."]
- [PMID:32764664 "The transport of peptides and peptide mimics via PfCRT is saturable, blocked by known PfCRT inhibitors, and is dependent on protons as well as on a co-substrate that remains to b"e identified]
- Physiological consequence: [PMID:32764664 "the PfCRT-mediated transport of peptides from the DV to the cytosol serves to (1) provide a source of amino acids to support the parasite’s high growth rate and (2) reduce peptide levels within the DV and thereby prevent the osmotic stress, swelling and dysfunction of this organelle."]

An earlier proteoliposome study with purified protein reported broader polyspecific,
proton-gradient-driven export, including basic amino acids and polyamines
[PMID:25733858 "All PfCRTs tested actively took up tetraethylammonium, verapamil, CQ, basic amino acids, polypeptides, and polyamines at the expense of an electrochemical proton gradient."].
UniProt's FUNCTION/CATALYTIC ACTIVITY blocks (arginine, lysine, histidine, histamine,
spermidine) come from this paper. Shafik et al. re-screened metabolites in oocytes and
in parasites and did not reproduce non-peptide transport, so the amino-acid/polyamine
substrates are treated here as in-vitro findings not yet corroborated in situ; peptide
export is the claim supported both in vitro and in situ.

Loss/perturbation phenotypes support the osmotic-homeostasis role: PfCRT mutations
C101F and L272F produce grossly swollen vacuoles
[PMID:26420308 "causing the development of enlarged food vacuoles"], and the same
mutations cut chloroquine transport
[PMID:26420308 "transport chloroquine by approximately 93 and 82%, respectively, when expressed"].

## 4. Drug (xenobiotic) transport

- Resistance mechanism: mutant PfCRT effluxes chloroquine out of the DV, away from its
  haem target. Wild-type does not transport CQ in oocytes
  [PMID:25378409 "mutant PfCRT transports the antimalarial drug"
  chloroquine away from its target, whereas the wild-type form of PfCRT does not].
- Mutant PfCRT is a genuine multidrug carrier
  [PMID:25378409 "mutant PfCRT also transports quinine, quinidine, and verapamil, indicating"
  that the protein behaves as a multidrug resistance carrier], with distinct but
  interacting substrate sites.
- Cryo-EM of the 7G8 isoform shows resistance mutations lining a central negatively
  charged cavity and confirms membrane-potential- and pH-dependent CQ transport
  [PMID:31776516 "The 7G8 isoform transports CQ in a membrane potential- and pH-dependent manner,"].
- Collateral sensitivity work shows CQ-resistant PfCRT isoforms, but not wild type,
  transport lumefantrine and mefloquine
  [PMID:35507548 "we demonstrate that these PfCRT isoforms transport all 3 drugs, whereas wild-type PfCRT does not."].
- The purified-protein study did detect CQ and verapamil uptake by the CQ-sensitive
  protein as well [PMID:25733858 "All PfCRTs tested actively took up tetraethylammonium, verapamil, CQ, basic amino acids, polypeptides, and polyamines at the expense of an electrochemical proton gradient."],
  so xenobiotic transporter activity is defensible for the gene product, but it is an
  acquired/secondary capability, strongly allele-dependent, and not the natural role.

## 5. Glutathione

- [PMID:23256874 "We further demonstrate via expression in Xenopus laevis oocytes that the mutant alleles of Pfcrt in CQR parasites selectively transport GSH."] —
  note "**mutant alleles**"; the paper's own model is that GSH influx into the DV is a
  property of the CQR isoforms, contributing to resistance, not the normal function of
  the 3D7 protein.
- Shafik et al. explicitly list "a glutathione transporter" among the incompatible
  earlier claims and screened GSH without finding it to be a substrate or co-substrate
  [PMID:32764664 "We screened many solutes, including Fe2+, Fe3+ and glutathione, but were unable to identify the co-substrate"].
- The IBA for `GO:0034635 glutathione transport` is seeded by *Arabidopsis* CRT-like
  (CLT) plastidic glutathione transporters (AGI_LocusCode:AT4G24460, AT5G12170,
  AT5G19380). The plant CLT clade is a distinct, plastid-targeted branch of the
  CRT-like family; transferring the GSH-transport role onto the apicomplexan DV
  transporter is exactly the kind of family-level over-reach the in-situ data argue
  against. Both GSH rows are therefore marked as over-annotation rather than removed
  (the oocyte IDA is real, just allele-specific and not reproduced).

## 6. Protist-specific checks performed

- No plant/animal-only terms survive: the only plant-derived inference is the
  glutathione-transport IBA, handled above.
- Organelle terms are apicomplexan-appropriate: food vacuole (GO:0020020) is the
  correct digestive compartment; no apicoplast, rhoptry, microneme or
  parasitophorous-vacuole claims are made.
- No host-vs-symbiont process confusion: PfCRT acts entirely within the parasite's own
  DV membrane; the peptides transported are host-derived but the transport event is
  intra-parasite, so symbiont-host interaction terms are not warranted.
- Paralog check: PfMDR1 (an ABC transporter, separate family) also sits in the DV
  membrane and transports several of the same drugs [PMID:35507548]; drug-transport
  terms should not be propagated between the two on the basis of shared phenotypes.

## 7. Curation decisions (summary)

| Term | Evidence | Action |
|---|---|---|
| GO:0005774 vacuolar membrane | IEA | ACCEPT (no food-vacuole-membrane term exists) |
| GO:0005783 endoplasmic reticulum | IDA | KEEP_AS_NON_CORE (biosynthetic transit) |
| GO:0009410 response to xenobiotic stimulus | IDA | KEEP_AS_NON_CORE |
| GO:0016020 membrane | TAS | TOO_GENERAL |
| GO:0020020 food vacuole | IDA | ACCEPT |
| GO:0022857 transmembrane transporter activity | IBA | MODIFY → GO:0035673 |
| GO:0034635 glutathione transport (IBA, IDA) | IBA/IDA | MARK_AS_OVER_ANNOTATED (both) |
| GO:0042908 xenobiotic transport | IEA | KEEP_AS_NON_CORE |
| GO:0042910 xenobiotic transmembrane transporter activity (IEA, IMP) | IEA/IMP | KEEP_AS_NON_CORE (both) |
| GO:0055085 transmembrane transport | IEA | MODIFY → GO:0015833 |
| GO:0035673 oligopeptide transmembrane transporter activity | — | NEW |
| GO:0015833 peptide transport | — | NEW |

Note on the ER row: only the abstract of PMID:20015114 is cached and it does not
mention the endoplasmic reticulum, so no verbatim quote can be attached. The action is
unchanged — the IDA rests on full-text trafficking data the curator read — but the
`supported_by` entry was dropped rather than filled with the threonine-416 sorting
quote, which names no compartment.

Proposed new term: *food vacuole membrane* (the membrane bounding GO:0020020), needed
because the DV membrane is the functional site of PfCRT, PfMDR1, PfV-type ATPase and
several drug-resistance determinants, and GO currently forces the generic
`GO:0005774 vacuolar membrane`.
