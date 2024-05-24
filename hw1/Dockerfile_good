FROM jupyterhub/jupyterhub:3.1.1

RUN apt-get update && apt-get install -y python3-pip

RUN useradd -m -s /bin/bash jupyteruser

WORKDIR /jupyterhub
RUN chown jupyteruser:jupyteruser -R /jupyterhub/

COPY requirements.txt /jupyterhub/

RUN pip3 install --no-cache-dir -r requirements.txt

USER jupyteruser
EXPOSE 8000

CMD ["jupyterhub"]