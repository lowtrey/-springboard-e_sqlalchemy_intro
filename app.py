from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, Pet

app = Flask(__name__)

# Congifure and Initialize Database
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_shop_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config['SECRET_KEY'] = "chickens"

connect_db(app)

@app.route("/")
def list_pets():
  """Shows list of all pets in db"""
  pets = Pet.query.all()
  return render_template("list.html", pets=pets)

@app.route("/", methods=["POST"])
def create_pet():
  name = request.form["name"]
  species = request.form["species"]
  hunger = request.form["hunger"]
  hunger = int(hunger) if hunger else None

  new_pet = Pet(name=name, species=species, hunger=hunger)
  db.session.add(new_pet)
  db.session.commit()

  return redirect(f"/{new_pet.id}")

@app.route("/<int:pet_id>")
def show_pet(pet_id):
  """Show details about a single pet"""
  pet = Pet.query.get_or_404(pet_id)
  return render_template("details.html", pet=pet)