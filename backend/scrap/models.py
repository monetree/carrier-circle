
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


class OdishaGovtJobs(models.Model):
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

class DadraNagarHaveliGovtJobs(models.Model):
    dadra_nagar_haveli_id = models.AutoField(primary_key=True)
    start_date            = models.CharField(max_length=60)
    last_date             = models.CharField(max_length=60)
    post_name             = models.CharField(max_length=255)
    education             = models.CharField(max_length=255)
    more_info             = models.TextField()
    requirement_board     = models.CharField(max_length=255)
    type                  = models.IntegerField()
    job_id                = models.IntegerField(default=None,blank=True,null=True)
    join_id               = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DadraNagarHavelis Govt Jobs"

class DamanDiuGovtJobs(models.Model):
    daman_diu_id      = models.AutoField(primary_key=True)
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
        return "DamanDiu Govt Jobs"

class DelhiGovtJobs(models.Model):
    delhi_id         = models.AutoField(primary_key=True)
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
        return "Delhi Govt Jobs"

class GoaGovernmentjobs(models.Model):
    goa_id            = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Goa Govt Jobs"

class GujuratGovtJobs(models.Model):
    gujurat_id        = models.AutoField(primary_key=True)
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
        return "Gujurat Govt Jobs"

class HaryanaGovtJobs(models.Model):
    haryana_id          = models.AutoField(primary_key=True)
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
        return "Haryana Govt Jobs"

class HimachalPradeshGovtJobs(models.Model):
    himachal_id       = models.AutoField(primary_key=True)
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
        return "HimachalPradesh Govt Jobs"

class JammuKashmirGovtJobs(models.Model):
    jammu_kashmir_id  = models.AutoField(primary_key=True)
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
        return "JammuKashmir Govt Jobs"

class JharkhandGovtJobs(models.Model):
    jharkhand_id      = models.AutoField(primary_key=True)
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
        return "Jharkhand Govt Jobs"

class KarnatakaGovtJobs(models.Model):
    karnataka_id      = models.AutoField(primary_key=True)
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
        return "karnataka Govt Jobs"

class KeralaGovtJobs(models.Model):
    kerala_id         = models.AutoField(primary_key=True)
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
        return "Kerala Govt Jobs"

class LakshadweepGovernmentjobs(models.Model):
    lakshadweep_id    = models.AutoField(primary_key=True)
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
        return "Lakshadweep Govt Jobs"

class MadhyaPradeshGovtJobs(models.Model):
    madhya_pradesh_id = models.AutoField(primary_key=True)
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
        return "MadhyaPradesh Govt Jobs"

class MaharashtraGovtJobs(models.Model):
    maharashtra_id    = models.AutoField(primary_key=True)
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
        return "Maharashtra Govt Jobs"

class ManipurGovtJobs(models.Model):
    manipur_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Manipur Govt Jobs"

class MeghalayaGovtJobs(models.Model):
    meghalaya_id   = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Meghalaya Govt Jobs"

class MizoramGovtJobs(models.Model):
    mizoram_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Mizoram Govt Jobs"

class NagalandGovtJobs(models.Model):
    nagaland_id       = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Nagaland Govt Jobs"

class PuduchheryGovtJobs(models.Model):
    puduchhery_id     = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Puduchhery Govt Jobs"

class PunjabGovernmentjobs(models.Model):
    punjab_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Govt Jobs"

class RajasthanGovtJobs(models.Model):
    rajasthan_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Rajasthan Govt Jobs"

class SikkimGovtJobs(models.Model):
    sikkim_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Sikkim Govt Jobs"

class TamilGovtJobs(models.Model):
    tamil_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tamil Govt Jobs"

class TelanganaGovtJobs(models.Model):
    telangana_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Telangana Govt Jobs"

class TripuraGovtJobs(models.Model):
    tripura_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tripura Govt Jobs"

class UttarakhandGovtJobs(models.Model):
    uttarakhand_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Uttarakhand Govt Jobs"

class UttarPradeshGovtJobs(models.Model):
    uttar_pradesh_id  = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "UttarPradesh Govt Jobs"

class WestBengalGovtJobs(models.Model):
    west_bengal_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "WestBengal Govt Jobs"


