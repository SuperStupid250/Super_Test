SHOW_NODEID = '''
{
    "layout":
{
    "background": {
        "bgColor": "WHITE",
        "enableButtonZone": false,
        "rectangle": {
            "block": {
                "x_percent": 0,
                "y_percent": 0,
                "w_percent": 0,
                "h_percent": 0
            }
        }
    },
    "items": [
         { "type": "BITMAP_URI",
          "data": {
            "id": "NODE_ID",
            "text": "<NODE_ID>",
            "font": "DDIN_24",
            "foregroundColor": "WHITE",
            "backgroundColor": "WHITE",
            "uri": "https://file.sync-sign.com/assets/img/car_black_part.bmp",
            "block": { "x": 0, "y": 0, "w": 880, "h": 528 }
          }
         },
           { "type": "BITMAP_URI",
          "data": {
            "id": "BEIJING_TIME",
            "text": "Fri, Jan 08 15:20",
            "font": "DDIN_CONDENSED_32",
            "foregroundColor": "RED",
            "backgroundColor": "WHITE",
            "uri": "https://file.sync-sign.com/assets/img/car_red_part.bmp",
            "block": { "x": 0, "y": 0, "w": 880, "h": 528 }
          }
         }
    ],
    "options" : { "pollRate": 5000 }
}}
'''