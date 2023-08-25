import requests,json,base64
from html_to_json import convert
#fuck...web-api amino has very few features
class Client():
	def __init__(self):
		self.partial = "https://aminoapps.com/partial"
		self.api="https://aminoapps.com/api"
		self.headers={"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36","x-requested-with": "xmlhttprequest"}
		self.user_Id=None
		self.sid=None
	def get_thread(self,ndc_Id: int,thread_Id: str):
	     data = {"ndcId": f"x{ndc_Id}","threadId": thread_Id}
	     return requests.get(f"{self.api}/get-one-thread",params=data,headers=self.headers).json()
	def get_user_profile(self,ndc_Id: int,user_Id: str):
	     data = {"ndcId": f"x{ndc_Id}","userId": user_Id}
	     return requests.get(f"{self.api}/chat/get-user-profile",params=data,headers=self.headers).json()
	def get_live_threads(self,ndc_Id: int,start: int = 0,size: int = 10):
		return requests.get(f"{self.api}/chat/live-threads?ndcId=x{ndc_Id}&start={start}&size={size}",headers=self.headers).json()
	def get_user_profile(self, ndc_Id: int):
	     data = {"ndcId": ndc_Id}
	     return requests.get(f"{self.api}/get-user-profile",params=data,headers=self.headers).json()
	def get_online_users(self,ndc_Id: int):
		return requests.get(f"{self.api}/x{ndc_Id}/online-members",headers=self.headers).json()["result"]["onlineMembersList"]
	def get_blog_votes(self, ndc_Id: str, blog_Id: str):
		return requests.get(f"{self.api}/x{ndc_Id}/blog/{blog_Id}/votes",headers=self.headers)
	def auth_sid(self, sid: str):
		try:
			value = str(base64.b64decode(sid.replace("sid=", "")))
			value_index = value.index("{")
			value_index_two = value.index("}")
			value = value[value_index: value_index_two + 1]
			data = json.loads(value)
			self.user_Id = data["2"]
			self.sid=sid
			self.headers["cookie"] = f"sid={sid}"
		except BaseException:
			pass
	def search_community(self,page:str,query:str):
		return convert(requests.get(f"{self.partial}/community/search-suggestion?q={query}&page={page}",headers=self.headers).text)
	def members_in_thread(self,ndc_Id: str,thread_Id: str,type: str = "default",start: int = 0,size: int = 10):
	       data = {"ndcId": f"x{ndc_Id}","threadId": thread_Id,"type": type,"start": start,"size": size}
	       return requests.get(f"{self.api}/members-in-thread",params=data,headers=self.headers).json()
	def thread_check(self, ndc_Id):
	       data = {"ndcId": f"x{ndc_Id}"}
	       return requests.get(f"{self.api}/thread-check",params=data,headers=self.headers).json()
	def get_web_socket_url(self):
		return requests.get(f"{self.api}/chat/web-socket-url",headers=self.headers).json()
	def block_full_list(self):
		return requests.get(f"{self.api}/block/full-list",headers=self.headers).json()
	def blog_category(self, ndc_Id: str):
		return requests.get(f"{self.api}/get-blog-category?ndcId={ndc_Id}",headers=self.headers).json()
	def get_live_layer(self, ndc_Id):
		return requests.get(f"{self.api}/x{ndc_Id}/s/live-layer/homepage?v=2",headers=self.headers).json()
	def chat_thread_messages(self,ndc_Id: str,thread_Id: str,size: int = 10):
	       data = {"ndcId": f"x{ndc_Id}", "threadId": thread_Id, "size": size}
	       return requests.get(f"{self.api}/chat-thread-messages",params=data,headers=self.headers).json()
	def my_community(self):
		return convert(requests.get(f"{self.partial}/global-chat-communities",headers=self.headers).text)