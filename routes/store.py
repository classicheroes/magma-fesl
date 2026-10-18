from flask import (
    Blueprint,
    request,
    Response,
    jsonify
)

import os
import xml.etree.ElementTree as ET

from config import XML_PATH

from models.models import (
    UserEntitlements
)

from database import db


# =================================
# BLUEPRINT
# =================================

store_bp = Blueprint(
    "store",
    __name__
)


print("""
================================
      Classic Heroes Store
      Powered by Classic Heroes
================================
""")


# =================================
# XML LOADER
# =================================

def load_xml(filename):

    path = os.path.join(
        XML_PATH,
        filename
    )

    if not os.path.exists(path):

        print(
            "MISSING XML:",
            path
        )

        return None

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


# =================================
# PRODUCTS.XML
# =================================

@store_bp.route(
    "/ofb/products",
    methods=["GET"]
)
def products():

    xml = load_xml(
        "products.xml"
    )

    if xml is None:

        return Response(
            "<error>products.xml missing</error>",
            status=404,
            content_type="text/xml"
        )

    return Response(
        xml,
        content_type="text/xml"
    )


# =================================
# BFH PRODUCT ALIAS
# =================================

@store_bp.route(
    "/ofb/product",
    methods=["GET"]
)
def product_alias():

    return products()


# =================================
# HOT DEALS
# =================================

@store_bp.route(
    "/en/game/hotDeals",
    methods=["GET"]
)
def hot_deals():

    xml = load_xml(
        "hotdeals.xml"
    )

    if xml is None:

        return Response(
            "<error>hotdeals.xml missing</error>",
            status=404,
            content_type="text/xml"
        )

    return Response(
        xml,
        content_type="text/xml"
    )
    
# =================================
# GAME STORE
# =================================

@store_bp.route(
    "/en/game/store",
    methods=["GET"]
)
def game_store():

    persona = request.args.get(
        "personaId",
        ""
    )

    xml_data = load_xml(
        "products.xml"
    )

    if xml_data is None:

        return """
        <html>
        <body>
        <h1>products.xml missing</h1>
        </body>
        </html>
        """

    try:

        root = ET.fromstring(
            xml_data
        )

    except Exception as e:

        return f"""
        <html>
        <body>

        <h1>XML ERROR</h1>

        <pre>{e}</pre>

        </body>
        </html>
        """

    products = root.findall(
        ".//product"
    )

    print(
        "STORE PRODUCTS:",
        len(products)
    )

    items = ""

    for product in products:

        product_id = product.get(
            "productId",
            "0"
        )

        # -----------------------------
        # NAME
        # -----------------------------

        name = "Unknown Item"

        for attr in product.findall(
            ".//attribute"
        ):

            if attr.get("name") == "Product Name":

                name = attr.get(
                    "value",
                    name
                )

                break

        # -----------------------------
        # PRICE
        # -----------------------------

        price = "0"

        price_node = product.find(
            ".//pricePoint[@currency='_DV']"
        )

        if price_node is None:

            price_node = product.find(
                ".//pricePoint"
            )

        if price_node is not None:

            price = price_node.get(
                "price",
                "0"
            )

        # -----------------------------
        # ENTITLEMENT
        # -----------------------------

        entitlement = product_id

        for attr in product.findall(
            ".//attribute"
        ):

            if attr.get("name") == "entitlementTag":

                entitlement = attr.get(
                    "value",
                    product_id
                )

                break

        items += f"""
<div style="background:#222;
border:1px solid #555;
padding:15px;
margin:15px;
width:350px;">

<h2>{name}</h2>

<p>
Product ID:
{product_id}
</p>

<p>
Price:
{price} VP
</p>

<p>
Entitlement:
{entitlement}
</p>

<form
method="post"
action="/ofb/purchase/{persona}/{product_id}">

<button>

BUY

</button>

</form>

</div>
"""

    return f"""

<!DOCTYPE html>

<html>

<head>

<title>

Classic Heroes Store

</title>

<style>

body {

    background:#111;

    color:white;

    font-family:Arial;

}

h1 {

    color:white;

}

.item {

    background:#222;

}

button {

    padding:10px;

    font-size:16px;

    cursor:pointer;

}

</style>

</head>

<body>

<center>

<h1>

Classic Heroes Store

</h1>

<h3>

Powered by Classic Heroes

</h3>

<p>

Persona ID:
{persona}

</p>

</center>

{items}

</body>

</html>

"""


# =================================
# PURCHASE SYSTEM
# =================================

