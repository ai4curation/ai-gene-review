"""Apply the independently adjudicated new-member decisions, preserving seed payloads."""

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
A = Path(__file__).resolve().parent
P = A.parent / "preflight"
BASE = json.loads((A / "baseline.json").read_text())
TERMS = {
    x["id"]: x["name"]
    for x in json.loads((A / "go-definitions.json").read_text())["results"]
}


def term(number):
    key = f"GO:{number:07d}"
    return {"id": key, "label": TERMS[key]}


def norm(text):
    return " ".join(text.split())


def support(pmid, quote):
    source = ROOT / f"publications/PMID_{pmid}.md"
    assert norm(quote) in norm(source.read_text()), (pmid, quote)
    return {"reference_id": f"PMID:{pmid}", "supporting_text": quote}


RELAY = support(
    16387657,
    "Efficient 2-thiouridine formation in vitro was reconstituted with recombinant TusA, a TusBCD complex, TusE, and previously identified IscS and MnmA.",
)
STIM = support(
    16387657,
    "The desulfurase activity of IscS is stimulated by TusA binding. IscS transfers the persulfide sulfur to TusA.",
)
TUSE = support(
    16387657,
    "TusE binds TusBCD complex and stimulates sulfur transfer from TusA to TusD. TusE also interacts with an MnmA-tRNA complex.",
)
BCD = support(
    16472754,
    "Here, we solved the 2.15 angstroms crystal structure of the E. coli TusBCD complex, a sulfur transfer mediator, forming a heterohexamer composed of a dimer of the heterotrimer.",
)
DCYS = support(
    16472754,
    "In vivo mutant analyses revealed that only Cys78, in the TusD subunit, participates in sulfur transfer during the s2U modification process.",
)
LIMIT = support(
    39660893,
    "Consequently, proof that TusE transfers the persulfide directly to MnmA in E. coli remains to be definitively provided.",
)
ECACT = support(
    12549933,
    "The activity requires MnmA, Mg-ATP, l-cysteine, and the cysteine desulfurase IscS.",
)
ECPROD = support(
    12549933,
    "HPLC analysis of thiolated tRNA digests using [(35)S]cysteine confirms that the product of the in vitro reaction is s(2)U.",
)
BS = support(
    25825430,
    "In vitro experiments demonstrated s(2)U formation by YrvO and MnmA, and kinetic analysis established a partnership between the B. subtilis proteins that is contingent upon the presence of ATP.",
)
TT = support(
    31801798,
    "In the absence of reductant, s2U was readily formed by the cysteine desulfurases using cysteine as the sulfur donor.",
)
TTLIMIT = support(
    31801798,
    "although indirect sulfur transfer via unidentified sulfur-carrier protein(s) could exist.",
)
FUR = support(
    38916309,
    "We were able to reveal that the increased iron levels in the ∆tusA mutant strain are mainly due to the reduced translation of fur mRNA, the main regulator of Fe homeostasis in E. coli.",
)
MOCO = support(
    23281480,
    "Whether TusA acts as a direct sulfur donor to provide the sulfur to MoeB/MoaD for Moco biosynthesis or other proteins like YnjE are involved as mediators in this reaction has to be investigated further in future studies.",
)
CYTO = support(
    10830496,
    "Western blotting showed that the hypothetical yhhP gene is indeed transcribed and translated as a minor cytoplasmic protein.",
)
PROTEOME = support(
    18304323,
    "we identified 1103 proteins from the cytosolic fraction of the Escherichia coli strain MC4100.",
)
T54 = support(
    16547008,
    "The addition of cysteine desulfurases such as IscS (TTC0087) or SufS (TTC1373) enhances the sulfur transfer reaction in vitro.",
)

