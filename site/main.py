from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FloatField, TextAreaField, FileField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email, NumberRange
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf.file import FileRequired, FileAllowed
import email_validator
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'we-smoke-woods-and-no-one-will-know'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wood.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/images'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


# User loader function
@login_manager.user_loader
def load_user(user_id):
    return UserData.query.get(int(user_id))


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    images_path = db.Column(db.String(200))
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    discount = db.Column(db.Float, nullable=True)
    status = db.Column(db.String(50), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)


class ContactMe(db.Model):
    request_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)


# Initialize the database with categories
def init_db():
    db.create_all()
    categories = ["Столешницы", "Стулья", "Шкафы", "Кресла", "Принадлежности", "Скамейки", "Кровати", "Декор"]
    for cat_name in categories:
        category = Category(name=cat_name)
        db.session.add(category)
    ##db.session.commit()


class UserData(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    mail = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    second_name = db.Column(db.String(50), nullable=False)
    father_name = db.Column(db.String(50), nullable=True)
    total_purchase = db.Column(db.Float, nullable=True)

    def get_id(self):
        return (self.user_id)

    @property
    def is_authenticated(self):
        # Assume all users are authenticated
        return True

    @property
    def is_active(self):
        # Assume all users are active
        return True

    @property
    def is_anonymous(self):
        # No anonymous users
        return False


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


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


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    images_path = FileField('Images', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')], render_kw={'multiple': True})
    amount = IntegerField('Amount', validators=[DataRequired()])
    description = TextAreaField('Description')
    discount = DecimalField('Discount', validators=[NumberRange(min=0, max=100)])
    submit = SubmitField('Submit')


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

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserData.query.filter_by(mail=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/catalog', methods=['GET'])
def catalog():
    categories = Category.query.all()
    products = Product.query.all()
    return render_template('catalog.html', categories=categories, products=products)


# Форма для создания/редактирования продукта
@app.route('/products', methods=['GET', 'POST'])
def manage_products():
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        name = request.form.get('name')
        price = request.form.get('price')
        amount = request.form.get('amount')
        description = request.form.get('description')
        discount = request.form.get('discount')
        status = request.form.get('status')
        category_id = request.form.get('category_id')

        if product_id:  # Обновление существующего продукта
            product = Product.query.get(product_id)
            product.name = name
            product.price = price
            product.amount = amount
            product.description = description
            product.discount = discount
            product.status = status
            product.category_id = category_id
        else:  # Создание нового продукта
            new_product = Product(
                name=name,
                price=price,
                amount=amount,
                description=description,
                discount=discount,
                status=status,
                category_id=category_id
            )
            db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('manage_products'))

    # Получение всех данных для отображения в соответствующих вкладках
    products = Product.query.all()
    orders = Order.query.all()
    reviews = Review.query.all()
    users = UserData.query.all()

    # Передача данных в шаблон
    return render_template('crm.html', products=products, orders=orders, reviews=reviews, users=users)


@app.route('/products/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('manage_products'))


@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        if not name or not email or not message:
            flash('Все поля должны быть заполнены.', 'error')
            return redirect(url_for('contact'))

        if '@' not in email or '.' not in email:
            flash('Введите корректный email.', 'error')
            return redirect(url_for('contact'))

        new_contact = ContactMe(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()

        flash('Сообщение отправлено.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/order_history')
def order_history():
    return render_template('order_history.html')


if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
