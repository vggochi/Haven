# 💙 HAVEN
### *Every voice deserves to be understood.*

<p align="center">

**🌐 Plataforma Inteligente de Comunicação e Acessibilidade em Libras**

</p>

<p align="center">

♿ Inclusão • 🤟 Libras • 🧠 Inteligência Artificial • 💬 Comunicação

</p>

---

# 📖 1. Sobre o projeto

O **HAVEN** é uma plataforma tecnológica voltada à acessibilidade e à comunicação entre pessoas surdas, pessoas com deficiência auditiva e pessoas ouvintes que não dominam a Língua Brasileira de Sinais (Libras).

A proposta é desenvolver um ambiente digital que utilize tecnologias de reconhecimento visual, inteligência artificial e processamento de informações para facilitar a comunicação em diferentes situações do cotidiano.

O sistema pretende oferecer ferramentas de tradução, consulta de sinais, aprendizagem de Libras e acompanhamento das atividades dos usuários.

🎯 **O HAVEN busca reduzir barreiras de comunicação em ambientes como:**

- 🏥 Hospitais e unidades de saúde.
- 🏫 Escolas e instituições de ensino.
- 🛍️ Estabelecimentos comerciais.
- 🏛️ Órgãos públicos.
- 💼 Ambientes profissionais.
- 🌎 Situações cotidianas.

## 🔎 1.1. Problema identificado

A comunicação entre pessoas surdas que utilizam Libras e pessoas ouvintes que não conhecem essa língua ainda representa uma barreira significativa.

Em muitos ambientes, a ausência de pessoas capacitadas em Libras dificulta o atendimento, a compreensão de informações e a participação social.

Embora existam dicionários digitais e ferramentas de aprendizagem, ainda existe espaço para desenvolver soluções que integrem consulta de sinais, reconhecimento visual, tradução e aprendizagem em uma única plataforma.

## 💡 1.2. Solução proposta

O HAVEN pretende reunir recursos de acessibilidade em uma plataforma integrada, permitindo:

- 🤟 Reconhecer sinais de Libras por meio de uma câmera, dentro de um vocabulário e escopo de reconhecimento definidos.
- 📝 Converter textos em representações visuais de sinais.
- 📚 Consultar um dicionário digital de Libras.
- 🎓 Aprender novos sinais por meio de módulos e exercícios.
- 🕘 Armazenar o histórico de traduções.
- ⭐ Salvar sinais favoritos.
- 📈 Acompanhar o progresso de aprendizagem.

## 🎯 1.3. Objetivo geral

Desenvolver uma plataforma inteligente de acessibilidade que utilize recursos tecnológicos para facilitar a comunicação em Libras e ampliar o acesso à informação e à aprendizagem.

## 📌 1.4. Objetivos específicos

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

# 🎨 2. Identidade do projeto

| Característica | Definição |
|---|---|
| 💙 Nome | HAVEN |
| ✨ Slogan | Every voice deserves to be understood. |
| 🧩 Categoria | Tecnologia, acessibilidade, saúde e qualidade de vida |
| 🤝 Conceito | Comunicação, inclusão, autonomia e acessibilidade |

## 🖌️ 2.1. Identidade visual

A identidade visual busca transmitir confiança, modernidade, simplicidade e acessibilidade.

**Paleta de cores:**

| Cor | Código | Aplicação |
|---|---|---|
| 🌌 Midnight | `#101C35` | Fundo principal e elementos institucionais |
| 🔵 Electric Blue | `#246BFD` | Botões e destaques |
| 🧊 Ice | `#EAF2FF` | Fundos secundários |
| ⚪ White | `#FFFFFF` | Textos e superfícies |

**Tipografia sugerida:**

- Sora — títulos.
- Inter — textos e conteúdo.
- Manrope — indicadores e números.

---

# 👥 3. Público-alvo

O HAVEN é destinado principalmente a:

1. Pessoas surdas que utilizam Libras.
2. Pessoas com deficiência auditiva.
3. Pessoas ouvintes que desejam aprender Libras.
4. Profissionais de atendimento.
5. Instituições de ensino.
6. Estabelecimentos de saúde.
7. Organizações que desejam melhorar sua acessibilidade.

A experiência deverá considerar diferentes níveis de familiaridade com tecnologia.

---

# 🚀 4. Funcionalidades principais

