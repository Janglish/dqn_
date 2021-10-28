FROM continuumio/anaconda3

RUN pip install --upgrade pip && \
    pip install autopep8 && \
    pip install stable-baselines3[extra] && \
    pip install gym[accept-rom-license] && \
    pip install gym[atari]

WORKDIR /workdir

EXPOSE 8888

ENTRYPOINT ["jupyter-lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]

CMD ["--notebook-dir=/workdir"]