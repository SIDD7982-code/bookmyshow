from django.shortcuts import render,redirect,HttpResponse
from tables.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import razorpay
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa



client=razorpay.Client(auth=("rzp_test_Oz4TKvlB4DggmA","t10b4MAJ5djKTzawnbzJgATr"))


def getpdf(template_name, data= {}):
    template= get_template(template_name)
    html= template.render(data)
    result= BytesIO()
    pdf= pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)

    if not pdf.err:
        return  HttpResponse(result.getvalue(),content_type='application/pdf')
    else:
        return None
    
    
    
def ViewPDF(request,id):
    ticket=MovieTicket.objects.get(id=id)
    response= getpdf('invoice.html',{"ticket":ticket})
    return response

def DownlaodPDF(request,id):
    ticket=MovieTicket.objects.get(id=id)
    response = getpdf('invoice.html',{"ticket":ticket})
    response['Content-Disposition']= "attachment;filename=abc.pdf"
    return response



def Home(request):
    movies=     Movie.objects.all()
    languages=  MovieLanguage.objects.all()
    genres=     MovieGenres.objects.all()
    formats=    MovieFormat.objects.all()
    categories= MovieCategory.objects.all()

    p= Paginator(movies,6)
    page_no= request.GET.get('page')

    if page_no:
        movies = p.page(page_no)
    else:
        movies= p.page(1)

    data= {"movies": movies,"languages":languages,"genres":genres,"formats":formats,"categories":categories}

    return render(request,"index.html",data)


def LanguageFilter(request,name):
    movies= Movie.objects.filter(languages__name= name)

    languages = MovieLanguage.objects.all()
    genres = MovieGenres.objects.all()
    formats = MovieFormat.objects.all()
    categories = MovieCategory.objects.all()

    p = Paginator(movies, 6)
    page_no = request.GET.get('page')

    if page_no:
        movies = p.page(page_no)
    else:
        movies = p.page(1)

    data = {"movies": movies, "languages": languages, "genres": genres, "formats": formats, "categories": categories}

    return render(request, "index.html", data)


def GenresFilter(request,name):
    movies= Movie.objects.filter(genres__name= name)

    languages = MovieLanguage.objects.all()
    genres = MovieGenres.objects.all()
    formats = MovieFormat.objects.all()
    categories = MovieCategory.objects.all()

    p = Paginator(movies, 6)
    page_no = request.GET.get('page')

    if page_no:
        movies = p.page(page_no)
    else:
        movies = p.page(1)

    data = {"movies": movies, "languages": languages, "genres": genres, "formats": formats, "categories": categories}

    return render(request, "index.html", data)

def FormatFilter(request,name):
    movies= Movie.objects.filter(formats__name= name)

    languages = MovieLanguage.objects.all()
    genres = MovieGenres.objects.all()
    formats = MovieFormat.objects.all()
    categories = MovieCategory.objects.all()

    p = Paginator(movies, 6)
    page_no = request.GET.get('page')

    if page_no:
        movies = p.page(page_no)
    else:
        movies = p.page(1)

    data = {"movies": movies, "languages": languages, "genres": genres, "formats": formats, "categories": categories}

    return render(request, "index.html", data)

def CategoryFilter(request,name):
    movies= Movie.objects.filter(category__name= name)

    languages = MovieLanguage.objects.all()
    genres = MovieGenres.objects.all()
    formats = MovieFormat.objects.all()
    categories = MovieCategory.objects.all()

    p = Paginator(movies, 6)
    page_no = request.GET.get('page')

    if page_no:
        movies = p.page(page_no)
    else:
        movies = p.page(1)

    data = {"movies": movies, "languages": languages, "genres": genres, "formats": formats, "categories": categories}

    return render(request, "index.html", data)