## 🔐 4.1. Cadastro e autenticação

O usuário poderá:

- Criar uma conta.
- Realizar login.
- Encerrar a sessão.
- Editar seu perfil.
- Alterar sua foto.
- Definir seu nível de conhecimento em Libras.
- Configurar preferências da plataforma.

**Tecnologia:** Supabase Auth.

## 🤟 4.2. Tradutor: Libras para Português

Essa funcionalidade permitirá utilizar a câmera para capturar movimentos das mãos e reconhecer sinais dentro do vocabulário suportado pelo modelo.

**Fluxo esperado:**

1. O usuário acessa o tradutor.
2. Autoriza o acesso à câmera.
3. O sistema captura os movimentos.
4. O modelo identifica os sinais suportados.
5. O resultado é apresentado em português.
6. O usuário poderá ouvir o resultado por síntese de voz.
7. A tradução poderá ser salva no histórico.

**Recursos previstos:**

- 📷 Captura pela câmera.
- ✋ Detecção de mãos.
- 🧠 Identificação de sinais.
- 💬 Apresentação do resultado.
- 📊 Indicador de reconhecimento, quando disponível.
- 🔊 Reprodução de texto em áudio.
- 🔄 Repetição da captura.
- 📝 Feedback e correção.

> ⚠️ **Importante:** Libras é uma língua natural com gramática própria. Reconhecer posições das mãos isoladamente não equivale a traduzir Libras. O projeto deverá considerar movimento, contexto, expressões faciais e outros elementos linguísticos. O primeiro protótipo trabalhará com um vocabulário controlado e validado por pessoas fluentes em Libras.

## ✍️ 4.3. Tradutor: Português para Libras

Essa funcionalidade permitirá inserir uma frase ou palavra em português e visualizar sua representação em Libras.

**Fluxo esperado:**

1. O usuário digita um texto.
2. O sistema processa a entrada.
3. O sistema identifica os sinais disponíveis.
4. Apresenta os sinais por meio de vídeos, animações ou representações visuais.
5. O usuário acompanha a sequência.

**Recursos previstos:**

- Campo de texto.
- Processamento da frase.
- Consulta ao dicionário.
- Apresentação dos sinais.
- Reprodução das demonstrações.
- Possibilidade de repetir a sequência.

A representação deverá respeitar a estrutura linguística da Libras, e não simplesmente substituir cada palavra do português por um gesto.

## 📚 4.4. Dicionário de Libras

O dicionário será uma das principais áreas do HAVEN.

A proposta é disponibilizar uma biblioteca organizada de sinais, com informações sobre significado, categorias, exemplos e demonstrações visuais.

**Recursos:**

- 🔎 Busca por palavra.
- 🗂️ Busca por categoria.
- 🔤 Busca alfabética.
- ✋ Busca por configuração de mão.
- 📖 Consulta de significados.
- 💬 Exemplos de utilização.
- 📝 Classe gramatical.
- 🎥 Vídeos demonstrativos.
- 🌎 Variações regionais.
- ⭐ Sinais favoritos.

### 🔗 Referências externas

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

> ⚖️ **Direitos de uso:** não copiar automaticamente vídeos, imagens ou descrições dos sites. É necessário verificar as licenças, permissões e condições de utilização. Sempre que possível, utilizar conteúdo próprio ou autorizado.

## 🎓 4.5. Aprendizagem de Libras

O módulo de aprendizagem permitirá que usuários estudem Libras de forma organizada.

**Recursos:**

- Módulos de aprendizagem.
- Lições.
- Vídeos explicativos.
- Exercícios.
- Questões de múltipla escolha.
- Atividades de identificação.
- Pontuação.
- Acompanhamento do progresso.
- Histórico de resultados.

**Exemplo de organização:**

| Módulo | Conteúdo |
|---|---|
| 01 | Introdução à Libras |
| 02 | Alfabeto manual |
| 03 | Números |
| 04 | Cumprimentos |
| 05 | Família |
| 06 | Saúde |
| 07 | Educação |
| 08 | Situações cotidianas |

## 🕘 4.6. Histórico de traduções

O usuário poderá consultar suas traduções anteriores.

Informações armazenadas:

- Tipo de tradução.
- Conteúdo original.
- Resultado.
- Data e horário.
- Duração do processamento.
- Status.

## ⭐ 4.7. Favoritos

