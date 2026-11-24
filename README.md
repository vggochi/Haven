# HAVEN
### Every voice deserves to be understood.

**Plataforma Inteligente de Comunicação e Acessibilidade em Libras**

> Documentação geral do projeto — TCC

---

# 1. Sobre o projeto

O **HAVEN** é uma plataforma tecnológica voltada à acessibilidade e à comunicação entre pessoas surdas, pessoas com deficiência auditiva e pessoas ouvintes que não dominam a Língua Brasileira de Sinais (Libras).

A proposta é desenvolver um ambiente digital que utilize tecnologias de reconhecimento visual, inteligência artificial e processamento de informações para facilitar a comunicação em diferentes situações do cotidiano.

O sistema pretende oferecer ferramentas de tradução, consulta de sinais, aprendizagem de Libras e acompanhamento das atividades dos usuários.

O HAVEN busca reduzir barreiras de comunicação em ambientes como:

- Hospitais e unidades de saúde.
- Escolas e instituições de ensino.
- Estabelecimentos comerciais.
- Órgãos públicos.
- Ambientes profissionais.
- Situações cotidianas.

## 1.1. Problema identificado

A comunicação entre pessoas surdas que utilizam Libras e pessoas ouvintes que não conhecem essa língua ainda representa uma barreira significativa.

Em muitos ambientes, a ausência de pessoas capacitadas em Libras dificulta o atendimento, a compreensão de informações e a participação social.

Embora existam dicionários digitais e ferramentas de aprendizagem, ainda existe espaço para desenvolver soluções que integrem consulta de sinais, reconhecimento visual, tradução e aprendizagem em uma única plataforma.

## 1.2. Solução proposta

O HAVEN pretende reunir recursos de acessibilidade em uma plataforma integrada, permitindo:

- Reconhecer sinais de Libras por meio de uma câmera, dentro de um vocabulário e escopo de reconhecimento definidos.
- Converter textos em representações visuais de sinais.
- Consultar um dicionário digital de Libras.
- Aprender novos sinais por meio de módulos e exercícios.
- Armazenar o histórico de traduções.
- Salvar sinais favoritos.
- Acompanhar o progresso de aprendizagem.

## 1.3. Objetivo geral

Desenvolver uma plataforma inteligente de acessibilidade que utilize recursos tecnológicos para facilitar a comunicação em Libras e ampliar o acesso à informação e à aprendizagem.

## 1.4. Objetivos específicos

- Desenvolver uma interface acessível e intuitiva.
- Implementar um sistema de cadastro e autenticação.
- Criar um banco de dados estruturado para informações de Libras.
- Desenvolver um dicionário digital.
- Integrar recursos de reconhecimento visual.
- Implementar funcionalidades de tradução.
- Criar um ambiente de aprendizagem.
- Permitir o armazenamento do histórico e das preferências dos usuários.
- Garantir a proteção dos dados por meio de políticas de segurança.

---

# 2. Identidade do projeto

**Nome:** HAVEN

**Slogan:** Every voice deserves to be understood.

**Categoria:** Tecnologia, acessibilidade, saúde e qualidade de vida.

**Conceito:** Comunicação, inclusão, autonomia e acessibilidade.

## 2.1. Identidade visual

Paleta inicial proposta:

| Cor | Código | Aplicação |
|---|---|---|
| Midnight | `#101C35` | Fundo principal e elementos institucionais |
| Electric Blue | `#246BFD` | Botões e destaques |
| Ice | `#EAF2FF` | Fundos secundários |
| White | `#FFFFFF` | Textos e superfícies |

**Tipografia sugerida:**

- Sora: títulos.
- Inter: textos e conteúdo.
- Manrope: indicadores e números.

A interface deve transmitir confiança, modernidade, simplicidade e acessibilidade.

---

# 3. Público-alvo

O HAVEN é destinado principalmente a:

1. Pessoas surdas que utilizam Libras.
2. Pessoas com deficiência auditiva.
3. Pessoas ouvintes que desejam aprender Libras.
4. Profissionais de atendimento.
5. Instituições de ensino.
6. Estabelecimentos de saúde.
7. Organizações que desejam melhorar sua acessibilidade.

A experiência deve considerar diferentes níveis de familiaridade com tecnologia.

---

# 4. Funcionalidades principais

## 4.1. Cadastro e autenticação

O usuário poderá:

- Criar uma conta.
- Realizar login.
- Encerrar a sessão.
- Editar seu perfil.
- Alterar sua foto.
- Definir seu nível de conhecimento em Libras.
- Configurar preferências da plataforma.

A autenticação será realizada pelo Supabase Auth.

## 4.2. Tradutor: Libras para Português

Essa funcionalidade permitirá utilizar a câmera para capturar movimentos das mãos e reconhecer sinais dentro do vocabulário suportado pelo modelo.

Fluxo esperado:

1. O usuário acessa o tradutor.
2. Autoriza o acesso à câmera.
3. O sistema captura os movimentos.
4. O modelo identifica os sinais suportados.
5. O resultado é apresentado em português.
6. O usuário poderá ouvir o resultado por síntese de voz.
7. A tradução poderá ser salva no histórico.

Recursos previstos:

- Captura pela câmera.
- Detecção de mãos.
- Identificação de sinais.
- Apresentação do resultado.
- Indicador de reconhecimento, quando disponível.
- Reprodução de texto em áudio.
- Repetição da captura.
- Feedback e correção.

**Importante:** Libras é uma língua natural com gramática própria. Reconhecer posições das mãos isoladamente não equivale a traduzir Libras. O projeto deverá considerar movimento, contexto, expressões faciais e outros elementos linguísticos.

O primeiro protótipo deverá trabalhar com um vocabulário controlado e validado por pessoas fluentes em Libras.

## 4.3. Tradutor: Português para Libras

Essa funcionalidade permitirá inserir uma frase ou palavra em português e visualizar sua representação em Libras.

Fluxo esperado:

1. O usuário digita um texto.
2. O sistema processa a entrada.
3. O sistema identifica os sinais disponíveis.
4. Apresenta os sinais por meio de vídeos, animações ou representações visuais.
5. O usuário acompanha a sequência.

A representação deve respeitar a estrutura linguística da Libras, e não simplesmente substituir cada palavra do português por um gesto.

Recursos previstos:

- Campo de texto.
- Processamento da frase.
- Consulta ao dicionário.
- Apresentação dos sinais.
- Reprodução das demonstrações.
- Possibilidade de repetir a sequência.

## 4.4. Dicionário de Libras

O dicionário será uma das principais áreas do HAVEN.

A proposta é disponibilizar uma biblioteca organizada de sinais, com informações sobre significado, categorias, exemplos e demonstrações visuais.

Recursos:

- Busca por palavra.
- Busca por categoria.
- Busca alfabética.
- Busca por configuração de mão.
- Consulta de significados.
- Exemplos de utilização.
- Classe gramatical.
- Vídeos demonstrativos.
- Variações regionais.
- Sinais favoritos.

### Referências externas

**Dicionário de Libras do INES**

https://dicionario.ines.gov.br/

Recursos de referência:

- Busca por ordem alfabética.
- Busca por assunto.
- Busca por configuração de mão.
- Vídeos demonstrativos.
- Exemplos.
- Classe gramatical.

**Dicionário Libras — Acessibilidade Brasil**

http://www.acessibilidadebrasil.org.br/libras_3/

Recursos de referência:

- Busca por palavra.
- Busca por assunto.
- Busca por configuração de mão.
- Vídeos.
- Significados.
- Exemplos.
- Informações de origem.

Esses dicionários servirão como referência para o desenvolvimento do módulo.

**Atenção aos direitos de uso:** não copiar automaticamente vídeos, imagens ou descrições dos sites. É necessário verificar as licenças, permissões e condições de utilização. Sempre que possível, utilizar conteúdo próprio ou autorizado.

## 4.5. Aprendizagem de Libras

O módulo de aprendizagem permitirá que usuários estudem Libras de forma organizada.

Recursos:

- Módulos de aprendizagem.
- Lições.
- Vídeos explicativos.
- Exercícios.
- Questões de múltipla escolha.
- Atividades de identificação.
- Pontuação.
- Acompanhamento do progresso.
- Histórico de resultados.

Exemplo de organização:

- Módulo 1: Introdução à Libras.
- Módulo 2: Alfabeto manual.
- Módulo 3: Números.
- Módulo 4: Cumprimentos.
- Módulo 5: Família.
- Módulo 6: Saúde.
- Módulo 7: Educação.
- Módulo 8: Situações cotidianas.

## 4.6. Histórico de traduções

O usuário poderá consultar suas traduções anteriores.

Informações:

- Tipo de tradução.
- Conteúdo original.
- Resultado.
- Data e horário.
- Duração do processamento.
- Status.

## 4.7. Favoritos

Permite salvar sinais para consulta posterior.

Cada usuário terá sua própria lista de favoritos.

## 4.8. Feedback das traduções

O usuário poderá:

- Avaliar uma tradução.
- Informar se o resultado foi adequado.
- Sugerir uma correção.
- Enviar comentários.

Esses dados poderão auxiliar na avaliação e melhoria do sistema.

---

# 5. Tecnologias previstas

A arquitetura tecnológica inicial será composta pelas seguintes ferramentas.

| Tecnologia | Utilização |
|---|---|
| React | Desenvolvimento da interface |
| JavaScript | Lógica da aplicação |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização |
| Supabase | Backend e banco de dados |
| PostgreSQL | Banco de dados relacional |
| Supabase Auth | Cadastro e autenticação |
| Supabase Storage | Armazenamento de arquivos |
| Python | Desenvolvimento do reconhecimento visual |
| OpenCV | Processamento de imagens |
| MediaPipe | Detecção e rastreamento das mãos |
| TensorFlow ou PyTorch | Treinamento e execução de modelos de aprendizado de máquina |

