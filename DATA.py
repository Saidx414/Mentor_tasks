# Чем заполнял таблицу
# Решения в Examples

# a1 = Author.objects.create(first_name='John', last_name='Black', email = 'johnblack@email.com')
# a2 = Author.objects.create(first_name='Ivan', last_name='Ivanov', email='ivanivanov@emailc.com')
# a3 = Author.objects.create(first_name='Alice', last_name='Macdonalds', email='aliceburger@email.com')
# a4 = Author.objects.create(first_name='Max', last_name='Petrov', email='maxpetrov@email.com')
# a5 = Author.objects.create(first_name='Harry', last_name='Potter', email='harry@email.com')
#
# b1 = Book.objects.create(title='django', author=a1, published_date=datetime.datetime(2025,1,21,11,30), price = 500, discount=0, metadata={'genre':'tech'})
#
# b2 = Book.objects.create(title='Advanced Python', author=a2, published_date=datetime.datetime(2025,2,22,10,10), price = 1000, discount=100, metadata={'genre':'tech'})
#
# b3 = Book.objects.create(title='Pro SQL', author=a3, published_date=datetime.datetime(2023,3,5,20,12), price = 800, discount=0, metadata={'genre':'tech'})
#
# b4 = Book.objects.create(title='Guide IT-English', author=a4, published_date=datetime.datetime(2023,6,14,9,30), price = 500, discount = 50, metadata={'tags':'bestseller'})
#
# r1 = Review.objects.create(book=b1, rating=10, comment='Лучшая книга')
# r2 = Review.objects.create(book=b2, rating=5, comment='Много воды')
# r3 = Review.objects.create(book=b3, rating=7, comment='Устаревшая информация')
# r4 = Review.objects.create(book=b4, rating=8, comment='Мне понравилась книга')