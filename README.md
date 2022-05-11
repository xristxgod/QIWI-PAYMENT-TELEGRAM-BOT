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

> Chapter 1
> ![page1](https://user-images.githubusercontent.com/84931791/167825363-a91d504e-a5ed-48cc-821e-d371e778c3d1.png)

> Chapter 2
> ![page2](https://user-images.githubusercontent.com/84931791/167825417-924cbdb1-e943-445f-a60d-abfbd14cd03e.png)

> Chapter 3
> ![page3](https://user-images.githubusercontent.com/84931791/167825465-3d750003-ded6-4680-999b-33572c4151e9.png)

> Chapter 4
> ![page4](https://user-images.githubusercontent.com/84931791/167825515-b56cced9-6576-4cb6-a1b8-5964751779c2.png)
