FROM python:3.8 AS builder

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
&& pip install --user --no-cache-dir -r requirements.txt

FROM python:3.8-slim

ENV PYTHONUNBUFFERED    1
ENV PYTHONPATH          /var/bot/mask/
ENV PATH                /root/.local:$PATH

COPY --from=builder /root/.local/ /root/.local/

WORKDIR /var/mask/

COPY . .

# EXPOSE 127.0.0.1:80:80

CMD ["python","-m", "main.py"]
# CMD ["bash"]