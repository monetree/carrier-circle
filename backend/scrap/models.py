
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
