"""Reproduce targeted family adjudication from immutable pre-edit snapshots."""

import copy
import csv
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASELINE = json.loads((HERE / "baseline.json").read_text())
FAMILIES = ["PTHR36837", "PTHR43194", "PTHR43433", "PTHR43798"]
LABELS = {}
for block in (ROOT / "interpro/panther/panther.obo").read_text().split("[Term]"):
    fields = dict(
        line.split(": ", 1)
        for line in block.splitlines()
        if line.startswith(("id: ", "name: "))
    )
    if fields.get("id", "").startswith(tuple("PANTHER:" + f for f in FAMILIES)):
        LABELS[fields["id"]] = fields["name"]
GO = {}
for filename in ["go-terms.json", "go-additional.json"]:
    for term in json.loads((HERE / filename).read_text())["results"]:
        GO[term["id"]] = term["name"]


def term(identifier):
    return {"id": identifier, "label": GO.get(identifier, LABELS.get(identifier))}


def support(ref, quote):
    return {"reference_id": ref, "supporting_text": quote}


def official(accession, section="FUNCTION"):
    obj = json.loads((HERE / f"{accession}-uniprot.json").read_text())
    return next(
        c["texts"][0]["value"]
        for c in obj.get("comments", [])
        if c["commentType"] == section
    )


def excerpt(accession, sentence):
    assert sentence in official(accession)
    return support(
        "file:" + str((HERE / f"{accession}-uniprot.json").relative_to(ROOT)), sentence
    )


def member(accession, gene, organism, review=None):
    row = {"id": "UniProtKB:" + accession, "gene_symbol": gene, "organism": organism}
    if review:
        row["gene_review"] = review
    return row


def scope(identifier, reason, evidence, value="UNRESOLVED"):
    return {
        "assessed_term": term(identifier),
        "scope": value,
        "scope_reason": reason,
        "supported_by": evidence,
    }


def new_family(family, name, summary, coherence, reference):
    return {
        "family_id": "PANTHER:" + family,
        "family_name": LABELS["PANTHER:" + family],
        "preferred_name": name,
        "summary": summary,
        "functional_coherence": "HETEROGENEOUS",
        "coherence_reason": coherence,
        "reference_protein": reference,
        "subfamilies": [],
        "node_assessments": [],
        "term_assessments": [],
        "references": [],
        "review_status": "COMPLETE",
        "reviewed_by": "codex",
        "review_date": "2026-11-07",
    }


def add_subfamily(doc, sf, description, members):
    identifier = doc["family_id"] + ":" + sf
    doc["subfamilies"].append(
        {
            "subfamily_id": identifier,
            "label": LABELS[identifier],
            "description": description,
            "representative_members": members,
            "diverged_from_family": False,
        }
    )


def collect_refs(value):
    if isinstance(value, dict):
        if "reference_id" in value:
            yield value["reference_id"]
        for child in value.values():
            yield from collect_refs(child)
    elif isinstance(value, list):
        for child in value:
            yield from collect_refs(child)


def finish(doc):
    existing = {r["id"] for r in doc.get("references", [])}
    for ref in sorted(set(collect_refs(doc)) - existing):
        if ref.startswith("PMID:"):
            path = ROOT / "publications" / (ref.replace(":", "_") + ".md")
            title = yaml.safe_load(path.read_text().split("---")[1])["title"]
        else:
            title = "Scoped source: " + ref.removeprefix("file:")
        doc["references"].append({"id": ref, "title": title})
    doc["reviewed_by"] = "codex"
    doc["review_date"] = "2026-11-07"
    return doc


