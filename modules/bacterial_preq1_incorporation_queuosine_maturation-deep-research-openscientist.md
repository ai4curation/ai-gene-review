---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T19:38:12.347769'
end_time: '2026-07-26T19:53:00.816302'
duration_seconds: 888.47
template_file: templates/module_research.md.j2
template_variables:
  module_title: Bacterial preQ1 incorporation and queuosine maturation
  module_summary: A reusable bacterial pathway that converts preQ0 to the mature queuosine
    modification at wobble position 34 of tRNA(Asp), tRNA(Asn), tRNA(His), and tRNA(Tyr).
    QueF reduces preQ0 to preQ1, Tgt exchanges guanine-34 for preQ1, QueA transfers
    and rearranges the ribose moiety of S-adenosylmethionine to form epoxyqueuosine,
    and QueG reduces epoxyqueuosine to queuosine.
  module_outline: "- Bacterial preQ1 incorporation and queuosine maturation\n  - 1.\
    \ preQ1 formation\n  - QueF-dependent preQ1 formation\n    - QueF preQ1 synthase\
    \ activity (molecular player: QueF preQ1 synthase family; activity or role: preQ1\
    \ synthase activity)\n  - 2. preQ1 incorporation at tRNA position 34\n  - Tgt-dependent\
    \ preQ1-tRNA formation\n    - Tgt tRNA-guanine transglycosylase activity (molecular\
    \ player: bacterial Tgt family; activity or role: bacterial tRNA-guanosine(34)\
    \ preQ1 transglycosylase activity)\n  - 3. epoxyqueuosine formation\n  - QueA-dependent\
    \ epoxyqueuosine formation\n    - QueA SAM:tRNA ribosyltransferase-isomerase activity\
    \ (molecular player: QueA family; activity or role: S-adenosylmethionine:tRNA\
    \ ribosyltransferase-isomerase activity)\n  - 4. epoxyqueuosine reduction\n  -\
    \ QueG-dependent queuosine formation\n    - QueG epoxyqueuosine reductase activity\
    \ (molecular player: QueG epoxyqueuosine reductase family; activity or role: epoxyqueuosine\
    \ reductase activity)"
  module_connections: '- QueF-dependent preQ1 formation feeds into Tgt-dependent preQ1-tRNA
    formation: QueF supplies preQ1 to Tgt.

    - Tgt-dependent preQ1-tRNA formation feeds into QueA-dependent epoxyqueuosine
    formation: Tgt produces the preQ1-tRNA consumed by QueA.

    - QueA-dependent epoxyqueuosine formation feeds into QueG-dependent queuosine
    formation: QueA produces the epoxyqueuosine-tRNA consumed by QueG.'
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 23
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: bacterial_preq1_incorporation_queuosine_maturation-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: bacterial_preq1_incorporation_queuosine_maturation-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Commissioned Review Brief

## Review Topic

Bacterial preQ1 incorporation and queuosine maturation

## Working Scope

A reusable bacterial pathway that converts preQ0 to the mature queuosine modification at wobble position 34 of tRNA(Asp), tRNA(Asn), tRNA(His), and tRNA(Tyr). QueF reduces preQ0 to preQ1, Tgt exchanges guanine-34 for preQ1, QueA transfers and rearranges the ribose moiety of S-adenosylmethionine to form epoxyqueuosine, and QueG reduces epoxyqueuosine to queuosine.

## Provisional Biological Outline

- Bacterial preQ1 incorporation and queuosine maturation
  - 1. preQ1 formation
  - QueF-dependent preQ1 formation
    - QueF preQ1 synthase activity (molecular player: QueF preQ1 synthase family; activity or role: preQ1 synthase activity)
  - 2. preQ1 incorporation at tRNA position 34
  - Tgt-dependent preQ1-tRNA formation
    - Tgt tRNA-guanine transglycosylase activity (molecular player: bacterial Tgt family; activity or role: bacterial tRNA-guanosine(34) preQ1 transglycosylase activity)
  - 3. epoxyqueuosine formation
  - QueA-dependent epoxyqueuosine formation
    - QueA SAM:tRNA ribosyltransferase-isomerase activity (molecular player: QueA family; activity or role: S-adenosylmethionine:tRNA ribosyltransferase-isomerase activity)
  - 4. epoxyqueuosine reduction
  - QueG-dependent queuosine formation
    - QueG epoxyqueuosine reductase activity (molecular player: QueG epoxyqueuosine reductase family; activity or role: epoxyqueuosine reductase activity)