"""
-------------------------------------------------
        @@ MODELS FOR BANK AND OTHER FINANCIAL JOBS @@    ||
-------------------------------------------------
"""

class AllBankJobs(models.Model):
    bankjobs_id       = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    bank_name         = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "All Bank Jobs"


class OtherFinancialJobs(models.Model):
    financialjobs_id  = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Other Financial Jobs"


"""
-------------------------------------------------
        @@ MODELS FOR SATE WISE TEACHING JOBS @@    ||
-------------------------------------------------
"""


class AllIndiaTeachingJobs(models.Model):
    all_india_id      = models.AutoField(primary_key=True)
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
        return "AllIndia Teaching Jobs"

class AndamanNicoborTeachingJobs(models.Model):
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
        return "AndamanNicobor Teaching Jobs"

class AndhraPradeshTeachingJobs(models.Model):
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
        return "AndhraPradesh Teaching Jobs"

class ArunachalPradeshTeachingJobs(models.Model):
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
        return "ArunachalPradesh Teaching Jobs"

class AssamTeachingJobs(models.Model):
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
        return "Assam Teaching Jobs"

class BiharTeachingJobs(models.Model):
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
        return "Bihar Teaching Jobs"

class ChandigarhTeachingJobs(models.Model):
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
        return "Chandigarh Teaching Jobs"

class ChhattisgarhTeachingJobs(models.Model):
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
        return "Chhattisgarh Teaching Jobs"

class DadraNagarHaveliTeachingJobs(models.Model):
    dadra_nagar_haveli_id = models.AutoField(primary_key=True)
    start_date            = models.CharField(max_length=60)
    last_date             = models.CharField(max_length=60)
    post_name             = models.CharField(max_length=255)
    education             = models.CharField(max_length=255)
    more_info             = models.TextField()
    requirement_board     = models.CharField(max_length=255)
    type                  = models.IntegerField()
    job_id                = models.IntegerField(default=None,blank=True,null=True)
    join_id               = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DadraNagarHavelis Teaching Jobs"

class DamanDiuTeachingJobs(models.Model):
    DamanDiuTeachingJobs      = models.AutoField(primary_key=True)
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
        return "DamanDiu Teaching Jobs"

class DelhiTeachingJobs(models.Model):
    delhi_id         = models.AutoField(primary_key=True)
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
        return "Delhi Teaching Jobs"

class GoaTeachingJobs(models.Model):
    goa_id            = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Goa Teaching Jobs"

class GujuratTeachingJobs(models.Model):
    gujurat_id        = models.AutoField(primary_key=True)
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
        return "Gujurat Teaching Jobs"

class HaryanaTeachingJobs(models.Model):
    haryana_id          = models.AutoField(primary_key=True)
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
        return "Haryana Teaching Jobs"

class HimachalPradeshTeachingJobs(models.Model):
    himachal_id       = models.AutoField(primary_key=True)
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
        return "HimachalPradesh Teaching Jobs"

class JammuKashmirTeachingJobs(models.Model):
    jammu_kashmir_id  = models.AutoField(primary_key=True)
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
        return "JammuKashmir Teaching Jobs"

class JharkhandTeachingJobs(models.Model):
    jharkhand_id      = models.AutoField(primary_key=True)
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
        return "Jharkhand Teaching Jobs"

class KarnatakaTeachingJobs(models.Model):
    karnataka_id      = models.AutoField(primary_key=True)
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
        return "karnataka Teaching Jobs"

class KeralaTeachingJobs(models.Model):
    kerala_id         = models.AutoField(primary_key=True)
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
        return "Kerala Teaching Jobs"

class LakshadweepTeachingJobs(models.Model):
    lakshadweep_id    = models.AutoField(primary_key=True)
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
        return "Lakshadweep Teaching Jobs"

class MadhyaPradeshTeachingJobs(models.Model):
    madhya_pradesh_id = models.AutoField(primary_key=True)
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
        return "MadhyaPradesh Teaching Jobs"

class MaharashtraTeachingJobs(models.Model):
    maharashtra_id    = models.AutoField(primary_key=True)
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
        return "Maharashtra Teaching Jobs"

class ManipurTeachingJobs(models.Model):
    manipur_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Manipur Teaching Jobs"