FINDINGS = {
    RELAY[
        "supporting_text"
    ]: "Recombinant E. coli sulfur-relay components reconstitute U34 thiolation; the result supports participation beyond mutant necessity.",
    STIM[
        "supporting_text"
    ]: "TusA accepts persulfide sulfur and stimulates IscS, supporting sulfur carriage and a direct contribution to cysteine breakdown.",
    TUSE[
        "supporting_text"
    ]: "TusE promotes transfer within TusBCD and interacts with MnmA–tRNA; this does not directly demonstrate covalent loading of MnmA.",
    BCD[
        "supporting_text"
    ]: "E. coli TusBCD is a structurally characterized heterohexamer, distinguishing structural subunits from independent catalytic proteins.",
    DCYS[
        "supporting_text"
    ]: "Mutant evidence implicates TusD Cys78 rather than the candidate TusC cysteine in sulfur transfer.",
    LIMIT[
        "supporting_text"
    ]: "The 2025 critical review identifies the terminal TusE-to-MnmA covalent handoff as unresolved.",
    ECACT[
        "supporting_text"
    ]: "The E. coli MnmA reaction requires ATP and a cysteine-derived sulfur source in the reported in-vitro system.",
    ECPROD[
        "supporting_text"
    ]: "The in-vitro E. coli reaction product is chemically identified as 2-thiouridine.",
    BS[
        "supporting_text"
    ]: "The cognate B. subtilis YrvO–MnmA pair directly reconstitutes ATP-dependent thiolation; native and heterologous evidence are separated in the source review.",
    TT[
        "supporting_text"
    ]: "HB27 IscS and SufS each support reconstituted MnmA thiolation after reductants are removed, establishing donor capacity rather than exclusive native assignment.",
    FUR[
        "supporting_text"
    ]: "TusA-dependent iron phenotypes include a causal change in Fur translation, rather than demonstrating direct cluster incorporation by TusA.",
    MOCO[
        "supporting_text"
    ]: "TusA contributes to sulfur allocation for Moco, while the immediate MPT sulfur acceptor and intervening mediators remain unresolved.",
    CYTO[
        "supporting_text"
    ]: "The original YhhP/TusA study reports a minor cytoplasmic protein; the specific curated cytosolic assignment is retained with soluble-reaction context.",
    PROTEOME[
        "supporting_text"
    ]: "The source is MC4100 cytosolic proteomics; MnmA's existing experimental assignment is retained without claiming independent peptide reidentification.",
    T54[
        "supporting_text"
    ]: "The same named Thermus donor loci also enhance a distinct TtuA/TtuB-dependent U54 reaction; that reaction is not attributed to MnmA.",
    "Twenty-six mutants, classified in the “Central Dogma,” exhibited sensitivity to BA": "MnmA/trmU occurs in a broad boric-acid-sensitive central-dogma mutant group, supporting a non-core stress phenotype rather than an acid-specific catalytic role.",
    "For the cysteine desulfurase coupled reactions, 0.1 mM Cys, 20 µM pyridoxal phosphate, and 75 pmol of IscS or SufS were included in the reaction mixture.": "The identified Thermus desulfurases were tested in a PLP-containing cysteine-fed reaction, consistent with their specific desulfurase signatures and catalytic cofactor.",
}