## Known Relationships Among Steps

- QueF-dependent preQ1 formation feeds into Tgt-dependent preQ1-tRNA formation: QueF supplies preQ1 to Tgt.
- Tgt-dependent preQ1-tRNA formation feeds into QueA-dependent epoxyqueuosine formation: Tgt produces the preQ1-tRNA consumed by QueA.
- QueA-dependent epoxyqueuosine formation feeds into QueG-dependent queuosine formation: QueA produces the epoxyqueuosine-tRNA consumed by QueG.

## Assignment

Write a rigorous, review-style synthesis suitable for a molecular biology
audience. Treat the topic as a biological system whose boundaries, core
mechanisms, variants, and unresolved points should be made clear to readers who
know the field but are not specialists in this specific process.

The review should be explanatory rather than encyclopedic. Anchor broad claims
in primary literature or authoritative reviews, but keep the focus on how the
system works and how its parts fit together.

## Questions To Address

1. **Scope and boundaries**
   - What exactly is included in this biological system?
   - Which neighboring pathways, organelle processes, complexes, or regulatory
     events are often confused with it but should be treated separately?
   - Are there competing definitions in the literature?

2. **Core mechanism**
   - What is the best current model for the sequence of events?
   - Which steps are obligatory, which are conditional, and which are accessory?
   - What molecular assemblies, enzymes, receptors, adaptors, transporters, or
     structural units carry out each major step?

3. **Variation**
   - How does the system vary across major evolutionary lineages?
   - Are there well-supported differences between cell types, tissues,
     developmental stages, physiological states, or compartments?
   - Where are there alternative routes that achieve a similar outcome by
     different molecular means?

4. **Conservation and origin**
   - What is the deepest plausible evolutionary origin of the system?
   - Which parts appear ancient and conserved, and which appear to be later
     elaborations, replacements, or lineage-specific losses?
   - When a protein family has expanded, which family members are the best
     representatives for understanding the ancestral role?

5. **Physical and biological constraints**
   - What steps must occur in a particular order?
   - Which events are mutually exclusive, compartment-specific, cell-type
     specific, substrate-specific, or stage-specific?
   - What evidence rules out otherwise plausible paths through the system?

6. **Evidence and controversy**
   - Which mechanistic claims are strongly supported by experiments?
   - Where does the literature disagree, rely on indirect evidence, or mix data
     from organisms that may not be comparable?
   - What are the most important open questions?

## Output Format

Use the style and structure of a concise review article:

1. Executive summary
2. Definition and biological boundaries
3. Mechanistic overview
4. Major molecular players and active assemblies
5. Evolutionary and cell-biological variation
6. Constraints, dependencies, and failure modes
7. Controversies and open questions
8. Key references

Include citations for major claims, preferably PMIDs or DOIs. Be explicit about
uncertainty and avoid overgeneralizing from one organism, cell type, or assay
system to all biology.

## Output

# Bacterial preQ1 Incorporation and Queuosine Maturation

*A concise, review-style synthesis for a molecular-biology audience*
*Search date: 2026-07-27. Databases: PubMed. This review is anchored to primary literature and authoritative reviews; PMIDs are given for major claims.*

---

## 1. Executive summary

Queuosine (Q) is a 7-deazaguanosine hypermodification found at the wobble position (nucleotide 34) of the four bacterial and eukaryotic tRNAs that read GUN codons — tRNA(Asp), tRNA(Asn), tRNA(His) and tRNA(Tyr). This review treats the **bacterial four-enzyme module that converts the precursor preQ0 into mature Q on tRNA**: (1) QueF reduces the nitrile of preQ0 to the primary amine preQ1; (2) Tgt (tRNA-guanine transglycosylase) exchanges guanine-34 for preQ1 by base exchange; (3) QueA transfers and isomerizes the ribosyl moiety of *S*-adenosylmethionine (SAM) onto preQ1-tRNA to form epoxyqueuosine (oQ); and (4) an epoxyqueuosine reductase (QueG or, in many lineages, QueH) reduces/deoxygenates oQ to the cyclopentene ring of mature Q (PMID: 39956694, 22787148, 8347586, 27638883, 34652139).

