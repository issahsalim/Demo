# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib import messages
# from django.utils.html import format_html
# from .models import absenceReport

# @receiver(post_save, sender=absenceReport)  
# def admin_notify(sender, instance, created, **kwargs):  
#     if created:  
#         admin_message = format_html(
#             '<b>An absence report is available from {} parents: {}</b>',
#             instance.Student_Name,
#             instance.reason[:10],   
#         )

         
#         messages.add_message(
#             request
#             level=messages.SUCCESS, 
#             message=admin_message,
#         ) 
