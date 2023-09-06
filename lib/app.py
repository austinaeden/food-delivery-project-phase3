# alembic upgrade head
# pip install faker
# alembic init migrations
# cd lib
# alembic revision -m "empty init"
# alembic upgrade head
# alembic revision --autogenerate -m "created tables"
# alembic upgrade head

from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Float, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the naming convention for foreign keys
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

# Create a metadata object with the naming convention
metadata = MetaData(naming_convention=convention)

# Create the base class for all models
Base = declarative_base(metadata=metadata)

# Define the database connection
engine = create_engine('sqlite:///restaurants.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Restaurant model
class Restaurant(Base):
    __tablename__ = "restaurants"

    # Define restaurant columns
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float, nullable=False)

    # Define the relationship with Review explicitly
    reviews = relationship("Review", back_populates="restaurant")

    # Make restaurant object readable
    def __repr__(self):
        return f'<Restaurant name:{self.name}, price:{self.price}>'

    # Return all reviews for a specific restaurant
    def restaurant_reviews(self):
        reviews = session.query(Review).filter_by(restaurant_id=self.id).all()
        return reviews

    # Return customers who have made reviews for a specific restaurant
    def restaurant_customers(self):
        reviews = session.query(Review).filter_by(restaurant_id=self.id).all()
        return [review.customer for review in reviews]

    # Return the fanciest restaurant
    @classmethod
    def fanciest_restaurant(cls):
        restaurant = session.query(Restaurant).order_by(Restaurant.price.desc()).first()
        return restaurant

    # Return all reviews for a given restaurant in a specific format
    def all_reviews(self):
        reviews = session.query(Review).filter_by(restaurant_id=self.id).all()
        return [review.full_review() for review in reviews]


# Customer model
class Customer(Base):
    __tablename__ = "customers"

    # Define customer columns
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define relationships
    reviews = relationship("Review", back_populates="customer")
    restaurants = relationship("Review", back_populates="customer", overlaps="reviews")

    # Make customer object readable
    def __repr__(self):
        return f"<Customer {self.first_name} {self.last_name}>"

    # Return all reviews for a specific customer
    def customer_reviews(self):
        reviews = session.query(Review).filter_by(customer_id=self.id).all()
        return reviews

    # Return all restaurants reviewed for a specific customer
    def customer_restaurants(self):
        reviews = session.query(Review).filter_by(customer_id=self.id).all()
        return [review.restaurant for review in reviews]

    # Return the full name of the customer
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Return the reviewed restaurant with the highest rating for a specific customer
    def favorite_restaurant(self):
        review = session.query(Review).filter_by(customer_id=self.id).order_by(Review.star_rating.desc()).limit(1).first()
        return review.restaurant

    # Add a review and persist it in the database
    def add_review(self, restaurant_id, rating):
        new_review = Review(
            star_rating=rating,
            restaurant_id=restaurant_id,
            customer=self
        )
        session.add(new_review)
        session.commit()
        return "Review added successfully"

    # Delete a review from the database
    def delete_review(self, restaurant_id):
        print(f"Deleting reviews for customer_id={self.id} and restaurant_id={restaurant_id}")
        reviews = session.query(Review).filter_by(customer_id=self.id, restaurant_id=restaurant_id).all()

        for review in reviews:
            print(f"Deleting review with id={review.id}")
            session.delete(review)

        session.commit()

        return "Reviews deleted successfully"


# Review model
class Review(Base):
    __tablename__ = "reviews"

    # Define review columns
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Define the relationships explicitly
    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    # Return the customer for a specific review
    def review_customer(self):
        return self.customer

    # Return the restaurant for a specific review
    def review_restaurant(self):
        return self.restaurant

    # Make the review object readable
    def __repr__(self):
        return f"<Review, Star rating: {self.star_rating}, customer id:{self.customer_id}, restaurant_id:{self.restaurant_id}>"

    # Return the review in a specific format
    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}  : {self.star_rating} stars"


# Test add_review and delete_review methods
customer1 = session.query(Customer).filter_by(id=20).first()  # Change the ID to the desired customer
print(customer1.delete_review(42))
customer2 = session.query(Customer).filter_by(id=10).first()  # Change the ID to the desired customer
print(customer2.add_review(18, 5))
