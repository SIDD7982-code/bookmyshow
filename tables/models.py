from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#movie genres (Comedy,Action)
class MovieGenres(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#movie format (2D,3D,IMAX).
class MovieFormat(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

#movie category (Bollywood,Hollywood,Tollywood)
class MovieCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name

#name of the language (e.g., "English," "Spanish").
class MovieLanguage(models.Model):
    name = models.CharField(max_length=255, unique=True)
    iso_code = models.CharField(max_length=5, unique=True, blank=True, null=True)
    def __str__(self):
        return self.name

class MovieTime(models.Model):
    show_time = models.TimeField() 
    def __str__(self):
        return f"Show Time: {self.show_time}"

class MovieRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    review = models.TextField(blank=True, null=True)
    movie  = models.ForeignKey('Movie', on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return f"{self.user.username} - Rating: {self.rating} - Movie: {self.movie.title}"

class MovieCast(models.Model):
    actor_name = models.CharField(max_length=255)
    character_name = models.CharField(max_length=255)
    cast_image = models.ImageField(upload_to='cast_images/', null=True, blank=True)
    def __str__(self):
        return f"{self.actor_name} as {self.character_name}"




class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    rating= models.DecimalField(max_digits=3, decimal_places=1,null=True)
    genres = models.ManyToManyField('MovieGenres')
    formats = models.ManyToManyField('MovieFormat')
    languages = models.ManyToManyField('MovieLanguage')
    duration = models.DurationField()
    about = models.TextField()
    cast = models.ManyToManyField('MovieCast')
    timings = models.ManyToManyField('MovieTime')
    category = models.ForeignKey('MovieCategory', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)
    banner_image = models.ImageField(upload_to='movie_banners/', null=True, blank=True)

    def __str__(self):
        return self.title


class MovieSeats(models.Model):
    seat_number = models.CharField(max_length=10)
    movie_timing = models.ForeignKey('MovieTime', on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    language = models.ForeignKey('MovieLanguage', on_delete=models.CASCADE)
    def __str__(self):
        return f"Seat {self.seat_number} - Movie: {self.movie.title} ({self.movie_timing.show_time})"


class MovieTicket(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    movie_timing = models.ForeignKey('MovieTime', on_delete=models.CASCADE)
    movie_language=models.ForeignKey('MovieLanguage',on_delete=models.CASCADE,null=True)
    seat = models.ManyToManyField('MovieSeats')
    razorpay_payment_id=models.CharField(max_length=255,default="Not Paid",null=True)
    razorpay_order_id=models.CharField(max_length=255,default="Not Paid",null=True)
    razorpay_signature=models.CharField(max_length=255,default="Not Paid",null=True)
    buyer_name = models.CharField(max_length=255)
    buyer_email = models.EmailField()
    purchase_date = models.DateTimeField(auto_now_add=True)
    price= models.IntegerField(null=True)

    def __str__(self):
        return f"Ticket for {self.movie.title} - {self.movie_timing.show_time} "
  