DESCRIPTIONS = {
    "ECOLI/tusA": "TusA is a small cytosolic sulfur-carrier protein that accepts persulfide sulfur from the cysteine desulfurase IscS and supplies the TusBCD/TusE relay for C2 thiolation of tRNA wobble uridine. Binding of TusA stimulates IscS activity. TusA also helps direct sulfur toward molybdenum-cofactor biosynthesis; its effects on iron-sulfur cluster abundance and iron homeostasis include indirect changes in Fur translation and sulfur-mobilization regulation.",
    "ECOLI/tusB": "TusB is a structural subunit of the cytoplasmic TusBCD sulfur-relay complex that participates in C2 thiolation of tRNA wobble uridine. Two copies each of TusB, TusC and TusD form a heterohexamer. TusB supports the sulfur-transfer assembly, whereas the experimentally implicated sulfur-bearing cysteine is on TusD.",
    "ECOLI/tusC": "TusC is a structural subunit of the cytoplasmic TusBCD sulfur-relay complex involved in C2 thiolation of tRNA wobble uridine. The complex contains two copies each of TusB, TusC and TusD. Although TusC contains a candidate exposed cysteine, the tested essential sulfur-transfer residue is TusD Cys78; TusC is not assigned independent covalent sulfur-carrier chemistry.",
    "ECOLI/tusD": "TusD is the sulfur-bearing subunit of the cytosolic TusBCD heterohexamer, which mediates sulfur transfer during C2 thiolation of tRNA wobble uridine. Sulfur from TusA enters the complex through the functionally implicated TusD Cys78 and proceeds through the TusE-dependent terminal reaction with MnmA and tRNA.",
    "ECOLI/tusE": "TusE is a cytoplasmic sulfur-relay protein involved in C2 thiolation of tRNA wobble uridine. It interacts with TusBCD, stimulates sulfur transfer from TusA to TusD, and associates with the MnmA–tRNA reaction. Its sulfur-carrier role is supported, while direct transfer of a TusE persulfide onto an MnmA cysteine has not been conclusively demonstrated.",
    "ECOLI/mnmA": "MnmA is a cytosolic ATP-dependent tRNA-uridine 2-sulfurtransferase that incorporates sulfur at C2 of wobble uridine in tRNAs for lysine, glutamate and glutamine. It activates U34 by adenylation and couples sulfur utilization to the IscS/Tus sulfur-relay system. The physiological requirement for an iron-sulfur cofactor in this D-type MnmA and the chemistry of the terminal sulfur handoff remain unresolved.",
    "BACSU/iscS1": "IscS1, also called YrvO, is a pyridoxal-phosphate-dependent cysteine desulfurase that mobilizes sulfur from L-cysteine for its cognate tRNA thiouridylase MnmA. The Bacillus subtilis YrvO–MnmA pair supports ATP-dependent C2 thiolation of tRNA wobble uridine without the Escherichia coli Tus relay. This dedicated sulfur-delivery role does not imply that IscS1 is a general iron-sulfur scaffold or the universal donor for all cellular sulfur pathways.",
    "BACSU/mnmA": "MnmA is an ATP-dependent tRNA-uridine 2-sulfurtransferase that introduces sulfur at C2 of wobble uridine. In Bacillus subtilis it works with the adjacent cysteine desulfurase YrvO/IscS1 through an abbreviated sulfur-delivery pathway. Biochemical reconstitution and genetic complementation support this cognate pair, distinct from the Tus-dependent relay of Escherichia coli.",
    "THET2/mnmA": "MnmA of Thermus thermophilus HB27 is a C-type ATP-dependent tRNA-uridine 2-sulfurtransferase. Its characterized reconstituted [4Fe–4S] form catalyzes C2 thiolation of tRNA wobble uridine. Purified IscS or SufS can supply cysteine-derived sulfur to this reaction without added reductants; the physiological choice of donor and possible additional carriers remain unresolved.",
    "THET2/TT_C0087": "TT_C0087 encodes the Thermus thermophilus HB27 IscS cysteine desulfurase, a pyridoxal-phosphate-dependent enzyme that mobilizes sulfur from L-cysteine. Purified IscS supports sulfur incorporation into tRNA U34 in a reaction with reconstituted MnmA. This biochemical donor capacity does not establish that IscS is the sole native donor or exclude intervening carriers in the cell.",
    "THET2/TT_C1373": "TT_C1373 encodes the Thermus thermophilus HB27 SufS cysteine desulfurase. It uses pyridoxal phosphate to mobilize sulfur from L-cysteine, and purified SufS supports C2 thiolation of tRNA wobble uridine by reconstituted MnmA. Its physiological allocation between sulfur pathways and its relative contribution compared with IscS remain unresolved.",
}
for donor in ("TT_C0087", "TT_C1373"):
    DESCRIPTIONS[f"THET2/{donor}"] += (
        " The same named donor also enhances the separate TtuA/TtuB-dependent tRNA U54 thiolation reaction in vitro."
    )


def review(action, reason, refs, replacement=None):
    result = {
        "summary": reason.split(". ")[0].rstrip(".") + ".",
        "action": action,
        "reason": reason,
        "supported_by": refs,
    }
    if replacement:
        result["proposed_replacement_terms"] = [term(replacement)]
    return result


def primary_for(org, gene):
    if org == "BACSU":
        return [BS]
    if org == "THET2":
        return [TT, T54] if gene != "mnmA" else [TT]
    if gene == "mnmA":
        return [ECACT, ECPROD]
    if gene in {"tusB", "tusC", "tusD"}:
        return [RELAY, BCD, DCYS]
    if gene == "tusE":
        return [TUSE, LIMIT]
    return [RELAY, STIM]


