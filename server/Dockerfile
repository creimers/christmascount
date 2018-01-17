FROM node:9

ADD . /project
WORKDIR /project

RUN npm install
RUN npm install --global nodemon

CMD ['node', 'index.js']
