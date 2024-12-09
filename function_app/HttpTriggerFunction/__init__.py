import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    val = req.params.get('val')
    if not val:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('val')

    if val:
        return func.HttpResponse(f"Function app {val}!")
    else:
        return func.HttpResponse(
            "",
            status_code=400
        )