The module is strictly ordered and largely obligatory once the tRNA is committed at the Tgt step. Its defining features are chemically unusual: QueF performs the only known biological nitrile-to-amine reduction (PMID: 22787148); QueA uses SAM in a non-methyl-transfer, ribosyl-transfer role (PMID: 8347586); and the final step is solved by two non-homologous enzymes — cobalamin/[4Fe-4S]-dependent QueG (a Class III cobalamin enzyme related to reductive dehalogenases) or cobalamin-independent QueH (PMID: 26378237, 34652139). The complete de novo route exists **only in bacteria**; eukaryotes are queuine auxotrophs that salvage the free base and insert it with a heterodimeric TGT (PMID: 39956693). The upstream precursor preQ0 (made from GTP by QueC/QueD/QueE) is shared with a distinct **DNA 7-deazaguanine modification** system used in phage/host defense — a neighboring pathway frequently confused with tRNA Q biosynthesis but mechanistically separate (PMID: 25353335, 26929322, 27937735).

---

## 2. Definition and biological boundaries

### 2.1 What is included

The system, as scoped here, is the **post-transcriptional maturation of Q on tRNA in bacteria**, comprising four catalytic steps acting on a common linear intermediate flow:

```
GTP ──(GCYH-I)──▶ dihydroneopterin-P3 ──(QueD)──▶ CPH4 ──(QueE, radical-SAM)──▶ CDG ──(QueC, ATP)──▶ preQ0
preQ0 ──(QueF, NADPH)──────────▶ preQ1                     [free-base chemistry]
G34-tRNA + preQ1 ──(Tgt)───────▶ preQ1-tRNA (34)          [base exchange on tRNA]
preQ1-tRNA + SAM ──(QueA)──────▶ epoxyqueuosine-tRNA (oQ) [on tRNA]
oQ-tRNA ──(QueG or QueH)───────▶ queuosine-tRNA (Q)       [on tRNA]
```

Steps 1–2 up to preQ1 formation are free-base metabolism; steps 3–5 (Tgt insertion, QueA, QueG/H) occur **on the intact tRNA** (PMID: 39956694, 12533518). The four substrate tRNAs (Asp, Asn, His, Tyr) all carry a GUN anticodon with a UGU recognition motif read by Tgt (PMID: 39956694).

### 2.2 Neighboring processes that should be treated separately

- **preQ0 de novo biosynthesis (QueC/QueD/QueE from GTP).** Often bundled with "Q biosynthesis," but chemically upstream and separable; a *Streptomyces* cluster bearing only queC/queD/queE (no queF) accumulates preQ0 as an end-product with no tRNA modification (PMID: 25353335). The provisional brief begins the module at "preQ1 formation," so QueC/D/E are boundary/context rather than core.
- **DNA 7-deazaguanine modification (DpdA/tgtA5 systems).** A paralogous transglycosylase (DpdA) inserts 7-deazaguanine derivatives (dPreQ0, dADG, and phage-specific mdPreQ1/fdPreQ1) into **DNA** for restriction-modification/anti-CRISPR defense in phages and diverse bacteria. It shares the preQ0 precursor and a TGT-fold enzyme but is a different macromolecular target and biological function (PMID: 26929322, 31784519, 37572349, 37503841, 27937735).
- **Archaeosine (G+) biosynthesis in archaea.** Archaeal TGT (ArcTGT) exchanges guanine for preQ0 in the **D-loop (position 15)** of tRNA, not the anticodon, and the downstream chemistry differs entirely (no QueA/QueG). It is a sister branch of the TGT superfamily, not part of the bacterial Q anticodon pathway (PMID: 39956694).
- **Eukaryotic queuine salvage.** Eukaryotes do not synthesize Q; they salvage dietary/microbiota-derived queuine and insert it with a heterodimeric TGT (QTRT1/QTRT2), then require a separate 2'-O-methylation on tRNA(Asp) in some taxa. This is a salvage branch sharing only the base-exchange concept (PMID: 39956693, 35815944).

