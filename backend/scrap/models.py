
from django.db import models
"""
-------------------------------------------------
        @@ MODELS FOR ALL INDIA GOVT JOBS @@    ||
-------------------------------------------------
"""

class UpscJobs(models.Model):
    upsc_id    = models.AutoField(primary_key=True)
    start_date = models.CharField(max_length=60)
    last_date  = models.CharField(max_length=60)
    post_name  = models.CharField(max_length=255)
    education  = models.CharField(max_length=255)
    more_info  = models.TextField()
    type       = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Upsc Jobs"

class SscJobs(models.Model):
    ssc_id     = models.AutoField(primary_key=True)
    start_date = models.CharField(max_length=60)
    last_date  = models.CharField(max_length=60)
    post_name  = models.CharField(max_length=255)
    education  = models.CharField(max_length=255)
    more_info  = models.TextField()
    type       = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Ssc Jobs"

class OtherAllIndiaJobs(models.Model):
    other_all_india_id= models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Other All India Jobs"


"""
-------------------------------------------------
        @@ MODELS FOR SATE WISE GOVT JOBS @@    ||
-------------------------------------------------
"""


class OdishGovtJobs(models.Model):
    odisha_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Odisha Govt Jobs"

class AndamanNicoborGovtJobs(models.Model):
    andaman_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndamanNicobor Govt Jobs"

class AndhraPradeshGovtJobs(models.Model):
    andhra_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "AndhraPradesh Govt Jobs"


class ArunachalPradeshGovernmentjobs(models.Model):
    arunachal_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "ArunachalPradesh Govt Jobs"

class AssamGovtJobs(models.Model):
    assam_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Assam Govt Jobs"

class BiharGovtJobs(models.Model):
    bihar_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Bihar Govt Jobs"

class ChandigarhGovtJobs(models.Model):
    chandigarh_id     = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chandigarh Govt Jobs"

class ChhattisgarhGovtJobs(models.Model):
    chhattisgarh_id   = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id     = models.IntegerField(default=None,blank=True,null=True)
    join_id    = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Chhattisgarh Govt Jobs"
