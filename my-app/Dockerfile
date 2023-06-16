# STAGE 1

FROM node:12-alpine AS build
WORKDIR /app
ADD /my-app/package.json ./package.json
RUN npm install
COPY ./my-app/ /app/
RUN npm run build

# STAGE 2

FROM nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]