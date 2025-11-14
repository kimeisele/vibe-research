#!/usr/bin/env bash
#
# Manual Sync Script: vibe-agency → vibe-research
#
# Usage:
#   ./scripts/manual-sync-from-vibe-agency.sh [source-branch]
#
# Example:
#   ./scripts/manual-sync-from-vibe-agency.sh main
#   ./scripts/manual-sync-from-vibe-agency.sh develop
#

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
VIBE_AGENCY_REPO="https://github.com/kimeisele/vibe-agency.git"
SOURCE_BRANCH="${1:-main}"
TEMP_DIR="/tmp/vibe-agency-sync-$$"

echo -e "${BLUE}╔════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  Manual Sync: vibe-agency → vibe-research     ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════╝${NC}"
echo ""

# Check if we're in the right directory
if [ ! -f "SYNC_SETUP_INSTRUCTIONS.md" ]; then
    echo -e "${RED}❌ Error: Must run from vibe-research root directory${NC}"
    exit 1
fi

# Step 1: Clone vibe-agency
echo -e "${YELLOW}[1/5]${NC} Cloning vibe-agency (branch: ${SOURCE_BRANCH})..."
git clone --depth 1 --branch "$SOURCE_BRANCH" "$VIBE_AGENCY_REPO" "$TEMP_DIR"

if [ ! -d "$TEMP_DIR" ]; then
    echo -e "${RED}❌ Failed to clone vibe-agency${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Cloned vibe-agency${NC}"
echo ""

# Step 2: Sync agency_os/
echo -e "${YELLOW}[2/5]${NC} Syncing agency_os/..."

if [ -d "$TEMP_DIR/agency_os" ]; then
    rm -rf agency_os
    cp -r "$TEMP_DIR/agency_os" .
    echo -e "${GREEN}✅ Synced agency_os/${NC}"
else
    echo -e "${RED}⚠️  Warning: agency_os/ not found in vibe-agency${NC}"
fi

echo ""

# Step 3: Sync Python runtime files
echo -e "${YELLOW}[3/5]${NC} Syncing Python runtime files..."

SYNCED_FILES=0

# Orchestrator
if [ -f "$TEMP_DIR/core_orchestrator.py" ]; then
    cp "$TEMP_DIR/core_orchestrator.py" scripts/
    echo -e "${GREEN}  ✅ core_orchestrator.py${NC}"
    SYNCED_FILES=$((SYNCED_FILES + 1))
fi

# Handlers
if [ -d "$TEMP_DIR/handlers" ]; then
    cp -r "$TEMP_DIR/handlers" scripts/
    echo -e "${GREEN}  ✅ handlers/${NC}"
    SYNCED_FILES=$((SYNCED_FILES + 1))
fi

# Requirements
if [ -f "$TEMP_DIR/requirements.txt" ]; then
    # Merge requirements
    cat "$TEMP_DIR/requirements.txt" >> requirements.txt
    sort -u requirements.txt -o requirements.txt
    echo -e "${GREEN}  ✅ requirements.txt (merged)${NC}"
    SYNCED_FILES=$((SYNCED_FILES + 1))
fi

if [ $SYNCED_FILES -eq 0 ]; then
    echo -e "${YELLOW}  ℹ️  No runtime files found${NC}"
fi

echo ""

# Step 4: Sync CLI
echo -e "${YELLOW}[4/5]${NC} Syncing CLI..."

if [ -f "$TEMP_DIR/vibe-cli.py" ]; then
    # Check if different
    if diff -q "$TEMP_DIR/vibe-cli.py" vibe-cli.py > /dev/null 2>&1; then
        echo -e "${BLUE}  ℹ️  CLI unchanged${NC}"
    else
        cp "$TEMP_DIR/vibe-cli.py" .
        echo -e "${GREEN}  ✅ vibe-cli.py updated${NC}"
    fi
else
    echo -e "${YELLOW}  ℹ️  CLI not found in vibe-agency${NC}"
fi

echo ""

# Step 5: Cleanup
echo -e "${YELLOW}[5/5]${NC} Cleanup..."
rm -rf "$TEMP_DIR"
echo -e "${GREEN}✅ Cleaned up temporary files${NC}"
echo ""

# Check for changes
if git diff --quiet; then
    echo -e "${BLUE}════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}No changes detected - repos already in sync${NC}"
    echo -e "${BLUE}════════════════════════════════════════════════${NC}"
else
    echo -e "${GREEN}════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}Sync complete! Changes detected:${NC}"
    echo -e "${GREEN}════════════════════════════════════════════════${NC}"
    echo ""
    git status --short
    echo ""
    echo -e "${YELLOW}Next steps:${NC}"
    echo "  1. Review changes: git diff"
    echo "  2. Commit: git add -A && git commit -m '🔄 Manual sync from vibe-agency'"
    echo "  3. Push: git push"
    echo ""
fi
