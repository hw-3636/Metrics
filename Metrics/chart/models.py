from django.db import models

class articles(models.Model):
    articlesCd = models.IntegerField(primary_key=True)
    news_organization_name = models.TextField()
    ranking_date = models.DateField()
    ranking = models.IntegerField()
    ranking_page_link = models.CharField()
    article_title = models.TextField()
    reporter_name = models.TextField()
    creation_time = models.TimeField()
    news_content = models.CharField()
    article_section = models.TextField()

class reporters(models.Model):
    reportersCd = models.IntegerField(primary_key=True)
    reporters_news_organization = models.TextField()
    reporters_reporter_name = models.TextField()
    reporters_creation_time = models.TimeField()
    reporters_title = models.TextField()
    reporters_news_content = models.CharField()



    # 메타 클래스 : 기본 컬럼 이외에 모델의 설정 정보를 담고 있는 내부 클래스
    # 예를 들어 테이블 이름이나, 정렬 방식등을 설정 할 수 있습니다.
    class Meta:
        db_table = 'articles','reporters'
