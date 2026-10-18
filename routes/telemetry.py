from flask import Blueprint, Response, request


telemetry_bp = Blueprint(
    "telemetry",
    __name__
)



@telemetry_bp.route(
    "/dc/submitTelemetry",
    methods=["POST"]
)
def telemetry():


    print(
        request.get_data(
            as_text=True
        )
    )


    return Response(
        "<success></success>",
        content_type="text/xml"
    )




@telemetry_bp.route(
    "/dc/submit",
    methods=["POST"]
)
def submit():


    return Response(
        "<success></success>",
        content_type="text/xml"
    )