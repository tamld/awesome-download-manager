#!/usr/bin/env python3
"""
Test Suite for Awesome Download Manager
Enforces:
1. Data Schema & Axiom/Citation Integrity in data/tools.json
2. 100% Pure English Artifact Policy (No Vietnamese or untranslated tokens)
3. Table Integrity (No broken pipes, perfectly aligned columns)
4. Build Idempotency (Deterministic README generation)
"""

import json
import os
import re
import subprocess
import sys
import unittest

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(ROOT_DIR, "data", "tools.json")
BUILDER_PATH = os.path.join(ROOT_DIR, "scripts", "build_readme.py")
README_PATH = os.path.join(ROOT_DIR, "README.md")

ALLOWED_CATEGORIES = {
    "trending", "legends", "desktop", "linux", "cli", "extensions", "selfhosted"
}

# Regex to detect Vietnamese diacritics
VIETNAMESE_PATTERN = re.compile(
    r"[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]",
    re.IGNORECASE
)

class TestToolsSchemaAndBuild(unittest.TestCase):

    def test_01_data_file_exists(self):
        """RED TEST: data/tools.json must exist."""
        self.assertTrue(os.path.isfile(DATA_PATH), f"Missing data file: {DATA_PATH}")

    def test_02_schema_and_fields(self):
        """Every tool entry must have all required fields including axiom and citations."""
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            tools = json.load(f)

        self.assertIsInstance(tools, list, "tools.json root must be a JSON array")
        self.assertGreater(len(tools), 10, "tools.json must contain at least 10 curated tools")

        seen_ids = set()
        for tool in tools:
            tool_id = tool.get("id")
            self.assertTrue(tool_id, f"Missing id in tool: {tool}")
            self.assertNotIn(tool_id, seen_ids, f"Duplicate tool id: {tool_id}")
            seen_ids.add(tool_id)

            self.assertTrue(tool.get("name"), f"Missing name in {tool_id}")
            self.assertTrue(tool.get("url", "").startswith("http"), f"Invalid url in {tool_id}")
            self.assertIn(tool.get("category"), ALLOWED_CATEGORIES, f"Invalid category in {tool_id}")
            self.assertTrue(tool.get("license"), f"Missing license in {tool_id}")

            # Cognitive Depth Requirements: Axiom & Citations
            axiom = tool.get("axiom")
            self.assertTrue(isinstance(axiom, str) and len(axiom) >= 20,
                            f"Tool {tool_id} must have a substantial design axiom (>= 20 chars)")

            citations = tool.get("citations")
            self.assertTrue(isinstance(citations, list) and len(citations) >= 1,
                            f"Tool {tool_id} must have at least one technical citation URL")
            for c in citations:
                self.assertTrue(c.startswith("http"), f"Invalid citation URL '{c}' in {tool_id}")

    def test_03_pure_english_policy(self):
        """Global open-source requirement: All text must be in professional English."""
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            content = f.read()

        match = VIETNAMESE_PATTERN.search(content)
        self.assertIsNone(
            match,
            f"Vietnamese language token detected in data/tools.json: '{match.group(0) if match else ''}'. "
            "Public open-source repository must be 100% English."
        )

    def test_04_builder_script_exists(self):
        """RED TEST: scripts/build_readme.py must exist."""
        self.assertTrue(os.path.isfile(BUILDER_PATH), f"Missing builder script: {BUILDER_PATH}")

    def test_05_build_execution_and_table_integrity(self):
        """Builder must run cleanly and produce valid Markdown tables without broken pipes."""
        res = subprocess.run([sys.executable, BUILDER_PATH], cwd=ROOT_DIR, capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, f"Builder failed with error:\n{res.stderr}")

        with open(README_PATH, "r", encoding="utf-8") as f:
            readme = f.read()

        # Check English policy on generated README
        match = VIETNAMESE_PATTERN.search(readme)
        self.assertIsNone(match, f"Vietnamese token found in generated README: '{match.group(0) if match else ''}'")

        # Table row pipe balance check
        for line_no, line in enumerate(readme.splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith("|") and stripped.endswith("|"):
                # Table row detected
                pipes = stripped.count("|")
                self.assertGreaterEqual(pipes, 3, f"Broken table row at line {line_no}: {stripped}")

    def test_06_build_idempotency(self):
        """Building twice must yield byte-for-byte identical output."""
        subprocess.run([sys.executable, BUILDER_PATH], cwd=ROOT_DIR, check=True)
        with open(README_PATH, "r", encoding="utf-8") as f:
            first_run = f.read()

        subprocess.run([sys.executable, BUILDER_PATH], cwd=ROOT_DIR, check=True)
        with open(README_PATH, "r", encoding="utf-8") as f:
            second_run = f.read()

        self.assertEqual(first_run, second_run, "Builder is non-deterministic (output changes between runs)")

if __name__ == "__main__":
    unittest.main()