A biblioteca de machine learning ainda deverá ser escolhida conforme os testes e a arquitetura do modelo.

## 5.1. Arquitetura geral

O projeto terá três componentes principais:

**Frontend — React**

Responsável pela interface, navegação, formulários, câmera, exibição de resultados e comunicação com o Supabase e o serviço de reconhecimento.

**Backend e banco de dados — Supabase**

Responsável por autenticação, persistência dos dados, relacionamentos, armazenamento e segurança.

**Reconhecimento visual — Python**

Responsável pelo processamento de imagens, detecção das mãos e reconhecimento dos sinais suportados.

Fluxo geral:

Usuário → React → Serviço de reconhecimento → Resultado da tradução → Supabase.

O frontend também poderá consultar diretamente o Supabase utilizando a chave pública apropriada e políticas RLS.

---

# 6. Banco de dados — Supabase

O banco de dados utilizará PostgreSQL por meio do Supabase.

A estrutura foi planejada para separar dicionário, usuários, traduções, aprendizagem e funcionalidades complementares.

## 6.1. Tabelas planejadas

### Módulo 1 — Dicionário

| Tabela | Responsabilidade |
|---|---|
| `categorias_sinais` | Categorias e assuntos do dicionário |
| `sinais` | Cadastro dos sinais e palavras |
| `variantes_sinais` | Variações regionais e linguísticas |
| `videos_sinais` | Vídeos demonstrativos |

### Módulo 2 — Usuários e traduções

| Tabela | Responsabilidade |
|---|---|
| `perfis` | Informações complementares dos usuários |
| `traducoes` | Histórico de traduções |
| `itens_traducao` | Palavras e sinais individuais de cada tradução |
| `favoritos` | Sinais salvos pelos usuários |
| `feedback_traducoes` | Avaliações e correções |

### Módulo 3 — Aprendizagem

| Tabela | Responsabilidade |
|---|---|
| `modulos_aprendizado` | Organização dos módulos |
| `licoes` | Conteúdos de cada módulo |
| `exercicios` | Atividades e perguntas |
| `resultados_exercicios` | Respostas e pontuações |
| `progresso_aprendizado` | Progresso individual |

### Módulo 4 — Sistema

| Tabela | Responsabilidade |
|---|---|
| `notificacoes` | Avisos e atualizações |
| `historico_acessos` | Registro de atividades relevantes |

**Total planejado: 16 tabelas.**

### 6.2. Ajuste importante no módulo do dicionário

O modelo inicial deverá ser refinado para representar corretamente a estrutura dos dicionários de Libras.

Recomendações:

- Uma palavra pode ter mais de um significado.
- Um sinal pode pertencer a várias categorias.
- Um sinal pode possuir diferentes vídeos.
- Um sinal pode apresentar variantes regionais.
- Uma configuração de mão pode ser utilizada em diferentes sinais.
- Vídeos e imagens devem ser armazenados no Supabase Storage, e suas referências ficam no PostgreSQL.

Para isso, avaliar a inclusão de:

- `acepcoes_sinais`: diferentes significados de um sinal ou palavra.
- `sinal_categorias`: relacionamento entre sinais e múltiplas categorias.
- `configuracoes_mao`: catálogo de configurações de mão.

Essas três estruturas são propostas de evolução e ainda não fazem parte do SQL inicial de 16 tabelas.

### 6.3. Relacionamentos principais

- `categorias_sinais` → `sinais`.
- `sinais` → `variantes_sinais`.
- `sinais` → `videos_sinais`.
- `auth.users` → `perfis`.
- `perfis` → `traducoes`.
- `traducoes` → `itens_traducao`.
- `perfis` → `favoritos`.
- `sinais` → `favoritos`.
- `modulos_aprendizado` → `licoes`.
- `licoes` → `exercicios`.
- `perfis` → `resultados_exercicios`.
- `exercicios` → `resultados_exercicios`.
- `perfis` → `progresso_aprendizado`.
- `licoes` → `progresso_aprendizado`.
- `traducoes` → `feedback_traducoes`.
- `perfis` → `notificacoes`.
- `perfis` → `historico_acessos`.

### 6.4. Segurança e RLS

Todas as tabelas do schema `public` deverão possuir Row Level Security (RLS) ativado.

Regras gerais:

- Usuários só podem consultar e modificar seus próprios perfis.
- Cada usuário só pode acessar suas próprias traduções.
- Cada usuário só pode acessar seus próprios favoritos.
- Cada usuário só pode consultar e atualizar seu progresso.
- Conteúdos publicados do dicionário podem ser consultados publicamente.
- Conteúdos não publicados não devem ser acessíveis ao público.
- Resultados e pontuações devem ser protegidos contra alterações indevidas.
- Notificações devem ser criadas por uma operação confiável do backend.

