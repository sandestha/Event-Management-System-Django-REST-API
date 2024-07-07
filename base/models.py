from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=300,default='username')
    password = models.CharField(max_length=300)
    groups = models.ManyToManyField(Group)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name_plural = 'User'

class Category(models.Model):
    name = models.CharField(max_length=300) 
    
    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name
    

class Venue(models.Model):
    name = models.CharField(max_length=300)
    capacity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Venue'

    def __str__(self):
        return self.name

class Events(models.Model):
    STATUS = (
        (1, 'Upcomming'),
        (2, 'Completed'),
        (3, 'Cancelled')
    )
    name = models.CharField(max_length=300)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    organizer_name = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,limit_choices_to={'groups__name': "Event Clients"})
    start_date = models.DateTimeField(blank=True,null=True)
    end_time = models.DateTimeField(blank=True,null=True)
    venue = models.ForeignKey(Venue,on_delete=models.SET_NULL,null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS, default=1)
    venue_cost = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    Food_cost_per_person = models.DecimalField(max_digits=8,decimal_places=2,blank=True,null=True)
    

    class Meta:
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name
    
class Attendees(models.Model):
    name = models.CharField(max_length=300)
    contact = models.IntegerField(null=True)
    email = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,limit_choices_to={'groups__name': "Attendees"})
    event = models.ForeignKey(Events,on_delete=models.SET_NULL,null=True,related_name='attendees')

    class Meta:
        verbose_name_plural = 'Attendees'

    def __str__(self):
        return self.name
    
class Vendors(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    contact_person = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,limit_choices_to={'groups__name': "Event Vendors"})

    class Meta:
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    booking_name = models.CharField(max_length=300)
    event = models.ForeignKey(Events,on_delete=models.SET_NULL,null=True)
    organizer_name = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,limit_choices_to={'groups__name': "Event Clients"})
    reserved_date = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return f'{self.booking_name}{' --> '}{self.event}'
    
class Tickets(models.Model):
    ticket_no = models.CharField(max_length=300,blank=True, null=True)
    event = models.ForeignKey(Events,on_delete=models.SET_NULL,null=True,related_name='tickets') 
    attendee = models.ForeignKey(Attendees,on_delete=models.SET_NULL,blank=True,null=True,related_name='tickets')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    payment_date = models.DateField(blank=True, null=True)
    payment_method = models.CharField(max_length=200,blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return f'{self.ticket_no}'

    # def __str__(self):
    #     if self.attendee == None:
    #         return f'{self.ticket_no},{self.booking_name}'
    #     elif self.booking_name == None:
    #         return f'{self.ticket_no},{self.attendee}{' --> '}{self.event}'
       
# class Payment(models.Model):
#     ticket_no = models.ForeignKey(Tickets,on_delete=models.SET_NULL,null=True)
#     transaction_no = models.CharField(max_length=300)
#     payment_amount = models.IntegerField()
#     payment_date = models.DateField()
#     payment_method = models.CharField(max_length=200)

#     class Meta:
#         verbose_name_plural = 'Payments'

#     def __str__(self):
#         return self.transaction_no
    
class Reviews(models.Model):
        reviewer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,limit_choices_to={'groups__name': "Attendees"})
        event = models.ForeignKey(Events,on_delete=models.SET_NULL,null=True)
        feedback = models.TextField()
        
        class Meta:
            verbose_name_plural = 'Reviews'

        def __str__(self):
            return f'{self.reviewer}{' --> '}{self.event}'
        