SHOW_NODEID = '''
{
    "layout":
    {
    "background": {
        "bgColor": "WHITE",
        "enableButtonZone": false,
        "rectangle": {
            "strokeThickness": 0,
            "fillColor": "RED",
            "block": {
                "x_percent": 0,
                "y_percent": 0,
                "w_percent": 100,
                "h_percent": 68
            }
        }
    },
    "items": [
        { "type": "TEXT",
          "data": {
            "text": "%ONGOING_TIME%",
            "id": "ONGOING_TIME",
            "textColor": "WHITE",
            "textAlign": "RIGHT",
            "backgroundColor": "RED",
            "font": "DDIN_24",
            "block": { "x": 0, "y": 0, "w": 296, "h": 32 },
            "offset": { "x": -4, "y": 0 }
          }
        },
        { "type": "TEXT",
          "data": {
            "text": "%ONGOING_EVENT_SUMMARY%",
            "id": "ONGOING_EVENT_SUMMARY",
            "textColor": "WHITE",
            "backgroundColor": "RED",
            "textAlign": "CENTER",
            "font": "YANONE_KAFFEESATZ_44_B",
            "lineSpace": 6,
            "block": { "x": 0, "y": 32, "w": 296, "h": 62 },
            "offset": { "x": 0, "y": 6 }
          }
        },
        { "type": "TEXT",
          "data": {
            "text": "%UPCOMING%",
            "id": "UPCOMING_1_TIME",
            "font": "DDIN_CONDENSED_16",
            "textAlign": "LEFT",
            "block": { "x": 0, "y": 96, "w": 296, "h": 16 },
            "offset": { "x": 2, "y": 0 }
          }
        },
        { "type": "TEXT",
          "data": {
            "text": "%UPCOMING%",
            "id": "UPCOMING_1_SUMMARY",
            "font": "DDIN_CONDENSED_16",
            "textAlign": "LEFT",
            "block": { "x": 0, "y": 112, "w": 296, "h": 16 },
            "offset": { "x": 2, "y": 0 }
          }
        }
    ]
}
}
'''