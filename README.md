## 🚀 LaunchLab UniFAP — Guia de Execução do Desafio Semanal
Este é um repositório corporativo e pedagógico de alto desempenho. A sua célula deve seguir rigorosamente as diretrizes contidas neste documento para validar as competências e conquistar a certificação da semana.


## 🛠️ 1. Instruções Iniciais de Configuração (Proibido dar FORK)
O ecossistema do LaunchLab simula o ambiente de engenharia de software do mercado real. Por questões de governança de TI e compliance corporativo, o fluxo de clonagem do projeto deve seguir regras estritas:

1. NÃO DEIXE UM FORK: É terminantemente proibido utilizar o botão Fork do GitHub neste repositório. O fork vincula seu código publicamente ao perfil do professor, quebrando o isolamento das equipes.
2. USE O TEMPLATE: O integrante líder da célula deve clicar exclusivamente no botão verde "Use this template" ➔ "Create a new repository".
3. ALTERE O OWNER: Na tela de criação do novo repositório, mude obrigatoriamente o campo Owner (Dono) do seu perfil pessoal para a organização oficial do programa: LaunchLab-UniFAP.
4. NOMENCLATURA PADRÃO: Nomeie o repositório utilizando estritamente a tag da sua bancada: desafio-w[NUMERO_DA_SEMANA]-[CURSO]-celula[NUMERO_DA_BANCADA]. (Exemplo: desafio-w2-ads-celula04).
5. CONVITE AO PARCEIRO E MONITOR: Vá em Settings ➔ Collaborators ➔ Add people e convide o outro membro da sua dupla e o usuário do GitHub do seu Embaixador.


## 👥 2. Matriz de Papéis e Responsabilidades na Célula
As células operam como equipes autônomas focadas na identidade e no orgulho de cada curso. Ninguém trabalha isolado.
## 🚀 O Papel do Desenvolvedor de ADS

* Missão: Construir o motor operacional, a mecânica lógica e a estabilidade das funções do software.
* Responsabilidade: Implementar algoritmos limpos, garantir o tratamento completo de exceções em tempo de execução e assegurar o sucesso nos testes de integração automatizados do sistema.

## 💼 O Papel do Desenvolvedor de SI

* Missão: Desenvolver a arquitetura estrutural de dados, governança de TI e regras estratégicas de negócio do projeto.
* Responsabilidade: Estruturar os metadados corporativos, implementar funções de validação de viabilidade econômica/processos e redigir as seções de conformidade, compliance legal e impacto do sistema.

## 🛡️ O Papel do Aluno Embaixador

* Missão: Atuar como Líder Técnico e monitor preventivo de ritmo ao longo da semana.
* Responsabilidade: Auditar os gráficos de commits, remover impedimentos de versionamento de código e responder às Issues abertas pelas células utilizando exclusivamente o método socrático.


## ⚠️ 3. Política de Compliance e Uso de Inteligência Artificial (IA)
O uso de ferramentas de IA (como ChatGPT, GitHub Copilot ou Claude) no LaunchLab UniFAP é regulado por normas estritas de ética profissional:

* 🟢 O que é PERMITIDO (Uso como Assistente): Utilizar a IA para explicar mensagens de erro retornadas pelo console do terminal, sugerir conceitos de sintaxe estruturada ou auxiliar na formatação de arquivos markdown.
* 🔴 O que é PROIBIDO (Sujeito a Retenção de Medalha - ND): Gerar o código-fonte por completo via prompts, copiar e colar funções inteiras sem compreender a mecânica, ou utilizar robôs para redigir as análises textuais do relatório.
* A Auditoria Docente: O professor pode realizar inspeções e arguições orais surpresa. Se um aluno for questionado em sala e não souber explicar a arquitetura ou o funcionamento do código assinado por ele, a competência será marcada imediatamente como Não Desenvolvida (ND) para toda a célula, acionando o Contrato de Convivência.


## ▶️ 4. Execução e validação

O projeto utiliza somente a biblioteca padrão do **Python 3.9 ou superior** e
não exige instalação de dependências externas.

### Projeção epidemiológica

O cálculo projeta um único ciclo pelo modelo multiplicativo:

```text
focos projetados = focos atuais × taxa de reprodução
```

As entradas precisam ser números reais, finitos e não negativos. Para executar
o exemplo incluído no projeto:

```bash
python3 src/endemia.py
```

### Relatório de rastreabilidade

Por padrão, o script audita os commits não relacionados a merge da semana atual:

```bash
python3 src/rastreabilidade_si.py
```

O período, repositório e tolerância podem ser informados explicitamente:

