import server  # noqa
from aiohttp import web

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]


@server.PromptServer.instance.routes.post("/graph_to_prompt")
async def graph_to_prompt(request):
    data = await request.json()
    print("\x1b[31m", data, "\x1b[m")
    server.PromptServer.instance.send_sync("run_workflow", data)
    return web.Response()


@server.PromptServer.instance.routes.post("/graph_to_prompt_from_js")
async def graph_to_prompt_from_js(request):
    data = await request.read()
    print("\x1b[32m", data, "\x1b[m")
    return web.Response()
