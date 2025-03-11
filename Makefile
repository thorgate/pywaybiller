OPENAPI_GENERATOR_VERSION ?= v7.12.0
API_HOST ?= app.waybiller.com

.PHONY:
lint:
	poetry run ruff check --select I pywaybiller --exclude pywaybiller/openapi_client
	poetry run ruff check pywaybiller --exclude pywaybiller/openapi_client

.PHONY:
fmt:
	poetry run ruff check --select I pywaybiller --fix --exclude pywaybiller/openapi_client
	poetry run ruff check pywaybiller --fix --exclude pywaybiller/openapi_client
	poetry run ruff format pywaybiller --exclude pywaybiller/openapi_client

.PHONY:
test: # run tests quickly with the default Python
	poetry run pytest

.PHONY:
test-all: # run tests on every Python version with tox
	tox

.PHONY:
openapi-fetch:
	curl https://$(API_HOST)/api/schema/ | poetry run python -c "import json; import sys; print(json.dumps(json.load(sys.stdin), indent=2))" > ./pywaybiller/openapi/waybiller_schema.json

.PHONY:
openapi-patch: openapi-fetch
	diff -Naur ./pywaybiller/openapi/waybiller_schema.json ./pywaybiller/openapi/waybiller_schema-patched.json > ./pywaybiller/openapi/patches/schema-fixes.patch || echo "Patch created"

.PHONY:
openapi-apply-patch: openapi-fetch
	patch -p0 < ./pywaybiller/openapi/patches/schema-fixes.patch

.PHONY:
openapi-build:
	rm -rf .openapi
	rm -rf ./pywaybiller/openapi_client
	rm -rf ./pywaybiller/docs
	docker run --rm --ulimit nofile=122880:122880  -v ${PWD}/pywaybiller/openapi/update_schema.sh:/helpers/update_schema.sh -v ${PWD}/pywaybiller/openapi/waybiller_schema.json:/waybiller_schema.json -v ${PWD}/.openapi/:/openapi openapitools/openapi-generator-cli:$(OPENAPI_GENERATOR_VERSION) /bin/bash /helpers/update_schema.sh /waybiller_schema.json
	sudo chown -R ${USER} .openapi
	cp -r .openapi/openapi_client pywaybiller/openapi_client
	cp -r .openapi/docs pywaybiller/docs
	rm -rf .openapi
	poetry run ruff check --select I pywaybiller/openapi_client --fix
	poetry run ruff format pywaybiller/openapi_client

.PHONY:
openapi: openapi-apply-patch openapi-build
