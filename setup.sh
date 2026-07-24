#!/usr/bin/env bash
#
# setup.sh — Bootstrap noHXW without requiring pip pre-installed.
#
# Handles:
#   1. Finds Python 3.10+
#   2. Installs pip via ensurepip if missing
#   3. Creates a virtual environment
#   4. Installs all dependencies
#   5. Prints next steps
#
# Usage:
#   chmod +x setup.sh && ./setup.sh

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}══════════════════════════════════════════════════${NC}"
echo -e "${CYAN}   noHXW — Setup Bootstrap${NC}"
echo -e "${CYAN}   No Hardware, No Problem${NC}"
echo -e "${CYAN}══════════════════════════════════════════════════${NC}"
echo ""

# ── Step 1: Find Python 3.10+ ─────────────────────────────────────
echo -e "${YELLOW}[1/5]${NC} Looking for Python 3.10+..."

PYTHON=""
for cmd in python3 python; do
    if command -v "$cmd" &>/dev/null; then
        ver=$("$cmd" -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")' 2>/dev/null)
        if [ -n "$ver" ]; then
            echo -e "  ✅ Found Python $ver via \`$cmd\`"
            PYTHON="$cmd"
            break
        fi
    fi
done

if [ -z "$PYTHON" ]; then
    echo -e "${RED}  ❌ Python 3.10+ not found!${NC}"
    echo "  Install from: https://www.python.org/downloads/"
    echo "  Or use your package manager:"
    echo "    macOS: brew install python"
    echo "    Ubuntu: sudo apt install python3 python3-venv"
    echo "    Fedora: sudo dnf install python3"
    exit 1
fi

# ── Step 2: Ensure pip ─────────────────────────────────────────────
echo -e "${YELLOW}[2/5]${NC} Making sure pip is available..."

if $PYTHON -m pip --version &>/dev/null; then
    echo -e "  ✅ pip ready"
else
    echo -e "  📦 Installing pip via \`python3 -m ensurepip\`..."
    $PYTHON -m ensurepip --upgrade 2>&1 | sed 's/^/     /'
    if ! $PYTHON -m pip --version &>/dev/null; then
        echo -e "${RED}  ❌ Could not install pip. Try:${NC}"
        echo "    curl -sS https://bootstrap.pypa.io/get-pip.py | $PYTHON"
        exit 1
    fi
    echo -e "  ✅ pip installed"
fi

# ── Step 3: Create virtual environment ─────────────────────────────
echo -e "${YELLOW}[3/5]${NC} Creating virtual environment..."

if [ -d ".venv" ]; then
    echo -e "  ✅ .venv already exists (reusing)"
else
    $PYTHON -m venv .venv
    echo -e "  ✅ Virtual environment created"
fi

# ── Step 4: Install dependencies ───────────────────────────────────
echo -e "${YELLOW}[4/5]${NC} Installing dependencies..."

.venv/bin/pip install --upgrade pip setuptools wheel -q 2>&1 | sed 's/^/     /'
.venv/bin/pip install -e . -q 2>&1 | sed 's/^/     /'

echo -e "  ✅ Dependencies installed"

# ── Step 5: Done ───────────────────────────────────────────────────
echo -e "${YELLOW}[5/5]${NC} Setup complete!"
echo ""
echo -e "${GREEN}══════════════════════════════════════════════════${NC}"
echo -e "${GREEN}   noHXW is ready to rock! 🚀${NC}"
echo -e "${GREEN}══════════════════════════════════════════════════${NC}"
echo ""
echo -e "  Start the server:"
echo -e "    ${CYAN}source .venv/bin/activate${NC}"
echo -e "    ${CYAN}noxhw${NC}"
echo ""
echo -e "  Or with one command:"
echo -e "    ${CYAN}.venv/bin/noxhw${NC}"
echo ""
echo -e "  Then open:"
echo -e "    ${CYAN}http://localhost:3000${NC}"
echo ""