```bash
python3 src/rastreabilidade_si.py \
  --desde 2026-09-14 \
  --ate 2026-09-20 \
  --tolerancia 1 \
  --json
```

A isonomia considera a diferença entre as quantidades de commits por e-mail.
Ela é apenas um indicador quantitativo: tamanho, complexidade e qualidade das
contribuições também precisam ser avaliados na revisão humana.

### Testes

```bash
python3 -m unittest discover -s tests -v
```

O workflow executa a verificação de sintaxe, os testes e a auditoria em pushes
e pull requests. As regras declaradas em `docs/governanca_dados.json` também
devem ser configuradas na proteção da branch `main`; o manifesto não substitui
as configurações do GitHub.

## 📑 5. Relatório de Entrega da Célula (Preenchimento Obrigatório)
Instrução: Edite as seções abaixo preenchendo as evidências críticas da dupla até o prazo limite estipulado no ciclo semanal.
## 📂 Identificação

* Curso: Sistemas de Informação
* Membro 1 (Nome & GitHub): @viniciuslacerd4 - Vinícius Lacerda Borges
* Membro 2 (Nome & GitHub): @matheusbwv - Matheus Wenes
* Embaixador Vinculado: @CaioTarso - Caio Tarso

## 🌍 Seção de Análise Crítica (Formação Geral)

Com base no cenário proposto da semana, descreva qual o impacto humano, social, ético ou ambiental da tecnologia que sua célula colocou em produção. Como as decisões de código impactam o mundo físico e a vida do cidadão/empresa?

💬 RESPOSTA DA CÉLULA: A projeção de focos pode apoiar a vigilância
epidemiológica na priorização de áreas, equipes e recursos. Por isso, um erro de
cálculo ou a aceitação de entradas inválidas poderia superestimar ou subestimar
o cenário e influenciar negativamente decisões que afetam a população. Para
reduzir esse risco, limitamos a projeção a um ciclo bem definido, validamos
valores negativos, não numéricos e não finitos e cobrimos esses casos com testes
automatizados. Também declaramos no manifesto que dados identificáveis de
pacientes não são permitidos e que informações epidemiológicas devem ser
anonimizadas, pseudonimizadas ou agregadas. Reconhecemos que este cálculo é uma
simplificação educacional e não deve ser usado isoladamente para orientar uma
decisão de saúde pública.

## 💻 Seção de Engenharia e Governança de TI

Justifique a decisão de arquitetura técnica adotada pela célula nesta entrega. Como as regras de negócio de ADS e as estruturas de dados de SI foram construidas para garantir que a solução seja escalável e de fácil manutenção?

💬 RESPOSTA DA CÉLULA: Organizamos a solução por responsabilidades. O arquivo
`src/endemia.py` contém apenas a regra de projeção e a validação das entradas;
`src/rastreabilidade_si.py` coleta o histórico Git e transforma os commits em
um relatório estruturado; e `docs/governanca_dados.json` mantém as políticas de
licença, LGPD e colaboração em formato legível por pessoas e por ferramentas.
As funções possuem entradas e saídas claras, tratamento explícito de erros e
dependem somente da biblioteca padrão do Python, o que reduz o acoplamento e
facilita a execução em outros ambientes. Os testes automatizados verificam as
regras de cálculo, rastreabilidade e governança, enquanto o GitHub Actions
executa compilação, testes, auditoria e validação das mensagens de commit. Essa
separação permite evoluir cada parte sem misturar a regra epidemiológica com a
infraestrutura de auditoria.

## 🛠️ Diário de Bordo da Bancada

* Maior travamento técnico superado pela dupla durante a semana: integrar as
  contribuições desenvolvidas separadamente e transformar o código inicial em
  uma entrega executável. O histórico mostra primeiro a preparação do
  repositório, depois a inclusão da governança e da rastreabilidade e, por fim,
  a correção do erro de sintaxe no cálculo, a definição do modelo de um ciclo e
  a inclusão dos testes. Também foi necessário fortalecer o workflow, pois a
  versão inicial conseguia passar sem executar o código Python.
* Como a intervenção ou a Issue aberta para o Embaixador ajudou a destravar a
  célula: o embaixador Caio Tarso preparou o repositório, enviou os convites de
  acesso e acompanhou a equipe, oferecendo suporte e orientação conforme as
  dúvidas surgiram. Esse apoio permitiu organizar o fluxo de branches e commits
  e manter os integrantes trabalhando no mesmo repositório.



## Lembrete de Fechamento: Garanta que todo o projeto esteja commitado na branch principal ('main') e responda ao Micro Simulado individual no AVA antes do prazo limite.