def adjudicate(org, gene, row):
    tid = row["term"]["id"]
    primary = primary_for(org, gene)
    source = row["original_reference_id"]
    if tid == "GO:0005515":
        return review(
            "REMOVE",
            f"The IscS interaction reported by {source} is biologically relevant, but bare protein binding does not describe TusA's sulfur-carrier mechanism. Remove this uninformative term under the protein-binding policy, not as a denial of interaction or a duplicate-row deletion. The specific carrier and IscS–TusA complex annotations are retained.",
            [STIM],
        )
    if tid == "GO:0016226":
        return review(
            "MARK_AS_OVER_ANNOTATED",
            "The full PMID:38916309 study establishes effects of TusA loss on Fe-S abundance and iron homeostasis, but traces them through reduced Fur translation, iron accumulation and changes in sulfur-mobilization regulation. GO:0016226 describes incorporation of iron and sulfur into a cluster. A pleiotropic requirement and modulation of IscS availability do not establish that TusA performs that incorporation step. This is an overextended process assignment, not a claim that the experimental phenotype is false or that TusA can never affect assembly.",
            [FUR],
        )
    if tid == "GO:0006777":
        return review(
            "ACCEPT",
            "TusA has a supported sulfur-distribution role in molybdenum-cofactor biosynthesis, supported by MPT/cPMP and molybdoenzyme phenotypes together with its IscS sulfur-carrier chemistry. The full PMID:23281480 study explicitly leaves direct donation to MoeB/MoaD versus an intervening carrier unresolved; it does not establish an obligatory TusA-only route. The later iron-regulatory effects do not negate the supported sulfur-distribution role.",
            [STIM, MOCO],
        )
    if tid == "GO:0019448":
        if gene == "tusA":
            return review(
                "ACCEPT",
                "TusA contributes directly to the sulfur-mobilizing breakdown of L-cysteine by stimulating IscS and accepting the released sulfur, as explicitly reported in PMID:16387657 and supported by the full PMID:23281480 activity study. This is a cofactor/acceptor contribution to the reaction, not an assertion that TusA itself has cysteine desulfurase activity or a conclusion from knockout necessity alone.",
                [STIM],
            )
        return review(
            "ACCEPT",
            "The characterized SufS protein mobilizes sulfur from L-cysteine in the MnmA-coupled reaction. This is direct cysteine breakdown chemistry, independently supporting the existing InterPro inference; it is not evidence that SufS is the sole physiological U34 sulfur donor.",
            [TT],
        )
    if tid == "GO:0097532":
        return review(
            "KEEP_AS_NON_CORE",
            "The full PMID:38466471 boric-acid study reports sensitivity of the trmU/mnmA mutant in a broad central-dogma mutant screen. Retain this experimentally supported stress-response context as non-core; the demonstrated molecular role is tRNA thiolation, not acid neutralization or a dedicated acid-sensing activity. No additional stress mechanism is inferred from sensitivity alone.",
            [
                support(
                    38466471,
                    "Twenty-six mutants, classified in the “Central Dogma,” exhibited sensitivity to BA",
                )
            ],
        )
    if tid == "GO:0030170":
        return review(
            "ACCEPT",
            "PLP is an integral cofactor of the characterized SufS desulfurase rather than peripheral binding. The HB27 protein's specific SufS/desulfurase signatures and the PLP-containing cysteine-fed reconstitution support the existing inference. This does not rely solely on the ARBA cofactor text or transfer a chloroplast localization from the family name.",
            [
                support(
                    31801798,
                    "For the cysteine desulfurase coupled reactions, 0.1 mM Cys, 20 µM pyridoxal phosphate, and 75 pmol of IscS or SufS were included in the reaction mixture.",
                )
            ],
        )
    if tid == "GO:0031071":
        if org == "BACSU":
            reason = "The PS832/168-lineage YrvO protein is the seeded IscS1 homolog and has direct cysteine-desulfurase and sulfur-donation support in PMID:25825430. The YrvO–MnmA pair acts in U34 thiolation; this validates the shared catalytic claim independently of the electronic or ISS source and does not transfer every function of the SufS donor P0A6B9. The original assay-to-reference-strain bridge is explicit in the identity evidence."
        else:
            reason = "The official HB27 locus identity and PMID:31801798 reconstitution identify this protein as the assayed IscS or SufS sulfur donor. Cysteine-derived sulfur supports MnmA-catalyzed U34 thiolation even after reductants are removed. Accept the desulfurase chemistry without claiming a uniquely assigned native U34 route, a measured complete native flux, or generic Fe-S assembly participation."
        return review("ACCEPT", reason, primary)
    if tid in {"GO:0006400", "GO:0008033"}:
        return review(
            "MODIFY",
            "The general tRNA modification/processing claim is correct, but the supported step is specifically C2 thiolation of wobble uridine, GO:0002143, already present in this review. Refine to that supported descendant. The protein performs catalytic sulfur transfer or supplies the characterized relay structure, rather than merely being a substrate or producing an indirect phenotype.",
            primary,
            2143,
        )
    if tid == "GO:0002143":
        reason = "The protein participates in the reconstituted U34 C2-thiolation mechanism, beyond the original necessity phenotype. "
        if gene in {"tusB", "tusC"}:
            reason += "Its contribution is the positively characterized TusBCD assembly; the sulfur-bearing residue identified by mutagenesis is on TusD, so no autonomous carrier activity is inferred for this subunit."
        elif org == "BACSU":
            reason += "The native PS832/168-lineage evidence and cognate YrvO–MnmA biochemistry support this abbreviated route; heterologous E. coli complementation is distinguished from the Bacillus experiment."
        elif org == "THET2":
            reason += "The target is HB27 TT_C1727, not the distinct HB8 protein. Purified reconstituted MnmA catalyzes the reaction; the donor comparison establishes in-vitro capacity without resolving physiological donor choice."
        elif gene == "tusE":
            reason += "TusE stimulates transfer within TusBCD and associates with the MnmA–tRNA reaction, but direct covalent loading of MnmA by TusE remains unproven."
        else:
            reason += "The catalytic or sulfur-carrier role is supported by biochemistry as well as genetics; the mechanistic limits of terminal sulfur delivery do not invalidate process participation."
        return review("ACCEPT", reason, primary)
    if tid in {"GO:0016740", "GO:0016783"}:
        if gene == "tusD":
            return review(
                "ACCEPT",
                "TusD is the sulfur-transfer subunit of the characterized TusBCD complex, with Cys78 implicated by mutagenesis. GO:0016783 is supported as complex-dependent sulfur transfer; GO:0097163 separately captures covalent carriage and is not a descendant of GO:0016783. Neither the mapping nor the core asserts an independently measured isolated-enzyme turnover cycle.",
                [BCD, DCYS],
            )
        return review(
            "MODIFY",
            "The transferase/sulfurtransferase claim is correct but the characterized substrate and position support tRNA-uridine 2-sulfurtransferase activity, GO:0103016, already present in this review. Refine to this specific descendant without inventing a new annotation or assuming one cofactor mechanism for all MnmA homologs.",
            primary,
            103016,
        )
    if tid == "GO:0103016":
        return review(
            "ACCEPT",
            "The target-specific biochemical evidence establishes ATP-dependent sulfur incorporation at C2 of tRNA U34. Accept the precise catalytic function. The reaction identity does not settle every terminal sulfur-transfer intermediate or imply that the Thermus cluster requirement applies to E. coli or Bacillus MnmA.",
            primary,
        )
    if tid == "GO:0097163":
        if gene == "tusA":
            return review(
                "ACCEPT",
                "TusA covalently accepts persulfide sulfur from IscS and supplies the downstream relay, directly matching the sulfur-carrier definition. Independent biochemistry supports the electronic mapping as well as the experimental row.",
                [STIM, RELAY],
            )
        if gene == "tusD":
            return review(
                "ACCEPT",
                "The TusD subunit supplies the implicated Cys78 sulfur-transfer site within TusBCD. The covalent carrier interpretation is supported by the relay study and site-specific mutant evidence; this is not a claim that every TusBCD subunit independently carries sulfur.",
                [DCYS, RELAY],
            )
        return review(
            "ACCEPT",
            "Retain the experimentally curated sulfur-carrier role of TusE and its conserved relay assignment, supported by the reconstituted pathway, TusBCD stimulation and MnmA–tRNA interaction. This does not turn the proposed direct TusE-persulfide-to-MnmA-cysteine handoff into an established molecular intermediate; the 2025 critical review explicitly leaves that step unresolved.",
            [TUSE, RELAY, LIMIT],
        )
    if tid == "GO:1990329":
        return review(
            "ACCEPT",
            "TusA binds IscS in the sulfur-mobilizing complex and stimulates its catalytic activity; this is the mechanistically informative complex annotation corresponding to the nonspecific interaction rows. No generalized protein-binding function is needed to capture this role.",
            [STIM],
        )
    if tid == "GO:1990228":
        if org == "BACSU":
            return review(
                "UNDECIDED",
                "GO:1990228 denotes a generic sulfurtransferase protein complex, not specifically the E. coli TusBCD assembly, so absence of Tus proteins does not refute it. PMID:25825430 establishes an ATP-dependent YrvO–MnmA partnership and direct sulfur delivery, but the consulted evidence does not independently establish the physical assembly underlying this inherited component annotation. Retain uncertainty about complex membership while accepting the demonstrated catalytic pair; neither partner absence nor a requirement for permanent association is asserted.",
                [BS],
            )
        if gene in {"tusB", "tusC", "tusD"}:
            return review(
                "ACCEPT",
                "The crystal structure and biochemical reconstitution establish membership of TusBCD, a heterohexamer with two copies of each subunit. GO:1990228 describes the sulfur-transfer complex; the direct structure supports the inherited node assertion without counting extant donors as phylogenetic evidence.",
                [BCD, RELAY],
            )
        return review(
            "ACCEPT",
            "The relay study supports association with the sulfur-transfer reaction assembly, including the MnmA–tRNA/TusE interaction. Retain the experimentally curated component claim without claiming that TusE or MnmA is a constitutive subunit of the structurally defined TusBCD heterohexamer, or that all proteins form one permanently stable complex.",
            [TUSE, RELAY],
        )
    if tid == "GO:0005737":
        if gene in {"tusA", "tusD", "mnmA"} and org == "ECOLI":
            refs = (
                [CYTO] if gene == "tusA" else [PROTEOME] if gene == "mnmA" else primary
            )
            return review(
                "MODIFY",
                "Cytoplasmic localization is correct; the soluble cytosolic sulfur relay and tRNA substrate context support the more specific cytosol term already carried by this gene. This refinement does not assert a newly measured fractionation experiment: the original localization evidence, characterized soluble protein and intracellular tRNA reaction are considered together.",
                refs,
                5829,
            )
        return review(
            "ACCEPT",
            "A cytoplasmic site is consistent with the soluble characterized protein and its intracellular tRNA sulfur-transfer reaction. This is a localization inference from the catalytic/structural context, not a new target-specific fractionation measurement; retain the existing general compartment rather than fabricate a finer localization assay.",
            primary,
        )
    if tid == "GO:0005829":
        refs = [CYTO] if gene == "tusA" else [PROTEOME] if gene == "mnmA" else primary
        return review(
            "ACCEPT",
            "Retain the curated cytosolic assignment, consistent with the soluble protein and its tRNA sulfur-transfer reaction. For the proteomic/localization sources this preserves the original curator's target assignment rather than claiming a target peptide was independently reidentified; for the inherited TusD row it is a conserved compartment inference, not a donor-count argument.",
            refs,
        )
    raise ValueError((org, gene, tid))


