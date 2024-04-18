FROM python:3.12.2-slim-bookworm

# Install system packages
RUN apt-get -qq update
RUN apt-get -qq -y install git

# Install Python packages
RUN pip install poetry
RUN poetry config virtualenvs.in-project true

WORKDIR /workspaces/qtest

# Install project dependencies
RUN patch -p1 < patch.diff
RUN cd qt
RUN poetry install
RUN cd ..
RUN cd Q-Synth
RUN poetry install
RUN cd ..
RUN cd OLSQ2
RUN poetry install
RUN cd ..
RUN poetry install

