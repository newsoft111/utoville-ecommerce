from django.core.mail import EmailMessage

def EmailSender(email=None, subject=None, message=None, mailType=None):
	if email is not None:
		subject = subject
		message = message
		mail = EmailMessage(subject, message, to=[email])
		if mailType is not None:
			mail.content_subtype = mailType
		mail.send()
		result = True
	else:
		result = False
	return result


def GetClientIp(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
	else:
			ip = request.META.get('REMOTE_ADDR')
	return ip