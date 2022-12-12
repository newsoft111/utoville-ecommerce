from django.core.mail import EmailMessage
from collections import OrderedDict

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

class LRUCache:
    def __init__(self, capacity):
        # 최대 캐시 크기
        self.capacity = capacity

        # 캐시 역할
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            # 캐시에 키가 없으므로 return None
            return None
        else:
            # 캐시에 이미 존재
            # 사용되 었으므로 캐시의 제일  뒤로 옮기기
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        # 캐시에 추가. 캐시에 이미 존재 했다면 value를 업데이트 수행
        self.cache[key] = value

        # 사용되 었으므로 캐시의 제일  뒤로 옮기기
        self.cache.move_to_end(key)

        # 캐시 사이즈가 최대 크기가 넘어섰다면
        if len(self.cache) > self.capacity:
            # 가장 오랫동안 참조되지 않은 아이템을 캐시에서 제거
            self.cache.popitem(last=False)
cache = LRUCache(capacity=1000)