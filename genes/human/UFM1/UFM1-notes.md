# UFM1 research notes

UniProt: P61960 (UFM1_HUMAN). 85 aa precursor; mature chain 1..83 after removal of C-terminal Ser-Cys (Gly-83 exposed). Ubiquitin-fold modifier 1.

## Core identity
UFM1 is a metazoan-specific ubiquitin-like protein modifier (Ubl). It is itself the **tag/modifier**, NOT an enzyme. Its molecular function is `protein tag activity` (GO:0031386) — it is covalently conjugated via an isopeptide bond from its C-terminal Gly-83 to lysine residues of substrate proteins.

- [PMID:15071506 "The C-terminally processed Ufm1 is activated by a novel E1-like enzyme, Uba5, by forming a high-energy thioester bond. Activated Ufm1 is then transferred to its cognate E2-like enzyme, Ufc1, in a similar thioester linkage."] — establishes the E1(UBA5)→E2(UFC1)→substrate cascade; UFM1 is the conjugated modifier.
- UniProt FUNCTION: "Ubiquitin-like modifier which can be covalently attached via an isopeptide bond to lysine residues of substrate proteins as a monomer or a lysine-linked polymer." Ufmylation requires E1 UBA5, E2 UFC1, E3 UFL1.

## Principal substrate / biological role
- **RPL26 (uL24) is the principal target of UFMylation**, on ER-bound ribosomes. [PMID:30626644 "a largely uncharacterized ribosomal protein, RPL26, is the principal target of UFM1 conjugation. RPL26 UFMylation and de-UFMylation is catalyzed by enzyme complexes tethered to the cytoplasmic surface of the ER and UFMylated RPL26 is highly enriched on ER membrane-bound ribosomes and polysomes."]
- UFMylation facilitates co-translational protein biogenesis at the ER and 60S ribosomal subunit recycling from the ER. [PMID:38383785 "UFM1 E3 ligase promotes recycling of 60S ribosomal subunits from the ER."]
- ER-phagy (reticulophagy) and response to ER stress depend on ER-resident UFMylation [PMID:32160526 genome-wide ER-phagy screen — ER-resident UFMylation].

## Self-ufmylation / poly-UFM1
- UFM1 can be conjugated as a monomer or a Lys-linked polymer; K69 is a UFM1-UFM1 linkage site (autoufmylation). GOA: GO:1990592 protein K69-linked ufmylation (IDA, PMID:25219498). CROSSLNK 69 "Glycyl lysine isopeptide ... interchain with G-Cter in UFM1".

## Other reported roles (more peripheral / substrate-context)
- ASC1 (TRIP4) ufmylation regulates ERα transactivation and breast cancer (PMID:25219498) — GO:0033146 regulation of intracellular estrogen receptor signaling pathway (IDA). Substrate-specific context.
- Brain development / disease: biallelic UFM1 (and UFC1) mutations cause hypomyelinating leukodystrophy HLD14; the R81C variant decreases thioester formation with UBA5/UFC1 and decreases ufmylation [PMID:29868776]. GO:0007420 brain development (IMP). This is a downstream organismal phenotype of impaired ufmylation.
- PD-1 UFMylation in T cells (PMID:38377992) — substrate context.
- Negative regulation of protein import into nucleus (GO:0042308 IMP PMID:28393202, CACAO) — single low-throughput annotation; peripheral.
- Negative regulation of apoptotic process (GO:0043066 ISS/IEA) — transferred, weak.

## Localization
- Nucleus and Cytoplasm (UniProt SUBCELLULAR LOCATION, PMID:15071506, IDA). Acts especially at ER-bound ribosomes (cytoplasmic surface of ER). ER localization annotations (IEA/ISS) reflect site of action of the ufmylation machinery; UFM1 itself is a soluble Ubl that is recruited there.

## Interactions (IPI protein binding annotations)
The GOA `protein binding` IPI rows are mostly with UBA5 (Q9GZZ9; the E1 — the functionally meaningful, recurrent partner), plus S100A6 (P06703), INCA1 (Q0VD86), KCTD21 (Q4G0X4), CDK5RAP3/Q96JB5, and Q8VE47 (mouse Lztr1?). The UBA5 interaction underpins activation (thioester transfer). Others are high-throughput / single-screen.

## Action plan
- Core MF: GO:0031386 protein tag activity (covalent modifier). Core BP: GO:0071569 protein ufmylation.
- Localizations cytoplasm/nucleus/ER: ACCEPT or KEEP_AS_NON_CORE; ER reflects site of action.
- protein binding IPI rows: KEEP_AS_NON_CORE (UBA5) or MODIFY/MARK_AS_OVER_ANNOTATED for uninformative singletons.
- Brain development, ER-phagy, ER stress, neg reg apoptosis, neg reg nuclear import, ER signaling: KEEP_AS_NON_CORE (downstream/substrate-specific) — keep ufmylation as the core.
</content>

## 2026-11-06 ORGANELLES ER batch 4 (endoplasmic reticulum rows)

- Rows: GO:0005783 IEA (GO_REF:0000107, Ensembl projection from mouse) and ISS (GO_REF:0000024, from mouse P61961), both located_in. Both were KEEP_AS_NON_CORE.
- Source: mouse Ufm1 GO:0005783 IDA from PMID:21494687 (QuickGO, 2026-11-06). Full text read: endogenous UFM1 in MIN6 fractions with GDH, LAMP2, BiP and HSPA8 markers [PMID:21494687 "It is clear that UFBP1 was present in the same fraction as BiP, indicative for ER localization"; "UFM1 partially co-localized with UFBP1 in the ER, but a significant amount of UFM1 protein was detected in the cytosolic fraction"]. Mouse and human UniProt list only Nucleus and Cytoplasm.
- Site of the principal function: [PMID:30626644 "UFMylated RPL26 is highly enriched on ER membrane-bound ribosomes and polysomes"] (abstract).
- Topology: 85-residue soluble modifier, held at the ER cytosolic face through UFBP1/DDRGK1 and the ER-tethered ligase; stays at root, no membrane or lumen row.
- Outcome: both rows KEEP_AS_NON_CORE -> ACCEPT, because the core activity (RPL26 UFMylation) is shown at the ER and core_functions already names the ER (this also clears two "location not reflected" validator warnings). Alternative: KEEP_AS_NON_CORE, since most free UFM1 is cytosolic/nuclear. Old reasons that cited a quote about the ligase complexes were replaced by quotes about UFM1 itself.