Permite salvar sinais para consulta posterior.

Cada usuário terá sua própria lista de favoritos.

## 💬 4.8. Feedback das traduções

O usuário poderá:

- Avaliar uma tradução.
- Informar se o resultado foi adequado.
- Sugerir uma correção.
- Enviar comentários.

Esses dados poderão auxiliar na avaliação e melhoria do sistema.

---

# 🛠️ 5. Tecnologias utilizadas e previstas

A arquitetura tecnológica inicial será composta pelas seguintes ferramentas:

| Tecnologia | Utilização |
|---|---|
| ⚛️ React | Desenvolvimento da interface |
| JavaScript | Lógica da aplicação |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização |
| Supabase | Backend e banco de dados |
| PostgreSQL | Banco de dados relacional |
| Supabase Auth | Cadastro e autenticação |
| Supabase Storage | Armazenamento de arquivos |
| 🐍 Python | Desenvolvimento do reconhecimento visual |
| OpenCV | Processamento de imagens |
| MediaPipe | Detecção e rastreamento das mãos |
| TensorFlow ou PyTorch | Treinamento e execução de modelos de aprendizado de máquina |

A biblioteca de machine learning ainda deverá ser escolhida conforme os testes e a arquitetura do modelo.

## 🏗️ 5.1. Arquitetura geral

O projeto terá três componentes principais:

**Frontend — React**

Responsável pela interface, navegação, formulários, câmera, exibição de resultados e comunicação com o Supabase e o serviço de reconhecimento.

**Backend e banco de dados — Supabase**

Responsável por autenticação, persistência dos dados, relacionamentos, armazenamento e segurança.

**Reconhecimento visual — Python**

Responsável pelo processamento de imagens, detecção das mãos e reconhecimento dos sinais suportados.

**Fluxo geral:**

```text
          👤 USUÁRIO
               |
               v
        ⚛️ FRONTEND REACT
               |
       +-------+-------+
       |               |
       v               v
  🐍 SERVIÇO       💙 SUPABASE
 RECONHECIMENTO    AUTH + DATABASE
       |
       v
  🧠 MODELO DE IA
       |
       v
  💬 RESULTADO
       |
       v
  📱 INTERFACE HAVEN
```

O frontend também poderá consultar diretamente o Supabase utilizando a chave pública apropriada e políticas RLS.

---

# 🗄️ 6. Banco de dados — Supabase

O banco de dados utilizará PostgreSQL por meio do Supabase.

A estrutura foi planejada para separar dicionário, usuários, traduções, aprendizagem e funcionalidades complementares.

## 📂 6.1. Tabelas planejadas

### 📚 Módulo 1 — Dicionário

| Tabela | Responsabilidade |
|---|---|
| `categorias_sinais` | Categorias e assuntos do dicionário |
| `sinais` | Cadastro dos sinais e palavras |
| `variantes_sinais` | Variações regionais e linguísticas |
| `videos_sinais` | Vídeos demonstrativos |

### 👤 Módulo 2 — Usuários e traduções

| Tabela | Responsabilidade |
|---|---|
| `perfis` | Informações complementares dos usuários |
| `traducoes` | Histórico de traduções |
| `itens_traducao` | Palavras e sinais individuais de cada tradução |
| `favoritos` | Sinais salvos pelos usuários |
| `feedback_traducoes` | Avaliações e correções |

### 🎓 Módulo 3 — Aprendizagem

| Tabela | Responsabilidade |
|---|---|
| `modulos_aprendizado` | Organização dos módulos |
| `licoes` | Conteúdos de cada módulo |
| `exercicios` | Atividades e perguntas |
| `resultados_exercicios` | Respostas e pontuações |
| `progresso_aprendizado` | Progresso individual |

### ⚙️ Módulo 4 — Sistema

| Tabela | Responsabilidade |
|---|---|
| `notificacoes` | Avisos e atualizações |
| `historico_acessos` | Registro de atividades relevantes |

<sub>📊 Total planejado: 16 tabelas.</sub>

## 🧩 6.2. Ajustes previstos no módulo do dicionário

O modelo inicial deverá ser refinado para representar corretamente a estrutura dos dicionários de Libras.

Recomendações:

