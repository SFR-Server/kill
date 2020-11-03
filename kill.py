# -*- coding: utf-8 -*-
def on_user_info(server,info):
    if info.content=="!!kill":
        server.execute("kill "+info.player)