O acesso deve ser validado por propriedade dos registros, não apenas pelo fato de o usuário estar autenticado.

**Importante:** a chave `service_role` ou qualquer chave secreta nunca deve ser exposta no frontend.

---

# 7. Armazenamento — Supabase Storage

O Supabase Storage será utilizado para arquivos e mídias.

Buckets sugeridos:

| Bucket | Conteúdo |
|---|---|
| `avatars` | Fotos de perfil |
| `videos-sinais` | Vídeos demonstrativos de Libras |
| `imagens-sinais` | Imagens relacionadas aos sinais |
| `materiais-aprendizado` | Materiais das lições |
| `arquivos-traducoes` | Arquivos enviados para processamento, quando necessário |

As políticas de Storage deverão respeitar o nível de acesso de cada arquivo.

Vídeos públicos autorizados podem ter leitura pública. Arquivos privados de usuários devem exigir autenticação e autorização adequada.

---

# 8. Estrutura sugerida do projeto

Uma organização inicial possível:

```text
HAVEN/
│
├── frontend/
│   ├── public/
│   │
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   │   ├── Home/
│   │   │   ├── Login/
│   │   │   ├── Register/
│   │   │   ├── Dashboard/
│   │   │   ├── LibrasToText/
│   │   │   ├── TextToLibras/
│   │   │   ├── Dictionary/
│   │   │   ├── Learning/
│   │   │   ├── History/
│   │   │   └── Profile/
│   │   │
│   │   ├── services/
│   │   │   ├── supabase.js
│   │   │   ├── auth.js
│   │   │   ├── translations.js
│   │   │   └── dictionary.js
│   │   │
│   │   ├── contexts/
│   │   ├── hooks/
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── .env.local
│   └── package.json
│
├── backend/
│   ├── recognition/
│   │   ├── models/
│   │   ├── datasets/
│   │   ├── preprocessing/
│   │   ├── training/
│   │   └── inference/
│   │
│   ├── api/
│   ├── requirements.txt
│   └── main.py
│
├── database/
│   ├── schema.sql
│   ├── policies.sql
│   └── seed.sql
│
├── docs/
│   ├── architecture.md
│   ├── database.md
│   └── project-plan.md
│
└── README.md
```

Essa é uma estrutura sugerida. Ela poderá ser adaptada à organização real dos arquivos durante o desenvolvimento.

---

# 9. Requisitos para executar o projeto

## 9.1. Ferramentas necessárias

- Node.js em versão LTS compatível com as dependências escolhidas.
- npm.
- Visual Studio Code ou editor equivalente.
- Git.
- Conta no Supabase.
- Navegador atualizado.
- Python 3.11 ou versão compatível com as bibliotecas selecionadas.
- Ambiente com câmera para testar o reconhecimento visual.

## 9.2. Configuração do frontend

Instalar as dependências:

```bash
cd frontend
npm install
```

Criar o arquivo `.env.local`:

```env
VITE_SUPABASE_URL=https://SEU-PROJETO.supabase.co
VITE_SUPABASE_ANON_KEY=SUA_CHAVE_PUBLICA
VITE_RECOGNITION_API=http://localhost:8000
```

A chave pública pode ser a chave publishable atual do Supabase ou a chave `anon` legada, caso o projeto ainda utilize esse formato.

Não colocar chaves secretas ou `service_role` nesse arquivo do frontend.

Executar:

```bash
npm run dev
```

Gerar versão de produção:

```bash
npm run build
```

## 9.3. Configuração do Supabase

1. Criar um projeto no Supabase.
2. Configurar o PostgreSQL.
3. Executar o SQL de criação das tabelas.
4. Conferir os relacionamentos.
5. Ativar e revisar as políticas RLS.
6. Configurar Supabase Auth.
7. Criar os buckets do Storage.
8. Configurar as permissões dos arquivos.
9. Inserir os primeiros dados do dicionário.
10. Testar as operações com usuários diferentes.

O projeto precisa de uma configuração adequada de autenticação, incluindo URLs de redirecionamento e confirmação de e-mail, se esse recurso for utilizado.

## 9.4. Configuração do serviço Python

Criar um ambiente virtual:

```bash
cd backend

python -m venv venv
```

Ativar no Windows:

```bash
venv\Scripts\activate
```