- Uma palavra pode ter mais de um significado.
- Um sinal pode pertencer a várias categorias.
- Um sinal pode possuir diferentes vídeos.
- Um sinal pode apresentar variantes regionais.
- Uma configuração de mão pode ser utilizada em diferentes sinais.
- Vídeos e imagens devem ser armazenados no Supabase Storage, e suas referências ficam no PostgreSQL.

**Estruturas adicionais propostas:**

- `acepcoes_sinais`: diferentes significados de um sinal ou palavra.
- `sinal_categorias`: relacionamento entre sinais e múltiplas categorias.
- `configuracoes_mao`: catálogo de configurações de mão.

Essas três estruturas são propostas de evolução e ainda não fazem parte do SQL inicial de 16 tabelas.

## 🔗 6.3. Relacionamentos principais

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

## 🔐 6.4. Segurança e RLS

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

> 🔒 A chave `service_role` ou qualquer chave secreta nunca deve ser exposta no frontend.

---

# ☁️ 7. Armazenamento — Supabase Storage

O Supabase Storage será utilizado para arquivos e mídias.

**Buckets sugeridos:**

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

# 📁 8. Estrutura sugerida do projeto

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

📌 Essa é uma estrutura sugerida. Ela poderá ser adaptada à organização real dos arquivos durante o desenvolvimento.

---

# 💻 9. Requisitos para executar o projeto

## 🧰 9.1. Ferramentas necessárias

- Node.js em versão LTS compatível com as dependências escolhidas.
- npm.
- Visual Studio Code ou editor equivalente.
- Git.
- Conta no Supabase.
- Navegador atualizado.
- Python 3.11 ou versão compatível com as bibliotecas selecionadas.
- Ambiente com câmera para testar o reconhecimento visual.

## ⚛️ 9.2. Configuração do frontend

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

## 💙 9.3. Configuração do Supabase

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

## 🐍 9.4. Configuração do serviço Python

Criar um ambiente virtual:

```bash
cd backend

python -m venv venv
```

Ativar no Windows:

```powershell
venv\Scripts\activate
```

