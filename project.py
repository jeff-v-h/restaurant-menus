from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#Fake Restaurants (TEMPORARY)
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}
restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]

#Fake Menu Items (TEMPORARY)
menuitems = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
menuitem =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


## Routes for listing, creating, editing and deleting restaurants
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
	return render_template('main.html', restaurants = restaurants)

@app.route('/restaurants/new/')
def newRestaurant():
	return render_template('newrestaurant.html')

@app.route('/restaurants/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
	return render_template('editrestaurant.html', restaurant = restaurant)

@app.route('/restaurants/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
	return render_template('deleterestaurant.html', restaurant = restaurant)


## Routes for listing, creating, editing and deleting menu items for a specified restaurant
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
	return render_template('menu.html', restaurant = restaurant, items = menuitems)

@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
	return render_template('newmenuitem.html', restaurant = restaurant)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
	return render_template('editmenuitem.html', restaurant=restaurant, item=menuitem)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
	return render_template('deletemenuitem.html', restaurant=restaurant, item=menuitem)


## For running website on localhost:5000 in debug mode (automatic refresh of webserver on file save)
if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)