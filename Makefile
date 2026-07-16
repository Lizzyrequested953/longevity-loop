.PHONY: build validate audit site graph track check help

help:
	@echo "longevity-loop — an AI-native compounding loop for aging science"
	@echo "  make build     Regenerate README.md + docs/ROADMAP.md from data/*.yml"
	@echo "  make validate  Schema-gate data/*.yml"
	@echo "  make audit     Self-audit vs the AI-native loop principles (data/loop.yml)"
	@echo "  make check     validate + audit + build drift-gate (CI finish line)"

build:
	python3 scripts/build.py

validate:
	python3 scripts/validate.py

audit:
	python3 scripts/audit.py --gate 80

site:
	python3 scripts/build_site.py
	python3 scripts/build_graph.py

graph:
	python3 scripts/build_graph.py

# Refresh live frontier signal (arXiv + GitHub) into data/_frontier.yml (needs network).
track:
	python3 scripts/track.py

# Finish line: data well-formed, still an AI-native loop, and generated docs match.
check: validate audit
	python3 scripts/build.py --check
