# Base Image
FROM spark-base:latest
LABEL maintainer="MarcLamberti"

# Arguments that can be set with docker build
ARG AIRFLOW_VERSION=1.10.10
ARG AIRFLOW_HOME=/usr/local/airflow

# Export the environment variable AIRFLOW_HOME where airflow will be installed
ENV AIRFLOW_HOME=${AIRFLOW_HOME}

# Install dependencies and tools
RUN apt-get update -y && \
    apt-get upgrade -yqq && \
    apt-get install -yqq --no-install-recommends \
    python3-dev \
    wget \
    libczmq-dev \
    curl \
    libssl-dev \
    git \
    inetutils-telnet \
    bind9utils freetds-dev \
    libkrb5-dev \
    libsasl2-dev \
    libffi-dev libpq-dev \
    freetds-bin build-essential \
    default-libmysqlclient-dev \
    apt-utils \
    rsync \
    zip \
    unzip \
    gcc \
    vim \
    netcat-openbsd && \
    apt-get autoremove -yqq --purge && apt-get clean

COPY ./requirements-python3.7.txt /requirements-python3.7.txt

# Instala dependências de compilação do Python
RUN apt-get install -yqq --no-install-recommends \
    make \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    liblzma-dev

# Instala Python 3.7 via pyenv (a versão que este projeto realmente espera)
ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="${PYENV_ROOT}/bin:${PYENV_ROOT}/shims:${PATH}"
RUN curl https://pyenv.run | bash && \
    pyenv install 3.7.17 && \
    pyenv global 3.7.17

# Upgrade pip
# Create airflow user 
# Install apache airflow with subpackages
RUN pip install --upgrade pip && \
    pip install "setuptools<58" wheel && \
    useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow && \
    pip install --no-build-isolation -c /requirements-python3.7.txt apache-airflow[crypto,celery,postgres,hive,jdbc,mysql,ssh,docker,hdfs,redis,slack,webhdfs]==${AIRFLOW_VERSION}

    # Copy the airflow.cfg file (config)
#COPY ./config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg

# Set the owner of the files in AIRFLOW_HOME to the user airflow
RUN chown -R airflow: ${AIRFLOW_HOME}

# /root is 700 by default, which would hide the pyenv-installed airflow
# binary from the non-root airflow user even though it's on PATH
RUN chmod o+x /root && chmod -R o+rX /root/.pyenv

# Copy the entrypoint.sh from host to container (at path AIRFLOW_HOME)
COPY ./start-airflow.sh ./start-airflow.sh

# Set the entrypoint.sh file to be executable
RUN chmod +x ./start-airflow.sh

# Set the username to use
USER airflow

# Create the folder dags inside $AIRFLOW_HOME
RUN mkdir -p ${AIRFLOW_HOME}/dags

# Expose ports (just to indicate that this container needs to map port)
EXPOSE 8080

# Execute start-airflow.sh
CMD [ "./start-airflow.sh" ]

    