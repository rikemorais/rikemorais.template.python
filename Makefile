.DEFAULT_GOAL = help

help:
	@echo "-------------------------------HELP-------------------------------"
	@echo
	@echo "- make docs: Executa e a Abre a Documentação no Navegador"
	@echo "- make interrogate: Verifica a cobertura de Docstrings no código."
	@echo
	@echo "------------------------------------------------------------------"

.PHONY: docs
docs:
	open http://127.0.0.1:8000/
	mkdocs serve

.PHONY: interrogate
interrogate:
	interrogate -vv