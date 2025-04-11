
# 🤖 Bot de Coleta de Preços de Faculdades - Educa Mais Brasil

Este projeto é um bot de automação desenvolvido em Python com Selenium que acessa o site **[Educa Mais Brasil](https://www.educamaisbrasil.com.br/)**, realiza uma busca por cursos, e extrai automaticamente as seguintes informações para cada faculdade listada:

<<<<<<< HEAD
- 🏫 Nome da faculdade (extraído do atributo ALT da logomarca)
=======
- 🏫 Nome da faculdade (extraído por OCR da logomarca)
>>>>>>> df1dcd4 (Update main.py)
- 💰 Valor da mensalidade
- 📘 Tipo do curso (Ex: Bacharelado, Licenciatura)
- 🏫 Modalidade (Presencial, EAD, etc.)
- 🎓 Nome do curso (Ex: Direito, Administração)

As informações são salvas em uma planilha Excel (`.xlsx`), formatada automaticamente para melhor visualização.

---

## 🧪 Tecnologias utilizadas

- Python 🐍
- Selenium 💻
<<<<<<< HEAD
=======
- pytesseract + OCR 🔍
>>>>>>> df1dcd4 (Update main.py)
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

<<<<<<< HEAD
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

=======
4. **Certifique-se de ter o Tesseract OCR instalado**:
Baixe aqui: https://github.com/tesseract-ocr/tesseract  
E adicione o caminho do executável no seu script, exemplo:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

5. **Execute o bot**:
```bash
python bot_faculdades.py
```

A planilha `faculdades_educamais.xlsx` será gerada automaticamente na raiz do projeto.

---

## 📌 Observações

- O bot foi projetado para lidar com a estrutura dinâmica do site.
- As logomarcas das faculdades são processadas com OCR para identificar o nome da instituição, pois não são exibidas como texto.
- O arquivo `.xlsx` é recriado a cada execução.
- A automação ainda pode ser adaptada para navegar por múltiplas páginas e refinar os filtros de busca.

---

## 🧑‍💻 Autor

>>>>>>> df1dcd4 (Update main.py)
Desenvolvido por **Narcisio Torquato**, desenvolvedor RPA Júnior.  
Contatos: [LinkedIn](https://www.linkedin.com/in/seu-perfil) | [GitHub](https://github.com/seu-usuario)