class MeghalayaTeachingJobs(models.Model):
    meghalaya_id   = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Meghalaya Teaching Jobs"

class MizoramTeachingJobs(models.Model):
    mizoram_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Mizoram Teaching Jobs"

class NagalandTeachingJobs(models.Model):
    nagaland_id       = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Nagaland Teaching Jobs"

class OdishaTeachingJobs(models.Model):
    odisha_id     = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Puduchhery Teaching Jobs"

class PuduchheryTeachingJobs(models.Model):
    puduchhery_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Teaching Jobs"

class PunjabTeachingJobs(models.Model):
    punjab_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Teaching Jobs"

class RajasthanTeachingJobs(models.Model):
    rajasthan_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Rajasthan Teaching Jobs"

class SikkimTeachingJobs(models.Model):
    sikkim_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Sikkim Teaching Jobs"

class TamilNaduTeachingJobs(models.Model):
    tamil_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tamil Teaching Jobs"

class TelanganaTeachingJobs(models.Model):
    telangana_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Telangana Teaching Jobs"

class TripuraTeachingJobs(models.Model):
    tripura_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tripura Teaching Jobs"

class UttarakhandTeachingJobs(models.Model):
    uttarakhand_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Uttarakhand Teaching Jobs"

class UttarPradeshTeachingJobs(models.Model):
    uttar_pradesh_id  = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "UttarPradesh Teaching Jobs"

class WestBengalTeachingJobs(models.Model):
    west_bengal_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "WestBengal Teaching Jobs"


"""
-------------------------------------------------
        @@ MODELS FOR SATE WISE ENGINEERING JOBS @@    ||
-------------------------------------------------
"""


class AllIndiaEnggJobs(models.Model):
    all_india_id      = models.AutoField(primary_key=True)
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
        return "AllIndia Engg Jobs"


class AllIndiaFellowEnggJobs(models.Model):
    all_india_fellow_id      = models.AutoField(primary_key=True)
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
        return "AllIndia Fellow Engg Jobs"

class AndamanNicoborEnggJobs(models.Model):
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
        return "AndamanNicobor Engg Jobs"

class AndhraPradeshEnggJobs(models.Model):
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
        return "AndhraPradesh Engg Jobs"

class ArunachalPradeshEnggJobs(models.Model):
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
        return "ArunachalPradesh Engg Jobs"

class AssamEnggJobs(models.Model):
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
        return "Assam Engg Jobs"

class BiharEnggJobs(models.Model):
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
        return "Bihar Engg Jobs"

class ChandigarhEnggJobs(models.Model):
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
        return "Chandigarh Engg Jobs"

class ChhattisgarhEnggJobs(models.Model):
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
        return "Chhattisgarh Engg Jobs"

class DadraNagarHaveliEnggJobs(models.Model):
    dadra_nagar_haveli_id = models.AutoField(primary_key=True)
    start_date            = models.CharField(max_length=60)
    last_date             = models.CharField(max_length=60)
    post_name             = models.CharField(max_length=255)
    education             = models.CharField(max_length=255)
    more_info             = models.TextField()
    requirement_board     = models.CharField(max_length=255)
    type                  = models.IntegerField()
    job_id                = models.IntegerField(default=None,blank=True,null=True)
    join_id               = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "DadraNagarHavelis Engg Jobs"

class DamanDiuEnggJobs(models.Model):
    DamanDiuEnggJobs      = models.AutoField(primary_key=True)
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
        return "DamanDiu Engg Jobs"

class DelhiEnggJobs(models.Model):
    delhi_id         = models.AutoField(primary_key=True)
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
        return "Delhi Engg Jobs"

class GoaEnggJobs(models.Model):
    goa_id            = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Goa Engg Jobs"

class GujuratEnggJobs(models.Model):
    gujurat_id        = models.AutoField(primary_key=True)
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
        return "Gujurat Engg Jobs"

class HaryanaEnggJobs(models.Model):
    haryana_id          = models.AutoField(primary_key=True)
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
        return "Haryana Engg Jobs"

class HimachalPradeshEnggJobs(models.Model):
    himachal_id       = models.AutoField(primary_key=True)
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
        return "HimachalPradesh Engg Jobs"

