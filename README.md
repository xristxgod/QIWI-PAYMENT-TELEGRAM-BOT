QIWI PAYMENT BOT
======
> Bot for accepting payments with QIWI

Run bot:
``` shell
# <<<====================>>> CMD <<<=======================>>>

# Run the bot with a token from the .env file.
python3 ./main.py
# Run the bot with the token indication via the console.
python3 ./main.py --tokenTG yourBotToken
python3 ./main.py -tt yourBotToken
# Run the bot with the qiwi token
python3 ./main.py --tokenQIWI yourQIWIToken
python3 ./main.py -tq yourQIWIToken

# <<<====================>>> Docker <<<====================>>>

# Run by docker
docker-compose --file ./bot-docker-compose.yml up --build
# Stop docker
docker-compose --file ./bot-docker-compose.yml stop

# <<<====================>>> Bush <<<====================>>>

# Run by bush
bush ./run.sh
# Stop bush
bush ./stop.sh
```