### 2.3 Competing definitions

Literature varies on where the "Q pathway" starts. Some reviews include GTP→preQ0 (QueC/D/E) as step 1; others (as in this brief) start at preQ1 formation. There is also terminological drift between "QueF" as a specific enzyme and "the nitrile reductase family," and between "queuosine biosynthesis" (bacterial, tRNA) and "deazaguanine modification" (which now spans tRNA and DNA). Being explicit about the target macromolecule (tRNA vs DNA) and the start metabolite (GTP vs preQ0 vs preQ1) resolves most ambiguity.

---

## 3. Mechanistic overview

### 3.1 Best current model of the sequence of events

1. **preQ1 formation (QueF).** QueF catalyzes the NADPH-dependent 4-electron reduction of the nitrile of preQ0 to the primary amine preQ1 — the only nitrile-to-amine reduction known in biology (PMID: 22787148). Catalysis proceeds through a covalent thioimide intermediate on a conserved active-site cysteine (Cys55 in *Bacillus subtilis*; Cys190 in *E. coli*), then a second hydride transfer to the amine; an imine intermediate is sequestered during turnover (PMID: 22787148, 29339556, 23595998). Substrate binding, not thioimide formation, triggers active-site closure (PMID: 22787148).

2. **preQ1 insertion (Tgt).** Bacterial TGT performs an **irreversible base-exchange** by a **double-displacement mechanism** through a covalent enzyme–RNA intermediate (PMID: 12909636). A conserved active-site aspartate is the nucleophile that attacks C1' of ribose-34 after guanine departs (Asp102 in *Zymomonas mobilis*; its Ala mutant is inactive and cannot form the covalent intermediate — PMID: 8961936); a second conserved aspartate (Asp264 in *E. coli*) mediates the proton transfers required to protonate the leaving guanine and deprotonate the incoming base (only the conservative D264E mutant retains activity — PMID: 12909636); and a distinct aspartate (Asp156 in *Z. mobilis*) is the principal preQ1-recognition element in the substrate pocket (PMID: 8961936). The anticodon stem-loop (ASL) bearing the UGU motif is the minimal substrate; full-length tRNA binds with higher affinity through additional contacts with the dimeric enzyme (PMID: 39956694). This is the committed step that places the precursor on the tRNA.

3. **Epoxyqueuosine formation (QueA).** QueA (SAM:tRNA ribosyltransferase-isomerase) forms oQ from preQ1-tRNA in a **single SAM-requiring step**, transferring and isomerizing the ribosyl moiety of SAM (not its methyl group) to build the 2,3-epoxy-4,5-dihydroxycyclopentane ring appended to the preQ1 aminomethyl group (PMID: 8347586). A 17-nt anticodon minihelix suffices as the RNA substrate; measured parameters include Km(SAM)≈101 µM, Km(tRNA)≈1.5 µM, kcat≈2.5 min⁻¹, optimal pH ≈8.7, with mM Mg²⁺/Mn²⁺ inhibitory (PMID: 12533518).

4. **Epoxyqueuosine reduction (QueG or QueH).** The final reduction/deoxygenation converts the epoxide to the cyclopentene, yielding mature Q (PMID: 34652139). QueG is cobalamin- and twin-[4Fe-4S]-dependent, structurally a Class III cobalamin enzyme; it carries a redox chain of two [4Fe-4S] clusters plus base-off cob(II)alamin and is proposed to act via Co–C bond formation with conserved Tyr/Asp acting as proton donors to the epoxide (PMID: 27638883, 26378237). Many organisms that lack QueG use **QueH**, a cobalamin-independent, structurally distinct metalloenzyme catalyzing the same step (PMID: 34652139).

### 3.2 Obligatory, conditional, and accessory steps

- **Obligatory (core):** QueF→Tgt→QueA→(QueG or QueH). Each product is the substrate of the next; skipping any step blocks maturation and leaves a defined intermediate on tRNA (preQ1-tRNA in queA mutants; oQ-tRNA in queG/queH mutants) (PMID: 8347586, 34652139).
- **Conditional / lineage-specific:** The identity of the final reductase (QueG vs QueH) is a non-orthologous alternative — one or the other, depending on lineage (PMID: 34652139).
- **Accessory / bypass:** preQ0/preQ1/queuine **salvage and transport** (e.g., the YhhQ preQ0 transporter and novel salvage enzymes in pathogens) can supply the precursor and bypass early de novo steps, so Tgt activity does not imply full de novo capacity (PMID: 28208705, 31481610).

