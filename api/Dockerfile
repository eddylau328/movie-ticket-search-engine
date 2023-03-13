FROM node:16-alpine

RUN apk add --no-cache grpc

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json ./
COPY yarn.lock ./

RUN yarn 

# Bundle app source
COPY . .

EXPOSE 8080

CMD [ "yarn", "start" ]