class JammuKashmirEnggJobs(models.Model):
    jammu_kashmir_id  = models.AutoField(primary_key=True)
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
        return "JammuKashmir Engg Jobs"

class JharkhandEnggJobs(models.Model):
    jharkhand_id      = models.AutoField(primary_key=True)
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
        return "Jharkhand Engg Jobs"

class KarnatakaEnggJobs(models.Model):
    karnataka_id      = models.AutoField(primary_key=True)
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
        return "karnataka Engg Jobs"

class KeralaEnggJobs(models.Model):
    kerala_id         = models.AutoField(primary_key=True)
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
        return "Kerala Engg Jobs"

class LakshadweepEnggJobs(models.Model):
    lakshadweep_id    = models.AutoField(primary_key=True)
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
        return "Lakshadweep Engg Jobs"

class MadhyaPradeshEnggJobs(models.Model):
    madhya_pradesh_id = models.AutoField(primary_key=True)
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
        return "MadhyaPradesh Engg Jobs"

class MaharashtraEnggJobs(models.Model):
    maharashtra_id    = models.AutoField(primary_key=True)
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
        return "Maharashtra Engg Jobs"

class ManipurEnggJobs(models.Model):
    manipur_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Manipur Engg Jobs"

class MeghalayaEnggJobs(models.Model):
    meghalaya_id   = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Meghalaya Engg Jobs"

class MizoramEnggJobs(models.Model):
    mizoram_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Mizoram Engg Jobs"

class NagalandEnggJobs(models.Model):
    nagaland_id       = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Nagaland Engg Jobs"

class OdishaEnggJobs(models.Model):
    odisha_id     = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Puduchhery Engg Jobs"

class PuduchheryEnggJobs(models.Model):
    puduchhery_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Engg Jobs"

class PunjabEnggJobs(models.Model):
    punjab_id         = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Punjab Engg Jobs"

class RajasthanEnggJobs(models.Model):
    rajasthan_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Rajasthan Engg Jobs"

class SikkimEnggJobs(models.Model):
    sikkim_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Sikkim Engg Jobs"

class TamilNaduEnggJobs(models.Model):
    tamil_id          = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tamil Engg Jobs"

class TelanganaEnggJobs(models.Model):
    telangana_id      = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Telangana Engg Jobs"

class TripuraEnggJobs(models.Model):
    tripura_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Tripura Engg Jobs"

class UttarakhandEnggJobs(models.Model):
    uttarakhand_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Uttarakhand Engg Jobs"

class UttarPradeshEnggJobs(models.Model):
    uttar_pradesh_id  = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "UttarPradesh Engg Jobs"

class WestBengalEnggJobs(models.Model):
    west_bengal_id    = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "WestBengal Engg Jobs"


"""
-------------------------------------------------
        @@ MODELS FOR RAILWAY JOBS @@    ||
-------------------------------------------------
"""


class RailwayJob(models.Model):
    railway_id        = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Railway Jobs Jobs"


"""
-------------------------------------------------
        @@ MODELS FOR POLICE AND DEFENCE JOBS @@    ||
-------------------------------------------------
"""

class StatewisePoliceJobs(models.Model):
    statewise_police_id = models.AutoField(primary_key=True)
    start_date          = models.CharField(max_length=60)
    last_date           = models.CharField(max_length=60)
    post_name           = models.CharField(max_length=255)
    education           = models.CharField(max_length=255)
    more_info           = models.TextField()
    requirement_board   = models.CharField(max_length=255)
    type                = models.IntegerField()
    job_id              = models.IntegerField(default=None,blank=True,null=True)
    join_id             = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Statewise Police Jobs"

class PoliceAndDefenceJobs(models.Model):
    police_defence_id = models.AutoField(primary_key=True)
    start_date        = models.CharField(max_length=60)
    last_date         = models.CharField(max_length=60)
    post_name         = models.CharField(max_length=255)
    education         = models.CharField(max_length=255)
    more_info         = models.TextField()
    requirement_board = models.CharField(max_length=255)
    type              = models.IntegerField()
    job_id            = models.IntegerField(default=None,blank=True,null=True)
    join_id           = models.IntegerField(default=None,blank=True,null=True)

    def __str__(self):
        return "Police Defence Jobs"
