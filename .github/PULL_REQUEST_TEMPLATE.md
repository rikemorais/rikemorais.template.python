<DETAILS open>
<SUMMARY><H2>✏️ Descrição</H2></SUMMARY>
Escreva um resumo do Projeto
</DETAILS>

<DETAILS open>
<SUMMARY> 📑 <H2>Tipo de Mudança</H2></SUMMARY><BR>
Selecione o tipo mais apropriado de mudança:

- [ ] Correção de Bugfix <SPAN TITLE="Correções de erros ou defeitos no código existente.">ℹ️</SPAN>
- [ ] Nova Feature <SPAN TITLE="Adição de uma nova funcionalidade ou recurso ao projeto.">ℹ️</SPAN>
- [ ] Refatoração de Código <SPAN TITLE="Modificações no código para melhorar a legibilidade, estrutura ou desempenho sem alterar o comportamento funcional.">ℹ️</SPAN>
- [ ] Documentação <SPAN TITLE="Mudanças na documentação do projeto, como README, wikis, ou comentários no código(inclusive testes).">ℹ️</SPAN> 
- [ ] Melhoria <SPAN TITLE="Melhorias gerais que não se encaixam nas categorias acima, como otimização de desempenho.">ℹ️</SPAN>
- [ ] Dependências <SPAN TITLE="Atualizações, adições ou remoções de bibliotecas e dependências do projeto.">ℹ️</SPAN>
- [ ] Testes <SPAN TITLE="Adição ou alteração de testes automatizados, incluindo testes unitários, de integração, etc.">ℹ️</SPAN>
- [ ] Configurações <SPAN TITLE="Alterações em arquivos de configuração, variáveis de ambiente, ou scripts de construção e implantação.">ℹ️</SPAN>

</DETAILS>

<DETAILS open>
<SUMMARY>💣 <H2>Impacto da Mudança</H2></SUMMARY><BR>
Defina o impacto desta mudança:

- [ ] **Pequeno**: Mudança que afeta poucas partes, como por exemplo modificações/inserções que não adicionam ou removem uma funcionalidade/comportamento (pode ser um hotfix simples, correção de typo ou type-hint, alguma alteração de código por conta de PEP etc), atualização de dependência que não seja crítica (caso do cryptography é crítico, por exemplo).
- [ ] **Médio**: Mudança que afeta algumas partes, como por exemplo alterar o input e output de uma funcionalidade (incluindo type-hints), adição ou remoção de funcionalidade/comportamento em um contexto já existente na aplicação, adição ou remoção de dependências que afetam scripts novos e já existentes.
- [ ] **Grande**: Mudança significativa que afeta o comportamento e contexto da aplicação, como por exemplo, um novo módulo (podendo ter vínculo com outros ou não), adição/remoção/atualização de dependência que gere grande impacto no projeto (como o SQLAlchemy da versão 1 para 2), refatoração da estrutura da aplicação (como já aconteceu no FS com o ETL e com a API).
</DETAILS>

<DETAILS>
<SUMMARY>🐛 <H2>Como foi Testado? </H2></SUMMARY><BR>
Uma descrição de como os testes foram realizados.
</DETAILS>

<DETAILS open>
<SUMMARY>✅ <H2>Checklist</H2></SUMMARY><BR>
Marque as ações que foram tomadas:

- [ ] Meu código segue as [diretrizes de estilo](https://contameupag.atlassian.net/wiki/spaces/MOTC/pages/2544730141/Pre-commit) do time (black, isort e flake8);
- [ ] Executei o pre-commit e todos os checks passaram;
- [ ] Revisei minhas mudanças de código para garantir clareza e conformidade;
- [ ] Comentei o código em áreas complexas para facilitar o entendimento;
- [ ] Realizei as alterações correspondentes na documentação (Confluence, wikis, README..)
- [ ] Adicionei ou atualizei os testes apropriados, assegurando que minha correção é eficaz ou que meu recurso funciona;
- [ ] Verifiquei o tamanho da PR e a dividi em partes menores quando necessário, respeitando os princípios de PRs atômicas;
- [ ] Certifiquei-me de que meu código não contém nenhum dado sensível ou que infrinja as normas de segurança da informação (como segredos, dados sensíveis..);
- [ ] Analisei o impacto de performance e fiz otimizações quando aplicável
- [ ] Assegurei que as novas dependências estão justificadas e não trazem riscos;
- [ ] Incluí informações suficientes na descrição da PR para permitir uma revisão completa (contexto, link dos cards, screenshots, se aplicável).
</DETAILS>

<DETAILS>
<SUMMARY>🔗 <H2>Links</H2></SUMMARY><BR>
Poste aqui os links importantes do Pull Request.
</DETAILS>