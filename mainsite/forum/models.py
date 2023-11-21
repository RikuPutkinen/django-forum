from django.db import models

class Board(models.Model):
    board_name = models.CharField(max_length=50)

    def __str__(self):
        return self.board_name


class Post(models.Model):
    nickname = models.CharField(max_length=20)
    post_title = models.CharField(max_length=50, default="")
    post_text = models.TextField()
    post_date = models.DateTimeField("Date posted")
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title


class Reply(models.Model):
    nickname = models.CharField(max_length=20)
    reply_text = models.TextField()
    post_date = models.DateTimeField("Date posted")
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.reply_text[:50]