@store_bp.route(
    "/ofb/purchase/<user_id>/<item_id>",
    methods=["POST"]
)
def purchase(
    user_id,
    item_id
):

    print("==============================")
    print("PURCHASE")
    print("USER:", user_id)
    print("ITEM:", item_id)
    print("==============================")

    xml = load_xml(
        "products.xml"
    )

    if xml is None:

        return Response(
            "<error>products.xml missing</error>",
            status=404,
            content_type="text/xml"
        )

    root = ET.fromstring(
        xml
    )

    selected_product = None

    for product in root.findall(".//product"):

        if product.get("productId") == item_id:

            selected_product = product
            break

    if selected_product is None:

        return Response(
            "<error>product not found</error>",
            status=404,
            content_type="text/xml"
        )

    entitlement = item_id

    for attr in selected_product.findall(".//attribute"):

        if attr.get("name") == "entitlementTag":

            entitlement = attr.get(
                "value",
                item_id
            )

            break

    use_count = 1

    for attr in selected_product.findall(".//attribute"):

        if attr.get("name") == "useCount":

            value = attr.get("value")

            if value and value.isdigit():

                use_count = int(value)

            break

    try:

        new_item = UserEntitlements(

            heroID=int(user_id),

            productID=int(
                entitlement.split("-")[0]
            ),

            usecount=use_count

        )

        db.session.add(
            new_item
        )

        db.session.commit()

        print(
            "ENTITLEMENT ADDED:",
            entitlement
        )

    except Exception as e:

        db.session.rollback()

        print(
            "DATABASE ERROR:",
            e
        )

    return Response(
        "<success></success>",
        content_type="text/xml"
    )
    
    # =================================
# OLD BFH BUY API
# =================================

@store_bp.route(
    "/en/store/game/buy",
    methods=["POST"]
)
def buy():

    item_id = request.form.get(
        "itemId",
        ""
    )

    persona = request.form.get(
        "personaId",
        ""
    )

    amount = request.form.get(
        "item" + str(item_id),
        "1"
    )

    print("==============================")
    print("OLD BUY API")
    print("ITEM:", item_id)
    print("PERSONA:", persona)
    print("AMOUNT:", amount)
    print("==============================")

    return jsonify({

        "result": "success",

        "data": {

            "itemId": item_id,

            "itemStatus": str(amount) + " uses left"

        }

    })


# =================================
# MUGSHOT
# =================================

@store_bp.route(
    "/api/mugshot/mayupload/<int:persona_id>",
    methods=["GET"]
)
def may_upload(persona_id):

    return jsonify({

        "mayUpload": False

    })


# =================================
# DEBUG STORE
# =================================

@store_bp.route(
    "/debug/store",
    methods=["GET"]
)
def debug_store():

    xml = load_xml(
        "products.xml"
    )

    if xml is None:

        return jsonify({

            "status": "missing",

            "path": XML_PATH

        })

    try:

        root = ET.fromstring(
            xml
        )

        products = root.findall(
            ".//product"
        )

        return jsonify({

            "status": "ok",

            "products": len(products),

            "xml_size": len(xml)

        })

    except Exception as e:

        return jsonify({

            "status": "xml_error",

            "error": str(e)

        })


# =================================
# REFUND / RETURN ITEM
# =================================

@store_bp.route(
    "/ofb/refund/<int:user_id>/<int:product_id>",
    methods=["POST", "GET"]
)
def refund(user_id, product_id):

    entitlement = UserEntitlements.query.filter_by(

        heroID=user_id,

        productID=product_id

    ).first()

    if entitlement is None:

        return Response(

            "<error>item not owned</error>",

            status=404,

            content_type="text/xml"

        )

    db.session.delete(
        entitlement
    )

    db.session.commit()

    print("==============================")
    print("ITEM REFUNDED")
    print("USER:", user_id)
    print("ITEM:", product_id)
    print("==============================")

    return Response(

        "<success></success>",

        content_type="text/xml"

    )


# =================================
# PLAYER ENTITLEMENTS
# =================================

@store_bp.route(
    "/ofb/entitlements/<int:user_id>",
    methods=["GET"]
)
def entitlements(user_id):

    items = UserEntitlements.query.filter_by(

        heroID=user_id

    ).all()

    root = ET.Element("entitlements")

    for item in items:

        ET.SubElement(

            root,

            "entitlement",

            productId=str(item.productID),

            useCount=str(item.usecount)

        )

    return Response(

        ET.tostring(
            root,
            encoding="unicode"
        ),

        content_type="text/xml"

    )


print("""

================================
      Store Loaded
================================

""")
    