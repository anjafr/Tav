import functions_framework
from models.character import Tav


@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_args = request.args
    tav_name = request_args.get("name", "Tav")
    number_of_classes = int(request_args.get("num_max_classes", 12))
    tav = Tav(name=tav_name, num_max_classes=number_of_classes)

    while tav.character_level < 12:
        tav.level_up()

    return tav.__dict__