def main():
    synthase = support(
        "file:genes/ECTOL/phaC1/phaC1-uniprot.txt",
        "Synthesizes poly(3-hydroxyalkanoates) (PHA), complements a mutant of P.putida that does not make PHA.",
    )
    class_two = support(
        "file:genes/ECTOL/phaC1/phaC1-uniprot.txt",
        "Belongs to the PHA/PHB synthase family. Type II PhaC subfamily.",
    )
    class_one = excerpt(
        "P23608",
        "Polymerizes (R)-3-hydroxybutyryl-CoA to create polyhydroxybutyrate (PHB) which consists of thousands of hydroxybutyrate molecules linked end to end.",
    )
    reverse = support(
        "PMID:9727022",
        "It catalyzes the transfer of the acyl moiety from in vitro synthesized 3-hydroxydecanoyl-CoA to acyl carrier protein, indicating that PhaG exhibits a 3-hydroxyacyl-CoA-acyl carrier protein transferase activity",
    )
    forward = support(
        "PMID:35338129",
        "no in vitro data on acyl-ACPs, the substrate in the forward direction is available",
    )
    product = support(
        "PMID:35338129",
        "The samples contained a total of 170\u2009mg/L C7–C13 methyl ketones but no detectable 3-hydroxy methyl esters",
    )
    depoly = support(
        "PMID:17170116",
        "We have demonstrated that PhaZ is an intracellular depolymerase that is located in PHA granules and that hydrolyzes specifically mcl-PHAs containing aliphatic and aromatic monomers.",
    )
    strain = support(
        "PMID:41055782", "pQE32 derivative containing phaZ gene from P. putida KT2442"
    )
    rescue = support(
        "file:genes/ECTOL/phaZ/phaZ-uniprot.txt",
        "Complements a mutant that does not degrade PHA; might be a lipase.",
    )
    abhd = excerpt(
        "Q9BV23",
        "Lipase that preferentially hydrolysis medium-chain saturated monoacylglycerols including 2-arachidonoylglycerol (PubMed:22969151).",
    )
    cyclase = excerpt(
        "O07732",
        "The C-terminal domain catalyzes the biosynthesis of cyclic AMP (cAMP) from ATP (PubMed:15678099).",
    )
    lipase = excerpt(
        "O07732", "The N-terminal domain exhibits lipolytic activity (PubMed:33960821)."
    )
    bioh = excerpt(
        "P13001",
        "The physiological role of BioH is to remove the methyl group introduced by BioC when the pimeloyl moiety is complete.",
    )
    assay_limit = "PMID17170116 assays KT2442 PhaZ; PMID41055782 also uses KT2442-derived constructs expressed in E. coli, with GPo1 supplying polymer. Q88D24 is the KT2440 reference and is supported by homolog/pathway/domain evidence, not relabeled as a directly assayed native KT2440 enzyme. Intracellular granule mobilization differs from secreted attack on extracellular polymer."
    docs = {}
    f = "PTHR36837"
    doc = new_family(
        f,
        "PHA synthases with variable polymer and subunit scope",
        "Proteins related to polyhydroxyalkanoate synthases catalyze ester-polymer formation from hydroxyacyl-CoA precursors. Characterized class I and class II enzymes differ in preferred substrates, and other classes have partner requirements. The same SF5 includes Cupriavidus necator PhaC and Pseudomonas-type class II PhaC1/PhaC2; its name does not make every member a PHB-specific or medium-chain-specific synthase.",
        "The family joins characterized synthases with unresolved branches. Class I/class II substrate preferences are not interchangeable, and a class label is not an absolute exclusion of secondary substrates. SF4 includes a submitter-named phaZ member, but that unreviewed name is not evidence of a verified catalytic switch.",
        member(
            "Q88D25",
            "phaA",
            "Pseudomonas putida KT2440",
            "genes/PSEPK/phaA/phaA-ai-review.yaml",
        ),
    )
    add_subfamily(
        doc,
        "SF5",
        "Includes class I PHB synthase and class II mcl-PHA synthases; no exclusive chain-length inference follows from the shared subfamily.",
        [
            member("P23608", "phaC", "Cupriavidus necator H16"),
            member(
                "P26494",
                "phaC1",
                "Ectopseudomonas oleovorans GPo1",
                "genes/ECTOL/phaC1/phaC1-ai-review.yaml",
            ),
            member(
                "P26496",
                "phaC2",
                "Ectopseudomonas oleovorans GPo1",
                "genes/ECTOL/phaC2/phaC2-ai-review.yaml",
            ),
            member(
                "Q88D25",
                "phaA",
                "Pseudomonas putida KT2440",
                "genes/PSEPK/phaA/phaA-ai-review.yaml",
            ),
            member(
                "Q88D23",
                "phaC",
                "Pseudomonas putida KT2440",
                "genes/PSEPK/phaC/phaC-ai-review.yaml",
            ),
        ],
    )
    add_subfamily(
        doc,
        "SF4",
        "An unresolved branch including Q8PAX3, whose PHB-depolymerase name is submitter-only ECO:0000313. That name is not used as proof of hydrolysis, loss of synthase activity, or secretion.",
        [member("Q8PAX3", "phaZ", "Xanthomonas campestris")],
    )
    doc["term_assessments"] = [
        scope(
            "GO:0016747",
            "Characterized synthases perform non-amino-acyl transfer during polyester elongation. A whole-family grant is withheld for unresolved branches; this does not deny the positive class I/class II synthase members or assert a hydrolase loss from a submitter label.",
            [synthase, class_one],
        ),
        scope(
            "GO:0042621",
            "Positive PHA biosynthesis is established for the characterized synthases. Family and SF5 classification alone do not resolve polymer composition, partner requirements or activity of every member.",
            [synthase, class_two],
        ),
        scope(
            "GO:0042619",
            "PHB formation is directly supported for C. necator P23608; the same SF5 includes mcl-PHA synthases. The PHB-specific process cannot be granted from SF5 membership alone. This is a scope uncertainty, not an assertion that class II enzymes never accept C4 or that class I enzymes never accept longer precursors.",
            [class_one, class_two],
        ),
        scope(
            "GO:0070088",
            "Granule-associated function is supported for bacterial PHA synthesis systems, but universal location and polymer context are not established for all branches of this broad family.",
            [synthase],
        ),
    ]
    doc["notes"] = (
        "Normal fetch-panther-paint resolved 30 nodes but found no node-level annotations; no PAINT rows or ancestral assertions were fabricated. Current official tree has 17 reference leaves, not an exhaustive census. The unchecked LLM metadata summary is not biological evidence. No residue discriminator or universal stoichiometry is asserted."
    )
    docs[f] = finish(doc)

    f = "PTHR43194"
    doc = copy.deepcopy(
        BASELINE["existing_reviews"][f"interpro/panther/{f}/{f}-review.yaml"][
            "document"
        ]
    )
    doc["summary"] += (
        " PhaG forward ACP-to-CoA routing is favored by heterologous metabolic controls; purified reverse CoA-to-ACP transfer is measured, while forward acyl-ACP kinetics remain unmeasured in the cited studies."
    )
    doc["coherence_reason"] = (
        "Members share an alpha/beta-hydrolase fold but have different established chemistries: BioH ester hydrolysis in biotin synthesis, PhaG/RhlA acyl transfer, RsbQ signaling, and Lpx1 lipase activity. Fold membership does not establish a specific substrate or uniform hydrolysis. The lipoyl-domain acetoin E2s remain grouped by NCBIfam NF011457, not this family."
    )
    doc["subfamilies"][0]["representative_members"].append(
        member(
            "Q51553",
            "phaG",
            "Pseudomonas aeruginosa PAO1",
            "genes/PSEAE/phaG/phaG-ai-review.yaml",
        )
    )
    archives = []
    for row in doc["term_assessments"]:
        archives.append(
            {
                "family": f,
                "term": row["assessed_term"]["id"],
                "original": copy.deepcopy(row),
            }
        )
        if row["assessed_term"]["id"] == "GO:0016787":
            row["scope"] = "UNRESOLVED"
            row["scope_reason"] = (
                "Broad hydrolase activity is established in several branches, but the family also includes acyltransferases. PhaG hydroxyacid/ligase phenotypes do not uniquely establish intrinsic thioesterase activity; 2022 product-sink controls favor ACP-to-CoA transfer. Neither secondary hydrolysis nor its universal absence is established. The pre-existing AcoC E2 acetyltransferase judgment is retained in notes and the archived original term assessment; its schema representation changes only because UNRESOLVED cannot carry member_exceptions."
            )
            row.pop("member_exceptions", None)
            row["supported_by"] = [reverse, forward, product]
        else:
            row["scope"] = "UNRESOLVED"
            row.pop("applicable_subfamilies", None)
            row.pop("member_exceptions", None)
            row["scope_reason"] = (
                "BioH is a positive pimeloyl-ACP methyl esterase, but SF5 also contains PhaG and RhlA with established different pathway roles. Those positive functions do not prove absence of secondary BioH-like chemistry. No whole-SF5 grant, categorical negative PhaG exception, or precise historical pruning point is justified here."
            )
            row["supported_by"] = [bioh, reverse]
    for row in doc["node_assessments"]:
        t = row["asserted_term"]["id"]
        if t == "GO:0016787":
            row["assessment"] = "UNRESOLVED"
            row["assessment_reason"] = (
                "The shared alpha/beta-hydrolase superfamily node is absent from this current family tree. Seeded hydrolase functions are real, but a fold alone does not establish chemistry in acyltransferase branches. PhaG transfer evidence does not settle possible secondary hydrolysis; no loss is asserted."
            )
            row["supported_by"] = [reverse, forward, product]
        elif t == "GO:0090499":
            row["assessment"] = "UNRESOLVED"
            row.pop("affected_subfamilies", None)
            row["assessment_reason"] = (
                "The actual 17-leaf bacterial node includes BioH, RhlA, PhaG and RsbQ; Q51553 is a verified reference-tree descendant. BioH provides positive esterase evidence. PhaG-specific acyl transfer establishes its native route but does not directly exclude secondary methyl-ester hydrolysis, so a definitive loss/pruning verdict is withdrawn."
            )
            row["supported_by"] = [bioh, reverse]
        elif t == "GO:0009102":
            row["assessment"] = "UNRESOLVED"
            row.pop("affected_subfamilies", None)
            row["assessment_reason"] = (
                "The bacterial node spans BioH and proteins with established PHA/rhamnolipid or stress-signaling roles. Biotin biosynthesis is a positive physiological function of BioH, but neither its universal propagation nor categorical absence in PhaG follows from those alternative roles. No target-negative assay or precise historical loss is established, so the prior TOO_DEEP verdict is withdrawn."
            )
            row["supported_by"] = [bioh, reverse]
    doc["term_assessments"] += [
        scope(
            "GO:0016747",
            "PhaG transfer is established for exact target proteins and RhlA has distinct acyl-transfer chemistry. Shared SF5 also contains BioH; no whole-family or whole-SF5 PhaG substrate grant is made. Forward routing is supported by genetic product-sink controls, not purified forward kinetics.",
            [reverse, product, forward],
        ),
        scope(
            "GO:0042621",
            "PhaG supplies precursor-routing work for PHA synthesis, but the broader family/SF5 also includes other pathways. The routing step is not universally required for PHA accumulation on every carbon source.",
            [
                reverse,
                support(
                    "PMID:10713430",
                    "whereas from fatty acids wild-type level PHA accumulation was obtained.",
                ),
            ],
        ),
    ]
    doc["notes"] += (
        " This follow-up retains AcoC Q88QE1 as a lipoyl-dependent acetyltransferase and preserves its prior quoted evidence in the archived original term assessment; it does not recurate that protein. Original member-exception objects are archived exactly in family-consultation/prior-term-assessments.json. PhaG hydrolysis and BioH-secondary-activity exclusions were withdrawn as unproven; original PAINT payloads remain unchanged, including historical seed lists. Tree-scope evidence is refreshed independently from the official API."
    )

    # Replace mutable self-review support throughout the targeted document with independent primary evidence.
    def fix_quotes(value):
        if isinstance(value, dict):
            if value.get("reference_id") == "file:genes/PSEPK/phaG/phaG-ai-review.yaml":
                value.clear()
                value.update(reverse)
            for child in value.values():
                fix_quotes(child)
        elif isinstance(value, list):
            for child in value:
                fix_quotes(child)

    fix_quotes(doc)
    docs[f] = finish(doc)

    f = "PTHR43433"
    doc = new_family(
        f,
        "Diverse alpha/beta hydrolases including intracellular PhaZ",
        "A diverse alpha/beta-hydrolase family includes esterases, LipJ proteins bearing a separate cyclase domain, and intracellular PHA depolymerase relatives. KT2440 Q88D24 has the intracellular PHA-depolymerase signature and is assigned to SF5, which also contains unrelated substrate-specific hydrolases. Neither the family nor SF5 defines triacylglycerol, PHA, membrane, or secreted-polymer specificity.",
        "The shared hydrolase fold supports related catalytic architecture but substrate, pathway, additional domains and compartment differ. PhaZ chemistry is qualified by exact target/homolog evidence; LipJ cyclase activity belongs to an additional domain and is not a general hydrolase-family function.",
        member(
            "Q88D24",
            "phaZ",
            "Pseudomonas putida KT2440",
            "genes/PSEPK/phaZ/phaZ-ai-review.yaml",
        ),
    )
    add_subfamily(
        doc,
        "SF5",
        "Mixed hydrolase subfamily including Q88D24 PhaZ and the LipG PAINT seed; membership alone does not establish a glycerolipid substrate.",
        [
            member(
                "Q88D24",
                "phaZ",
                "Pseudomonas putida KT2440",
                "genes/PSEPK/phaZ/phaZ-ai-review.yaml",
            ),
            member("P96935", "lipG", "Mycobacterium tuberculosis H37Rv"),
        ],
    )
    add_subfamily(
        doc,
        "SF8",
        "LipJ-related proteins; an additional C-terminal cyclase domain explains the directly characterized LipJ cAMP activity.",
        [member("O07732", "lipJ", "Mycobacterium tuberculosis H37Rv")],
    )
    raw = list(
        csv.DictReader(
            (ROOT / f"interpro/panther/{f}/{f}-paint.tsv").open(), delimiter="\t"
        )
    )
    for r in raw:
        row = {
            "node_id": "PANTHER:" + r["node"],
            "asserted_term": term(r["go_id"]),
            "evidence": r["evidence"],
            "negated": r["negated"] == "true",
            "paint_snapshot": r["date"],
            "seeds": [{"id": x} for x in r["seeds"].split("|")],
            "assessment": "UNRESOLVED",
        }
        if r["taxon"] != "taxon:":
            row["node_taxon"] = {
                "id": r["taxon"].replace("taxon:", "NCBITaxon:"),
                "label": "Bacteria",
            }
        if r["node"] == "PTN001335022":
            row["assessment_reason"] = (
                "The 13-leaf reference node includes the LipG seed and the P. aeruginosa PHA-depolymerase relative G3XD91. Substrate-specific glycerolipid activity is not licensed for every member by the fold. PhaZ polymer hydrolysis neither proves nor disproves secondary triacylglycerol hydrolysis; no unsupported negative or pruning point is assigned."
            )
            row["supported_by"] = [depoly, strain]
        elif r["node"] == "PTN005163452":
            row["assessment_reason"] = (
                "LipJ O07732 has directly curated C-terminal adenylate cyclase activity. The node has three reference leaves; full cyclase architecture and activity of the other descendants were not established here. The positive seed is retained without granting cAMP synthesis to the whole hydrolase family."
            )
            row["supported_by"] = [cyclase]
        elif r["node"] == "PTN002881150":
            row["assessment_reason"] = (
                "This current root contains 70 reference leaves across diverse hydrolase branches. Positive hydrolysis is supported for LipJ and PhaZ relatives, but the present targeted audit does not establish catalytic functionality of every branch. No secondary hydrolysis loss or broad membrane/polymer function is inferred."
            )
            row["supported_by"] = [lipase, depoly]
        else:
            row["assessment_reason"] = (
                "This PAINT assertion is retained exactly, but its node is absent from the current PTHR43433 tree. Its propagation extent cannot be reconstructed from this tree alone. Neither a superfamily hydrolase annotation nor another family membrane seed resolves Q88D24 localization or substrate."
            )
            row["supported_by"] = [depoly]
        doc["node_assessments"].append(row)
    for identifier, reason, evidence in [
        (
            "GO:0050527",
            "Intracellular mcl-PHA depolymerization is supported for the PhaZ lineage, including C8-rich polymer. Neither SF5 nor the whole family has this substrate specificity. "
            + assay_limit,
            [depoly, strain],
        ),
        (
            "GO:0042620",
            "PhaZ performs polyester mobilization; LipG/LipJ and other hydrolase roles do not establish universal PHA metabolism. "
            + assay_limit,
            [depoly],
        ),
        (
            "GO:0016787",
            "Positive hydrolysis is established in characterized branches, but this targeted review does not certify all family members. This is uncertainty about universal scope, not absence of hydrolase activity in the positive PhaZ/LipJ members.",
            [depoly, lipase],
        ),
        (
            "GO:0004806",
            "Triacylglycerol hydrolysis and hydroxyalkanoate-polyester hydrolysis use different substrates. The original LipG seed is retained; no negative PhaZ TAG assay or universal TAG grant follows from classification.",
            [depoly],
        ),
        (
            "GO:0046503",
            "Glycerolipid catabolism is not synonymous with PHA turnover because PHA has no glycerol backbone. Actual secondary glycerolipid participation of every PhaZ relative remains unresolved.",
            [depoly],
        ),
        (
            "GO:0016020",
            "Intracellular storage-granule association does not by itself establish lipid-bilayer membrane localization, and secreted polymer degradation is a different role.",
            [depoly],
        ),
    ]:
        doc["term_assessments"].append(scope(identifier, reason, evidence))
    doc["notes"] = (
        assay_limit
        + " All seven original raw PAINT assertions are represented without changing identifiers, seeds, dates or polarity. Some cached PAINT nodes are absent from the current family tree; missing topology is disclosed, not invented. No residue or subfamily discriminator is asserted."
    )
    docs[f] = finish(doc)

    f = "PTHR43798"
    doc = copy.deepcopy(
        BASELINE["existing_reviews"][f"interpro/panther/{f}/{f}-review.yaml"][
            "document"
        ]
    )
    doc["summary"] += (
        " The same SF5 also contains the bacterial intracellular-PHA-mobilization protein PhaZ P26495 from Ectopseudomonas oleovorans GPo1; the ABHD6 subfamily label does not establish monoacylglycerol specificity for that member."
    )
    doc["coherence_reason"] += (
        " GPo1 PhaZ adds a directly supported native polyester-mobilization role within SF5. The reviewed ABHD6 positive remains valid; a new PhaZ function does not prove loss of possible secondary monoacylglycerol hydrolysis."
    )
    sf = next(x for x in doc["subfamilies"] if x["subfamily_id"].endswith(":SF5"))
    sf["description"] = (
        "Includes vertebrate ABHD6 monoacylglycerol lipases and GPo1 PhaZ P26495. Shared classification is verified; exact substrate and compartment must be resolved independently."
    )
    sf["representative_members"] = [
        member("Q9BV23", "ABHD6", "Homo sapiens"),
        member(
            "P26495",
            "phaZ",
            "Ectopseudomonas oleovorans GPo1",
            "genes/ECTOL/phaZ/phaZ-ai-review.yaml",
        ),
    ]
    for row in doc["node_assessments"]:
        if row["asserted_term"]["id"] in {"GO:0047372", "GO:0046464"}:
            row["assessment"] = "UNRESOLVED"
            row.pop("affected_subfamilies", None)
            row["assessment_reason"] = (
                "This 64-leaf node contains characterized ABHD6 positives and other hydrolase branches. The previous absence-of-assay rationale did not establish a catalytic loss. GPo1 PhaZ is officially SF5, but is not a reference-tree leaf, so its exact graft is not reconstructed here. Native polyester turnover supports PhaZ without excluding secondary monoacylglycerol activity; universal substrate/process scope remains unresolved."
            )
            row["supported_by"] = [abhd, rescue]
    for row in doc["term_assessments"]:
        if row["assessed_term"]["id"] == "GO:0047372":
            row["scope"] = "UNRESOLVED"
            row.pop("applicable_subfamilies", None)
            row["scope_reason"] = (
                "ABHD6 is a positive monoacylglycerol lipase, but official SF5 also includes GPo1 PhaZ. Its native polyester-mobilization evidence does not establish monoacylglycerol hydrolysis and does not prove its absence. Retain positive ABHD6 biology without an unjustified universal SF5 grant or an invented PhaZ negative exception."
            )
            row["supported_by"] = [abhd, rescue]
    doc["term_assessments"] += [
        scope(
            "GO:0050527",
            "GPo1 PhaZ supports native intracellular mcl-PHA mobilization, but exact poly(3-hydroxyoctanoate) substrate/product chemistry was not established by that mutant/rescue evidence. Neither a precise single-enzyme activity nor universal SF5 depolymerase activity is granted. Positive ABHD6 and PhaZ biology remain distinct.",
            [rescue],
        ),
        scope(
            "GO:0042620",
            "GPo1 PhaZ does work in native PHA turnover. The family contains other hydrolase functions, so this process is not universally granted.",
            [rescue],
        ),
    ]
    doc["notes"] += (
        " This targeted follow-up preserves the prior AcoC assessment and unrelated PAINT objects/judgments. P26495 is confirmed in PTHR43798:SF5 by both raw entries and official UniProt; it is not forcibly moved into PTHR43433. TreeGrafter PTN002465558 has 49 reference descendants, but P26495 is not one of the reference leaves; no precise graft attachment is independently claimed. Granule association is not itself a membrane assay, and absence of a TM helix is not proof of no peripheral association. Native GPo1 mutant is leaky and the rescue fragment includes phaC1 plus phaZ; no purified forward-product, intracellular-versus-extracellular equivalence, or secondary-MAG negative claim follows."
    )
    docs[f] = finish(doc)
    (HERE / "prior-term-assessments.json").write_text(
        json.dumps(archives, indent=2) + "\n"
    )
    row = docs["PTHR43194"]["term_assessments"][0]
    aco = archives[0]["original"]["member_exceptions"][0]
    row["supported_by"] += aco["supported_by"]
    row["scope_reason"] += (
        " AcoC Q88QE1 remains judged not to perform hydrolase activity in this family review, on its E2 acetyltransferase assignment. The current schema/semantic combination cannot preserve that independently negative member as a live member_exceptions object under UNRESOLVED; current-member-judgments.yaml retains it explicitly, with the enforcement limitation documented."
    )
    class_one_extended = support(
        "PMID:10612741",
        "R. eutropha PHA synthase accepts, besides the main substrate 3-hydroxybutyryl-CoA, also the CoA thioesters of 3HO and 3HDD.",
    )
    docs["PTHR36837"]["term_assessments"][2]["supported_by"].append(class_one_extended)
    docs["PTHR36837"]["term_assessments"][2]["scope_reason"] += (
        " Primary10612741 reports C8/C12 comonomer incorporation by the class I enzyme in engineered E. coli precursor contexts; this is PHB-rich copolymer synthesis, not a pure-mcl-polymer or complete native H16 turnover assay."
    )
    gpo_construct = support(
        "file:analysis/module_audits/bacterial_mcl_pha_synthesis_and_mobilization/family-consultation/primary-excerpts.md",
        "Plasmid pGEc422 carrying phaC1 and phaZ genes",
    )
    for row in docs["PTHR43798"]["term_assessments"]:
        if row["assessed_term"]["id"] in {"GO:0050527", "GO:0042620"}:
            row["supported_by"].append(gpo_construct)
    finish(docs["PTHR36837"])
    finish(docs["PTHR43798"])
    for family, doc in docs.items():
        (ROOT / f"interpro/panther/{family}/{family}-review.yaml").write_text(
            yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100)
        )
    (HERE / "official-labels.json").write_text(json.dumps(LABELS, indent=2) + "\n")
    print("Curated", ",".join(docs))


if __name__ == "__main__":
    main()
