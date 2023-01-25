from fastapi import FastAPI, Request
from heyoo import WhatsApp
import time

token = 'EAASus1U5WsMBALswNdNlxEjcZCCdaYotLjOQkXS279EJ9GXwB3opjfuJDVqcZCOqm8DjZCZAZAVJoWMo3iShXzbfMh0J7GNJ4LnFUeR8dyD3TxltsPXZCDK2H494siaKn3ZAyceYN7GBCufSC5u43Spfd9qfMscZALWZAaTicfi4QfZCz8Gk73zuDf1LeOdUFRTPu95fTP5CwMmgZDZD'

app = FastAPI()

messenger = WhatsApp(token, phone_number_id=106016522397824)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/prueba")
async def say_hello(request: Request):
    try:
        # messenger.send_message('hola estoy usando la API de whatsapp', "525613171220")
        # messenger.send_template("hello_world", "525570701748")
        # time.sleep(10)
        messenger.send_reply_button(
            recipient_id="525570701748",
            button={
                "type": "button",
                "body": {
                    "text": "Esto es una notificación de Aduana:\n"
                            "No. Integración: SATNxxxxxxxxx\n"
                            "Datos de identificación del vehiculo: id5161XXXX\n"
                            "Estatus: ready\n"
                            "Tiempo en la aduana: 2 hrs\n"
                            "Candados: sadxxxxx, 45sxxxxxxx"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "b1",
                                "title": "Okay"
                            }
                        },
                        # {
                        #     "type": "reply",
                        #     "reply": {
                        #         "id": "b2",
                        #         "title": "this is button 2"
                        #     }
                        # }
                    ]
                }
            },
        )
        # request.query_params
        # data = request.json()
        # new_message = messenger.get_mobile(data)
        # if new_message:
        #     mobile = messenger.get_mobile(data)
        #     name = messenger.get_name(data)
        #     message_type = messenger.get_message_type(data)


        return {"message": f"Se envio"}
        # return {"message": f"recivimos: mobile: {mobile}, name: {name}, type: {message_type}"}
    except:
        return {"message": f"No se envio"}
