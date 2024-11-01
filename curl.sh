curl 'https://highseas.hackclub.com/shop' \
  -H 'content-type: text/plain;charset=UTF-8' \
  -H "cookie: ${HS_SESSION_TOKEN}" \
  -H 'next-action: 24c833d8076ace77d8754d64382e8f126f9b3564' \
  -H 'origin: https://highseas.hackclub.com' \
  --data-raw '[]' \
  -o input.txt