def build_core(org, gene):
    core = {
        "description": DESCRIPTIONS[f"{org}/{gene}"],
        "supported_by": primary_for(org, gene),
    }
    if gene in {"tusB", "tusC"}:
        core["contributes_to_molecular_function"] = term(16783)
    elif gene in {"tusA", "tusD", "tusE"}:
        core["molecular_function"] = term(97163)
    elif gene == "mnmA":
        core["molecular_function"] = term(103016)
    else:
        core["molecular_function"] = term(31071)
    core["directly_involved_in"] = [term(2143)]
    core["locations"] = [
        term(5829 if org == "ECOLI" and gene in {"tusA", "tusD", "mnmA"} else 5737)
    ]
    if gene in {"tusB", "tusC", "tusD", "tusE"}:
        core["in_complex"] = term(1990228)
    elif gene == "tusA":
        core["in_complex"] = term(1990329)
    if org == "THET2":
        core["knowledge_gaps"] = [
            {
                "gap_statement": "The native allocation between IscS and SufS and possible additional sulfur carriers is unresolved.",
                "significance": "Both purified donors support MnmA activity; biochemical capacity is not evidence that either supplies all native U34 flux.",
            }
        ]
    if org == "ECOLI" and gene in {"tusE", "mnmA"}:
        core["knowledge_gaps"] = [
            {
                "gap_statement": "Direct TusE-to-MnmA covalent sulfur loading and the physiological Fe-S requirement of E. coli MnmA remain unresolved.",
                "significance": "The supported U34 reaction and relay participation do not resolve the competing terminal catalytic mechanisms.",
            }
        ]
    result = [core]
    if gene == "tusA":
        result.append(
            {
                "description": "Sulfur carriage and allocation supporting molybdenum-cofactor biosynthesis, with the immediate terminal acceptor unresolved.",
                "molecular_function": term(97163),
                "directly_involved_in": [term(6777)],
                "locations": [term(5829)],
                "supported_by": [STIM, MOCO],
            }
        )
    return result


