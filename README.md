# rasa
abre recurso do windows
subsistema do windows para linux
reinicia

instala o ubuntu na microsoft store

```
curl https://raw.githubusercontent.com/rslgp/rasa/main/sources.list > /etc/apt/sources.list
```

```
sudo apt-get update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9
```

```
sudo apt install python3-pip
pip3 install -U pip
```

```
pip3 install rasa
```

```
rasa init
```
```
socketio:
  user_message_evt: user_uttered
  bot_message_evt: bot_uttered
  session_persistence: true
```
```
rasa run -m models --enable-api --cors "*" --debug
```

https://www.youtube.com/watch?v=eJMT2FovZsM
***

para abrir a pasta do ubuntu no windows
```
C:\Users\%USERNAME%\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState\rootfs\root

 \\wsl$\
```

```
//client.rest
POST http://localhost:5005/webhooks/rest/webhook HTTP/1.1
Content-Type: application/json

{
  "sender": "test_user",
  "message": "Hi"
}
```

***
nodejs
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
```
reinicia o terminal
```
nvm install node
```

