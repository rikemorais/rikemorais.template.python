.DEFAULT_GOAL = help

help:
	@echo "-------------------------------HELP-------------------------------"
	@echo
	@echo "- make docs: Executa e a Abre a Documentação no Navegador"
	@echo
	@echo "------------------------------------------------------------------"

.PHONY: docs
docs:
	open http://127.0.0.1:8000/
	mkdocs serve
