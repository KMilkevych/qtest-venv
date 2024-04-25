FROM python:3.12.2-bookworm

# Install system packages
RUN apt-get -qq update
RUN apt-get -qq -y install git g++ cmake wget gpg software-properties-common
RUN curl https://pyenv.run | bash

ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"

# Install Python packages
RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN pip install setuptools

RUN pyenv install 3.8

WORKDIR /app
COPY . .

RUN cd OLSQ2 && pyenv local 3.8 && poetry env use 3.8 && poetry install
RUN cd Q-Synth && poetry install
RUN cd qt && poetry install
RUN poetry install

ENTRYPOINT ["/bin/bash"]