Instalar as dependências:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` deverá conter as versões efetivamente testadas das bibliotecas utilizadas, como:

- OpenCV.
- MediaPipe.
- TensorFlow ou PyTorch.
- FastAPI.

Iniciar a API com FastAPI:

```bash
uvicorn main:app --reload
```

A API deverá receber os dados de entrada, processar os sinais e retornar resultados estruturados.

---

# 🧠 10. Reconhecimento de Libras e inteligência artificial

Essa é uma das partes tecnicamente mais importantes do HAVEN.

O reconhecimento visual não deve ser tratado apenas como identificação de imagens estáticas.

A aplicação poderá utilizar:

1. 📷 Captura de vídeo.
2. ✋ Detecção de mãos.
3. 📍 Identificação de pontos de referência das mãos.
4. 📐 Extração de características espaciais.
5. ⏱️ Análise temporal dos movimentos.
6. 🧠 Classificação dos sinais suportados.
7. 💬 Conversão dos resultados para uma representação textual.

## ✋ 10.1. MediaPipe

Pode ser utilizado para detectar mãos e extrair pontos de referência.

Esses pontos poderão servir como entrada para um modelo de reconhecimento.

## 🎥 10.2. OpenCV

Pode auxiliar em:

- Captura de vídeo.
- Tratamento de imagens.
- Conversão de quadros.
- Pré-processamento.
- Integração com a câmera.

## 🤖 10.3. Modelo de reconhecimento

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

## ⚠️ 10.4. Limitações e cuidados

O HAVEN não deve afirmar que traduz qualquer conversa em Libras de maneira perfeita.

A Libras possui estrutura gramatical própria e utiliza expressões faciais, movimentos, orientação espacial e outros elementos.

Um modelo limitado a posições das mãos poderá reconhecer alguns sinais, mas não compreenderá necessariamente frases completas.

O objetivo inicial é demonstrar uma solução funcional, mensurável e tecnicamente validada.

A plataforma deve auxiliar a comunicação, sem substituir intérpretes profissionais, especialmente em situações médicas, jurídicas ou de emergência.

---

# 🖥️ 11. Interface e telas previstas

A interface deverá seguir uma identidade visual consistente, com navegação simples e foco na acessibilidade.

| Tela | Função |
|---|---|
| 🏠 Landing Page | Apresentação do HAVEN |
| 🔐 Login | Acesso à conta |
| 📝 Cadastro | Criação de conta |
| 📊 Dashboard | Painel principal |
| 🤟 Libras → Texto | Reconhecimento pela câmera |
| ✍️ Texto → Libras | Conversão e demonstração visual |
| 📚 Dicionário | Consulta de sinais |
| 🔎 Detalhes do sinal | Informações e vídeos |
| 🎓 Aprendizagem | Módulos e lições |
| 🧩 Exercícios | Atividades práticas |
| 🕘 Histórico | Traduções anteriores |
| ⭐ Favoritos | Sinais salvos |
| 👤 Perfil | Dados e preferências |
| ⚙️ Configurações | Ajustes de acessibilidade |

## 📊 11.1. Dashboard

O painel principal deverá apresentar:

- Saudação ao usuário.
- Acesso rápido aos dois tradutores.
- Acesso ao dicionário.
- Acesso à aprendizagem.
- Resumo do progresso.
- Últimas traduções.
- Sinais favoritos.

## ♿ 11.2. Acessibilidade da interface

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

# 🔒 12. Segurança e privacidade

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

📌 As gravações da câmera não deverão ser armazenadas automaticamente. O processamento deve priorizar a minimização de dados.

---

# 🗺️ 13. Etapas de desenvolvimento

O projeto deverá ser desenvolvido em etapas.

## 📝 Etapa 1 — Planejamento e documentação

- Definir requisitos.
- Finalizar identidade visual.
- Planejar arquitetura.
- Modelar o banco de dados.
- Criar protótipos no Figma.

## 🗄️ Etapa 2 — Backend e banco de dados

- Criar projeto Supabase.
- Criar tabelas.
- Configurar relacionamentos.
- Configurar RLS.
- Configurar autenticação.
- Criar buckets do Storage.
- Inserir dados iniciais.

## 🎨 Etapa 3 — Frontend

- Criar estrutura React.
- Desenvolver identidade visual.
- Criar login e cadastro.
- Implementar dashboard.
- Criar dicionário.
- Desenvolver páginas de tradução.
- Implementar aprendizagem.
- Integrar histórico e favoritos.

## 🧠 Etapa 4 — Serviço de reconhecimento

- Configurar Python.
- Integrar OpenCV.
- Integrar MediaPipe.
- Criar conjunto de dados.
- Treinar ou adaptar o modelo.
- Criar API.
- Integrar a API ao frontend.

## 🔗 Etapa 5 — Integração

- Integrar autenticação.
- Integrar dicionário.
- Integrar traduções.
- Integrar reconhecimento.
- Integrar aprendizagem.
- Integrar armazenamento.

## 🧪 Etapa 6 — Testes e validação

- Testar cadastro e login.
- Testar permissões.
- Testar RLS.
- Testar consultas do dicionário.
- Testar reconhecimento.
- Avaliar precisão.
- Testar em diferentes dispositivos.
- Validar os sinais com pessoas fluentes em Libras.
- Corrigir problemas de acessibilidade.

## 🏁 Etapa 7 — Finalização

- Preparar demonstração.
- Documentar resultados.
- Preparar apresentação do TCC.
- Apresentar limitações.
- Demonstrar funcionalidades desenvolvidas.

---

# 🧪 14. Testes necessários

O projeto deverá possuir testes funcionais e de segurança.

### 🔐 Autenticação

- Cadastro de usuário.
- Login.
- Logout.
- Recuperação de senha.
- Persistência da sessão.

### 🗄️ Banco de dados

- Inserção de sinais.
- Consulta de categorias.
- Consulta de vídeos.
- Registro de traduções.
- Consulta de favoritos.
- Registro de progresso.

### 🛡️ Segurança

- Um usuário não pode acessar traduções de outro.
- Um usuário não pode alterar o perfil de outro.
- Conteúdos não publicados não podem ser consultados publicamente.
- Usuários não podem manipular pontuações indevidamente.

### 🤟 Reconhecimento

- Testar sinais individuais.
- Testar diferentes velocidades.
- Testar iluminação.
- Testar diferentes posições.
- Medir precisão e taxa de erro.
- Verificar o comportamento quando nenhum sinal é reconhecido.

---

# 📌 15. Pontos que ainda precisam ser definidos

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

# 📈 16. Estado atual do projeto

**Status geral: estruturação e desenvolvimento inicial do backend.**

## ✅ Alterações realizadas

- [x] Ambiente Python 3.13 configurado.
- [x] Dependências do ambiente instaladas.
- [x] NumPy adicionado.
- [x] Scikit-learn adicionado.
- [x] Joblib adicionado.
- [x] Arquivo principal `main.py` criado.
- [x] Aplicação FastAPI inicializada.
- [x] Configuração CORS implementada no `main.py`.
- [x] Rota principal `/` respondendo.
- [x] Rota `/api/health` criada.
- [x] Organização inicial dos módulos definida.
- [x] Rota de recebimento de landmarks adicionada ao código de traduções.
- [x] Modelos de validação de landmarks definidos.
- [x] Serviço inicial `recognition.py` criado.

## 🟡 Em andamento ou aguardando validação

- [ ] Conferência de todas as rotas na documentação `/docs`.
- [ ] Testes de autenticação e validação de token.
- [ ] Testes do endpoint de landmarks.
- [ ] Testes de integração com Supabase.
- [ ] Integração da câmera com o frontend.
- [ ] Integração do MediaPipe.

## ⏳ Ainda não implementado

- [ ] Modelo treinado para reconhecimento do alfabeto.
- [ ] Reconhecimento real de sinais.
- [ ] Reconhecimento de sinais isolados.
- [ ] Reconhecimento de sequências e frases.
- [ ] Tradução gramaticalmente adequada entre português e Libras.
- [ ] Síntese de voz integrada.
- [ ] Validação de precisão com usuários.

> 📍 **Último teste confirmado:** a rota principal respondeu corretamente em `http://127.0.0.1:8000`, retornando a mensagem de que a API está funcionando. Isso confirma a inicialização da aplicação, mas não comprova que todos os módulos e integrações já foram testados.

