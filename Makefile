.PHONY: install test health lint python-examples

install:
	cd examples/python && pip install -r requirements.txt -r requirements-dev.txt

test:
	cd examples/python && python -m unittest discover -s tests -v

health:
	cd examples/python && python health_check.py

lint:
	cd examples/python && python -m ruff check . || true

python-examples:
	@echo "Run: make install && export MULTILOGIN_TOKEN=... MULTILOGIN_PROFILE_ID=..."
	@echo "  make health"
	@echo "  cd examples/python && python list_profiles.py"
