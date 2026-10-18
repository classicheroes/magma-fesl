from flask import Blueprint, Response


relationships_bp = Blueprint(
    "relationships",
    __name__
)



@relationships_bp.route(
    "/relationships/roster/nucleus:<id>",
    methods=["GET"]
)
def nucleus_roster(id):


    xml = """
<roster count="1">

    <relationship id="0">

        <new>true</new>

        <state>3</state>

        <tag>friends</tag>

        <realid>21</realid>

        <type>server</type>

        <status>
        {"O":5,"N":"aimdll","T":1,"K":1,"L":1,"S":"Test-Server"}
        </status>

        <name>
        5:aimdll
        </name>

    </relationship>

</roster>
"""


    return Response(
        xml,
        content_type="text/xml"
    )

@relationships_bp.route(
    "/relationships/status/server:Test-Server",
    methods=["POST"]
)
def status():


    xml = """

<update>

<status>
5
</status>

<name>
aimdll
</name>

</update>

"""


    return Response(
        xml,
        content_type="text/xml"
    )





@relationships_bp.route(
    "/relationships/roster/server:Test-Server/bvip/1,3"
)
def roster():


    xml = """

<update>

<status>
3
</status>

<name>
aimdll
</name>

</update>

"""


    return Response(
        xml,
        content_type="text/xml"
    )