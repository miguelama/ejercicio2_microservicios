import strawberry
from strawberry.flask.views import GraphQLView
from typing import List

from app.models import Cart, db


@strawberry.type
class CartType:
    id: int
    name: str
    price: float
    quantity: int
    created_at: str
    updated_at: str


@strawberry.type
class Query:
    @strawberry.field
    def carts(self) -> List[CartType]:
        carts = Cart.query.all()
        return [CartType(**cart.__dict__) for cart in carts]


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_cart(self, name: str, price: float, quantity: int) -> CartType:
        new_cart = Cart(name=name, price=price, quantity=quantity)
        db.session.add(new_cart)
        db.session.commit()
        return CartType(**new_cart.__dict__)

    @strawberry.mutation
    def update_cart(self, id: int, name: str, price: float, quantity: int) -> CartType:
        cart = Cart.query.get(id)
        if cart:
            cart.name = name
            cart.price = price
            cart.quantity = quantity
            db.session.commit()
        return CartType(**cart.__dict__)

    @strawberry.mutation
    def delete_cart(self, id: int) -> bool:
        cart = Cart.query.get(id)
        if cart:
            db.session.delete(cart)
            db.session.commit()
            return True
        return False


schema = strawberry.Schema(query=Query, mutation=Mutation)
