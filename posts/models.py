from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.paginator import Paginator

# Create your models here.
class Post(models.Model):
	image = models.ImageField(upload_to='posts')
	date_posted =models.DateTimeField(default= timezone.now)
	caption = models.TextField()
	author = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.author} --> post'

	@classmethod
	def paginate(cls,page_num,paginate_by=10):
		posts = cls.objects.order_by('-date_posted').all()
		
		paginator = Paginator(posts,paginate_by)
		page_obj = paginator.page(page_num)
		paginated_messages = page_obj.object_list
		has_more = page_obj.has_next()
		
		if has_more:
			next_page = page_obj.next_page_number()
			return paginated_messages, has_more, next_page
		return paginated_messages, has_more, False