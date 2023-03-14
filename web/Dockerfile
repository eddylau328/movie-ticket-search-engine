FROM node:16-alpine 

WORKDIR /usr/src/app
# Copy app files

COPY package.json yarn.lock ./

RUN yarn

COPY . .
RUN yarn build

ENV NODE_ENV production

EXPOSE 3000

CMD [ "npx", "serve", "build" ]