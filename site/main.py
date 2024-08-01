from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField, FileField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug.security import generate_password_hash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'we-smoke-woods-and-no-one-will-know'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wood.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/images'

db = SQLAlchemy(app)


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    images_path = db.Column(db.String(200))
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    discount = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(50), nullable=False)


class UserData(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    father_name = db.Column(db.String(50), nullable=True)
    total_purchase = db.Column(db.Float, nullable=True)


class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_data.user_id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    mark = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_data.user_id'), primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    images_path = FileField('Images', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')], render_kw={'multiple': True})
    amount = IntegerField('Amount', validators=[DataRequired()])
    description = TextAreaField('Description')
    discount = DecimalField('Discount', validators=[NumberRange(min=0, max=100)])
    submit = SubmitField('Submit')


@app.route('/crm', methods=['GET', 'POST'])
def crm():
    form = ProductForm()
    if form.validate_on_submit():
        # Save the product first to generate an ID
        new_product = Product(
            name=form.name.data,
            price=form.price.data,
            amount=form.amount.data,
            description=form.description.data,
            discount=form.discount.data,
            status='active'
        )
        db.session.add(new_product)
        db.session.commit()

        # Now save the images
        product_id = new_product.product_id
        image_folder = os.path.join(app.config['UPLOAD_FOLDER'], f'product_{product_id}')
        os.makedirs(image_folder, exist_ok=True)

        # Save each file in the uploaded files
        for file in request.files.getlist('images_path'):
            if file and file.filename:
                file.save(os.path.join(image_folder, file.filename))

        # Update the product with the image path
        new_product.images_path = f'uploads/images/product_{product_id}'
        db.session.commit()

        return redirect(url_for('crm'))
    return render_template('crm.html', form=form)


admin = Admin(app, name='CRM', template_mode='bootstrap3')
admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(UserData, db.session))
admin.add_view(ModelView(Review, db.session))
admin.add_view(ModelView(Order, db.session))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        first_name = request.form['first_name']
        second_name = request.form['second_name']
        father_name = request.form.get('father_name')
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if password != confirm_password:
            # Add a flash message or any kind of alert that passwords do not match
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = UserData(
            mail=email,
            password_hash=hashed_password,
            first_name=first_name,
            second_name=second_name,
            father_name=father_name
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('registration.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/catalog')
def catalog():
    products = Product.query.all()
    product_data = []

    for product in products:
        if product.images_path:  # Check if images_path is not None
            image_folder = os.path.join(app.root_path, product.images_path)
            print(image_folder, "====================================================================")
            if os.path.exists(image_folder):
                images = [os.path.join(product.images_path, img) for img in os.listdir(image_folder)]

                print( "+++++++++++++++++++++")
            else:
                images = []
                print("secondIF")
        else:
            images = []  # Or set a default image path if needed
        product_data.append({
            'name': product.name,
            'price': product.price,
            'images': images
        })
        print(images)

    return render_template('catalog.html', products=product_data)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