Instalar as dependências definidas no projeto:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` deverá conter as versões efetivamente testadas das bibliotecas utilizadas, como:

- OpenCV.
- MediaPipe.
- TensorFlow ou PyTorch.
- FastAPI ou Flask, caso seja utilizada uma API Python.

Iniciar a API dependerá do framework escolhido. Por exemplo, com FastAPI:

```bash
uvicorn main:app --reload
```

A API deverá receber os dados de entrada, processar os sinais e retornar resultados estruturados.

---

# 10. Reconhecimento de Libras e inteligência artificial

Essa é uma das partes tecnicamente mais importantes do HAVEN.

O reconhecimento visual não deve ser tratado apenas como identificação de imagens estáticas.

A aplicação poderá utilizar:

1. Captura de vídeo.
2. Detecção de mãos.
3. Identificação de pontos de referência das mãos.
4. Extração de características espaciais.
5. Análise temporal dos movimentos.
6. Classificação dos sinais suportados.
7. Conversão dos resultados para uma representação textual.

## 10.1. MediaPipe

Pode ser utilizado para detectar mãos e extrair pontos de referência.

Esses pontos poderão servir como entrada para um modelo de reconhecimento.

## 10.2. OpenCV

Pode auxiliar em:

- Captura de vídeo.
- Tratamento de imagens.
- Conversão de quadros.
- Pré-processamento.
- Integração com a câmera.

## 10.3. Modelo de reconhecimento

O modelo deverá ser treinado ou adaptado utilizando dados de sinais devidamente autorizados.

O conjunto de dados deverá considerar:

- Diferentes pessoas.
- Diferentes tons de pele.
- Diferentes posições de câmera.
- Diferentes iluminações.
- Diferentes velocidades de execução.
- Variações de movimentos.
- Diferenças regionais quando aplicáveis.

Para um primeiro protótipo, recomenda-se trabalhar com um conjunto limitado de sinais, validar a qualidade e expandir gradualmente.

## 10.4. Limitações e cuidados

O HAVEN não deve afirmar que traduz qualquer conversa em Libras de maneira perfeita.

A Libras possui estrutura gramatical própria e utiliza expressões faciais, movimentos, orientação espacial e outros elementos.

Um modelo limitado a posições das mãos poderá reconhecer alguns sinais, mas não compreenderá necessariamente frases completas.

O objetivo inicial é demonstrar uma solução funcional, mensurável e tecnicamente validada.

A plataforma deve auxiliar a comunicação, sem substituir intérpretes profissionais, especialmente em situações médicas, jurídicas ou de emergência.

---

# 11. Interface e telas previstas

A interface deverá seguir uma identidade visual consistente, com navegação simples e foco na acessibilidade.

Telas planejadas:

| Tela | Função |
|---|---|
| Landing Page | Apresentação do HAVEN |
| Login | Acesso à conta |
| Cadastro | Criação de conta |
| Dashboard | Painel principal |
| Libras → Texto | Reconhecimento pela câmera |
| Texto → Libras | Conversão e demonstração visual |
| Dicionário | Consulta de sinais |
| Detalhes do sinal | Informações e vídeos |
| Aprendizagem | Módulos e lições |
| Exercícios | Atividades práticas |
| Histórico | Traduções anteriores |
| Favoritos | Sinais salvos |
| Perfil | Dados e preferências |
| Configurações | Ajustes de acessibilidade |

## 11.1. Dashboard

O painel principal deverá apresentar:

- Saudação ao usuário.
- Acesso rápido aos dois tradutores.
- Acesso ao dicionário.
- Acesso à aprendizagem.
- Resumo do progresso.
- Últimas traduções.
- Sinais favoritos.

## 11.2. Acessibilidade da interface

A plataforma deverá considerar:

- Contraste adequado.
- Textos legíveis.
- Navegação por teclado.
- Descrições alternativas em imagens.
- Estados visuais claros.
- Botões com áreas de toque adequadas.
- Responsividade.
- Linguagem simples.
- Feedback visual das ações.

---

# 12. Segurança e privacidade

O HAVEN poderá lidar com informações pessoais, imagens, vídeos e registros de uso.

Portanto, será necessário:

- Utilizar autenticação segura.
- Aplicar RLS nas tabelas expostas.
- Proteger os arquivos no Storage.
- Evitar armazenar vídeos pessoais sem necessidade.
- Solicitar autorização para utilização da câmera.
- Informar quando a câmera estiver ativa.
- Definir políticas de retenção de dados.
- Permitir que usuários solicitem a exclusão de seus dados.
- Evitar o envio de informações sensíveis desnecessárias.
- Seguir a LGPD.

As gravações da câmera não deverão ser armazenadas automaticamente. O processamento deve priorizar a minimização de dados.

---

# 13. Etapas de desenvolvimento

O projeto deverá ser desenvolvido em etapas.

## Etapa 1 — Planejamento e documentação

- Definir requisitos.
- Finalizar identidade visual.
- Planejar arquitetura.
- Modelar o banco de dados.
- Criar protótipos no Figma.

## Etapa 2 — Backend e banco de dados

- Criar projeto Supabase.
- Criar tabelas.
- Configurar relacionamentos.
- Configurar RLS.
- Configurar autenticação.
- Criar buckets do Storage.
- Inserir dados iniciais.

## Etapa 3 — Frontend

- Criar estrutura React.
- Desenvolver identidade visual.
- Criar login e cadastro.
- Implementar dashboard.
- Criar dicionário.
- Desenvolver páginas de tradução.
- Implementar aprendizagem.
- Integrar histórico e favoritos.

## Etapa 4 — Serviço de reconhecimento

- Configurar Python.
- Integrar OpenCV.
- Integrar MediaPipe.
- Criar conjunto de dados.
- Treinar ou adaptar o modelo.
- Criar API.
- Integrar a API ao frontend.

## Etapa 5 — Integração

- Integrar autenticação.
- Integrar dicionário.
- Integrar traduções.
- Integrar reconhecimento.
- Integrar aprendizagem.
- Integrar armazenamento.

## Etapa 6 — Testes e validação

- Testar cadastro e login.
- Testar permissões.
- Testar RLS.
- Testar consultas do dicionário.
- Testar reconhecimento.
- Avaliar precisão.
- Testar em diferentes dispositivos.
- Validar os sinais com pessoas fluentes em Libras.
- Corrigir problemas de acessibilidade.

## Etapa 7 — Finalização

- Preparar demonstração.
- Documentar resultados.
- Preparar apresentação do TCC.
- Apresentar limitações.
- Demonstrar funcionalidades desenvolvidas.

---

# 14. Testes necessários

O projeto deverá possuir testes funcionais e de segurança.

### Autenticação

- Cadastro de usuário.
- Login.
- Logout.
- Recuperação de senha.
- Persistência da sessão.

### Banco de dados

- Inserção de sinais.
- Consulta de categorias.
- Consulta de vídeos.
- Registro de traduções.
- Consulta de favoritos.
- Registro de progresso.

### Segurança

- Um usuário não pode acessar traduções de outro.
- Um usuário não pode alterar o perfil de outro.
- Conteúdos não publicados não podem ser consultados publicamente.
- Usuários não podem manipular pontuações indevidamente.

### Reconhecimento

- Testar sinais individuais.
- Testar diferentes velocidades.
- Testar iluminação.
- Testar diferentes posições.
- Medir precisão e taxa de erro.
- Verificar o comportamento quando nenhum sinal é reconhecido.

---

# 15. Pontos que ainda precisam ser definidos

As decisões abaixo deverão ser tomadas durante o desenvolvimento:

- Qual será o modelo final de reconhecimento?
- Quantos sinais serão suportados no primeiro protótipo?
- Quais dados poderão ser utilizados para treinamento?
- Como será feita a validação linguística?
- Será utilizado avatar 3D, animações ou vídeos para representar Libras?
- Como será feita a interpretação de frases?
- Quais serão os critérios de avaliação do reconhecimento?
- Quais conteúdos do dicionário poderão ser utilizados legalmente?
- Como será feita a administração dos conteúdos?
- Qual será a política de armazenamento dos arquivos enviados?

Essas decisões não devem ser consideradas implementadas até que sejam desenvolvidas e testadas.

---

# 16. Estado atual do projeto

**Status geral: planejamento e estruturação do backend.**

Até o momento, foram definidos:

- Nome HAVEN.
- Slogan.
- Proposta e objetivos.
- Público-alvo.
- Funcionalidades principais.
- Identidade visual inicial.
- Tecnologias previstas.
- Referências de dicionários.
- Estrutura inicial do banco de dados.
- Estratégia de RLS.
- Organização inicial dos módulos.

### Banco de dados

Foi elaborado um SQL inicial com 16 tabelas:

1. `categorias_sinais`
2. `sinais`
3. `variantes_sinais`
4. `videos_sinais`
5. `perfis`
6. `traducoes`
7. `itens_traducao`
8. `favoritos`
9. `modulos_aprendizado`
10. `licoes`
11. `exercicios`
12. `resultados_exercicios`
13. `progresso_aprendizado`
14. `feedback_traducoes`
15. `notificacoes`
16. `historico_acessos`

**Atenção:** o SQL foi elaborado, mas não há confirmação de que tenha sido executado no Supabase. Também é necessário revisar o modelo do dicionário para contemplar acepções, múltiplas categorias e configurações de mão.

Não considerar nenhuma dessas funcionalidades como concluída apenas porque sua estrutura foi planejada.

---

# 17. Orientações para continuar o projeto

Ao continuar o desenvolvimento do HAVEN, seguir estas diretrizes:

1. Preservar o nome e a identidade visual do projeto.
2. Não alterar funcionalidades existentes sem necessidade.
3. Priorizar uma arquitetura organizada e escalável.
4. Não criar tabelas duplicadas.
5. Manter relacionamentos coerentes no PostgreSQL.
6. Aplicar RLS em todas as tabelas expostas.
7. Não expor chaves secretas no frontend.
8. Desenvolver funcionalidades de forma incremental.
9. Testar cada integração antes de avançar.
10. Validar os conteúdos de Libras com pessoas qualificadas.
11. Não afirmar que uma tradução funciona perfeitamente sem testes.
12. Manter a documentação atualizada.

Sempre que uma funcionalidade for implementada, atualizar este README para refletir o estado real do projeto.

---

# 18. Visão final do HAVEN

O HAVEN pretende ser mais do que um dicionário digital.

A proposta é construir um ambiente integrado de comunicação e aprendizagem, combinando acessibilidade, tecnologia e inteligência artificial.

O projeto reúne três pilares:

**COMUNICAR** — Facilitar a comunicação entre pessoas surdas e ouvintes.

**APRENDER** — Tornar o aprendizado de Libras mais acessível.

**CONECTAR** — Aproximar pessoas e reduzir barreiras de comunicação.

> HAVEN — Every voice deserves to be understood.

---

# RELATÓRIO TÉCNICO — HAVEN
## Desenvolvimento do backend e reconhecimento de Libras

**Projeto:** HAVEN  
**Área:** Tecnologia, acessibilidade e comunicação  
**Objetivo:** Desenvolver uma plataforma que facilite a comunicação entre pessoas surdas e ouvintes por meio de recursos de tradução e reconhecimento de Libras.

---

# 1. Objetivo do desenvolvimento atual

Nesta etapa, o foco foi estruturar e iniciar o backend do HAVEN, conectar a aplicação ao Supabase e preparar a infraestrutura necessária para implementar o reconhecimento de sinais de Libras utilizando a câmera.

A arquitetura está sendo desenvolvida com Python, FastAPI e Supabase, enquanto o reconhecimento visual será integrado ao frontend por meio de tecnologia de visão computacional.

# 2. Alterações realizadas

## 2.1. Configuração do ambiente Python

Foi configurado o ambiente virtual do backend, utilizando Python 3.13.

Também foram atualizadas as dependências do projeto no arquivo `requirements.txt`.

**Dependências adicionadas:**

| Biblioteca | Finalidade |
|---|---|
| NumPy | Operações matemáticas e processamento de dados numéricos |
| Scikit-learn | Treinamento e classificação de sinais |
| Joblib | Salvamento e carregamento de modelos treinados |

**Comando utilizado:**

```bash
python -m pip install -r requirements.txt
```

A instalação foi concluída com sucesso.

## 2.2. Criação do arquivo principal `main.py`

Foi criado o arquivo `main.py`, responsável por inicializar a API do HAVEN.

Foram implementados:

- Inicialização da aplicação FastAPI.
- Configuração do CORS para permitir comunicação com o frontend.
- Rota principal `/`.
- Rota de verificação `/api/health`.
- Importação e registro dos módulos de autenticação, perfil, preferências, traduções, aulas, progresso e dashboard.

**Resultado:** a API iniciou corretamente e retornou:

```json
{
  "success": true,
  "name": "HAVEN API",
  "message": "API funcionando corretamente.",
  "version": "1.0.0"
}
```

Isso confirma que a aplicação principal está respondendo.

## 2.3. Organização da arquitetura

Foi definida a seguinte organização para o backend:

```text
backend/
│
├── main.py
├── .env
├── requirements.txt
│
└── app/
    ├── __init__.py
    ├── config.py
    ├── security.py
    │
    ├── routes/
    │   ├── __init__.py
    │   ├── auth.py
    │   ├── profile.py
    │   ├── preferences.py
    │   ├── translations.py
    │   ├── lessons.py
    │   ├── progress.py
    │   └── dashboard.py
    │
    ├── schemas/
    │   ├── __init__.py
    │   ├── auth.py
    │   └── translations.py
    │
    └── services/
        ├── __init__.py
        ├── supabase.py
        ├── libras.py
        └── recognition.py