---

## 4. Major molecular players and active assemblies

| Step | Enzyme | Reaction | Cofactor / chemistry | Assembly | Key refs |
|------|--------|----------|----------------------|----------|----------|
| 1 | **QueF** | preQ0 → preQ1 | NADPH; covalent thioimide on catalytic Cys; only biological nitrile reductase | Tunnel-fold (T-fold) homodecamer (2 head-to-head pentamers), 10 interfacial active sites; "unimodular" and "bimodular" QueF subtypes exist | 22787148, 28300774, 29339556 |
| 2 | **Tgt** | G34 + preQ1 → preQ1-tRNA34 + G | Double-displacement base exchange via covalent Asp102–ribose intermediate (Asp264 proton transfer; Asp156 preQ1 recognition); no cofactor | Homodimer (bacteria); (β/α)8 TIM-barrel + zinc-binding subdomain; ASL/UGU recognition | 39956694, 8961936, 12909636, 21131277 |
| 3 | **QueA** | preQ1-tRNA + SAM → oQ-tRNA | SAM ribosyl transfer + isomerization (non-methyl role) | Monomeric two-domain enzyme; acts on ASL minihelix | 8347586, 12533518 |
| 4 | **QueG** | oQ-tRNA → Q-tRNA | Cobalamin (base-off cob(II)alamin) + two [4Fe-4S]; Co–C bond mechanism; Class III cobalamin enzyme (RdhA-like) | Monomer with redox chain; docks tRNA anticodon | 27638883, 26378237 |
| 4′ | **QueH** | oQ-tRNA → Q-tRNA | Cobalamin-**independent** unique metalloenzyme | Structurally distinct from QueG | 34652139 |
| upstream | **GCYH-I + QueD + QueE + QueC** | GTP → CDG → preQ0 | GTP cyclohydrolase I; QueD = 6-carboxy-5,6,7,8-tetrahydropterin (CPH4) synthase; QueE = radical-SAM CDG synthase (ring rearrangement); QueC = ATP-dependent nitrile synthase (CDG→preQ0) | multi-enzyme | 25353335, 30097106, 28045519 |
| accessory | **YhhQ / salvage enzymes** | preQ0/queuine import & reuse | membrane transporter (COG1738); salvage kinases/glycosylases | — | 28208705, 31481610 |
| eukaryotic salvage | **QTRT1/QTRT2 (eukaryotic TGT)** | G34 + queuine → Q-tRNA34 | base exchange; inserts the free base queuine, not preQ1 | obligate heterodimer | 39956693, 35815944, 21131277 |

**Substrate-specificity logic in TGT.** Divergent evolution tuned the TGT active site to its cognate 7-deazaguanine: bacterial TGT uses a Cys (e.g., Cys145 in *E. coli*) to recognize preQ1, whereas the eukaryotic enzyme substitutes a Val to favor queuine over preQ1 (PMID: 21131277). This single-residue logic is why bacteria insert preQ1 (then mature it in situ) while eukaryotes insert the finished base.

---

## 5. Evolutionary and cell-biological variation

### 5.1 Across evolutionary lineages

- **Bacteria:** full de novo pathway (QueC/D/E→QueF→Tgt→QueA→QueG/H). Final-step reductase is **QueG or QueH** depending on lineage — a textbook non-orthologous gene displacement (PMID: 34652139).
- **Eukaryotes:** no de novo synthesis; queuine auxotrophy with salvage and insertion by heterodimeric QTRT1/QTRT2. In many eukaryotes tRNA(Asp) Q is further modified by 2'-O-mannosyl/galactosyl or ribose methylation, elaborations absent in bacteria (PMID: 39956693).
- **Archaea:** ArcTGT makes archaeosine at D-loop position 15 using preQ0 directly; no anticodon Q pathway (a sister TGT branch) (PMID: 39956694).
- **Phages/mobile elements:** DpdA/tgtA5 paralogs redeploy the deazaguanine transglycosylase chemistry onto **DNA**, inserting preQ0/preQ1-derived bases for defense; these are horizontally transferred and phylogenetically widespread (PMID: 26929322, 31784519, 37572349).

