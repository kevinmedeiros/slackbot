from flask import Flask, Response
from slackeventsapi import SlackEventAdapter
import os
import requests
from bs4 import BeautifulSoup
from threading import Thread
from slack import WebClient
from dotenv import load_dotenv

load_dotenv()

# This `app` represents your existing Flask app
app = Flask(__name__)

greetings = ["dolar agora", "dollar now"]

SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']
slack_token = os.environ['SLACK_BOT_TOKEN']
VERIFICATION_TOKEN = os.environ['VERIFICATION_TOKEN']

#instantiating slack client
slack_client = WebClient(slack_token)


def requestHtml(link: str) -> BeautifulSoup:
    """
    requestHtml(): Serve para retornar o codigo html do site
    :param link: str, link do site
    :return: BeutifulSoup, codigo html
    """
    headers = {
        'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                       ' (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')}

    resposta = requests.get(link, headers)
    return BeautifulSoup(resposta.text, 'html.parser')


def dolar() -> float:
    """
    dolar(): Serve para retornar o preço atual do dólar
    :return: float: preço do dólar
    """
    dados = requestHtml('https://dolarhoje.com/')
    preco = str(dados.find('span', class_='cotMoeda nacional').find('input'))
    return float(preco[preco.find('value="') + 7:preco.rfind('"')].replace(',', '.'))



# An example of one of your Flask app's routes
@app.route("/")
def event_hook(request):
    json_dict = json.loads(request.body.decode("utf-8"))
    if json_dict["token"] != VERIFICATION_TOKEN:
        return {"status": 403}

    if "type" in json_dict:
        if json_dict["type"] == "url_verification":
            response_dict = {"challenge": json_dict["challenge"]}
            print(response_dict)
            return response_dict
    return {"status": 500}
    return


slack_events_adapter = SlackEventAdapter(
    SLACK_SIGNING_SECRET, "/slack/events", app
)


@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))
    return Response(status=500)

@slack_events_adapter.on("message")
def listen_for_messages(event_data):
    def send_reply(value):
        event_data = value
        message = event_data["event"]
        dollar = dolar()
        if message.get("subtype") is None:
            command = message.get("text")
            channel_id = message["channel"]
            if dolar() < 5:
                if any(item in command.lower() for item in greetings):
                    message = (
                        "Oi <@%s>! cotação atual é de R$: %s :broken_heart:"
                        % (message["user"], dollar)  # noqa
                    )
                    slack_client.chat_postMessage(channel=channel_id, text=message)
            else:
                if any(item in command.lower() for item in greetings):
                    message = (
                        "Ola <@%s>! cotação atual é de R$: %s :moneybag:"
                        % (message["user"], dollar)  # noqa
                    )
                    slack_client.chat_postMessage(channel=channel_id, text=message)
    thread = Thread(target=send_reply, kwargs={"value": event_data})
    thread.start()
    return Response(status=200)

# Start the server on port 3000
if __name__ == "__main__":
  app.run(port=3000)