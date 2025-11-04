# 🧱 API de Gerenciamento de Tasks

Projeto simples em **Flask** para gerenciamento de tarefas (CRUD completo).

---

## 📁 Estrutura do Projeto

```
CRUD_TASKS_API/
├── models/
│   └── task.py
├── app.py
├── requirements.txt
└── readme.md
```

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPO.git
cd CRUD_TASKS_API
```

### 2️⃣ Criar ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

Ativar o ambiente:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o servidor

```bash
python app.py
```

O servidor Flask iniciará em:

```
http://127.0.0.1:5000
```

---

## 🧩 Endpoints

### ➕ Criar Task

**POST** `/tasks`

**Body (JSON):**

```json
{
  "title": "string",
  "description": "string"
}
```

---

### 📋 Listar Todas as Tasks

**GET** `/tasks`

---

### 🔍 Buscar Task por ID

**GET** `/tasks/<task_id>`

---

### ✏️ Atualizar parcialmente uma Task

**PATCH** `/tasks/<task_id>`

**Body (JSON):**

```json
{
  "description": "string"
}
```

---

### ♻️ Donar uma Task

**PUT** `/tasks/<task_id>`

---

### ❌ Deletar uma Task

**DELETE** `/tasks/<task_id>`

---

## 📦 Dependências

Arquivo `requirements.txt` deve conter:

```
Flask==2.3.0
Flask-SQLAlchemy==3.1.1
Flask-Cors==3.0.10
Werkzeug==2.3.0
requests==2.31.0
pytest==7.4.3

```

_(ou a versão que você estiver utilizando)_

---

## 🧑‍💻 Autor

Desenvolvido por **Vitor Nascimento**

---

## 🪶 Licença

Este projeto é de uso livre para fins de estudo e aprendizado.
