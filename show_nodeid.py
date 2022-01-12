SHOW_NODEID = '''
{
    "layout":
    {
  "background": {
  "bgColor": "BLACK",
  "enableButtonZone": false,
  "rectangle": {
    "strokeThickness": 6,
    "strokeColor": "BLACK",
    "fillColor": "RED",
    "block": {
      "x_percent": 10,
      "y_percent": 30,
      "w_percent": 80,
      "h_percent": 40
    }
  }
},
        "items": [
            { "type": "TEXT",
                "data": {
                    "id": "NODE_ID",
                    "text": "<NODE_ID>",
                    "textColor": "BLACK",
                    "textAlign": "CENTER",
                    "backgroundColor": "BLACK",
                    "font": "DDIN_24",
                    "block": { "x": 8, "y": 56, "w": 280, "h": 48 },
                    "offset": { "x": 0, "y": 0 }
                }
            },
            { "type": "TEXT",
                "data": {
                    "id": "BEIJING_TIME",
                    "text": "Fri, Jan 08 15:20",
                    "textColor": "RED",
                    "textAlign": "CENTER",
                    "backgroundColor": "RED",
                    "font": "DDIN_CONDENSED_32",
                    "block": { "x": 0, "y": 0, "w": 296, "h": 32 },
                    "offset": { "x": -4, "y": 0 }
                }
            }
        ]
    }
}
'''