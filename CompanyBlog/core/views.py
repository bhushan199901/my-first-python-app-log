# core/views

from flask import render_template, request, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from CompanyBlog.models import BlogPost
import stripe

# Blueprint for for better organisation
core = Blueprint('core', __name__)

# payment keys - from stripe

public_key = "pk_test_51HtqirEqqKeUnAHaud7Mr19azD5DSTUuiVG8LfKhVoy665ZSpUL2vdKzJotdu4DmcoSVWKRSOhAXfEhFf09HURqQ001GqMBNRB"
stripe.api_key = "sk_test_51HtqirEqqKeUnAHau5w6T3orSkAptt8zLwFZWzhhvXbNFqX4k54HSt3GdW1KAwC0zj8f20zd6XmxNJT3ZpKC5Wc0008eKADEEB"


@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    blog_post = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)

    return render_template('index.html', blog_post=blog_post)

@core.route('/info')
def info():
    return render_template('info.html')


@core.route('/donation')
@login_required
def donation():
    return render_template('donation.html', public_key=public_key)




@core.route('/payment', methods=["POST"])
@login_required
def payment():
    #customer info
    customer = stripe.Customer.create(email=request.form['stripeEmail'],
                                      source=request.form['stripeToken'])

    # payment information
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=1000,
        currency='INR',
        description='Test donation'
    )

    return render_template('Pthankyou.html')