### 5.2 Origin and ancestral representatives

- **Deep origin:** The 7-deazaguanine/deazapurine metabolism is ancient and modular, spanning tRNA (Q, archaeosine) and DNA modification across all domains and their viruses (PMID: 27937735). The TGT fold and the T-fold (QueF/GCYH-I family) are old scaffolds.
- **QueF family:** QueF is evolutionarily derived from the GTP cyclohydrolase I / tunnel-fold (T-fold) superfamily; "unimodular" QueF (single T-fold domain, decameric) versus "bimodular" QueF (two fused T-fold domains, pentameric) subtypes exist, with the unimodular form generally regarded as closer to the ancestral GTP-cyclohydrolase-like architecture (PMID: 22787148, 28300774).
- **Best ancestral representatives:** For understanding the ancestral base-exchange role of TGT, the **bacterial homodimeric Tgt** (e.g., *Zymomonas mobilis*/*E. coli*) is the best-characterized and most representative; the eukaryotic heterodimer and archaeal ArcTGT are derived elaborations with altered substrate/target (PMID: 39956694, 21131277). For the final step, **QueG** was the first characterized and provides the mechanistic template (cobalamin/[4Fe-4S]), while QueH represents an independent, later-recognized solution (PMID: 27638883, 34652139).

### 5.3 Physiological/state variation

Q levels vary with growth phase, precursor (queuine/preQ) availability, and stress; Q at the wobble position tunes decoding speed and fidelity of GUN codons and buffers translation under stress. In eukaryotes, dependence on gut-microbiota-supplied queuine links host translation to the microbiome, and Q loss affects oxidative-stress response, mitochondrial function, and protein folding (PMID: 39956693, 27974624, 36120552). These functional/physiological data derive largely from eukaryotic systems and should not be assumed identical in bacteria.

---

## 6. Constraints, dependencies, and failure modes

- **Strict step order.** Because each enzyme's substrate is the previous product, the sequence QueF→Tgt→QueA→QueG/H is obligatory. QueA cannot act before Tgt has placed preQ1 on tRNA; QueG/H cannot act before QueA has made oQ (PMID: 8347586, 12533518).
- **Commitment and irreversibility at the insertion step.** The Tgt reaction proceeds through a covalent Asp102–ribose intermediate (double displacement); because guanine is physically released and replaced, the base-exchange is effectively unidirectional in vivo, committing that tRNA to maturation (PMID: 8961936, 12909636).
- **On-tRNA constraint.** Only step 1 (QueF) is free-base chemistry. Tgt, QueA, and QueG/H all require the tRNA (or an ASL minihelix) as substrate; this rules out a purely free-base route to mature Q in which Q is synthesized off-tRNA and inserted — bacteria insert preQ1 and mature it *in situ* (PMID: 39956694, 8347586). (Eukaryotes are the exception: they insert the pre-made base queuine, which is why eukaryotic salvage cannot be extrapolated to bacterial mechanism.)
- **Mutually exclusive final enzymes.** QueG and QueH are alternative solutions to the same reaction; an organism's route is determined by which gene it carries (PMID: 34652139).
- **Cofactor dependencies as failure points.** QueF's catalytic Cys is oxidation-prone and is protected in vivo by a conserved intramolecular disulfide; loss of this protection inactivates the enzyme (PMID: 28300774). QueG requires cobalamin and assembled [4Fe-4S] clusters — B12 limitation or defective Fe-S biogenesis can block Q maturation, whereas QueH-using organisms are B12-independent (PMID: 27638883, 34652139).
- **Defined stall intermediates.** Pathway lesions leave diagnostic intermediates on tRNA: preQ1-tRNA accumulates in queA mutants; oQ-tRNA accumulates in queG/queH mutants (PMID: 8347586, 34652139). These are the experimental fingerprints used to order the pathway.
- **Substrate specificity.** TGT selects its 7-deazaguanine by active-site residues (Cys vs Val), so mis-specification (e.g., inserting queuine vs preQ1) is prevented at the insertion step (PMID: 21131277).

---

## 7. Controversies and open questions

**Strongly supported:**
- The four-step logic and the identity/order of QueF, Tgt, QueA, and the epoxyqueuosine reductase are established by enzymology, genetics, and structures (PMID: 22787148, 39956694, 8347586, 27638883).
- QueF's unique nitrile-reduction chemistry and thioimide intermediate (PMID: 22787148, 29339556).
- QueA's single-step SAM ribosyl-transfer/isomerization (PMID: 8347586).
- QueG's cobalamin/[4Fe-4S] redox chain and RdhA relationship (PMID: 26378237, 27638883).

**Debated / indirect / organism-mixing:**
- **Final-step mechanism details.** Whether QueG proceeds strictly via Co–C bond formation with Tyr/Asp proton donors is a structure-based proposal that remains to be fully validated kinetically (PMID: 26378237). QueH's mechanism and metal identity are newly described and not yet resolved to the depth of QueG (PMID: 34652139).
- **Extrapolation across domains.** Much functional data (decoding, stress, disease links) come from eukaryotes, where the pathway is only a salvage branch; applying these phenotypes to bacterial Q biology risks conflating distinct systems (PMID: 39956693, 27974624).
- **QueF architecture and ancestry.** The functional and evolutionary significance of unimodular vs bimodular QueF, and the exact path from GTP cyclohydrolase I to QueF, is inferred from structure/phylogeny rather than ancestral reconstruction (PMID: 22787148, 28300774).
- **Scope of the deazaguanine "arms race."** The full diversity of DNA deazaguanine modifications and their enzymes is still expanding (four new derivatives reported in 2023), so the boundary between "Q pathway" genes and "DNA-defense" paralogs continues to shift (PMID: 37572349).

**Most important open questions:**
1. What is the definitive catalytic mechanism and metal cofactor of QueH, and why did two unrelated enzymes converge on oQ reduction?
2. How is pathway flux regulated in bacteria (precursor sensing, coupling of de novo vs salvage), and how does Q status feed back on translation under stress?
3. What determines tRNA selectivity and the order in which the four isoacceptors are modified in vivo?
4. How ancient is the split between tRNA-Q and DNA-deazaguanine functions, and which extant enzyme best represents the ancestral transglycosylase?

---

## 8. Key references

- Ehrenhofer-Murray, A.E. *Queuine: A Bacterial Nucleobase Shaping Translation in Eukaryotes.* 2025. **PMID: 39956693** — scope, bacteria-only de novo pathway, eukaryotic auxotrophy, function.
- Reuter, K. & Ficner, R. *RNA-modification by Base Exchange: Structure, Function and Application of tRNA-guanine Transglycosylases.* 2025. **PMID: 39956694** — TGT mechanism, ASL/UGU recognition, DpdA.
- Chikwana, V.M. et al. *Structural basis of biological nitrile reduction.* PNAS 2012. **PMID: 22787148** — QueF structure, thioimide, decamer, unique nitrile reductase.
- Mohammad, A. et al. *Protection of QueF from Irreversible Oxidation by a Conserved Intramolecular Disulfide.* 2017. **PMID: 28300774** — NADPH mechanism, catalytic-Cys redox protection.
- Jung, J. & Nidetzky, B. *Evidence of a sequestered imine intermediate during reduction of nitrile to amine by QueF.* 2018. **PMID: 29339556** — reaction intermediates.
- Chen, Y.-C. et al. *Evolution of eukaryal tRNA-guanine transglycosylase…* 2011. **PMID: 21131277** — TGT substrate specificity (Cys145 vs Val), divergent evolution.
- Romier, C. et al. *Mutagenesis and crystallographic studies of Z. mobilis TGT reveal aspartate 102 as the active site nucleophile.* 1996. **PMID: 8961936** — covalent Asp102-ribose intermediate; Asp156 preQ1 recognition.
- Kittendorf, J.D. et al. *An essential role for aspartate 264 in catalysis by TGT from E. coli.* 2003. **PMID: 12909636** — double-displacement mechanism, Asp264 proton transfer.
- Lewis, W.G. (Lewis, Bruender, Bandarian). *QueE: A Radical SAM Enzyme Involved in the Biosynthesis of 7-Deazapurine Containing Natural Products.* 2018. **PMID: 30097106** — GTP→CDG via GCYH-I/QueD/QueE.
- Bruender, N.A. et al. *7-Carboxy-7-deazaguanine Synthase: A Radical SAM Enzyme with Polar Tendencies.* 2017. **PMID: 28045519** — QueE radical-SAM mechanism.
- Slany, R.K. et al. *The ribosyl moiety of AdoMet is the precursor of the cyclopentenediol moiety of queuine.* 1993. **PMID: 8347586** — QueA single-step SAM ribosyl transfer/isomerization.
- Van Lanen, S.G. et al. *tRNA modification by SAM:tRNA ribosyltransferase-isomerase.* 2003. **PMID: 12533518** — QueA kinetics, ASL minihelix substrate.
- Dowling, D.P. et al. *Molecular basis of cobalamin-dependent RNA modification.* PNAS 2016. **PMID: 27638883** — QueG cobalamin/[4Fe-4S], tRNA-bound structures.
- Payne, K.A.P. et al. *Epoxyqueuosine Reductase Structure Suggests a Mechanism for Cobalamin-dependent tRNA Modification.* 2015. **PMID: 26378237** — QueG redox chain, RdhA homology, Co–C proposal.
- Li, X. et al. *Epoxyqueuosine Reductase QueH … Is a Unique Metalloenzyme.* 2021. **PMID: 34652139** — cobalamin-independent QueH alternative for the final step.
- Xu, F. et al. *PreQ0 base … from Streptomyces qinglanensis.* 2015. **PMID: 25353335** — queC/queD/queE suffice for preQ0.
- Thiaville, J.J. et al. *Novel genomic island modifies DNA with 7-deazaguanine derivatives.* 2016. **PMID: 26929322** — tgtA5/DpdA DNA modification, shared preQ0.
- Hutinet, G. et al. *7-Deazaguanine modifications protect phage DNA from host restriction systems.* Nat Commun 2019. **PMID: 31784519** — DNA deazaguanine defense function.
- Hutinet, G., Swarjo, M.A., de Crécy-Lagard, V. *Deazaguanine derivatives, examples of crosstalk between RNA and DNA modification pathways.* 2017. **PMID: 27937735** — RNA/DNA crosstalk and plasticity.
- Cui, W. et al. *Four additional natural 7-deazaguanine derivatives in phages…* 2023. **PMID: 37572349** — expanding DNA modification diversity.
- Zallot, R., Yuan, Y., de Crécy-Lagard, V. *The E. coli COG1738 Member YhhQ Is Involved in preQ0 Transport.* 2017. **PMID: 28208705** — precursor transport/salvage.
- Yuan, Y. et al. *Discovery of novel bacterial queuine salvage enzymes and pathways in human pathogens.* 2019. **PMID: 31481610** — bacterial salvage routes.
- Tuorto, F. & Lyko, F. *Genome recoding by tRNA modifications.* 2016. **PMID: 27974624** — anticodon-loop modifications and decoding.

---

### Limitations of this review

This synthesis was assembled from PubMed abstracts and authoritative reviews within a constrained iteration budget; it did not perform full-text extraction, citation-network chaining, or PRISMA-style screening. Quantitative claims (kinetic constants, structural details) are reproduced from the primary abstracts and should be verified against full texts before use in a formal publication. Functional/phenotypic statements drawn from eukaryotic systems are flagged and should not be generalized to bacteria without direct evidence.


## Artifacts

- [OpenScientist final report](bacterial_preq1_incorporation_queuosine_maturation-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](bacterial_preq1_incorporation_queuosine_maturation-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:39956694
2. PMID:22787148
3. PMID:8347586
4. PMID:26378237
5. PMID:39956693
6. PMID:25353335
7. PMID:26929322
8. PMID:12909636
9. PMID:8961936
10. PMID:12533518
11. PMID:34652139
12. PMID:27638883
13. PMID:28208705
14. PMID:21131277
15. PMID:27937735
16. PMID:28300774
17. PMID:37572349
18. PMID:29339556
19. PMID:30097106
20. PMID:28045519
21. PMID:31784519
22. PMID:31481610
23. PMID:27974624