```

Essa estrutura separa as responsabilidades da aplicação, facilitando futuras atualizações e manutenção.

## 2.4. Integração com Supabase

Foi mantida a estrutura de comunicação com o Supabase por meio do arquivo:

`app/services/supabase.py`

Ele utiliza HTTPX para realizar requisições à API do Supabase.

Também foram mantidas as configurações:

- URL do projeto.
- Chave pública de acesso.
- Variáveis de ambiente.
- Autenticação por token.

O arquivo `app/config.py` centraliza essas configurações.

## 2.5. Autenticação e segurança

Foi mantido o sistema de autenticação utilizando Supabase Auth.

As funcionalidades previstas nas rotas existentes incluem:

- Cadastro de usuários.
- Login.
- Logout.
- Consulta dos dados do usuário autenticado.
- Validação do token de acesso.

O arquivo `app/security.py` verifica se a requisição possui um token Bearer válido antes de permitir o acesso às rotas protegidas.

## 2.6. Atualização do sistema de traduções

O arquivo `app/routes/translations.py` foi atualizado.

As funcionalidades anteriores foram preservadas:

- Tradução de texto para sinais.
- Consulta do histórico de traduções.
- Salvamento de traduções.
- Exclusão de uma tradução.
- Limpeza do histórico.

Também foi criada uma nova rota:

`POST /api/translations/sign-to-text/landmarks`

Essa rota prepara o backend para receber os pontos identificados pela câmera.

## 2.7. Validação dos movimentos das mãos

O arquivo `app/schemas/translations.py` recebeu novos modelos de validação:

- `LandmarkPoint`
- `LandmarkFrame`
- `SignLandmarksRequest`

A estrutura considera:

- 21 pontos por mão.
- Coordenadas tridimensionais X, Y e Z.
- Identificação da mão esquerda.
- Identificação da mão direita.
- Sequências de até 120 frames.
- Taxa de captura configurável entre 1 e 60 FPS.

Essa estrutura permitirá transmitir informações sobre os movimentos das mãos sem precisar enviar continuamente imagens completas ao backend.

## 2.8. Criação do serviço de reconhecimento

Foi criado:

`app/services/recognition.py`

Esse serviço recebe os landmarks, valida a sequência e contabiliza:

- Quantidade de frames recebidos.
- Frames com mão esquerda identificada.
- Frames com mão direita identificada.
- Taxa de captura utilizada.

O serviço também retorna o estado:

`model_not_trained`

Isso significa que a infraestrutura de recebimento está preparada, mas o classificador ainda não foi treinado.

**Importante:** o HAVEN ainda não reconhece sinais reais por meio dessa rota. Nenhuma tradução é inventada enquanto não houver um modelo confiável.

# 3. Situação atual do projeto

| Componente | Situação |
|---|---|
| Ambiente Python 3.13 | Configurado |
| Dependências | Instaladas |
| FastAPI | Inicializado |
| Arquivo main.py | Criado |
| Configuração CORS | Implementada |
| Integração Supabase | Estrutura existente |
| Autenticação | Rotas existentes |
| Histórico de traduções | Rotas existentes |
| Recebimento de landmarks | Estruturado |
| Validação dos pontos das mãos | Implementada |
| Modelo de reconhecimento | Pendente |
| Reconhecimento real de Libras | Pendente |
| Integração da câmera com a API | Pendente |

**Último teste realizado:** a rota principal respondeu corretamente em `http://127.0.0.1:8000`.

