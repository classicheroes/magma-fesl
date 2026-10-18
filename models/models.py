from database import db
from datetime import datetime



# ===================================
# ENTITLEMENTS
# ===================================

class Entitlement(db.Model):

    __tablename__ = "entitlements"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer
    )

    product_id = db.Column(
        db.Integer
    )

    purchase_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )



# ===================================
# GAME STATS
# ===================================

class GameStats(db.Model):

    __tablename__ = "game_stats"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    heroID = db.Column(
        db.Integer
    )

    statsKey = db.Column(
        db.String(255)
    )

    statsValue = db.Column(
        db.String(255)
    )

    user_id = db.Column(
        db.Integer
    )



# ===================================
# USER ENTITLEMENTS
# ===================================

class UserEntitlements(db.Model):

    __tablename__ = "user_entitlements"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    heroID = db.Column(
        db.Integer,
        nullable=False
    )

    productID = db.Column(
        db.Integer,
        nullable=True
    )

    usecount = db.Column(
        db.Integer
    )

    bitistarihi = db.Column(
        db.String(255)
    )

    alimtarihi = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )



# ===================================
# USERS
# ===================================

class Users(db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(255)
    )

    game_token = db.Column(
        db.String(255)
    )



# ===================================
# FRIENDS / RELATIONSHIPS
# ===================================

class UsersFriends(db.Model):

    __tablename__ = "users_friends"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    nucleusID1 = db.Column(
        db.Integer
    )


    nucleus1Name = db.Column(
        db.String(255)
    )


    nucleusID2 = db.Column(
        db.Integer
    )


    nucleus2Name = db.Column(
        db.String(255)
    )


    relationship_type = db.Column(
        db.String(50),
        nullable=False
    )


    relationship_id = db.Column(
        db.Integer,
        default=0
    )



# ===================================
# IN GAME STORE
# ===================================

class IngameStore(db.Model):

    __tablename__ = "ingame_store"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    ItemID = db.Column(
        db.String(50)
    )


    value = db.Column(
        db.Integer
    )


    price = db.Column(
        db.Integer
    )



# ===================================
# ONLINE ROSTER
# ===================================

class RosterNucleus(db.Model):

    __tablename__ = "roster_nucleus"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    username = db.Column(
        db.String(255)
    )


    IsOnline = db.Column(
        db.Integer
    )


    heroname = db.Column(
        db.String(50)
    )


    user_id = db.Column(
        db.Integer,
        nullable=False
    )



# ===================================
# GAME HEROES
# ===================================

class GameHeroes(db.Model):

    __tablename__ = "game_heroes"


    id = db.Column(
        db.Integer,
        primary_key=True
    )


    user_id = db.Column(
        db.Integer
    )


    heroName = db.Column(
        db.String(255)
    )