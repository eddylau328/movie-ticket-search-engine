FROM node:16-alpine 

WORKDIR /usr/src/app
# Copy app files

COPY . .

RUN yarn

ENV NODE_ENV production

EXPOSE 3000

CMD [ "npx", "serve", "build" ]