def MovieDetails(request,id):
    movie= Movie.objects.get(id= id)
    duration= f"{int(movie.duration.total_seconds() // 3600)}h {int((movie.duration.total_seconds()%3600)//60)}min"

    comments= MovieRating.objects.filter(movie= movie)
    return render(request,"movie.html",{ "movie": movie ,"duration": duration,"comments":comments})


def SignUp(request):
    username= request.POST.get("username")
    password= request.POST.get("password")
    email= request.POST.get("email")

    print(username,password,email)
    User.objects.create_user(username= username,password= password,email= email)

    return redirect('home')

def SignIn(request):
    username= request.POST.get("username")
    password= request.POST.get("password")

    user= authenticate(username= username,password=password)

    if user is not None:
        login(request,user)

    return redirect('home')

def SignOut(request):
    logout(request)

    return redirect('home')

def Search(request):
    name= request.GET.get('name')
    movies = Movie.objects.filter(title__icontains= name)

    languages = MovieLanguage.objects.all()
    genres = MovieGenres.objects.all()
    formats = MovieFormat.objects.all()
    categories = MovieCategory.objects.all()
    data = {"movies": movies, "languages": languages, "genres": genres, "formats": formats, "categories": categories}

    return render(request, "index.html", data)

@login_required(login_url='/')
def Profile(request):

    if request.method == 'POST':
        username= request.POST.get('username')
        email= request.POST.get('email')

        user= request.user
        user.email= email
        user.username= username

        user.save()
        
        
        
    tickets=MovieTicket.objects.filter(buyer_name = request.user.username)
    
    return render(request,"profile.html",{"tickets": tickets})


@login_required(login_url='/')
def SubmitRating(request):

    movieid= request.POST.get("movieid")
    rating= request.POST.get("rating")
    review= request.POST.get("review")
    user= request.user



    movie = Movie.objects.get(id=movieid)
    duration = f"{int(movie.duration.total_seconds() // 3600)}h {int((movie.duration.total_seconds() % 3600) // 60)}min"

    MovieRating.objects.create(user=user, rating=rating, review=review,movie= movie)
    comments= MovieRating.objects.filter(movie= movie)

    return render(request, "movie.html", {"movie": movie, "duration": duration,"comments": comments})


@login_required(login_url='/')
def BookSeat(request):
    movieid= request.POST.get('movieid')
    language= request.POST.get("Language")
    time= request.POST.get("Timing")

    seat_tuple= []
    reserved_seats= MovieSeats.objects.filter(movie__id= movieid,language__name= language,movie_timing__show_time= time)

    for seat in reserved_seats:
        seat_tuple.append({"seat": seat.seat_number})


    return render(request,"book.html",{"id":movieid,"language":language,"time":time,"reserved_seats":seat_tuple})

@login_required(login_url='/')
def PayNow(request):
    movieid = request.POST.get('movieid')
    language = request.POST.get("language")
    time = request.POST.get("time")
    price= request.POST.get("price")
    seat= request.POST.getlist("seat") #['a1','n12']
    seats= []

    movie= Movie.objects.get(id= movieid)
    movie_time= MovieTime.objects.get(show_time= time)
    buyer_name= request.user.username
    buyer_email= request.user.email
    language= MovieLanguage.objects.get(name= language)
    price= int(price)

    for x in seat:
        seat_number= x
        seats.append(MovieSeats.objects.create(seat_number= seat_number,movie_timing=movie_time,movie= movie,language=language))


    ticket= MovieTicket.objects.create(movie= movie,movie_timing= movie_time,buyer_name= buyer_name,buyer_email= buyer_email,price= price,movie_language=language)
    ticket.seat.add(*seats)

    DATA = {
        "amount": price*100,
        "currency": "INR",
        "receipt": "Movie Ticket",
        "payment_capture": 1
    }
    order= client.order.create(data=DATA)

    return render(request,"payment.html",{"ticket": ticket,"order": order})






def PaymnetSuccess(request):
    return render(request,"success.html")


def Paymnetfailed(request):
    return render(request,"failure.html")