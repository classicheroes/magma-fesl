from flask import (
    Blueprint,
    request,
    Response,
    make_response
)

from datetime import datetime
import os
import xml.etree.ElementTree as ET


from config import XML_PATH

from database import db

from models.models import (
    Users,
    RosterNucleus,
    UserEntitlements
)



nucleus_bp = Blueprint(
    "nucleus",
    __name__
)



# =====================================
# XML LOADER
# =====================================

def load_xml(filename):

    path = os.path.join(
        XML_PATH,
        filename
    )

    if not os.path.exists(path):
        return None


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()



# =====================================
# AUTH TOKEN
# =====================================

@nucleus_bp.route(
    "/nucleus/authToken",
    methods=["GET"]
)
def authToken():

    root = ET.Element(
        "success"
    )


    token = ET.SubElement(
        root,
        "token",
        {
            "code":"NEW_TOKEN"
        }
    )


    token.text = request.cookies.get(
        "magma",
        ""
    )


    xml = ET.tostring(
        root,
        encoding="utf-8"
    )


    response = make_response(
        xml
    )


    response.headers[
        "Content-Type"
    ] = "text/xml; charset=utf-8"


    return response





# =====================================
# CHECK USER
# =====================================

@nucleus_bp.route(
    "/nucleus/check/user/<int:user_id>",
    methods=["GET"]
)
def checkUser(user_id):


    user = Users.query.filter_by(
        id=user_id
    ).first()



    if user:


        online = RosterNucleus.query.filter_by(
            user_id=user_id
        ).first()



        if online:

            online.IsOnline = 5


        else:

            online = RosterNucleus(
                username=user.username,
                IsOnline=5,
                user_id=user_id
            )

            db.session.add(
                online
            )


        db.session.commit()



        xml = f"""
        <success>
            IsOnline for {user.username} set to 5
        </success>
        """


    else:

        xml = """
        <error>
        User not found
        </error>
        """



    return Response(
        xml,
        content_type="text/xml"
    )





# =====================================
# WALLET
# =====================================

@nucleus_bp.route(
    "/nucleus/wallets/<user_id>",
    methods=["GET"]
)
def wallets(user_id):


    xml = """
<?xml version="1.0" encoding="UTF-8"?>

<billingAccounts>

    <walletAccount>

        <currency>
        _DV
        </currency>

        <balance>
        999999
        </balance>

    </walletAccount>



    <walletAccount>

        <currency>
        _DB
        </currency>

        <balance>
        999999
        </balance>

    </walletAccount>


    <walletAccount>

        <currency>
        _DH
        </currency>

        <balance>
        999999
        </balance>

    </walletAccount>


</billingAccounts>
"""


    return Response(
        xml,
        content_type="text/xml"
    )





# =====================================
# ENTITLEMENTS
# =====================================

@nucleus_bp.route(
    "/nucleus/entitlements/<user_id>",
    methods=["GET"]
)
def entitlements(user_id):


    data = UserEntitlements.query.filter_by(
        heroID=user_id
    ).all()



    xml = """
<?xml version="1.0" encoding="UTF-8"?>

<entitlements>
"""


    for item in data:


        xml += f"""

<entitlement>

    <entitlementId>
    1
    </entitlementId>


    <entitlementTag>
    {item.productID}
    </entitlementTag>


    <useCount>
    {item.usecount}
    </useCount>


    <grantDate />



    <terminationDate>
    {item.bitistarihi}
    </terminationDate>



    <userId>
    {user_id}
    </userId>


    <status>
    ACTIVE
    </status>


</entitlement>

"""


    xml += """
</entitlements>
"""


    return Response(
        xml,
        content_type="text/xml"
    )

# =====================================
# REFUND ABILITIES
# =====================================

@nucleus_bp.route(
    "/nucleus/refundAbilities",
    methods=["POST"]
)
def refundAbilities():

    xml = load_xml(
        "refundAbilities.xml"
    )

    if xml is None:

        return Response(
            "<error>XML missing</error>",
            status=404,
            content_type="text/xml"
        )

    return Response(
        xml,
        content_type="text/xml"
    )
