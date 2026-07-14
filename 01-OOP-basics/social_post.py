class SocialPost:
    def __init__(self,username,caption):
        self.username=username
        self.caption=caption
        self.like_count=0
        self.comments=[]
    def likes(self):
        self.like_count+=1
        print(f"❤️ someone liked @{self.username}'s post")
    def add_comment(self,commenter,text):
        full_comment=f"{commenter}:{text}"
        self.comments.append(full_comment)
        print(f"💭 New comment by {self.username}")
    def display_engagement(self):
        print(f"\n----- Post by @{self.username} ------")
        print(f"{self.caption}")
        print(f"Likes: {self.like_count}")
        print("comments: ")
        for i in self.comments:
            print(f"  {i}")
    
#creating object
post1=SocialPost("Python_journey","Just created my 1st gitHub repo!!")
post1.likes()
post1.likes()
post1.add_comment("coder123","Keep it up!!!")
post1.add_comment("developer321","Good Job!")
post1.display_engagement()