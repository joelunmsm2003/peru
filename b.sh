
curl --header 'Access-Token: o.CkwgbghQdKuxqT5bxubgavgiCYMFhbeN' \
     --header 'Content-Type: application/json' \
     --data-binary '{"body":"'" $body"'","title":"'"$title"'","type":"note"}' \
     --request POST \
     https://api.pushbullet.com/v2/pushes


curl --header 'Access-Token: o.CkwgbghQdKuxqT5bxubgavgiCYMFhbeN' \
     --header 'Content-Type: application/json' \
     --data-binary '{"body":"'" $body"'","title":"'"$title"'","type":"note","email":"mayra.tananta.1@gmail.com"}' \
     --request POST \
     https://api.pushbullet.com/v2/pushes
