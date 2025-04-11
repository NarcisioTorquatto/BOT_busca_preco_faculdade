
# 🤖 Bot de Coleta de Preços de Faculdades - Educa Mais Brasil

Este projeto é um bot de automação desenvolvido em Python com Selenium que acessa o site **[Educa Mais Brasil](https://www.educamaisbrasil.com.br/)**, realiza uma busca por cursos, e extrai automaticamente as seguintes informações para cada faculdade listada:

- 🏫 Nome da faculdade (extraído do atributo ALT da logomarca)
- 💰 Valor da mensalidade
- 📘 Tipo do curso (Ex: Bacharelado, Licenciatura)
- 🏫 Modalidade (Presencial, EAD, etc.)
- 🎓 Nome do curso (Ex: Direito, Administração)

As informações são salvas em uma planilha Excel (`.xlsx`), formatada automaticamente para melhor visualização.

---

## 🧪 Tecnologias utilizadas

- Python 🐍
- Selenium 💻
- pandas 📊
- openpyxl 📘

---

## ⚙️ Como executar

1. **Clone o repositório**:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. **Crie e ative o ambiente virtual (opcional, mas recomendado)**:
```bash
python -m venv venv
venv\Scripts\activate  # no Windows
```

3. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

4. **Execute o bot**:
```bash
python bot_faculdades.py
```

A planilha `faculdades_educamais.xlsx` será gerada automaticamente na raiz do projeto.

---

## 📌 Observações

- O bot foi projetado para lidar com a estrutura dinâmica do site.
- O nome da faculdade é obtido diretamente do atributo `alt` da imagem da logomarca.
- O arquivo `.xlsx` é recriado a cada execução.
- A automação pode ser adaptada para navegar por múltiplas páginas e refinar os filtros de busca.

---

## 🧑‍💻 Autor

Desenvolvido por **Narcisio Torquato**, desenvolvedor RPA Júnior.  
Contatos: [LinkedIn](www.linkedin.com/in/narcisiotorquato) | [GitHub](https://github.com/NarcisioTorquatto)
