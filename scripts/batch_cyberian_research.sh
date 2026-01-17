#!/bin/bash
# Batch process cyberian deep research for all human genes missing it
# Run: nohup ./scripts/batch_cyberian_research.sh > /tmp/batch_cyberian.log 2>&1 &

cd /Users/cjm/repos/ai-gene-review

LOG_FILE="/tmp/batch_cyberian_progress.log"
echo "$(date): Starting batch cyberian deep research" > "$LOG_FILE"

# Get list of genes needing cyberian research
genes=()
for gene in $(ls genes/human/); do
  if [ -d "genes/human/$gene" ] && [ ! -f "genes/human/$gene/${gene}-deep-research-cyberian.md" ]; then
    # Check if it has a uniprot file (valid gene folder)
    if [ -f "genes/human/$gene/${gene}-uniprot.txt" ]; then
      genes+=("$gene")
    fi
  fi
done

total=${#genes[@]}
echo "$(date): Found $total genes needing cyberian research" >> "$LOG_FILE"

count=0
for gene in "${genes[@]}"; do
  count=$((count + 1))
  echo "$(date): [$count/$total] Processing $gene..." >> "$LOG_FILE"

  # Run cyberian research (will block until complete)
  just deep-research-cyberian human "$gene" 2>&1 >> "$LOG_FILE"

  # Check if successful
  if [ -f "genes/human/$gene/${gene}-deep-research-cyberian.md" ]; then
    echo "$(date): [$count/$total] SUCCESS: $gene" >> "$LOG_FILE"
  else
    echo "$(date): [$count/$total] FAILED: $gene" >> "$LOG_FILE"
  fi

  # Small delay between jobs
  sleep 2
done

echo "$(date): Batch complete. Processed $count genes." >> "$LOG_FILE"