### 🐍 Estrutura técnica atual do backend

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

---

# 🚀 17. Próximas atualizações

A sequência recomendada para continuar o desenvolvimento é:

| Ordem | Atualização | Prioridade |
|---|---|---|
| 01 | Conferir e testar todas as rotas da API | 🔴 Alta |
| 02 | Testar autenticação e Supabase | 🔴 Alta |
| 03 | Conectar a câmera ao frontend | 🔴 Alta |
| 04 | Integrar MediaPipe | 🔴 Alta |
| 05 | Enviar landmarks para o backend | 🔴 Alta |
| 06 | Coletar exemplos reais do alfabeto manual | 🔴 Alta |
| 07 | Treinar e avaliar o primeiro classificador | 🔴 Alta |
| 08 | Reconhecer sinais isolados | 🟠 Média |
| 09 | Desenvolver o reconhecimento de sequências | 🟠 Média |
| 10 | Aprimorar o tradutor Português → Libras | 🟠 Média |
| 11 | Integrar histórico e favoritos | 🟠 Média |
| 12 | Finalizar testes e documentação | 🔴 Alta |

### 🎯 Próximo grande marco

Conectar a câmera do frontend ao backend, utilizando MediaPipe para extrair os pontos das mãos e enviar sequências de movimentos para a API.

Depois disso, iniciar a coleta e o treinamento do primeiro modelo de reconhecimento do alfabeto manual.

---

# 💙 18. Visão final do HAVEN

O HAVEN pretende ser mais do que um dicionário digital.

A proposta é construir um ambiente integrado de comunicação e aprendizagem, combinando acessibilidade, tecnologia e inteligência artificial.

### Três pilares fundamentais

<sub>💬 COMUNICAR</sub>

Facilitar a comunicação entre pessoas surdas e ouvintes.

<sub>📚 APRENDER</sub>

Tornar o aprendizado de Libras mais acessível.

<sub>🤝 CONECTAR</sub>

Aproximar pessoas e reduzir barreiras de comunicação.

---

<p align="center">

# 💙 HAVEN

### *Every voice deserves to be understood.*

**Tecnologia para aproximar pessoas e tornar a comunicação mais acessível.**

♿ Inclusão • 🤟 Comunicação • 🧠 Inovação

</p>

---

<sub>📄 Documento de referência do projeto HAVEN — TCC. Este README representa o planejamento técnico e funcional e o estado de desenvolvimento conhecido. As tecnologias, funcionalidades e estruturas descritas deverão ser ajustadas conforme a implementação, os testes e a validação do projeto.</sub>
