from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='store/static/store/media', default='store/static/store/media/default.jpg')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='store/static/store/media/', default='store/static/store/media/default.jpg')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'Cart of {self.user.username}'


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.customer_name} on {self.order_date}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.quantity} of {self.product.name} in cart'

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.quantity} of {self.product.name} in cart'