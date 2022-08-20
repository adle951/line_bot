from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('DtsSiiLQjM9jLvv/HP5P5Nen1XWVtmMDxeNL9DGJ7SYxDmQlU+xsOLRsxBXZD09xy50Te9EkMju7eJIKxNBDZYjDKm1rAUMco5ODH/jTwcm5UYbYZP+7mz9BWFolUa+zSr0O+KtVN0/xE2LG9ZBaXQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e6c973767e150e0bc966638b5d3de588')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我看不懂你在說甚麼'

    if '貼圖': in msg
        line_bot_api.reply_message(
            event.reply_token,
            sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
            )


    
    if msg == "你吃飯了嗎?":
        r = "還沒"
    elif '如何' in msg:
        r = '還不錯'



    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()