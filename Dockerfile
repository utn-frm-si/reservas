FROM python:3.4

# Configura el modo no interactivo.
ENV DEBIAN_FRONTEND noninteractive

# Crea el directorio '/code' y lo establece como directorio de trabajo.
RUN mkdir /code
WORKDIR /code

# Añade el contenido del repositorio al directorio '/code'.
ADD . /code/

# Instala las dependencias del proyecto, mediante pip.
RUN pip install -r requirements.txt

# Instala NodeJS.
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get install -y nodejs

# Instala Bower.
RUN npm install -g bower
