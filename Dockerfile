# Dockerfile

# 1. Use uma imagem base oficial do Python.
# A versão 'slim' é menor e ideal para produção.
FROM python:3.9-slim

# 2. Defina o diretório de trabalho dentro do container.
WORKDIR /app

# 3. Copie o arquivo de dependências primeiro.
# Isso aproveita o cache do Docker. Se o requirements.txt não mudar,
# o Docker não reinstalará as dependências em builds futuros.
COPY requirements.txt requirements.txt

# 4. Instale as dependências.
# --no-cache-dir cria uma imagem menor.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copie o resto do código da sua aplicação para o diretório de trabalho.
COPY . .

# 6. Exponha a porta em que o Gunicorn rodará.
# Pode ser 5000, 8000, ou qualquer outra.
EXPOSE 5000

# 7. Defina o comando para iniciar a aplicação com Gunicorn.
# Este comando será executado quando o container iniciar.
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]