# 4. Futuras atualizações

As próximas atualizações serão divididas em etapas para garantir que o reconhecimento funcione corretamente.

## ETAPA 1 — Integração da câmera com o frontend

**Prioridade: alta**

Implementar a comunicação entre a câmera do navegador e o backend.

Funcionalidades:

- Solicitação de permissão para acessar a câmera.
- Inicialização e encerramento da captura.
- Identificação das mãos em tempo real.
- Extração dos 21 pontos de cada mão.
- Envio dos landmarks para a API.
- Exibição do estado da captura na interface.

Tecnologia prevista: MediaPipe no frontend.

## ETAPA 2 — Reconhecimento do alfabeto manual

**Prioridade: alta**

Desenvolver o primeiro modelo de inteligência artificial do HAVEN.

O objetivo será reconhecer as letras do alfabeto manual de Libras.

Funcionalidades:

- Identificação das configurações das mãos.
- Reconhecimento das letras.
- Tratamento de variações de posição e orientação.
- Reconhecimento de sinais que dependem de movimento, como J e Z.
- Exibição da letra reconhecida.
- Apresentação de uma estimativa de confiança do modelo.

Será necessário utilizar exemplos reais e devidamente identificados para treinar e avaliar o modelo.

## ETAPA 3 — Reconhecimento de sinais isolados

**Prioridade: alta**

Depois do alfabeto, será desenvolvido um vocabulário inicial de sinais.

Exemplos de categorias:

- Cumprimentos.
- Expressões cotidianas.
- Perguntas.
- Sentimentos.
- Necessidades básicas.
- Comunicação em ambientes escolares.

O modelo deverá considerar movimentos, orientação das mãos e informações corporais relevantes, não apenas posições estáticas dos dedos.

## ETAPA 4 — Formação de palavras e frases

**Prioridade: alta**

Evoluir do reconhecimento de sinais individuais para sequências contínuas.

Funcionalidades planejadas:

- Identificação de sequências de sinais.
- Reconhecimento de movimentos ao longo do tempo.
- Formação de mensagens.
- Organização dos sinais reconhecidos em texto.
- Tratamento de pausas e trans

**Documento de referência do projeto HAVEN — TCC.**

Este documento representa o planejamento técnico e funcional inicial. As tecnologias, funcionalidades e estruturas descritas deverão ser ajustadas conforme a implementação, os testes e a validação do projeto.
