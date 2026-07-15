.PHONY: build validate audit check help

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

# Finish line: data well-formed, still an AI-native loop, and generated docs match.
check: validate audit
	python3 scripts/build.py --check
