# 🎭 Playwright Course — Page Object Model (POM)

Projeto de automação de testes end-to-end desenvolvido com **Playwright** e **pytest**, utilizando o padrão de design **Page Object Model (POM)**. Os testes cobrem funcionalidades de um banco simulado ([SimulaBank](https://leogcarvalho.github.io/simulabank/login.html)), incluindo login, Pix e empréstimos.

---

## 🗂️ Estrutura do Projeto

```
playwright-course-pom/
│
├── .github/
│   └── workflows/
│       └── playwright.yml        # Pipeline de CI com GitHub Actions
│
├── pages/                        # Page Objects (POM)
│   ├── common_page.py            # Ações comuns a todas as páginas
│   ├── emprestimos_page.py       # Página de empréstimos
│   ├── home_page.py              # Página inicial (dashboard)
│   ├── login_page.py             # Página de login
│   └── pix_page.py               # Página de Pix
│
├── tests/                        # Casos de teste
│   ├── test_001_login_successful.py
│   ├── test_002_fazer_pix.py
│   ├── test_003_contratar_emprestimo_2000.py
│   ├── test_004_verificar_emprestimo_contrata...py
│   └── test_005_verificar_pix_acima_limite.py
│
├── conftest.py                   # Fixtures globais do pytest
├── requirements.txt              # Dependências do projeto
└── .gitignore
```

---

## 🧪 Casos de Teste

| Arquivo | Descrição |
|---|---|
| `test_001_login_successful.py` | Valida o login com credenciais válidas |
| `test_002_fazer_pix.py` | Realiza uma transferência via Pix |
| `test_003_contratar_emprestimo_2000.py` | Contrata um empréstimo de R$ 2.000 |
| `test_004_verificar_emprestimo_contrata...py` | Verifica se o empréstimo contratado aparece no extrato |
| `test_005_verificar_pix_acima_limite.py` | Valida o comportamento ao tentar Pix acima do limite |

---

## ⚙️ Pré-requisitos

- Python 3.8+
- pip

---

## 🚀 Instalação

**1. Clone o repositório:**

```bash
git clone https://github.com/Mileeski/playwright-course-pom.git
cd playwright-course-pom
```

**2. Crie e ative um ambiente virtual:**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Instale os browsers do Playwright:**

```bash
playwright install
```

---

## ▶️ Executando os Testes

**Rodar todos os testes:**

```bash
pytest tests/
```

**Rodar um teste específico:**

```bash
pytest tests/test_001_login_successful.py
```

**Rodar em modo headed (com janela do browser visível):**

```bash
pytest tests/ --headed
```

**Rodar com relatório detalhado:**

```bash
pytest tests/ -v
```

---

## 🏗️ Padrão Page Object Model (POM)

O projeto segue o padrão **POM**, onde cada página da aplicação possui uma classe dedicada em `pages/`. Isso garante:

- **Reutilização** — os seletores e ações ficam centralizados em um único lugar.
- **Manutenibilidade** — mudanças na UI exigem alteração em apenas um arquivo.
- **Legibilidade** — os testes descrevem *o quê* está sendo testado, não *como* interagir com a UI.

**Exemplo de fixture no `conftest.py`:**

```python
@pytest.fixture
def page(page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://leogcarvalho.github.io/simulabank/login.html")
    return page
```

---

## 🤖 CI/CD com GitHub Actions

O projeto conta com um workflow em `.github/workflows/playwright.yml` que executa os testes automaticamente a cada push ou pull request, garantindo a integridade do código continuamente.

---

## 📦 Principais Dependências

| Pacote | Versão | Finalidade |
|---|---|---|
| `playwright` | 1.60.0 | Automação de browser |
| `pytest` | 9.1.1 | Framework de testes |
| `pytest-playwright` | 0.8.0 | Integração Playwright + pytest |
| `pytest-base-url` | 2.1.0 | Configuração de URL base |

---

## 🌐 Aplicação Alvo

Os testes são executados sobre o **SimulaBank**, um banco fictício criado para fins educacionais:

🔗 [https://leogcarvalho.github.io/simulabank/login.html](https://leogcarvalho.github.io/simulabank/login.html)

---

## 📝 Licença

Este projeto é de uso educacional, desenvolvido como parte de um curso de automação de testes com Playwright.
