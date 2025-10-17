# notifications-manager


# run

docker:
```
docker compose up --build -d
```
or

manual:
```
uvicorn src/app/main:app --host 0.0.0.0 --port 8000
```


# test

```
curl -X POST http://localhost:8000/notify -H 'Content-Type: application/json' -d '{"text":"Test notification ✅"}'
or
curl -X POST http://<your-vps-ip>:8000/notify -H 'Content-Type: application/json' -d '{"text":"Hello from Docker FastAPI! 🚀"}'
or
curl -X POST localhost:8000/notify \
     -H "Content-Type: application/json" \
     -d '{"text":"Build finished successfully 🎉"}'

```



# my learning setup path:

install telegram app 
message @BotFather /newbot
name bot and then copy bot token somewhere save and in the .env
write a few messages then send curl and redo this cycle till you see a json with id which is your TELEGRAM_CHAT_ID to put in .env
curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates

