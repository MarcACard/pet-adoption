from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import adopt, connect_db, db
from form import PetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "RePlACE_Me_pLeaSe"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home():
    """Return the homepage of the Pet Adoption Website"""
    pets = adopt.query.all()

    return render_template("home.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Display & Process New Pet Adoption Form"""

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = adopt(
            name=name, species=species, photo_url=photo_url, age=age, notes=notes
        )
        flash(message=f"{name} was added for adoption!")
        db.session.add(pet)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)


@app.route("/<int:id>", methods=["GET", "POST"])
def pet_details(id):
    """Display Pet Details & Provide/Process Pet Information Updates"""

    pet = adopt.query.get_or_404(id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.availability = form.availability.data

        db.session.commit()

        flash(message="Changes Successful Saved")
        return redirect(f"/{id}")
    else:
        return render_template("pet_details.html", form=form, pet=pet)
