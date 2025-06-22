# Изначально делал всё через терминал

import os
from datetime import datetime

import django
from django.db.models import Count, F, Q, Avg, ExpressionWrapper, DecimalField

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

django.setup()

from mybooks.models import Author, Book, Review

# Базовые фильтры
# Найди всех авторов с именем «John».
Author.objects.filter(first_name='John')

# Найди всех авторов, кроме тех, у кого фамилия «Doe».
Author.objects.exclude(last_name='Doe')
# ------------------------

#Числовые сравнения
# Найди все книги, цена которых меньше 500.
Book.objects.filter(price__lt=500)

# Найди все книги с ценой не более 300.
Book.objects.filter(price__lte=300)

# Найди все книги дороже 1000.
Book.objects.filter(price__gt=1000)

# Найди все книги с ценой от 750 и выше.
Book.objects.filter(price__gte=750)
#------------------------

# Поиск текста
# Найди все книги, содержащие слово «django» в названии.
Book.objects.filter(title__contains='django')

# Найди книги, в названии которых есть «python» (без учёта регистра).
Book.objects.filter(title__icontains='python')

# Найди книги, название которых начинается со слова «Advanced».
Book.objects.filter(title__startswith='Advanced')

# Найди книги, название которых начинается с «pro» (игнорируя регистр).
Book.objects.filter(title__istartswith='pro')

# Найди книги, название которых заканчивается на слово «Guide».
Book.objects.filter(title__endswith='Guide')

# Найди книги, название которых заканчивается на «tutorial» (без учёта регистра
Book.objects.filter(title__iendswith='tutorial')
#------------------------

#Проверка на null
# Найди все отзывы без комментариев.
Review.objects.filter(comment__isnull=True)

# Найди все отзывы, у которых есть комментари
Review.objects.filter(comment__isnull=False)
#------------------------

# IN и Range
# Найди авторов с идентификаторами 1, 3 и 5.
Author.objects.filter(id__in=[1, 3, 5])

# Найди книги, опубликованные с 1 января по 31 декабря 2023 года
Book.objects.filter(published_date__range=[datetime(2023, 1, 1), datetime(2023, 12, 31)])

#Регулярные выражения
# Найди книги, название которых начинается со слова «Python».
Book.objects.filter(title__regex=r'^Python')

# Найди авторов, чья фамилия начинается на «Mc» (игнорируя регистр)
Author.objects.filter(last_name__iregex=r'^Mc')

#------------------------

# Даты и время
# Найди книги, опубликованные в 2024 году.
Book.objects.filter(published_date__year=2024)

# Найди книги, опубликованные в июне.
Book.objects.filter(published_date__month=6)

# Найди отзывы, оставленные 11-го числа любого месяца.
Review.objects.filter(created_at__day=11)

# Найди книги, опубликованные на 23-й неделе года.
Book.objects.filter(published_date__week=23)

# Найди отзывы, оставленные во вторник.
Review.objects.filter(created_at__week_day=3) # 1 - Воскресенье

# Найди книги, опубликованные во втором квартале года.
Book.objects.filter(published_date__month__gte=4, published_date__month__lte=6)

# Найди отзывы, сделанные в определённую дату.
Review.objects.filter(created_at=datetime(2025,20,2))

# Найди отзывы, сделанные ровно в 15:30.
Review.objects.filter(created_at__hour=15, created_at__minute=30)

# Найди отзывы, сделанные в 15 часов.
Review.objects.filter(created_at__hour=15)

# Найди отзывы, сделанные в 30 минут любого часа.
Review.objects.filter(created_at__minute=30)

# Найди отзывы, созданные в момент, когда секунды были равны 0.
Review.objects.filter(created_at__second=0)
#------------------------

# Связанные поля
# Найди книги, написанные автором с почтой «author@example.com».
Book.objects.filter(author__email='author@example.com')

# Найди книги авторов, чья фамилия содержит «smith» (без учёта регистра).
Book.objects.filter(author__last_name__icontains='smith')

# Найди авторов, написавших более пяти книг.
Author.objects.filter(book_count=Count('books').filter(book_count__gt=5))
#------------------------

# JSON-поля
# Найди книги, у которых значение ключа «genre» равно «fiction».
Book.objects.filter(metadata__genre='fiction')

# Найди книги, где значение ключа «tags» содержит слово «bestseller» (игнорируя регистр).
Book.objects.filter(metadata__tags__icontains='bestseller')
#------------------------

# Использование выражений F и Q
# Найди книги, у которых цена равна скидке.
Book.objects.filter(discount=F('price'))

# Найди книги, у которых цена больше скидки.
Book.objects.filter(price__gt=F('discount'))

# Найди авторов с именем «Alice» или с фамилией, не равной «Brown»
Author.objects.filter(Q(first_name='Alice') | ~Q(last_name='Brown'))
#------------------------

# Задания на аннотации
# Подсчитай количество книг каждого автора.
Author.objects.annotate(book_count=Count('books'))

# Подсчитай средний рейтинг каждой книги.
Book.objects.annotate(avg_rating=Avg('reviews_rating'))

# Посчитай окончательную цену книги (цена минус скидка).
Book.objects.annotate(
     final_price=ExpressionWrapper(F('price') - F('discount'), output_field=DecimalField())
 )

#------------------------
# Использование select_related и prefetch_related
# Получи список книг и авторов так, чтобы выполнить всего один SQL-запрос.
books = Book.objects.select_related('author').all()

# Получи список авторов и всех их книг так, чтобы было выполнено ровно два SQL-запроса.
authors = Author.objects.prefetch_related('books').all()
for author in authors:
    print(author.first_name, author.last_name)
    for book in author.books.all():
        print(book.title)





