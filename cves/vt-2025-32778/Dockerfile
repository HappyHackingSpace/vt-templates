FROM node:18-alpine

RUN apk add --no-cache chromium git curl

WORKDIR /app

RUN git clone https://github.com/Lissy93/web-check.git . && \
    git checkout 0e4958aa10b2650d32439a799f6fc83a7cd46cef~1

RUN npm install --legacy-peer-deps

ENV CHROME_PATH=/usr/bin/chromium
ENV PORT=3000

EXPOSE 3000

CMD ["npm", "start"]