def metadata(pmid):
    text = (ROOT / f"publications/PMID_{pmid}.md").read_text()
    return yaml.safe_load(text.split("---", 2)[1])


def main():
    ledger = []
    for seed in BASE["seeds"]:
        org, gene = seed["organism"], seed["gene"]
        path = ROOT / seed["review"]
        document = yaml.safe_load(path.read_text())
        document["description"] = DESCRIPTIONS[f"{org}/{gene}"]
        document["status"] = "COMPLETE"
        for row in document["existing_annotations"]:
            row["review"] = adjudicate(org, gene, row)
            if row["evidence_type"] in {"IBA", "IEA"} and any(
                x.startswith("PANTHER:PTN") for x in row.get("supporting_entities", [])
            ):
                nodes = [
                    x for x in row["supporting_entities"] if x.startswith("PANTHER:PTN")
                ]
                row["review"]["reason"] += (
                    " The recorded ancestral source "
                    + ", ".join(nodes)
                    + " is assessed as an inherited functional claim, not a pairwise donor count; self-inclusion among descendant evidence is not circular. The lineage-loss check and target-specific source scope are recorded in the consultation."
                )
                if (
                    row["evidence_type"] == "IBA"
                    and row["review"]["action"] == "MODIFY"
                ):
                    row["review"]["propagation_review"] = {
                        "root_cause": "TERM_SCOPING_PROBLEM",
                        "failure_modes": ["GRANULARITY_MISMATCH"],
                        "source_entities": [
                            {
                                "source_id": node,
                                "source_status": "SUPPORTS_TRANSFER",
                                "comment": "The cached PAINT IBD places sulfurtransferase activity on this ancestral node. That positive claim is retained; target-specific U34 biochemistry supports refinement to existing GO:0103016. No ancestral loss or mistaken donor is inferred.",
                            }
                            for node in nodes
                        ],
                    }
                if org == "BACSU" and row["term"]["id"] == "GO:1990228":
                    row["review"]["propagation_review"] = {
                        "root_cause": "UNRESOLVED",
                        "source_entities": [
                            {
                                "source_id": node,
                                "source_status": "UNRESOLVED",
                                "comment": "The cached IBD at this bacterial node is grounded by E. coli MnmA. Bacillus has a positively characterized YrvO–MnmA catalytic partnership, but the source consulted does not independently resolve the physical sulfurtransferase assembly claimed for this member. Tus absence is not evidence against the generic complex term; no loss node is proposed.",
                            }
                            for node in nodes
                        ],
                    }
            ledger.append(
                {
                    "gene": f"{org}/{gene}",
                    "row": len([x for x in ledger if x["gene"] == f"{org}/{gene}"]),
                    "term": row["term"]["id"],
                    "action": row["review"]["action"],
                }
            )
        document["core_functions"] = build_core(org, gene)
        used = {}
        for row in document["existing_annotations"]:
            for ref in row["review"]["supported_by"]:
                used.setdefault(ref["reference_id"], []).append(ref["supporting_text"])
        for core in document["core_functions"]:
            for ref in core["supported_by"]:
                used.setdefault(ref["reference_id"], []).append(ref["supporting_text"])
        for pmid in [39660893] if gene.startswith("tus") or gene == "mnmA" else []:
            used.setdefault(f"PMID:{pmid}", []).append(LIMIT["supporting_text"])
        refs = {x["id"]: x for x in document["references"]}
        for rid in used:
            refs.setdefault(
                rid, {"id": rid, "title": metadata(rid.split(":")[1])["title"]}
            )
        for rid, ref in refs.items():
            if not rid.startswith("PMID:"):
                continue
            meta = metadata(rid.split(":")[1])
            ref["title"] = meta["title"]
            ref["findings"] = [
                {"statement": FINDINGS[q], "supporting_text": q}
                for q in dict.fromkeys(used.get(rid, []))
            ]
            if not meta.get("full_text_available"):
                ref["full_text_unavailable"] = True
            scope = (
                "Full cached primary/review text consulted."
                if meta.get("full_text_available")
                else "Cached abstract consulted; original full text was not recovered. Existing curator assignments are not rejected because of inaccessible details."
            )
            if rid == "PMID:25825430":
                scope = "Normal cache is abstract-only; genuine full publisher text was separately read and preserved in preflight/25825430-web-result.json. PS832 is a 168 derivative; E. coli complementation and native Bacillus evidence are distinguished."
            if rid == "PMID:18304323":
                scope += " The study is MC4100 cytosolic proteomics; the existing MnmA target assignment is retained without claiming an independent peptide-level reanalysis."
            if rid == "PMID:39660893":
                scope += " This critical review bounds terminal E. coli sulfur chemistry and disputed Fe-S dependence; it is not a new target assay."
            if rid in {"PMID:15690043", "PMID:16606699", "PMID:24561554"}:
                scope += " The interaction claim is not denied; removal of bare protein binding follows the repository information-content policy."
            ref["reference_review"] = {
                "relevance": "HIGH" if rid in used else "MEDIUM",
                "correctness": "VERIFIED",
                "review_notes": scope,
            }
        if org == "THET2" and gene == "TT_C1373":
            rid = "file:THET2/TT_C1373/TT_C1373-uniprot.txt"
            quote = "DR   InterPro; IPR010970; Cys_dSase_SufS."
            assert quote in (path.parent / "TT_C1373-uniprot.txt").read_text()
            refs[rid] = {
                "id": rid,
                "title": "Frozen UniProt Q72HV9 specific SufS signature",
                "findings": [
                    {
                        "statement": "The target has the specific SufS cysteine-desulfurase signature; this supports the PLP-enzyme inference and is not a direct cofactor-occupancy measurement.",
                        "record_section": ["DR:InterPro"],
                        "supporting_text": quote,
                    }
                ],
            }
            for row in document["existing_annotations"]:
                if row["term"]["id"] == "GO:0030170":
                    row["review"]["supported_by"].append(
                        {
                            "reference_id": rid,
                            "record_section": ["DR:InterPro"],
                            "supporting_text": quote,
                        }
                    )
        document["references"] = list(refs.values())
        # The exact seed assertions must remain, with only their review objects edited.
        before = [{k: v for k, v in x.items() if k != "review"} for x in seed["rows"]]
        after = [
            {k: v for k, v in x.items() if k != "review"}
            for x in document["existing_annotations"]
        ]
        assert before == after, (org, gene)
        path.write_text(
            yaml.safe_dump(document, sort_keys=False, allow_unicode=True, width=100)
        )
        notes = path.parent / f"{gene}-notes.md"
        notes.write_text(
            f"# {org} {gene}: source-bounded annotation review\n\n{DESCRIPTIONS[f'{org}/{gene}']}\n\n"
            "Reviewed all seeded rows without changing their payloads, order or qualifiers. No NEW rows were added. Broad functions/processes are refined only to existing supported descendants.\n\n"
            "A genuine Falcon attempt failed; its command and error are preserved in the new-member-consultation provider ledger and per-gene log. No provider report was fabricated. Manual primary/review reading and official identity records support this review.\n\n"
            "The shared evidence and access limits are documented in analysis/module_audits/bacterial_mnma_trna_thiolation/new-member-consultation/evidence.md. The immutable preflight ledger supplies official assay-strain/locus/accession bridges. Target identities are not inferred from a family name alone.\n\n"
            + "\n\n".join(
                f"- {r['term']['id']} ({r['evidence_type']}; {r['original_reference_id']}): {r['review']['action']}. {r['review']['reason']}"
                for r in document["existing_annotations"]
            )
            + "\n"
        )
    (A / "action-ledger.json").write_text(json.dumps(ledger, indent=2) + "\n")


if __name__ == "__main__":
    main()
