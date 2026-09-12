#!/usr/bin/env bash
# Launch falcon deep-research for 10 TreeGrafter exemplars: a GENE run (blinded
# function hypothesis) and a FAMILY run (family-function characterization) each.
set -uo pipefail
cd /home/user/ai-gene-review
S=/tmp/claude-0/-home-user-ai-gene-review/1a22a3e6-dfb7-5df6-91cd-c7a823f9e5b7/scratchpad
LOG=$S/falcon_logs; mkdir -p "$LOG"
MAXJOBS=8

# fields: org|gene|uniprot|term_id|term_label|family_id|family_name|subfamily
ROWS=(
"DESVH|Q72DT2|Q72DT2|GO:0000104|succinate dehydrogenase activity|PTHR11632|SUCCINATE DEHYDROGENASE 2 FLAVOPROTEIN SUBUNIT|PTHR11632:SF51 SUCCINATE DEHYDROGENASE [UBIQUINONE] FLAVOPROTEIN SUBUNIT, MITOCHONDRIAL"
"PSEPK|fcs|Q88HK0|GO:0031956|medium-chain fatty acid-CoA ligase activity|PTHR43201|ACYL-COA SYNTHETASE|PTHR43201:SF32 2-SUCCINYLBENZOATE--COA LIGASE"
"OCTVU|OCTS1|P27013|GO:0004364|glutathione transferase activity|PTHR11571|GLUTATHIONE S-TRANSFERASE|PTHR11571:SF150 GLUTATHIONE S-TRANSFERASE"
"SACEN|eryAIII|A4F7P1|GO:0004312|fatty acid synthase activity|PTHR43775|FATTY ACID SYNTHASE|PTHR43775:SF51 INACTIVE PHENOLPHTHIOCEROL SYNTHESIS POLYKETIDE SYNTHASE TYPE I PKS1-RELATED"
"ECOLX|mcr-1|A0A0R6L508|GO:0016776|phosphotransferase activity, phosphate group as acceptor|PTHR30443|INNER MEMBRANE PROTEIN|PTHR30443:SF0 PHOSPHOETHANOLAMINE TRANSFERASE EPTA"
"NICAT|NaPMT3|A0A314LG79|GO:0004766|spermidine synthase activity|PTHR11558|SPERMIDINE/SPERMINE SYNTHASE|PTHR11558:SF53 PUTRESCINE N-METHYLTRANSFERASE 1"
"DOROP|ADAR2|C1JAR3|GO:0008251|tRNA-specific adenosine deaminase activity|PTHR10910|EUKARYOTE SPECIFIC DSRNA BINDING PROTEIN|PTHR10910:SF62 AT07585P-RELATED"
"NICAT|NaUGT1_candidate_UGT85A2_0|A0A2H4GSI3|GO:0080043|quercetin 3-O-glucosyltransferase activity|PTHR11926|GLUCOSYL/GLUCURONOSYL TRANSFERASES|PTHR11926:SF1392 GLYCOSYLTRANSFERASE"
"PSEPK|aceK|Q88EA1|GO:0004721|phosphoprotein phosphatase activity|PTHR39559|ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE (family)|PTHR39559:SF1 ISOCITRATE DEHYDROGENASE KINASE/PHOSPHATASE"
"PSEPK|ahpC|Q88K52|GO:0008379|thioredoxin peroxidase activity|PTHR10681|THIOREDOXIN PEROXIDASE|PTHR10681:SF121 ALKYL HYDROPEROXIDE REDUCTASE C"
)

gate() { while (( $(jobs -rp | wc -l) >= MAXJOBS )); do wait -n; done; }

gene_run() {
  local org="$1" gene="$2" term="$3"
  uv run python scripts/gene_hypothesis_deep_research.py run "$org" "$gene" falcon \
    --annotation-term-id "$term" --as-function-hypothesis \
    --template templates/treegrafter_function_hypothesis.md --timeout-seconds 8100 \
    > "$LOG/gene_${gene}.log" 2>&1
  echo "GENE $gene exit=$?" >> "$LOG/_summary.log"
}

family_run() {
  local fam="$1" famname="$2" sub="$3" sym="$4" acc="$5" org="$6" term="$7"
  local d="interpro/panther/$fam"; mkdir -p "$d"
  uv run deep-research-client research --provider falcon \
    --template templates/treegrafter_family_function.md \
    --var "family_id=$fam" --var "family_name=$famname" --var "subfamily=$sub" \
    --var "gene_symbol=$sym" --var "uniprot=$acc" --var "organism=$org" --var "taxon_label=$org" \
    --var "propagated_term=$term" \
    --output "$d/${fam}-function-falcon.md" \
    --separate-citations "$d/${fam}-function-falcon.citations.md" \
    > "$LOG/family_${fam}.log" 2>&1
  echo "FAMILY $fam exit=$?" >> "$LOG/_summary.log"
}

: > "$LOG/_summary.log"
for row in "${ROWS[@]}"; do
  IFS='|' read -r org gene acc term term_label fam famname sub <<< "$row"
  gate; gene_run "$org" "$gene" "$term" &
  gate; family_run "$fam" "$famname" "$sub" "$gene" "$acc" "$org" "$term_label ($term)" &
done
wait
echo "ALL FALCON RUNS COMPLETE" >> "$LOG/_summary.log"
